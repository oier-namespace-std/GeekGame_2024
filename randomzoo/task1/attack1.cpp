#include <cstring>
#include <fstream>
#include <iostream>
#include <cstdio>
using namespace std;
char flag[100];
int flag_len;
unsigned int rand_init;
int main(int argc, char **argv){
    long long x;
    std::cin>>x;
    unsigned z = 0;
    if(argc == 2)
        z = atoi(argv[1]);
    for(unsigned i = z; ; i++)
    {
        //if(i % 1000000 == 0)
        //    fprintf(stderr,"i: %d\n", i);
        srand(i);
        if((long long)rand() + (long long)'f' == x) {
            // std::cout<<i<<std::endl;
            printf("f");
            for(int z = 1; z <= 200; z++)
            {
                long long f;
                std::cin>>f;
                f = f - (long long)rand();
                printf("%c", char(f));
            }
            return 0;
        }
    }
}


// [5]   Done                    ./attack1 400000000 < input.txt
// flag{Do_Y0U_enUmEraTed_a1l_Se3d5?}flag{Do_Y0U_enUmEraTed_a1l_Se3d5?}flag{Do_Y0U_enUmEraTed_a1Qܾ[���C�e_�;��A>��;%N�*�P���tm$6*�A/�!����������
