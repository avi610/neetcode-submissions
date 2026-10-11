#include <vector>

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        std::vector<int> seen(256, 0);
        for (char c : s) {
            seen[c-'a']++;
        }
        for (char c : t) {
            if(--seen[c-'a'] < 0) {
                return false;
            }
        }
        return true;
    }
};
