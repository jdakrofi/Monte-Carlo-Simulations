//
// Created by Joshua Akrofi on 28/08/2024.
//
/*
 *This code uses a Monte Carlo simulation to estimate the value of π (pi).
 *The program will randomly generate points in a square and count how many fall within a quarter circle inscribed within that square.
 * By calculating the ratio of points inside the quarter circle to the total number of points, we can estimate the value of π.
 */
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <cmath>

// Function to run the Monte Carlo simulation
double estimatePi(int numSamples) {
    int pointsInsideCircle = 0;

    // Seed the random number generator
    std::srand(static_cast<unsigned>(std::time(0)));

    // Perform the simulation
    for (int i = 0; i < numSamples; ++i) {
        // Generate random point (x, y) in the range [0, 1)
        double x = static_cast<double>(std::rand()) / RAND_MAX;
        double y = static_cast<double>(std::rand()) / RAND_MAX;

        // Check if the point is inside the quarter circle
        if (x * x + y * y <= 1.0) {
            pointsInsideCircle++;
        }
    }

    // Estimate π using the ratio of points inside the circle to total points
    return 4.0 * pointsInsideCircle / numSamples;
}

int main() {
    int numSamples;

    // Get the number of samples from the user
    std::cout << "Enter the number of samples for the Monte Carlo simulation: ";
    std::cin >> numSamples;

    // Estimate π
    double piEstimate = estimatePi(numSamples);

    // Output the result
    std::cout << "Estimated value of Pi using " << numSamples << " samples: " << piEstimate << std::endl;

    return 0;
}
