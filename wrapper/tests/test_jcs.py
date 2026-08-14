"""Unit tests for the RFC 8785 (JCS) module."""
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
import jcs


class TestNumbers(unittest.TestCase):
    CASES = [
        (0, "0"),
        (-0.0, "0"),
        (1, "1"),
        (-1, "-1"),
        (1.0, "1"),
        (100.0, "100"),
        (0.5, "0.5"),
        (0.95, "0.95"),
        (-0.95, "-0.95"),
        (1e21, "1e+21"),
        (1.5e22, "1.5e+22"),
        (1e-7, "1e-7"),
        (1e-6, "0.000001"),
        (0.000001, "0.000001"),
        (333333333.3333333, "333333333.3333333"),
        (9007199254740991, "9007199254740991"),  # 2^53 - 1
        (2**53 - 1.0, "9007199254740991"),
    ]

    def test_cases(self):
        for value, expected in self.CASES:
            with self.subTest(value=value):
                self.assertEqual(
                    jcs.canonicalize(value).decode("utf-8"), expected)

    def test_rejects(self):
        for bad in (float("nan"), float("inf"), float("-inf"), 2**53, -(2**53)):
            with self.subTest(value=bad):
                with self.assertRaises(ValueError):
                    jcs.canonicalize(bad)


class TestStringsAndStructure(unittest.TestCase):
    def test_escapes(self):
        src = "a" + chr(34) + "b" + chr(92) + "c" + chr(10) + "d" + chr(9) \
            + "e" + chr(1)
        expected = ('"a' + chr(92) + chr(34) + "b" + chr(92) + chr(92)
                    + "c" + chr(92) + "nd" + chr(92) + "te" + chr(92)
                    + 'u0001"').encode("utf-8")
        self.assertEqual(jcs.canonicalize(src), expected)

    def test_unicode_literal(self):
        self.assertEqual(jcs.canonicalize("ñandú €"),
                         '"ñandú €"'.encode("utf-8"))

    def test_key_sort_utf16(self):
        # RFC 8785 §3.2.3: member names sort by UTF-16 code units. U+1D306
        # encodes as a surrogate pair starting 0xD834, which precedes U+FF01
        # in code-unit order even though its code point is higher.
        obj = {"\U0001d306": 1, "！": 2, "a": 3}
        out = jcs.canonicalize(obj).decode("utf-8")
        self.assertLess(out.index("a"), out.index("\U0001d306"))
        self.assertLess(out.index("\U0001d306"), out.index("！"))

    def test_rfc_number_and_literal_composite(self):
        obj = {
            "literals": [None, True, False],
            "numbers": [333333333.3333333, 1e30, 4.5, 0.002, 1e-27],
        }
        self.assertEqual(
            jcs.canonicalize(obj).decode("utf-8"),
            '{"literals":[null,true,false],'
            '"numbers":[333333333.3333333,1e+30,4.5,0.002,1e-27]}',
        )

    def test_rejects_non_string_keys_and_odd_types(self):
        with self.assertRaises(ValueError):
            jcs.canonicalize({1: "a"})
        with self.assertRaises(ValueError):
            jcs.canonicalize({"a": set()})

    def test_hash_stability(self):
        self.assertEqual(
            jcs.sha256_jcs(["KHI-A22-LOTTERY-20260814", "agi/lima/464"]),
            jcs.sha256_jcs(["KHI-A22-LOTTERY-20260814", "agi/lima/464"]),
        )


if __name__ == "__main__":
    unittest.main()
