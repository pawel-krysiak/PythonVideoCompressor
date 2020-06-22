import os, argparse, sys

class ArgumentParser:
    def __init__(self):
        parser = argparse.ArgumentParser(description='Unique Codes Picture Watermarker')
        parser.add_argument('image_path', metavar='image_path', nargs=1, help='Image path')
        parser.add_argument('number_of_tickets', metavar='number_of_tickets', nargs=1, help='Number of tickets that will be generated with unique codes', type=int)
        args = parser.parse_args()

        print("Use -h for help. \n")
        
        for k,v in sorted(args.__dict__.items()):
            print("{0}: {1}".format(k,v))

        answer = input('\nProceed with presented arguments? [y\\n]')
        if answer.strip().lower() == 'y':
            print(args)
        else:
            sys.exit()