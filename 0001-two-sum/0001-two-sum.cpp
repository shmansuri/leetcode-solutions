class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
    //     vector<int> arr;
    //     for(int i =0; i<(int)nums.size(); i++){
    //         for(int j=i+1; j<(int)nums.size(); j++){
    //             if(nums[i]+ nums[j] == target){
    //                 arr.push_back(i);
    //                 arr.push_back(j);
    //                 return arr;
    //             }
    //         }
    //     }
    //    return{}; 

     unordered_map<int,int> mp; // value -> index
        for (int i = 0; i < (int)nums.size(); ++i) {
            int need = target - nums[i];
            if (mp.find(need) != mp.end()) {
                return { mp[need], i }; // found complement
            }
            mp[nums[i]] = i;
        }
        return {};
    }
    
};