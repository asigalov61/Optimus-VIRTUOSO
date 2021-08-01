# -*- coding: utf-8 -*-
"""Optimus_VIRTUOSO_Composer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/asigalov61/Optimus-VIRTUOSO/blob/main/Optimus_VIRTUOSO_Composer.ipynb

# Optimus VIRTUOSO Composer (ver. 3.0)

## "Music never allows falsehoods for even the deaf hear flat notes!" ---OV

***

Powered by tegridy-tools TMIDIX Optimus Processors: https://github.com/asigalov61/tegridy-tools

***

Credit for char-based GPT2 code used in this colab goes out to Andrej Karpathy: https://github.com/karpathy/minGPT

***

WARNING: This complete implementation is a functioning model of the Artificial Intelligence. Please excercise great humility, care, and respect. https://www.nscai.gov/

***

#### Project Los Angeles

#### Tegridy Code 2021

***

# Setup Environment, clone needed repos, and install all required dependencies
"""

#@title nvidia-smi gpu check
!nvidia-smi

#@title Install all dependencies (run only once per session)

!git clone https://github.com/asigalov61/tegridy-tools

!pip install torch
!pip install tqdm

!apt install fluidsynth #Pip does not work for some reason. Only apt works
!pip install midi2audio
!pip install pretty_midi

#@title Import all needed modules

print('Loading needed modules. Please wait...')
import os
from datetime import datetime
import secrets

import tqdm
from tqdm import auto

if not os.path.exists('/content/Dataset'):
    os.makedirs('/content/Dataset')

print('Loading TMIDIX module...')
os.chdir('/content/tegridy-tools/tegridy-tools')
import TMIDIX

os.chdir('/content/tegridy-tools/tegridy-tools')
from minGPT import *

from midi2audio import FluidSynth
import pretty_midi
import librosa.display
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

from IPython.display import display, Javascript, HTML, Audio

from google.colab import output, drive

os.chdir('/content/')
print('Loading complete. Enjoy! :)')

"""# Setup and prep the model"""

# Commented out IPython magic to ensure Python compatibility.
#@title Download ready-to-use pre-trained composer model and the TXT dataset
# %cd /content/

print('=' * 70)
print('Downloading pre-trained dataset-model...Please wait...')
print('=' * 70)

!wget https://github.com/asigalov61/Optimus-VIRTUOSO/raw/main/Dataset-Model/MuseNet/Custom-Children-Songs/Optimus-VIRTUOSO-Dataset-Model.zip.001
!wget https://github.com/asigalov61/Optimus-VIRTUOSO/raw/main/Dataset-Model/MuseNet/Custom-Children-Songs/Optimus-VIRTUOSO-Dataset-Model.zip.002
!wget https://github.com/asigalov61/Optimus-VIRTUOSO/raw/main/Dataset-Model/MuseNet/Custom-Children-Songs/Optimus-VIRTUOSO-Dataset-Model.zip.003

!cat Optimus-VIRTUOSO-Dataset-Model.zip* > Optimus-VIRTUOSO-Dataset-Model.zip
print('=' * 70)

!unzip -j Optimus-VIRTUOSO-Dataset-Model.zip
print('=' * 70)

print('Done! Enjoy! :)')
print('=' * 70)
# %cd /content/

#@title Load the downloaded model and the dataset

full_path_to_training_text_file = "/content/Optimus-VIRTUOSO-Music-Dataset.txt"
model_attention_span_in_tokens = 512
model_embed_size = 512
number_of_heads = 8
number_of_layers = 6
number_of_training_epochs = 5
training_batch_size = 48
number_of_dataloader_threads = 4
model_learning_rate = 6e-4
checkpoint_full_path = "" 

if checkpoint_full_path == '':
  checkpoint_full_path = None


