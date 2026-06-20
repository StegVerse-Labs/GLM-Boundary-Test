# Invalid-Control Notes

## Purpose

The invalid-control files are deliberate test artifacts.

They exist to prove that Boundary Test can reject unsafe boundary behavior instead of only confirming the prepared review-only fixture.

## Included Invalid-Control Files

- `negative-control-boundary-manifest.json`
- `invalid-control-comparison-fixture.json`
- `run_boundary_regression.py`

## What The Invalid-Control Case Tests

The invalid-control case introduces an artifact that claims authority linkage through adjacency.

Boundary Test must reject that condition.

Expected result:

```text
FAIL
```

## Why This Matters

A boundary test is not strong enough if it only demonstrates a clean review path.

It must also demonstrate that the system can identify a boundary violation, including:

- authority inheritance
- delegated authority
- implied interoperability
- external validity dependency

## Regression Command

Run:

```bash
python run_boundary_regression.py
```

Expected result:

```text
{
  "regression": "PASS",
  ...
}
```

This means the normal fixture returns `REVIEW_ONLY` and the invalid-control fixture returns `FAIL`.
