# MVP Scope Definition



## 1. MVP Overview



The MVP delivers a text-based AI customer support system capable of

ingesting web-based inquiries, classifying customer intent, automatically

resolving low-risk requests, and routing complex or uncertain issues to a

basic human agent dashboard.



The MVP prioritizes correctness, observability, and operational control

over feature breadth or automation depth.



---



## 2. In-Scope Features (MVP)



- Web-based support widget (text form)

- Centralized ticket creation and status tracking

- AI-based intent classification with confidence scoring

- Auto-resolution for predefined “safe” intents using deterministic

&nbsp; responses

- Human handoff and routing for low-confidence or high-risk tickets

- Basic agent dashboard for review and resolution

- SLA timer tracking and breach detection

- Full end-to-end event logging



---



## 3. Out-of-Scope Features (Post-MVP)



- Voice or phone-based support

- Multilingual support

- Real-time live chat

- CRM-driven personalization

- Transactional workflows (refunds, payments, account changes)

- Proactive outbound messaging

- Advanced sentiment analysis

- Automated model retraining pipelines



---



## 4. Build vs Mock Matrix



| Component              | Status | Notes |

|------------------------|--------|-------|

| Web Intake UI          | Build  | Simple React-based form |

| Ingestion API          | Build  | REST endpoint for ticket creation |

| Intent Classification | Build  | LLM / classifier with confidence score |

| Auto-Resolution Rules | Build  | Hard-coded safe intent mappings |

| Decision Engine        | Build  | Threshold-based routing logic |

| Agent Dashboard        | Build  | Minimal UI for review and resolution |

| SLA Timer Engine       | Build  | Timestamp-based enforcement |

| User History / CRM     | Mock   | Static JSON payload |

| Payment Gateway        | Mock   | Simulated sandbox responses |

| Sentiment Analysis     | Mock   | Placeholder score injection |

| Real-Time Chat         | Defer  | Explicitly excluded |

| Voice Support          | Defer  | Explicitly excluded |



---



## 5. Logging Plan (Day-One)



The following events are logged from MVP launch:



- Ticket created

- Ticket updated

- Ticket resolved

- Ticket escalated

- AI intent prediction generated

- Confidence score recorded

- Decision outcome (auto-resolve vs escalate)

- Human agent action

- SLA warning triggered

- SLA breach triggered

- Error or exception events

- Model version used

- Decision rule identifier applied



All logs include timestamps and correlation IDs to support traceability,

debugging, and metric computation.



---



## 6. Data Schemas (High-Level)



### Tickets

Fields:

- ticket_id

- user_id

- channel

- raw_text

- status

- priority

- created_timestamp

- resolved_timestamp



---



### Predictions

Fields:

- prediction_id

- ticket_id

- model_version

- predicted_intent

- confidence_score

- prediction_timestamp



---



### Decisions

Fields:

- decision_id

- ticket_id

- decision_type (auto_resolve / escalate)

- rule_applied

- decision_timestamp



---



### Overrides

Fields:

- override_id

- ticket_id

- ai_predicted_label

- human_final_label

- agent_id

- override_reason

- override_timestamp



---



### Metrics Snapshots

Fields:

- snapshot_id

- metric_name

- metric_value

- time_window

- computed_timestamp



---



## 7. Metrics Activation Plan



### Live in MVP



- Traffic volume

- First Response Time (FRT)

- Time to Resolution (TTR)

- Escalation Rate

- Automation Resolution Rate (Deflection)

- SLA breach rate

- AI confidence distribution

- Human override rate



---



### Post-MVP



- Customer Satisfaction Proxy (CSAT)

- Cost per Ticket

- Retention Delta

- Model drift score

- Advanced sentiment analysis



