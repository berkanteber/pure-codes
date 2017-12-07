number(1..n).
1{q(I, J) : number(I)}1 :- number(J).
:- q(I, J), q(I, K), number(I; J; K), J < K.
:- q(I, J), q(K, L), number(I; J; K; L), I < K, |K - I| == |L - J|.

q(1, 1).

#show q/2.
