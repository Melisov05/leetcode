[link](https://leetcode.com/problems/encode-and-decode-strings/description/)

In this problem I used length-prefix encoding, so when we decode our string we won't hit corner cases.
By using length#string approach in decode we can clearly identify when the next string begins and where it ends.
I used two while loops to shift pointer to track the length of a string and find # symbol to then parse the line and add to our result array.