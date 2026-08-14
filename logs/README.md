# logs/ — Audit logs (APPEND-ONLY, CI-ENFORCED)

- search-log.jsonl — THE HOLM DENOMINATOR. One line per (khipu, document,
  grouping) triple scored, appended before interpretation; also every
  LLM-triage candidate suggestion (logged as a search action per G5).
- operator-log.md — every manual data act by the operator (A24.4, A26).
- custody-log.md — Phase C custodian's log (A12); a tribunal deliverable.
- agent-prompts/ — full prompt + configuration of every agent invocation,
  committed no later than the invocation (A24.2). Uncommitted prompt ⇒
  inadmissible output.
