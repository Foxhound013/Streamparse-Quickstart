# the point of this script is simply to emit words until the end of time (or you end the script)
from itertools import cycle

from streamparse import Spout


class WordSpout(Spout):
    outputs = ['word'] #storm works on tuples, here we're specifying the name of the output fields that will be produced by the stream.

    #stormconf(dict) - storm config for this component, provided by topology.
    #context(dict) - informs the component about where it belongs in the topology.
    def initialize(self, stormconf, context):
        self.words = cycle(['dog', 'cat', 'zebra', 'elephant']) #cycling through a predefined list to infinitely generate words.
        #cycles through these values and sets each one to self.words. This simulates real time data as it is always running and producing a new value

    def next_tuple(self): 
        word = next(self.words) #gets the next value from the initialize self.words section, saves it to word. Next works on an iterator, so it's getting the next value in the cycle.
        self.emit([word]) #the word is being added coerced to a list and sent to the bolt.


#initialize is called, generating a word, followed by next_tuple, pairing the word with it's grouping name and sending it off to the bolt according to the topology.