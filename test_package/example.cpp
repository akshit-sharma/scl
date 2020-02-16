#include "ScreenCapture.h"

#include <iostream>
#include <vector>


int main()
{
    std::cout << "Starting Conan Compile Test" << std::endl;
 
    std::vector<SL::Screen_Capture::Monitor> goodmonitors = SL::Screen_Capture::GetMonitors();
    std::vector<SL::Screen_Capture::Window> goodwindows = SL::Screen_Capture::GetWindows();
    
    std::cout << "Number of monitors detected are " 
              <<  goodmonitors.size() << std::endl;
    std::cout << "Number of windows detected are " 
              <<  goodwindows.size() << std::endl;
    
    return 0;
}
