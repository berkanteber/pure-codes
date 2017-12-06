vertex(1..11).

edge(1, 2; 1, 3).
edge(2, 1; 2, 3; 2, 4).
edge(3, 1; 3, 2; 3, 4; 3, 7).
edge(4, 2; 4, 3; 4, 6).
edge(5, 6).
edge(6, 4; 6, 5).
edge(7, 3; 7, 8; 7, 10).
edge(8, 7; 8, 9; 8, 10).
edge(9, 8).
edge(10, 7; 10, 8; 10, 11).
edge(11, 10).

color(red; green; blue).

{map(V, C) : color(C)} = 1 :- vertex(V).

:- edge(X, Y), map(X, C), map(Y, C), color(C).

:- not map(1, red; 4, red; 9, red; 10, red).
:- not map(3, blue; 5, blue; 8, blue; 11, blue).
:- not map(2, green; 6, green; 7, green).

#show map/2.
