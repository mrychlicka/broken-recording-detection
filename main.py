import sys
import numpy as np
import matplotlib.pyplot as plt
import wave
import soundfile as sf
from pandas import DataFrame


def draw_plot(audio_file):
    """
    Draw a plot of audio file
    :param audio_file: String - path to audio file. Should be .wav
    :return: Plot of audio file (x - time, y - dBFs)
    """
    spf = wave.open(audio_file, 'r')
    signal = spf.readframes(-1)
    signal = np.fromstring(signal, 'Int16')
    plt.figure(1)
    plt.plot(signal)
    return plt.show()


def get_audio_total_sample(audio_file):
    """
    Get basic information about audio file
    :param audio_file: String - path to audio file. Should be .wav
    :return: Return dict with pair of information name and value
    """
    f = sf.SoundFile(audio_file)
    return len(f)


def get_audio_sample_rate(audio_file):
    """
    Get basic information about audio file
    :param audio_file: String - path to audio file. Should be .wav
    :return: Return dict with pair of information name and value
    """
    f = sf.SoundFile(audio_file)
    return f.samplerate


def put_signal_to_dataframe(audio_file):
    spf = wave.open(audio_file, 'r')
    signal = spf.readframes(-1)
    signal = np.fromstring(signal, 'Int16')
    df = DataFrame(signal)
    df['sample'] = [i for i in range(get_audio_total_sample(audio_file=audio_file))]
    return df


FILENAME = sys.argv[1]

draw_plot(audio_file=FILENAME)
sample_rate = get_audio_sample_rate(audio_file=FILENAME)


dataframe = put_signal_to_dataframe(audio_file=FILENAME)
# print(dataframe)

# odciecie poczatku pliku
start_silence = 0
start_signal_index = 0
for sample_ampli in dataframe[0]:
	start_signal_index += 1
	if abs(sample_ampli) > 20:  # TODO: nie hardkodowac
		start_silence += 1
	if start_silence > 50:
		break

print("start_silence: ", start_silence)
print("start_signal_index: ", start_signal_index)

# odciecie konca pliku
end_silence = 0
end_signal_index = get_audio_total_sample(FILENAME)
for sample_ampli in reversed(dataframe[0]):
	end_signal_index -= 1
	if abs(sample_ampli) > 20:  # TODO: nie hardkodowac
		end_silence += 1
	if end_silence > 50:
		break

print("end_silence: ", end_silence)
print("end_signal_index: ", end_signal_index)

# szukanie dziury
ile_sampli = 130
start_gap_sample = 0
gap_length = 0
for idx, sample_ampli in enumerate(dataframe[0]):
	if idx >= start_signal_index and idx <= end_signal_index:
		if abs(sample_ampli) <= 1:
			start_gap_sample = idx
			print("start_gap_sample: ", start_gap_sample)
			gap_length += 1
		else:
			gap_length = 0

		if gap_length >= ile_sampli:
			print("there is a gap, start sample: ", start_gap_sample - ile_sampli)
			break
