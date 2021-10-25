#include <stdio.h>
main()
{
  int max=0,b[9],a;
  for(int i = 0; i<9; i++)
  {
    scanf("%d",&b[i]);
    if(max<=b[i]) max = b[i],a=i+1;
  }
  printf("%d\n%d",max,a);
}
