from flask import Blueprint, request, jsonify
from models import db, Category, Attribute, CategoryAttribute, Product, ProductAttributeValue
import json

api = Blueprint('api', __name__)

# ---- Category CRUD ----
@api.post('/categories')
def create_category():
    data = request.get_json()
    name = data.get('name')
    if not name:
        return jsonify(error='name is required'), 400
    c = Category(name=name)
    db.session.add(c)
    db.session.commit()
    return jsonify(id=c.id, name=c.name), 201

@api.get('/categories')
def list_categories():
    items = Category.query.all()
    return jsonify([{'id': c.id, 'name': c.name} for c in items])

@api.post('/categories/<int:category_id>/attributes')
def assign_attribute(category_id):
    data = request.get_json()
    attribute_id = data.get('attribute_id')
    is_required = bool(data.get('is_required', False))
    is_visible = bool(data.get('is_visible', True))
    sort_order = int(data.get('sort_order', 0))

    if not attribute_id:
        return jsonify(error='attribute_id is required'), 400

    ca = CategoryAttribute(category_id=category_id, attribute_id=attribute_id,
                           is_required=is_required, is_visible=is_visible, sort_order=sort_order)
    db.session.add(ca)
    db.session.commit()
    return jsonify(id=ca.id), 201

# ---- Attribute CRUD ----
@api.post('/attributes')
def create_attribute():
    data = request.get_json()
    name = data.get('name')
    data_type = data.get('data_type')
    allowed_values = data.get('allowed_values')
    if not (name and data_type):
        return jsonify(error='name and data_type are required'), 400
    a = Attribute(name=name, data_type=data_type,
                  allowed_values=json.dumps(allowed_values) if allowed_values else None)
    db.session.add(a)
    db.session.commit()
    return jsonify(id=a.id, name=a.name, data_type=a.data_type), 201

@api.get('/attributes')
def list_attributes():
    items = Attribute.query.all()
    def parse_allowed(a):
        try:
            return json.loads(a.allowed_values) if a.allowed_values else None
        except Exception:
            return None
    return jsonify([{'id': a.id, 'name': a.name, 'data_type': a.data_type, 'allowed_values': parse_allowed(a)} for a in items])

# ---- Product CRUD ----
@api.post('/products')
def create_product():
    data = request.get_json()
    required = ['name', 'sku', 'category_id', 'price']
    if not all(k in data for k in required):
        return jsonify(error=f"Required fields: {', '.join(required)}"), 400

    p = Product(name=data['name'], sku=data['sku'], category_id=data['category_id'], price=data['price'])
    db.session.add(p)
    db.session.flush()  # get p.id before committing

    # Accept attribute_values: [{"attribute_id":1,"value":"128GB"}, ...]
    for av in data.get('attribute_values', []):
        pav = ProductAttributeValue(product_id=p.id, attribute_id=av['attribute_id'], value=str(av.get('value')))
        db.session.add(pav)

    db.session.commit()
    return jsonify(id=p.id), 201

@api.get('/products')
def list_products():
    category_id = request.args.get('category_id', type=int)
    q = Product.query
    if category_id:
        q = q.filter_by(category_id=category_id)
    items = q.all()

    def av_map(p):
        out = []
        for av in p.attribute_values:
            out.append({'attribute_id': av.attribute_id, 'attribute_name': av.attribute.name, 'value': av.value})
        return out

    return jsonify([{
        'id': p.id,
        'name': p.name,
        'sku': p.sku,
        'category_id': p.category_id,
        'price': float(p.price),
        'status': p.status,
        'attribute_values': av_map(p)
    } for p in items])

@api.patch('/products/<int:product_id>')
def update_product(product_id):
    p = Product.query.get_or_404(product_id)
    data = request.get_json()
    for field in ['name', 'sku', 'category_id', 'price', 'status']:
        if field in data:
            setattr(p, field, data[field])
    db.session.commit()
    return jsonify(message='updated')

@api.post('/products/<int:product_id>/attributes')
def upsert_product_attribute(product_id):
    p = Product.query.get_or_404(product_id)
    data = request.get_json()
    attribute_id = data.get('attribute_id')
    value = data.get('value')
    if attribute_id is None:
        return jsonify(error='attribute_id is required'), 400
    pav = ProductAttributeValue.query.filter_by(product_id=p.id, attribute_id=attribute_id).first()
    if pav:
        pav.value = str(value)
    else:
        pav = ProductAttributeValue(product_id=p.id, attribute_id=attribute_id, value=str(value))
        db.session.add(pav)
    db.session.commit()
    return jsonify(message='ok')