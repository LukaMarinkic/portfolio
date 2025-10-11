#include <iostream>
#include <string>

void calcm2() { std::cout << "calcm2 was called"; };
void calcd() { std::cout << "calcd was called"; };

int main() {
  enum searched {
    m2,
    d,
  };

  searched theSearchedVariable;
  std::string temporaryString;
  std::cout << "Whacha looking for? (m2|d): ";
  std::cin >> temporaryString;

  if (temporaryString == "m2") {
    theSearchedVariable = m2;
  } else if (temporaryString == "d") {
    theSearchedVariable = d;
  }

  switch (theSearchedVariable) {
  case m2:
    calcm2();
    break;
  case d:
    calcd();
    break;
  }
  return 0;
}
