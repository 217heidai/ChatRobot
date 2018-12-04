# ChatRobot
a python chat robot

#百度语音SDK
pip install baidu-aip

#
pip install numpy
pip install scipy
#pyaudio麦克风
pip install PyAudio
apt install python-pyaudio python3-pyaudio
#######依赖######
#portaudio
Download the portaudio
http://www.portaudio.com/archives/pa_stable_v190600_20161030.tgz
tar -zxvf pa_stable_v190600_20161030.tgz
cd portaudio
./configure
Edit the Makefile and add '-fPIC' compiler flag.
make
make install
Copy the portaudio static library (.a & .la) from /usr/local/lib to /lib
pip install pyaudio
################
#音频转换
apt install ffmpeg

#语音播放器
apt install mplayer