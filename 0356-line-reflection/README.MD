When I was thinking about the solution, I started drawing in my notebook to visualize the problem.
On a simple case I noticed that if we have 2 points that are mirrored, then mirror point would be their average. For example if we had (2,2) and (6,2) their mirror point would be at x = 4
So, I thought with n points our mirror point would be average of all x points.
And it would be true if points indeed had their mirrored version. 
The case with duplicated points could be resolved by using hash set and then computing the mean.
After getting the mirror point (which is c) we could check if mirrored version exists in our hashset using the formula (2c-x,y).
If it's not in hashset then we don't have symmetry and return false
However, I noticed later that we could encounter problems with floating point if we divide.
So the better approach would be figuring out the min and the max x points and getting their sum. 
It would give us 2c without the need to divide. By having 2c we could check every point to see if it has its mirrored version.
If it doesn't have then we return False, if it does have -> return True.