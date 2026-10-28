# SQL Interview Lab (PostgreSQL)

A practice database built around departments, employees, customers, products, orders, and order items. The related tables let me practise SQL logic against realistic relationships instead of memorizing isolated queries.

## Setup

Create a practice database, then run schema.sql followed by seed.sql.

\`\`\`bash
createdb sql_interview_lab
psql -d sql_interview_lab -f sql-interview-lab/schema.sql
psql -d sql_interview_lab -f sql-interview-lab/seed.sql
\`\`\`

Run the questions in challenges.md using your SQL client.

## Tables

- departments → employees
- customers → orders
- orders → order_items → products

## Topics

Filtering, sorting, pagination, inner and left joins, aggregation, HAVING, correlated and non-correlated subqueries, multi-row subqueries, and NULL logic.

## Practice rules

- Explain what one output row represents.
- Check whether one-to-many joins can duplicate rows.
- Prefer readable aliases and consistent formatting.
- State how NULL values and cancelled or pending orders affect the result.
- Attempt each challenge before looking up a solution.

The seed data is synthetic and intended for learning, not business reporting.
