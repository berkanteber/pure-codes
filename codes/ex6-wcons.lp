vertex(1..4).

edge(1, 2; 1, 3).
edge(2, 1; 2, 3).
edge(3, 1; 3, 2; 3, 4).
edge(4, 3).

color(red; green; blue).

{map(V, C) : color(C)} = 1 :- vertex(V).

:- edge(X, Y), map(X, C), map(Y, C), color(C).

cost(1, 2).
cost(2, 3).
cost(3, 1).
cost(4, 5).

:~ not map(V, red), vertex(V), cost(V, W). [W@1, V]

#show map/2.
