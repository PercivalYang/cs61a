def autocorrect(typed_word, word_list, diff_function,limit):
    if typed_word in word_list:
        return typed_word
    score_lst = []
    for word in word_list:
        score_lst.append(diff_function(typed_word,word,limit))
    min_index, min_score = min(enumerate(score_lst))
    if min_score < limit:
        return word_list[min_index]
    return typed_word

abs_diff = lambda w1, w2, limit: abs(len(w2)-len(w1))
autocorrect('cul', ['culture','cult','cultivate'], abs_diff,10)
