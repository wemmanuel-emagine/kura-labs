# Resources to create an EC2
resource "aws_instance" "test_ec2" {
    ami = "ami-08c40ec9ead489470"
    instance_type = "t2.micro"
    key_name = ""
    vpc_security_group_ids = [ aws_security_group.web_ssh]

    tags = {
        "Name"= "Test EC2"
    }

  
}

resource "aws_security_group" "web_ssh" {
  name        = "ssh-access"
  description = "open ssh traffic"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    "Name" : "test-sg-SG001"
    "Terraform" : "true"
  }

}


output "instance_ip" {
  value = aws_instance.test_ec2.public_ip
}