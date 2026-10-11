#include <vector>
#include <unordered_set>

using std::vector;
using std::unordered_set;

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seen(nums.begin(),nums.end());
        return seen.size() != nums.size();
    }
};