terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region = "eu-central-1"
}

backend "s3" {
  bucket         = "annomate-terraform-state"
  key            = "lambda"
  region         = "eu-central-1"
  dynamodb_table = "terraform-lock"
}
