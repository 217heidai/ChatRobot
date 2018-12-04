#!/usr/bin/python
# -*- encoding=utf-8 -*- s
# 文件名：voice.py


import pyaudio
import numpy as np
from scipy import fftpack
import wave
from tools import Tools

class Voice(object):
    def __init__(self):
        self.__filename = "speech.wav"
        self.__time = 5 # 录音时间,如果指定时间，按时间来录音，默认为自动识别是否结束录音
        self.__threshold = 7000 # 判断录音结束的阈值
        self.__tools = Tools()

    def get_voice(self):
        CHUNK = 1024  # 块大小
        FORMAT = pyaudio.paInt16  # 每次采集的位数
        CHANNELS = 1  # 声道数
        RATE = 16000  # 采样率：每秒采集数据的次数
        RECORD_SECONDS = self.__time  # 录音时间
        WAVE_OUTPUT_FILENAME = self.__filename  # 文件存放位置
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
        print("* 录音中...")
        frames = []
        if RECORD_SECONDS > 0:
            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data = stream.read(CHUNK)
                frames.append(data)
        else:
            stopflag = 0
            stopflag2 = 0
            while True:
                data = stream.read(CHUNK)
                rt_data = np.frombuffer(data, np.dtype('<i2'))
                # print(rt_data*10)
                # 傅里叶变换
                fft_temp_data = fftpack.fft(rt_data, rt_data.size, overwrite_x=True)
                fft_data = np.abs(fft_temp_data)[0:fft_temp_data.size // 2 + 1]

                # 测试阈值，输出值用来判断阈值
                # print(sum(fft_data) // len(fft_data))

                # 判断麦克风是否停止，判断说话是否结束，# 麦克风阈值，默认7000
                if sum(fft_data) // len(fft_data) > self.__threshold:
                    stopflag += 1
                else:
                    stopflag2 += 1
                oneSecond = int(RATE / CHUNK)
                if stopflag2 + stopflag > oneSecond:
                    if stopflag2 > oneSecond // 3 * 2:
                        break
                    else:
                        stopflag2 = 0
                        stopflag = 0
                frames.append(data)
        print("* 录音结束")
        stream.stop_stream()
        stream.close()
        p.terminate()
        with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
        
if __name__ == '__main__':
    voice = Voice()
    voice.get_voice()