// Bucket Sort
// Time: O(n)
// Space: O(n)

#include <queue>
#include <unordered_map>

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // Calculate Frequencies
        std::unordered_map<int, int> freq{};
        for (const auto num : nums) {
            freq[num]++;
        }

        // Create a vector where
        // Index -- 1 2 3 4 5 6 7 8 9 ... n
        // has an empty vector which will be filled with all elements that have that frequency
        vector<vector<int>> countMap(nums.size());
        for (const auto& [i, count] : freq) {
            countMap[count-1].push_back(i);
        }

        vector<int> res;
        int i = countMap.size()-1;
        while (res.size() < k && i >= 0) {
            for (int j = 0; j < countMap[i].size() && res.size() < k; j++) {
                res.push_back(countMap[i][j]);
            }
            --i;
        }
        return res;
    }
};
