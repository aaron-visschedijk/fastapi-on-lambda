terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0.0"
    }
  }

  backend "s3" {
    bucket         = "terraform-state"
    key            = "service/VAR_ENV/VAR_KEY"
    region         = "eu-central-1"
    dynamodb_table = "terraform-lock"
  }
}
