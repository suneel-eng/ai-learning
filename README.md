# 🧭 Your AI Developer Roadmap (Index)
Here’s the structured path we’ll follow:

## Phase 1: Foundations (Programming, Math, Data)
1. ✅ [Hello world](./python-basics/1_helloWorld.py)

2. ✅ [Variables](./python-basics/2_variables.py)

3. ✅ Data Types

| Type | Example | Description |
|------|---------|-------------|
| Int | ```42``` | Whole numbers |
| float | ```3.14``` | Decimal numbers |
| str | ```"Hello"``` | Text strings |
| bool | ```True, False``` | Boolean values |
| list | ```[1,2,3]``` | Ordered collection |
| dict | ```{"name": "suneel"}``` | Key-value pairs |

4. ✅ [Operators](./python-basics/4_operators.py)

5. ✅ [Control Flow (if, loops)](./python-basics/5_controlFlow.py)

6. ✅ [Functions](./python-basics/6_functions.py)

7. ✅ [Modules](./python-basics/7_modules.py)

8. ✅ [Lists](./python-basics/8_lists.py)

9. ✅ [Dictionaries](./python-basics/9_dictionaries.py)

10. ✅ [Sets](./python-basics/10_sets.py)

11. ✅ [Tuples](./python-basics/11_tuples.py)

12. ✅ [Working with Files](./python-basics/12_workingWithFiles.py)

13. ✅ [Reading csv file](./python-basics/13_readingCsvFile.py)

14. ✅ [Object-Oriented Programming](./python-basics/14_OOP.py)

15. ✅ [NumPy Basics](./python-basics/15_numpy_basics.py)

16. ✅ [Introduction to Pandas](./python-basics/16_intro_to_pandas.py)

17. ✅ [Data Cleaning & Preprocessing](./python-basics/17_data_cleaning.py)

| Task | Purpose |
|------|---------|
| Handling missing data | Fill or remove gaps |
| Removing duplicates | Avoid bias and redundancy |
| Type conversion | Ensure correct formats |
| Normalization | Scale values for better learning |
| Encoding categories | Convert text to numbers |

18. ✅ [Basic Statistics](./python-basics/18_basic_statistics.py)

Statistics helps you:
- understand data distributions
- detect outliers and patterns
- evaluate model performance
- make data driven decissions

Key concepts:
| Concept | Meaning | Python example |
|---------|---------|----------------|
| Mean | Average value | ```np.mean(data)``` |
| Median | Middle value | ```np.median(data)``` |
| Mode | Most frequent value | ```stats.mode(data)``` |
| Variance | Spread of data from the mean | ```np.var(data)```|
| Standard deviation | Average distance from the mean | ```np.std(data)``` |
| Range | Difference between max and min | ```np.max(data) - np.min(data)``` |

19. ✅ [Probability Concepts](./python-basics/19_probability_basics.py)

| Term | Meaning | Example |
|------|---------|---------|
| Experiment | Any process with an uncertain outcome | Tossing a coin |
| Outcome | Result of an experiment | Heads |
| Event | A set of outcomes | Getting heads |
| Probability | Measure of likelihood (0 to 1) | 0.5 for heads in a fair coin |

Basic formula:
<math>
    <mtable>
        <mtr>
            <mtd>
                <mi>P</mi>
                <mo>(</mo>
                <mi>E</mi>
                <mo>)</mo>
            </mtd>
            <mtd>=</mtd>
            <mtd>
                <mfrac>
                    <mi>Number of favorable outcomes</mi>
                    <mi>Total outcomes</mi>
                </mfrac>
            </mtd>
        </mtr>
    </mtable>
</math>

Types of Probability

1) Independent events: One event doesn’t affect the other Example: Tossing two coins
2) Dependent events: One event affects the other Example: Drawing cards without replacement
3) Conditional probability: Probability of A given B

Linear Algebra Essentials

Calculus for ML

SQL for Data Querying

Data Visualization (Matplotlib, Seaborn)

## Phase 2: Machine Learning Core
What is Machine Learning?

Supervised vs Unsupervised Learning

Regression Algorithms

Classification Algorithms

Clustering Algorithms

Model Evaluation Metrics

Overfitting & Underfitting

Feature Engineering

Cross-Validation

Hyperparameter Tuning

Scikit-Learn in Practice

Building Your First ML Model

Project: Predict House Prices

## Phase 3: Deep Learning & Neural Networks
What is Deep Learning?

Neural Network Architecture

Activation Functions

Forward & Backpropagation

Loss Functions

Optimizers (SGD, Adam)

TensorFlow Basics

Keras for Model Building

CNNs for Image Data

RNNs for Sequence Data

LSTMs & GRUs

Project: Image Classification

Project: Text Sentiment Analysis

## Phase 4: NLP & Transformers
NLP Basics

Text Preprocessing

Word Embeddings

BERT & Transformers

Hugging Face Transformers

Fine-Tuning Pretrained Models

Project: Chatbot or Text Summarizer

## Phase 5: MLOps & Deployment
Model Deployment Basics

Flask/FastAPI for ML APIs

Docker for ML

CI/CD for ML

AWS SageMaker

Monitoring & Logging

Project: Deploy ML Model to AWS

## Phase 6: Advanced Topics
Reinforcement Learning

Generative AI (GANs, Diffusion Models)

Ethics in AI

AI for Edge Devices

Building Your Own Dataset

Custom Model Training

Final Capstone Project