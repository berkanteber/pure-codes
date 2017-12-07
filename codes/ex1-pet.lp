% INPUT

firstname(abner; bruce; chuck; duane).
lastname(engel; foster; gunter; halevy).
pet(cobra; iguana; jackal; llama).

% GENERATE

{fullname(F, L) : firstname(F)} = 1 :- lastname(L).
:- {fullname(F, L) : lastname(L)} > 1, firstname(F).

{map(P, F, L) : fullname(F, L)} = 1 :- pet(P).
:- {map(P, F, L) : pet(P)} > 1, fullname(F, L).

fmap(P, F) :- map(P, F, L), fullname(F, L).
lmap(P, L) :- map(P, F, L), fullname(F, L).

% TEST

% 0
:- petname(P, PN1), petname(P, PN2), PN1 != PN2.

% 1
petname(P, sparky) :- lmap(P, engel), pet(P).
:- fullname(abner, engel).
:- fullname(abner, foster).

% 2
:- fmap(iguana, chuck).
:- fmap(iguana, duane).

% 3
:- lmap(jackal, foster).
:- lmap(cobra, foster).

% 4
petname(P, waggles) :- fmap(P, duane), pet(P).
:- fmap(llama, duane).

% 5
:- fmap(cobra, abner).
:- fullname(abner, gunter).

% 6
:- fullname(bruce, foster).

% 7
:- lmap(iguana, halevy).

% SHOW

#show map/3.
