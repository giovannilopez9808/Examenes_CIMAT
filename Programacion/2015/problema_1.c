#include <stdio.h>
#include <string.h>
int main()
{
    int count = 0;
    int select = 1;
    char zero[] = "0";
    char a[] = "a";
    char list[15][2] = {"a",
                        "d",
                        "a",
                        "a",
                        "f",
                        "a",
                        "g",
                        "r",
                        "r",
                        "a",
                        "0"};
    while (strcmp(list[select], zero) != 0)
    {
        if (strcmp(list[select - 1], a) != 0 && strcmp(list[select + 1], a) != 0)
        {
            count++;
        }
        select++;
    }
    printf("Existen %i letras que cumplen la condicion\n", count);
}
