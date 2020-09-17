#include	<stdlib.h>
#include	<stdio.h>
#include	<math.h>
#include	<time.h>

double case1(double tau, double b, double len)
{
  if(b<len*sin(tau))
  {
    return 2.0*tau;
  }
  else return 0;
}

double rand_tau()
{
  return drand48()*2.0*M_PI/4.0;
}

double rand_b()
{
  return drand48()*1.5;
} 

double rand_side(double* array)
{
  return array[lrand48() % 3];
}

int main(int argc, char** argv)
{
  double l = atoi(argv[1]);
  double lengths[] = {1,1,l};
  double Theta;
  srand48(time(0));
  for(int i = 0; i<atoi(argv[2]);)
  {
    double tau = rand_tau();
    Theta=fabs(case1(tau,rand_b(),rand_side(lengths)));
    if(Theta>0){
      printf("%f\n",Theta);
      i++;
    }
  }
}

