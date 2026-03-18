#include <iostream>
#include <string>
#include <map>

int main() {
    int n, qntd;
    std::string number;

    std::map<char, int> paineis = {
        { '1', 2 },
        { '2', 5 },
        { '3', 5 },
        { '4', 4 },
        { '5', 5 },
        { '6', 6 },
        { '7', 3 },
        { '8', 7 },
        { '9', 6 },
        { '0', 6 }
    };
    std::cin >> n;
    for (int i=0;i<n;i++){
        std::cin >> number;
        qntd = 0;
        
        for(char c : number){
            qntd += paineis[c];
        }
        std::cout << qntd << " leds" << std::endl;
    }
    return 0;
}