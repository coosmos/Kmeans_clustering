#include <bits/stdc++.h>

using namespace std;

int main() {
    vector<pair<int, int>> intervals = {
        {1, 5}, {3, 7}, {4, 6}, {6, 8}, {10, 15}
    };

    map<int,int>m;
    //creating the difference array
    for(auto it:intervals){
        m[it.first]+=1;
        m[it.second+1]+=-1;

    }
    for(auto it:m){
        cout<<it.first<< " " <<it.second << "\n ";
    }
    //check for overlaps
        int maxOverlap = 0, currentOverlap = 0;
    for (auto& event :m) {
        currentOverlap += event.second; // Add contribution
        maxOverlap = max(maxOverlap, currentOverlap);
    }
    cout << "Maximum overlap: " << maxOverlap << endl;
    return 0;
}
