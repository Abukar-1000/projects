#include "Windows.h"
#include <iostream>
#include <map>
#define pass 0;

const std::map<char,int> indexTable = {{'0', 0x30}, {'1',0x31}, {'2', 0x32}, {'3',0x33},
{'4', 0x34}, {'5',0x35}, {'6', 0x36}, {'7', 0x37}, {'8', 0x38}, {'9', 0x39}};

bool isPressed(char key){
    auto HEXVALUE = indexTable.find(key);
    std::cout << HEXVALUE->second << "\n";
    GetKeyState(key) & HEXVALUE->second;
    return false;
}
int main(){

    // keys to listen for 
    const char KEYS[36] = {'0','1','2','3','4','5','6','7','8','9'
                    ,'A','B','C','D','E','F','G','H','I','J'
                    ,'K','L','M','N','O','P','Q','R','S','T'
                    ,'U','V','W','X','Y','Z'};
    // special keys
    const WORD ALLKEYS[10] = {};
    bool keepGoing = true;
    // bool* trigger = new bool;
    bool trigger = false;
    while (keepGoing){
        WORD spaceButton = VK_SPACE;
        if (GetKeyState(spaceButton) & 0x8000)
        {
            std::cout << "Space pressed\n";
            keepGoing = false;
        }
    }
    return 0;
}