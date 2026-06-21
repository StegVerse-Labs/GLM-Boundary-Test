# Review Ownership Policy

## Purpose

This document defines the review posture for boundary-sensitive changes in this repository.

It is advisory only. It does not alter repository permissions, create delegated authority, create execution authority, establish GLM conformance, or establish interoperability.

## Review-Sensitive Changes

The following changes should receive boundary review before merge:

- changes to boundary artifacts
- changes to comparison fixtures
- changes to invalid-control artifacts
- changes to schemas
- changes to SDK descriptors
- changes to runners or verification scripts
- changes to CI workflows
- changes to reviewer-facing documentation
- changes to claims, non-claims, authority scope, or outcome language

## Review Questions

Every boundary-sensitive change should answer:

1. Does this change preserve REVIEW-ONLY as the top-level GLM-adjacent posture?
2. Does this change avoid GLM conformance or compatibility claims?
3. Does this change avoid interoperability-by-adjacency?
4. Does this change avoid delegated authority?
5. Does this change avoid execution authority?
6. Does this change avoid consequence authority?
7. Do validation commands still pass?

## Required Validation

Run or confirm CI runs:

```bash
python generate_status.py
python validate_boundary_schemas.py
python run_example_cases.py
python run_boundary_test.py
python run_boundary_regression.py
```

## Review Outcome Language

Use this top-level posture for the prepared GLM-adjacent fixture:

```text
REVIEW-ONLY
```

Use PASS only for specific boundary checks.

Do not use a bare PASS as the final GLM-adjacent result.

## Non-Authority Statement

Review ownership in this repository is procedural.

It does not create external framework conformance, interoperability, adoption, endorsement, delegated authority, execution authority, or consequence authority.
