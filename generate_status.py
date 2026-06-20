import json
from pathlib import Path

BASE = Path(__file__).resolve().parent

REQUIRED_GROUPS = {
    "core_artifacts": [
        "organization-index.json",
        "stegverse-boundary-manifest.json",
        "glm-boundary-placeholder.json",
        "boundary-comparison-fixture.json",
        "five-question-resolution.md",
        "test-plan.md",
    ],
    "sdk_artifacts": [
        "boundary-test-option.json",
        "boundary-test-outcomes.json",
        "sdk-boundary-test.md",
        "boundary-test-user-guide.md",
        "run_boundary_test.py",
    ],
    "verification_artifacts": [
        "verify_boundary_fixture.py",
        "run_boundary_regression.py",
        "validate_boundary_schemas.py",
        "run_example_cases.py",
    ],
    "invalid_control_artifacts": [
        "negative-control-boundary-manifest.json",
        "invalid-control-comparison-fixture.json",
        "invalid-control-notes.md",
    ],
    "schema_artifacts": [
        "schemas/boundary-artifact.schema.json",
        "schemas/comparison-fixture.schema.json",
        "schema-validation.md",
    ],
    "reviewer_artifacts": [
        "reviewer-handoff.md",
        "release-readiness-checklist.md",
        "repository-index.md",
        "boundary-test-manifest.json",
        "release-notes-v0.1.0.md",
        "CHANGELOG.md",
        "VERSION",
    ],
    "ci_artifacts": [
        ".github/workflows/boundary-test.yml",
        "ci-boundary-test.md",
    ],
}


def exists(path_name):
    return (BASE / path_name).exists()


def group_status(files):
    present = [name for name in files if exists(name)]
    missing = [name for name in files if not exists(name)]
    return {
        "present": present,
        "missing": missing,
        "complete": len(missing) == 0,
        "completion_ratio": f"{len(present)}/{len(files)}",
    }


def main():
    groups = {name: group_status(files) for name, files in REQUIRED_GROUPS.items()}
    all_complete = all(group["complete"] for group in groups.values())

    status = {
        "repository": "StegVerse-Labs/Boundary-Test",
        "version": (BASE / "VERSION").read_text(encoding="utf-8").strip() if exists("VERSION") else "UNKNOWN",
        "status": "READY_FOR_REVIEW" if all_complete else "INCOMPLETE",
        "top_level_expected_outcome": "REVIEW_ONLY",
        "boundary_checks_expected": "PASS",
        "invalid_control_expected": "FAIL",
        "groups": groups,
        "non_claims": [
            "GLM conformance",
            "GLM compatibility",
            "GLM adoption",
            "GLM endorsement",
            "runtime interoperability",
            "delegated authority",
            "execution authority",
            "consequence authority",
        ],
    }

    print(json.dumps(status, indent=2))


if __name__ == "__main__":
    main()
