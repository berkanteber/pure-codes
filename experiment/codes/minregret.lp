% OPTIMIZATION

% pair rank

mrank(M, R) :- pair(M, F), mpref(M, F, R).
wrank(F, R) :- pair(M, F), wpref(F, M, R).

% total rank

regret(man, T) :- T = #max{R, M: mrank(M, R)}.
regret(woman, T) :- T = #max{R, F: wrank(F, R)}.

maxregret(H) :- regret(_, H), regret(_, L), H > L.

% weak constraint

:~ maxregret(R). [R]

% SHOW

#show regret/2.
#show maxregret/1.
