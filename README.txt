====== BROKEN RECORDING DETECTOR  ======

Program takes as input digital audio signal (.wav) produced by NAN system and checks if signal is corrupted - if includes sudden silent gap.
OUTPUT:
A digital audio signal visualization plot (time/amplitude) and information: file name, valid/invalid
and number of first sample of silence gap if file is invalid

=== Installing ===

To install required packages run: pip3 install -r requirements.txt

=== Run ===

Run program by typing in terminal: python3 -m main [file_name.wav] where 'file_name' is name of recording

=== Steps ===

1. Put audio file to folder in which script is located
2. Run program by typing in terminal: python3 -m main [file_name.wav]
3. Visualization plot shows
4. After closing plot window program returns output:
[file_name] [valid] - in case file includes no sudden silence gap
[file_name] [invalid] [index_of_first_dropped_sample] - if recording includes silence gap

=== Author ===

Malgorzata Rychlicka
