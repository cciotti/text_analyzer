# coding=utf-8
__date__ = "29 September 2022"

import contextlib
import io
import logging

import pytest

from analyzer.text_analyzer import TextAnalyzer
from tests.conftest import does_not_raise

logger = logging.getLogger(__name__)


class TestTextAnalyzer:
    @pytest.mark.parametrize(
        "data,token_count",
        [
            ("The quick brown fox jumps over the lazy dog", 9),
            ("Foo ? Bar ! Baz.", 3),
            ("Who's line is it anyway?", 5),
        ],
        ids=["simple_count", "ignore_punctuation", "allow_apostrophe"],
    )
    def test_tokenize(self, data, token_count):
        ta = TextAnalyzer(data)
        tokens = ta._tokenize()
        assert tokens is not None
        assert type(tokens) is list
        assert len(tokens) == token_count

    def test_display(self):
        ta = TextAnalyzer("ignore me")
        data = [(("Foo", "bar", "baz"), 3)]
        expected = "Foo bar baz - 3\n"
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            ta._display(data)
            assert out.getvalue() == expected

    @pytest.mark.parametrize(
        "data,expectation,ngram_size,top_count,output",
        [
            ("test_data", does_not_raise(), 3, 3, "ipsum dolor sit - 3\nlorem ipsum dolor - 2\ndolor sit amet - 1\n"),
            ("test_data", does_not_raise(), 2, 3, "ipsum dolor - 4\ndolor sit - 3\nlorem ipsum - 2\n"),
            ("bad_test_data", pytest.raises(ValueError), 1, 1, None),
        ],
        ids=["trigram", "bigram", "error"],
    )
    def test_find_most_common(self, data, expectation, ngram_size, top_count, output, request):
        with expectation:
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                ta = TextAnalyzer(request.getfixturevalue(data), ngram_size, top_count)
                ta.find_most_common()
                assert out.getvalue() == output
