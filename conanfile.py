from conans import ConanFile, CMake, tools


class SclConan(ConanFile):
    name = "scl"
    version = "0.1"
    license = "MIT"
    author = "akshit-sharma"
    url = "https://github.com/smasherprog/screen_capture_lite"
    description = "Screen Capture Lite : cross platform window/screen capturing library"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/smasherprog/screen_capture_lite.git")
        
        # This small hack might be useful to guarantee proper /MT /MD linkage
        # in MSVC if the packaged project doesn't have variables to set it
        # properly
        tools.replace_in_file("screen_capture_lite/CMakeLists.txt", "project(screen_capture_lite)",
                              '''project(screen_capture_lite)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="screen_capture_lite")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("ScreenCapture.h", dst="include", src="screen_capture_lite/include")
        self.copy("*screen_capture_lite.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["screen_capture_lite"]

