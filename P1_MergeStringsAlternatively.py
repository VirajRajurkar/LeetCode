"""
Merge Strings Alternately
https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
        a p b q c r
"""

def mergeAlternately(word1, word2):
    wordOutput = ""
    i, j = 0, 0

    while i < len (word1) or j < len(word2):
        if i < len(word1):
            wordOutput +=  word1[i]
            i +=1
        if j < len(word2):
            wordOutput +=  word2[j] 
            j += 1

    return (wordOutput )

print(mergeAlternately("abcd", "pq")) #outputs "apbqcd"
print(mergeAlternately("ab", "pqrs")) #outputs "apbqrs"
print(mergeAlternately("abc", "pqr")) #outputs "apbqcr"
print(mergeAlternately("abcd", "")) #outputs "abcd"