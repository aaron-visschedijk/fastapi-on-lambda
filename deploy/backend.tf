terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.10.0"
    }
  }

  backend "s3" {
    bucket         = "annomate-terraform-state"
    key            = "service/dev/test"
    region         = "eu-central-1"
    dynamodb_table = "terraform-lock"
  }
}
