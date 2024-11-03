Note: to run tests just type `python -m unittest` into the terminal

### Runtime Notes

(All of this is for 2 generators)

#### For determining the number of collections of size $s$ that are "good"
- There are $\frac{q^{2^m} - 1}{q-1}$ hypersurfaces of degree $m$ in $(\mathbb{P}^1)^m$, since they can be associated with points in $\mathbb{P}^{2^m - 1}$. We generate them in roughly (*very* roughly) $\Theta(m \cdot \frac{q^{2^m} - 1}{q-1})$ time
- We check if an $m$-tuple lies on a hypersurface in $\Theta(2^m)$ time, since we compute $$
\sum_{i_1, \dots, i_m} \alpha_{i_1, \dots, i_m} \lambda_{i_1} \cdots \lambda_{i_m} $$
which has $2^m$ many terms. Each term can be computed in constant time since we cache a matrix of size $2^m \times 2^m$ which gives the value of each monomial at each point
- So determining the number of collections of size $s$ that are good is $$ {(q + 1)^m \choose s} \cdot \frac{q^{2^m} - 1}{q-1} \cdot 2^m$$