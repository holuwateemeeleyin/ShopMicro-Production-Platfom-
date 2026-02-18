# This is a simplified version for the project
resource "aws_eks_cluster" "shopmicro" {
  name     = "shopmicro-cluster"
  role_arn = aws_iam_role.eks_cluster.arn

  vpc_config {
    subnet_ids = [aws_subnet.public.id]
  }
}