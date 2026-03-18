#include <iostream>
#include <string>
#include <map>

int main() {
    int t, n, hash;
    std::string str;

    std::cin >> t;
    for (int i=0;i<t;i++){
        std::cin >> n;
        hash = 0;
        
        for (int j=0;j<n;j++){
            std::cin >> str;
            
            for (int k=0; k<str.length();k++){
                hash += (str[k] - 'A') + j + k;
            }
        }

        std::cout << hash << std::endl;
    }
    return 0;
}