# Metrics Specification



This document defines the key metrics used to evaluate customer experience,

operational efficiency, AI performance, and business impact. Each metric

includes ownership and an explicit action trigger to enable operational

decision-making.



# A. Customer Experience Metrics



## Metric Name: First Response Time (FRT)



Definition:

Time elapsed between ticket creation and the first meaningful response,

whether automated or human.



Formula:

timestamp\_first\_response - timestamp\_ticket\_created



Data Source:

Helpdesk / CRM system



Owner:

Support Team Lead



Action Trigger:

Trigger alert if average FRT exceeds SLA (e.g., 1 hour) for 2 consecutive hours.




## Metric Name: Time to Resolution (TTR)



Definition:

Total time from ticket creation to final resolution or closure, excluding

time waiting on customer response where applicable.



Formula:

timestamp\_resolved - timestamp\_ticket\_created



Data Source:

Helpdesk / CRM system



Owner:

Support Operations Manager



Action Trigger:

Initiate root-cause review if average TTR increases by more than 10%

week-over-week.




## Metric Name: Escalation Rate



Definition:

Percentage of tickets escalated from AI or Tier 1 support to Tier 2 or Tier 3

specialists.



Formula:

(count\_escalated\_tickets / total\_tickets) \* 100



Data Source:

Helpdesk / CRM system



Owner:

Support Quality Assurance Lead



Action Trigger:

Trigger topic-level investigation if escalation rate exceeds 15% for the same

category for 2 consecutive weeks.




## Metric Name: Customer Satisfaction Proxy (CSAT)



Definition:

Customer satisfaction score derived from post-interaction surveys or sentiment

analysis of conversation logs.



Formula:

Average survey score OR Average(sentiment\_score\_0\_to\_1)



Data Source:

Survey system / Sentiment analysis pipeline



Owner:

Head of Customer Experience



Action Trigger:

Trigger service recovery workflow if any individual score falls below 2 out of 5.





# B. Operational Efficiency Metrics



## Metric Name: Average Handle Time (AHT)



Definition:

Average time an agent actively spends handling a ticket, including interaction

and wrap-up time.



Formula:

sum\_active\_work\_time / total\_tickets\_handled



Data Source:

Helpdesk system / Workforce management logs



Owner:

Support Operations Manager



Action Trigger:

Review workflows if AHT deviates more than 20% from team baseline for 1 week.




## Metric Name: Tickets per Agent



Definition:

Number of tickets resolved by an individual agent within a defined period.



Formula:

count\_resolved\_tickets WHERE agent\_id = X



Data Source:

Helpdesk reporting system



Owner:

Support Team Lead



Action Trigger:

Initiate 1:1 coaching if agent volume remains below 70% of team average for 2

consecutive weeks.




## Metric Name: Automation Resolution Rate



Definition:

Percentage of inbound tickets fully resolved by AI or self-service without

human intervention.



Formula:

(count\_ai\_resolved\_tickets / total\_inbound\_tickets) \* 100



Data Source:

AI system logs / Chatbot analytics



Owner:

AI Product Manager



Action Trigger:

Audit top unanswered intents if automation resolution rate drops below 30% for

1 week.




## Metric Name: Backlog Size



Definition:

Total number of tickets in an open, new, or pending state at the end of a

measurement period.



Formula:

count\_tickets WHERE status IN ('New', 'Open', 'Pending')



Data Source:

Helpdesk system



Owner:

Support Operations Manager



Action Trigger:

Trigger capacity rebalancing or overtime if backlog exceeds 3× daily average

volume for 2 consecutive days.





# C. AI Performance Metrics



## Metric Name: Intent Classification Accuracy



Definition:

Percentage of tickets where the AI correctly identifies the customer intent or

category.



Formula:

(count\_correct\_predictions / total\_predictions) \* 100



Data Source:

AI prediction logs and QA validation samples



Owner:

Machine Learning Engineer



Action Trigger:

Initiate model retraining if accuracy falls below 85% for high-volume intents.



Scope:

Applies to intent classification and routing models only.




## Metric Name: False Escalation Rate



Definition:

Percentage of escalated tickets that could have been resolved by AI based on

existing capabilities.



Formula:

(count\_false\_escalations / total\_escalations) \* 100



Data Source:

QA audit logs



Owner:

AI Product Manager



Action Trigger:

Review confidence thresholds if false escalation rate exceeds 10% for 2

consecutive weeks.





\### Metric Name: AI Override Rate



Definition:

Frequency with which human agents edit or reject AI-generated responses or

recommendations.



Formula:

(count\_human\_overrides / count\_ai\_suggestions) \* 100



Data Source:

Agent assist tool logs



Owner:

Knowledge Base Manager



Action Trigger:

Review and update knowledge base content if override rate exceeds 40% for a

specific topic.




## Metric Name: Model Drift Score



Definition:

Statistical measure of divergence between live data distributions and training

data.



Formula:

Statistical distance (e.g., KL divergence) between training data and rolling

production window



Data Source:

Model monitoring system



Owner:

Data Scientist



Action Trigger:

Trigger automated retraining pipeline if drift score exceeds 0.1.



Scope:

Applies to intent classification and routing models.






# D. Business Impact Metrics



## Metric Name: Cost per Ticket



Definition:

Fully loaded cost required to resolve a single support ticket.



Formula:

(Total support operating costs + technology costs) / total tickets resolved



Data Source:

Finance system and helpdesk data



Owner:

VP of Operations



Action Trigger:

Review vendor contracts or staffing model if cost per ticket exceeds budgeted

threshold.





## Metric Name: Support-Adjusted Retention Delta



Definition:

Difference in churn rate between customers who contacted support and those who

did not.



Formula:

churn\_rate\_contacted\_group - churn\_rate\_control\_group



Data Source:

CRM and subscription management system



Owner:

Customer Success Lead



Action Trigger:

Launch at-risk retention campaign if delta exceeds 5% over a quarterly period.




## Metric Name: Support Cost Ratio



Definition:

Support operating costs as a percentage of total company revenue.



Formula:

(Total support costs / total company revenue) \* 100



Data Source:

Finance / ERP system



Owner:

Chief Financial Officer



Action Trigger:

Freeze hiring and initiate cost optimization review if ratio exceeds approved

budget threshold.



