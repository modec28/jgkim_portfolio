#include <stdio.h>
main()
{
  int a,b;
  scanf("%d",&a);
  scanf("%d",&b);
  int c = a*b;
  printf("%d\n",a*(b%10));
  printf("%d\n",a*((b/10)%10));
  printf("%d\n",a*(b/100));
  printf("%d",c);
}
