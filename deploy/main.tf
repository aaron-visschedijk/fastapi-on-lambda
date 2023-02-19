resource "aws_iam_role" "iam_for_lambda" {
  name = "iam_for_lambda"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_lambda_function" "lambda" {
  function_name = var.project_name
  role          = aws_iam_role.iam_for_lambda.arn
  handler       = "lambda_handler"

  s3_bucket = data.aws_s3_bucket.lambda_bucket.id
  s3_key = "/terraform-aws-lambda-pipeline/lambda-pkg-2f9732ca46c899caca2fc3a4d424cfc937e3b745.zip"

  runtime = "python3.9"
}