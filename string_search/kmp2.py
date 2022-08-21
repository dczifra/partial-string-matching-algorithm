def kmp_v2(text, pattern): 
    """Find the first index of `pattern` in `text`
    using the Knuth-Morris-Pratt algorithm. If
    nothing is found, then return None.
    
    text -- Sequence. E.g. "hello" or [1, 2, 3, 4].
    pattern -- Sequence. E.g. "ll" or [2, 3].
    """
    index = knuth_morris_pratt(
        text=OneBased(text), pattern=OneBased(pattern)
    )
    if index is not None:
        return True
    else:
        return False


class OneBased:
    """A proxy object that allows sequences to use
    1-based indexing."""

    def __init__(self, seq):
        self.seq = seq

    def __getitem__(self, key):
        assert key >= 1
        return self.seq[key - 1]

    def __len__(self):
        return len(self.seq)

def knuth_morris_pratt(text, pattern):
    """Run the Knuth-Morris-Pratt algorithm on
    sequences `text` and `pattern`. The
    sequences must use 1-based indexing, not
    0-based indexing. Returns the 1-based index
    of the first match, or returns None if no
    match is found.
    
    text -- OneBased. E.g. OneBased("hello") or
        OneBased([1, 2, 3, 4]).
    pattern - OneBased. E.g. OneBased("ll") or
        OneBased([2, 3]).
    
    For more information, see:
    
    > Knuth, Donald, Morris, James, Pratt, Vaughan. 1977.
    > "Fast Pattern Matching in Strings."
    > SIAM J. Comput., 6(2), 323–350. (28 pages)
    > https://doi.org/10.1137/0206024
    """
    n, m = len(text), len(pattern)
    
    # Compute the "next" table.
    
    j = 1; t = 0; next = {1:0}
    while j < m:
        while t > 0 and pattern[j] != pattern[t]:
            t = next[t]
        t = t + 1; j = j + 1
        if pattern[j] == pattern[t]:
            next[j] = next[t]
        else:
            next[j] = t
            
    # Pattern-match process.

    j = k = 1
    while j <= m and k <= n:
        while j > 0 and text[k] != pattern[j]:
            j = next[j]
        k = k + 1; j = j + 1
    
    if j > m:
        return k - m