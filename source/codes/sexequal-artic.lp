
% OPTIMIZE
mancost(M ,K):-marry(M, W),mrank(M, W, K).
womancost(W, K):-marry(M, W),wrank(W, M, K).
mancost(M, T):- T = #max{R: mrank(M, _, R)}, msingle(M), T>#inf.
womancost(W, T):- T = #max{R: wrank(W, _, R)},wsingle(W), T>#inf.
mantotal(T):- T =  #sum{R , M: mancost(M, R)}.
womantotal(T):- T= #sum{R , W: womancost(W, R)}.
:~ T = |M - W|, mantotal(M), womantotal(W). [T]


