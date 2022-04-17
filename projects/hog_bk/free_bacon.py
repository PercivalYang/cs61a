def free_bacon(score):
    """Return the points scored from rolling 0 dice (Free Bacon).

    score:  The opponent's current score.
    """
    assert score < 100, 'The game should be over.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    score_num = []
    score = score**3
    total_score = 0
    while score // 10:
        score_num.append(score % 10)
        score //= 10
    score_num.append(score)
    for num in score_num[::-1]: 
        total_score += num
        total_score = -total_score
    return 1+abs(total_score)
    # END PROBLEM 2


