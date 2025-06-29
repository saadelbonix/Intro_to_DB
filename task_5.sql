echo "INSERT INTO CUSTOMERS (CUSTOMER_ID, CUSTOMER_NAME, EMAIL, ADDRESS)
VALUES (1, 'Cole Baidoo', 'cbaidoo@sandtech.com', '123 Happiness Ave.');" > task_5.sql

git add task_5.sql
git commit -m "Add script to insert row into customers table"
git push origin main
