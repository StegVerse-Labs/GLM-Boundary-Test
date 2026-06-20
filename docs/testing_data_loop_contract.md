# Testing Data Loop Contract

Boundary-Test is a downstream boundary and GLM-style evaluation route.

Boundary fixtures reach this repository after the corrected testing data loop has produced receipt-bound artifacts and any private-review-first naming concerns have been resolved.

## Required Upstream Loop

```text
User
→ StegVerse-org/StegVerse-SDK or LLM Adapter
→ StegVerse-org ingestion
→ StegGhost/entity-sandbox-runner ingestion/CGE
→ ephemeral sandbox batch
→ StegGhost/entity-sandbox-runner ingestion/CGE return validation
→ StegVerse-org ingestion
→ Boundary-Test
```

## Required Input Evidence

Boundary inputs preserve:

```text
sdk_or_llm_adapter_intake receipt
stegverse_org_ingestion_outbound receipt
stegghost_ingestion_cge_admission receipt
ephemeral_sandbox_batch receipt
stegghost_ingestion_cge_return_validation receipt
stegverse_org_ingestion_return receipt
master-records action receipt references
```

## Boundary Responsibility

Boundary-Test checks boundary declaration, non-claim preservation, and manifest composability.

It does not imply external adoption, endorsement, compatibility, conformance, delegated authority, shared execution authority, or authority inheritance.

SDK contract reference:

```text
StegVerse-org/StegVerse-SDK/docs/TESTING_DATA_LOOP_CONTRACT.md
```

Route result schema:

```text
StegVerse-org/StegVerse-SDK/schemas/formal-testing-route-result.schema.json
```
