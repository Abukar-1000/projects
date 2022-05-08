#include <iostream>
#include <filesystem>
#include <vector>
std::string getPath(){
    std::string path = "";
    std::cout << "Enter path:   \n";
    getline(std::cin,path);
    return path;
}
int main(){
    std::string path = "";
    path = getPath();
    std::cout << path;
    // print files in a directory 
    for (auto &file: std::filesystem::directory_iterator(path)){
        std::cout << file.path() << "\n";
    }
    return 0;
}