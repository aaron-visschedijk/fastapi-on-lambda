resource "aws_dynamodb_table" "users" {
  name = "users"
  hash_key = "id"
  read_capacity = 1
  write_capacity = 1
  
  attribute {
    name = "id"
    type = "S"
  }

  attribute {
    name = "email"
    type = "S"
  }

  global_secondary_index {
    name = "email-index"
    hash_key = "email"
    projection_type = "KEYS_ONLY"
    write_capacity = 1
    read_capacity = 1
  }
}