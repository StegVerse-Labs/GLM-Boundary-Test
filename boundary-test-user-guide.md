# Boundary Test User Guide

## What Boundary Test Does

Boundary Test checks whether governance artifacts can be discovered and reviewed together without creating unintended authority inheritance, interoperability assumptions, delegated authority, conformance claims, or execution authority.

Use it when you want to compare governance artifacts without accidentally treating comparison as compatibility.

## When To Choose Boundary Test

Choose `Boundary Test` when asking:

- Can these governance artifacts be reviewed together?
- Does one artifact inherit authority from another?
- Does a reference imply interoperability?
- Does a comparison imply conformance?
- Does discoverability create shared authority?
- Does a boundary manifest clearly state its claims and non-claims?

## What To Provide

Provide one or more of the following:

- a governance artifact
- an organization index
- a boundary manifest
- a governance-layer manifest
- a comparison fixture
- a repository URL containing the artifacts

If no user fixture is supplied, the SDK may use this repository as the default example fixture.

## Expected Result For The Prepared GLM Boundary Exercise

The preferred top-level result is:

```text
REVIEW-ONLY: independently discoverable, independently reviewable, no authority inheritance detected.
Boundary checks: PASS.
Conformance claim: NOT MADE.
Interoperability claim: NOT MADE.
Adoption claim: NOT MADE.
Execution authority: NOT GRANTED.
```

This means the artifacts can be reviewed together, but the test does not claim GLM conformance, interoperability, adoption, endorsement, or execution authority.

## Outcome Meanings

### REVIEW-ONLY

The artifacts can be compared for boundary review, but no conformance, interoperability, adoption, delegation, or execution authority is claimed.

### PASS

A specific boundary check passed.

PASS must not be used by itself as the final GLM-adjacent outcome.

### FAIL

A boundary violation was detected, such as authority inheritance, delegated authority, implied interoperability, or external validity dependency.

### INCOMPLETE

The SDK does not have enough artifact information to evaluate the boundary. Claims, non-claims, authority scope, or required files may be missing.

## What Boundary Test Does Not Do

Boundary Test does not prove:

- GLM conformance
- StegVerse conformance
- interoperability
- external endorsement
- runtime enforcement
- execution admissibility
- delegated authority
- consequence authority

## Local Command

From this repository, run:

```bash
python run_boundary_test.py
```

For the included fixture, the expected result is `REVIEW-ONLY` with boundary checks passing.
