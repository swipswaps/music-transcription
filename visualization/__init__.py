import librosa
import librosa.display


import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scipy

from IPython.display import Audio

def audioplayer(path):
    y, fs = librosa.load(path, sr=None)
    return Audio(y, rate=fs)

def samplesplayer(samples, fs):
    return Audio(samples, rate=fs)

def flatten(notesets):
    indices = [i for i, notes in enumerate(notesets) for n in notes]
    flatnotes = [n for notes in notesets for n in notes]
    return indices, flatnotes

def draw_notes(ref, est, style = "."):
    fig, ax = plt.subplots()
    ax.set_ylim(0,128)

    ax.set(xlabel='frame', ylabel='midi note')

    # ref = np.array(ref, dtype=np.float16)
    # est = np.array(est, dtype=np.float16)
    
    indices_correct, correct = flatten([[n for n in fest if n in fref] for fref, fest in zip(ref, est)])
    indices_incorrect, incorrect = flatten([[n for n in fest if n not in fref] for fref, fest in zip(ref, est)])
    indices_ref_rest, ref_rest = flatten([[n for n in fref if n not in fest] for fref, fest in zip(ref, est)])

    ax.plot(indices_ref_rest, ref_rest, style, color="#222222", label="REF")
    ax.plot(indices_incorrect, incorrect, style, color="#ff300e", label="EST incorrect")
    ax.plot(indices_correct, correct, style, color="#0ab02d", label="EST correct")

    legend = ax.legend()

    # return fig

def draw_spectrum(audio, samplerate): 
    fig, ax = plt.subplots()
    
    f, t, X = scipy.signal.stft(audio, samplerate, nperseg=2048, noverlap=2048-256)
    S = librosa.amplitude_to_db(np.abs(X))

    ax.set_yscale('log')
    ax.pcolormesh(t, f, S, cmap="inferno")
    ax.set_ylim(27.5,4400)

def draw_cqt(audio, samplerate):
    s = 3
    C = librosa.cqt(audio, sr=samplerate, n_bins=60 * s, bins_per_octave=12 * s, hop_length=16)
    librosa.display.specshow(librosa.amplitude_to_db(C, ref=np.max),
                             sr=samplerate, x_axis='time', y_axis='cqt_note')