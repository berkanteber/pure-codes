% DEFINITIONS

maccept(M,W) :- mrank(M,W,_), man(M), woman(W).
waccept(W,M) :- wrank(W,M,_), man(M), woman(W).

% GENERATE

marry(M,W) :- manpropose(M,W), womanpropose(W,M).

manpropose(M,W) :- man(M), maccept(M,W), mrank(M,W,H),
  {marry(M,X) : maccept(M,X), mrank(M,X,L), L <= H, W != X}0.
womanpropose(W,M) :- woman(W), waccept(W,M), wrank(W,M,H),
  {marry(X,W) : waccept(W,X), wrank(W,X,L), L <= H, M != X}0.

msingle(M) :- man(M), not marry(M,W) : maccept(M,W).
wsingle(W) :-  woman(W), not marry(M,W) : waccept(W,M).

% SHOW

#show marry/2.
#show msingle/1.
#show wsingle/1.
