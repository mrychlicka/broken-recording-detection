  ====== BROKEN RECORDING DETECTOR  ======

Program takes as input audio file (.wav) and checks if recording is corrupted - if includes sudden silent gap.

 === Installing ===

To install required packages run: pip3 install -r requirements.txt

 === Run ===

 Run program by typing in terminal: python -m main.py [file_name.wav] where 'audio_file_name' is name of recording

 === Steps ===

1. Put audio file to folder in which script is located
2. Run program by typing in terminal: python -m main.py [file_name.wav] where 'file_name' is name of recording
3. First thing you will see is recording visualization plot, which you can zoom to analyse signal
4. After closing plot window program returns output:
[file_name] [valid] - in case file includes no sudden silence gap
[file_name] [invalid] [index_of_first_dropped_sample] - if recording includes silence gap

 === Author ===

Malgorzata Rychlicka

