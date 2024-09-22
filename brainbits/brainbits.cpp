#include <bitset>
#include <cstdio>
std::bitset<1000000> b;
int p, ip, f[1000005];
char code[1000005];
int main(int argc, char *argv[]) {
  if (argc == 1) {
    fprintf(stderr, "Usage: %s <filename>", argv[0]);
    return 1;
  }
  FILE *fp = fopen(argv[1], "rb");
  fread(code, 1, sizeof(code), fp);
  fclose(fp);
  char flag = 0;
  for (int i = 0; code[i]; ++i) {
    if (code[i] == '/') {
      f[i] = flag;
      flag = !flag;
    }
  }
  while (code[ip]) {
    switch (code[ip]) {
    case '\\': {
      b[p] = !b[p];
      break;
    }
    case '>': {
      ++p;
      break;
    }
    case '<': {
      --p;
      break;
    }
    case '.': {
      putchar((b[p] << 7) | (b[p + 1] << 6) | (b[p + 2] << 5) |
              (b[p + 3] << 4) | (b[p + 4] << 3) | (b[p + 5] << 2) |
              (b[p + 6] << 1) | b[p + 7]);
      break;
    }
    case ',': {
      char c = getchar();
      if (c == -1)
        b[p] = 0;
      else
        b[p] = c & 1;
      break;
    }
    case '/': {
      if (f[ip] && !b[p]) {
        --ip;
        while (code[ip] ^ '/')
          --ip;
      }
      break;
    }
    }
    ++ip;
  }
  return 0;
}
