provider "aws" {
  region = "ap-south-1"
}

resource "aws_s3_bucket" "test" {
  bucket = "risk-poc-demo-bucket"
}

resource "aws_security_group" "web" {
  name = "risk-poc-sg"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}