% OPTIMIZATION

% pair rank

mrank(M, R) :- pair(M, F), mpref(M, F, R).
wrank(F, R) :- pair(M, F), wpref(F, M, R).

% total rank

mtot(T) :- T = #sum{R, M: mrank(M, R)}.
wtot(T) :- T = #sum{R, F: wrank(F, R)}.
ttot(M+F) :- mtot(M), wtot(F).

% weak constraint

:~ ttot(T). [T]

% SHOW

#show mtot/1.
#show wtot/1.
#show ttot/1.
