% INPUT

man(a; b; c).
woman(a; b; c).

mpref(a, a, 1; a, b, 2; a, c, 3).
mpref(b, b, 1; b, c, 2; b, a, 3).
mpref(c, c, 1; c, a, 2; c, b, 3).

wpref(a, b, 1; a, c, 2; a, a, 3).
wpref(b, c, 1; b, a, 2; b, b, 3).
wpref(c, a, 1; c, b, 2; c, c, 3).

% GENERATE

{pair(M, F) : woman(F)} = 1 :- man(M).
:- {pair(M, F) : man(M)} > 1, woman(F).

% DEFINE

% M1 prefers F2 to F1.
mprefer(M, DF, CF) :- mpref(M, CF, CUR), mpref(M, DF, DEV), DEV < CUR.

% F2 prefers M2 to M1.
wprefer(F, DM, CM) :- wpref(F, CM, CUR), wpref(F, DM, DEV),  DEV < CUR.

% TEST

:- man(M1; M2), woman(F1; F2), pair(M1, F1), pair(M2, F2), mprefer(M1, F2, F1), wprefer(F2, M1, M2).

% WEAK CONSTRAINT

:~ pair(M, F), man(M), woman(F), mpref(M, F, R). [R@1, M]
:~ pair(M, F), man(M), woman(F), wpref(F, M, R). [R@2, F]

% SHOW

#show pair/2.
