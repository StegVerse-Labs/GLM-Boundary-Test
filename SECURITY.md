# Security and Boundary-Risk Reporting

## Scope

This repository is a review-only Boundary Test fixture.

It is not a runtime system, enforcement service, authentication layer, production SDK, or execution authority.

Security reporting in this repository is limited to boundary-risk concerns that could cause reviewers or tooling to misread review artifacts as conformance, interoperability, delegated authority, execution authority, or consequence authority.

## Reportable Boundary Risks

Please report concerns such as:

- language implying GLM conformance or compatibility
- language implying external adoption or endorsement
- implied interoperability by adjacency
- unintended authority inheritance
- unintended delegated authority
- unintended execution authority
- unclear claims or non-claims
- missing or misleading authority scope
- verifier behavior that accepts unsafe authority linkage
- invalid-control cases that do not fail as expected

## Non-Scope

This repository does not operate live services or handle secrets.

Do not submit reports expecting runtime incident response, credential rotation, production service remediation, or exploit handling for deployed systems.

## Preferred Public Reporting Path

For non-sensitive boundary concerns, open an issue using one of the repository issue templates:

- Boundary Review
- Artifact Proposal
- Boundary Violation

## Sensitive Reporting

If a concern should not be public, contact the repository owner directly through an available private channel before posting details publicly.

## Safe Outcome Language

The expected top-level outcome for the prepared GLM-adjacent fixture remains:

```text
REVIEW-ONLY
```

Boundary checks may pass, but this repository must not be interpreted as claiming GLM conformance, GLM compatibility, adoption, endorsement, runtime interoperability, delegated authority, execution authority, or consequence authority.
