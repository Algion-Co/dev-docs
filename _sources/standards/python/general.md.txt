## General Rules

- Use type hinting. See [Type Hints](#) section.
- Write docstrings for all functions save for exempt functions. See
  [Docstrings](#) section.
- Comment your code. Some things may be easy to follow as you are working on the
  code but when you come back a year later, you will need to sit for an hour to
  understand it.
- Do not leave any lines of code commented out because that is confusing. If you
  really must, have another comment that states why it was commented out.
- Always use key word arguments for calling functions/methods you wrote yourself
  because when you change things around, you will need to alter that everywhere
  else you called the function. The situation becomes worse when the wrong
  arguments is of the same type as the new argument; then the function will
  happily use the wrong argument.
