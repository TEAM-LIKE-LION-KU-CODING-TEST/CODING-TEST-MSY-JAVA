# Backend Configuration
# State Locking
terraform {
    backend "s3" {
        bucket = "infra-tf-state-bucket"
        key = "hybrid-nerwork/terraform.tfstate"
        region = "ap-northeast-2"
        dynamodb_table = "terraform-state-lock" # 이 속성이 핵심 (Locking 주체 설정)
        encrypt = true
    }
}

# 최신 방식 (Terraform v1.10 이상)
# 기존의 dynamodb_table 속성을 지우고 use_lockfile = true 한 줄만 넣으면
# S3 자체적으로 .tflock 파일을 생성해 더 간단하게 Locking을 구현할 수 있음
terraform {
    backend "s3" {
        bucket       = "infra-tf-state-bucket"
        key          = "hybrid-nerwork/terraform.tfstate"
        region       = "ap-northeast-2"
        encrypt      = true
        use_lockfile = true  # Changed: DynamoDB 대신 S3 자체 잠금 사용
    }
}

# Transit Gateway
resource "aws_ec2_transit_gateway" "main" {
    description = "Hybrid Cloud Central TGW"
    default_route_table_association = "disable"
    default_route_table_propagation = "disable"
    tags = {
        Name = "main-tgw"
    }
}

# Production VPC Attatchment
resource "aws_ec2_transit_gateway_vpc_attatchment" "prod" {
    subnet_ids = aws_subnet.prod_private[*].subnet_ids
    transit_gateway_id = aws_ec2_transit_gateway.main.subnet_ids
    vpc_id = aws_vpc.prod.id
}