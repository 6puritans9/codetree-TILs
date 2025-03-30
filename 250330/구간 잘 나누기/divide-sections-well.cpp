#include <iostream>
#include <vector>

using namespace std;

bool can_partition(int n, int m, vector<int>& numbers, int max_sum){
    int cur_sum = 0;
    int partitions = 1;

    for (int num: numbers){
        if (num > max_sum){
            return false;
        }
        
        if (cur_sum + num > max_sum) {
            partitions += 1;
            if (partitions > m){
                return false;
            }
            cur_sum = num;
        }
        else {
            cur_sum += num;
        }
    }
    return true;
}

int find_minimized_max_subset_sum(int n, int m, vector<int>& numbers) {
    int low = 0; // max(numbers)
    int high = 0; // sum(numbers)
    for (int num: numbers){
        if (num > low){
            low = num;
        }
        high += num;
    }
        
    int best_max_sum = high;

    while (low <= high){
        int mid = (low + high) / 2;

        if (can_partition(n, m, numbers, mid)){
            best_max_sum = mid;
            high = mid - 1;
        }
        else{
            low = mid + 1;
        }
    }

    return best_max_sum;
}

int main() {
    int n, m; cin >> n >> m;
    vector<int> numbers(n);
    for (int i=0; i<n; i++){
        cin >> numbers[i];
    }

    int result = find_minimized_max_subset_sum(n, m, numbers);
    cout << result << endl;
    
    return 0;
}