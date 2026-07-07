# 1. State 저장을 위한 S3 버킷 생성
resource "aws_s3_bucket" "terraform_state" {
    bucket = "fin-bank-terraform-state-prod"

    # tfstate 파일의 우발적 삭제 방지 Policy
    lifecycle {
      prevent_destroy = true
    }
}

# S3 버킷 버전 관리
# 파일 손상 시 복구를 위함
resource "aws_s3_bucket_versioning" "state_versioning" {
    bucket = aws_s3_bucket.terraform_state.id
    versioning_configuration {
      status = "Enabled"
    }
}

# S3 버킷 KMS CMK 암호화
resource "aws_s3_bucket_server_side_encryption_configuration" "state_encryption" {
    bucket = aws_s3_bucket.terraform_state.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "aws:kms"
      kms_master_key_id = aws_kms_key.state_ket.arn
    }
  }
}

# 2. State 잠금용 DynamoDB 테이블 생성
resource "aws_dynamodb_table" "terraform_locks" {
    name = "fin-bank-state-locks"
    billing_mode = "PAY_PER_REQUEST"
    # Terraform이 DynamoDB를 사용해 State 잠금을 걸 때
    # 내부적으로 무조건 "LockID"라는 이름의 파티션 키를 찾도록 하드코딩되어 있음
    hash_key = "LockID" # LockID 속성은 예약어이므로 반드시 일치해야 함

    # DynamoDB는 NoSQL 데이터베이스라 미리 스키마를 짤 필요가 없지만
    # Primary Key로 사용할 속성의 이름과 데이터 타입은 반드시 명시해야 함
    attribute {
      name = "LockID" # hash_key에서 지정한 이름과 동일하게 맞춰 속성을 정의
      type = "S"  # String, Terraform은 잠금을 걸 때 fin-bank-network/terraform.tfstate-md5 등 사용
    }
}