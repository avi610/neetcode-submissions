#include <unordered_map>

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }
        std::array<int, 256> counts{};
        for (char c : s) {
            counts[c - 'a']++;
        }

        for (char c : t) {
            if (--counts[c-'a'] < 0) {
                return false;
            }
        }

        return true;
    }
};
