terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0.0"
    }
  }

  backend "s3" {
    bucket         = "annomate-terraform-state"
    key            = var.project_name
    region         = "eu-central-1"
    dynamodb_table = "terraform-lock"
  }
}
