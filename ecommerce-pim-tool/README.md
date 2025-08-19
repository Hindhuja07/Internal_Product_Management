# Internal Product Management Tool (Interview Assignment)

This repository contains:
- **Step 1 (ERD)**: `docs/ERD.png` (or `docs/ERD.dot` if Graphviz was unavailable)
- **Step 2 (Class Diagram)**: `docs/ClassDiagram.png` (or `docs/ClassDiagram.dot` fallback)
- **Step 3 (Implementation)**: Minimal Flask + SQLAlchemy backend with CRUD for Categories, Attributes, and Products.

## Quick Start

```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

API will run at `http://127.0.0.1:5000`

### Sample Calls (HTTP)
- Create Category: `POST /api/categories` body: `{ "name": "Smartphones" }`
- Create Attribute: `POST /api/attributes` body: `{ "name": "RAM", "data_type": "string" }`
- Assign Attribute to Category: `POST /api/categories/{category_id}/attributes` body: `{ "attribute_id": 1, "is_required": true }`
- Create Product with attributes: `POST /api/products` body:
```json
{
  "name": "Pixel 8",
  "sku": "PIX-8-128",
  "category_id": 1,
  "price": 699.00,
  "attribute_values": [
    {"attribute_id": 1, "value": "Android"},
    {"attribute_id": 2, "value": "8GB"},
    {"attribute_id": 3, "value": "4575 mAh"}
  ]
}
```

## Tech Stack
- Flask, SQLAlchemy, SQLite (for simplicity)
- Clean, normalized schema supporting dynamic categories & attributes

## Notes
- Attribute values stored as text; validated in business layer based on `data_type` (can be extended).
- Adding new categories or attributes requires **no schema changes**.