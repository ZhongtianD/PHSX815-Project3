# PHSX815-Project3

Fit_function.py generates samples of the function we are tring to find and fit using  polynomials.

Use the -h flag to see instructions on input parameters.

For example, to fit using 10 samples from a sine curve use

python Fit_function.py -Mode 0 -Nsample 10 -Degree 5 -sigma 0.1

It will generate a fitting plot and print out the reduced chi-square statistic.

![alt text](https://github.com/ZhongtianD/PHSX815-Project3/blob/main/Fit_result.png?raw=true)

The Mode refers to the function time. 0 is Sine function, 1 is Cosine function, 2 is a Square wave, 3 is a sawtooth signal and 4 is a Gaussian pulse.
