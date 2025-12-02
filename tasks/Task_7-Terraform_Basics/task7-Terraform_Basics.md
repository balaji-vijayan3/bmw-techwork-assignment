This task demonstrates how to provision an Amazon S3 bucket using Terraform.
It includes:

Setting up AWS credentials

Creating a Terraform configuration file (main.tf)

Initializing Terraform

Reviewing the execution plan

Applying the infrastructure changes

The bucket is created using default private settings (no ACL and no versioning).

2. Prerequisites
✔ AWS CLI installed
✔ AWS credentials configured

To configure AWS credentials on the VM:

aws configure


Provide:

AWS Access Key ID

AWS Secret Access Key

Default region (e.g., us-east-1)

Output format (json)

You can verify credentials with:

aws sts get-caller-identity


3. Terraform Configuration (main.tf)

Use the following modern, compliant configuration (no ACLs, no versioning):

########################################
# AWS Provider
########################################
provider "aws" {
  region = "us-east-1"
}

########################################
# S3 Bucket (default private)
########################################
resource "aws_s3_bucket" "Assignment_bucket" {
  bucket = "bmw-assignment-s3-bucket"   # Must be globally unique
}

4. Command Used

terraform init - This downloads the AWS provider and prepares the working directory.

terraform plan - Terraform shows what resources will be created, changed, or destroyed.

terraform apply - The S3 bucket will be created.

Do you want to perform these actions?
Enter a value: yes

terraform destroy - To delete the created the resources

######################################################################################3



