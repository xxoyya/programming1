# 단어의 수 세기 (3번)
def count_words(s):
    s = s.replace(',', ' ').replace('.',' ').replace('!',' ')
    words = s.split()

    with open("words.txt", "w") as out:
        for word in words:
            out.write(f"{word}\n")
        out.write(f"Total {len(words)} words.\n")


# 문단의 수 세기 (3번)        
def count_sentences(s):
    s = s.replace('.\t', '. ').replace('\n', '. ')
    sentences = list(s.split(". "))
    for sentence in sentences:
        if len(sentence) == 0:
            sentences.remove(sentence)
    print(f"This file has {len(sentences)} sentences.")


# 문자 유형 분류하기 (3번)
def count_charclass(s):   
    length = len(s)
    lowers = uppers = nums = specials = whitespaces = 0

    for c in s:
        if c.isupper(): uppers += 1
        elif c.islower(): lowers += 1
        elif c.isdigit(): nums += 1
        elif c.isspace(): whitespaces += 1
        else: specials += 1

    print(f"대문자수: {uppers}")
    print(f"소문자수: {lowers}")
    print(f"숫자수: {nums}")
    print(f"공백문자수: {whitespaces}")
    print(f"특수문자수: {specials}")
    print(f"총 문자수: {length}")


# 각 문자 별로 문자수 세기 (4번)
def count_chars(s):
    char_dict = {}
    for c in s:
        if char_dict.get(c) == None:
            char_dict[c] = 1
        else:
            char_dict[c] += 1

    with open("char_count.txt", "w") as f:
        for c in sorted(char_dict.keys()):
            f.write(f"{c}: {char_dict[c]}개\n")

            
file = open("test.txt", "r")
s = file.read()
count_charclass(s)
count_chars(s)
count_words(s)
count_sentences(s)
file.close()
