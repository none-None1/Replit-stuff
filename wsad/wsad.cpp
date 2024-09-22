#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <stack>
#include <string>
std::string s, code, tok = "wsad", tab = "+-[],.<>;:()@?!$";
std::stack<int> st;
int ip = 0, p = 0, match[1000005], bracket[1000005];
char tape[1000005];
int main() {
  srand(time(0));
  char c;
  while ((c = getchar()) != '!') {
    c = tolower(c);
    if (c == 'w' || c == 's' || c == 'a' || c == 'd')
      s += c;
  }
  for (int i = 0; i < s.size(); i += 2) {
    code += tab[tok.find(s[i]) * 4 +
                tok.find(s[i + 1])]; // Turn two-letter commands into one-letter
                                     // commands for simplicity
  }
  for (int i = 0; i < code.size(); i++) {
    if (st.size())
      bracket[i] = st.top();
    if (code[i] == '[' || code[i] == '(')
      st.push(i); // Match brackets
    else if (code[i] == ']' || code[i] == ')') {
      int top = st.top();
      st.pop();
      match[top] = i;
      match[i] = top;
    }
  }
  while (ip < code.size()) {
    switch (code[ip]) {
    case '+': {
      tape[p]++;
      break;
    }
    case '-': {
      tape[p]--;
      break;
    }
    case '>': {
      p++;
      break;
    }
    case '<': {
      p--;
      break;
    }
    case ',': {
      tape[p] = getchar();
      break;
    }
    case '.': {
      putchar(tape[p]);
      break;
    }
    case '?': {
      tape[p] = rand() & 255;
      break;
    }
    case '@': {
      return 0;
    }
    case '$': {
      ip = -1;
      break;
    }
    case ':': {
      printf("%u\n", (unsigned char)tape[p]);
      break;
    }
    case ';': {
      int x;
      scanf("%d", &x);
      tape[p] = x;
      break;
    }
    case '[': {
      if (!tape[p]) {
        ip = match[ip];
      }
      break;
    }
    case ']': {
      if (tape[p]) {
        ip = match[ip];
      }
      break;
    }
    case '(': {
      if (tape[p]) {
        ip = match[ip];
      }
      break;
    }
    case ')': {
      if (!tape[p]) {
        ip = match[ip];
      }
      break;
    }
    case '!': {
      ip = match[bracket[ip]]; // Break a loop
      break;
    }
    }
    ++ip;
  }
  return 0;
}
