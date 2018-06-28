from utils.time_utils import *
from collections import Counter

if __name__ == '__main__':
    """
        Counter 对象可以接受任意的由可哈希（hashable）元素构成的序列对象。
    """
    with timer('test counter'):
        words = [
            'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
            'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
            'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
            'my', 'eyes', "you're", 'under'
        ]
        word_counts = Counter(words)
        top_three = word_counts.most_common(3)
        print(f'raw word counts is: {word_counts}\n'
              f'top three word counts is: {top_three}')
        # 允许存在在之前没有统计的数据
        more_words = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes', 'learn']
        word_counts.update(more_words)
        print(f'update word count is: {word_counts}')
        print('=' * 60)
        a = Counter(words)
        b = Counter(more_words)
        print(f'word counts a is: {a}\n'
              f'word counts b is: {b}\n'
              f'combine counts is: {a + b}\n'
              f'subtract counts is: {a - b}')

