import os
import subprocess
import sys
from pathlib import Path
import pytest

import src.calculator as calculator


def _set_history_env(tmp_path: Path, monkeypatch) -> Path:
    history_file = tmp_path / "history.log"
    monkeypatch.setenv("CALC_HISTORY_FILE", str(history_file))
    monkeypatch.setattr(calculator, "HISTORY_FILE", str(history_file))
    return history_file


def test_basic_operations(tmp_path, monkeypatch):
    _set_history_env(tmp_path, monkeypatch)
    assert calculator.add(2, 3) == 5
    assert calculator.subtract(10, 4) == 6
    assert calculator.multiply(3, 4) == 12
    assert calculator.divide(10, 2) == 5


def test_divide_by_zero(tmp_path, monkeypatch):
    _set_history_env(tmp_path, monkeypatch)
    with pytest.raises(ValueError):
        calculator.divide(1, 0)


def test_invalid_operation(tmp_path, monkeypatch):
    _set_history_env(tmp_path, monkeypatch)
    with pytest.raises(ValueError):
        calculator.calculate("power", 2, 3)


def test_history_records_operations(tmp_path, monkeypatch):
    history_file = _set_history_env(tmp_path, monkeypatch)
    calculator.add(1, 2)
    calculator.subtract(5, 3)
    assert calculator.get_history() == ["1 + 2 = 3", "5 - 3 = 2"]
    assert history_file.read_text().strip().splitlines() == [
        "1 + 2 = 3",
        "5 - 3 = 2",
    ]


def test_cli_add(tmp_path):
    history_file = tmp_path / "cli_history.log"
    env = os.environ.copy()
    env["CALC_HISTORY_FILE"] = str(history_file)
    result = subprocess.run(
        [sys.executable, "main.py", "add", "2", "3"],
        capture_output=True,
        text=True,
        env=env,
        check=True,
    )
    assert float(result.stdout.strip()) == 5.0
    assert history_file.read_text().strip() == "2.0 + 3.0 = 5.0"
