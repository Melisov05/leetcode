[link](https://leetcode.com/problems/group-anagrams/description/)

In this problem I had the following approach:

First of all I created a dictionary to match the words by their frequency. As a key I had a sorted word, but since lists are mutable, they can't be map keys, so I converted the word to a tuple type. After that I iterated through our string word by word. I converted each word into its sorted tuple version and added to a dictionary, after all the words are covered, I printed the final result

