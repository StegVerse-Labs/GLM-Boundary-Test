# Comparison Report Guide

## Purpose

The comparison report generator creates a reviewer-ready Markdown report from the Boundary Test repository.

The report summarizes:

- repository version
- review-only posture
- expected GLM-adjacent result
- non-claims
- fixture expectations
- verification command outputs
- final interpretation

## Command

Run:

```bash
python generate_comparison_report.py
```

Expected output:

```text
Wrote comparison-report.md
PASS: comparison report generated.
```

## Generated File

The command writes:

```text
comparison-report.md
```

## Safe Interpretation

A generated passing report supports review-only comparison.

It does not establish GLM conformance, GLM compatibility, adoption, endorsement, runtime interoperability, delegated authority, execution authority, or consequence authority.

## Recommended Use

Generate the report before sending the repository to an external reviewer or before preparing a release package.
