#Christian Flores 21/02/2021

from cmath import phase

float_complex_input = complex(input())

print(abs(complex(float_complex_input.real, float_complex_input.imag)))
print(phase(complex(float_complex_input.real, float_complex_input.imag)))

