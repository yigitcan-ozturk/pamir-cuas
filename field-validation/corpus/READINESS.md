# Corpus execution readiness

| Case | Harness | Real source required | Perturbation allowed | Execution gate |
|---|---|---|---|---|
| C-FV01 | Ready | Yes | No | source inventory + hashes |
| C-FV02 | Ready | Yes | Only if no observed case | source inventory + hashes |
| C-FV03 | Ready | Yes | Sensor dropout | source inventory + hashes |
| C-FV04 | Ready | Yes | Sensor delay | source inventory + hashes |
| C-FV05 | Ready | Yes | Index offset | source inventory + hashes |
| C-FV06 | Ready | Yes | Derived/controlled | source inventory + hashes |
| C-FV07 | Ready | Yes, non-drone reference | No | source inventory + hashes + declared detection rule |

The harness is structurally ready. PASS/FAIL results remain intentionally unset until source payload acquisition and checksum verification are complete.
