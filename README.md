# How to get your Kube token?

- Log into the machine from where you manage your kubernetes clusters. 
-- Check by running the command - `kubectl config view`
-- If this shows you a list of k8s clusters, then you are in the right place. Else ask someone.
- Check if python3 is installed. This script needs python3+. 
-- Run this command to find out = `python3 --version` 
-- If this shows you a version which is > 3.0, then it is installed. 
-- If it is not installed, go through this link to install - https://www.python.org/downloads/
- If you are in the right place and python3 is installed:
-- Run this command to download the token generation script - `wget https://github.com/DrDroidLab/droid-cli/blob/main/scripts/generate_kube_token.py`
-- Run command - `python3 generate_kube_token.py`
- This output you are seeing is the token that you need to pass to the `droid configure` command prompt.

# How to generate your AWS Key ID and Secret Access Key?
- Log onto your AWS account which hosts your infrastructure and manages your EKS clusters.