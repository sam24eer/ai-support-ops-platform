\# Incident Postmortem



\## Summary

An increase in incorrectly auto-resolved refund-related tickets was observed due to

overconfidence in the intent classification logic. Several tickets that required

human review were auto-resolved, leading to delayed issue resolution.



\## Impact

\- Affected Users: ~12 customers

\- Duration: ~45 minutes

\- Impact Type: Incorrect ticket handling and delayed support response

\- Business Impact: Reduced customer satisfaction and increased follow-up workload for agents



\## Detection

The issue was detected through a spike in the `ticket\_auto\_resolved` metric combined

with an abnormal drop in manual escalations for refund-related intents.



\## Root Cause

The intent classifier returned moderate confidence scores for refund-related queries,

but the decision engine confidence threshold was set too low for this intent.

As a result, tickets that should have been escalated were auto-resolved.



\## Resolution

The decision engine was updated to temporarily escalate all refund-related tickets

regardless of confidence score. The service was restarted to apply the change,

and affected tickets were manually reviewed by support agents.



\## Prevention

\- Introduce intent-specific confidence thresholds

\- Add alerts for sudden changes in auto-resolution or escalation rates

\- Require manual review for high-risk intents such as billing and refunds

\- Include pre-deployment validation checks for decision logic changes



\## Learnings

\- AI confidence scores must be interpreted in context, not used globally

\- Business rules are essential safeguards around AI predictions

\- Metrics and observability enable early detection of systemic issues

\- High-risk customer intents should default to conservative handling



\## Action Items

\- \[ ] Implement intent-specific thresholds in the decision engine

\- \[ ] Add escalation-rate anomaly alerts

\- \[ ] Document high-risk intents in SOP

\- \[ ] Review AI decision logic weekly during MVP phase



