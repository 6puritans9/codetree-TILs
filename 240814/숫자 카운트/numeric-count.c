#include <stdio.h>

int main() {
    int N;
    scanf("%d", &N);

    int guesses[N][3];
    int count1[N], count2[N];

    for(int i =0; i < N; i++){
        int guess;
        scanf("%d %d %d", &guess, &count1[i], &count2[i]);

        // hundreds
        guesses[i][0] = guess / 100; 
        // tens
        guesses[i][1] = (guess / 10) % 10;
        // units
        guesses[i][2] = guess % 10; 
    }

    int valid_count = 0;

    for(int d1 = 0; d1 < 9; d1++){
        for (int d2 = 0; d2 < 9; d2++){
            for(int d3 = 0; d3 < 9; d3++){
                if(d1 == d2 || d2 == d3 || d3 == d1)
                    continue;

                int is_valid = 1;

                for(int i = 0; i < N; i++){
                    int actual_count1 = 0;
                    int actual_count2 = 0;
                    
                    if(d1 == guesses[i][0]) actual_count1++;
                    if(d2 == guesses[i][1]) actual_count1++;
                    if(d3 == guesses[i][2]) actual_count1++;

                    if(d1 == guesses[i][1] || d1 == guesses[i][2]) actual_count2++;
                    if(d2 == guesses[i][0] || d2 == guesses[i][2]) actual_count2++;
                    if(d3 == guesses[i][0] || d3 == guesses[i][1]) actual_count2++;

                    if(actual_count1 != count1[i] || actual_count2 != count2[i]){
                        is_valid = 0;
                    }
                }

                if(is_valid)
                    valid_count++;
            }
        }
    }

    printf("%d\n", valid_count);

    return 0;
}