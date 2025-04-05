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
"""

word1 = "abc"
word2 = "pqr"
word1New = ""
word2New = ""

for i in range(len(word1)):
    word1New += word1[i]

    if i <= (len(word1)-1):
        word1New += " "


for i in range(len(word2)):
    word2New += word2[i]

    if i <= (len(word2)-1):
        word2New += " "

word2New = " " + word2New


print (word1New)
print (word2New)

