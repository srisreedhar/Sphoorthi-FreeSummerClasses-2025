/*

CUSTOMER                       PRODUCT
+---------------+             +---------------+
| CUSTOMER_ID   |◄──┐         | PRODUCT_ID    |◄──┐
| FIRST_NAME    |   │         | PRODUCT_NAME  |   │
| LAST_NAME     |   │         | STANDARD_COST |   │
| MIDDLE_NAME   |   │         | COLOR         |   │
| ADDRESS_LINE1 |   │         | LIST_PRICE    |   │
| ADDRESS_LINE2 |   │         | PRODUCT_SIZE  |   │
| CITY          |   │         | WEIGHT        |   │
| COUNTRY       |   │         | PRODUCT_CAT.. |   │
| DATE_ADDED    |   │         +---------------+   │
| REGION        |   │                           │
+---------------+   │                           │
                    │                           │
SALESPERSON         │                           │
+---------------+   │                           │
| SALESPERSON_ID|◄──┤                           │
| JOB_TITLE     |   │                           │
| FIRST_NAME    |   │                           │
| LAST_NAME     |   │                           │
| MIDDLE_NAME   |   │                           │
| ADDRESS_LINE1 |   │                           │
| ADDRESS_LINE2 |   │                           │
| CITY          |   │                           │
| COUNTRY       |   │                           │
| DATE_ADDED    |   │                           │
| MANAGER       |   │                           │
+---------------+   │                           │
                    │                           │
SALES               │                           │
+---------------+   │                           │
| SALES_DATE    |   │                           │
| ORDER_ID      |◄──┼───────────────┐           │
| PRODUCT_ID    |───┘               │           │
| CUSTOMER_ID   |───────────────────┘           │
| SALESPERSON_ID|-------------------------------┘
| QUANTITY      |
| UNIT_PRICE    |
| SALES_AMOUNT  |
| TAX_AMOUNT    |
| TOTAL_AMOUNT  |
+---------------+

SALES_HISTORY
+---------------+
| SALES_DATE    |
| ORDER_ID      |◄──┬───────────────┐
| PRODUCT_ID    |───┘               │
| CUSTOMER_ID   |───────────────────┘
| SALESPERSON_ID|-------------------------------┐
| QUANTITY      |                               │
| UNIT_PRICE    |                               │
| SALES_AMOUNT  |                               │
| TAX_AMOUNT    |                               │
| TOTAL_AMOUNT  |                               │
+---------------+                               │
                                               │
                                               ▼
                                        (References same tables)




*/
