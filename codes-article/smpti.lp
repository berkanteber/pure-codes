% DEFINITONS

maccept(M,W) :- mpref(M,W,_), W != s.
waccept(W,M) :- wpref(W,M,_), M != s.

mmagnitude(M, X) :- mpref(M, s, X), man(M).
wmagnitude(W, X) :- wpref(W, s, X), woman(W).

% GENERATE

accept(M,W) :- manpropose(M,W), womanpropose(M,W).

accept(M,M) :- man(M), not accept(M,W) : maccept(M,W).
accept(W,W) :- woman(W), not accept(M,W) : waccept(W,M).

manpropose(M,W) :- man(M), woman(W), mpref(M,W,H), mmagnitude(M, MM), H < MM, not accept(M,X) : maccept(M,X), mpref(M,X,L), L <= H, W != X.
manpropose(M,W) :- man(M), woman(W), mpref(M,W,H), mmagnitude(M, MM), H = MM, not accept(M,M), not accept(M,X) : maccept(M,X), mpref(M,X,L), L <= H, W != X.

womanpropose(M,W) :- man(M), woman(W), wpref(W,M,H), wmagnitude(W, WW), H < WW, not accept(X,W) : waccept(W,X), wpref(W,X,L), L <= H, M != X.
womanpropose(M,W) :- man(M), woman(W), wpref(W,M,H), wmagnitude(W, WW), H = WW, not accept(W,W), not accept(X,W) : waccept(W,X), wpref(W,X,L), L <= H, M != X.

% SHOW

#show accept/2.
