String toBinary(int n) {
  if (n <= 0) return '0';
  return n.toRadixString(2);
}

void main() {
  for (int i = 0; i <= 15; i++) {
    print('$i = ${toBinary(i)}');
  }
}