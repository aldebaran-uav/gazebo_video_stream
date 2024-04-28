### ONEMLI !!! ###

OpenCV GStream desteği için source code ile build edilmeli.

OpenCV'yi ve ekstra modulleri indirin.:
```shell
$ git clone https://github.com/opencv/opencv.git
$ cd opencv
$ git clone https://github.com/opencv/opencv_contrib.git
```
Bir build dizini oluşturun ve build'i yapılandırmak için CMake'i çalıştırın:
```shell
$ cd ..
$ mkdir build
$ cd build
$ cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D OPENCV_EXTRA_MODULES_PATH=../opencv_contrib/modules -D WITH_GSTREAMER=ON -D WITH_GTK=ON ..
```
OpenCV'yi compile edin ve sisteminize yükleyin.
```shell
$ make -j$(nproc)
$ sudo make install
```
