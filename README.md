# Internal_Product_Management
# Internal Product Management Tool for eCommerce

This project is an internal tool to manage the product catalog of an eCommerce platform.  
It allows internal users (merchandisers, category managers) to manage categories, attributes, and products dynamically.

---

## 📂 Repository Structure

ecommerce-pim-tool/
│
├── backend/
│ ├── app.py # Main Flask app
│ ├── models.py # SQLAlchemy ORM models
│ ├── seed.py # Database seeding script
│ ├── requirements.txt # Python dependencies
│ └── init.py # Package initializer
│
├── docs/
│ ├── ERD.png # Database ERD diagram
│ └── ClassDiagram.png # Class diagram
│
├── README.md # Project documentation
└── .gitignore # Ignore venv, pycache, etc.

yaml
Copy
Edit

---

## ⚡ Features

- *Category Management:* Create and view product categories.
- *Attribute Management:* Define attributes per category (e.g., size, color, RAM).
- *Product Management:* Add products with category-specific attributes.
- *Dynamic & Scalable:* Easily extend to new product categories.
- *Database Integrity:* Enforces data consistency using SQLAlchemy ORM.

---

## 📊 Database Design

- *ERD (Entity Relationship Diagram):* docs/ERD.png
- Relational database schema supports:
  - Dynamic product categories
  - Custom attributes per category
  - Product creation and updates

---

## 🧩 Class Design

- *Class Diagram:* docs/ClassDiagram.png
- Highlights:
  - Category, Attribute, Product classes
  - Relationships between classes
  - Key methods for CRUD operations

---

## 🛠 Tech Stack

- Python 3
- Flask
- Flask-SQLAlchemy
- SQLite (can be replaced with other DBs)
- Flask-CORS

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone <your-github-repo-url>
cd ecommerce-pim-tool/backend
2. Create a virtual environment and install dependencies
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate    # Windows
source venv/bin/activate # macOS/Linux
pip install -r requirements.txt
3. Run the Flask backend
bash
Copy
Edit
python app.py
Backend will run at: http://127.0.0.1:5000

4. Seed the database (initial data)
bash
Copy
Edit
python seed.py
🔗 API Endpoints
Action Method URL Body Example
List Categories GET /categories -
Create Category POST /categories {"name": "Watches"}
List Attributes GET /attributes -
Create Attribute POST /attributes {"name": "Size", "data_type": "string"}
List Products GET /products -
Create Product POST /products {"name": "Summer Dress", "sku": "SKU123", "category_id": 1, "price": 1200}
Ping Backend GET /ping -

✅ Testing the API
Use Postman or cURL to test endpoints.

Example: GET Categories

bash
Copy
Edit
GET http://127.0.0.1:5000/categories
Example: POST Category

json
Copy
Edit
POST http://127.0.0.1:5000/categories
{
  "name": "Watches"
}
📄 Notes
Add new categories and attributes before creating products.

Ensure sku is unique for products.

You can expand to other product categories easily without changing the database structure.

📸 Diagrams
ERD: docs/ERD.png

Class Diagram: docs/ClassDiagram.png
