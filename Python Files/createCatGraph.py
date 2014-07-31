#-------------------------------------------------------------------------------
# Name:        createCatGraph
# Purpose:     create a graph to render in Gephi
#
# Author:      Animesh Pandey
#
# Created:     21/07/2014
# Copyright:   (c) Animesh Pandey 2014
#-------------------------------------------------------------------------------

import csv
import networkx as nx
import itertools

G = nx.Graph()

def csv_reader(path):
    with open(path, 'rb') as f:
        content = csv.reader(f)
        content_list = [row for row in content]

    return content_list

def removeRedundancy(k):
    import itertools
    return list(k for k,_ in itertools.groupby(k))

def add_node_cat(category, weight = None):
    if not G.has_node(category):
        G.add_node(category)
        G.node[category]['weight'] = weight
    else:
        pass

def add_edge_cat(cat1, cat2, weight = None):
    if not G.has_edge(cat1, cat2):
        G.add_edge(cat1, cat2)
        G[cat1][cat2]['weight'] = 1
    else:
        G[cat1][cat2]['weight'] += 1

def put_in_edge(allPatterns, allNodes):
    for n in allNodes:
        for p in allPatterns:
            if n in p:
                for t in p:
                    if t != n:
                        add_edge_cat(n, t)
                    else:
                        pass

def sortDictByValue(x):
    import operator
    sorted_x = sorted(x.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sorted_x

def all_subsets(ss):
    from itertools import chain, combinations
    c = chain(*map(lambda x: combinations(ss, x), range(0, len(ss)+1)))
    return [sets for sets in c]

if __name__ == '__main__':
    pattern_data = csv_reader('dataAndCatPatterns.csv')

    patterns = [(data[-1].split(';'), data[0]) for data in pattern_data]
    spatterns = [sorted(data[-1].split(';')) for data in pattern_data]
    spatterns_uni = removeRedundancy(spatterns)

    all_nodes = set(sum(spatterns_uni, []))

    [add_node_cat(n, sum(spatterns_uni, []).count(n)) for n in all_nodes]

    put_in_edge(spatterns_uni, all_nodes)

    for i in G.edges():
        G[i[0]][i[1]]['weight'] /= 2

    mapping_cat_weight = dict()
    [mapping_cat_weight.update({g : G.node[g]['weight']}) for g in G.nodes()]
    mapping_cat_weight = sortDictByValue(mapping_cat_weight)

    all_possible_edges = list(itertools.combinations([t[0] for t in mapping_cat_weight if t[1] > 10], 2))

    valid_edges_final = list(set(G.edges()).intersection(all_possible_edges))

    print [G[a][b]['weight'] for a, b in valid_edges_final]

    H = nx.Graph()
    for a,b in valid_edges_final:
        H.add_edge(a, b)
        H[a][b]['weight'] = G[a][b]['weight']


    nx.write_graphml(H, "categories4.graphml")
