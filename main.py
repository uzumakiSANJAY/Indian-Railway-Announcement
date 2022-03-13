from email.mime import audio
import os
import pandas as pd
from pip import main
from pydub import AudioSegment
from gtts import gTTS


def textToSpeech(text,filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext , lang= language , slow= False)
    myobj.save(filename)

#This function returns pydubs audio segment
def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined


def generateSkeleton():
    #1 Generate kripya dhayan dijiya
    audio = AudioSegment.from_mp3('Indian RAILWAYS Announcements.mp3')
    start = 2000
    finish = 3500
    audioProcessed = audio[start : finish]
    audioProcessed.export("1_hindi.mp3", format="mp3")

    # 2 is from - city

    # 3 - Generate se chalkar 
    start = 9000
    finish = 9500
    audioProcessed = audio[start : finish]
    audioProcessed.export("2_hindi.mp3", format="mp3")

    # 4 - is via-city

    # 5 - Genarete se ana wali
    start = 11000
    finish = 12000
    audioProcessed = audio[start : finish]
    audioProcessed.export("3_hindi.mp3", format="mp3")

    # 6 is to - city

    # 7 Generate ko jaane wali gaari sankhya

    # 8 is train no name

    # 9 - Genarate kuch hi samay me platform sankhya

    # 10 - is platform number

    # 11 - Generate par aa rahi hai 

def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index , item in df.iterrows():
        # 2 Generate from - city
        textToSpeech(item['From'],'2_hindi.mp3')
        # 4 - Generate via-city
        textToSpeech(item['via'],'4_hindi.mp3')
        # 6 - Generate to - city
        textToSpeech(item['to'],'6_hindi.mp3')
        # 8 - Generate train no name
        textToSpeech(item['train_no'] +" " +item['train_name'],'8_hindi.mp3')
        # 10 - Generate platform number
        textToSpeech(item['platfrom'],'10_hindi.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(1,12)]

        announcement = mergeAudios(audios)
        announcement.export(f"announcement_{index+1}.mp3",format = "mp3")

    

if __name__ == "__main__":
    print("Generating skeleton")
    generateSkeleton()
    print("Now generating announcement..")
    generateAnnouncement('announce_hindi.xlsx')
