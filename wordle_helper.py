import enchant

# INPUT FUNCTIONS
def get_greens():
    r = ['', '', '', '', '']
    x = input("Give your greens like this: 'a2 b4' for 'a' in the 2nd and 'b' in the 4th slot: ")
    for t in x.split():
        r[int(t[1])-1] = t[0]
    return r

def get_yellows():
    r = [[], [], [], [], []]
    x = input("Give your yellows like this: 'c1 c2 d3' for 'c' not in the 1st or 2nd, and 'd' not in the 3rd slot: ")
    for t in x.split():
        r[int(t[1])-1].append(t[0])
    return r

def get_grays():
    r = []
    x = input("[OPTIONAL. Press Enter (empty) to skip] Give your grays like this: `a b c` if these letters are gray: ")
    for t in x.split():
        r.append(t)
    return r

# WORDLE CHECK FUNCTIONS
def green_check(c):
    for i in range(len(greens)):
        if greens[i].isalpha() and c[i] != greens[i]:
            return False
    return True

def yellow_check(c):
    for i in range(len(yellows)):
        for j in range(len(yellows[i])):
            if yellows[i][j] not in c or yellows[i][j] == c[i]:
                return False
    return True

# WORD CONSTRUCTOR
def construct(c, l):
    for i in range(len(l)):
        if len(c) == 5:
            if green_check(c) and yellow_check(c):
                words.append(c)
            return
        c += l[i]
        _l = l.copy()
        _l.pop(i)
        construct(c, _l)
        c = c[:-1]

letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
words = []

# get inputs
greens = get_greens()
yellows = get_yellows()
grays = get_grays()
# keep only non-gray letters
letters = list(filter(lambda item: item not in grays, letters))

construct('', letters)

good_words = []
d = enchant.Dict("en_US")
for word in words:
    if (d.check(word)):
        good_words.append(word)

print(good_words)
