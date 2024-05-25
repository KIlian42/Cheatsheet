# AutoGrad package -> gradient calculation, backpropagation
import torch

def main():
    x = torch.randn(3, requires_grad=True)

    y = x+2
    print(y)
    z = y*y*2
    z = z.mean()
    print(z)

    z.backward()
    print(x.grad)

if __name__ == "__main__":
    main()
