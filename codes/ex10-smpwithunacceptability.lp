% INPUT
man(a; b; c).
woman(a; b; c).

mpref(a, a, 1; a, b, 2; a, c, 3).
mpref(b, a, 1; b, b, 2; b, c, 3).
mpref(c, a, 1; c, b, 2; c, c, 3).

wpref(a, a, 1; a, b, 2).
wpref(b, a, 1).
wpref(c, a, 1; c, b, 2).

% GENERATE

{msingle(M) : man(M)} < 3.
:- man(M), woman(F), msingle(M), pair(M, F).

{wsingle(F) : woman(F)} < 3.
:- man(M), woman(F), wsingle(F), pair(M, F).

{pair(M, F) : woman(F)} = 1 :- man(M), not msingle(M).
:- {pair(M, F) : man(M)} != 1, woman(F), not wsingle(F).
:- {pair(M, F) : man(M)} != 0, woman(F), wsingle(F).

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

% SHOW

#show pair/2.
#show msingle/1.
#show wsingle/1.
