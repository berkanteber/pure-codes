% CONSTRUCT THE SETTING
table(1..n).
person(1..m*n).

% INPUT
sitTogether(1; 3; 5).
sitAway(2; 4).

% GENERATE
{sit(P, T) : person(P)} = m :- table(T).
:- {sit(P, T) : table(T)} > 1, person(P).

% TEST
:- sitTogether(P1), sitTogether(P2), P1 != P2, sit(P1, T1), sit(P2, T2), T1 != T2.
:- sitAway(P1), sitAway(P2), P1 != P2, sit(P1, T1), sit(P2, T2), T1 = T2.

% SHOW
#show sit/2.
