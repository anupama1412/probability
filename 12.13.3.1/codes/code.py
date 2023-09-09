import numpy as np

# Define the probabilities of outcomes
probabilities = {
    1: 0.2,
    2: 0.2,
    3: 0.1,
    4: 0.3,
    5: 0.1,
    6: 0.1
}

# Probability of event A: Same number each time
p_event_a = probabilities[1] ** 2 + probabilities[2] ** 2 + probabilities[3] ** 2 + probabilities[4] ** 2 + probabilities[5] ** 2 + probabilities[6] ** 2 

# Probability of event B: Total score is 10 or more
p_event_b = probabilities[4]*probabilities[6] + probabilities[5]*probabilities[5] + probabilities[6]*probabilities[4] + probabilities[5]*probabilities[6] + probabilities[6]*probabilities[5] + probabilities[6]*probabilities[6]

# Probability of both events A and B occurring
p_event_a_and_b = probabilities[5] ** 2 + probabilities[6] ** 2  # (5, 5) and (6, 6) results in both A and B

# Check if A and B are independent
independent = abs(p_event_a_and_b - (p_event_a * p_event_b)) < 1e-6

# Output the results
print(f"Probability of event A (Same number each time): {p_event_a:.4f}")
print(f"Probability of event B (Total score is 10 or more): {p_event_b:.4f}")
print(f"Probability of both events A and B occurring: {p_event_a_and_b:.4f}")
print(f"A and B are {'independent' if independent else 'not independent'}.")


