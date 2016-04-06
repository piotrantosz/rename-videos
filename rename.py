from guessit import guessit
import os.path

mypath = raw_input("Enter the path of your movies catalog: ")

for root, subdirs, files in os.walk(mypath):
    for f in files:
        guess_file = guessit(f)
        re_f = guess_file['title'].title()
        if 'season' in guess_file:
            re_f += ' - season ' + str(guess_file['season'])
            if 'episode' in guess_file:
                re_f += ' episode ' + str(guess_file['episode'])
        re_f += '.' + guess_file['container']
        os.rename(os.path.join(root, f), os.path.join(root, re_f))

    for d in subdirs:
        guess_dir = guessit(d)
        re_d = guess_dir['title'].title()
        if 'season' in guess_dir:
            re_d += ' - season ' + str(guess_dir['season'])
            if 'episode' in guess_dir:
                re_d += ' episode ' + str(guess_dir['episode'])
        os.rename(os.path.join(root, d), os.path.join(root, re_d))

