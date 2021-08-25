# SOTA Relative Global Attention Model

## Trained to 0.027 Floss/0.993 acc for 2 epoch on Google Colab Tesla SXM2 GPU (~16 hours)

## Dataset: Endless Piano Carousel MIDI dataset (not included so download it or make sure to use random/custom priming)

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
