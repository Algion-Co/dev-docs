# Machine Learning Stack

Our tech stack comprises the following components.

Refer to [Setup Guides](#) for details on how to correctly configure some of the
tools and software discussed.

Refer also to the [Python Stack page](#).

## Programming Languages

Our standard for most machine learning and data science projects is Python. When
high performance is essential, we use C++ and for embedded systems with no
requirement for C++ features, we use C.

## Deep Learning Frameworks

### PyTorch

The primary deep learning framework that we use is
[PyTorch](https://pytorch.org/). This is because of its widespread adoption in
the research community which allows us to leverage research very quickly. Read
[OpenAI's blog on why they standardised PyTorch](https://openai.com/index/openai-pytorch/).
There may, however, be rare exceptions where you will need to use
[TensorFlow](https://www.tensorflow.org/) or other deep learning frameworks.

Refer to the [PyTorch website](https://pytorch.org/) for installation details.

```{note}

Use pip even if you are installing into a Conda environment unless you have a
specific reason for doing otherwise. This is discussed in detail in the
[Conda Setup Guide](#).
```

<!-- Link to specific setup guides for each. -->

## Python Environment

Python development should, at all times, be done within a Conda environment or a
virtual environment.

### Conda

For most machine learning projects, use Conda because this allows for
installation of other things such as CUDA and cuDNN within the environment which
creates flexibility to use different versions for different projects with
relative ease.

[Miniconda](https://docs.anaconda.com/miniconda/) is our recommended means to
use the Conda package manager. It is a miniature installation of the Anaconda
distribution which only includes Conda, Python and the packages they depend on.

[Anaconda](https://www.anaconda.com/) is a comprehensive Python and R
distribution that includes the Conda package manager, popular data science
libraries, and development tools like Jupyter notebooks. While it provides a
complete environment with pre-installed packages such as NumPy, Pandas, and
Scikit-learn, the full installation requires several gigabytes of storage space.
Hence, unless you have a specific need for the features of Anaconda, it is
recommended that you use Miniconda.

Refer to the
[Miniconda installation documentation](https://docs.anaconda.com/miniconda/miniconda-install/)
for installation details.

Refer also to the
[Conda Environment section of the Python Environments setup guide](#) for
details on how to set up your Conda environment.

### Virtual Environment

For simple cases or non-machine learning projects, use Python virtual
environments.

Refer to the
[Virtual Environment section of the Python Environments setup guide](#) for
details on how to set up your virtual environment environment.

## MLOps

Machine learning operations (MLOps) are a set of practices that help to manage
the machine learning (ML) life cycle more efficiently. Below are the tools we
use data management, model management, pipeline management etc.

### Data Version Control (DVC)

[Data Version Control (DVC)](https://dvc.org/) is an open-source version control
system specifically designed for dataset version tracking and managing machine
learning models and workflows.

We will only use DVC for dataset version tracking as MLflow is a much better
solution for workflow management.

Refer to the [DVC installation documentation](https://dvc.org/doc/install) for
installation details. It is recommended that you install it as a system
application rather than a Python package so that you can use the software across
various projects as you would Git. However, installing as a Python package is
also fine.

### Apache Airflow

[Apache Airflow](https://airflow.apache.org/) is an open-source
[data orchestration](#) platform that allows you to programmatically author,
schedule and monitor workflows

### MLflow

[MLflow](https://mlflow.org/) is an open-source end-to-end MLOps platform which
we use for experiment tracking, visualisation, evaluation, model registries
among other things.

Refer to the
[MLflow Tracking Quickstart documentation](https://mlflow.org/docs/latest/getting-started/intro-quickstart/index.html)
for installation details.

## DevOps

Refer to [DevOps Stack](#) page.

<!-- Link to DevOps stack -->
