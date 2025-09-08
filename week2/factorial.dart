int factorial(int n) {
  if (n <= 0) return 1;
  return n * factorial(n - 1);
}

void main() {
  for (int i = 0; i <= 8; i++) {
    print('$i! = ${factorial(i)}');
  }
}