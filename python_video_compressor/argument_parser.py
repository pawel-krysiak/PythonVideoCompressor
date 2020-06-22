import os, argparse, sys

from pathlib import Path

OUTPUT_DIR = 'compressed'

class ArgumentParser:
    def parse(self):
        parser = argparse.ArgumentParser(description='Python Video Compressor')
        parser.add_argument('dir', metavar='dir', nargs=1, help='Video directory')
        parser.add_argument('--bitrate', nargs='?', help='Output video bitrate. 1000k - low, 2000k - medium, >3000k - high. Default: 3000k')
        parser.add_argument('--ignore-files-below', nargs='?', help='Do not compress files below size. Default: 50MB')
        args = parser.parse_args()

        print("Use -h for help. \n")
        
        for k,v in sorted(args.__dict__.items()):
            print("{0}: {1}".format(k,v))

        answer = input('\nProceed with presented arguments? [y\\n]\n')
        if answer.strip().lower() == 'y':
            self.input_dir = self.__input_dir_path(args)
            self.output_dir = (self.input_dir + OUTPUT_DIR).replace('//','/')
            self.bitrate = args.bitrate
            self.ignore_files_below = self.__minimum_file_size(args)
            return [self.input_dir, self.output_dir, self.bitrate, self.ignore_files_below]
        else:
            sys.exit()
    
    def __minimum_file_size(self, args):
        try:
            return int(args.ignore_files_below.replace('MB',''))
        except:
            pass
    
    def __input_dir_path(self,args):
        if args.dir[0] == '.':
            return str(Path(args.dir[0]).resolve())
        else:
            return args.dir[0]