import ast
from pathlib import Path

APP_ROOT = Path(__file__).parents[2] / "app"


def imported_modules(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    modules: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            modules.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            modules.add(node.module)
    return modules


def python_modules(layer: str) -> set[str]:
    modules: set[str] = set()
    for path in (APP_ROOT / layer).glob("*.py"):
        modules.update(imported_modules(path))
    return modules


def test_controller_does_not_bypass_service_layer() -> None:
    modules = python_modules("controllers")
    assert not any(module.startswith("app.repositories") for module in modules)
    assert any(module.startswith("app.services") for module in modules)


def test_service_does_not_import_controller_layer() -> None:
    modules = python_modules("services")
    assert not any(module.startswith("app.controllers") for module in modules)
    assert any(module.startswith("app.repositories") for module in modules)


def test_repository_does_not_depend_on_upper_layers() -> None:
    modules = python_modules("repositories")
    forbidden = ("app.controllers", "app.services")
    assert not any(module.startswith(forbidden) for module in modules)

