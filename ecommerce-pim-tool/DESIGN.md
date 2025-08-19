# Design Justification

## Database
- **Normalization**: Attributes are de-duplicated and linked via `CategoryAttribute`. No sparse columns or EAV anti-pattern beyond the controlled `ProductAttributeValue` value store.
- **Flexibility**: New categories/attributes are data entries, not schema migrations.
- **Integrity**: FK constraints; `CategoryAttribute.is_required` and `sort_order` control UI/validation policies.
- **Scalability**: Reads can be optimized with indexes (e.g., `(product_id, attribute_id)`), caching, and pagination.

## Key Tables
- `Category(id, name, ...)`
- `Attribute(id, name, data_type, allowed_values)`
- `CategoryAttribute(category_id, attribute_id, is_required, is_visible, sort_order)`
- `Product(id, name, sku, category_id, price, status, ...)`
- `ProductAttributeValue(product_id, attribute_id, value)`

### Data Types
- `Attribute.data_type`: `string | int | float | bool | enum | date`
- `allowed_values` is JSON when `data_type='enum'`

## Class Design
- `CatalogManager` orchestrates creation and assignment operations.
- `Product` owns `ProductAttributeValue` entries; `Attribute.validate(value)` enforces type/enum checks (extendable).

## Future-Proofing
- Add `Variant` and `Inventory` tables without impacting attribute model.
- Add audit tables for change history if required.
- Move `value` to typed columns (or JSONB) in PostgreSQL if stricter typing is needed.