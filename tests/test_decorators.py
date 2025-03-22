import os
import pytest
from src.decorators import log


def test_log_success_console(capsys):
    @log()
    def add(x, y):
        return x + y
    
    result = add(1, 2)
    captured = capsys.readouterr()
    
    assert result == 3
    assert "add ok" in captured.out


def test_log_error_console(capsys):
    @log()
    def divide(x, y):
        return x / y
    
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
    
    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError. Inputs: (1, 0), {}" in captured.out


def test_log_success_file(tmp_path):
    log_file = tmp_path / "test.log"
    
    @log(filename=str(log_file))
    def multiply(x, y):
        return x * y
    
    result = multiply(2, 3)
    
    assert result == 6
    with open(log_file, 'r', encoding='utf-8') as f:
        content = f.read()
    assert "multiply ok" in content


def test_log_error_file(tmp_path):
    log_file = tmp_path / "test_error.log"
    
    @log(filename=str(log_file))
    def raise_error():
        raise ValueError("Test error")
    
    with pytest.raises(ValueError):
        raise_error()
    
    with open(log_file, 'r', encoding='utf-8') as f:
        content = f.read()
    assert "raise_error error: ValueError. Inputs: (), {}" in content 