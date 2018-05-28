%OPTIMIZATION
mancost(M ,K):-marry(M, W), mrank(M, W, K).
womancost(W, K):-marry(M, W), wrank(W, M, K).
mancost(M, T) :- T= #max{R: mrank(M,_, R)}, msingle(M).
womancost(W, T) :- T= #max{R: wrank(W, _, R)}, wsingle(W).


regret(R1;R2) :- mancost(M, R1), womancost(W, R2).
:~ T = #max{R: regret(R)}, T > #inf. [T]
