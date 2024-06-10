#subclass of dictionary collection 
from collections import defaultdict
#A heap is a binar trees for which every parent node has a value less than or equal to any of its children
from heapq import *

def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    q, seen, mins = [(0,f,())], set(), {f: 0}
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    return float("inf"), None

#Create collection of connections between streets and values for connections
if __name__ == "__main__":
    edges = [
        ("ParkPlace", "Boardwalk", 6),
        ("ParkPlace", "Chambers", 7),
        ("Boardwalk", "Wadsworth", 11),
        ("Boardwalk", "Chambers", 4),
        ("Boardwalk", "Elmwood", 5),
        ("Wadsworth", "Elmwood", 3),
        ("Chambers", "Elmwood", 5),
        ("Chambers", "Franklin", 17),
        ("Elmwood", "Franklin", 3),
        ("Elmwood", "Kipling", 1),
        ("Franklin", "Kipling", 11)
    ]

    print ("=== Dijkstra ===")
    print (edges)
    print ("ParkPlace -> Kipling:")
    #Define in an input which edges to traverse from start to finish
    print (dijkstra(edges, "ParkPlace", "Kipling"))
    #Secone quicker example
    print ("Franklin -> Kipling:")
    print (dijkstra(edges, "Franklin", "Kipling"))