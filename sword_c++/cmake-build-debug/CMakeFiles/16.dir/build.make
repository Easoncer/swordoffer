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
include CMakeFiles/16.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/16.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/16.dir/flags.make

CMakeFiles/16.dir/合并两个排序的链表.cpp.o: CMakeFiles/16.dir/flags.make
CMakeFiles/16.dir/合并两个排序的链表.cpp.o: ../合并两个排序的链表.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/lixiansheng/Documents/github/swordoffer/sword_c++/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/16.dir/合并两个排序的链表.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/16.dir/合并两个排序的链表.cpp.o -c /Users/lixiansheng/Documents/github/swordoffer/sword_c++/合并两个排序的链表.cpp

CMakeFiles/16.dir/合并两个排序的链表.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/16.dir/合并两个排序的链表.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/lixiansheng/Documents/github/swordoffer/sword_c++/合并两个排序的链表.cpp > CMakeFiles/16.dir/合并两个排序的链表.cpp.i

CMakeFiles/16.dir/合并两个排序的链表.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/16.dir/合并两个排序的链表.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/lixiansheng/Documents/github/swordoffer/sword_c++/合并两个排序的链表.cpp -o CMakeFiles/16.dir/合并两个排序的链表.cpp.s

# Object files for target 16
16_OBJECTS = \
"CMakeFiles/16.dir/合并两个排序的链表.cpp.o"

# External object files for target 16
16_EXTERNAL_OBJECTS =

16: CMakeFiles/16.dir/合并两个排序的链表.cpp.o
16: CMakeFiles/16.dir/build.make
16: CMakeFiles/16.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/lixiansheng/Documents/github/swordoffer/sword_c++/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable 16"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/16.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/16.dir/build: 16

.PHONY : CMakeFiles/16.dir/build

CMakeFiles/16.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/16.dir/cmake_clean.cmake
.PHONY : CMakeFiles/16.dir/clean

CMakeFiles/16.dir/depend:
	cd /Users/lixiansheng/Documents/github/swordoffer/sword_c++/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/lixiansheng/Documents/github/swordoffer/sword_c++ /Users/lixiansheng/Documents/github/swordoffer/sword_c++ /Users/lixiansheng/Documents/github/swordoffer/sword_c++/cmake-build-debug /Users/lixiansheng/Documents/github/swordoffer/sword_c++/cmake-build-debug /Users/lixiansheng/Documents/github/swordoffer/sword_c++/cmake-build-debug/CMakeFiles/16.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/16.dir/depend

