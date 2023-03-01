resource "aws_instance" "jenkins_ec2" {
     ami                    = "ami-08c40ec9ead489470"
     instance_type = "t2.micro"
     vpc_security_group_ids = [aws_security_group.ec2_sg.id]

     user_data = "${file("server.sh")}"

     key_name = "deploy"
     tags = {
       "Name" = "Final Project Jenkins"
     }
  
}
resource "aws_instance" "docker_ec2" {
     ami                    = "ami-08c40ec9ead489470"
     instance_type = "t2.micro"
     vpc_security_group_ids = [aws_security_group.ec2_sg.id]

     user_data = "${file("docker.sh")}"

     key_name = "deploy"
     tags = {
       "Name" = "Final Project docker"
     }
  
}
resource "aws_instance" "terraform_ec2" {
     ami                    = "ami-08c40ec9ead489470"
     instance_type = "t2.micro"
     vpc_security_group_ids = [aws_security_group.ec2_sg.id]

     user_data = "${file("terrafrom.sh")}"

     key_name = "deploy"
     tags = {
       "Name" = "Final Project Terraform"
     }
  
}

# Terraform Public IP
output "terraform_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.terraform_ec2.public_ip
}

# Docker Puiblic IP
output "docker_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.docker_ec2.public_ip
}
# Jenkins Puiblic IP
output "docker_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.jenkins_ec2.public_ip
}
