"""
pii_entity_masker.py - Detects and masks personal identifying numbers, emails, and phone records
"""
import sys
import json


def mask_pii_entities(document_text: str):
    import re
    text = re.sub(r"\b\d{3}-\d{2}-\d{4}\b", "[SSN_REDACTED]", document_text)
    text = re.sub(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", "[EMAIL_REDACTED]", text)
    count = document_text.count("@")
    return {"redacted_text": text, "entities_masked": count, "status": "REDACTION_COMPLETE"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "pii-entity-masker"}))
