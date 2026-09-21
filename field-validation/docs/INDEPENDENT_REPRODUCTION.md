# Independent reproduction protocol

An independent reproduction must start from the published dataset record, not from a previously generated PAMIR-CUAS output.

The reproducer must record:
1. dataset DOI and resolved source file identifiers;
2. source repository checksum where supplied;
3. independently computed SHA-256;
4. PAMIR-CUAS code commit;
5. case parameters and any controlled perturbation specification;
6. generated output SHA-256;
7. environment metadata;
8. comparison outcome against the reference Evidence Object.

A reproduction is not successful merely because code executes. The evidence-relevant fields must deterministically agree under the declared comparison policy.
