

def levenshtein3(s1, s2):
    """ returns the levenshtein, or 'edit' distance between strings s1 and s2
        weights strings that match the first three letters
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
    
    modifier = 5
    if s2[0] == s1[0]:
        modifier = 4

    if len(s2) > 1 and len(s1) > 1:
        if s2[0:1] == s1[0:1]:
            modifier = 3

            if len(s2) > 2 and len(s1) > 2:
                if s2[0:2] == s1[0:2]:
                    modifier = 1

                    if len(s2) > 3 and len(s1) > 3:
                        if s2[0:3] == s1[0:3]:
                            modifier = 0

    previous_row = xrange(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1] + modifier
