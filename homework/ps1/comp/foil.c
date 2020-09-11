#include	<stdlib.h>
#include	<stdio.h>
#include	<math.h>
#include	<time.h>

double case1(double tau, double b)
{
  if(b<0.5*sin(tau))
  {
    return -(M_PI-2.0*tau);
  }
  else return 0;
}

double case2(double tau, double b)
{
  if(b>sin(M_PI/3.0-tau)/sqrt(3.0) && b<sin(tau)/sqrt(3.0))
  {
    return M_PI-2.0*(M_PI/3.0-tau);
  }
  else if (b<sin(M_PI/3.0-tau)/sqrt(3.0) && b<sin(tau-2.0*M_PI/3.0)/sqrt(3.0))
    return -(M_PI-2.0*tau);
  else return 0;
}

double rand_tau()
{
  return drand48()*2.0*M_PI/6.0;
}

double rand_b()
{
  return drand48()*0.5;
} 

int main(int argc, char** argv)
{
  double Theta;
  srand48(time(0));
  for(int i = 0; i<atoi(argv[1]);)
  {
    double tau = rand_tau();
    if(tau<M_PI/6.0)
    {
      Theta=fabs(case1(tau,rand_b()));
    }
    if(tau>M_PI/6.0)
    {
      Theta=fabs(case2(tau,rand_b()));
    }
    if(Theta>0){
      printf("%f\n",Theta);
      i++;
    }
  }
}

