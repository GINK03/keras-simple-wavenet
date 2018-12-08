
import glob
import os

from concurrent.futures import ThreadPoolExecutor as TPE

args = [(i,fn) for i, fn in enumerate(glob.glob('./LibriSpeech/dev-clean/*/*/*.flac')[:100])]
def tmap(arg):
	i, fn = arg
	print(i, fn)
	os.system(f'ffmpeg -i {fn} {i}.wav')
with TPE(max_workers=16) as exe:
	exe.map(tmap, args)
os.system('cat *.wav > ../train.wav')
os.system('rm *.wav')

args = [(i,fn) for i, fn in enumerate(glob.glob('./LibriSpeech/test-clean/*/*/*.flac')[:100])]
def tmap(arg):
	i, fn = arg
	print(i, fn)
	os.system(f'ffmpeg -i {fn} {i}.wav')
with TPE(max_workers=16) as exe:
	exe.map(tmap, args)
os.system('cat *.wav > ../validate.wav')
os.system('rm *.wav')
