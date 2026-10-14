#include <unordered_map>
#include <array>

using std::array;
using std::unordered_map;

class Solution {
   public:
    string getFrequencyMap(string str) {
        vector<int> frequencies(26, 0);
        for (char c : str) {
            frequencies[c - 'a']++;
        }
        string key;
        for (int count : frequencies) {
            key += to_string(count) + '#';
        }
        return key;
    }

    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groupedStrs{};
        for (string str : strs) {
            string frequencies = getFrequencyMap(str);
            groupedStrs[frequencies].push_back(str);
        };

        vector<vector<string>> res{};
        for (const auto& [_, value] : groupedStrs) {
            res.push_back(value);
        }
        return res;
    }
};