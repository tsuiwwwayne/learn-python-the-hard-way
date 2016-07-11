import pytest
from ex48_advanced_user_input import parser

def test_complete_valid_sentence():
    # input is a sentence with subject, verb and object
    example = parser.parse_sentence([('noun', 'bear'), ('verb', 'eat'),
                                     ('stop', 'the'), ('noun', 'honey')])

    assert example.subject == "bear"
    assert example.verb == "eat"
    assert example.object == "honey"

def test_incomplete_valid_sentence():
    # input is a sentence with verb and object only
    example = parser.parse_sentence([('verb', 'run'), ('direction', 'north')])

    assert example.subject == "player"
    assert example.verb == "run"
    assert example.object == "north"

def test_complete_invalid_sentence():
    # input is a sentence with subject, two consecutive verbs and object
    with pytest.raises(parser.ParserError):
        example = parser.parse_sentence([('noun', 'bear'), ('verb', 'eat'), ('verb', 'eat'),
                                         ('stop', 'the'), ('noun', 'honey')])

def test_incomplete_invalid_sentence():
    # input is only a verb, no subject or object
    with pytest.raises(parser.ParserError):
        example = parser.parse_sentence(('verb', 'eat'))
