// This is a comment

print(10);  // <-- Statements end in

|x = 36; // Variables can be declared as "|IDENTIFIER = VALUE", and can be referenced from the same identifier
|y = x^0.5;  // <-- Floats can be defined in decimal format, ...

|z = -y;    // ... as well as negation of numbers

// Additionally, all basic artihmetic operations function too

print(x + y);
print(x - y);
print(x * y);
print(x / y);
print(x % y);

// As well as parenthetic priority
print(2 * (4+1) -8);  // Remember BIDMAS 

// Furthermore, SIN and COS are now inbuilt functions, in radians.

|pi = 3.141592653589;

|s45 = sin(pi / 4);
|c45 = cos(pi / 4);

print(s45 ^ 2 + c45^2); // sin(t)^2 + cos(t)^2 = 1

// And the language has a function dedicated to the solving of quadratics

print(qsolve(1, 1, -1));
