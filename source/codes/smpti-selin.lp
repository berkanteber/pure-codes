2{wed(M, W):women(W),men(M)}2.%map for marriage
:-wed(M,W),wed(M1,W),M!=M1.
:-wed(M,W),wed(M,W1),W!=W1.

mprefer(A,D,B) :- mrank(A,D,R),mrank(A,B,R1),R<R1.
wprefer(D,A,C) :- wrank(D,A,R2),wrank(D,C,R3),R2<R3.
:- wed(A,B), wed(C,D), mprefer(A,D,B), wprefer(D,A,C).

singles(A,B):women(B),men(A).
:-singles(A,B),wed(A,C),women(C).
:-singles(A,C),wed(B,C),men(B).
:- women(A),men(B),mrank(B,A,R),wrank(A,B,R1),singles(A,B).
#show wed/2.
#show singles/2.
