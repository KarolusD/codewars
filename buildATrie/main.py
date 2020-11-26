def build_trie(*words):
    if len(words) == 0 or words[0] == "":
        return {}
    words_list = [list(i) for i in words][0]
    longest_word = max(words_list, key=len)
    value = None
    key = longest_word[:]
    #results = {}
    for i in range(len(list(longest_word))):
        value = {key: value}
        print(value)
        key = longest_word[:-i-1]

# def check_exact_len(word_len, words):


# test_data = {
#     tuple(): {},
#     ("", ): {},
#     ("trie",):
#     {'t': {'tr': {'tri': {'trie': None}}}},
#     ("tree",):
#         {'t': {'tr': {'tre': {'tree': None}}}},
#     ("trie", "trie"):
#         {'t': {'tr': {'tri': {'trie': None}}}},
#     ("A", "to", "tea", "ted", "ten", "i", "in", "inn"):
#         {'A': None, 't': {'to': None, 'te': {'tea': None,
#                                              'ted': None, 'ten': None}}, 'i': {'in': {'inn': None}}},
#     ("true", "trust"):
#     {'t': {'tr': {'tru': {'true': None, 'trus': {'trust': None}}}}},
# }

# for test_input, expected in sorted(test_data.items()):
#     print(build_trie(*test_input))


print(build_trie(("true", "trust")))
