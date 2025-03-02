# Python Environments Setup

The following is a guide for setting up your Python development environment.

You may need to refer to the [Tech Stacks](#) pages if unfamiliar with the
platforms discussed or for clarity on why they are our standards.

## Virtual Environment

To create a virtual environment, run the command

```
python -m venv <virtual_environment_dir_name>
```

For the virtual environment directory name, use one of the following:

- `.venv` (recommended)
- `.env`
- `venv`
- `env`

These are the standards that will be included in ignore files such as
`.gitignore`.

Activate your virtual environment and install Python packages.

If available for a particular project, you can install packages from a
`requirements.txt` file, using:

```
pip install -r <path_to_requirements.txt_file>
```

Note down each new package you install and its version (excluding its
dependencies) in a new or existing `requirements.txt` file.

## Conda Environment

After downloading Miniconda (recommended) (see
[Miniconda installation documentation](https://www.anaconda.com/docs/getting-started/miniconda/install#quickstart-install-instructions))
or Anaconda (see [Anaconda download page](https://www.anaconda.com/download)),
launch the Miniconda or Anaconda prompt.

Follow steps below to configure a new environment from scratch or configure an
environment from environment files.

```{note}

Follow the steps in the given order as some steps depend on previous ones and
some conflicts may arise if order of steps is not observed.
```

### Setting Up Conda Environment from Scratch

1. Create an Conda environment using:

   ```

   conda create -n <environment-name> [python=x.x] [space-separated-packages]

   ```

   The environment name should be kebab case.

2. Activate your new environment using:

   ```
   conda activate <environment-name>
   ```

3. If using Miniconda, install conda-build using:

   ```

   conda install conda-build

   ```

   This allows you to use such command as `conda develop` which adds paths to
   the Python path and to create Conda packages from pip packages.

4. Add any directories in which you want the Python interpreter to search for
   local packages using

   ```
   conda develop <path_to_local_package_dir>
   ```

5. If not installed already, install pip using;

   ```
   conda install pip
   ```

6. If required, install CUDA and cuDNN. Have a look at
   [Docker Hub PyTorch tags](https://hub.docker.com/r/pytorch/pytorch/tags),
   [Docker Hub TensorFlow tags](https://hub.docker.com/r/tensorflow/tensorflow/tags)
   etc. for combinations of versions which work well together:

   ```
   conda install cuda=xx.x cudnn=x.xx -c nvidia
   ```

   ```{note}

   Ensure that the versions you are installing are compatible with:
   1. The specific version of the deep learning framework you would like to use
   2. The specific version of any SDK you might intend to use e.g. TensorRT
      (which in turn depends on the GPU architecture you are using)
   ```

7. Install Python packages **using pip where possible**. If available, you can
   also install packages from a `requirements.txt` file, using:

   ```
   pip install -r <path_to_requirements.txt_file>
   ```

   We use pip instead of Conda albeit installing into Conda environments
   because:

   - it offers the most up-to-date packages
   - there are several cases where Python packages are available via pip but not
     Conda
   - when you have to use pip for the aforementioned reasons, mixing pip
     packages with Conda packages can result in conflicts and other strange
     things
   - packages can easily be installed via `requirements.txt` files
   - it makes the environment somewhat reproducible in a virtual environment

8. If you intend to use Jupyter

   1. Install `ipykernel` using:

      ```
      pip install ipykernel
      ```

   2. Create a new kernel using:

      ```
      ipython kernel install --user --name=<any-name-for-kernel>
      ```

   The kernel name should be kebab case.

<!--
TODO:
- Discussion of conda channels?
-->