trainer, model, train_dataset = MainLoader(full_path_to_training_text_file,
                                          None,
                                          number_of_dataloader_threads,
                                          model_attention_span_in_tokens,
                                          model_embed_size,
                                          number_of_heads,
                                          number_of_layers,
                                          number_of_training_epochs,
                                          training_batch_size,
                                          model_learning_rate,
                                          ckpt_path=checkpoint_full_path)

full_path_to_model_checkpoint = "/content/Optimus-VIRTUOSO-Trained-Model.pth"
model = torch.load(full_path_to_model_checkpoint)
model.eval()

#@title Visually check positional embeddings to make sure everything is ok

PlotPositionalEmbeddings(model, model_attention_span_in_tokens)

"""# Generate original compound music

# STEP 1: Generate the composition seed
"""

#@title (BEST) Self-continuation from the dataset

#@markdown NOTE: You can repeat this step as many times as you like until you find the right seed that you like

completion = ''
completion1 = ''
completion2 = ''
completion3 = ''

print('Optimus VIRTUOSO Model Generator')
# print('Starting up...')
number_of_tokens_to_generate = 1024
creativity_temperature = 1
top_k_prob = 64
input_prompt = "SONG="
self_continuation = True

os.chdir('/content/')

if self_continuation:
    with open(full_path_to_training_text_file) as f:
      dataset = f.read()

    idx = secrets.randbelow(len(dataset)-256)
    input_prompt = 'SONG=Self-Continuation' + chr(10)
    input_prompt += dataset[idx:idx+256]

completion = Generate(model,
                      train_dataset,
                      trainer,
                      number_of_tokens_to_generate,
                      creativity_temperature,
                      top_k_prob,
                      input_prompt)

# Stuff for datetime stamp
filename = '/content/Optimus-VIRTUOSO-Composition-' + 'generated-on-' 
fname = TMIDIX.Tegridy_File_Time_Stamp(filename)
fname1 = TMIDIX.Tegridy_File_Time_Stamp(filename)
fname2 = TMIDIX.Tegridy_File_Time_Stamp(filename)


number_of_ticks_per_quarter = 500
dataset_time_denominator = 1
melody_conditioned_encoding = False
encoding_has_MIDI_channels = True
encoding_has_velocities = True
simulate_velocity = False
save_only_first_composition = False
chars_encoding_offset_used_for_dataset = 33


output_list, song_name = TMIDIX.Optimus_TXT_to_Notes_Converter(completion, 
                                                                has_MIDI_channels=encoding_has_MIDI_channels, 
                                                                simulate_velocity=simulate_velocity,
                                                                char_encoding_offset=chars_encoding_offset_used_for_dataset,
                                                                save_only_first_composition=save_only_first_composition,
                                                                dataset_MIDI_events_time_denominator=dataset_time_denominator,
                                                                has_velocities=encoding_has_velocities
                                                                )

# print('Converting Song to MIDI...')

output_signature = 'Optimus VIRTUOSO'

detailed_stats = TMIDIX.Tegridy_SONG_to_MIDI_Converter(output_list,
                                                      output_signature = output_signature,  
                                                      output_file_name = fname, 
                                                      track_name=song_name, 
                                                      number_of_ticks_per_quarter=number_of_ticks_per_quarter)

fn = os.path.basename(fname + '.mid')
fn1 = fn.split('.')[0]

# print('Plotting the composition. Please wait...')

pm = pretty_midi.PrettyMIDI(fname + '.mid')

# Retrieve piano roll of the MIDI file
piano_roll = pm.get_piano_roll()

plt.figure(figsize=(14, 5))
librosa.display.specshow(piano_roll, x_axis='time', y_axis='cqt_note', fmin=1, hop_length=160, sr=16000, cmap=plt.cm.hot)
plt.title(fn1)

FluidSynth("/usr/share/sounds/sf2/FluidR3_GM.sf2", 16000).midi_to_audio(str(fname + '.mid'), str(fname + '.wav'))
Audio(str(fname + '.wav'), rate=16000)

