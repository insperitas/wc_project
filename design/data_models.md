Data models — WindowCleanr
==========================

Overview
--------
This document defines core relational data models for the WindowCleanr platform. Use PostgreSQL (PostGIS optional) as the primary store.

Entities
--------

- `users`
  - `id` (uuid, PK)
  - `email` (varchar, unique, indexed)
  - `password_hash` (varchar) — store salted hash
  - `role` (enum: customer, cleaner, admin)
  - `is_active` (bool)
  - `created_at`, `updated_at`

- `profiles`
  - `user_id` (uuid, PK, FK -> users.id)
  - `first_name`, `last_name`
  - `phone` (varchar)
  - `address_line1`, `address_line2`, `city`, `postcode`, `country`
  - `location` (geometry(Point) or latitude/longitude)
  - `house_style` (enum or varchar) — e.g., terraced/semi/detached
  - `house_size_estimate` (enum: small/med/large) or numeric `num_windows`

- `areas`
  - `id` (uuid, PK)
  - `name` (varchar)
  - `boundary` (geometry(Polygon)) or `geohash`/centroid + radius
  - `is_active` (bool)

- `cleaner_areas` (many-to-many)
  - `id` (uuid, PK)
  - `cleaner_id` (uuid, FK -> users.id)
  - `area_id` (uuid, FK -> areas.id)
  - `status` (enum: available, paused)

- `waitlist`
  - `id` (uuid, PK)
  - `customer_id` (uuid, FK -> users.id)
  - `area_id` (uuid, FK -> areas.id) nullable
  - `address` (text)
  - `requested_at`

- `bookings`
  - `id` (uuid, PK)
  - `customer_id` (uuid, FK -> users.id)
  - `area_id` (uuid, FK -> areas.id)
  - `status` (enum: requested, quoted, paid, scheduled, completed, cancelled)
  - `requested_at`, `scheduled_at` (timestamp)
  - `notes` (text)

- `quotes`
  - `id` (uuid, PK)
  - `booking_id` (uuid, FK -> bookings.id)
  - `cleaner_id` (uuid, FK -> users.id)
  - `amount_cents` (integer)
  - `currency` (varchar)
  - `expires_at` (timestamp)
  - `created_at`

- `payments`
  - `id` (uuid, PK)
  - `booking_id` (uuid, FK)
  - `stripe_payment_intent` (varchar)
  - `amount_cents`, `currency`
  - `status` (enum: pending, succeeded, failed, refunded)
  - `created_at`

- `ratings`
  - `id` (uuid, PK)
  - `booking_id` (uuid, FK)
  - `customer_id` (uuid, FK)
  - `cleaner_id` (uuid, FK)
  - `rating` (smallint 1-5)
  - `review` (text)
  - `created_at`

- `transactions` (platform accounting/payouts)
  - `id` (uuid, PK)
  - `cleaner_id` (uuid, FK)
  - `booking_id` (uuid, FK)
  - `type` (enum: payout, fee, refund)
  - `amount_cents`, `currency`
  - `stripe_transfer_id`
  - `status`

Indexes / Performance
---------------------
- Index `users.email` unique for auth
- GiST index on `profiles.location` or `areas.boundary` for spatial queries
- Index on `cleaner_areas.cleaner_id` and `area_id` for fast matching
- Index `bookings.status, bookings.requested_at` for queueing

Notes / Constraints
-------------------
- Keep PII minimal. Encrypt phone/address fields if required.
- Use `ON DELETE SET NULL` on optional FK relations if appropriate.
- Consider materialized views or denormalized tables for cleaner availability and metrics.

Example ER relationships
------------------------
- `users` 1—1 `profiles`
- `users` (role=cleaner) N—M `areas` via `cleaner_areas`
- `customers` 1—N `bookings`
- `bookings` 1—N `quotes`
- `bookings` 1—1 `payments` (or 1—N for multiple attempts)
- `bookings` 1—1 `ratings` (after completion)
