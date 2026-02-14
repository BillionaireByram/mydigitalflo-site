# AVA — Capabilities & Skills Reference

*What AVA can do for clients*

---

## Core Capabilities

### 1. Knowledge & Context
AVA knows everything about the client's business:
- Company overview and mission
- Products/services and pricing
- Target audience and ICP
- Team members and roles
- SOPs and processes
- Historical performance data

### 2. Communication
AVA can communicate through:
- Discord (current)
- Slack (current)
- Telegram (current)
- In-app chat (future)
- Email (future)
- SMS/Text (via GHL)
- Voice calls (via Retell - future)

### 3. Data & Reporting
AVA can pull and report:
- KPIs and metrics on demand
- Scheduled reports (daily, weekly, monthly)
- Ad performance (Facebook, Google)
- Webinar/funnel metrics
- Team performance data
- Revenue and sales data

### 4. Actions & Automation
AVA can execute:
- Update database records
- Trigger automations
- Send notifications
- Schedule reminders
- Create tasks
- Manage calendar events

---

## Skills Library

### Marketing & Ads

**`facebook-ads-stats`**
- Pull campaign performance
- Spend, clicks, CTR, CPC, CPM
- Conversion metrics
- Automated weekly reports

**`webinarkit-stats`**
- Registration numbers
- Attendance rates
- Completion rates
- Offer click-through

### Sales & CRM

**`ghl-conversations`**
- Handle inbound texts/SMS
- Lead qualification via chat
- Appointment booking
- Follow-up sequences

**`retell-voice`** (Future)
- Outbound sales calls
- Appointment confirmation
- Lead qualification by phone
- Call analytics

### Operations

**`trading-journal`** (Example of custom skill)
- Log trading sessions
- Track performance metrics
- Pattern analysis
- Psychology tracking

### General

**`web_search`**
- Research competitors
- Find information
- Market research

**`web_fetch`**
- Pull data from URLs
- Extract page content
- Monitor websites

---

## What AVA Can Do (Examples)

### On-Demand Requests
```
"AVA, what were our ad metrics this week?"
→ Pulls Facebook Ads data, formats report

"AVA, how many webinar registrations did we get?"
→ Pulls WebinarKit data, provides summary

"AVA, add John Smith as a new team member - he's a setter"
→ Updates database, confirms addition

"AVA, what's our close rate this month?"
→ Calculates from deals data, responds with analysis
```

### Scheduled Reports
```
Every Friday 10 AM:
→ Combined Facebook Ads + Webinar metrics report
→ Sent to #ai-team channel

Every Monday 9 AM:
→ Week-ahead priorities
→ Outstanding tasks reminder
```

### Proactive Alerts
```
When: New deal closed
→ AVA announces in channel, updates revenue tracking

When: Ad spend exceeds threshold
→ AVA alerts team, suggests action

When: Metrics drop significantly
→ AVA flags for review
```

---

## Building Custom Skills

### Skill Structure
```
/skills/
  └── skill-name/
      ├── SKILL.md (instructions for AVA)
      ├── scripts/ (optional automation scripts)
      └── assets/ (optional reference files)
```

### SKILL.md Format
```markdown
# Skill Name

## Description
What this skill does.

## Triggers
When to use this skill.

## Instructions
Step-by-step how to execute.

## Examples
Sample inputs and outputs.
```

### Adding to Client Build
1. Create skill folder in client workspace
2. Write SKILL.md with client-specific context
3. Add any necessary scripts
4. Test with sample queries
5. Document in client's knowledge base

---

## Capability Levels

### Level 1: Basic (MVP)
- Answer questions from knowledge base
- Pull metrics on demand
- Send scheduled reports
- Basic database updates

### Level 2: Intermediate
- Handle multi-step workflows
- Make decisions based on data
- Trigger complex automations
- Cross-reference multiple data sources

### Level 3: Advanced (AVA PRO)
- Autonomous operations management
- Strategic recommendations
- Predictive analytics
- Full system control

---

## Limitations (Current)

### Cannot Do (Yet)
- Real-time voice conversations (Retell integration pending)
- Direct GHL API writes (read-only for safety)
- Process payments
- Access external systems without API setup

### Guardrails
- Will not share client data across clients
- Will not execute destructive actions without confirmation
- Will not make financial decisions autonomously
- Will ask for clarification when uncertain

---

## Client-Specific Customization

Each client build includes:

1. **Custom Context** — CONTEXT.md with their specific business info
2. **Custom Skills** — Any integrations specific to their stack
3. **Custom Reports** — Metrics that matter to their business
4. **Custom Voice** — Tone and personality matching their brand

---

*AVA's capabilities expand as new skills are built and integrations are added.*
