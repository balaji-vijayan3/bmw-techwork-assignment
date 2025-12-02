########################################
# AWS Provider
########################################
provider "aws" {
  region = "us-east-1"  
}

########################################
# S3 Bucket Resource 
########################################
resource "aws_s3_bucket" "Assignment_bucket" {
  bucket = "bmw-assignment-s3-bucket"  
}

