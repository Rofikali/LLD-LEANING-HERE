# Architecture Decisions

ADR-001

Decision:
Use PostgreSQL

Reason:
ACID transactions

Tradeoff:
Horizontal scaling harder

------------------------------------------------

ADR-002

Decision:
Journal entries immutable

Reason:
Auditability

Tradeoff:
Requires reversal entries

------------------------------------------------

ADR-003

Decision:
Use Repository Pattern

Reason:
Database independence