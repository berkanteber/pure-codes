% GENERATE

% M prefers F to single
m2single(M, F) :- man(M), woman(F), mrank(M, F, X).

% F prefers M to single
w2single(F, M) :- man(M), woman(F), wrank(F, M, X).

% acceptability
acceptable(M,F) :- m2single(M, F), w2single(F, M).

{marry(M,F) : woman(F), acceptable(M,F)}1 :- man(M).
:- {marry(M,F) : man(M)} > 1, woman(F).
%:- not wsingle(F), {marry(M,F): man(M)}0, woman(F).

msingle(M) :- man(M), {marry(M,F): woman(F)}0.
wsingle(F) :- woman(F), {marry(M,F): man(M)}0.

% DEFINE

% M prefers DF to CF.
mprefer(M,DF,CF) :- mrank(M,CF,CUR), mrank(M,DF,DEV),
  woman(CF), woman(DF), DEV < CUR.

% F prefers DM to CM.
wprefer(F,DM,CM) :- wrank(F,CM,CUR), wrank(F,DM,DEV),
  man(CM), man(DM), DEV < CUR.

% TEST

% it is assumed that marriage to an acceptable partner is preferred over being single

% m1-f1, m2-f2 -- m1 and f2 block the matching
:- man(M1), man(M2), woman(F1), woman(F2),
   marry(M1,F1), marry(M2,F2),
   mprefer(M1,F2,F1), wprefer(F2,M1,M2).

% m-f1, f2 single -- m and f2 block the matching
:- man(M), woman(F1), woman(F2), acceptable(M,F2),
   wsingle(F2), marry(M,F1), mprefer(M,F2,F1).

% m1-f, m2 single -- m2 and f block the matching
:- man(M1), man(M2), woman(F), acceptable(M2,F),
   msingle(M2), marry(M1,F), wprefer(F,M2,M1).

% m, f single -- m and f block the matching
:- man(M), woman(F), acceptable(M,F),
   msingle(M), wsingle(F).

% SHOW

#show marry/2.
#show msingle/1.
#show wsingle/1.

