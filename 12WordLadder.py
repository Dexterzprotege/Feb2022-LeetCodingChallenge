# Question: https://leetcode.com/problems/word-ladder/

# Solution:
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adjacencyList = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1: ]
                adjacencyList[pattern].append(word)
        visited = set([beginWord])
        queue = [beginWord]
        ans = 1
        while queue:
            for i in range(len(queue)):
                word = queue.pop(0)
                if word == endWord:
                    return ans
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1: ]
                    for neighbor in adjacencyList[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
            ans += 1
        return 0

# Verdict:
# Runtime: 124 ms, faster than 93.09% of Python3 online submissions for Word Ladder.
# Memory Usage: 17.4 MB, less than 53.66% of Python3 online submissions for Word Ladder.
