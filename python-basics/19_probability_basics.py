# Machine learning models don’t “know” the future — they estimate the likelihood of outcomes.
# - A spam filter might say: “This email has a 92% probability of being spam.”
# A fraud detection model might say: “This transaction has a 3% probability of being fraudulent.”

import random

trials = 100
heads = 0

for _ in range(trials):
    if random.choice(['H', 'T']) == 'H':
        heads += 1

print("Estimated Probability of Heads:", heads / trials)