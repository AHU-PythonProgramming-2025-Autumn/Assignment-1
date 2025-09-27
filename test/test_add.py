# tests/test_solution.py
import os
import subprocess
import sys
import src.add as add
from pathlib import Path

def test_add_from_str_basic_1():
    assert add.add_from_str("1 2") == 3

def test_add_from_str_basic_2():
    assert add.add_from_str("0 0") == 0

def test_add_from_str_basic_3():
    assert add.add_from_str("-5 7") == 2

def test_add_from_str_basic_4():
    assert add.add_from_str("10 20") == 30


def test_input_and_print():
    # 测试学生脚本确实能从 stdin 读 input 并输出正确结果
    current_file = Path(__file__).resolve()
    project_root = current_file.parents[1]
    path = os.path.join(project_root, "./src/add.py")
    p = subprocess.run([sys.executable, path],
                       input="123 456\n",
                       text=True,
                       capture_output=True)
    stdout = p.stdout
    assert stdout == "579\n"
    print("\ninput、print功能通过测试！")
