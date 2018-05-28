% DEFINITIONS

maccept(M,W) :- mrank(M,W,_), W != s.
waccept(W,M) :- wrank(W,M,_), M != s.

msinglepref(M, X) :- mrank(M, s, X), man(M).
wsinglepref(W, X) :- wrank(W, s, X), woman(W).

% GENERATE

accept(M,W) :- manpropose(M,W), womanpropose(M,W).

msingle(M) :- man(M), not accept(M, W) : maccept(M, W).
wsingle(W) :-  woman(W), not accept(M, W) : waccept(W, M).

manpropose(M, W) :- man(M), mrank(M, W, H), msinglepref(M, MM), H < MM,  not accept(M,X) : maccept(M,X), mrank(M,X,L), L <= H, W != X.
manpropose(M, W) :- man(M), mrank(M,W,H),  W!=s,  msinglepref(M, MM), H = MM, not msingle(M), not accept(M,X) : maccept(M,X), mrank(M,X,L), L <= H, W != X.

womanpropose(M, W) :- woman(W), wrank(W, M, H), wsinglepref(W, WW), H < WW, not accept(X, W) : waccept(W, X), wrank(W, X, L), L <= H, M != X.
womanpropose(M, W) :- woman(W), wrank(W, M, H), M!=s, wsinglepref(W, WW), H = WW, not wsingle(W), not accept(X, W) : waccept(W, X), wrank(W, X, L), L <= H, M != X.

% SHOW

#show accept/2.
#show msingle/1.
#show wsingle/1.
