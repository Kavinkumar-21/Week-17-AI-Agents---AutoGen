import math

def count_permutations(word):
    n = len(word)
    count = dict()
    for i in word:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    permutations = math.factorial(n)
    for key in count:
        permutations /= math.factorial(count[key])
    return int(permutations)

word = "ALGEbRA"
print(count_permutations(word))