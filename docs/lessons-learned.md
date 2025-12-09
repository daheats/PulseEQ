# Lessons Learned
PulseEQ is intentionally designed as a learning project to explore real-world data ingestion, NLP enrichment, and visualization workflows. Throughout development, several key lessons emerged that shaped the architecture and approach.

## 1. Dataset Formats Aren't Always Forward-Compatible

The first major lesson from PulseEQ was discovering that the McAuley-Lab Amazon Reviews 2023 dataset uses a script-based loader, which is no longer supported in newer versions of the Hugging Face datasets library (3.x and above).

This caused ingestion failures until:

- The issue was diagnosed
- The library version was pinned to datasets==2.19.1
- Documentation was updated to reflect the constraint

#### Key Takeaways

- Always check how a dataset is structured (Parquet, JSON, Arrow, script-loader, etc.) before designing your pipeline.
- Library updates can break previously working datasets, especially academic or older community-contributed ones.
- Pinning dependencies early prevents downstream errors and improves reproducibility.
- MVP velocity dramatically improves when you detect format incompatibilities upfront instead of mid-build.

#### Future Consideration
Consider switching to a Parquet-based Amazon Reviews dataset post-MVP to eliminate dependency constraints and enable easier scaling, faster load times, and compatibility with modern versions of the datasets library.

This single insight directly influenced PulseEQ’s dataset loading strategy, environment setup, and technical documentation.

## 2. Dataset Bonus Fields

Some datasets include bonus fields (e.g., images) that are not needed for the MVP but may become valuable later. It’s helpful to note their potential early to avoid limiting future functionality.

## 3. Placeholder Lesson: Something Profound Definitely Goes Here

This section is intentionally left blank(-ish).

Future Heather will fill this with another hard-won insight once PulseEQ teaches her something new — ideally not involving cryptic stack traces or accidental dependency chaos.

_Stay tuned. Wisdom pending._