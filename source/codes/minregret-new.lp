% OPTIMIZATION

regret(R1;R2) :- marry(M, F), mrank(M, F, R1), wrank(F, M, R2).
:~ T = #max{R: regret(R)}, T > #inf. [T]
