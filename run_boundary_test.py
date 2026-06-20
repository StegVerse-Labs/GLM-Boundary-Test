import json
from pathlib import Path

BASE = Path(__file__).resolve().parent

REQUIRED_ARTIFACTS = [
    "organization-index.json",
    "stegverse-boundary-manifest.json",
    "glm-boundary-placeholder.json",
    "boundary-comparison-fixture.json",
]


def load_json(path_name):
    path = BASE / path_name
    if not path.exists():
        return None, f"missing file: {path_name}"
    try:
        return json.loads(path.read_text(encoding="utf-8")), None
    except json.JSONDecodeError as exc:
        return None, f"invalid json in {path_name}: {exc}"


def authority_scope_errors(artifact, path_name):
    errors = []
    scope = artifact.get("authority_scope")
    if not isinstance(scope, dict):
        return [f"{path_name}: missing authority_scope"]

    if scope.get("inherits_authority_from") != []:
        errors.append(f"{path_name}: authority inheritance detected")
    if scope.get("grants_authority_to") != []:
        errors.append(f"{path_name}: delegated authority detected")
    return errors


def incomplete_errors(artifact, path_name):
    errors = []
    if "authority_scope" not in artifact:
        errors.append(f"{path_name}: missing authority_scope")
    if path_name != "organization-index.json":
        if "claims" not in artifact:
            errors.append(f"{path_name}: missing claims")
        if "non_claims" not in artifact:
            errors.append(f"{path_name}: missing non_claims")
    return errors


def evaluate():
    loaded = {}
    incomplete = []
    failures = []

    for path_name in REQUIRED_ARTIFACTS:
        artifact, error = load_json(path_name)
        if error:
            incomplete.append(error)
            continue
        loaded[path_name] = artifact
        incomplete.extend(incomplete_errors(artifact, path_name))
        failures.extend(authority_scope_errors(artifact, path_name))

    fixture = loaded.get("boundary-comparison-fixture.json")
    if fixture:
        expected = fixture.get("expected_results", {})
        if expected.get("authority_inheritance_allowed") is not False:
            failures.append("fixture: authority inheritance must be denied")
        if expected.get("interoperability_claim_allowed") is not False:
            failures.append("fixture: interoperability by adjacency must be denied")
        if expected.get("external_validity_dependency_allowed") is not False:
            failures.append("fixture: external validity dependency must be denied")

    org_index = loaded.get("organization-index.json")
    if org_index:
        review = org_index.get("review_posture", {})
        if review.get("requires_external_manifest_to_be_valid") is not False:
            failures.append("organization-index.json: external validity dependency detected")

    if incomplete:
        return {
            "top_level_outcome": "INCOMPLETE",
            "boundary_checks": "NOT_RUN",
            "reasons": incomplete,
        }

    if failures:
        return {
            "top_level_outcome": "FAIL",
            "boundary_checks": "FAIL",
            "reasons": failures,
        }

    return {
        "top_level_outcome": "REVIEW_ONLY",
        "boundary_checks": "PASS",
        "conformance_claim": "NOT_MADE",
        "interoperability_claim": "NOT_MADE",
        "adoption_claim": "NOT_MADE",
        "execution_authority": "NOT_GRANTED",
        "summary": "independently discoverable, independently reviewable, no authority inheritance detected",
    }


def render(result):
    if result["top_level_outcome"] == "REVIEW_ONLY":
        return "\n".join([
            "REVIEW-ONLY: " + result["summary"] + ".",
            "Boundary checks: " + result["boundary_checks"] + ".",
            "Conformance claim: " + result["conformance_claim"] + ".",
            "Interoperability claim: " + result["interoperability_claim"] + ".",
            "Adoption claim: " + result["adoption_claim"] + ".",
            "Execution authority: " + result["execution_authority"] + ".",
        ])

    lines = [f"{result['top_level_outcome']}: Boundary Test could not return REVIEW-ONLY."]
    lines.append("Boundary checks: " + result.get("boundary_checks", "UNKNOWN") + ".")
    for reason in result.get("reasons", []):
        lines.append("- " + reason)
    return "\n".join(lines)


def main():
    print(render(evaluate()))


if __name__ == "__main__":
    main()
