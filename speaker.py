def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == '__main__':
    print("Enter the message you want to listen")
    ls = ["ankur", "yug", "jason", "jarvis", "alex"]
    for i in ls:
        speak(i)
