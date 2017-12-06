% CONSTRUCT GRAPH
vertex(1..6).

edge(1, 2; 1, 3).
edge(2, 1; 2, 3; 2, 4; 2, 5).
edge(3, 1; 3, 2; 3, 5; 3, 6).
edge(4, 2; 4, 5).
edge(5, 2; 5, 3; 5, 4; 5, 6).
edge(6, 3; 6, 5).

% GENERATE
{clique(V) : vertex(V)} = k.

% TEST
:- clique(U), clique(V), U != V, not edge(U, V).
:~ not clique(6).[1@1, 6]
:~ not clique(4).[1@1, 4]

% SHOW
#show clique/1.
