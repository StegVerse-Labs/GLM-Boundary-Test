# Example Validation

## Purpose

Example validation confirms that instructional examples demonstrate the expected Boundary Test outcome classes.

This validation does not create GLM conformance, GLM compatibility, interoperability, adoption, endorsement, delegated authority, or execution authority.

## Command

Run:

```bash
python run_example_cases.py
```

## Expected Result

```text
{
  "examples": "PASS",
  ...
}
```

## Covered Examples

| Example | Expected Outcome |
|---|---|
| `examples/review-only-clean-mapping.json` | `REVIEW_ONLY` |
| `examples/incomplete-missing-authority-scope.json` | `INCOMPLETE` |

## Relationship To Main Boundary Test

Example validation is instructional.

The main prepared Boundary Test remains:

```bash
python run_boundary_test.py
```

The regression test remains:

```bash
python run_boundary_regression.py
```
