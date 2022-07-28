# [How to get your Kube token?](#k8s)

1. Log into the machine from where you manage your kubernetes clusters. 
  1. Check by running the command - `kubectl config view`
  2. If this shows you a list of k8s clusters, then you are in the right place. Else ask someone.
2. Check if python3 is installed. This script needs python3+. 
  * Run this command to find out - `python3 --version` 
  * If this shows you a version which is > 3.0, then it is installed. 
  * If it is not installed, go through [this link](https://www.python.org/downloads/) to install
3. If you are in the right place and python3 is installed:
  * Run this command to download the token generation script - `curl https://raw.githubusercontent.com/DrDroidLab/DrDroidLab.github.io/main/generate_kube_token.py -o generate_kube_token.py`
  * Run command - `python3 generate_kube_token.py`
4. This output you are seeing is the token that you need to pass to the `droid configure` command prompt.

# [How to generate your AWS Key ID and Secret Access Key?](#aws)
1. Log onto your AWS account which hosts your infrastructure and manages your EKS clusters.