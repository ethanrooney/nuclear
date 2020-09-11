#include	<stdlib.h>
#include	<stdio.h>
#include	<math.h>
#include  <time.h>

#define TRUE 1
#define FALSE 0


int main(int argc, char** argv)
{ 
  double l=atof(argv[1]);
  double beta=acos(1-l*l*0.5);
  double a[]={0,0};
  double b[]={1,0};
  double c[]={cos(beta),sin(beta)};
  double d[]={0,0};
  double e[]={0,0};
  double f[]={0,0};
  double g[]={0,0};
  
  double ab[2];
  double ac[2];
  double cb[2];
  double de[2];
  double gf[2];
  
  double fcan0[2];
  double fcan1[2];
  double fcan2[2];

  srand48(time(0));

  rand_unit(d);
  rand_unit(e);
  rand_unit(f);
  rand_unit(g);

  mkline(ab, a, b);
  mkline(ac, a, c);
  mkline(cb, c, b);
  mkline(de, d, e);
  mkline(gf, g, f);
  
  printf("a=(%f,%f)\n", a[0], a[1]);
  printf("b=(%f,%f)\n", b[0], b[1]);
  printf("c=(%f,%f)\n", c[0], c[1]);
  printf("d=(%f,%f)\n", d[0], d[1]);
  printf("e=(%f,%f)\n", e[0], e[1]);
  printf("f=(%f,%f)\n", f[0], f[1]);
  printf("g=(%f,%f)\n", g[0], g[1]);

  candidate(de, ab, fcan0);
  candidate(de, ac, fcan1);
  candidate(de, cb, fcan2);
  isBetween(a,fcan0,b);
  isBetween(a,fcan1,c);
  isBetween(c,fcan2,b);
}
