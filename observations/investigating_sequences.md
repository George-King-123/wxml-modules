Set $q=2$, $n = q + 2 = 4$. We try to build sequences that will satisfy all the constraints. There are $36$ length $8$ sequences that work. These satisfy the constraints for $m = 1$ at the first five offsets, and the constraints for $m = 2$ at the starting offset (the only one which makes sense). It is impossible to extend any of these to work, they won't work with $m = 2$ at the second offset.

Now examine $q = 2, n = q + 3 = 5$. There are $102$ sequences of length $15$ that work. These satisfy the constraints for $m = 1$ at the first $11$ offsets, the constraints for $m = 2$ at the first $6$ offsets, and the constraints for $m = 3$ at the first offset (the only one which makes sense). It is impossible to extend any of these to work, they won't work with $m = 3$ at the second offset.

Looking at $q = 2, n = q + 4 = 6$, there are tons of sequences of length $23$ that work ($109098$ of them), then many fewer of length $24$ (just $816$), which makes sense since length $24$ is the first time we can apply constraints for $m = 4$. Nonetheless, the second offset for $m = 4$ doesn't kill all of these sequences, it reduced the number from $816$ to $48$. It is the third offset for $m = 4$ that kills of the sequences, i.e. there are no good sequences of length $26$. \
(It took about 10 minutes to run sequence builder on this, up from half a second for $q = 2, n = 5$).

This pattern of the first offset working for a new value of $m$ doesn't always hold: 
- With $q=3, n = q + 2 = 5$ the first offset breaks for $m = 2$. In other words, there are lots of sequences of length $9$ that work, none of length $10$. 
- For $q=3, n = q + 3 = 6$, there are good sequences of length $14$ but not $15$ (very bad for the pattern)
- For $q=5, n = q + 2 = 7$, the first offset breaks for $m = 2$, i.e. there are lots of sequences of length $13$ that work ($1170720$ of them), but none of length $14$.

### dump of output for $q = 2, n = q + 4 = 6$ 
Time taken, in seconds: 712.5301980999939  
There are 1 successful seqs of length 0\
There are 3 successful seqs of length 1\
There are 9 successful seqs of length 2\
There are 27 successful seqs of length 3\
There are 81 successful seqs of length 4\
There are 243 successful seqs of length 5\
There are 540 successful seqs of length 6\
There are 1440 successful seqs of length 7\
There are 3804 successful seqs of length 8\
There are 9960 successful seqs of length 9\
There are 25908 successful seqs of length 10\
There are 67344 successful seqs of length 11\
There are 91362 successful seqs of length 12\
There are 129894 successful seqs of length 13\
There are 255294 successful seqs of length 14\
There are 510762 successful seqs of length 15\
There are 1017870 successful seqs of length 16\
There are 2099826 successful seqs of length 17\
There are 507318 successful seqs of length 18\
There are 229338 successful seqs of length 19\
There are 89472 successful seqs of length 20\
There are 92478 successful seqs of length 21\
There are 105252 successful seqs of length 22\
There are 109098 successful seqs of length 23\
There are 816 successful seqs of length 24\
There are 48 successful seqs of length 25\
There are 0 successful seqs of length 26\
There are 0 successful seqs of length 27\
...

### $q = 2, n = 4$ <a name="one"></a>
AACBACAB\
BBACCBAB\
ACABCBAA\
CCBAACBC\
CCBABCAC\
CCABCACB\
BCBAACBB\
AABCABAC\
ACBCABCC\
ACABBCAA\
CBABCABB\
CCBACBCA\
CABACBAA\
ABACCBAA\
BCACBACC\
CBCAABCC\
CACBABCC\
BBACBABC\
BBACABCB\
AACBCABA\
ABACBCAA\
CBCABACC\
AABCCABA\
CCABACBC\
BBCABCBA\
BABCCABB\
CACBBACC\
BABCACBB\
BCBACABB\
CCABBCAC\
AACBBACA\
AABCBACA\
BBCAABCB\
BACABCAA\
ABCBACBB\
BBCACBAB\

### $q = 2, n = 5$ <a name="two"></a>

ABAACABCBAAACBA\
ACABCCACBCCABCA\
ACBACBAABCCAABB\
ABACBAAACBCABBA\
BCCABBCBABBCBAC\
BCBBABCACBBBACC\
ABCACCBCACCBAAC\
BCBACBBBACABCCB\
BABCABBBCACBAAB\
CAABCCACBCCACBA\
AACCBBACCABCABC\
BCBACABBBCACBAB\
BACBACBBCAABBCC\
ABAACABCBAAACBC\
CBACAABACAABCCA\
BBCCAABCCBACBAC\
CBBACCBCACCBCAB\
CBBCABACCCBACBC\
AACBBBACABCBBAB\
CCBAAACBCABAACA\
ACBAAACBCABAACA\
CBACCCBABCACCBC\
AABCCBACBACCABB\
ABCABCAACBBAACC\
BABCACBBBACABCB\
BBCAAABCBACAABA\
CCBBAACABAACCBB\
ACAABACBCAAABCB\
BACBCCACBCCABBC\
CACCBCABACCCBAB\
AABBCCABBACBACB\
CBCAAABCBACAABA\
AABCCCABACBCCAC\
BCABBBCACBABBCB\
ABBACBCAAABCABA\
BABCCCABACBCCAC\
ABCABBCBABBCABA\
BCBACCBCACCBACB\
ACAABACBCAAABCA\
CACCBCABACCCBAA\
CCBBAACBBCABCAB\
CBCCACBABCCCABB\
BBACCABCABCCBAA\
BBAACCBAABCABCA\
AACCBBABCBBAACC\
CBACBACCABBCCAA\
CBCABCCCABACBBC\
CBCABBCBABBCABC\
CACBAACABAACBAC\
CCABBBCACBABBCB\
CBCCACBABCCCABA\
BBACCCBABCACCBC\
CAACBABCCCABCAC\
BBCAACBACBAABCC\
CACBACCCBABCAAC\
CCBAABCABCAACBB\
ACCABCBAAACBACA\
BABBCBACABBBCAB\
CBCABACCCBABCAC\
BCCBACABBBCABCB\
ACAABACBCAAABCC\
CACCBCABACCCBAC\
CABCAABACAABCAC\
AABBCCACBCCAABB\
CCAABBCBABBCCAA\
BAABCACBBBACBAB\
BABBCBACABBBCAA\
AACBBCABCABBACC\
CACBBBACABCBBAB\
ACBABBCBABBCAAB\
BBCCAABACAABBCC\
CBACBBABCBBACBC\
ABBCAABACAABACB\
ACABCAAABCBACCA\
ABACBBABCBBACBA\
BCABCCACBCCABCB\
BACBBBACABCBBAB\
BCBAAACBCABAACA\
CACBABCCCABACBC\
CBCCACBABCCCABC\
BCBBABCACBBBACB\
BACBAACABAACBAB\
BBAACCBCACCBBAA\
CCABBACBACBBCAA\
BCABAACABAACBBA\
ACABCBAAACBCABA\
BABCAABACAABCAB\
CABCBBABCBBACCB\
BAACBBABCBBABCA\
BCBBABCACBBBACA\
CABCABCCBAACCBB\
ABACCCBABCACCBC\
ACABBBCACBABBCB\
BABBCBACABBBCAC\
ABAACABCBAAACBB\
ABACBCAAABCBACA\
ABCAAABCBACAABA\
ACBACCBCACCBACA\
BCABCABBACCBBAA\
CABCCCABACBCCAC\
ACCBAACABAACABC\
CCAABBCAACBACBA\