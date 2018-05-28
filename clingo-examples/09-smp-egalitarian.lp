% INPUT
man(a; b).
woman(a; b).

mpref(a, a, 1; a, b, 2).
mpref(b, b, 1; b, a, 2).

wpref(a, a, 1; a, b, 2).
wpref(b, b, 1; b, a, 2).

% GENERATE

{pair(M, F) : woman(F)} = 1 :- man(M).
:- {pair(M, F) : man(M)} > 1, woman(F).

% DEFINE

% M prefers DF to CF.
mprefer(M, DF, CF) :- mpref(M, CF, CUR), mpref(M, DF, DEV), DEV < CUR.

% F prefers DM to CM.
wprefer(F, DM, CM) :- wpref(F, CM, CUR), wpref(F, DM, DEV),  DEV < CUR.

% TEST

:- man(M1; M2), woman(F1; F2), pair(M1, F1), pair(M2, F2), mprefer(M1, F2, F1), wprefer(F2, M1, M2).

% OPTIMIZE

mrank(M, R) :- pair(M, F), mpref(M, F, R).
wrank(F, R) :- pair(M, F), wpref(F, M, R).

mtot(T) :- T = #sum{R, M: mrank(M, R)}.
wtot(T) :- T = #sum{R, F: wrank(F, R)}.

:~ mtot(M), wtot(F). [M+F]

% SHOW

#show pair/2.
#show mtot/1.
#show wtot/1.
