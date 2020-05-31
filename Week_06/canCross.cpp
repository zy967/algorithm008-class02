class Solution {
public:
    bool canCross(vector<int>& stones) {
        int n = stones.size();
        vector<vector<bool>> dp(n, vector<bool>(n+1, false));
        dp[0][0] = true;
        for (int i = 1; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                int diff = stones[i] - stones[j];
                if (diff > i) continue; 
                if (dp[j][diff] || dp[j][diff-1] || diff < n - 1 && dp[j][diff+1]) {
                    dp[i][diff] = true;
                }
            }
        }
        for (int i = 1; i <= n; ++i) {
            if (dp[n-1][i]) return true;
        }
        return false;
    }
};
