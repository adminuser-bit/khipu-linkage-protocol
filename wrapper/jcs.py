"""RFC 8785 (JSON Canonicalization Scheme) serialization.

Implements the JCS rules used by every structured hash in this record
(A20.9 as extended to invocation records by A24.2 implementation):

- Object member names sorted by their UTF-16 code units (achieved here by
  sorting on the UTF-16BE encoding of each key, which yields the identical
  order).
- Minimal string escaping: \\" \\\\ \\b \\t \\n \\f \\r, other control
  characters as lowercase \\u00xx, all other characters emitted literally;
  output encoded as UTF-8.
- Numbers serialized per ECMAScript Number::toString (shortest round-trip
  form). Integers outside +/-(2^53 - 1) are rejected (not representable as
  IEEE-754 doubles without loss). NaN and infinities are rejected.
- Only null, bool, int, float, str, list, tuple, and dict (with str keys)
  are accepted. Anything else raises ValueError rather than guessing.

No dependencies beyond the standard library.
"""

import hashlib
import math

_ESCAPES = {
    '"': '\\"',
    "\\": "\\\\",
    "\b": "\\b",
    "\t": "\\t",
    "\n": "\\n",
    "\f": "\\f",
    "\r": "\\r",
}

_MAX_SAFE_INT = 2**53 - 1


def _serialize_string(s: str) -> str:
    out = ['"']
    for ch in s:
        esc = _ESCAPES.get(ch)
        if esc is not None:
            out.append(esc)
        elif ord(ch) < 0x20:
            out.append("\\u%04x" % ord(ch))
        else:
            out.append(ch)
    out.append('"')
    return "".join(out)


def format_double(x: float) -> str:
    """ECMAScript Number::toString for a finite double (RFC 8785 §3.2.2.3)."""
    if math.isnan(x) or math.isinf(x):
        raise ValueError("NaN and Infinity are not permitted in JCS")
    if x == 0:
        return "0"  # covers -0.0, per ECMAScript String(-0) == "0"
    r = repr(abs(x))  # shortest round-trip digits
    if "e" in r:
        mantissa, _, exp_s = r.partition("e")
        exp = int(exp_s)
    else:
        mantissa, exp = r, 0
    int_part, _, frac_part = mantissa.partition(".")
    digits = int_part + frac_part
    # n = position of the decimal point relative to the first significant digit
    n = len(int_part) + exp
    stripped = digits.lstrip("0")
    n -= len(digits) - len(stripped)
    digits = stripped.rstrip("0")
    k = len(digits)
    if k <= n <= 21:
        out = digits + "0" * (n - k)
    elif 0 < n <= 21:
        out = digits[:n] + "." + digits[n:]
    elif -6 < n <= 0:
        out = "0." + "0" * (-n) + digits
    else:
        e = n - 1
        mant_out = digits[0] + ("." + digits[1:] if k > 1 else "")
        out = mant_out + "e" + ("+" if e >= 0 else "-") + str(abs(e))
    return "-" + out if x < 0 else out


def _serialize(value) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        if abs(value) > _MAX_SAFE_INT:
            raise ValueError(
                "integer %d exceeds 2^53-1 and is not exactly representable "
                "as an IEEE-754 double" % value
            )
        return str(value)
    if isinstance(value, float):
        return format_double(value)
    if isinstance(value, str):
        return _serialize_string(value)
    if isinstance(value, (list, tuple)):
        return "[" + ",".join(_serialize(v) for v in value) + "]"
    if isinstance(value, dict):
        for k in value:
            if not isinstance(k, str):
                raise ValueError("JCS object member names must be strings")
        keys = sorted(value.keys(), key=lambda k: k.encode("utf-16-be"))
        return "{" + ",".join(
            _serialize_string(k) + ":" + _serialize(value[k]) for k in keys
        ) + "}"
    raise ValueError("type not permitted in JCS input: %r" % type(value))


def canonicalize(value) -> bytes:
    """Return the RFC 8785 canonical UTF-8 encoding of *value*."""
    return _serialize(value).encode("utf-8")


def sha256_jcs(value) -> str:
    """SHA-256 over exactly JCS(value), hex digest (A20.9: no prefix,
    suffix, delimiter, or additional normalization)."""
    return hashlib.sha256(canonicalize(value)).hexdigest()
