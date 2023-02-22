resource "aws_dynamo_db" "users" {
  name = "users"
  hash_key = "id"
  hash_key_type = "S"
  read_capacity = 1
  write_capacity = 1
}