import sympy as sp
from sympy.abc import m,n,k,x,y
import argparse

λ = sp.symbols("λ")

def plot_helper(y, k, m):
    # construct your green's function
    eigen_functions_mul = sp.sin(n * sp.pi * y) * sp.sin(n * sp.pi * x) \
        / (k**2 - n**2 * sp.pi**2)
    greens_function     = 2 * sp.Sum(eigen_functions_mul, (n, 1, m))
    
    sp.textplot(
        greens_function.subs({
            y : y,
            k : k, 
            m : m  
        }),
        0, 1
    )
    
def main(args):
    plot_helper(args.y, args.k, args.m)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-y", type=float)
    parser.add_argument("-k", type=float)
    parser.add_argument("-m", type=int)
    args = parser.parse_args()
    
    # usage 
    # python greens_eigen_series.py
    main(args)