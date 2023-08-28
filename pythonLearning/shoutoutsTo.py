import win32com.client as wincl

def shoutoutVoice():
    speaker_number = 0
    spk = wincl.Dispatch("SAPI.SpVoice")
    vcs = spk.GetVoices()
    SVSFlag=11
    print(vcs.Item (speaker_number) .GetAttribute ("Name")) # speaker name 
    spk.Voice               
    spk.SetVoice(vcs.Item(speaker_number)) # set voice (see Windows Text-to-Speech settings)
    shoutOutList=['Nishant Chapagai','Sahil Khadka','Utshav Khadka','Binay Thakur','Anisha Kumari Dhakal','Rakesh Joshi']
    spk.Rate=1
    spk.Speak("Jay Shree Ram!") 
    for names in shoutOutList:
        spk.Speak(f"Shoutout to:{names}")
    spk.Speak("Thank you everybody. Jay Shree Ram!")
shoutoutVoice()