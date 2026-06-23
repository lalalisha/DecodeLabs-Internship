"""
Unit tests for rulebot.py
Run with: python -m pytest tests/ -v
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rulebot import get_response


# ── Exit detection ─────────────────────────────────────────────────────────────

def test_exit_bye():
    _, should_exit = get_response("bye")
    assert should_exit is True

def test_exit_goodbye():
    _, should_exit = get_response("goodbye")
    assert should_exit is True

def test_exit_quit():
    _, should_exit = get_response("quit")
    assert should_exit is True

def test_no_exit_on_normal_input():
    _, should_exit = get_response("hello")
    assert should_exit is False


# ── Greeting rule ──────────────────────────────────────────────────────────────

def test_greeting_hello():
    response, _ = get_response("hello")
    assert isinstance(response, str) and len(response) > 0

def test_greeting_hey():
    response, _ = get_response("hey there")
    assert isinstance(response, str) and len(response) > 0

def test_greeting_good_morning():
    response, _ = get_response("good morning!")
    assert isinstance(response, str) and len(response) > 0


# ── Time / date ────────────────────────────────────────────────────────────────

def test_time_response():
    response, _ = get_response("what time is it")
    # Should mention AM or PM
    assert "AM" in response or "PM" in response

def test_date_response():
    response, _ = get_response("what is today's date")
    assert isinstance(response, str) and len(response) > 0


# ── Joke rule ──────────────────────────────────────────────────────────────────

def test_joke():
    response, _ = get_response("tell me a joke")
    assert isinstance(response, str) and len(response) > 0

def test_funny():
    response, _ = get_response("say something funny")
    assert isinstance(response, str) and len(response) > 0


# ── Help rule ──────────────────────────────────────────────────────────────────

def test_help():
    response, _ = get_response("help")
    assert "Greetings" in response or "greetings" in response.lower()


# ── Default (no match) ─────────────────────────────────────────────────────────

def test_no_match_returns_fallback():
    response, should_exit = get_response("xyzzy frobulate quux")
    assert should_exit is False
    assert "help" in response.lower()

def test_empty_input_is_safe():
    # Empty string should not crash; behaviour is fallback
    response, should_exit = get_response("   ")
    assert isinstance(response, str)
    assert should_exit is False


# ── Motivation / facts ─────────────────────────────────────────────────────────

def test_motivation():
    response, _ = get_response("motivate me")
    assert isinstance(response, str) and len(response) > 0

def test_fun_fact():
    response, _ = get_response("tell me a fun fact")
    assert isinstance(response, str) and len(response) > 0


# ── Case insensitivity ─────────────────────────────────────────────────────────

def test_uppercase_input():
    response, _ = get_response("HELLO")
    assert isinstance(response, str) and len(response) > 0

def test_mixed_case_input():
    response, _ = get_response("HeLLo ThErE")
    assert isinstance(response, str) and len(response) > 0
