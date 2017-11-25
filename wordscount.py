def count_words(s, n):
    """Return the n most frequently occuring words in s."""

    # TODO: Count the number of occurences of each word in s

    # TODO: Sort the occurences in descending order (alphabetically in case of ties)

    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    res = {}
    slist = s.split()
    for word in slist:
        if word in res.keys():
            res[word] += 1
        else:
            res[word] = 1
    sorted_res = sorted(res.iteritems(), key = lambda x: x[1], reverse=True)
    top_n = sorted_res[:n]
    return top_n


print count_words("betty bought a bit of butter but the butter was bitter", 3)
