Objective

Identify and troubleshoot Terraform errors related to provider authentication and state management in AWS-based infrastructure deployment.

I manually deactivated the Access_Key and Secret_Key from the provider

When running Terraform commands such as:

terraform init
terraform plan

Errour Output:

Error: Retrieving AWS account details: validating provider credentials:
operation error STS: GetCallerIdentity, https response error StatusCode: 403
api error InvalidClientTokenId: The security token included in the request is invalid.


terraform show terraform.tfstate
Error: open terraform.tfstate: no such file or directory

Debug:

Validated AWS CLI authentication

aws sts get-caller-identity
Output:
An error occurred (InvalidClientTokenId) when calling the GetCallerIdentity operation: The security token included in the request is invalid.

Reviewed Terraform AWS provider configuration

provider "aws" {
  region  = "ap-south-1"
  profile = "bmw-assignment"   # Example profile
}

I have enabled the AWS provider Authentication

{
    "UserId": "AIDA5P3RRWDFZE5FTEIZ4",
    "Account": "927414202571",
    "Arn": "arn:aws:iam::927414202571:user/Ansible"
}

Re-initialized Terraform

terraform init
terraform plan

Terraform successfully connected to AWS → resolved the authentication error.

ls
terraform.tfstate


###############################################################################################
