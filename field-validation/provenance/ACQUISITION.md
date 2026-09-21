# Source acquisition protocol

1. Resolve the published TSMS-Drone Figshare record from its DOI.
2. Capture record metadata and file inventory before downloading payloads.
3. Download only from the public repository-provided file URL.
4. Preserve each downloaded source file read-only.
5. Verify repository-provided checksum when available and independently compute SHA-256.
6. Record source filename, byte size, repository file ID, repository checksum, local SHA-256, acquisition date, and dataset DOI.
7. Never commit large third-party source payloads to this repository. Commit manifests and derived evidence artefacts only unless redistribution is explicitly required and appropriate.

Figshare documents that public item metadata exposes per-file download URLs through its API. The harness therefore separates metadata inventory from payload acquisition.
