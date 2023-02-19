variable "env" {
  type    = string
  default = "dev"
}

variable project_name {
  type = string
}

variable build_tag {
  type = string
}

variable "aws_region" {
  type    = string
  default = "eu-central-1"
}

variable "lambda_bucket" {
  type = string
  default = "annomate-lambdas"
}