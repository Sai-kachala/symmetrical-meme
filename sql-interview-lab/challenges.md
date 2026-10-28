# SQL Interview Challenges

Use the schema and seed data in this folder. Solve in order and briefly explain why each query returns the correct rows.

## Level 1 — Filtering and sorting
1. List employees earning more than 70,000, highest salary first.
2. Find employees hired on or after 2023-01-01.
3. Show the five most expensive products.
4. List distinct customer cities alphabetically.
5. Find products with zero stock.

## Level 2 — Aggregation
6. Count employees in each department, showing the department name.
7. Show departments whose average salary is above 75,000.
8. Count orders by status.
9. Find the average product price for each category.
10. Show categories containing at least two products.

## Level 3 — Joins
11. Show every employee with their department; keep employees who have no department.
12. List each order with customer name and order date.
13. Show each order line with product name, quantity, and line total.
14. Find customers who have never placed an order.
15. Find products that have never appeared in order items.

## Level 4 — Subqueries
16. Find employees earning more than the company-wide average salary.
17. Find employees earning more than the average salary in their own department.
18. Find products priced above the average price of their category.
19. Find customers who placed at least one order using IN or EXISTS.
20. Find customers who placed no orders using NOT EXISTS.

## Level 5 — Multi-row and correlated logic
21. Find employees whose salary matches the highest salary in any department.
22. Find employees earning more than every employee in HR. Consider an empty HR department.
23. Find departments with at least one employee earning above 80,000.
24. Find customers who ordered an Electronics product.
25. Find orders whose total is above the average order total; state how cancelled orders are handled.

## Level 6 — Business logic
26. Calculate paid/shipped revenue by customer using the purchase-time price, not current product price.
27. Rank employees by salary within each department using a window function.
28. Return each customer's most recent order. Explain how ties are handled.
29. Calculate each product's percentage contribution to non-cancelled order value.
30. Find customers whose spending is above average customer spending. State how customers with no qualifying orders are handled.

## Interview checklist
- Explain WHERE vs HAVING.
- Explain join cardinality and duplicate parent rows.
- Explain IN vs EXISTS and the NULL risk with NOT IN.
- Explain scalar vs multi-row subqueries.
- State assumptions for NULL, cancelled, and pending orders.
- Test edge cases, not only the seed data.
