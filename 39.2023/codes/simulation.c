#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double gammaCDF(double x, int n) {
    double result = 1;
    for (int i = 1; i <= n - 1; ++i) {
        result *= x / i;
    }
    double cdf = 1 - exp(-x) * result;
    // Ensure CDF is between 0 and 1
    if (cdf < 0) {
        return 0;
    } else if (cdf > 1) {
        return 1;
    }
    return cdf;
}

int main() {
    int n = 5; // Shape parameter
    int numPoints = 100; // Number of points for the graph
    double start = 0.1; // Start value for x
    double end = 5.0; // End value for x
    double step = (end - start) / numPoints; // Step size

    // Calculate and store CDF values for a range of input values
    for (double x = start; x <= end; x += step) {
        double cdf = gammaCDF(n * x, n);
        printf("%lf %lf\n", x, cdf); // Print x and corresponding CDF value
    }

    return 0;
}

