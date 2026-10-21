import subprocess
import sys
from pathlib import Path


def test_train_script_runs():
    script = Path(__file__).with_name("train.py")
    result = subprocess.run(
        [sys.executable, str(script)],
        check=True,
        capture_output=True,
        text=True,
    )

    assert result.stdout.strip() == "Hi, This is my first time : )"
