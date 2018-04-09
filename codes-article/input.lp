man(m1;m2).
woman(w1;w2;w3).

mpref(m1,w1,1;m1,w2,2;m1,w3,2;m1,s,3).
mpref(m2,w2,1;m2,w1,2;m2,s,2).

wpref(w1,m1,1;w1,m2,1;w1,s,2).
wpref(w2,m1,1;w2,s,2).
wpref(w3,m2,1;w3,m1,2;w3,s,3).
