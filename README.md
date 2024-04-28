## OpenCV Gazebo Camera Video Stream and Process with GStreamer over udp ##

### Ubuntu 22.04 Setup ###

#### GStreamer install ####
```shell
$ sudo apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio
```

#### OpenCV with GStream support ####

Download OpenCV and extra modules:
```shell
$ git clone https://github.com/opencv/opencv.git
$ cd opencv
$ git clone https://github.com/opencv/opencv_contrib.git
```
Create a build directory and run CMake to configure the build:
```shell
$ cd ..
$ mkdir build
$ cd build
$ cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D OPENCV_EXTRA_MODULES_PATH=../opencv_contrib/modules -D WITH_GSTREAMER=ON -D WITH_GTK=ON ..
```
Compile OpenCV and install it on your system.
```shell
$ make -j$(nproc)
$ sudo make install
```
