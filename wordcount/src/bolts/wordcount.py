import os
from collections import Counter

from streamparse import Bolt


class WordCountBolt(Bolt):
    outputs = ['word', 'count']

    def initialize(self, conf, ctx):
        self.counter = Counter() #Counter is a dictionary {(tuple of interest): value}, in this case value is the count of that word in the tuple
        self.pid = os.getpid() #Just gets the process ID, this is for display at end and has no bearing on the Bolt's operation
        self.total = 0

    def _increment(self, word, inc_by):
        self.counter[word] += inc_by #access the dictionary value corresponding to word in the counter dictionary and increment it by 1
        self.total += inc_by #keeps track of total increments

    #process is always called when a tuple has been emitted by an incoming spout (or bolt, but it's a spout in this case).
    #any processing desired can be done here. Tuples can be emitted again here if one wants.
    def process(self, tup):
        word = tup.values[0] #gets the first value in the tuple, there doesn't appear to be any other values in the tuple in this example.
        self._increment(word, 10 if word == "dog" else 1) #applies the increment method based on the word given by the tuple from the spout.
        if self.total % 1000 == 0: #logs the data to the console every 1000 increments (roughly)
            self.logger.info("counted [{:,}] words [pid={}]".format(self.total, self.pid))
            #self.logger.info(word) # can use this line to see what word is being counted at each increment
        self.emit([word, self.counter[word]]) #emits the word and the count
