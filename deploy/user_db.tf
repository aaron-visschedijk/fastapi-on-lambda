resource "aws_dynamodb_table" "users" {
  name = "users"
  hash_key = "id"
  
  attribute {
    name = "id"
    type = "S"
  }


  read_capacity = 1
  write_capacity = 1
}