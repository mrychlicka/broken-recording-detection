import sys
import numpy as np
import matplotlib.pyplot as plt
import wave
import soundfile as sf
from pandas import DataFrame


def draw_plot(audio_file):
    """
    Draw a signal as a plot
    :param audio_file: String - path to audio file (.wav)
    :return: Return signal plot (x - time, y - amplitude)
    """
    spf = wave.open(audio_file, 'r')
    signal = np.fromstring(spf.readframes(-1), 'Int16')
    plt.figure(1)
    plt.plot(signal)
    return plt.show()


def get_audio_total_sample(audio_file):
    """
    Get audio file total sample amount
    :param audio_file: String - path to audio file (.wav)
    :return: Return total sample amount in audio file
    """
    f = sf.SoundFile(audio_file)
    return len(f)


def get_audio_sample_rate(audio_file):
    """
    Get sample rate
    :param audio_file: String - path to audio file (.wav)
    :return: Return sample rate
    """
    f = sf.SoundFile(audio_file)
    return f.samplerate


def put_signal_to_dataframe(audio_file):
    """
	Present audio signal as a dataframe
	:param audio_file: String - path to audio file (.wav)
	:return: Return dataframe with two columns: amplitude and sample number
	"""
    spf = wave.open(audio_file, 'r')
    signal = np.fromstring(spf.readframes(-1), 'Int16')
    df = DataFrame(signal)
    df['sample'] = [i for i in range(get_audio_total_sample(audio_file=audio_file))]
    return df


FILENAME = sys.argv[1]
# FILENAME = '/home/gosia/python/broken_recording_detection/nan-ai-file-2.wav'
SAMPLE_RATE = get_audio_sample_rate(audio_file=FILENAME)
FROM_SILENCE_TO_NOISE = 20
MIN_SAMPLES_NUMBER_IN_GAP = 130

draw_plot(audio_file=FILENAME)
dataframe = put_signal_to_dataframe(audio_file=FILENAME)

start_silence = 0  # eliminate audio start silence
start_signal_index = 0
for sample_ampli in dataframe[0]:
	start_signal_index += 1
	if abs(sample_ampli) > FROM_SILENCE_TO_NOISE:
		start_silence += 1
	if start_silence > 50:
		break

end_silence = 0  # eliminate audio end silence
end_signal_index = get_audio_total_sample(FILENAME)
for sample_ampli in reversed(dataframe[0]):
	end_signal_index -= 1
	if abs(sample_ampli) > FROM_SILENCE_TO_NOISE:
		end_silence += 1
	if end_silence > 50:
		break

start_gap_sample = 0
gap_length = 0
invalid = False
for idx, sample_ampli in enumerate(dataframe[0]):
	if idx >= start_signal_index and idx <= end_signal_index:
		if abs(sample_ampli) <= 1:
			start_gap_sample = idx
			# logging.info("start_gap_sample: ", start_gap_sample)
			gap_length += 1
		else:
			gap_length = 0

		if gap_length >= MIN_SAMPLES_NUMBER_IN_GAP:
			invalid = True
			print("{} {} {}".format(FILENAME, 'invalid', start_gap_sample - MIN_SAMPLES_NUMBER_IN_GAP))
			break

if not invalid:
	print('{} {}'.format(FILENAME, 'valid'))