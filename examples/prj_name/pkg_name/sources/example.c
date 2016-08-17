#include "example.h"
#include "ncephes/cprob.h"

double sum(double a, double b)
{
    return a + b + ncephes_incbet(1, 3, 0.3);
}
