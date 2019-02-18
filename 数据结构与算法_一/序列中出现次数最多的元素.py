from collections import Counter
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
# 出现频率最高的三个单词
word_counts = Counter(words)   #在底层实现上，一个 Counter 对象就是一个字典
top_three = Counter(words).most_common(3)
print(top_three)
print(word_counts["look"])   #在底层实现上，一个 Counter 对象就是一个字典
# Outputs:[('eyes', 8), ('the', 5), ('look', 4)]