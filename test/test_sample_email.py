
import sys
import os
import io
# Add 'scr' folder to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../scr')))

import pytest

import sample_email as sml

def test_email_with_user_input_no_at_sign(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('bruce,wayne2wayneenterprises,com'))
    assert sml.get_email_from_input() is None

def test_email_with_user_input_no_dot(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('brucewayne@wayneenterprises,com'))
    assert sml.get_email_from_input() is None

def test_email_with_user_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('bruce.wayne@wayneenterprisescom'))
    assert sml.get_email_from_input() == 'bruce.wayne@wayneenterprisescom'