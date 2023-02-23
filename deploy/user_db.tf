resource "aws_dynamodb_table" "users" {
  name = "users"
  hash_key = "id"
  range_key = "creation_date"
  
  attribute {
    name = "id"
    type = "S"
  }

  attribute {
    name = "creation_date"
    type = "S"
  }

  attribute {
    name = "email"
    type = "S"
  }

  global_secondary_index {
    name = "email-index"
    hash_key = "email"
    range_key = "creation_date"
    projection_type = "KEYS_ONLY"
    write_capacity = 1
    read_capacity = 1
  }

  read_capacity = 1
  write_capacity = 1
}