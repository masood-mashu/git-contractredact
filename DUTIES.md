# Separation of Duties (SOD) & Operational Boundaries

To ensure robust compliance, security, and verification, **GitContractRedact** implements a strict tripartite Separation of Duties architecture.

---

### 1. Maker
* **Assigned Entity**: `GitContractRedact Automation Engine`
* **Responsibilities**:
  * Applies cryptographic regex and NLP entity masking to sensitive contract clauses.
  * Ingests raw repository data, configurations, and input artifacts.
  * Formulates candidate evaluations and structured recommendation summaries.
  * Records execution logs into `memory/audit.log`.

---

### 2. Checker
* **Assigned Entity**: `GitContractRedact Verification & Policy Enforcer`
* **Responsibilities**:
  * Verifies that masked strings cannot be reversed or extracted through PDF text layers.
  * Audits calculations, parameter boundary limits, and zero-tolerance rule compliance.
  * Asserts schema validity on all output manifests.
  * Issues preliminary assessment: `APPROVED`, `BLOCKED`, or `NEEDS_REVIEW`.

---

### 3. Approver
* **Assigned Entity**: `General Counsel / Senior Partner (Reserved for human review).`
* **Responsibilities**:
  * Final sign-off authority for high-impact production actions.
  * Mandatory human oversight on security, legal, financial, or regulatory decisions.
  * Reviews unresolvable edge cases and policy override exceptions.
