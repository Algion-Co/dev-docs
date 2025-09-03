## Collections

- To check if sequences are empty, in accordance with
  [PEP 8](https://peps.python.org/pep-0008/), use the fact that empty sequences
  are false:

  ```python
  # Good:
  if not seq:
  if seq:

  # Bad:
  if len(seq):
  if not len(seq):
  ```
