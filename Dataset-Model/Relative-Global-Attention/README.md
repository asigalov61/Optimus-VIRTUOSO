# SOTA Relative Global Attention Model

[![Open In Colab][colab-badge2]][colab-notebook2]

[colab-notebook2]: <https://colab.research.google.com/github/asigalov61/Optimus-VIRTUOSO/blob/main/Optimus_VIRTUOSO_Relative_Global_Attention_Edition.ipynb>
[colab-badge2]: <https://colab.research.google.com/assets/colab-badge.svg>

***

## Trained to 0.027 Floss/0.993 acc for 2 epoch on Google Colab Tesla SXM2 GPU (~16 hours)

## Final model size: 41.1 MB (43,171,840 bytes) [Compare with Google PT or OpenAI Musenet]

## Dataset: Endless Piano Carousel MIDI dataset (not included so download it or make sure to use random/custom priming)

***

### NOTES: This is a one-short learner architecture and model, so the tests have confirmed that training for 2 epcchs is only detrimental to the results. At least with Music. This architecture either learns or it does not, so if you are not getting good results, it is always a great idea to thoroughly check the dataset...

***

### Model Specs

```
max_seq = 1024
n_layers = 6
num_heads = 8
d_model = 512
dim_feedforward = 512
dropout_prob = 0.1

```

***

### Training Loss Graph:

<img width="512" src="https://github.com/asigalov61/Optimus-VIRTUOSO/raw/main/Dataset-Model/Relative-Global-Attention/training-loss.png">

### Raw stats/SOTA proof

```
Epoch: 1 Loss: 0.051 LR: 9.3368691e-05: 100%|██████████| 224041/224041 [7:31:31<00:00,  8.27it/s]
Loss val: 0.01719  Acc: 0.993: 100%|██████████| 67213/67213 [59:44<00:00, 18.75it/s]
Best eval acc epoch: 1
Best eval acc: 0.992951141857323

Best eval loss epoch: 1
Best eval loss: 0.027301499948002867
Epoch: 2 Loss: 0.03646 LR: 6.6021634e-05: 100%|██████████| 224041/224041 [7:34:10<00:00,  8.22it/s]
Loss val: 0.0241  Acc: 0.994:   1%|▏         | 841/67213 [00:45<59:13, 18.68it/s]

```

### Raw performance/music generation stats example:

```

1000 / 1024
100%|██████████| 300/300 [1:10:36<00:00, 14.12s/it]

======================================================================
Block number: 300
Composition length so far: 307200 notes
======================================================================
Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!Done!
Total blocks: 300
Final omposition length: 307200 notes
======================================================================

Converting to MIDI. Please stand-by...
Done! Enjoy! :)
Done!
Downloading your composition now...
======================================================================
Detailed MIDI stats:
======================================================================
bank_select | []
======================================================================
channels_by_track | [set(), {0}]
======================================================================
channels_total | {0}
======================================================================
general_midi_mode | []
======================================================================
ntracks | 2
======================================================================
nticks | 5300180
======================================================================
num_notes_by_channel | {0: 72248}
======================================================================
patch_changes_by_track | [{}, {0: 0, 1: 24, 2: 32, 3: 40, 4: 42, 5: 46, 6: 56, 7: 71, 8: 73, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0}]
======================================================================
patch_changes_total | {0, 32, 71, 40, 73, 42, 46, 24, 56}
======================================================================
percussion | {}
======================================================================
pitches | {52: 1267, 60: 2794, 59: 1542, 64: 2131, 153: 1, 76: 1405, 71: 1595, 67: 3087, 61: 1620, 57: 1390, 152: 1, 69: 1937, 33: 263, 54: 877, 66: 1472, 63: 2482, 68: 2304, 56: 1712, 72: 2911, 75: 1572, 73: 1632, 49: 1141, 45: 682, 51: 1352, 44: 938, 48: 1349, 27: 31, 32: 246, 34: 314, 36: 697, 47: 621, 40: 529, 42: 504, 39: 577, 37: 542, 46: 810, 62: 2077, 50: 1029, 38: 464, 74: 1629, 78: 819, 35: 252, 30: 180, 28: 66, 80: 925, 81: 797, 83: 390, 85: 347, 84: 716, 87: 325, 88: 180, 90: 75, 86: 337, 25: 21, 92: 167, 53: 1340, 58: 1566, 41: 819, 65: 2590, 70: 2188, 22: 22, 29: 214, 17: 15, 77: 1638, 82: 875, 89: 273, 94: 161, 97: 46, 101: 33, 24: 23, 79: 1398, 104: 19, 55: 1979, 91: 210, 93: 83, 96: 78, 98: 24, 99: 57, 106: 9, 43: 1033, 31: 240, 95: 71, 103: 15, 107: 4, 100: 17, 26: 57, 20: 1, 14: 2, 21: 8, 16: 1, 23: 6, 18: 2, 102: 7}
======================================================================
pitch_range_by_track | [(0, 0), (14, 153)]
======================================================================
pitch_range_sum | 139
======================================================================
ticks_per_quarter | 500
======================================================================
======================================================================

```
