import json
from pathlib import Path

BASE = Path(__file__).resolve().parent


def load(name):
    path = BASE / name
    if not path.exists():
        raise AssertionError(f"Missing required file: {name}")
    return json.loads(path.read_text(encoding="utf-8"))


def assert_no_authority_transfer(artifact, name):
    scope = artifact.get("authority_scope", {})
    inherited = scope.get("inherits_authority_from", None)
    granted = scope.get("grants_authority_to", None)

    if inherited != []:
        raise AssertionError(f"{name} inherits authority: {inherited}")
    if granted != []:
        raise AssertionError(f"{name} grants authority: {granted}")


def main():
    fixture = load("boundary-comparison-fixture.json")
    expected = fixture["expected_results"]

    if expected.get("authority_inheritance_allowed") is not False:
        raise AssertionError("Fixture must prohibit authority inheritance.")

    if expected.get("interoperability_claim_allowed") is not False:
        raise AssertionError("Fixture must prohibit interoperability claims.")

    if expected.get("external_validity_dependency_allowed") is not False:
        raise AssertionError("Fixture must prohibit external validity dependency.")

    for item in fixture["artifacts"]:
        if item.get("expected_independently_discoverable") is not True:
            raise AssertionError(f"{item['artifact_id']} is not expected to be independently discoverable.")

        artifact = load(item["path"])
        assert_no_authority_transfer(artifact, item["path"])

    org_index = load("organization-index.json")
    review = org_index.get("review_posture", {})
    if review.get("requires_external_manifest_to_be_valid") is not False:
        raise AssertionError("Organization index must not require an external manifest to be valid.")

    print("PASS: boundary fixture preserves independent discoverability without authority inheritance.")


if __name__ == "__main__":
    main()