#@title (ALTERNATIVE) Continue your own MIDI

#@markdown NOTE: The model was trained on a relatively small dataset, so custom MIDI continuations may not be perfect

full_path_to_custom_MIDI_file = "/content/tegridy-tools/tegridy-tools/seed.mid" #@param {type:"string"}

completion = ''
completion1 = ''
completion2 = ''

# Stuff for datetime stamp
filename = '/content/Optimus-VIRTUOSO-Composition-' + 'generated-on-' 
fname = TMIDIX.Tegridy_File_Time_Stamp(filename)
fname1 = TMIDIX.Tegridy_File_Time_Stamp(filename)
fname2 = TMIDIX.Tegridy_File_Time_Stamp(filename)

data = TMIDIX.Optimus_MIDI_TXT_Processor(full_path_to_custom_MIDI_file,
                                         output_velocity=True,
                                         output_MIDI_channels=True,
                                         MIDI_channel=16,
                                         MIDI_patch=range(0, 127),
                                         char_offset=33,
                                         perfect_timings=True,
                                         musenet_encoding=True)
custom_prime = data[0][-1024:]
completion3 = data[0]
completion4 = data[0][:len(custom_prime)]
completion = custom_prime

# print('Plotting the composition. Please wait...')

# print('Done!')
# print('Saving to', str(fname + '.txt'))
with open(fname + '.txt', "w") as text_file:
    print(completion3, file=text_file)

number_of_ticks_per_quarter = 500
dataset_time_denominator = 1
melody_conditioned_encoding = False
encoding_has_MIDI_channels = True
encoding_has_velocities = True
simulate_velocity = False
save_only_first_composition = False
chars_encoding_offset_used_for_dataset = 33


output_list, song_name = TMIDIX.Optimus_TXT_to_Notes_Converter(completion3, 
                                                                has_MIDI_channels=encoding_has_MIDI_channels, 
                                                                simulate_velocity=simulate_velocity,
                                                                char_encoding_offset=chars_encoding_offset_used_for_dataset,
                                                                save_only_first_composition=save_only_first_composition,
                                                                dataset_MIDI_events_time_denominator=dataset_time_denominator,
                                                                has_velocities=encoding_has_velocities
                                                                )

# print('Converting Song to MIDI...')

output_signature = 'Optimus VIRTUOSO'

detailed_stats = TMIDIX.Tegridy_SONG_to_MIDI_Converter(output_list,
                                                      output_signature = output_signature,  
                                                      output_file_name = fname, 
                                                      track_name=song_name, 
                                                      number_of_ticks_per_quarter=number_of_ticks_per_quarter)

fn = os.path.basename(fname + '.mid')
fn1 = fn.split('.')[0]

pm = pretty_midi.PrettyMIDI(fname + '.mid')

# Retrieve piano roll of the MIDI file
piano_roll = pm.get_piano_roll()

plt.figure(figsize=(14, 5))
librosa.display.specshow(piano_roll, x_axis='time', y_axis='cqt_note', fmin=1, hop_length=160, sr=16000, cmap=plt.cm.hot)
plt.title(fn1)

FluidSynth("/usr/share/sounds/sf2/FluidR3_GM.sf2", 16000).midi_to_audio(str(fname + '.mid'), str(fname + '.wav'))
Audio(str(fname + '.wav'), rate=16000)

"""# STEP 2: Continuation"""

#@title Generate continuation

#@markdown NOTE: You can repeat this step until you find a perfect continuation that you like


print('Optimus VIRTUOSO Model Generator')
# print('Starting up...')
number_of_tokens_to_generate = 1024
creativity_temperature = 1
top_k_prob = 64
if completion2 == '':
  input_prompt = completion
else:
  input_prompt = completion2
self_continuation = False

os.chdir('/content/')

completion1 = Generate(model,
                      train_dataset,
                      trainer,
                      number_of_tokens_to_generate,
                      creativity_temperature,
                      top_k_prob,
                      input_prompt)[-2048:]

