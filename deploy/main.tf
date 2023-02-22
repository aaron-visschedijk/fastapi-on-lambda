resource "aws_lambda_function" "lambda" {
  function_name = var.project_name
  role          = aws_iam_role.lambda_role.arn
  handler       = "main.handler"

  s3_bucket = data.aws_s3_bucket.lambda_bucket.id
  s3_key = "${var.project_name}/lambda-pkg-${var.build_tag}.zip"

  runtime = "python3.9"
}

resource "aws_lambda_function_url" "lambda_url" {
  function_name      = aws_lambda_function.lambda.arn
  authorization_type = "NONE"
}