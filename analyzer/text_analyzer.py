# coding=utf-8
__date__ = "29 September 2022"

import logging
from dataclasses import dataclass

import nltk
from nltk import RegexpTokenizer

from analyzer.config import settings

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class TextAnalyzer:
    """
    Analyze arbitrary text.

    Attributes:
        text (str):
            The text to analyze.
        ngram_size (int):
            The size of the sequences you're interested in. The default is three.
        top_count (int):
            When analyzing the text, top_count controls the number of results you see. The default is 100.
    """

    text: str
    ngram_size: int = settings.ngram_size
    top_count: int = settings.top_count

    def __post_init__(self):
        if not self.text:
            raise ValueError("You must specify the text to analyze.")

    def _tokenize(self) -> list[str]:
        """
        Tokenize a string.

        Returns:
            list[str]: a list of string tokens.
        """
        tokenizer = RegexpTokenizer(settings.tokenizer_regex)
        tokens = tokenizer.tokenize(self.text)
        logger.info("Found %d tokens", len(tokens))
        return [token.lower() for token in tokens]

    def _most_common(self, freq_dist: nltk.FreqDist) -> list[tuple]:
        """
        Find the most common occurrences in a `nltk.FreqDist`.

        Args:
            freq_dist (nltk.FreqDist): A `nltk.FreqDist` object.

        Returns:
             list[tuple]: A list of tuples containing the count data.
                          Index 0 contains a tuple with the text fragments. The number of
                            fragments is equal to ngram_size.
                          Index 1 contains the number of times the fragment was found.
        """
        _count = self.top_count
        logger.debug("Count is %d", _count)
        return freq_dist.most_common(_count)

    def _display(self, data: list[tuple]):
        """
        Display the count data.

        Args:
            list[tuple]: A list of tuples containing the count data. See `_most_common`.
        """
        for d in data:
            _fragment = " ".join([str(x) for x in d[settings.fragment_index]])
            _count = d[settings.count_index]
            print(f"{_fragment} - {_count}")

    def find_most_common(self):
        """
        Find the most common occurrences of words or phrases in a body of text.
        """
        tokens = self._tokenize()
        ngrams = nltk.ngrams(tokens, self.ngram_size)

        most_common = self._most_common(nltk.FreqDist(ngrams))
        logger.debug("Most common: %s", most_common)
        self._display(most_common)