# print('Done!')
# print('Saving to', str(fname + '.txt'))
with open(fname2 + '.txt', "w") as text_file:
    print(completion1, file=text_file)

number_of_ticks_per_quarter = 500
dataset_time_denominator = 1
melody_conditioned_encoding = False
encoding_has_MIDI_channels = True
encoding_has_velocities = True
simulate_velocity = False
save_only_first_composition = False
chars_encoding_offset_used_for_dataset = 33

output_list, song_name = TMIDIX.Optimus_TXT_to_Notes_Converter(completion1, 
                                                                has_MIDI_channels=encoding_has_MIDI_channels, 
                                                                simulate_velocity=simulate_velocity,
                                                                char_encoding_offset=chars_encoding_offset_used_for_dataset,
                                                                save_only_first_composition=save_only_first_composition,
                                                                dataset_MIDI_events_time_denominator=dataset_time_denominator,
                                                                has_velocities=encoding_has_velocities
                                                                )

# print('Converting Song to MIDI...')

output_signature = 'Optimus VIRTUOSO'

detailed_stats = TMIDIX.Tegridy_SONG_to_MIDI_Converter(output_list,
                                                      output_signature = output_signature,  
                                                      output_file_name = fname2, 
                                                      track_name=song_name, 
                                                      number_of_ticks_per_quarter=number_of_ticks_per_quarter)

fn = os.path.basename(fname2 + '.mid')
fn1 = fn.split('.')[0]

# print('Plotting the composition. Please wait...')

pm = pretty_midi.PrettyMIDI(fname2 + '.mid')

# Retrieve piano roll of the MIDI file
piano_roll = pm.get_piano_roll()

plt.figure(figsize=(14, 5))
librosa.display.specshow(piano_roll, x_axis='time', y_axis='cqt_note', fmin=1, hop_length=160, sr=16000, cmap=plt.cm.hot)
plt.title(fn1)

FluidSynth("/usr/share/sounds/sf2/FluidR3_GM.sf2", 16000).midi_to_audio(str(fname2 + '.mid'), str(fname2 + '.wav'))
Audio(str(fname2 + '.wav'), rate=16000)

"""# STEP 3: Final composition"""

#@title (STEP 3) Add last continuation to the final composition

#@markdown NOTE: DO NOT REPEAT THIS STEP until you have generated the next continuation block in STEP 2

if completion2 == '':
  completion2 = completion1
else:
  completion2 += completion1[-1024:]

if completion3 != '' and custom_prime != '':
  completion2 = completion3 + completion1[1024:]
  completion3 = ''

completion2 = 'SONG=Continuation' + chr(10) + completion2

# print('Done!')
# print('Saving to', str(fname + '.txt'))
with open(fname1 + '.txt', "w") as text_file:
    print(completion2, file=text_file)

number_of_ticks_per_quarter = 500
dataset_time_denominator = 1
melody_conditioned_encoding = False
encoding_has_MIDI_channels = True
encoding_has_velocities = True
simulate_velocity = False
save_only_first_composition = False
chars_encoding_offset_used_for_dataset = 33


output_list, song_name = TMIDIX.Optimus_TXT_to_Notes_Converter(completion2, 
                                                                has_MIDI_channels=encoding_has_MIDI_channels, 
                                                                simulate_velocity=simulate_velocity,
                                                                char_encoding_offset=chars_encoding_offset_used_for_dataset,
                                                                save_only_first_composition=save_only_first_composition,
                                                                dataset_MIDI_events_time_denominator=dataset_time_denominator,
                                                                has_velocities=encoding_has_velocities
                                                                )

# print('Converting Song to MIDI...')

output_signature = 'Optimus VIRTUOSO Composer'

