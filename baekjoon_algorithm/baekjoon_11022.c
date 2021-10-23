#include <stdio.h>
main()
{
  int a;
  scanf("%d",&a);
  for(int i = 0;i<a;i++)
  {
    int b,c;
    scanf("%d %d",&b,&c);
    printf("Case #%d: %d + %d = %d\n",i+1,b,c,b+c);
  }
}
