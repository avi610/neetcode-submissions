#include <unordered_map>

class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> seen;
        for (char c : s) {
            if (seen.contains(c)) {
                seen[c] += 1;
            } else {
                seen[c] = 1;
            }
        }
        for (char c : t) {
            if (!seen.contains(c) or seen[c] <= 0) {
                return false;
            } else if (seen[c] == 1) {
                seen.erase(c);
            } else {
                seen[c] -= 1;
            }
        }
        return seen.size() == 0;
    }
};
