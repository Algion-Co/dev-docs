# O

## Oracle

A source of 'perfect' ground truth information.

- **Theoretical oracle:** In theory and algorithm design, an oracle is a
  hypothetical entity that can instantly provide the correct answer to a
  specific query or problem. For example:

  - In active learning, an oracle is assumed to provide the correct label for a
    given data point when asked.
  - In optimization, an oracle might return the optimal solution, gradient, or
    subgradient for a given point.

- **Labeling oracle:** In practical ML, especially active learning, an oracle is
  often a human annotator (like a domain expert) who provides the correct labels
  when queried. The model may ask the oracle to label only the most informative
  samples to reduce labeling cost.

- **Evaluation oracle:** Sometimes, especially in simulations or research, an
  oracle is a component that simulates the "true environment" to evaluate model
  performance, generate feedback, or produce the next state in reinforcement
  learning.
