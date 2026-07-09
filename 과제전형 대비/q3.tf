# /dev/app/main.tf
terraform {
    backend "s3" {
      bucket = "fin-terraform-state-prod"
      key = "dev/app/terraform.tfstate" # app 전용 tfstate 파일
      region = "ap-northeast-2"
      dynamodb_table = "terraform-state-lock"
    }
}

# 다른 도메인(DB)의 tfstate 파일을 Read Only로 참조
data "terraform_remote_state" "db"{
    backend = "s3"
    config = {
      bucket = "fin-terraform-state-prod"
      key = "dev/database/terraform.tfstate" # 참조 대상 tfstate 파일 경로
      region = "ap-northeast-2"
    }
}

resource "aws_ssm_parameter" "db_endpoint" {
    name = "/dev/app/db-endpoint"
    type = "String"
    # 원격 tfstate 파일에서 출력된 데이터베이스 주소 활용
    value = "data.terraform_remote_state.db.output.db_address"
}

### 망 분리 환경 내 별도 tfstate 파일이 아닌 모듈 형태로 활용할 경우
# ├── modules/                   # 1. 템플릿화된 재사용 모듈 (DRY)
# │   └── network/
# │       ├── main.tf            # resource "aws_vpc" { ... }
# │       └── variables.tf       # variable "cidr_block" { ... }
# │
# ├── dev/                       # 2. 상태 격리 디렉터리 
# │   └── network/
# │       ├── main.tf            # module "network" { source = "../../modules/network" ... } // Changed: 리소스를 직접 짜지 않고 모듈 호출
# │       └── terraform.tfvars   # cidr_block = "10.0.0.0/16" 
# │
# └── prod/                      # 3. 상태 격리 디렉터리
#     └── network/
#         ├── main.tf            # module "network" { source = "../../modules/network" ... } // Changed: dev와 동일하게 모듈 호출
#         └── terraform.tfvars   # cidr_block = "10.1.0.0/16"