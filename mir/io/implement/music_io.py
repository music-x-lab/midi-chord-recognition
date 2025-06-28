from mir.io.feature_io_base import *
import librosa
import soundfile as sf

class MusicIO(FeatureIO):
    def read(self, filename, entry):
        y, sr = librosa.load(filename, sr=entry.prop.sr, mono=True)
        return y #(y-np.mean(y))/np.std(y)

    def write(self, data, filename, entry):
        sr=entry.prop.sr
        # librosa.output.write_wav(filename, y=data, sr=sr, norm=False)
        # Write with soundfile
        sf.write(filename, data, sr, format='WAV', subtype='PCM_16')

    def visualize(self, data, filename, entry, override_sr):
        sr=entry.prop.sr
        # librosa.output.write_wav(filename, y=data, sr=sr, norm=True)
        # Write with soundfile
        sf.write(filename, data, sr, format='WAV', subtype='PCM_16')

    def get_visualize_extention_name(self):
        return "wav"