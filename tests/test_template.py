import os
import subprocess
import tempfile
from pathlib import Path

import pytest


@pytest.fixture
def cookiecutter_template_path():
    """Return the path to the cookiecutter template."""
    return str(Path(__file__).parent.parent)


def test_cookiecutter_creates_project(cookiecutter_template_path):
    """Test if the cookiecutter template successfully creates a project."""
    with tempfile.TemporaryDirectory() as temp_dir:
        project_name = "test_project"

        subprocess.run(
            [
                "uvx",
                "cookiecutter",
                cookiecutter_template_path,
                "--no-input",
                "--output-dir",
                temp_dir,
                f"project_name={project_name}",
            ],
            check=True,
        )

        created_project_path = Path(temp_dir) / project_name
        assert created_project_path.exists(), (
            f"Project directory was not created at {created_project_path}"
        )

        # Verify key files exist
        expected_files = [
            "pyproject.toml",
            ".pre-commit-config.yaml",
            "README.md",
            ".github/workflows/mypy.yml",
            ".github/workflows/pytest.yml",
            ".github/workflows/deptry.yml",
        ]

        for file_path in expected_files:
            full_path = created_project_path / file_path
            assert full_path.exists(), f"Expected file {file_path} does not exist"


def test_generated_project_passes_checks(cookiecutter_template_path):
    """Test if the generated project passes basic checks."""
    with tempfile.TemporaryDirectory() as temp_dir:
        project_name = "test_project"
        subprocess.run(
            [
                "uvx",
                "cookiecutter",
                cookiecutter_template_path,
                "--no-input",
                "--output-dir",
                temp_dir,
                f"project_name={project_name}",
            ],
            check=True,
        )

        project_dir = os.path.join(temp_dir, project_name)

        cwd = os.getcwd()
        os.chdir(project_dir)

        try:
            subprocess.run(["uv", "sync", "--all-extras", "--dev"], check=True)
            subprocess.run(["uv", "run", "mypy", "."], check=True)
            subprocess.run(["uv", "run", "pytest"], check=True)
            subprocess.run(["uv", "run", "deptry", "."], check=True)
        finally:
            os.chdir(cwd)
