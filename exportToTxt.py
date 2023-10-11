import re

def process_srt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    transcript = ''
    for line in lines:
        # Skip time range lines and index lines
        if re.match(r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}', line) or re.match(r'^\d+$', line):
            continue
        # Append text lines to transcript
        transcript += line.strip() + ' '

    # Remove extra spaces
    transcript = re.sub(r'\s+', ' ', transcript).strip()

    # Add a line break whenever there is an opening parenthesis
    transcript = re.sub(r'(\()', r'\n\1', transcript)

    return transcript

def write_transcript(transcript, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(transcript)

# Usage
input_file_path = 'C:/Users/doren/Downloads/ワンピース.S01E01.第1話　俺はルフィ！海賊王になる男だ！.WEBRip.Amazon.ja-jp[sdh].srt'  # Replace with the path to your .srt file
output_file_path = 'C:/EpisodeTranscripts/cleaned_transcript.txt'  # Replace with the desired output file path
transcript = process_srt(input_file_path)
write_transcript(transcript, output_file_path)
