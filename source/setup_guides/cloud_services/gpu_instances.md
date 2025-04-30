# GPU Instance Setup

The following is a general setup guide for GPU instances.

<!-- Consider moving 1 to a Linux setup or something and putting link here -->

1.  Install CUDA Toolkit and NVIDIA drivers.

    ```{note}

    Be very careful when doing this installation as mistakes may be very
    difficult to revert.
    ```

    To install CUDA Toolkit and NVIDA, follow the instructions on the NVIDIA
    [CUDA Downloads page](https://developer.nvidia.com/cuda-downloads). It is
    unclear whether you need the entire CUDA Toolkit to use GPUs; however,
    install it anyway.

    For 'Installer Type' choose **deb local** and for the driver, install the
    **open kernel module flavor**.

    When installation is done, as per the recommendation of
    [this Ask Ubuntu answer](https://askubuntu.com/a/885627/1737528), add CUDA
    to the `.bashrc` file as follows:

    1. Open `/home/&lt;username&gt;/.bashrc` with your text editor of choice.

    2. Inside the file (typically at the bottom unless an export line already
       exists), add the export statements below. If an export line is present,
       append the path to it, separating paths with. (Replace cuda-12.8 with
       your version).

       ```
       export PATH="$PATH:/usr/local/cuda-12.8/bin"
       export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/cuda-12.8/lib64"
       ```

    3. Save and close the editor.

    4. Either run `source .bashrc` or close the current terminal and open a new
       one.

    Now check that the drivers are working by running:

    ```
    nvidia-smi
    ```

    This should give you an output similar to:

    ```
     +-----------------------------------------------------------------------------------------+
     | NVIDIA-SMI 570.86.10              Driver Version: 570.86.10      CUDA Version: 12.8     |
     |-----------------------------------------+------------------------+----------------------+
     | GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
     | Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
     |                                         |                        |               MIG M. |
     |=========================================+========================+======================|
     |   0  Quadro T1000                   Off |   00000000:01:00.0 Off |                  N/A |
     | N/A   47C    P8              1W /   50W |       5MiB /   4096MiB |      0%      Default |
     |                                         |                        |                  N/A |
     +-----------------------------------------+------------------------+----------------------+

     +-----------------------------------------------------------------------------------------+
     | Processes:                                                                              |
     |  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
     |        ID   ID                                                               Usage      |
     |=========================================================================================|
     |    0   N/A  N/A            2059      G   /usr/lib/xorg/Xorg                        4MiB |
     +-----------------------------------------------------------------------------------------+
    ```

    Also check that the CUDA compiler driver is working by running

    ```
    nvcc --version
    ```

    See the [CUDA and NVIDIA Troubleshooting page](#) if you encounter any
    challenges.

2.  Install Minicoda (recommended) or Anaconda.

    To install Miniconda or Anaconda, see the
    [Miniconda installation documentation](https://www.anaconda.com/docs/getting-started/miniconda/install#quickstart-install-instructions))
    or the Anaconda (see
    [Anaconda download page](https://www.anaconda.com/download))

3.  Install Docker.

    To install Docker, see the
    [Install Docker Engine page](https://docs.docker.com/engine/install/) and
    follow the link to your specific operating system.
