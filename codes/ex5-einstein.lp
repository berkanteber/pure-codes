% INPUT

house(blue; green; red; white; yellow).
person(dane; english; german; norwegian; swede).

cigarette(blend; bluemasters; dunhills; pallmall; prince).
drink(bier; coffee; milk; tea; water).
pet(bird; cat; dog; fish; horse).

% GENERATE

{lives(P, H) : house(H)} = 1 :- person(P).
:- {lives(P, H) : person(P)} > 1, house(H).

{drinks(P, D) : drink(D)} = 1 :- person(P).
:- {drinks(P, D) : person(P)} > 1, drink(D).

{smokes(P, C) : cigarette(C)} = 1 :- person(P).
:- {smokes(P, C) : person(P)} > 1, cigarette(C).

{keeps(P, A) : pet(A)} = 1 :- person(P).
:- {keeps(P, A) : person(P)} > 1, pet(A).

index(1..5).
{order(H, I) : index(I)} = 1 :- house(H).
:- {order(H, I) : house(H)} > 1, index(I).

% TEST

% 1
:- not lives(english, red).

% 2
:- not keeps(swede, dog).

% 3
:- not drinks(dane, tea).

% 4
:- order(green, X), order(white, Y), X != Y - 1.

% 5
:- person(P), lives(P, green), not drinks(P, coffee).

% 6
:- person(P), smokes(P, pallmall), not keeps(P, bird).

% 7
:- person(P), lives(P, yellow), not smokes(P, dunhills).

% 8
:- person(P), house(H), lives(P, H), order(H, 3), not drinks(P, milk).

% 9
:- house(H), lives(norwegian, H), not order(H, 1).

% 10
:- person(P1), smokes(P1, blend), house(H1), lives(P1, H1), order(H1, X), person(P2), keeps(P2, cat), house(H2), lives(P2, H2), order(H2, Y), |X - Y| != 1.

% 11
:- person(P), drinks(P, bier), not smokes(P, bluemasters).

% 12
:- person(P1), keeps(P1, horse), house(H1), lives(P1, H1), order(H1, X), person(P2), smokes(P2, dunhills), house(H2), lives(P2, H2), order(H2, Y), |X - Y| != 1.

% 13
:- not smokes(german, prince).

% 14
:- house(H), lives(norwegian, H), order(H, X), order(blue, Y), |X - Y| != 1.

% 15
:- person(P1), smokes(P1, blend), house(H1), lives(P1, H1), order(H1, X), person(P2), drinks(P2, water), house(H2), lives(P2, H2), order(H2, Y), |X - Y| != 1.

% SHOW

answer(P) :- person(P), keeps(P, fish).
#show answer/1.
