
def levenshtein(s1, s2):
    """ returns the levenshtein, or 'edit' distance between strings s1 and s2
    """
    if s1 is None:
        s1 = ''
    if s2 is None:
        s2 = ''

    if len(s1) < len(s2):
        return levenshtein(s2, s1)
    
    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)
    
    previous_row = xrange(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]



def levenshtein3(s1, s2):
    """ returns the levenshtein, or 'edit' distance between strings s1 and s2
    """
    if s1 is None:
        s1 = ''
    if s2 is None:
        s2 = ''

    if len(s1) < len(s2):
        return levenshtein3(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)
    
    ret_val = 5
    if s2[0] == s1[0]:
        ret_val = 4

    if len(s2) > 1 and len(s1) > 1:
        if s2[0:1] == s1[0:1]:
            ret_val = 3

        if len(s2) > 2 and len(s1) > 2:
            if s2[0:2] == s1[0:2]:
                ret_val = 1

            if len(s2) > 3 and len(s1) > 3:
                if s2[0:3] == s1[0:3]:
                    ret_val = 0

    previous_row = xrange(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1] + ret_val



def levenshtein2(s, t):
    ''' from wikipedia AND added a decay to favor shorter matches and matches on the beginning of the word'''
    #degenerate cases
    if s == t:
        return 0;
    if len(s) == 0:
        return len(t);
    if len(t) == 0:
        return len(s);
 
    # create two work vectors of integer distances
    #int[] v0 = new int[t.Length + 1];
    v0 = [0] * (len(t)+1)
    #int[] v1 = new int[t.Length + 1];
    v1 = [0] * (len(t)+1)
 
    #// initialize v0 (the previous row of distances)
    #// this row is A[0][i]: edit distance for an empty s
    #// the distance is just the number of characters to delete from t
    #for (int i = 0; i < v0.Length; i++)
    for i in range(len(t)):
        v0[i] = i
 
    #for (int i = 0; i < s.Length; i++)
    decay = 1
    for i in range(len(s)):
        #// calculate v1 (current row distances) from the previous row v0
 
        #// first element of v1 is A[i+1][0]
        #//   edit distance is delete (i+1) chars from s to match empty t
        v1[0] = i + 1;
 
        #// use formula to fill in the rest of the row
        for j in range(len(t)): 
            cost = 0 if s[i] == t[j] else 1
            v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost);
 
        #// copy v1 (current row) to v0 (previous row) for next iteration
        for j in range(len(v0)):
            v0[j] = v1[j] * decay;
        decay = decay * 2
 
    return v1[len(t)];
