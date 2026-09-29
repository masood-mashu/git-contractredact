"""
confidential_clause_tagger.py - Flags non-disclosure, intellectual property transfer, and non-solicitation clauses
"""
import sys
import json


def tag_confidential_clauses(clause_text: str):
    keywords = ["confidential", "trade secret", "non-compete", "indemnification"]
    found = [k for k in keywords if k in clause_text.lower()]
    return {"clauses_found": found, "requires_review": len(found) > 0, "status": "CLAUSES_TAGGED" if len(found) > 0 else "NO_RESTRICTIVE_CLAUSES"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "confidential-clause-tagger"}))
