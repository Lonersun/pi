# -*- coding:utf-8 -*-
import wave, pyaudio
from datetime import datetime


class AudioModule(object):

    # 缓存大小
    chunk = 1024
    # 取样值的量化格式
    format = pyaudio.paInt16
    # 取样频率，百度语音识别库指定8000
    rate = 8000
    # 声道数，百度语音识别库指定1
    channels = 1
    # 时间段，秒
    record_seconds = 5
    # 存放目录
    audio_dir = '/tmp/'

    def record_wave(self):
        """
        录制wav文件
        :return:
        """
        pa = pyaudio.PyAudio()
        # format 取样值的量化格式
        # channels 声道数
        # rate 取样频率，一秒内对声音信号的采集次数
        # input 输入流标志
        # frames_per_buffer 底层缓存块的大小
        stream = pa.open(format=self.format,
                         channels=self.channels,
                         rate=self.rate,
                         input=True,
                         frames_per_buffer=self.chunk)
        print("* recording")
        save_buffer = []
        for i in range(0, int(self.rate / self.chunk * self.record_seconds)):
            audio_data = stream.read(self.chunk)
            save_buffer.append(audio_data)
        print("* done recording")
        # stop
        stream.stop_stream()
        stream.close()
        pa.terminate()
        # wav path
        file_name = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")+".wav"
        if self.audio_dir.endswith('/'):
            file_path = self.audio_dir + file_name
        else:
            file_path = self.audio_dir + "/" + file_name
        # save file
        wf = wave.open(file_path, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(pa.get_sample_size(self.format))
        wf.setframerate(self.rate)
        # 注意join 前的类型，如果是str类型会出错
        wf.writeframes(b''.join(save_buffer))
        wf.close()
        return file_path

    def get_wav_data(self, file_str=""):
        """
        读取wav文件
        :param file_str:
        :return:
        """
        if file_str is None or len(file_str) == 0:
            return None
        # 使用"rb"(二进制模式)打开文件
        wav_file = wave.open(file_str, 'rb')
        nframes = wav_file.getnframes()
        audio_data = wav_file.readframes(nframes)
        return audio_data, nframes


