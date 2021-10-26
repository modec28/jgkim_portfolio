#include <stdio.h>

main()
{
  int a;
  scanf("%d",&a);
  for(int i = 0; i < a; i++)
  {
    int b,count = 0;
    float  d = 0;
    scanf("%d",&b);
    int c[b];
    for(int j = 0; j < b; j++)
    {
      scanf("%d",&c[j]);
      d += c[j];
    }
    d /= b;
    for(int j = 0; j < b; j++)
    {
      if(c[j]>d)
      {
        count ++;
      }
    }
    printf("%.3f%%\n",(float)count/b*100);
  }
}
