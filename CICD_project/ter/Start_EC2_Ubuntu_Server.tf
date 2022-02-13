module "ec2_instance" {
  source  = "terraform-aws-modules/ec2-instance/aws"
  version = "~> 3.0"

  name = "Server-Ubuntu"

  ami                    = "ami-0d527b8c289b4af7f"
  instance_type          = "t2.micro"
  key_name               = "ILIA-FR-KEY"
  monitoring             = true
  vpc_security_group_ids = ["sg-0a313f1aa81b8c859"]


  tags = {
    Terraform   = "true"
    Environment = "dev"
  }
}
provider "aws" {
    access_key = "AKIAYRZM7VDELFDMX2YV"
    secret_key = "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"
    region     = "eu-central-1"
}

