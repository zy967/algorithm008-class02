class Solution {
public:
    struct PositionHash {
        size_t operator()(const pair<int, int> &val) const
        {
            return val.first ^ val.second;
        }
    };
    
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {        
        unordered_set<pair<int, int>, PositionHash> obs;
        for (const auto &o : obstacles) {
            obs.insert({o[0], o[1]});
        }

        int maxDestSq = 0;
        int pos[2] = {0, 0};
        int dir[2] = {0, 1};
        for (int c : commands) {
            if (c == -1) {
                dir[0] = -dir[0];
                swap(dir[0], dir[1]);
            } else if (c == -2) {
                dir[1] = -dir[1];
                swap(dir[0], dir[1]);
            } else if (c >= 1 && c <= 9) {
                while (c--) {
                    int px = pos[0] + dir[0];
                    int py = pos[1] + dir[1];
                    if (obs.find({px, py}) != obs.end()) {
                        break;
                    }

                    pos[0] = px;
                    pos[1] = py;
                }
                
                int destSq = pos[0] * pos[0] + pos[1] * pos[1];
                if (destSq > maxDestSq) {
                    maxDestSq = destSq;
                }
            }
            
        }
        
        return maxDestSq;
    }
};
