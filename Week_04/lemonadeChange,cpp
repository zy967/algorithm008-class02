class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int fiveDollars = 0;
        int tenDollars = 0;
        if (bills[0] != 5) {
            return false;
        }
        for (int i = 0; i < bills.size(); i++) {
            if (bills[i] == 5) {
                fiveDollars++;
            }else if (bills[i] == 10) {
                fiveDollars--;
                tenDollars++;
            }else if (bills[i] == 20){
                if (tenDollars > 0) {
                    tenDollars--;
                    fiveDollars--;
                }else {
                    fiveDollars -= 3;
                }
            }
            if (fiveDollars < 0) {
                return false;
            }
        }
        return true;
    }
};
