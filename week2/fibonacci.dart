int fibonacci(int n) {
  if (n <= 0) return 0;
  if (n == 1) return 1;
  return fibonacci(n - 1) + fibonacci(n - 2);
}

void main() {
  for (int i = 0; i <= 10; i++) {
    print('F($i) = ${fibonacci(i)}');
  }
}