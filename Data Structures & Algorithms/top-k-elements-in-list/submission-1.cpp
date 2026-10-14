#include <queue>

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // Calculate Frequencies
        std::unordered_map<int, int> freq{};
        for (const auto num : nums) {
            freq[num]++;
        }
        
        // Min Heap of Size K so we can remove the least frequent element whenever we get to a more popular number
        std::priority_queue<pair<int,int>, vector<pair<int,int>>, std::greater<pair<int,int>>> minHeap;
        for (const auto& [key, value] : freq) {
            minHeap.push({value, key});
            if (minHeap.size() > k) {
                minHeap.pop(); // Pop the least frequent
            }
        }

        vector<int> res;
        while (minHeap.size() > 0) {
            res.push_back(minHeap.top().second);
            minHeap.pop();
        }
        return res;
    }
};
