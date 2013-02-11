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

g=nx.Graph()        # Create an empty graph

file=open('flu-vac_string.edgelist', 'r')


while 1:
    line = file.readline()
    if not line:
        break
    else: tweet = shlex.split(line)
    #g.add_node(tweet)       # Add each tweet to the graph as a node
    print 'Source: ' + tweet[0]
    print 'Target: ' + tweet[1]
    print 'tweetCount: ' + tweet[2]
    print ''

