/**
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
Notice that you may not slant the container.

Example 1:
Input: height = [1,1]
Output: 1
  
Example 2:
Input: height = [4,3,2,1,4]
Output: 16
  
Example 3:
Input: height = [1,2,1]
Output: 2
*/

public class Solution {
    public int MaxArea(int[] height) {
        int maxArea=0;
        int i=0;
        int j=height.Length-1;
        while(i<j){
            int area=Math.Min(height[i],height[j])* Math.Abs(i-j);
            if(maxArea<area){
                maxArea=area;
            }
            if(height[i]<=height[j]){
                i++;
            }
            else if(height[i]>height[j]){
                j--;
            }
        }
        return maxArea;
    }
}
