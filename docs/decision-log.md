# Summary

This document captures key technical and architectural decisions made during the development of PulseEQ. 

The goal is to provide transparency, traceability, and clear reasoning for choices that impact the system’s design and long-term maintainability.

| ID   | Decision                     | Date              | Status    | Description |
|------|------------------------------|-------------------|-----------|-------------|
| 001  | Pin `datasets` to `2.19.1`   | December 8, 2025  | Accepted  | Ensures compatibility with script-based dataset loader used by Amazon Reviews 2023. |
| 002  | Exclude image processing for MVP | December 8, 2025 | Accepted | Image data is available but not used in the initial version. May be incorporated in later versions to validate negative reviews or detect product defects. |
| 003  | Generate product labels using AI for MVP | December 8, 2025 | Accepted | ASINs in the dataset have no product names. AI-generated labels allow grouping and analysis without requiring an external Amazon catalog. |