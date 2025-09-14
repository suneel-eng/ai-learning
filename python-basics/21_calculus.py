# In machine learning, calculus is used to:
# Optimize models (find the best weights)
# Compute gradients (direction to adjust weights)
# Understand loss functions (how far predictions are from reality)
# Without calculus, neural networks wouldn’t know how to improve during training.

# Simple derivative example
def f(x):
    return x**2

def derivative(x):
    return 2*x

x = 3
print("f(x):", f(x))
print("f'(x):", derivative(x))
