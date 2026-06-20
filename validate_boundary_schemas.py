import json
from pathlib import Path

BASE = Path(__file__).resolve().parent

BOUNDARY_ARTIFACTS = [
    "stegverse-boundary-manifest.json",
    "glm-boundary-placeholder.json",
    "negative-control-boundary-manifest.json",
]

COMPARISON_FIXTURES = [
    "boundary-comparison-fixture.json",
    "invalid-control-comparison-fixture.json",
]


def load_json(path_name):
    path = BASE / path_name
    if not path.exists():
        raise AssertionError(f"missing file: {path_name}")
    return json.loads(path.read_text(encoding="utf-8"))


def require_keys(obj, keys, label):
    missing = [key for key in keys if key not in obj]
    if missing:
        raise AssertionError(f"{label}: missing required keys: {', '.join(missing)}")


def validate_boundary_artifact(path_name):
    data = load_json(path_name)
    require_keys(
        data,
        ["artifact_type", "artifact_version", "artifact_id", "issuer", "purpose", "authority_scope"],
        path_name,
    )
    scope = data["authority_scope"]
    if not isinstance(scope, dict):
        raise AssertionError(f"{path_name}: authority_scope must be an object")
    require_keys(scope, ["inherits_authority_from", "grants_authority_to"], f"{path_name}.authority_scope")
    if not isinstance(scope["inherits_authority_from"], list):
        raise AssertionError(f"{path_name}: inherits_authority_from must be a list")
    if not isinstance(scope["grants_authority_to"], list):
        raise AssertionError(f"{path_name}: grants_authority_to must be a list")


def validate_comparison_fixture(path_name):
    data = load_json(path_name)
    require_keys(data, ["fixture_type", "fixture_version", "test_name", "artifacts", "expected_results"], path_name)
    if not isinstance(data["artifacts"], list) or not data["artifacts"]:
        raise AssertionError(f"{path_name}: artifacts must be a non-empty list")
    for index, artifact in enumerate(data["artifacts"]):
        require_keys(artifact, ["artifact_id", "path", "expected_independently_discoverable"], f"{path_name}.artifacts[{index}]")
        if not isinstance(artifact["expected_independently_discoverable"], bool):
            raise AssertionError(f"{path_name}.artifacts[{index}]: expected_independently_discoverable must be boolean")
    expected = data["expected_results"]
    require_keys(
        expected,
        [
            "authority_inheritance_allowed",
            "interoperability_claim_allowed",
            "external_validity_dependency_allowed",
        ],
        f"{path_name}.expected_results",
    )


def main():
    for path_name in BOUNDARY_ARTIFACTS:
        validate_boundary_artifact(path_name)
    for path_name in COMPARISON_FIXTURES:
        validate_comparison_fixture(path_name)
    print("PASS: boundary artifact and comparison fixture schemas validated.")


if __name__ == "__main__":
    main()
