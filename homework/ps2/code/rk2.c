#include	<stdlib.h>
#include	<stdio.h>
#include	<math.h>
#include	<complex.h>


double complex k(double x, double energy)
{
  return csqrt(energy-(3-2*x-x*x)*exp(x));
}

void f( double complex* vect, double complex* res , double x, double energy)
{
	res[1] = k(x, energy)*cexp(I*k(x, energy)*x);
	res[0] = vect[1]; //dx/dt = v_x
}


void integrate_rk2(double complex* y, double dx, double complex* yn, double x, double energy)
{
	double complex k1[2], k2[2];
	double complex yhalf[2];

	f(y, k1, x, energy);

	yhalf[0]= y[0] + 0.5*dx*k1[0];
	yhalf[1]= y[1] + 0.5*dx*k1[1];

	f(yhalf, k2, x, energy);

	yn[0] = y[0] + k2[0]*dx;
	yn[1] = y[1] + k2[1]*dx;
}

int main(int argc, char** argv)
{
	if(argc != 3)

	{
		printf("This program takes 1 argument: n_steps\n");
		return -1;
	}

	double x = 1;
	double dx = x/atof(argv[1]);
  const double energy = atof(argv[2]);

  for (double e=0; e<energy; e += energy/1000.)
  {
    x=1;
    double complex Psi[2] = {cexp(I*k(x,e)*x), I*cexp(I*k(x, e)*x)};
    double complex Psin[2];
    double bnorm = creal(Psi[0]*conj(Psi[0])); 
    while ( x > 0 )
    {
      integrate_rk2(Psi, dx, Psin, x, e);
      x -= dx;
      Psi[0] = Psin[0];
      Psi[1] = Psin[1];
    }
    double anorm = creal(Psi[0]*conj(Psi[0])); 
    double out = bnorm+anorm;
    double trans = 1./(out);
    double ref = 1.-trans;
    printf(" %15.15f %15.15f %15.15f\n", e, ref, trans);
  }

	return 0;

}
