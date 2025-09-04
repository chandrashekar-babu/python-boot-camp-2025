#include <stdio.h>

int main()
{
    int i = 10;
    int j = 11;

    j += j++ + ++i; /* Whoa! */
    printf("i = %d, j = %d\n", i, j);
    return 0;
}