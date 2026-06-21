# Pull Request Guide

## Purpose

This repository includes a pull request template to keep future changes aligned with Boundary Test rules.

## Template Path

Displayed path without the leading dot:

`github/pull_request_template.md`

Note: the actual repository path uses GitHub's standard leading-dot directory.

## Required Pull Request Posture

Every pull request should preserve the distinction between:

- review
- comparison
- conformance
- interoperability
- adoption
- endorsement
- delegation
- execution authority
- consequence authority

## Required Validation Commands

Pull requests should preserve successful execution of:

```bash
python generate_status.py
python validate_boundary_schemas.py
python run_example_cases.py
python run_boundary_test.py
python run_boundary_regression.py
```

## Safe Expected Result

For the prepared GLM-adjacent fixture, the top-level result should remain:

```text
REVIEW-ONLY
```

A pull request must not turn this result into a bare PASS, GLM conformance, GLM compatibility, adoption, endorsement, interoperability, delegation, or execution authority claim.
