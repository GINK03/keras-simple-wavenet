
import glob
import os
import shutil
from concurrent.futures import ThreadPoolExecutor as TPE

args = [(i,fn) for i, fn in enumerate(glob.glob('./LibriSpeech/dev-clean/*/*/*.flac'))]
def tmap(arg):
	i, fn = arg
	print(i, fn)
	os.popen(f'ffmpeg -i {fn} {i}.wav 2>&1').read()
with TPE(max_workers=16) as exe:
	exe.map(tmap, args)

with open('file.txt', 'w') as fp:
	fp.write('#file.txt\n')
	for fn in glob.glob('*.wav'):
		fp.write(f"file '{fn}' \n")
os.system('ffmpeg -f concat -i file.txt -c copy train.wav')
shutil.move('train.wav', '../train.wav')
os.system('rm *.wav')

args = [(i,fn) for i, fn in enumerate(glob.glob('./LibriSpeech/test-clean/*/*/*.flac'))]
def tmap(arg):
	i, fn = arg
	print(i, fn)
	os.popen(f'ffmpeg -i {fn} {i}.wav 2>&1').read()
with TPE(max_workers=16) as exe:
	exe.map(tmap, args)

with open('file.txt', 'w') as fp:
	fp.write('#file.txt\n')
	for fn in glob.glob('*.wav'):
		fp.write(f"file '{fn}' \n")
os.system('ffmpeg -f concat -i file.txt -c copy validate.wav')
shutil.move('validate.wav', '../validate.wav')
os.system('rm *.wav')
