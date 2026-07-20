# provider.tf
terraform {
  required_providers {
    aws = {
        aws = "hashicorp/aws"
        version = "~> 5.0"
    }
    openstack = {
        source = "terraform-provider-openstack/openstack"
        version = "~> 1.50"
    }
  }
}

provider "aws" {
  region = "ap-northeast-2"
}

provider "openstack"{
    auth_url = var.os_auth_url
    tenant_name = var.os_tenant_name
    user_name = var.os_user_name
    password = var.os_password
}

# main.tf (OpenStack DB)
resource "openstack_compute_instance_v2" "backend_db"{
    name = "hybrid-backend-db"
    image_name = "rocky-linux-9"
    flavor_name = "m1.large"
    key_pair = "os-ssh-key"
    security_groups = ["default"]

    network = {
        name = "private-network-192.168"
    }
}

# main.tf (AWS EKS Node Group)
resource "aws_eks_node_group" "frontend_nodes" {
    cluster_name = aws_eks_cluster.main.name
    node_group_name = "frontend-nodes"
    node_role_arn = aws_iam_role.node_role.arn
    subnet_ids = [aws_subnet.private.id]

    scaling_config {
      desired_size = 2
      max_size = 5
      min_size = 2
    }

    # Cross-Provider 의존성 주입
    # DB의 접속 IP를 EKS Node의 Tag나 UserData로 주입하여 암시적 의존성 생성
    tags = {
        "Backend_DB_IP" = openstack_compute_instance_v2.backend_db.access_ip_v4
    }
}

# OpenStack API 응답 지연으로 인스턴스는 생성되었지만 네트워크 포트 할당이 늦어지면
# Terraform이 IP를 빈 값으로 AWS 태그에 밀어 넣는 엣지 케이스 방어 : local-exec
resource "null_resource" "wait_for_db" {
  depends_on = [openstack_compute_instance_v2.backend_db]

  provisioner "local-exec" {
    command = "while ! nc -z ${openstack_compute_instance_v2.backend_db.access_ip_v4} 5432; do sleep 5; done"
  }
}