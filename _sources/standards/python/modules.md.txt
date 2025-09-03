## Modules

### Module Structure

### Module Header

Each Python module should have the following dunder variables after the module
docstring and before the module imports:

```python
__author__ = "<name(s) of author(s)>"
__copyright__ = "Copyright <year of creation>, Company X"
__date__ = "10 December 2024"
__maintainer__ = "<name(s) of maintainer(s)>"
__email__ = "<email(s) of maintainer(s)>"
```

The following is an example:

```python
__author__ = "Jane Doe, Richard Roe"
__copyright__ = "Copyright 2024, Company X"
__date__ = "10 December 2024"
__maintainer__ = "Jane Doe, John Smith, Alice Johnson"
__email__ = "jane@companyx.com, john@companyx.com, alice@companyx.com"
```

The table below explains the dunder variables in more detail:

<div class="table-container">
  <b>Module Dunder Variables</b>
  <div class="table-wrapper">
    <table>
      <thead>
        <tr>
          <th>Field</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>author</code></td>
          <td>The full name(s) and initial(s) (if relevant) of the author(s) or developer(s) with significant contributions to the module. Multiple authors or major contributors should be listed in a single string with commas separating each author.</td>
        </tr>
        <tr>
          <td><code>copyright</code></td>
          <td>Copyright notice. This should use the year in which the module was created.</td>
        </tr>
        <tr>
          <td><code>date</code></td>
          <td>For now, this is the date on which the module was created. In the future, we use pre-commit hooks to automatically modify the date to the last update date.</td>
        </tr>
        <tr>
          <td><code>maintainer</code></td>
          <td>The full name(s) and initial(s) (if relevant) of the point(s) of contact for support regarding the module. Multiple maintainers should be listed in a single string with commas separating each maintainer.</td>
        </tr>
        <tr>
          <td><code>email</code></td>
          <td>The email(s) of the maintainer(s). Multiple emails should be listed in a single string with commas separating each email. They should also be ordered in the same order as the list of maintainers.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

- We do not use `__version__` because it could get a bit hairy managing version
  information in multiple files. It is also not so necessary as the version
  information really needed is the project version information which can be
  stored in a more accessible location.

### Module Imports
