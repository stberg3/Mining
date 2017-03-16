// asm.c
#include <stdio.h>

int main(){
  int i;
  int sum = 0;
  int x = 16;
  // int a[x];

  // for(i=0; i<x; i++) a[i] = i*2;

  for(i=0; i<x; i++) sum += i;

  printf("%d\n", sum);
}
