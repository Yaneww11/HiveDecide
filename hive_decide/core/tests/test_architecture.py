"""Guards the rule that `core` stays independent of Django and the apps.

`core` lives inside the `hive_decide` project package, so the only allowed
imports from that package are other `hive_decide.core` modules.
"""

import ast
from pathlib import Path

CORE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR = CORE_DIR.parent.parent
CORE_PACKAGE = "hive_decide.core"
FORBIDDEN_ROOTS = {"django", "ninja"}


def module_name(path: Path) -> str:
    parts = path.relative_to(PROJECT_DIR).with_suffix("").parts
    return ".".join(parts[:-1] if parts[-1] == "__init__" else parts)


def imported_modules(source: str, package: str) -> set[str]:
    """Absolute names of every module imported by `source`, which lives in `package`."""
    modules: set[str] = set()
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Import):
            modules.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            if node.level == 0:
                modules.add(node.module or "")
            else:
                base = package.split(".")[: len(package.split(".")) - node.level + 1]
                modules.add(".".join([*base, *([node.module] if node.module else [])]))
    return modules


def is_forbidden(module: str) -> bool:
    if module.split(".")[0] in FORBIDDEN_ROOTS:
        return True
    in_project = module == "hive_decide" or module.startswith("hive_decide.")
    in_core = module == CORE_PACKAGE or module.startswith(CORE_PACKAGE + ".")
    return in_project and not in_core


def test_core_imports_nothing_from_django_or_the_apps() -> None:
    violations: dict[str, list[str]] = {}
    for path in CORE_DIR.rglob("*.py"):
        if "tests" in path.relative_to(CORE_DIR).parts:
            continue
        name = module_name(path)
        package = name if path.name == "__init__.py" else name.rpartition(".")[0]
        forbidden = sorted(
            m for m in imported_modules(path.read_text(), package) if is_forbidden(m)
        )
        if forbidden:
            violations[str(path.relative_to(CORE_DIR))] = forbidden
    assert violations == {}
