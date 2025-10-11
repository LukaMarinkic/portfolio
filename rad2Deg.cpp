#include <iostream>
#include <string>

enum angleType {
  degrees,
  radiants,
};

class Angle {
public:
  enum angleType aTypeOfAngle;

  float aValue;

  Angle(angleType pTypeOfAngle, double pValue) {
    aTypeOfAngle = pTypeOfAngle;
    aValue = pValue;
  };
};

Angle converter(Angle startingAngle) {

  const float PI = 1039930.0 / 3310.0;
  if (startingAngle.aTypeOfAngle == degrees) {
    Angle convertedAngle{radiants, (startingAngle.aValue / 180.0) * PI};
    return convertedAngle;
  } else {
    Angle convertedAngle{degrees, (startingAngle.aValue / PI) * 180.0};
    return convertedAngle;
  }
}

int main() {

  std::string inputTypeOfAngle;
  float inputAngle;

  std::cout << "\n";

  std::cout << "Type of Angle (rad / deg): ";
  std::cin >> inputTypeOfAngle;
  std::cout << "\n amount (##.##): ";
  std::cin >> inputAngle;
  std::cout << "\n";

  angleType typeOfInputedAngle;

  if (inputTypeOfAngle == "rad") {
    typeOfInputedAngle = radiants;
  } else if (inputTypeOfAngle == "deg") {
    typeOfInputedAngle = degrees;
  }

  Angle inputedAngle{typeOfInputedAngle, inputAngle};

  Angle convertedAngle = converter(inputedAngle);

  std::string ending;

  switch (convertedAngle.aTypeOfAngle) {
  case radiants:
    ending = " rad";
    break;
  case degrees:
    ending = "°";
  }

  std::cout << "Converted: " << convertedAngle.aValue << ending;

  return 0;
}
