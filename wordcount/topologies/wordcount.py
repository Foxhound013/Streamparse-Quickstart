"""
Word count topology
"""

from streamparse import Grouping, Topology

from bolts.wordcount import WordCountBolt
from spouts.words import WordSpout


class WordCount(Topology):
    word_spout = WordSpout.spec() # spec sets the specification of a spout or bolt. can take a name, par, and config argument.
    count_bolt = WordCountBolt.spec(inputs={word_spout: Grouping.fields('word')}, par=2) # par refers to the number of parallel processes for that operation.
