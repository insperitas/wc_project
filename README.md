WindowCleanr — Online Window Cleaning Marketplace
=================================================

Project overview
----------------
WindowCleanr connects customers who need domestic window cleaning with local freelance cleaners. Customers sign up, provide an address and basic house details; cleaners submit quotes via a cleaners' webapp. All payments are taken through the site in advance. The platform supports area-based matching, waiting lists for uncovered areas, ratings, and secure payments.

Primary goals
-------------
- Allow customers to: sign up, enter address + house style/size, request service, pay online, and rate cleaners.
- Allow cleaners to: register, claim availability for areas, submit quotes, view bookings and receive payments.
- Admin/ops: manage areas, monitor bookings, handle payouts, and resolve disputes.

Key user flows
--------------
1. Customer signs up and provides address + house details.
2. System checks for active cleaners in the customer's area.
   - If no cleaner: place customer on waitlist and optionally collect contact permission.
   - If cleaner available: notify cleaner(s) or route request to assigned cleaner.
3. Cleaner responds with a quoted price via their webapp.
4. Customer approves and pays online. Payment held until job completion (or instant payout model).
5. Cleaner performs job; customer rates the cleaner afterwards.

Core features / modules
-----------------------
- Authentication & user profiles (customers, cleaners, admins)
- Geo/area management and matching
- Cleaner webapp (quotes, schedules, earnings)
- Customer booking flow & payments
- Ratings & reviews
- Notifications (email/SMS/push)
- Admin dashboard & reporting

Suggested tech stack (initial)
------------------------------
- Backend: Python (FastAPI) or Node.js (Nest/Express)
- Database: PostgreSQL (PostGIS optional for geo)
- Payments: Stripe (recommended) for card processing and marketplace payouts
- Frontend: React (Customer) + React Native or React (Cleaner) webapp
- Hosting: Vercel/Netlify (frontend), AWS/GCP/Azure for backend and DB

Security & compliance
---------------------
- Use Stripe to manage PCI compliance for payments.
- Store minimal PII; encrypt sensitive fields at rest.
- Implement email verification, rate-limiting, and monitoring for fraud.

Progress so far
--------------
- Initial project concept, user flows and feature list drafted (this repo).
- No code or infrastructure created yet — next step is scaffolding.

Immediate next steps
--------------------
1. Agree tech stack and deployment targets.
2. Produce high-level architecture diagram and API surface.
3. Create data model (users, areas, bookings, quotes, payments, ratings).
4. Scaffold repo with basic auth and a placeholder API endpoint.

How to use this file
---------------------
This README is intended for new contributors and for AI agents to quickly understand project goals and status. Update the "Progress so far" section as work completes.

Contact / ownership
-------------------
Project owner: (add owner name and contact)
