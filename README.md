

## Setup

# Generate terraform cloud API token
1. go to https://cloud.hashicorp.com/products/terraform
2. sign into your corporation/create your corporation
3. Go to Settings > Teams > Team API Token
4. Generate token and copy to clipboard
5. Go to your github repo
6. Go to Settings > Security > Secrets and Variables > Actions
7. Create a new secret called TF_API_TOKEN and paste the token
8. Click add secret


TODO:
- Clean up terraform/lambda code
- Check if checksum is necessary
- Write a workflow that sets up terraform initially (and check if this is worth it)

later:
- Try out fastapi on lambda
- Think about api versioning
- use cloudfront and lambda function url to access this api
- Build auth on said fastapi
- connect a database