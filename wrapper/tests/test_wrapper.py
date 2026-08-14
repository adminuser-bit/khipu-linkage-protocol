"""Unit tests for wrapper internals that need no git remote.

The full A24.2 path (pre-commit push verification, capture, result commit)
is exercised end-to-end by `invoke.py selftest`, whose records live in
logs/invocations/.
"""
import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import invoke
import jcs


class TestRunIds(unittest.TestCase):
    def test_run_id_regex(self):
        m = invoke.RUN_ID_RE.match("KHI-RUN-000042.pre.json")
        self.assertIsNotNone(m)
        self.assertEqual(m.group(1), "000042")
        for bad in ("KHI-RUN-42.pre.json", "KHI-RUN-000042.result.json",
                    "khi-run-000042.pre.json", "KHI-RUN-0000420.pre.json"):
            self.assertIsNone(invoke.RUN_ID_RE.match(bad), bad)

    def test_next_run_id_monotonic(self):
        orig = invoke.INVOCATIONS_DIR
        try:
            with tempfile.TemporaryDirectory() as td:
                invoke.INVOCATIONS_DIR = pathlib.Path(td)
                self.assertEqual(invoke.next_run_id(), "KHI-RUN-000001")
                (invoke.INVOCATIONS_DIR / "KHI-RUN-000007.pre.json").touch()
                self.assertEqual(invoke.next_run_id(), "KHI-RUN-000008")
                self.assertEqual(invoke.pending_runs(), ["KHI-RUN-000007"])
                (invoke.INVOCATIONS_DIR
                 / "KHI-RUN-000007.result.json").touch()
                self.assertEqual(invoke.pending_runs(), [])
        finally:
            invoke.INVOCATIONS_DIR = orig


class TestRecords(unittest.TestCase):
    def test_write_record_hash_is_jcs_not_file_bytes(self):
        with tempfile.TemporaryDirectory() as td:
            p = pathlib.Path(td) / "r.json"
            record = {"b": 1, "a": [True, None, "ñ"]}
            digest = invoke.write_record(p, record)
            self.assertEqual(digest, jcs.sha256_jcs(record))
            # reload from the pretty rendering; JCS hash must be identical
            self.assertEqual(jcs.sha256_jcs(invoke.load_record(p)), digest)


class TestRoles(unittest.TestCase):
    def test_selftest_role_not_registered(self):
        self.assertNotIn(invoke.SELFTEST_ROLE, invoke.REGISTERED_ROLES)


if __name__ == "__main__":
    unittest.main()
