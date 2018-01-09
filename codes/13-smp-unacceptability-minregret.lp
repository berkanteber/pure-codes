% INPUT
man(a; b; c; d; e; f; g; h).
woman(a; b; c; d; e).

mpref(a, a, 1; a, b, 2; a, c, 2; a, d, 4; a, e, 4).
mpref(b, a, 1; b, b, 2; b, c, 2; b, d, 4; b, e, 4).
mpref(c, a, 1; c, b, 2; c, c, 2; c, d, 4; c, e, 4).
mpref(d, a, 1; d, b, 2; d, c, 3; d, d, 3; d, e, 3).
mpref(e, a, 1; e, b, 2; e, c, 3; e, d, 3; e, e, 3).
mpref(f, a, 1; f, b, 2; f, c, 3; f, d, 3; f, e, 3).
mpref(g, a, 1; g, b, 2; g, c, 3; g, d, 3; g, e, 3).
mpref(h, a, 1; h, b, 2; h, c, 3; h, d, 3; h, e, 3).

wpref(a, a, 1; a, b, 2; a, c, 3; a, d, 3; a, e, 5; a, f, 5; a, g, 7; a, h, 8).
wpref(b, a, 1; b, b, 2).
wpref(c, b, 1; c, a, 2).
wpref(d, a, 1; d, b, 2; d, c, 3; d, d, 4).
wpref(e, a, 4; e, b, 3; e, c, 2, d, d, 1).

% GENERATE

{msingle(M)} :- man(M).
{wsingle(F)} :- woman(F).

{pair(M, F) : woman(F)} = 1 :- man(M), not msingle(M).
:- {pair(M, F) : man(M)} > 1, woman(F).

marriedwoman(F) :- man(M), woman(F), pair(M, F).
:- marriedwoman(F), wsingle(F), woman(F).
:- not wsingle(F), not marriedwoman(F), woman(F).

% DEFINE

% M prefers F to single
m2single(M, F) :- man(M), woman(F), mpref(M, F, X).

% F prefers M to single
w2single(F, M) :- man(M), woman(F), wpref(F, M, X).

% M prefers DF to CF.
mprefer(M, DF, CF) :- mpref(M, CF, CUR), mpref(M, DF, DEV), DEV < CUR.

% F prefers DM to CM.
wprefer(F, DM, CM) :- wpref(F, CM, CUR), wpref(F, DM, DEV),  DEV < CUR.

% TEST

% a pair deviates (4 cases)

% m1-f1, m2-f2 -- m1 and f2 deviate to m1-f2
:- man(M1; M2), woman(F1; F2), pair(M1, F1), pair(M2, F2), mprefer(M1, F2, F1), wprefer(F2, M1, M2).

% m-f1, f2 single -- m and f2 deviate to m-f2
:- man(M), woman(F1; F2), pair(M, F1), wsingle(F2), mprefer(M, F2, F1), wpref(F2, M, X).

% m1-f, m2 single -- m2 and f deviate to m2-f
:- man(M1; M2), woman(F), pair(M1, F), msingle(M2), wprefer(F, M2, M1), mpref(M2, F, X).

% m, f single -- m and f deviate to m-f
:- man(M), woman(F), msingle(M), wsingle(F), mpref(M, F, X), wpref(F, M, Y).

% an individual deviates (2 cases)

% m-f -- m deviates to single
:- man(M), woman(F), pair(M, F), not m2single(M, F).

% m-f -- f deviates to single
:- man(M), woman(F), pair(M, F), not w2single(F, M).

% OPTIMIZATION

% pair rank

mrank(M, R) :- pair(M, F), mpref(M, F, R).
wrank(F, R) :- pair(M, F), wpref(F, M, R).

% total rank

% ranked(R) :- man(M), mrank(M, R).
% ranked(R) :- woman(F), wrank(F, R).

% maxregret(T) :- ranked(T), not ranked(S), S > T.

regret(man, T) :- T = #max{R, M: mrank(M, R)}.
regret(woman, T) :- T = #max{R, F: wrank(F, R)}.

maxregret(T) :- T = #max{R: regret(X, R)}.

% weak constraint

:~ maxregret(R). [R]

% SHOW

#show pair/2.
#show regret/2.
#show maxregret/1.
