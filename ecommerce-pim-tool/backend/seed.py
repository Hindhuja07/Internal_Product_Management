from app import db, Category, Attribute, Product
from datetime import datetime

# Use app context
from app import app
with app.app_context():

    # Clear existing data
    db.drop_all()
    db.create_all()

    # --- Categories ---
    dresses = Category(name="Dresses")
    shoes = Category(name="Shoes")
    watches = Category(name="Watches")

    db.session.add_all([dresses, shoes, watches])
    db.session.commit()

    # --- Attributes ---
    attr_size = Attribute(name="Size", data_type="string", category_id=dresses.id)
    attr_color = Attribute(name="Color", data_type="string", category_id=dresses.id)
    attr_material = Attribute(name="Material", data_type="string", category_id=shoes.id)
    attr_dial_color = Attribute(name="Dial Color", data_type="string", category_id=watches.id)
    attr_strap_type = Attribute(name="Strap Type", data_type="string", category_id=watches.id)

    db.session.add_all([attr_size, attr_color, attr_material, attr_dial_color, attr_strap_type])
    db.session.commit()

    # --- Products ---
    dress_product = Product(name="Summer Dress", sku="DRESS001", category_id=dresses.id, price=49.99)
    shoes_product = Product(name="Running Shoes", sku="SHOE001", category_id=shoes.id, price=89.99)
    watch_product = Product(name="Classic Watch", sku="WATCH001", category_id=watches.id, price=199.99)

    db.session.add_all([dress_product, shoes_product, watch_product])
    db.session.commit()

    print("Database seeded successfully! 🚀")
