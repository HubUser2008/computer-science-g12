#include <stdio.h>
//#include "cs3u.h"

int main(void) {
    char npcs[3][7]={"Bethan","Blucas", "Boliver" };
    char statorder[4][14]={"strength", "dexterity", "intelligence","charisma"};
    for(int i = 0; i<4;i++){
        //printf("%s",npcs[i]);
    }
    int stats[3][4] =  {{2,3,4,6},{1,7,8,9},{3,4,2,9}};
    stats[1][3] = 7;

    for(int i=0; i<3; i++){
        printf("Character %s \n",npcs[i]);{
        for(int j=0;j<4;j++){
            printf("%s : %d",statorder[j],stats[i][j]);
            printf("\n");
        }
    }
}
}
