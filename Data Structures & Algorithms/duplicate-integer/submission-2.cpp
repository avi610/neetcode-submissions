#include <set>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> seen;
        for (int num : nums) {
            seen.insert(num);
        }
        return seen.size() != nums.size();
    }
};