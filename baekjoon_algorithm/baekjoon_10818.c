//10818

#include <stdio.h>
main()
{
  int a,max = -1000000,min = 1000000;
  scanf("%d",&a);
  int b[a];
  for(int i = 0; i<a; i++)
  {
    scanf("%d",&b[i]);
    if(max<=b[i]) max = b[i];
    if(min>=b[i]) min = b[i];
  }
  printf("%d %d",min,max);
}
