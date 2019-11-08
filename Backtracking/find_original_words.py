'''
Find Original Words

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. 
If there is no possible reconstruction, then return null.

Input: sentence = 'thequickbrownfox', words = ['quick', 'brown', 'the', 'fox']
Output: ['the', 'quick', 'brown', 'fox']

Input: sentence = 'bedbathandbeyond', words = ['bed', 'bath', 'bedbath', 'and', 'beyond']
Output: ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond']

=========================================
Backtracking, iterate the sentence construct a substring and check if that substring exist in the set of words.
If the end is reached but the last word doesn't exist in the words, go back 1 word from the result (backtracking).
	Time Complexity: 	O(N)    , (worst case, about O(W! * N), for example sentence='aaaaaac', words=['a','aa','aaa','aaaa','aaaaa', 'aaaaaa'])
	Space Complexity: 	O(W)    , W = number of words
'''


############
# Solution #
############

def find_words(sentence, words):
    all_words = set()
    
    # create a set from all words
    for i in range(len(words)):
        all_words.add(words[i])
    
    n = len(sentence)
    i = 0
    subsentence = ''
    result = []

    # go letter by letter and save the new letter in subsentence
    while (i < n) or (len(subsentence) != 0):
        # if there are no left letters in the sentence, then this combination is not valid
        # remove the last word from the results and continue from that word
        if i == n:
            i -= len(subsentence)
            # if there are no words in the result, then this string is not composed only from the given words
            if len(result) == 0:
                return None
            subsentence = result[-1]
            del result[-1]

        # add the new letter into subsentence and remove it from the sentence
        subsentence += sentence[i]
        i += 1

        # check if the new word exist in the set
        if subsentence in all_words:
            result.append(subsentence)
            subsentence = ''
    
    return result


###########
# Testing #
###########

# Test 1
# Correct result => ['the', 'quick', 'brown', 'fox']
print(find_words('thequickbrownfox', ['quick', 'brown', 'the', 'fox']))

# Test 2
# Correct result => ['bed', 'bath', 'and', 'beyond']
print(find_words('bedbathandbeyond', ['bed', 'bath', 'bedbath', 'and', 'beyond']))

# Test 3
# Correct result => ['bed', 'bathand', 'beyond']
print(find_words('bedbathandbeyond', ['bed', 'bath', 'bedbath', 'bathand', 'beyond']))

# Test 4
# Correct result => None ('beyo' doesn't exist)
print(find_words('bedbathandbeyo', ['bed', 'bath', 'bedbath', 'bathand', 'beyond']))