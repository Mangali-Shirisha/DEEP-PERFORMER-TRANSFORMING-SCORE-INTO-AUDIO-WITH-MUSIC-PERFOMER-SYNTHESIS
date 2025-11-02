from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import UserRegistrationModel


# Create your views here.




def UserRegisterActions(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'You have been successfully registered')
            form = UserRegistrationForm()
            return render(request, 'UserRegistrations.html', {'form': form})
        else:
            messages.success(request, 'Email or Mobile Already Existed')
            print("Invalid form")
    else:
        form = UserRegistrationForm()
    return render(request, 'UserRegistrations.html', {'form': form})


def UserLoginCheck(request):
    if request.method =='POST':
        loginid=request.POST.get('loginid')
        pswd=request.POST.get('pswd')
        print("Login ID = ", loginid, ' Password = ', pswd)
        try:
            check = UserRegistrationModel.objects.get(
                loginid=loginid, password=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "activated":
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['loginid'] = loginid
                request.session['email'] = check.email
                print("User id At", check.id, status)
                return render(request, 'users/userhome.html', {})
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request, 'userlogin.html')
        except Exception as e:
            print('Exception is ', str(e))
            pass
            messages.success(request, 'Invalid Login id and password')
        return render(request, 'userlogin.html', {})


def UserHome(request):

    return render(request, 'users/userhome.html', {})


def viewData(request):
    import pandas as pd

    from django.conf import settings
    import os
    path=os.path.join(settings.MEDIA_ROOT,'violin.csv')
    df=pd.read_csv(path)
    df=df.to_html



    return render(request, 'users/userviewdata.html', {'data': df})
def violin_audio(request):
    import  librosa.display
    import  os
    from django.conf import settings
    from matplotlib import pyplot as plt
    from pygame import mixer
    import pygame.mixer
    import pygame
    audiopath = os.path.join(settings.MEDIA_ROOT,'Bhairavi01.wav')
    pygame.mixer.init()
    pygame.mixer.music.load(audiopath)
    pygame.mixer.music.play()
    
    import  soundfile as sf
    data, samplerate = sf.read(audiopath)
    plt.figure(figsize=(15, 5))
    librosa.display.waveshow(data, sr=samplerate)
    plt.show()

    return render(request,'Users/violin.html')
def piano_audio(request):
    import librosa.display
    import os
    import numpy as np
    from django.conf import settings
    from matplotlib import pyplot as plt
    from pygame import mixer
    audiopath = os.path.join(settings.MEDIA_ROOT, 'A_dim_2_0.wav')
    mixer.init()
    mixer.music.load(audiopath)
    mixer.music.play()
    import soundfile as sf
    data, samplerate = sf.read(audiopath)
    fig,ax=plt.subplots(figsize=(15, 5),nrows=1,ncols=3)
    librosa.display.waveshow(data, sr=samplerate,ax=ax[0])
    librosa.display.waveshow(data, sr=samplerate, alpha=0.25, ax=ax[1])
    librosa.display.waveshow(data, sr=samplerate, color='r', alpha=0.5, ax=ax[1])
    S = librosa.feature.melspectrogram(y=data, sr=samplerate, n_mels=128, fmax=8000)
    S_dB = librosa.power_to_db(S, ref=np.max)
    mel = librosa.display.specshow(S_dB, x_axis='time', y_axis='mel', sr=samplerate, fmax=8000, ax=ax[2])
    fig.colorbar(mel, ax=ax[2], format='%+2.0f dB')
    ax[0].set(title='Monophonic')
    ax[1].set(title='Harmonic & Percussive')
    ax[2].set(title='Mel-frequency spectrogram')
    plt.show()

    C = librosa.feature.chroma_cqt(y=data, sr=samplerate)
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(C, sr=samplerate, x_axis='time', y_axis='chroma', vmin=0, vmax=1)
    plt.title('Chromagram')
    plt.colorbar()
    plt.tight_layout()
    plt.show()
    return render(request,'Users/piano.html')


def violin_cll(request):
    from .utility import algorithm
    accuracy, recall, f1score = algorithm.calc_random_forest()

    print("====", accuracy)

    return render(request, 'users/violinrf.html',
                  {'accuracy': accuracy, "recall": recall, "f1score": f1score})


def piano_rfcll(request):
    from .utility import piano
    accuracy, recall, f1score = piano.calc_random_forest()

    print("====", accuracy)

    return render(request, 'users/pianorf.html',
                  {'accuracy': accuracy, "recall": recall, "f1score": f1score})



