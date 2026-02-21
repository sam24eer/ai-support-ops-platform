# AI Customer Support Operations Platform



## Overview

An AI-powered support operations platform designed to ingest customer inquiries,

classify intent, make safe automation decisions, and provide full operational

visibility for support teams.



## Problem

Small and mid-sized businesses struggle with slow, manual support workflows,

leading to poor response times, high costs, and customer churn.



## Solution

This platform introduces:

* Structured ticket intake
* AI-based intent classification
* Confidence-based decision engine
* Automated vs human escalation logic
* End-to-end observability and metrics



## Architecture

* FastAPI backend
* Modular services (classification, decision engine, metrics)
* Clear separation between AI predictions and business rules



## Key Features

* Ticket ingestion API
* Intent classification with confidence scoring
* Rule-based auto-resolution vs escalation
* Metrics and event tracking
* Operational documentation and runbooks



## Metrics Tracked

* Ticket volume
* Auto-resolution rate
* Escalation rate
* Decision audit trail



## Project Status

* Week 1: Problem definition and system design ✅
* Week 2: Backend, AI logic, metrics, and ops documentation ✅
* Week 3: User interface, ticket history, ops view, and Dockerization ✅



## Future Improvements

* Persist tickets and metrics using SQLite or PostgreSQL
* Add authentication for Ops UI
* Backend filtering and pagination for ticket history
* Alerts for SLA breaches and escalation spikes
* Replace classifier stub with trained ML or LLM-based model



# Case Study



## Context

Support teams often adopt AI tools without sufficient controls, leading to

misclassification, poor customer experience, and lack of trust.



## Approach

The system was designed with an ops-first mindset:

* AI provides predictions, not decisions
* Business rules control automation
* All decisions are logged and measurable
* Failure scenarios are documented upfront



## Outcome

The resulting platform demonstrates how AI can safely reduce support workload

while maintaining accountability and observability.



## Key Learnings

* AI confidence must be treated as an input, not authority
* Metrics are essential for trust in automation
* Operational readiness is as important as model accuracy



## User Interface (New)



To improve usability and enable realistic testing, a lightweight web-based UI was added.



#### End-User UI



Allows users to submit support tickets via a simple form



Eliminates the need to manually craft JSON requests in API docs



Intended for testers and non-technical users



#### Ops / Admin UI



Dedicated page for viewing ticket history



Search tickets by user name



Provides operational visibility without exposing data to end users



This separation mirrors real-world systems where customer-facing interfaces and internal ops tools are distinct.



#### Ticket History \& Search



All tickets created during a session are stored in memory



Ops users can view all tickets in a single dashboard



Search functionality enables quick lookup by user name



Designed for testing and analysis during the MVP phase



Note:

Ticket history is intentionally in-memory and resets on service restart.

Persistence is planned as a future improvement.



## Docker Support (New)



The entire application is fully Dockerized to simplify setup and ensure consistent execution across environments.



What Docker Enables



One-command startup



No local Python or virtual environment required



Backend API and UI served together



Identical behavior for all users



#### Run with Docker



docker-compose up --build



#### Access Points

* Ticket UI: http://localhost:8000/ui
* Ops UI: http://localhost:8000/ops
* API Docs: http://localhost:8000/docs
* Metrics: http://localhost:8000/metrics
* Health Check: http://localhost:8000/health



Docker support makes the project easier to evaluate, demo, and share.



## Design Decisions (Interview Notes)



#### Why separate AI and decision logic?

To prevent AI from directly triggering irreversible actions and to

allow business rules to control risk and accountability.



#### Why metrics before dashboards?

Metrics ensure correctness first; visualization can be layered later.



#### Why stubbed AI?

The project focuses on AI Ops architecture rather than model training.

Replacing the classifier does not affect system design.



## Summary



This project now demonstrates not only safe AI automation and observability, but also:



Realistic user interaction



Operational visibility



Deployment readiness



Clear separation of concerns between users and operators



The system is intentionally scoped as an MVP, with architectural decisions that support future scaling without redesign.

