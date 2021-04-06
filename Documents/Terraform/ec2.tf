provider "aws" {
    access_key = ""
    secret_key = ""
    region = "us-east-1"
  
}

resource "aws_instance" "database" {
    ami = "ami-0915bcb5fa77e4892"
    instance_type = "t2.small"
  
}

resource "aws_s3_bucket" "mypower-database-bucket" {
  
}