detailed_stats = TMIDIX.Tegridy_SONG_to_MIDI_Converter(output_list,
                                                      output_signature = output_signature,  
                                                      output_file_name = fname1, 
                                                      track_name=song_name, 
                                                      number_of_ticks_per_quarter=number_of_ticks_per_quarter)

fn = os.path.basename(fname1 + '.mid')
fn1 = fn.split('.')[0]

# print('Plotting the composition. Please wait...')

pm = pretty_midi.PrettyMIDI(fname1 + '.mid')

# Retrieve piano roll of the MIDI file
piano_roll = pm.get_piano_roll()

plt.figure(figsize=(14, 5))
librosa.display.specshow(piano_roll, x_axis='time', y_axis='cqt_note', fmin=1, hop_length=160, sr=16000, cmap=plt.cm.hot)
plt.title(fn1)

FluidSynth("/usr/share/sounds/sf2/FluidR3_GM.sf2", 16000).midi_to_audio(str(fname1 + '.mid'), str(fname1 + '.wav'))
Audio(str(fname1 + '.wav'), rate=16000)

#@title (OPTIONAL STEP) Undo the last continuation

#@markdown You can undo the last continuation here just in case. Then you can go to STEP 2 to regenerate it

#@markdown NOTE: You can undo as many continuation blocks as you like

print('=' * 70)
print('Removing last continuation block...')
print('=' * 70)
print('Old song length is', len(completion2), 'tokens')
completion2 = completion2[:-1024]
print('New song length is', len(completion2), 'tokens')
print('=' * 70)

if completion2 != '':
  # print('Plotting the composition. Please wait...')

  # print('Done!')
  # print('Saving to', str(fname + '.txt'))
  with open(fname1 + '.txt', "w") as text_file:
      print(completion2, file=text_file)

  number_of_ticks_per_quarter = 500
  dataset_time_denominator = 1
  melody_conditioned_encoding = False
  encoding_has_MIDI_channels = True
  encoding_has_velocities = True
  simulate_velocity = False
  save_only_first_composition = False
  chars_encoding_offset_used_for_dataset = 33


  output_list, song_name = TMIDIX.Optimus_TXT_to_Notes_Converter(completion2, 
                                                                  has_MIDI_channels=encoding_has_MIDI_channels, 
                                                                  simulate_velocity=simulate_velocity,
                                                                  char_encoding_offset=chars_encoding_offset_used_for_dataset,
                                                                  save_only_first_composition=save_only_first_composition,
                                                                  dataset_MIDI_events_time_denominator=dataset_time_denominator,
                                                                  has_velocities=encoding_has_velocities
                                                                  )

  # print('Converting Song to MIDI...')

  output_signature = 'Optimus VIRTUOSO'

  detailed_stats = TMIDIX.Tegridy_SONG_to_MIDI_Converter(output_list,
                                                        output_signature = output_signature,  
                                                        output_file_name = fname1, 
                                                        track_name=song_name, 
                                                        number_of_ticks_per_quarter=number_of_ticks_per_quarter)

  fn = os.path.basename(fname1 + '.mid')
  fn1 = fn.split('.')[0]

  pm = pretty_midi.PrettyMIDI(fname1 + '.mid')

  # Retrieve piano roll of the MIDI file
  piano_roll = pm.get_piano_roll()

  plt.figure(figsize=(14, 5))
  librosa.display.specshow(piano_roll, x_axis='time', y_axis='cqt_note', fmin=1, hop_length=160, sr=16000, cmap=plt.cm.hot)
  plt.title(fn1)

  FluidSynth("/usr/share/sounds/sf2/FluidR3_GM.sf2", 16000).midi_to_audio(str(fname1 + '.mid'), str(fname1 + '.wav'))
  Audio(str(fname1 + '.wav'), rate=16000)

"""# STEP 4: Download the result"""

#@title Download the final composition
print('Downloading your composition now...')
print(fname1)
from google.colab import files
files.download(fname1 + '.mid')

"""# Congrats! You did it! :)"""