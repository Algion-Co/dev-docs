## Machine Learning Project Structure

Machine learning projects should generally be structured as follows:

```
project-root/
  |- doc/
  |- data/
  |- src/
       |- <pipeline_modules>
  |- .gitignore
  |- environment.yaml
  |- params.yaml
  |- pyproject.toml
  |- README.md
  |- requirements.txt
```

A description of the files and directories is given below:

<div class="table-container">
  <b>AI/ML Project Structure</b>
  <div class="table-wrapper">
    <table>
      <thead>
        <tr>
          <th>File / Directory</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>doc</code></td>
          <td>Documentation directory. Typically applies to libraries and concerns Sphinx documentation but any reasonable exceptions are accepted.</td>
        </tr>
        <tr>
          <td><code>data</code></td>
          <td>Datasets directory. Datasets should be tracked with DVC and ignored by Git. Refer to [Datasets standards](#) for further details on how datasets should be structured.</td>
        </tr>
        <tr>
          <td><code>src</code></td>
          <td>Source code directory. Contains the implementation of the project's core functionality, organised into pipeline modules or subdirectories. Refer to the [Pipeline Stages](#) table below for further details.</td>
        </tr>
        <tr>
          <td><code>.gitignore</code></td>
          <td>Specifies files and directories that should be ignored by Git, such as large files tracked by DVC or sensitive configurations. See [Gitigore Templates](#).</td>
        </tr>
        <tr>
          <td><code>environment.yaml</code></td>
          <td>Defines the Conda environment, listing dependencies required to run the project. This should only include packages installed using Conda. Packages installed using pip (which is the majority of the dependencies) should be specified in `requirements.txt`.</td>
        </tr>
        <tr>
          <td><code>params.yaml</code></td>
          <td>Configuration file for specifying parameters used in the pipeline.</td>
        </tr>
        <tr>
          <td><code>pyproject.toml</code></td>
          <td>Project metadata and configuration file for Python builds and dependency management tools. Typically applies to libraries but any reasonable exceptions are accepted.</td>
        </tr>
        <tr>
          <td><code>README.md</code></td>
          <td>Project overview, usage instructions, and additional information to help users understand and work with the project. See [README Template](#). </td>
        </tr>
        <tr>
          <td><code>requirements.txt</code></td>
          <td>Lists Python (pip) dependencies for the project. Refer to [`requirements.txt`](#) for best practices with regards to the file.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

```{note}

They may be cases where multiple projects, each with the structure described
above, will need to be grouped together into a single parent directory.
```

<!--
TODO:
- featurise.py
- infer.py
- evaluate.py [Can include speed evaluation]
- export.py
- models.py
- prepare.py
- train.py
-->
