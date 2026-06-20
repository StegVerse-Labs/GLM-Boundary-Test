# Changelog

All notable changes to this repository should be documented here.

This repository is a review-only Boundary Test fixture. Version changes must not imply GLM conformance, GLM compatibility, interoperability, adoption, endorsement, delegated authority, execution authority, or consequence authority.

## 0.1.0 - Initial Boundary Test Baseline

### Added

- Organization-index fixture.
- StegVerse boundary manifest fixture.
- GLM placeholder artifact for comparison only.
- Boundary comparison fixture.
- Five-question resolution.
- Manual test plan.
- Deterministic positive fixture verifier.
- SDK Boundary Test option descriptor.
- SDK Boundary Test user instructions.
- Boundary Test outcome taxonomy.
- SDK-style Boundary Test runner.
- Boundary Test user guide.
- Invalid-control fixture and notes.
- Regression runner for positive and invalid-control paths.
- GitHub Actions CI workflow.
- CI documentation.
- Release readiness checklist.
- Reviewer handoff.
- Repository index.
- Machine-readable repository manifest.
- JSON schemas for boundary artifacts and comparison fixtures.
- Standard-library schema validator.
- Extension guide and templates.
- Example cases and example validation runner.

### Expected Baseline Results

```text
python validate_boundary_schemas.py
PASS: boundary artifact and comparison fixture schemas validated.

python run_example_cases.py
examples: PASS

python run_boundary_test.py
REVIEW-ONLY

python run_boundary_regression.py
regression: PASS
```

### Non-Claims

Version 0.1.0 does not claim:

- GLM conformance
- GLM compatibility
- GLM adoption
- GLM endorsement
- runtime interoperability
- delegated authority
- execution authority
- consequence authority
