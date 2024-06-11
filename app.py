import os
import requests
import json
from similarity import SimilarityFinder
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import os


temp_folder = "./Input"


class Handler():
    def __init__(self):
        self.similarity = SimilarityFinder()
        self.bot_sentences = self.similarity.bot_sentences
        self.output_path = "./Output"

    def process_all_wav_files(self,directory):
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if file_path.endswith('.wav'):
                print(f"Processing file: {file_path}")
                self.process_new_file(file_path)

    def process_new_file(self,file_path):
        if file_path.endswith('.wav'):
            response = requests.post('http://localhost:8000/uploadfile', files={'file': open(file_path, 'rb')})
            if response.status_code == 200:
                try:
                    data = response.json()
                except json.JSONDecodeError:
                    print("Failed to decode JSON from the response")
                    return

                if data.get("status"):
                    self.save_json(data.get("msg"), file_path)
                    # print(data.get("msg"))

    def save_json(self,data, original_file_path):
        if not isinstance(data, dict):
            print("Data is not a dictionary.")
            return

        # Extracting main text from each speaker
        processed_data = {key: value["trascript"] for key, value in data.items() if isinstance(value, dict)}

        time_stamps = {
            key: {
                "time_stamp_start": value["time_stamp_start"],
                "time_stamp_end": value["time_stamp_end"]
            }
            for key, value in data.items()
            if isinstance(value, dict)
        }

        print("Transcript",processed_data)
        print("time_stamps",time_stamps)
        print("original_file_path",original_file_path)

        # Check if json_data is not empty before processing
        # if processed_data:
        #     self.process_transcripts(processed_data, original_file_path)
        #     print("Converted successfully.")
        # else:
        #     print("No valid transcript data found.")

    def process_transcripts(self, processed_data, original_file_path):
        print("before:",processed_data)
        speaker_list = list(processed_data.keys())
        splitted_transcript = [processed_data[speaker] for speaker in speaker_list]
        bot_indexes = self.similarity.similarityFinder(self.bot_sentences, splitted_transcript)
        bot_indexes = list(set(bot_indexes))

        tagged_transcript = []
        for index, transcript in enumerate(splitted_transcript):
            speaker_tag = "Bot Speaker" if index in bot_indexes else "Customer Speaker"
            tagged_transcript.append({speaker_tag: transcript})

        folder_name = os.path.basename(original_file_path).split('.')[0]
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)

        output_file_path = os.path.join(self.output_path, folder_name + ".json")
        with open(output_file_path, 'w') as outfile:
            json.dump(tagged_transcript, outfile, indent=4)


app = FastAPI()

# Assuming the Handler class and its methods are correctly defined as you provided

handler = Handler()  # Create an instance of your Handler        

handler.process_all_wav_files(temp_folder)