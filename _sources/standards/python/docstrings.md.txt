## Docstrings

### Docstring Style

- Use Google style docstrings as these are easier to read than reStructuredText
  or the Numpy style. An example can be found
  [here](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).

- Acronyms and abbreviations in docstrings need to be defined once, as close to
  the beginning as possible, per module.

- For default values, add `Defaults to <value>` at the and of the argument
  description. Even though the enclose in pairs of backticks, with the exception
  of numerical values. There is no need to add the quotes for strings as that is
  implied.

- Document a single return value as follows (note the indentation levels):

  ```python
  """
  Returns:
      <rtype>:
          <Description>
  """
  ```

  The RTD theme will detect the return type automatically.

  Where the value is an iterable, give the shape in the description e.g.

  ```python
  """
  Returns:
      numpy.array:
          A numpy array of shape (n_classes, n_classes) representing the input.
  """
  ```

- If a function does not return a value, be explicit that it does not return a
  value i.e. returns `None` as follows:

  ```python
  """
  Returns:
      `None`
  """
  ```

  Note that `None` is a keyword; therefore, enclose in pairs of backticks.
