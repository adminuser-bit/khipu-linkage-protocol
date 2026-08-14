# sealed/ — Ciphertexts only (APPEND-ONLY, CI-ENFORCED)

Only .age/.gpg ciphertexts and .sha256 commitments may live here — never
plaintext before its registered unmasking. Scheme (shadow-pilot pattern):
commit sha256(plaintext) + ciphertext before data contact; passphrase held by
the custodian for that item (operator in Phases A–B; independent human
custodian in Phase C per A12). Unmasking = committing the plaintext to
results/, which must verify against the prior commitment.
