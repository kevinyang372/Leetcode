# You have an initial power of P, an initial score of 0, and a bag of tokens where tokens[i] is the value of the ith token (0-indexed).

# Your goal is to maximize your total score by potentially playing each token in one of two ways:

# If your current power is at least tokens[i], you may play the ith token face up, losing tokens[i] power and gaining 1 score.
# If your current score is at least 1, you may play the ith token face down, gaining tokens[i] power and losing 1 score.
# Each token may be played at most once and in any order. You do not have to play all the tokens.

# Return the largest possible score you can achieve after playing any number of tokens.

 

# Example 1:

# Input: tokens = [100], P = 50
# Output: 0
# Explanation: Playing the only token in the bag is impossible because you either have too little power or too little score.
# Example 2:

# Input: tokens = [100,200], P = 150
# Output: 1
# Explanation: Play the 0th token (100) face up, your power becomes 50 and score becomes 1.
# There is no need to play the 1st token since you cannot play it face up to add to your score.
# Example 3:

# Input: tokens = [100,200,300,400], P = 200
# Output: 2
# Explanation: Play the tokens in this order to get a score of 2:
# 1. Play the 0th token (100) face up, your power becomes 100 and score becomes 1.
# 2. Play the 3rd token (400) face down, your power becomes 500 and score becomes 0.
# 3. Play the 1st token (200) face up, your power becomes 300 and score becomes 1.
# 4. Play the 2nd token (300) face up, your power becomes 0 and score becomes 2.
 

# Constraints:

# 0 <= tokens.length <= 1000
# 0 <= tokens[i], P < 104

def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
    tokens = sorted(tokens)
    
    @lru_cache
    def get_max(i, j, power, score):
        if i > j: return score
        
        option1 = option2 = 0
        if score > 0:
            option1 = get_max(i, j - 1, power + tokens[j], score - 1)
        
        if power >= tokens[i]:
            option2 = get_max(i + 1, j, power - tokens[i], score + 1)
            
        return max(score, option1, option2)
    
    return get_max(0, len(tokens) - 1, P, 0)

# greedy
def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
    tokens = sorted(tokens)
    i, j = 0, len(tokens) - 1
    
    max_s = 0
    s = 0
    
    while i <= j:
        if P >= tokens[i]:
            P -= tokens[i]
            s += 1
            i += 1
            max_s = max(max_s, s)
        elif s > 0:
            P += tokens[j]
            s -= 1
            j -= 1
        else:
            break
    
    return max_s