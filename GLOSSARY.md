# HiveDecide

Group multi-criteria decision making: a group ranks a fixed set of alternatives over several iterations until a group method declares a final result. Each entry gives the Bulgarian term used in the thesis first, then the English name used in code.

## People and roles

**Координатор** (`coordinator`):
The user who creates a task, enters its decision matrix and parameters, and runs its life cycle.
_Avoid_: администратор, фасилитатор, owner

**ЛВР** (`Participant`):
A decision maker of a task: a user with a participant record in it, who submits a ranking in every iteration.
_Avoid_: участник (except for the membership record itself), гласуващ, member

**Участник** (`Participant`):
The membership record that makes a user an ЛВР of one task; every участник is an ЛВР and nobody else is.
_Avoid_: using it for the coordinator when they are not an ЛВР

**Лидер** (`leader`):
Under GCBIM, the coordinator in their role of choosing each iteration's ranking and ending the task; always an ЛВР too.
_Avoid_: storing it as a separate role

## Decision matrix

**Алтернатива** (`Alternative`):
One of the finite set of options the group ranks.
_Avoid_: вариант, option

**Критерий** (`Criterion`):
A dimension along which alternatives are compared, either maximised or minimised.
_Avoid_: атрибут, feature

**Оценка** (`Score`):
The value of one alternative on one criterion: a single cell of the decision matrix.
_Avoid_: стойност; using оценка for a WSM total

**Тегло** (`weight`):
The relative importance an ЛВР gives one criterion in one iteration; an ЛВР's weights sum to 1.
_Avoid_: тежест, приоритет

**Тежест** (`lambda`, λₑ):
The influence of one ЛВР's ranking on the group ranking.
_Avoid_: тегло

## Rankings and results

**Подредба** (`Ranking`):
An ordering of the alternatives, best first, in which alternatives may be tied.
_Avoid_: класиране, order

**Индивидуален резултат** (`individual_result`):
The WSM total of one alternative for one ЛВР in one iteration; it determines the ЛВР's ranking.
_Avoid_: оценка, точки

**Групова подредба** (`group_ranking`):
The ranking obtained by aggregating every ЛВР's ranking in one iteration.
_Avoid_: обща подредба, консенсус

**Групов резултат** (`group_result`):
The Borda or Copeland total of one alternative in one iteration; it determines the group ranking.
_Avoid_: точки, оценка

**Подредба на итерацията** (`chosen_ranking`, P*⁽ʰ⁾):
Under GCBIM, the ranking the leader picks after an iteration closes: the group ranking or any ЛВР's submitted ranking.
_Avoid_: избрано изпращане, лидерска подредба

**Краен резултат** (`final_result`):
The ranking that ends a task: under GCBIM the last ranking chosen by the leader, under BIMBee1 the group ranking of the alternatives that were not eliminated.
_Avoid_: резултат on its own, outcome

**Победител** (`winner`):
The first place of the final result; several alternatives can share it when they are tied.
_Avoid_: избор, избрана алтернатива

## Agreement

**Разстояние** (`distance`, d):
The number of pairs of alternatives that one ЛВР's ranking and the group ranking order in opposite ways.
_Avoid_: отклонение, грешка

**Коефициент на съгласие** (`agreement_coefficient`):
Spearman's ρ or Kendall's τ between one ЛВР's ranking and the group ranking; the coordinator picks one of the two per task.
_Avoid_: мярка (alone), корелация

**Среден коефициент** (`average_coefficient`):
The coefficient of agreement averaged over all ЛВР in one iteration; the group-wide indicator of agreement.

## BIMBee1

**Отпадане** (`elimination`):
Permanently removing the alternatives with the lowest group results after a BIMBee1 iteration.
_Avoid_: изключване, премахване

**Граница** (`boundary`, b_q):
The q-th lowest group result in a BIMBee1 iteration; alternatives at or below it are eliminated unless fewer than t would remain.

## Process

**Задача** (`Task`):
One group decision: a decision matrix, a group method with its parameters, and a group of ЛВР.
_Avoid_: проект, сесия, problem

**Чернова** (`draft`):
Task state in which the matrix, parameters and group can still change and the join code is valid.

**Активна** (`active`):
Task state after start: matrix, methods, parameters and group are locked and iterations run.

**Приключена** (`finished`):
Terminal task state reached through the group method's own stopping rule; it has a final result.
_Avoid_: завършена, closed

**Прекратена** (`cancelled`):
Terminal task state reached when the coordinator stops an active task early; it has no final result.
_Avoid_: изтрита, aborted

**Итерация** (`Iteration`):
One round in which every ЛВР submits a ranking and the rankings are aggregated into a group ranking.
_Avoid_: кръг, рунд, round

**Отворена** (`open`):
Iteration state in which submissions are accepted.

**Затворена** (`closed`):
Iteration state after the last submission: the group ranking is computed and, under GCBIM, the leader has not yet decided.

**Решена** (`resolved`):
Iteration state after the leader's decision (GCBIM) or after elimination (BIMBee1).

**Изпращане** (`Submission`):
An ЛВР's final, irrevocable weights and resulting ranking for one iteration.
_Avoid_: глас, vote

**Моментно състояние** (`snapshot`):
The record of an iteration's outcome, fixed when the iteration closes and never changed afterwards.
_Avoid_: групов резултат, кеш

**Преглед** (`preview`):
Computing a ranking from trial weights without recording anything.
_Avoid_: чернова (reserved for the task state)
