class Solution(object):
    def boldWords(self, words_raw, S):
        N = len(S)
        bold = [0] * (N + 2)
        words = words_raw.split(',')
        for word in words:
            start = 0
            while True:
                idx = S[start:].find(word)
                if idx < 0: break
                for x in range(start + idx, start + idx + len(word)):
                    bold[x + 1] = 1
                start += idx + 1
        S = list(S) + ['']
        ans = []
        for x in range(1, N + 1):
            if bold[x] == 1 and bold[x - 1] == 0:
                ans.append('<bold>')
            ans.append(S[x - 1])
            if bold[x] == 1 and bold[x + 1] == 0:
                ans.append('</bold>')
        return ''.join(ans)

if __name__ == '__main__':
    # words = 'abc,123'
    # S = 'abcxyz123'
    # words = 'aaa,aab,bc'
    # S = 'aaabbcc'
    # words = 'aa,bb'
    # S = 'aabbc'
    words = input()
    S = input()
    solu = Solution()
    print(solu.boldWords(words, S))