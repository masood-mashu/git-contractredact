"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitContractRedact.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.pii_entity_masker import *
from tools.confidential_clause_tagger import *
from tools.redaction_hash_verifier import *

class TestGitContractRedactPredictability(unittest.TestCase):
    def test_pii_entity_masker(self):
        res = mask_pii_entities("Contact the witness at john.doe@example.com for deposition.")
        self.assertIn("[EMAIL_REDACTED]", res["redacted_text"])
        self.assertEqual(res["status"], "REDACTION_COMPLETE")

    def test_confidential_clause_tagger(self):
        res = tag_confidential_clauses("All financial terms shall remain strictly confidential between parties.")
        self.assertTrue(res["requires_review"])
        self.assertEqual(res["status"], "CLAUSES_TAGGED")

    def test_redaction_hash_verifier(self):
        res = verify_redaction_hash("Party A agrees to [REDACTED] on closing.")
        self.assertEqual(len(res["sha256_hash"]), 64)
        self.assertEqual(res["status"], "SEAL_VALID")


if __name__ == "__main__":
    unittest.main()
