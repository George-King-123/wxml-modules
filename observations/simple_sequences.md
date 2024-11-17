Call a set of $S$ of $m$-tuples of elements of $\mathbb{P}^d(F_q)$ "simple" if it contains a subset $C \subseteq S$ with $|C| = |\mathbb{P}^d(F_q)|$ such that all elements of $C$ have $m-1$ indices in common (and then necessarily they differ at the other index, and points occupying that index in $C$ run over all elements of $\mathbb{P}^d(F_q)$). 

Call a (potentially truncated) multilinearly uniformly recurrent sequence of points in $\mathbb{P}^d(F_q)$ simple if it satisfies the contraints of an MUR sequence only with simple sets.

For $n = 6, q = 2, d = 1$ here is a map from length to number of sequences for simple sequences\
{0: 1, 1: 3, 2: 9, 3: 27, 4: 81, 5: 243, 6: 540, 7: 1440, 8: 3804, 9: 9960, 10: 25908, 11: 67344, 12: 84510, 13: 112038, 14: 215730, 15: 427338, 16: 850578, 17: 1749768, 18: 404682, 19: 182400, 20: 65532, 21: 68880, 22: 78684, 23: 83928, 24: 504, 25: 36, 26: 0}


And for all sequences (of course, these numbers are larger). What is interesting is that they both fail at $26$, one might expect the simple ones to fail much sooner.\
{0: 1, 1: 3, 2: 9, 3: 27, 4: 81, 5: 243, 6: 540, 7: 1440, 8: 3804, 9: 9960, 10: 25908, 11: 67344, 12: 91362, 13: 129894, 14: 255294, 15: 510762, 16: 1017870, 17: 2099826, 18: 507318, 19: 229338, 20: 89472, 21: 92478, 22: 105252, 23: 109098, 24: 816, 25: 48, 26: 0}

For reference, it took $48$ seconds to compute the simple sequences and $400$ seconds for the non-simple ones.