#include	<stdlib.h>
#include	<stdio.h>
#include	<math.h>
#include  <complex.h>

double PI =		3.1415926535897932385;

double complex f(double complex* x, double complex* res)
{
  double complex k = csqrt((3-2*x[0]-x[0]*x[0])*exp(x[0]));
	res[0] = k*cexp(I*k*x[0]);
  res[1] = x[1]
}

double complex integratemiddle(double a, double b, long int N)
{
	double delx = (b - a)/N;
	double complex res = f(a);
  double position = a;

	for(long long int i=0; i<N; i++)
	{
    printf("Psi(%5.5lf)=%5.5lf + %5.5lfi \n", position, creal(res), cimag(res));
    position += delx;
		res -= delx*f(a+delx*i+0.5*delx); //you don't need to put in {} if it is a single line statment
	}
  printf("Psi(%5.5lf)=%5.5lf + %5.5lfi \n", position, creal(res), cimag(res));

	return res;
}

int main(int argc, char** argv)
{
	if(argc == 2)
	{
		double complex resMiddle = integratemiddle(1, 0, atoi(argv[1]));
	}
	else
	{
		printf("You must provide an integer number between 1 and 2147483647\n");
	}
}

