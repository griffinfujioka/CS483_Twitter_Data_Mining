"""
CptS 483
Twitter Flu graph 
------------------
Generate a directed multigraph over the twitter data in the file
flu-vac_string.edgelist.

The lines are formatted as:
        [source] [target] [tweet_count]

Two tweets are connected by an edge between the source and target
users. 
"""
__author__ = """\n""".join(['Griffin Fujioka (fujiokag@hotmail.com)'])


import networkx as nx
import shlex            # for parsing lines of text
import matplotlib.pyplot as plt

g=nx.Graph()        # Create an empty graph

# Open the data file for reading 
file=open('flu-vac_string.edgelist-short', 'r')
i = 0
counter = 0
temp = 0
while 1:
    line = file.readline()
    if not line:
        break       # We've read in all lines from the file 
    else:
        nodes_array = g.nodes()   # Get all nodes currently in the graph
        tweet = shlex.split(line)
        source = tweet[0]
        target = tweet[1]
        tweetCountAsString = tweet[2]
        #print 'tweetCountAsString = ' + tweetCountAsString
        tweetCount = int(tweet[2])  # Get integer value of tweetCount
        

        if source in nodes_array:
            if target in nodes_array:

                # Check to see if an edge already exists. If so, get its weight
                g.add_edge(source, target, weight=tweetCount)
                #print 'Edge added from ' + source + ' to ' + target
            else:
                g.add_node(target)      # We must add the target node first
                g.add_edge(source, target, weight=tweetCount)
                #print 'Added node ' + target + '. Edge added from ' + source + ' to ' + target
        else:
            g.add_node(source)
            if target in nodes_array:
                g.add_edge(source, target, weight=tweetCount)
                #print 'Edge added from ' + source + ' to ' + target
            else:
                g.add_node(target)      # We must add the target node first
                g.add_edge(source, target, weight=tweetCount)
                #print 'Added node ' + target + '. Edge added from ' + source + ' to ' + target
                   

nx.draw(g)
plt.savefig("graph.png")

