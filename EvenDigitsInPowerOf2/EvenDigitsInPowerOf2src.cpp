#include <iostream>
#include <string>

using namespace std;
string addStrings(string a, string b) {
    string result = "";
    int carry = 0;
    int i;
    while (a.length() < b.length()) a += '0';
    while (b.length() < a.length()) b += '0';
    for (i = 0; i < a.length(); ++i) {
        int digitA = a[i] - '0';
        int digitB = b[i] - '0';
        int sum = digitA + digitB + carry;
        result += (sum % 10) + '0';
        carry = sum / 10;
    }
    if (carry > 0)
        result += carry + '0';
    return result;
}

void printNumber(string number) {
    int ok=1;
    for (int i = number.length() - 1; i >= 0; --i)
        if ((number[i] - '0') % 2 == 1) {
            ok = 0;
            break;
        }
    if (ok)
        cout << number;
    else
        cout << "nah";
}
int main() {
    string current = "1"; // 2^0 = 1
    int maxPower = 1000000;
    for (int n = 0; n <= maxPower; ++n) {
        cout << "2^" << n << " = ";
        printNumber(current);
        cout << endl;
        current = addStrings(current, current);
    }
    return 0;
}
