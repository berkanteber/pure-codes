

% OPTIMIZE
mancost(M ,K):-marry(M, W),mrank(M, W, K).
womancost(W, K):-marry(M, W),wrank(W, M, K).
mancost(M, T):- T = #max{R: mrank(M,_,R)}, msingle(M), T>#inf.
womancost(W, T):- T = #max{R: wrank(W,_,R)}, wsingle(W), T>#inf.

:~ T = #sum{R1, M: mancost(M, R1)}. [T]
:~ T = #sum{R2, F: womancost(F, R2)}. [T]
