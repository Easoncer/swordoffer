# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.12

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /Applications/CLion.app/Contents/bin/cmake/mac/bin/cmake

# The command to remove a file.
RM = /Applications/CLion.app/Contents/bin/cmake/mac/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/lixiansheng/Documents/github/swordoffer/sword_c++

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/lixiansheng/Documents/github/swordoffer/sword_c++/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/11.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/11.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/11.dir/flags.make

CMakeFiles/11.dir/二进制中1的个数.cpp.o: CMakeFiles/11.dir/flags.make
CMakeFiles/11.dir/二进制中1的个数.cpp.o: ../二进制中1的个数.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/lixiansheng/Documents/github/swordoffer/sword_c++/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/11.dir/二进制中1的个数.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/11.dir/二进制中1的个数.cpp.o -c /Users/lixiansheng/Documents/github/swordoffer/sword_c++/二进制中1的个数.cpp

CMakeFiles/11.dir/二进制中1的个数.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/11.dir/二进制中1的个数.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/lixiansheng/Documents/github/swordoffer/sword_c++/二进制中1的个数.cpp > CMakeFiles/11.dir/二进制中1的个数.cpp.i

CMakeFiles/11.dir/二进制中1的个数.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/11.dir/二进制中1的个数.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/lixiansheng/Documents/github/swordoffer/sword_c++/二进制中1的个数.cpp -o CMakeFiles/11.dir/二进制中1的个数.cpp.s

# Object files for target 11
11_OBJECTS = \
"CMakeFiles/11.dir/二进制中1的个数.cpp.o"

# External object files for target 11
11_EXTERNAL_OBJECTS =

11: CMakeFiles/11.dir/二进制中1的个数.cpp.o
11: CMakeFiles/11.dir/build.make
11: CMakeFiles/11.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/lixiansheng/Documents/github/swordoffer/sword_c++/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable 11"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/11.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/11.dir/build: 11

.PHONY : CMakeFiles/11.dir/build

CMakeFiles/11.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/11.dir/cmake_clean.cmake
.PHONY : CMakeFiles/11.dir/clean

CMakeFiles/11.dir/depend:
	cd /Users/lixiansheng/Documents/github/swordoffer/sword_c++/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/lixiansheng/Documents/github/swordoffer/sword_c++ /Users/lixiansheng/Documents/github/swordoffer/sword_c++ /Users/lixiansheng/Documents/github/swordoffer/sword_c++/cmake-build-debug /Users/lixiansheng/Documents/github/swordoffer/sword_c++/cmake-build-debug /Users/lixiansheng/Documents/github/swordoffer/sword_c++/cmake-build-debug/CMakeFiles/11.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/11.dir/depend

