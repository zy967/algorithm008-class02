class Solution {
public:
    int mod=1000000000+7,size;
    int cal_all(int dp[][3][2],int p,int lflag,int aflag){
        if(p==size)return 1;
        int res=0;
        if(dp[p][lflag][aflag]!=-1)return dp[p][lflag][aflag];

        res+=cal_all(dp,p+1,0,aflag);
        res%=mod;

        if(lflag<2){
            res+=cal_all(dp,p+1,lflag+1,aflag);
            res%=mod;
        }

        if(!aflag){
            res+=cal_all(dp,p+1,0,1);
            res%=mod;
        }
        dp[p][lflag][aflag]=res;
        return res;
    }
    int checkRecord(int n) {
        int dp[n][3][2];
        size=n;
        memset(dp,-1,sizeof(dp));
        return cal_all(dp,0,0,0);
    }
};
