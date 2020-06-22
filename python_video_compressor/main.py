#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python Video Compressor
# Compresses all .mp4 Video files in given directory ussing ffmpeg

import os, argparse, sys
from .argument_parser import ArgumentParser
from .video_file_scanner import VideoFileScanner
from pathlib import Path

class VideoCompressor:
    
    def __init__(self):
        self.input_dir, self.output_dir, self.bitrate, self.ignore_files_below = ArgumentParser().parse()
        self.video_files = VideoFileScanner().scan(self.input_dir)

    def compress(self):
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        for file_path in self.video_files:
            self.__remove_old_output_file(file_path)
            self.__create_output_dir(file_path)
            if self.__file_size_in_MB(file_path) >= (self.ignore_files_below or 0):
                print(f"Compressing: {file_path}")
                self.__compress_file(file_path)
                print(self.__file_stats(file_path))
            else:
                print(f"Ommitting: {file_path} because of file size")
        print("Done.")
    
    def __compress_file(self, file_path):
        os.system(self.__ffmpeg_command(file_path, self.__output_video_path(file_path), self.bitrate or '3000k'))

    def __ffmpeg_command(self, input_file_path, output_file_path, bitrate):
        return f"ffmpeg -loglevel error -i {input_file_path} -vcodec h264 -b:v {bitrate} -acodec mp3 {output_file_path}"

    def __output_video_path(self, video_path):
        return (self.output_dir + '/' + video_path.replace(self.input_dir, '')).replace("//", '/')

    def __create_output_dir(self, video_path):
        dir_name = os.path.dirname(self.__output_video_path(video_path))
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

    def __remove_old_output_file(self, video_path):
        try:
            os.remove(self.__output_video_path(video_path))
        except OSError:
            pass

    def __file_stats(self, file_path):
        return f"Original size: {self.__file_size_in_MB(file_path)}MB | Compressed: {self.__file_size_in_MB(self.__output_video_path(file_path))}MB"

    def __file_size_in_MB(self, file_path):
        if os.path.exists(file_path):
            file = Path(file_path)
            size = file.stat().st_size
            return size >> 20

if __name__ == '__main__':
    VideoCompressor().compress()