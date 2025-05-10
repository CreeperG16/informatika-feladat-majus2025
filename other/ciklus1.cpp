#include <iostream>

int main() {
    std::cout << "- 1. feladat\n";
    for (int i = 10; i --> 0;) if ((10 - i) % 2 == 0) std::cout << (10 - i) << "\n";

    std::cout << "\n- 2. feladat\n";
    for (int i = 11; i --> 1;) std::cout << i << "\n";

    std::cout << "\n- 3. feladat\n";
    for (int i = 10; i --> 0;) if (i % 2) std::cout << i << "\n";

    std::cout << "\n- 4. feladat\n";
    
    std::string text;
    std::cout << "Mi legyen a szöveg? ";
    std::cin >> text;

    int n;
    std::cout << "Hányszor írja ki a szöveget? ";
    std::cin >> n; // implicit integer parsing? unsure what's happening in this operator>>

    for (int i = n; i --> 0;) std::cout << text << "\n";

    std::cout << "\n- 5. feladat\n";
    int m;
    while (m % 2) {
        std::cout << "Egy páros szám: ";
        std::cin >> m;
    }

    std::cout << "\n- 6. feladat\n";
    int numThree = 0;
    srand(time(0));
    for (int i = 20; i --> 0;) {
        int x = (rand() % 12) + 1;
        if (x % 3 != 0) continue;
        
        std::cout << x << "\n";
        numThree++;
    }
    std::cout << "Összesen " << numThree << " darab hárommal osztható szám lett generálva.\n";
}
