#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Function to generate Gamma CDF from uniform random variable
double gamma_cdf(double x, double alpha, double beta) {
    return 1 - exp(-pow(x / beta, alpha));
}

// Function to generate random uniform variable between 0 and 1
double uniform_random() {
    return (double)rand() / RAND_MAX;
}

int main() {
    int num_simulations = 100000; // Number of simulations
    double alpha = 2.0; // Shape parameter of Gamma distribution
    double beta = 0.5; // Scale parameter of Gamma distribution
    double start_x = 0.1; // Start value of x
    double end_x = 5.0; // End value of x
    double step = 0.1; // Step size for x values

    // Seed for random number generation
    srand(1234);

    // Loop over different x values
    for (double x = start_x; x <= end_x; x += step) {
        int count = 0;

        // Verify Gamma CDF through simulation
        for (int i = 0; i < num_simulations; ++i) {
            double gamma_cdf_value = gamma_cdf(x, alpha, beta); // Calculate Gamma CDF value
            double simulated_value = (double)rand() / RAND_MAX; // Generate uniform random variable for comparison

            // Check if simulated value falls below Gamma CDF value
            if (simulated_value <= gamma_cdf_value) {
                count++;
            }
        }

        // Calculate and print the empirical probability
        double empirical_probability = (double)count / num_simulations;
        printf("%f\n", empirical_probability);
    }

    return 0;
}

