Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S.

In case of multiple subarrays, return the subarray which comes first on moving from left to right
https://practice.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1?page=1&difficulty[]=0&curated[]=1&sortBy=submissions

 vector<int> subarraySum(int arr[], int n, long long s)
    {    
        int start=0, end=0;
        long long sum=arr[0];
        
        if(s==0)
            return {-1};
        
        while(end<n)
        {
            if(sum==s)
                return {start+1, end+1};
            else if(sum < s)
            {
                sum = sum + arr[++end];
            }
            else{
                sum= sum-arr[start++];
            }
        }
        
        return {-1};
    }
