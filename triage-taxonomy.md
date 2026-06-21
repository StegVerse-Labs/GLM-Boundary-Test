# Triage Taxonomy

## Purpose

This document defines suggested triage categories for Boundary Test issues and pull requests.

The taxonomy is advisory only. It does not create GLM conformance, interoperability, adoption, endorsement, delegated authority, execution authority, or consequence authority.

## Suggested Categories

| Category | Use |
|---|---|
| boundary review | Request or track review of a boundary artifact, fixture, or claim |
| artifact proposal | Propose a new artifact, fixture, example, schema, or documentation file |
| boundary violation | Track suspected authority inheritance, implied interoperability, or unclear authority scope |
| schema | Changes to schemas or schema validation |
| sdk | Changes to SDK option descriptors, user instructions, or runner behavior |
| ci | Changes to verification automation |
| documentation | Changes to Markdown guidance or reviewer-facing notes |
| invalid control | Changes to deliberate failing examples or regression controls |
| release | Version, changelog, release note, or readiness changes |
| review only | Changes preserving or clarifying the REVIEW-ONLY posture |

## Triage Rules

- Use boundary violation when a change may create authority inheritance, implied conformance, implied interoperability, adoption, endorsement, delegated authority, execution authority, or consequence authority.
- Use review only when a change clarifies review or comparison without adding external authority claims.
- Use invalid control only for deliberate failing cases.
- Use sdk when a change affects user-facing Boundary Test behavior.
- Use schema when a change affects JSON structure or validation.

## Required Boundary Reminder

Triage categories are organizational aids only.

They do not indicate GLM conformance, GLM compatibility, interoperability, adoption, endorsement, delegated authority, execution authority, or consequence authority.
