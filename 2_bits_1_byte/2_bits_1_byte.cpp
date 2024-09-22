#include <cstdio>
#define DON 0
#define ACT 1
#define JMP 2
#define END 3
int tape[4], trans[4] = {3, 2, 0, 1};
int main() {
  char c = getchar();
  tape[0] = (c >> 6) & 3;
  tape[1] = (c >> 4) & 3;
  tape[2] = (c >> 2) & 3;
  tape[3] = c & 3;
  int ip = 0;
  while (1) {
    switch (tape[ip]) {
    case DON: {
      ip = (ip + 1) % 4;
      break;
    }
    case END: {
      putchar((tape[0] << 6) + (tape[1] << 4) + (tape[2] << 2) + tape[3]);
      return 0;
    }
    case JMP: {
      ip = tape[(ip + 1) % 4];
      break;
    }
    case ACT: {
      tape[tape[(ip + 1) % 4]] = trans[tape[tape[(ip + 1) % 4]]];
      ip = (ip + 2) % 4;
      break;
    }
    }
  }
  return 0;
}
