# tf_python_restapi
create a python flask restapi using terraform and ansible

We create an EC2 instance using Terraform

We provision the EC2 instance using Ansible playbook Install_restapi.yml

We use Python and Flask to create a Rest Api.  The python code and the Dockerfile are in the code folder.

The docker image is built and run with Ansible.

Once completed Terraform outputs the EC2 public ip.

We can then check that the rest api container is running with the following command:

curl <EC@ public ip>:5000/store

with response:
[] -- this means no stores 

We can post a store as follows:

curl --location '<EC@ public ip>:5000/store?store=fruits' --header 'Content-Type: application/json' --data '{"name": "fruits"}'

curl <EC@ public ip>:5000/store

response:
[
  {
    "id": 1,
    "items": [],
    "name": "fruits"
  }
]







