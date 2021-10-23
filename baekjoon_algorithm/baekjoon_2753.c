#include <stdio.h>
main()
{
  int a;
  scanf("%d",&a);
  int y = 0;
  if((a % 4 == 0 && a % 100 != 0) || a % 400 == 0)
  {
    y = 1;
  }
  printf("%d", y);
}
