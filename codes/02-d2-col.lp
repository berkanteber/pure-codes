vertex(1..5).

edge(1, 5).
edge(2, 3).
edge(3, 2).
edge(3, 4).
edge(3, 5).
edge(4, 3).
edge(4, 5).
edge(5, 1).
edge(5, 3).
edge(5, 4).

{color(X, 1..k)} = 1 :- vertex(X).

:- edge(X, Y), color(X, C), color(Y, C).
:- edge(X, Y), edge(Y, Z), X != Z, color(X, C), color(Z, C).

#show color/2.
