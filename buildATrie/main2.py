def build_trie(*words):
    if len(words) == 0 or words[0] == "":
        return {}
    trie = {}
    words_list = list(reversed(sorted([list(i) for i in words][0])))
    # print(words_list)
    value = None
    for i in range(len(words_list)):
        key = words_list[i]

        for j in range(len(words_list[i])):

            value = {key: value}
            key = words_list[i][:-j-1]
            #print(key, value, value.get(key))
            print(value)
        trie.update(value)

    # value={key: value}
    # key=longest_word[:-i-1]
    #print(trie, 'co tam?')


print(build_trie(("true", "trust")))
