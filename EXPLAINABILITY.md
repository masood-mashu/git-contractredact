# Explainability, Auditability & Decision Logic: GitContractRedact

This document details the transparent decision architecture, algorithmic criteria, data provenance, and operational boundaries of **GitContractRedact**, ensuring complete compliance with OpenGAP standards and Checkpoint 02 requirements.

---

## 1. Input Data and Data Sources Used

**GitContractRedact** ingests structured, machine-verifiable data artifacts from well-defined sources to ensure total repeatability:
- **Raw**: Raw contract text files, OCR litigation scans, and legal agreement drafts.
- **Statutory**: Statutory PII definition taxonomies (GDPR, CCPA, HIPAA).
- **Party-negotiated**: Party-negotiated Confidential Information disclosure schedules.
- **OpenGAP Specification Manifests**: Ingests `agent.yaml`, `RULES.md`, and local state from `memory/MEMORY.md`.

All data sources are parsed deterministically without dynamic external unverified calls, ensuring that evaluations reflect the exact state of the repository at the moment of inspection.

---

## 2. How It Decides and Reasoning Process

The decision pipeline operates through a multi-stage validation sequence designed to eliminate subjective ambiguity:

1. **Syntax & Schema Verification**: Ingested inputs are first validated against strict JSON and YAML schemas defined in `tools/`. Any malformed payloads are immediately rejected.
2. **Deterministic Metric Extraction**:
   - **mask_pii_entities**: Uses `pii-entity-masker` to calculate detects and masks personal identifying numbers, emails, and phone records.
   - **tag_confidential_clauses**: Uses `confidential-clause-tagger` to calculate flags non-disclosure, intellectual property transfer, and non-solicitation clauses.
   - **verify_redaction_hash**: Uses `redaction-hash-verifier` to calculate generates sha-256 cryptographic seal of redacted document content.
3. **Policy Boundary Checks**: Extracted metrics are evaluated against the non-negotiable rules defined in `RULES.md`.
4. **Verdict Synthesis**:
   - **`APPROVED`**: Issued when all criteria strictly pass thresholds, zero compliance violations are detected, and data integrity is certified.
   - **`NEEDS_REVIEW`**: Issued when borderline metrics or ambiguous edge cases require human supervisor assessment.
   - **`BLOCKED`**: Issued immediately upon detecting any violation of zero-tolerance rules, severe risk factors, or non-compliant parameters.

When an agreement is submitted for redaction, the agent runs pii_entity_masker, confidential_clause_tagger, and redaction_hash_verifier. If all PII is masked and the hash seals cleanly, it issues APPROVED. If non-standard commercial disclosures are present, it issues NEEDS_REVIEW. If unmasked personal identifiers persist, it issues BLOCKED.

---

## 3. Constraints, Limitations, and Known Issues

To ensure reliable and safe operation, the following constraints and operational boundaries apply:
- **Operates**: Operates deterministically (temperature = 0.1) using regex patterns and exact entity matching.
- **Does**: Does not render legal advice on contract enforceability under state jurisdictions.
- **Preserves**: Preserves original unredacted archives strictly in client-encrypted legal vault.
- **Deterministic Execution Constraint**: All model prompts and evaluations must run with low temperature (`0.1`) to ensure predictable, reproducible scoring and eliminate hallucinated findings.
- **Human Authority**: The agent cannot self-execute irreversible external mutations; final approval is reserved strictly for human authorities as specified in `DUTIES.md`.
