





```
vggish/embedding:0
VGGish(
  (features): Sequential(
    (0): Conv2d(1, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (1): ReLU(inplace=True)
    (2): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
    (3): Conv2d(64, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (4): ReLU(inplace=True)
    (5): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
    (6): Conv2d(128, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (7): ReLU(inplace=True)
    (8): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (9): ReLU(inplace=True)
    (10): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
    (11): Conv2d(256, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (12): ReLU(inplace=True)
    (13): Conv2d(512, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (14): ReLU(inplace=True)
    (15): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
  )
  (embeddings): Sequential(
    (0): Linear(in_features=12288, out_features=4096, bias=True)
    (1): ReLU(inplace=True)
    (2): Linear(in_features=4096, out_features=4096, bias=True)
    (3): ReLU(inplace=True)
    (4): Linear(in_features=4096, out_features=128, bias=True)
    (5): ReLU(inplace=True)
  )
  (classfilter): Sequential(
    (0): Linear(in_features=128, out_features=64, bias=True)
    (1): Sigmoid()
    (2): Linear(in_features=64, out_features=5, bias=True)
    (3): Softmax(dim=1)
  )
)
Epoch 1/100
train Loss: 1.6214 Acc: 0.0000
valid Loss: 1.6206 Acc: 0.0000
Epoch 2/100
train Loss: 1.6201 Acc: 0.0000
valid Loss: 1.6192 Acc: 0.0000
Epoch 3/100
train Loss: 1.6188 Acc: 0.0000
valid Loss: 1.6179 Acc: 0.0000
Epoch 4/100
train Loss: 1.6174 Acc: 0.0000
valid Loss: 1.6166 Acc: 0.0000
Epoch 5/100
train Loss: 1.6161 Acc: 0.0000
valid Loss: 1.6152 Acc: 0.0000
Epoch 6/100
train Loss: 1.6148 Acc: 0.0000
valid Loss: 1.6139 Acc: 0.0000
Epoch 7/100
train Loss: 1.6134 Acc: 0.0000
valid Loss: 1.6126 Acc: 0.0000
Epoch 8/100
train Loss: 1.6121 Acc: 0.0000
valid Loss: 1.6112 Acc: 0.0000
Epoch 9/100
train Loss: 1.6108 Acc: 0.0000
valid Loss: 1.6099 Acc: 0.0000
Epoch 10/100
train Loss: 1.6094 Acc: 0.0000
valid Loss: 1.6085 Acc: 0.0000
Epoch 11/100
train Loss: 1.6081 Acc: 0.0000
valid Loss: 1.6072 Acc: 0.0000
Epoch 12/100
train Loss: 1.6067 Acc: 0.0000
valid Loss: 1.6058 Acc: 0.0000
Epoch 13/100
train Loss: 1.6054 Acc: 0.0000
valid Loss: 1.6044 Acc: 0.0000
Epoch 14/100
train Loss: 1.6040 Acc: 0.0000
valid Loss: 1.6031 Acc: 0.0000
Epoch 15/100
train Loss: 1.6027 Acc: 0.0000
valid Loss: 1.6017 Acc: 0.0000
Epoch 16/100
train Loss: 1.6013 Acc: 0.0000
valid Loss: 1.6004 Acc: 0.0000
Epoch 17/100
train Loss: 1.5999 Acc: 0.0016
valid Loss: 1.5990 Acc: 0.0000
Epoch 18/100
train Loss: 1.5986 Acc: 0.0016
valid Loss: 1.5976 Acc: 0.0000
Epoch 19/100
train Loss: 1.5972 Acc: 0.0048
valid Loss: 1.5962 Acc: 0.0118
Epoch 20/100
train Loss: 1.5958 Acc: 0.0112
valid Loss: 1.5949 Acc: 0.0353
Epoch 21/100
train Loss: 1.5945 Acc: 0.0383
valid Loss: 1.5935 Acc: 0.0647
Epoch 22/100
train Loss: 1.5931 Acc: 0.0702
valid Loss: 1.5921 Acc: 0.1529
Epoch 23/100
train Loss: 1.5917 Acc: 0.1069
valid Loss: 1.5908 Acc: 0.2353
Epoch 24/100
train Loss: 1.5904 Acc: 0.1547
valid Loss: 1.5894 Acc: 0.3176
Epoch 25/100
train Loss: 1.5890 Acc: 0.2472
valid Loss: 1.5880 Acc: 0.3882
Epoch 26/100
train Loss: 1.5876 Acc: 0.3301
valid Loss: 1.5866 Acc: 0.4294
Epoch 27/100
train Loss: 1.5863 Acc: 0.3923
valid Loss: 1.5853 Acc: 0.4471
Epoch 28/100
train Loss: 1.5849 Acc: 0.4450
valid Loss: 1.5839 Acc: 0.4706
Epoch 29/100
train Loss: 1.5835 Acc: 0.4721
valid Loss: 1.5825 Acc: 0.4706
Epoch 30/100
train Loss: 1.5821 Acc: 0.4848
valid Loss: 1.5811 Acc: 0.4706
Epoch 31/100
train Loss: 1.5808 Acc: 0.4960
valid Loss: 1.5798 Acc: 0.4706
Epoch 32/100
train Loss: 1.5794 Acc: 0.5024
valid Loss: 1.5784 Acc: 0.4706
Epoch 33/100
train Loss: 1.5780 Acc: 0.5024
valid Loss: 1.5770 Acc: 0.4706
Epoch 34/100
train Loss: 1.5767 Acc: 0.5024
valid Loss: 1.5757 Acc: 0.4706
Epoch 35/100
train Loss: 1.5753 Acc: 0.5040
valid Loss: 1.5743 Acc: 0.4706
Epoch 36/100
train Loss: 1.5739 Acc: 0.5040
valid Loss: 1.5729 Acc: 0.4706
Epoch 37/100
train Loss: 1.5726 Acc: 0.5040
valid Loss: 1.5716 Acc: 0.4706
Epoch 38/100
train Loss: 1.5712 Acc: 0.5040
valid Loss: 1.5702 Acc: 0.4706
Epoch 39/100
train Loss: 1.5699 Acc: 0.5040
valid Loss: 1.5688 Acc: 0.4706
Epoch 40/100
train Loss: 1.5685 Acc: 0.5040
valid Loss: 1.5675 Acc: 0.4706
Epoch 41/100
train Loss: 1.5671 Acc: 0.5040
valid Loss: 1.5661 Acc: 0.4706
Epoch 42/100
train Loss: 1.5658 Acc: 0.5040
valid Loss: 1.5648 Acc: 0.4706
Epoch 43/100
train Loss: 1.5644 Acc: 0.5040
valid Loss: 1.5634 Acc: 0.4706
Epoch 44/100
train Loss: 1.5631 Acc: 0.5040
valid Loss: 1.5621 Acc: 0.4706
Epoch 45/100
train Loss: 1.5617 Acc: 0.5040
valid Loss: 1.5607 Acc: 0.4706
Epoch 46/100
train Loss: 1.5604 Acc: 0.5040
valid Loss: 1.5594 Acc: 0.4706
Epoch 47/100
train Loss: 1.5591 Acc: 0.5040
valid Loss: 1.5580 Acc: 0.4706
Epoch 48/100
train Loss: 1.5577 Acc: 0.5040
valid Loss: 1.5567 Acc: 0.4706
Epoch 49/100
train Loss: 1.5564 Acc: 0.5040
valid Loss: 1.5553 Acc: 0.4706
Epoch 50/100
train Loss: 1.5551 Acc: 0.5040
valid Loss: 1.5540 Acc: 0.4706
Epoch 51/100
train Loss: 1.5537 Acc: 0.5040
valid Loss: 1.5527 Acc: 0.4706
Epoch 52/100
train Loss: 1.5524 Acc: 0.5040
valid Loss: 1.5514 Acc: 0.4706
Epoch 53/100
train Loss: 1.5511 Acc: 0.5040
valid Loss: 1.5500 Acc: 0.4706
Epoch 54/100
train Loss: 1.5498 Acc: 0.5040
valid Loss: 1.5487 Acc: 0.4706
Epoch 55/100
train Loss: 1.5485 Acc: 0.5040
valid Loss: 1.5474 Acc: 0.4706
Epoch 56/100
train Loss: 1.5472 Acc: 0.5040
valid Loss: 1.5461 Acc: 0.4706
Epoch 57/100
train Loss: 1.5459 Acc: 0.5040
valid Loss: 1.5448 Acc: 0.4706
Epoch 58/100
train Loss: 1.5446 Acc: 0.5040
valid Loss: 1.5435 Acc: 0.4706
Epoch 59/100
train Loss: 1.5433 Acc: 0.5040
valid Loss: 1.5422 Acc: 0.4706
Epoch 60/100
train Loss: 1.5420 Acc: 0.5040
valid Loss: 1.5409 Acc: 0.4706
Epoch 61/100
train Loss: 1.5407 Acc: 0.5040
valid Loss: 1.5397 Acc: 0.4706
Epoch 62/100
train Loss: 1.5394 Acc: 0.5040
valid Loss: 1.5384 Acc: 0.4706
Epoch 63/100
train Loss: 1.5381 Acc: 0.5040
valid Loss: 1.5371 Acc: 0.4706
Epoch 64/100
train Loss: 1.5369 Acc: 0.5040
valid Loss: 1.5358 Acc: 0.4706
Epoch 65/100
train Loss: 1.5356 Acc: 0.5040
valid Loss: 1.5346 Acc: 0.4706
Epoch 66/100
train Loss: 1.5344 Acc: 0.5040
valid Loss: 1.5333 Acc: 0.4706
Epoch 67/100
train Loss: 1.5331 Acc: 0.5040
valid Loss: 1.5321 Acc: 0.4706
Epoch 68/100
train Loss: 1.5319 Acc: 0.5040
valid Loss: 1.5308 Acc: 0.4706
Epoch 69/100
train Loss: 1.5306 Acc: 0.5040
valid Loss: 1.5296 Acc: 0.4706
Epoch 70/100
train Loss: 1.5294 Acc: 0.5040
valid Loss: 1.5284 Acc: 0.4706
Epoch 71/100
train Loss: 1.5282 Acc: 0.5040
valid Loss: 1.5271 Acc: 0.4706
Epoch 72/100
train Loss: 1.5269 Acc: 0.5040
valid Loss: 1.5259 Acc: 0.4706
Epoch 73/100
train Loss: 1.5257 Acc: 0.5040
valid Loss: 1.5247 Acc: 0.4706
Epoch 74/100
train Loss: 1.5245 Acc: 0.5040
valid Loss: 1.5235 Acc: 0.4706
Epoch 75/100
train Loss: 1.5233 Acc: 0.5040
valid Loss: 1.5223 Acc: 0.4706
Epoch 76/100
train Loss: 1.5221 Acc: 0.5040
valid Loss: 1.5211 Acc: 0.4706
Epoch 77/100
train Loss: 1.5209 Acc: 0.5040
valid Loss: 1.5199 Acc: 0.4706
Epoch 78/100
train Loss: 1.5197 Acc: 0.5040
valid Loss: 1.5187 Acc: 0.4706
Epoch 79/100
train Loss: 1.5186 Acc: 0.5040
valid Loss: 1.5175 Acc: 0.4706
Epoch 80/100
train Loss: 1.5174 Acc: 0.5040
valid Loss: 1.5164 Acc: 0.4706
Epoch 81/100
train Loss: 1.5162 Acc: 0.5040
valid Loss: 1.5152 Acc: 0.4706
Epoch 82/100
train Loss: 1.5151 Acc: 0.5040
valid Loss: 1.5140 Acc: 0.4706
Epoch 83/100
train Loss: 1.5139 Acc: 0.5040
valid Loss: 1.5129 Acc: 0.4706
Epoch 84/100
train Loss: 1.5128 Acc: 0.5040
valid Loss: 1.5118 Acc: 0.4706
Epoch 85/100
train Loss: 1.5116 Acc: 0.5040
valid Loss: 1.5106 Acc: 0.4706
Epoch 86/100
train Loss: 1.5105 Acc: 0.5040
valid Loss: 1.5095 Acc: 0.4706
Epoch 87/100
train Loss: 1.5094 Acc: 0.5040
valid Loss: 1.5084 Acc: 0.4706
Epoch 88/100
train Loss: 1.5083 Acc: 0.5040
valid Loss: 1.5073 Acc: 0.4706
Epoch 89/100
train Loss: 1.5072 Acc: 0.5040
valid Loss: 1.5062 Acc: 0.4706
Epoch 90/100
train Loss: 1.5061 Acc: 0.5040
valid Loss: 1.5051 Acc: 0.4706
Epoch 91/100
train Loss: 1.5050 Acc: 0.5040
valid Loss: 1.5040 Acc: 0.4706
Epoch 92/100
train Loss: 1.5039 Acc: 0.5040
valid Loss: 1.5029 Acc: 0.4706
Epoch 93/100
train Loss: 1.5028 Acc: 0.5040
valid Loss: 1.5018 Acc: 0.4706
Epoch 94/100
train Loss: 1.5017 Acc: 0.5040
valid Loss: 1.5007 Acc: 0.4706
Epoch 95/100
train Loss: 1.5007 Acc: 0.5040
valid Loss: 1.4997 Acc: 0.4706
Epoch 96/100
train Loss: 1.4996 Acc: 0.5040
valid Loss: 1.4986 Acc: 0.4706
Epoch 97/100
train Loss: 1.4986 Acc: 0.5040
valid Loss: 1.4975 Acc: 0.4706
Epoch 98/100
train Loss: 1.4975 Acc: 0.5040
valid Loss: 1.4965 Acc: 0.4706
Epoch 99/100
train Loss: 1.4965 Acc: 0.5040
valid Loss: 1.4955 Acc: 0.4706
Epoch 100/100
train Loss: 1.4954 Acc: 0.5040
valid Loss: 1.4944 Acc: 0.4706
```

</div></details>


![img](data:image/png;base64,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)

```
VGGish(
  (features): Sequential(
    (0): Conv2d(1, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (1): ReLU(inplace=True)
    (2): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
    (3): Conv2d(64, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (4): ReLU(inplace=True)
    (5): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
    (6): Conv2d(128, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (7): ReLU(inplace=True)
    (8): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (9): ReLU(inplace=True)
    (10): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
    (11): Conv2d(256, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (12): ReLU(inplace=True)
    (13): Conv2d(512, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (14): ReLU(inplace=True)
    (15): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
  )
  (embeddings): Sequential(
    (0): Linear(in_features=12288, out_features=4096, bias=True)
    (1): ReLU(inplace=True)
    (2): Linear(in_features=4096, out_features=4096, bias=True)
    (3): ReLU(inplace=True)
    (4): Linear(in_features=4096, out_features=128, bias=True)
    (5): ReLU(inplace=True)
  )
  (classfilter): Sequential(
    (0): Linear(in_features=128, out_features=64, bias=True)
    (1): Sigmoid()
    (2): Linear(in_features=64, out_features=5, bias=True)
    (3): Softmax(dim=1)
  )
)
Epoch 1/100
train Loss: 1.4901 Acc: 0.5040
valid Loss: 1.4846 Acc: 0.4706
Epoch 2/100
train Loss: 1.4806 Acc: 0.5040
valid Loss: 1.4754 Acc: 0.4706
Epoch 3/100
train Loss: 1.4717 Acc: 0.5056
valid Loss: 1.4669 Acc: 0.4706
Epoch 4/100
train Loss: 1.4636 Acc: 0.5040
valid Loss: 1.4591 Acc: 0.4706
Epoch 5/100
train Loss: 1.4561 Acc: 0.5040
valid Loss: 1.4519 Acc: 0.4706
Epoch 6/100
train Loss: 1.4492 Acc: 0.5072
valid Loss: 1.4453 Acc: 0.4706
Epoch 7/100
train Loss: 1.4429 Acc: 0.5040
valid Loss: 1.4392 Acc: 0.4706
Epoch 8/100
train Loss: 1.4371 Acc: 0.5088
valid Loss: 1.4336 Acc: 0.4706
Epoch 9/100
train Loss: 1.4317 Acc: 0.5104
valid Loss: 1.4285 Acc: 0.4706
Epoch 10/100
train Loss: 1.4268 Acc: 0.5167
valid Loss: 1.4237 Acc: 0.4706
Epoch 11/100
train Loss: 1.4223 Acc: 0.5167
valid Loss: 1.4193 Acc: 0.4765
Epoch 12/100
train Loss: 1.4181 Acc: 0.5183
valid Loss: 1.4153 Acc: 0.4765
Epoch 13/100
train Loss: 1.4142 Acc: 0.5279
valid Loss: 1.4115 Acc: 0.4765
Epoch 14/100
train Loss: 1.4106 Acc: 0.5295
valid Loss: 1.4080 Acc: 0.4824
Epoch 15/100
train Loss: 1.4073 Acc: 0.5455
valid Loss: 1.4048 Acc: 0.4941
Epoch 16/100
train Loss: 1.4042 Acc: 0.5534
valid Loss: 1.4018 Acc: 0.4941
Epoch 17/100
train Loss: 1.4014 Acc: 0.5534
valid Loss: 1.3990 Acc: 0.5118
Epoch 18/100
train Loss: 1.3987 Acc: 0.5678
valid Loss: 1.3964 Acc: 0.5294
Epoch 19/100
train Loss: 1.3963 Acc: 0.5694
valid Loss: 1.3940 Acc: 0.5471
Epoch 20/100
train Loss: 1.3939 Acc: 0.5710
valid Loss: 1.3917 Acc: 0.5471
Epoch 21/100
train Loss: 1.3917 Acc: 0.5742
valid Loss: 1.3896 Acc: 0.5706
Epoch 22/100
train Loss: 1.3897 Acc: 0.5821
valid Loss: 1.3876 Acc: 0.5941
Epoch 23/100
train Loss: 1.3878 Acc: 0.5837
valid Loss: 1.3857 Acc: 0.6118
Epoch 24/100
train Loss: 1.3860 Acc: 0.5774
valid Loss: 1.3839 Acc: 0.6118
Epoch 25/100
train Loss: 1.3843 Acc: 0.5758
valid Loss: 1.3822 Acc: 0.6176
Epoch 26/100
train Loss: 1.3827 Acc: 0.5821
valid Loss: 1.3806 Acc: 0.6000
Epoch 27/100
train Loss: 1.3812 Acc: 0.5805
valid Loss: 1.3791 Acc: 0.6059
Epoch 28/100
train Loss: 1.3798 Acc: 0.5821
valid Loss: 1.3777 Acc: 0.6235
Epoch 29/100
train Loss: 1.3784 Acc: 0.5726
valid Loss: 1.3763 Acc: 0.6294
Epoch 30/100
train Loss: 1.3771 Acc: 0.5582
valid Loss: 1.3751 Acc: 0.6118
Epoch 31/100
train Loss: 1.3760 Acc: 0.5774
valid Loss: 1.3739 Acc: 0.6412
Epoch 32/100
train Loss: 1.3748 Acc: 0.5646
valid Loss: 1.3727 Acc: 0.6412
Epoch 33/100
train Loss: 1.3737 Acc: 0.5104
valid Loss: 1.3716 Acc: 0.6294
Epoch 34/100
train Loss: 1.3726 Acc: 0.5423
valid Loss: 1.3706 Acc: 0.6294
Epoch 35/100
train Loss: 1.3716 Acc: 0.5343
valid Loss: 1.3696 Acc: 0.6176
Epoch 36/100
train Loss: 1.3706 Acc: 0.5407
valid Loss: 1.3686 Acc: 0.6294
Epoch 37/100
train Loss: 1.3697 Acc: 0.5295
valid Loss: 1.3677 Acc: 0.6353
Epoch 38/100
train Loss: 1.3689 Acc: 0.5279
valid Loss: 1.3668 Acc: 0.6353
Epoch 39/100
train Loss: 1.3680 Acc: 0.5183
valid Loss: 1.3660 Acc: 0.6294
Epoch 40/100
train Loss: 1.3672 Acc: 0.5215
valid Loss: 1.3652 Acc: 0.6471
Epoch 41/100
train Loss: 1.3664 Acc: 0.5152
valid Loss: 1.3644 Acc: 0.6529
Epoch 42/100
train Loss: 1.3657 Acc: 0.5247
valid Loss: 1.3637 Acc: 0.6412
Epoch 43/100
train Loss: 1.3650 Acc: 0.5279
valid Loss: 1.3630 Acc: 0.6412
Epoch 44/100
train Loss: 1.3643 Acc: 0.5183
valid Loss: 1.3623 Acc: 0.6471
Epoch 45/100
train Loss: 1.3636 Acc: 0.5279
valid Loss: 1.3616 Acc: 0.6529
Epoch 46/100
train Loss: 1.3630 Acc: 0.5327
valid Loss: 1.3610 Acc: 0.6529
Epoch 47/100
train Loss: 1.3623 Acc: 0.5470
valid Loss: 1.3604 Acc: 0.6529
Epoch 48/100
train Loss: 1.3617 Acc: 0.5215
valid Loss: 1.3598 Acc: 0.6529
Epoch 49/100
train Loss: 1.3612 Acc: 0.5375
valid Loss: 1.3592 Acc: 0.6588
Epoch 50/100
train Loss: 1.3606 Acc: 0.5199
valid Loss: 1.3587 Acc: 0.6588
Epoch 51/100
train Loss: 1.3601 Acc: 0.5263
valid Loss: 1.3581 Acc: 0.6588
Epoch 52/100
train Loss: 1.3596 Acc: 0.5167
valid Loss: 1.3576 Acc: 0.6647
Epoch 53/100
train Loss: 1.3590 Acc: 0.5375
valid Loss: 1.3571 Acc: 0.6529
Epoch 54/100
train Loss: 1.3585 Acc: 0.5566
valid Loss: 1.3566 Acc: 0.6529
Epoch 55/100
train Loss: 1.3580 Acc: 0.5311
valid Loss: 1.3562 Acc: 0.6529
Epoch 56/100
train Loss: 1.3576 Acc: 0.5136
valid Loss: 1.3557 Acc: 0.6529
Epoch 57/100
train Loss: 1.3571 Acc: 0.5120
valid Loss: 1.3553 Acc: 0.6529
Epoch 58/100
train Loss: 1.3567 Acc: 0.5104
valid Loss: 1.3548 Acc: 0.6529
Epoch 59/100
train Loss: 1.3563 Acc: 0.5136
valid Loss: 1.3544 Acc: 0.6529
Epoch 60/100
train Loss: 1.3558 Acc: 0.5152
valid Loss: 1.3540 Acc: 0.6529
Epoch 61/100
train Loss: 1.3555 Acc: 0.5327
valid Loss: 1.3536 Acc: 0.6471
Epoch 62/100
train Loss: 1.3550 Acc: 0.5167
valid Loss: 1.3532 Acc: 0.6471
Epoch 63/100
train Loss: 1.3547 Acc: 0.5088
valid Loss: 1.3529 Acc: 0.6471
Epoch 64/100
train Loss: 1.3543 Acc: 0.5104
valid Loss: 1.3525 Acc: 0.6471
Epoch 65/100
train Loss: 1.3539 Acc: 0.5183
valid Loss: 1.3521 Acc: 0.6471
Epoch 66/100
train Loss: 1.3535 Acc: 0.5183
valid Loss: 1.3518 Acc: 0.6471
Epoch 67/100
train Loss: 1.3532 Acc: 0.5279
valid Loss: 1.3514 Acc: 0.6471
Epoch 68/100
train Loss: 1.3528 Acc: 0.5231
valid Loss: 1.3511 Acc: 0.6471
Epoch 69/100
train Loss: 1.3525 Acc: 0.5311
valid Loss: 1.3508 Acc: 0.6471
Epoch 70/100
train Loss: 1.3522 Acc: 0.5199
valid Loss: 1.3505 Acc: 0.6471
Epoch 71/100
train Loss: 1.3518 Acc: 0.5183
valid Loss: 1.3502 Acc: 0.6529
Epoch 72/100
train Loss: 1.3515 Acc: 0.5279
valid Loss: 1.3499 Acc: 0.6529
Epoch 73/100
train Loss: 1.3512 Acc: 0.5375
valid Loss: 1.3496 Acc: 0.6471
Epoch 74/100
train Loss: 1.3509 Acc: 0.5534
valid Loss: 1.3493 Acc: 0.6471
Epoch 75/100
train Loss: 1.3506 Acc: 0.5279
valid Loss: 1.3490 Acc: 0.6471
Epoch 76/100
train Loss: 1.3503 Acc: 0.5279
valid Loss: 1.3487 Acc: 0.6471
Epoch 77/100
train Loss: 1.3500 Acc: 0.5391
valid Loss: 1.3484 Acc: 0.6471
Epoch 78/100
train Loss: 1.3497 Acc: 0.5247
valid Loss: 1.3482 Acc: 0.6588
Epoch 79/100
train Loss: 1.3495 Acc: 0.5295
valid Loss: 1.3479 Acc: 0.6588
Epoch 80/100
train Loss: 1.3492 Acc: 0.5391
valid Loss: 1.3476 Acc: 0.6529
Epoch 81/100
train Loss: 1.3489 Acc: 0.5614
valid Loss: 1.3474 Acc: 0.6529
Epoch 82/100
train Loss: 1.3486 Acc: 0.5502
valid Loss: 1.3471 Acc: 0.6529
Epoch 83/100
train Loss: 1.3484 Acc: 0.5391
valid Loss: 1.3469 Acc: 0.6588
Epoch 84/100
train Loss: 1.3481 Acc: 0.5582
valid Loss: 1.3466 Acc: 0.6529
Epoch 85/100
train Loss: 1.3479 Acc: 0.5949
valid Loss: 1.3464 Acc: 0.6529
Epoch 86/100
train Loss: 1.3476 Acc: 0.5566
valid Loss: 1.3461 Acc: 0.6529
Epoch 87/100
train Loss: 1.3474 Acc: 0.5279
valid Loss: 1.3459 Acc: 0.6529
Epoch 88/100
train Loss: 1.3471 Acc: 0.5295
valid Loss: 1.3457 Acc: 0.6529
Epoch 89/100
train Loss: 1.3469 Acc: 0.5455
valid Loss: 1.3454 Acc: 0.6529
Epoch 90/100
train Loss: 1.3467 Acc: 0.5375
valid Loss: 1.3452 Acc: 0.6529
Epoch 91/100
train Loss: 1.3464 Acc: 0.5630
valid Loss: 1.3450 Acc: 0.6529
Epoch 92/100
train Loss: 1.3462 Acc: 0.5423
valid Loss: 1.3448 Acc: 0.6529
Epoch 93/100
train Loss: 1.3460 Acc: 0.5263
valid Loss: 1.3446 Acc: 0.6588
Epoch 94/100
train Loss: 1.3457 Acc: 0.5614
valid Loss: 1.3444 Acc: 0.6588
Epoch 95/100
train Loss: 1.3455 Acc: 0.5646
valid Loss: 1.3442 Acc: 0.6588
Epoch 96/100
train Loss: 1.3453 Acc: 0.5805
valid Loss: 1.3440 Acc: 0.6588
Epoch 97/100
train Loss: 1.3451 Acc: 0.5407
valid Loss: 1.3438 Acc: 0.6588
Epoch 98/100
train Loss: 1.3449 Acc: 0.5869
valid Loss: 1.3435 Acc: 0.6588
Epoch 99/100
train Loss: 1.3447 Acc: 0.5343
valid Loss: 1.3434 Acc: 0.6647
Epoch 100/100
train Loss: 1.3444 Acc: 0.5534
valid Loss: 1.3432 Acc: 0.6647
```

![img](data:image/png;base64,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)

```
VGGish(
  (features): Sequential(
    (0): Conv2d(1, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (1): ReLU(inplace=True)
    (2): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
    (3): Conv2d(64, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (4): ReLU(inplace=True)
    (5): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
    (6): Conv2d(128, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (7): ReLU(inplace=True)
    (8): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (9): ReLU(inplace=True)
    (10): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
    (11): Conv2d(256, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (12): ReLU(inplace=True)
    (13): Conv2d(512, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (14): ReLU(inplace=True)
    (15): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
  )
  (embeddings): Sequential(
    (0): Linear(in_features=12288, out_features=4096, bias=True)
    (1): ReLU(inplace=True)
    (2): Linear(in_features=4096, out_features=4096, bias=True)
    (3): ReLU(inplace=True)
    (4): Linear(in_features=4096, out_features=128, bias=True)
    (5): ReLU(inplace=True)
  )
  (classfilter): Sequential(
    (0): Linear(in_features=128, out_features=64, bias=True)
    (1): Sigmoid()
    (2): Linear(in_features=64, out_features=5, bias=True)
    (3): Softmax(dim=1)
  )
)
Epoch 1/100
train Loss: 1.3442 Acc: 0.6172
valid Loss: 1.3409 Acc: 0.6118
Epoch 2/100
train Loss: 1.3424 Acc: 0.5550
valid Loss: 1.3394 Acc: 0.6412
Epoch 3/100
train Loss: 1.3404 Acc: 0.6810
valid Loss: 1.3373 Acc: 0.5824
Epoch 4/100
train Loss: 1.3387 Acc: 0.5869
valid Loss: 1.3360 Acc: 0.6176
Epoch 5/100
train Loss: 1.3372 Acc: 0.5534
valid Loss: 1.3350 Acc: 0.6588
Epoch 6/100
train Loss: 1.3356 Acc: 0.6571
valid Loss: 1.3336 Acc: 0.6588
Epoch 7/100
train Loss: 1.3340 Acc: 0.6587
valid Loss: 1.3318 Acc: 0.6235
Epoch 8/100
train Loss: 1.3329 Acc: 0.6316
valid Loss: 1.3310 Acc: 0.6941
Epoch 9/100
train Loss: 1.3312 Acc: 0.5758
valid Loss: 1.3304 Acc: 0.7235
Epoch 10/100
train Loss: 1.3298 Acc: 0.7257
valid Loss: 1.3292 Acc: 0.7353
Epoch 11/100
train Loss: 1.3282 Acc: 0.6938
valid Loss: 1.3278 Acc: 0.7412
Epoch 12/100
train Loss: 1.3251 Acc: 0.6332
valid Loss: 1.3248 Acc: 0.6235
Epoch 13/100
train Loss: 1.3248 Acc: 0.6986
valid Loss: 1.3237 Acc: 0.6588
Epoch 14/100
train Loss: 1.3234 Acc: 0.5949
valid Loss: 1.3237 Acc: 0.7529
Epoch 15/100
train Loss: 1.3216 Acc: 0.7911
valid Loss: 1.3221 Acc: 0.7353
Epoch 16/100
train Loss: 1.3195 Acc: 0.7576
valid Loss: 1.3196 Acc: 0.6647
Epoch 17/100
train Loss: 1.3181 Acc: 0.7624
valid Loss: 1.3183 Acc: 0.6824
Epoch 18/100
train Loss: 1.3162 Acc: 0.7608
valid Loss: 1.3165 Acc: 0.6706
Epoch 19/100
train Loss: 1.3143 Acc: 0.7831
valid Loss: 1.3149 Acc: 0.6529
Epoch 20/100
train Loss: 1.3123 Acc: 0.7990
valid Loss: 1.3136 Acc: 0.7118
Epoch 21/100
train Loss: 1.3103 Acc: 0.7927
valid Loss: 1.3127 Acc: 0.7882
Epoch 22/100
train Loss: 1.3087 Acc: 0.8086
valid Loss: 1.3100 Acc: 0.7412
Epoch 23/100
train Loss: 1.3059 Acc: 0.7831
valid Loss: 1.3084 Acc: 0.7471
Epoch 24/100
train Loss: 1.3037 Acc: 0.7943
valid Loss: 1.3063 Acc: 0.7471
Epoch 25/100
train Loss: 1.3014 Acc: 0.8086
valid Loss: 1.3037 Acc: 0.7176
Epoch 26/100
train Loss: 1.2990 Acc: 0.8293
valid Loss: 1.3016 Acc: 0.7176
Epoch 27/100
train Loss: 1.2963 Acc: 0.8325
valid Loss: 1.2995 Acc: 0.7294
Epoch 28/100
train Loss: 1.2938 Acc: 0.8150
valid Loss: 1.2977 Acc: 0.7412
Epoch 29/100
train Loss: 1.2911 Acc: 0.8357
valid Loss: 1.2953 Acc: 0.7529
Epoch 30/100
train Loss: 1.2881 Acc: 0.8309
valid Loss: 1.2940 Acc: 0.7941
Epoch 31/100
train Loss: 1.2852 Acc: 0.8357
valid Loss: 1.2914 Acc: 0.7941
Epoch 32/100
train Loss: 1.2821 Acc: 0.8341
valid Loss: 1.2883 Acc: 0.7824
Epoch 33/100
train Loss: 1.2791 Acc: 0.8293
valid Loss: 1.2851 Acc: 0.7529
Epoch 34/100
train Loss: 1.2758 Acc: 0.8182
valid Loss: 1.2836 Acc: 0.8000
Epoch 35/100
train Loss: 1.2725 Acc: 0.8246
valid Loss: 1.2802 Acc: 0.7882
Epoch 36/100
train Loss: 1.2691 Acc: 0.8341
valid Loss: 1.2773 Acc: 0.7824
Epoch 37/100
train Loss: 1.2660 Acc: 0.8325
valid Loss: 1.2748 Acc: 0.8000
Epoch 38/100
train Loss: 1.2624 Acc: 0.8405
valid Loss: 1.2727 Acc: 0.8000
Epoch 39/100
train Loss: 1.2592 Acc: 0.8405
valid Loss: 1.2691 Acc: 0.8000
Epoch 40/100
train Loss: 1.2553 Acc: 0.8373
valid Loss: 1.2663 Acc: 0.8000
Epoch 41/100
train Loss: 1.2515 Acc: 0.8309
valid Loss: 1.2629 Acc: 0.8059
Epoch 42/100
train Loss: 1.2477 Acc: 0.8357
valid Loss: 1.2588 Acc: 0.7471
Epoch 43/100
train Loss: 1.2440 Acc: 0.8405
valid Loss: 1.2569 Acc: 0.8000
Epoch 44/100
train Loss: 1.2400 Acc: 0.8373
valid Loss: 1.2529 Acc: 0.7882
Epoch 45/100
train Loss: 1.2365 Acc: 0.8373
valid Loss: 1.2497 Acc: 0.7882
Epoch 46/100
train Loss: 1.2328 Acc: 0.8389
valid Loss: 1.2467 Acc: 0.7882
Epoch 47/100
train Loss: 1.2284 Acc: 0.8453
valid Loss: 1.2432 Acc: 0.7882
Epoch 48/100
train Loss: 1.2249 Acc: 0.8421
valid Loss: 1.2409 Acc: 0.8059
Epoch 49/100
train Loss: 1.2209 Acc: 0.8501
valid Loss: 1.2383 Acc: 0.8059
Epoch 50/100
train Loss: 1.2171 Acc: 0.8421
valid Loss: 1.2350 Acc: 0.8000
Epoch 51/100
train Loss: 1.2124 Acc: 0.8437
valid Loss: 1.2302 Acc: 0.7529
Epoch 52/100
train Loss: 1.2093 Acc: 0.8437
valid Loss: 1.2280 Acc: 0.8000
Epoch 53/100
train Loss: 1.2056 Acc: 0.8469
valid Loss: 1.2247 Acc: 0.7941
Epoch 54/100
train Loss: 1.2018 Acc: 0.8469
valid Loss: 1.2216 Acc: 0.7882
Epoch 55/100
train Loss: 1.1979 Acc: 0.8421
valid Loss: 1.2195 Acc: 0.8059
Epoch 56/100
train Loss: 1.1945 Acc: 0.8517
valid Loss: 1.2160 Acc: 0.8000
Epoch 57/100
train Loss: 1.1907 Acc: 0.8501
valid Loss: 1.2128 Acc: 0.7941
Epoch 58/100
train Loss: 1.1871 Acc: 0.8485
valid Loss: 1.2106 Acc: 0.7941
Epoch 59/100
train Loss: 1.1834 Acc: 0.8469
valid Loss: 1.2078 Acc: 0.7941
Epoch 60/100
train Loss: 1.1801 Acc: 0.8565
valid Loss: 1.2056 Acc: 0.8118
Epoch 61/100
train Loss: 1.1767 Acc: 0.8469
valid Loss: 1.2021 Acc: 0.7941
Epoch 62/100
train Loss: 1.1733 Acc: 0.8469
valid Loss: 1.1991 Acc: 0.7882
Epoch 63/100
train Loss: 1.1700 Acc: 0.8501
valid Loss: 1.1970 Acc: 0.7941
Epoch 64/100
train Loss: 1.1668 Acc: 0.8533
valid Loss: 1.1945 Acc: 0.7941
Epoch 65/100
train Loss: 1.1636 Acc: 0.8501
valid Loss: 1.1921 Acc: 0.7941
Epoch 66/100
train Loss: 1.1605 Acc: 0.8517
valid Loss: 1.1894 Acc: 0.7882
Epoch 67/100
train Loss: 1.1575 Acc: 0.8612
valid Loss: 1.1871 Acc: 0.7882
Epoch 68/100
train Loss: 1.1545 Acc: 0.8549
valid Loss: 1.1849 Acc: 0.7882
Epoch 69/100
train Loss: 1.1516 Acc: 0.8533
valid Loss: 1.1822 Acc: 0.7824
Epoch 70/100
train Loss: 1.1492 Acc: 0.8581
valid Loss: 1.1802 Acc: 0.7824
Epoch 71/100
train Loss: 1.1460 Acc: 0.8565
valid Loss: 1.1784 Acc: 0.7882
Epoch 72/100
train Loss: 1.1434 Acc: 0.8596
valid Loss: 1.1766 Acc: 0.7941
Epoch 73/100
train Loss: 1.1410 Acc: 0.8565
valid Loss: 1.1745 Acc: 0.7882
Epoch 74/100
train Loss: 1.1383 Acc: 0.8596
valid Loss: 1.1730 Acc: 0.8000
Epoch 75/100
train Loss: 1.1359 Acc: 0.8660
valid Loss: 1.1712 Acc: 0.8000
Epoch 76/100
train Loss: 1.1336 Acc: 0.8581
valid Loss: 1.1685 Acc: 0.7882
Epoch 77/100
train Loss: 1.1312 Acc: 0.8612
valid Loss: 1.1668 Acc: 0.7882
Epoch 78/100
train Loss: 1.1290 Acc: 0.8628
valid Loss: 1.1652 Acc: 0.7882
Epoch 79/100
train Loss: 1.1266 Acc: 0.8628
valid Loss: 1.1636 Acc: 0.7824
Epoch 80/100
train Loss: 1.1245 Acc: 0.8660
valid Loss: 1.1621 Acc: 0.7824
Epoch 81/100
train Loss: 1.1224 Acc: 0.8644
valid Loss: 1.1604 Acc: 0.7882
Epoch 82/100
train Loss: 1.1202 Acc: 0.8612
valid Loss: 1.1588 Acc: 0.7882
Epoch 83/100
train Loss: 1.1184 Acc: 0.8660
valid Loss: 1.1573 Acc: 0.7882
Epoch 84/100
train Loss: 1.1164 Acc: 0.8676
valid Loss: 1.1559 Acc: 0.7882
Epoch 85/100
train Loss: 1.1146 Acc: 0.8644
valid Loss: 1.1545 Acc: 0.7882
Epoch 86/100
train Loss: 1.1128 Acc: 0.8660
valid Loss: 1.1532 Acc: 0.7882
Epoch 87/100
train Loss: 1.1108 Acc: 0.8644
valid Loss: 1.1519 Acc: 0.7882
Epoch 88/100
train Loss: 1.1091 Acc: 0.8644
valid Loss: 1.1506 Acc: 0.7882
Epoch 89/100
train Loss: 1.1075 Acc: 0.8660
valid Loss: 1.1493 Acc: 0.7882
Epoch 90/100
train Loss: 1.1057 Acc: 0.8676
valid Loss: 1.1481 Acc: 0.7882
Epoch 91/100
train Loss: 1.1041 Acc: 0.8676
valid Loss: 1.1470 Acc: 0.7882
Epoch 92/100
train Loss: 1.1025 Acc: 0.8676
valid Loss: 1.1458 Acc: 0.7882
Epoch 93/100
train Loss: 1.1011 Acc: 0.8692
valid Loss: 1.1448 Acc: 0.7882
Epoch 94/100
train Loss: 1.0994 Acc: 0.8724
valid Loss: 1.1437 Acc: 0.7882
Epoch 95/100
train Loss: 1.0980 Acc: 0.8692
valid Loss: 1.1426 Acc: 0.7882
Epoch 96/100
train Loss: 1.0966 Acc: 0.8676
valid Loss: 1.1417 Acc: 0.7882
Epoch 97/100
train Loss: 1.0953 Acc: 0.8660
valid Loss: 1.1407 Acc: 0.7882
Epoch 98/100
train Loss: 1.0938 Acc: 0.8708
valid Loss: 1.1397 Acc: 0.7882
Epoch 99/100
train Loss: 1.0925 Acc: 0.8724
valid Loss: 1.1388 Acc: 0.7882
Epoch 100/100
train Loss: 1.0912 Acc: 0.8756
valid Loss: 1.1378 Acc: 0.7882
```

![img](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAYUAAAFTCAYAAADWRBB6AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8QVMy6AAAACXBIWXMAAAsTAAALEwEAmpwYAABxAUlEQVR4nO2dZ5gUVdaA3zORycCQM0gGEQUVlVUQA6AY0FXMusG8pjVg2sX4ue66a15EZQ2rawYTghgQs4ICkkFynGFIk5h4vh+3uqe6p7une/L03Pd5+pmpqhuruu+pc86954qqYrFYLBYLQExDN8BisVgsjQcrFCwWi8XixQoFi8VisXixQsFisVgsXqxQsFgsFosXKxQsFovF4sUKBUujQUT6icjPIpIrIuUicrdzfpSIbGno9tU1IpInIr3CSNdDRFRE4lznrhCRR+u0gZZmgRUKlsbErcA8VU1T1RhVvS+cTCIyUkS+EZF9IrJbRL4WkcPruK01QkTmicgf3OdUNVVV11WjrATgLuDvtdU+S/PFCgVLY6I7sCySDCKSDnwAPAG0BjoD9wBFtd66xsvpwEpV3drQDbE0faxQsDQKROQzYDTwpGNGeVVE7g8ja18AVf2fqpapaqGqfqyqS1xl/05EVojIHhGZIyLdXddOFJGVjpbxpIh84XmDF5EpIvJfV1ofs42IZIjI8yKyXUS2isj9IhLrXLtURL4SkX849a4XkXHOtQeA37j6+qRzXkWkt/P/KY4pbb+IbBaRKSHuwTjgizDulcVSJVYoWBoFqno88CVwraqmAsXB0orI0yLytHO4GigTkRdFZJyItPJLewZwBzARaOvU8T/nWhvgbYzppQ3wK3BMBM1+ESgFegOHAicBbpPQkcAqp+yHgedFRFT1TndfVfXaAGXnAxcDLYFTgKucvgTiYKcei6XGWKFgaXKo6tWqerXz/35gJKDAs0C2iLwnIu2d5FcA/6eqK1S1FHgQGOpoC+OB5ar6lqqWAI8CO8Jpg1P+OOAGVc1X1SzgX8AkV7KNqvqsqpZhBEhHoH3l0gL2cZ6q/qKq5Y7W8z/guCDJWwK54ZRrsVSFFQqWJo8z4F+qql2AwUAnzAAPxk/xmIjsFZG9wG5AML6HTsBmVznqPq6C7kA8sN1V9jNAO1car4BR1QLn39RwCheRI0XkcxHJFpF9wJUYjSMQe4C0MNttsYTECgVLVKGqK4EXMMIBzCB/haq2dH2SVPUbYDvQ1ZNXRMR9jDHhJLuOO7j+34xxZrdxlZuuqoPCbWoV118F3gO6qmoGMBUjzAKxBMe3YrHUFCsULE0aEekvIn8WkS7OcVfgPOA7J8lU4HYRGeRczxCR3zrXPgQGichEx3l8Hb4D/yLgWBHpJiIZwO2eC6q6HfgYeERE0kUkRkQOEpFgJh5/dgKh1iSkAbtV9YCIHAGcHyLtLIKbliyWiLBCwdLkEJGpIjLVOczFOHS/F5F8jDBYCvwZQFVnAH8DXhOR/c61cc61XcBvgYeAHKAP8LWnHlWdC7yOeRNfiJn66uZiIAFYjjHhvIXxG4TDY8DZzsykxwNcvxq4V0Rygb8Ab4Qo632gv4h0CrNuiyUoYjfZsVgqEJF5wH9V9bmGbkskiMjlwEBVvaGh22Jp2sRVncRisTR2VHVaQ7fBEh1Y85HFYrFYvFjzkcVisVi8WE3BYrFYLF6sULBYLBaLl0YnFJywx4eGmfYHz/zzWqj3IxG5pDbKqmb9/yciNzj//0ZEahzLRkSuEpGdTtC1zBo30tKgiMiZTnC8vHB/I5bKSBX7czhTnu+uzzbVNSLyjoiMDSuxqjaaDzABmO137kZMuIB9wHQg0XXtHODtCMq/FPiqofsZoF1tga1AUi2WGQ8UAofUQlk9MCtw4xr6XoVoYwJmncAGp62j/K7fglmjkAusB27xuz4UE6RuH7AF+Es9tXsDcEKYaX8FTq+lehXo3dDPrYo2xgL3A9uc5/Yz0DJAus8i+X4Co4AtjaB/dwB5zucAUOY6XlbLdR0BLAwnbWPTFK4EXvYciMjJwGRgDGZg6oWJle/hPWC0iIS7YKhRIRU7Z10KzFLVwlosvj3Qggj3J6gLxFAf37WvgAsJHNROMIvNWgFjgWtFxB287lVgPmZPhuMwUUlPq9vmRkzE+03UFZ4Q4XXMPcDRwFFAOnARZvB0t+MCmujUelV9UE2U3FTM2Pet51hd4VJq4/ejqj8A6SIyPJzEjeKDedMrBLq4zr0KPOg6HgPs8Ms3F7gkzDouJYimAMwD/uBOB/wDs1J1PTDOlTYDeB4TO2cr5m0m1rl2EObNJQfYBbyC6+0G82Z4G2aVbBHmC/0ZcKErzShcbzJOnpudPPswq2xbhOhnX0zcHsW8dXzmnO/v3K/dmFDL57jynIJ5E9uPieszxXVtk6usPMyPdApmkZcnTQ9cb2vO/XwAs0K4EBNeOlT94zErg3Ode3pzDb5LW/DTFAKkeRx4wnVcgFn85Tl+E7g9zPo6YV5QdgNrgT+6rr0A3B/o2WJegMqd+5MH3Bqk/ETnujrP9VdXvW8D2Zjv6HWuPEcA3wJ7Md/TJ4EE59p8V1l5wLkE+G3g0iacfvwbE1IjHzghjPoXON+nncA/I3yGrZy2HRQiTQYmdPoIqqEpYN7Ud2F+XxcEemZOOz5w+rjH+d89Rl0KrKNCA70gkn76lfOV63gelX8/G3BplVT+DY4AvnGe+WIqa8vPAn+tsi3V/eHV9gcYBOT7nVsMnOs6buM8/EzXucfdXzjnhowM58b7XZuHr1AoAf6IUWGvwqiwnim8MzERMVMwUTF/wARdw3l4J2J+yG0xP8BHXfVswMTU6YpjLnK+cIf7f2n98vyA+RG2BlYAV1ZxP3vgO0inYAb7yzCC6DDMD2KQq86DMX6mIZgf8hmBygryhfSvbx5GmAxy6suoov7twG9cP8TDnP+7Oc802Of8AH0PKRQwWsPP7nuICan9EMbs1s8p4/BQ99iV9wvgaYxmNtR5nmOcay8QRCi4nm245iP3IB2DCb3xF8wLVS/M4HSyc30YZpCIc57NCkyY70plBfttUFko7MPsNxGDCRQYqv5vgYuc/1OBEX6/0WCfyU6aY53j2zCa32rgGr/2PYUxL/cgcqFQCvwT8zs9DiPo+vk/MyATOMvpbxrmZWGm6ze135WvIxXf55FV9HOkX5t87j+Vfz/xhBAKmKi/OZiXqxjMGJQDtHWlvwl4p6r705jUrpZUjgmfivkievD8n4bpME4er/lIVVvWUns2quqzACLyIuZH315EFBM7p6Uac0++iPwLuBx4RlXXYt4WwcT2/yfwV7+yH1dVd4jmllQdD/9xVd3mtOd9zOATCacCG1T1P87xTyLyNnA2xn45z5V2iYh44vfPjLAeNy+o6jKnzWND1Y8RwgNFZLGq7sG8laGqmzD3pzaZgvnh/Md17gPgJYxGFgvcq6o/VlWQE4BvJHCqqh4AFonIcxhTx6e13G43h2N+8Pc6x+tE5FnMfg5zVHWhK+0GEXkG8zwfrUGd76rq1wAicnCo+jHPs7eItFETY8oToDDc32gXzItEX6AnJi7VpyKyWlXnOmaQY4DrnbTV4W5VLQK+EJEPMT5Kn33BVTUHow0B3l3zPnclKQcGi8gmNUEStzv5vqLm31vv78epO1TaCzEm6FnO8VwRWYAREi8653LDaVNj8insoXJM+DyMLdGD53/3AJqGkby1TbBY+N0JEUdfRNqJyGtitmfcD/yXynHw/WP2B+p70PZgTB1hxeV30R040tNmp90X4EQFjTB+f7i4+xmyfszb2Hhgo5gtMY+qYd0BEZFrMb6FU5wBARFpDcwG7sW87XcFThaRq8MoshMmmqn7O7kR8+ZWl3QHOvndzztwNvERkb4i8oGI7HC+hw9S+88zaP3A7zED+koR+VFETo2wLo9/7V41W6wuAV4Dxjv29aeB69VsnFQd9qhqvut4I+ZZ+iAiySLyjIhsdO7jfKCliMQ6+c/F/Fa2i8iHItK/mu0JRLh7e4B5Hr/1ex4j8Q3QGNZY2ZiEwhqMT8X9Y1oGHOI6PgTY6UhvDwMwZqb6oqo4+v+HUWWHqGo6RoL7i3j1O66PePibgS/Ud1+BVFW9yrkeKn6/f3sh9F4DHtz5Qtavqj+q6ukY4ToTJyqomLDVeSE+F4R7A0TkdzgTF1TVPSWxF1Cmqi+paqlz7TWMkKqKbUBrEXEL9W4YvwhUfZ8C3dtw2Ays97ufaarqafO/gZVAH+d7eAfB92Oo1E4RCed5Bq1fVdeo6nmY5/k34C0RSXHKDvU873DKXxKgTg/pwHDgdRHZAXg0ui0i8psQfXTTytMeh26YZ+nPnzHmxCOd+3isc16cfs5R1RMxg+9KjN3eM608VD/Daad/36va3+Nlv+eRoqoPudKENVY2GqGgZjvET/CNC/8S8HsRGShm7927MPY+AEQkEWM7nRtBVSIiLdyfCNtZVRz9NIyGs9cRcLeEUWx9xMP/AOgrIheJSLzzOVxEBjjXQ8Xvz8aoye74/4sIstdApPWLSIKIXCAiGc73YD9meh6qukkrZmQE+rziqUBEEl3PM8F5vuJcuwDztnyiqq7za9tqk0TOd55nB8wb4GInbw8RURHp4d8pxwz4DfB/Tn1DMG/JnnYtwrzdtnbKvcGviKr2VQjGD8B+EblNRJJEJFZEBovI4c71NMx9zHPeXq/yy+9f72LM3hJDnXs4pSb1i8iFItJWVcupeDv1PNNQz/NBJ82vmCnCdzrPdQDmmXyAMSN3wphQh1IhvIcB3zv1vyAiL1TRh3uc795vMObVNwOkScNoLXvFaJReU7CItBeR0xzhUoT53Xv6+GUV/fyyirYFYhEwyfntDMeYXj38F5ggIic7z6KFmPUYbtPaccBHVVXSaISCwzMYWywAqjobs+H55xj1biO+9vnTgHkeWzt430JCSeGjMQ/Z+5GKqaHhEiqO/j0YJ+o+zCYu74RR3kuYgSMpwnaEjWPeOAlj892GMUf9DeNogxDx+x3z2QPA145qOkKr3msg0vovwti+92PU8Qur0c1VmGfaGWPXLsSo1WBmiGUCP7re1qY6bdsPTMQ4LfdgfnxLnT6DMSdtpOLt35/zMM7ObcAMzAwPz4vKy5gBdwPmZeJ1v7z/B9zl3Nebw+2omn2fJ2AGxfUYp/1zGDs8GN/I+RhT67MB6p0CvOjUe46qrsaYzz7BaO1f1bD+scAyEcnD7B0xyfG5RMJ5mOeXg/kt3a2qn6phh+eDeWkBY0Uodv7vimtvjADswDzrbRgBfqWaXfv8eRRIcvr3HcbM6CEGo0lsw8w8Ow7zO6or7sbMbtyDGWde9VxwXk5Ox2iE2RjN4RanjTjCOl/N1NSQNLqAeCLyFfAnVf05jLTfA79X1aV137K6RUQeBLJU9dGGbovFFxG5C8hW1Wcaui2WqhGRBIwgHuJons0eMZM6nnc5ooOnbWxCwWKxWCwNR2MzH1kiQETuCOLEqtJuaGl8OH6VQM+zUaxitjQPrKZgsVgsFi9WU7A0eqSBIuc65S0TkVG1VV5t1CsBonyKb5TdISLyTZ030hKVWKFgadSIyAQg1zPxwJn2OEdEdolZXe7PPzCzaMItP0FEHhGRLY6pZr2YFeoAqOog9V3tXS9EUq+ItMXMiHvGybsEM4VyQt210BKtWKFgaez4RM7FhE94A7MWIBCRRs69HbMQ6gjMnPTRmLhITYlLqRxl9xXgioZpjqUpY4WCpdHiTC08HhNwDgBVXaWqzxMkhLQzF34hZk1EOBwOzFDVbc789w2q+pKrDRtE5ATn/yQReVFE9ojIChG51W3GcdLeIiJLRCRfRJ53Fjh9JCK5IvKJmEWYnvSnOWaivSIyTyoWEgaq9wWn3uVOm92Mc98jh3nAGDELPC2WsLFCwdKY6QOU+4WkCIcVuMKjOIPuyCBpvwNuEpGrReRgkZBRx/5Kxb4eJxJ4gd1ZzrW+mMVdH2EWFLXB/N6uc9rUF/gfZoVzW8yq9vcdQRio3oOcz8nAJX7XD8Ys3POiqlsxWlW/EP2xWCphhYKlMdOSqqPHBsInGqQTBybYCt3/w6ysvgAT/3+rBN+W9RzM/h57HEH1eIA0T6jqTmdQ/hL4XlV/VhN8bwbgcZifC3yoqnOdBVb/wKycPTpIvQ+o6m5n5ap/vS0JfJ/CioppsbixQsHSmAknemwgwo6cq6plqvqUqh6DGUAfAKa7TTkuOuEbuTJQFMudrv8LAxx7ott2woTO8LSj3CkvUHRV/3o3+l0Pdp/qKoKwJYqxQsHSmAkUOTccqhU5V02I5qcwg+zAAEm24xu7v2ukdbjYRkVcJhyzVVcCx1fa7ldXN7/rlaLsikgnTHyuVVgsEWCFgqXREihyrhhaYAY8nGiQia7rEUXOFZEbnHn/SSIS55iO0gg8A+kN4HYRaeUIqmur2zenrFNEZIyIxGMCqxVhIq6GqrcL8Ce/64Gi7I7CbMNaVIM2WpohVihYGjs+kXMxb9eFVMw+KsT3bTjSyLmFwCOYqJm7gGuAswKE1waz/mELJiroJ5jouNUadFV1FcZR/YRT7wRggivKp5t7MCaj9ZhIqy/7XQ8UZfcCzJ4YFktE2DAXlkZPY42cKyJXYUJC1/VeGOG0xRtlV8xWmdNUtU52r7NEN1YoWCxh4iyI64XZlL4PJsb/kzbcuSWaiHRzGYulOZOAMWf1xMzqeQ2zV7DFEjVYTcFisVgsXqyj2WKxWCxerFCwWCwWi5cmJxQaKra+E9QsWPiDOscvXv5vRKTGi5JE5CoR2elM2cyscSMtdYoTXG++E1zvkYZuT2NGRKaIyH9DXG+QfTLqChFJFJGVItKupmU1KaEQILb+JSKyUET2O/HwHxYRt/M80tj6lzrTHyuhquNU9cUadaCaBIiX/6Wq1ijQmbNg6p/ASaqaqqo5NSirh4io371vdIhIsog8LWYvhn0iMj9AmgTnxxVpEL7qtink4OXH5Zg1Demq+uca1vuCiNxfkzLqGqeNxeK7NWlsbZRdX/tkOC+TnraX+PWn1taROIsUpwO31bSsJiUUqBxbPxkTZbINcCQwBrjZdT3S2PqNCtcgeymV4+XXlPZAC4KEoK5PnFXK9fFdnAa0xoTBaA3cGCDNLUBWPbSlOnQHlmsjmB1Sjy8ADzsvLZ5PWT3VWys4L5OpqpqK2ePC3Z8rPelq6X6+ClxS43DpqtokPpjpgIVAlxBpbgLe9zs3F7gkzDouBb4Kcm0e8Ad3Oowmsgez0nScK20G8DwmZs1W4H4g1rl2EPAZkIN563sFaOnKuwEj7ZdgVsvGOekvdKUZBWzxy3Ozk2cf8DrQIkQ/+wL5gAJ5mHAIAP2d+7Ubs0r4HFeeUzChH/ZjgrNNcV3b5CorDzgKmAL815Wmh5MmznU/HwC+dp5r7yrqHw8sx0T+3ArcHOH3p5/T9vQQaXpiwm6Pc9/fMMqOAe7CrDrOwqwwzgj0rFzP6wRgLFCMCXGdBywOUccLTrpiJ+0JTr2TgV+d79MbQGtXnjcxK7X3AfOBQc75y/3Ket85r0Bvvzrvd/cD893cgXk5C1o/5oXjv875vcCPQPsIn5m3/mqMF1MwK85fd74zPwGH+D8D5/8jMGtP9mJ+s08CCc41Af7lPNd9mN/Y4Gq2yac/zv2+BhPjaz1+vxH/ccc5/p3zHd0DzAG6+9WxBjiuOu3zfJqSphBObP1jqfzmG0ls/Ug4EjNwtQEeBp53xeJ/ESjFDHSHYjZ8+YOnCZhwzZ0wb6xdMV9gN+dhBuGWqlpKgHj5ATgHM8j0BIZgBFdAVHU14PG1tFTV40UkBTMgvwq0c9rwtMsnk48xYbV02naViJzhXDvWVVaqqn5bRVs9XIQZoNKA7Crqfx64QlXTgMEYQYmIdHOeabDP+U7+IzGD9j2O+egXETnLrz1PYPY+iFQju9T5jMYsbkvFDCwhUdXZwIPA6859OyRE2kvxfdP8BLM3wxmYuEedMAPFU65sH2F+N+0wg+IrTlnT/MoKd9vODhgNqzvmuYWq/xLMy1FXIBOj5RcCOCa8YM9riV+dV4vIbsdM7P+8quJ0jGBsjflezXTMpv6UYbTGNpgXmjHA1c61kzDf776Y7/65GEGHiEwO9d0Ls41nYL6bgQIw+uD83u4AJmL24PgSsyeHG5/xrlrURKLU5wc4BtgR4vplmDeZNn7nHwCmh1nHpYSvKax1XUvGSPgOGLNMEZDkun4e8HmQcs8AfnYdbwB+55emBOjvOh5FZU3BrUk8DEytoq898H1zPxf40i/NM8Bfg+R/FPhXoLKcc1OoWlO413U9ZP0YbeQKQrzpV9HfO5z6p2C0zuMwb8kDnOtnArMD3d8wyv4UuNp13M95ZnGBysL3LdXnPlVRzwv4vmmuAMa4jjt66g2Qt6XT/4xAZTnnqtIUinFpoKHqx7zRfgMMqc7zcso7DCNQ4jCaYi5wTJh5pwDfuY5jMFrAb/yfQYC8N2B24wOz899qYAQQU92+BHl+Chwf7Dfi+p14xp2PMCFc3H0qwKUtYIT9X2rSzqakKewhSGx9R4I+hDHh7PK7XFcx5Xd4/lHVAuffVMxbVDyw3fXG8AzmbQ0RaScir4nIVhHZj1Gx2/iV7R+nP2jfA7UH80VJDZYwCN2BI/3edC7ACDpE5EgR+VxEskVkH+bNz7/dkeLuZ8j6MTuajQc2isgXIhJpXJ9CzIB1v6oWq+oXwOfASY6W9DCVo4+Gi8/eCM7/cZgXhLqkOzDDdb9WYN5624tIrIg8JCK/Ot+zDU6emjyzbDXbnVZZP8a8NAd4TUS2OZNAAr2lB0VVf1LVHFUtVdVZmAFvYgRFeL9favar2IJ5Vj6ISF8R+UBEdjj36kGc+6Sqn2G0vqeAnSIyTUTSI+lHuG0Mg+7AY677vRtjeXCHlq/xeNeUhELA2PoiMhZ4FhNh8pcA+aoVW78GbMZoCm3U7PjVUlXTVdVjBvk/zNvAEFVNx0TK9N8CUv2OK8XLrwM2A1+42txSjWnhKuf6qxjHfVdVzcBE4PS027+9YMxNya7jDgHSuPOFrF9Vf1TV0zHCdSbGfu0xH+WF+FzglO9vlnDTB/OW9qWI7ADeATo6g0SPEPk8+OyNgNnvoBSzwY7PfXBmz7QNcg8iZTPmRch9z1qo2fXtfIz55ASMGcfTj1DPrIDQz8w/T9D6VbVEVe9R1YGY3eROxZgfEZGpIZ5XqIkPSuXfSii8e1A4Exm6YJ6VP/8GVgJ9nN/kHe56VPVxVR2GMbn2xUxGQETuCPXdC7ON7nua7/wN9gw2Y0yo7vudpKrucOs1Hu+ajFDQwLH1j8e8PZylqj/455EIY+tXZJMW7k+E7dyOCW/8iIiki0iMiBwkIp52p2HMFnsdAXdLGMUGipdf23wA9BWRi0Qk3vkcLhU7kKUBu1X1gIgcgRl0PGQD5Rh7uodFwLHOoJ0B3F7d+sVME71ARDKc78F+zBspqrpJfWen+H9eccqfjzFB3S5m34RjMCaROcBSzAAy1Pn8ATOgD8V5kxOReSIyJUjb/wfcKCI9RSSVCj9BKcb00EJETnHelO8C3LNDdgI9pHqzr6YCD4hId6eNbUXkdOdaGublJAczyDzol3cnvs8LzDM739EyxlL1dy5o/SIyWsye17GY51VCxTO7MsTz8q4rEpGzRSTV+Q2dhHmBes91fYOIXBqifcNEZKKYmT03OPfjuwDp0pw25olIf8DzIoTzHTzSeXb5wAFXPx4M9d2r4t5VQlWzMZMoLnSewe8wE1M8TMV8fwc5bcsQkd+62toZ4z8J1MewaTJCwcE/tv7dmLegWS4J/ZHreqSx9cG81RS6PxL5dLGLMXbr5RjTz1sYeyuY2PiHYWYyfIh5K62KQPHyaxVVzcU41SZh3qZ2YPYu9gxgVwP3ikgu8BecN3UnbwHOTCJHtR2hqnMxMz+WAAsxg35N6r8I2OCo91diBohI+leCeXMej7n3zwIXq+pKxzyxw/PBqOXlzrFnCmRXzEypQEzHmEvmY2aRHMAxRanqPsy9ew7zg8/HmDE8vOn8zRGRnyLpE/AYZpD82Hku32GclmC+MxudOpdTeaB4HhjoPK+ZzrnrMfs67MWY7mYSmlD1d8B87/djzEpfYEylkXC90/69wN+BP6qztkBEEjD+hlAD4LsYX9UezPdnovM98OdmzEtOLuZ78brrWrpzbg/mfuZgZh3WFX/EvCjmYDQTrxagqjMwv4nXnN/BUsxMOQ/nAy9qDTdWanIB8aSRxtava8QVL7+h29LcELPb2Ztq9ydoNIiZQXiNqp7X0G1pDDhWkcXAsapao3U2TU4oWCwWi6XuaGrmI0sEhHCEfVR1bktDEMJxGcrkabHUGlZTsFgsFosXqylYahVpoCi2YdSVJCLviwmE92bVOeq8PQNFZEGI696AdVJLUXFrgohcJyIPNWQbLPWDFQqWWkMqR7GdJCKrnIE4S0ReFN+FP5FGsU0QkUfERMTNE5H1IvKvMLOfjVlUlamqv5WGjxJ6H2HOYtFaiIobDmIWZq0SkfIAUz2nYaZK1jg0s6VxY4WCpTbxj2L7NSYsQQZmTnwcJjigh0ij2N4ODMcEMEvDxBqqchaaQ3dgtbN2oEFx+juaqqd81jeLMdNnK02NdVYyf4SzAM0SvVihYKkVnHnjx2PmowOgqpv9wo6UYYIEeq4fwKxhOCnMag7HxKTZpoYNqvqSqw0DnEVme8VsonKac/4ezNqKcx0N4wrMPPxbneP3nXQbROQWEVkiIvki8ryYjW0+ErOxzSci0spV35tiVj3vE7P5jWdRUYKILBKRPznHsY5Z7S9O1hOBn9whI0TkUBH5yanndUyUUc+1UeLa3yHSdoaLqj6lqp9i1lkEYh4mGKIlirFCwVJbBIxiKyIjxcRKysXEL3rUL18kUWy/A24SkavFrJYVV7544H3MavJ2mMVjr4hIP1X9K77RSJ8heJTQszCDdl/MQq6PMGEP2mB+L9e50gaLQlqMWVx3r5gV4ZOBWMwCP/CLeusI1JkYLas1ZkFbVRFBw26nhI4iO7mKetzUPAKnpdHTqHfKsjQpWmIGfh9U9SsgQ8wS/D9SEZjNQy4Vq71R1ZYh6vg/zMrSCzAx7nNE5HY1O+KNwAQBfEhN8LPPROQDTITaKRH04wlV3QkgIl9iFgx6fCQzMGGVPW2d7vlfTAiMPWJCcexT1aWOz2IGxpdxhGt1dEuc8MsOIzBBFB9VMx3wLRG5qRbb2TKC/ociFxNBwBLFWE3BUluEjOTqBGmbDbzmdynsqI6qWuaYOI7BDKwPANOdt/FOwGZHIHjYiG8EyXDY6fq/MMBxKnhNQlVFIX0RE4hulqqucZ33v1edgK3qOz/cHXW12u2sZdIwIUIsUYwVCpbaImAUWz/i8A3wBdWM6qiqhar6FGaAHYiJl9RVfAPLdcPEzglYRKR1+lFVFFKApzExn072M4n5R73dDnR2m8Mwba8VJHQU2TsiKKq+Iw5bGgArFCy1QpAotheIiZIqYiJpPoDZkMZzPaIotiJyg+N0TRIT6fQSzNvrz8D3mGBzt4qJsDoKY2v310w8BIoSGgkho5CKyEWYvl2Kse+/KCaCKpj+HiYVEXi/xYTavs7p10TMDKtaoYoost52Ow7yFhjBFi8mSrB7jDgO47uwRDFWKFhqE/8otgMxUR7zMNNTV2H8Ch4ijWJbCDyCiaC6C7O/7Vmqus5x7p6GiRq5C/OWfrGqrgxSVqAooZEQNAqpiHTDONQvVtU8VX0VWIDxg+D4Aj7DaBoex/REjADZg4nsGU703NrmY8w9PhqzLqEQZ6tVR1iMx5jELFGMDXNhqVWkmUaxjRQRGYgZYI/QJvAjdKbXdlXVWxu6LZa6xQoFi8VisXix5iOLxWKxeLFCwWKxWCxerFCwWCwWixcrFCxRg4QIxS0iU0Qk0j2CLZZmhxUKlmgiolDc1UVEhorIQhEpcP4ODZE2UUSmi8h+J3jeTX7XQ4WrtljqHSsULNFEpKG4ARCRsGOAOcHr3gX+C7TCTCt91zkfiCmYoHndMeGybxWRsa7rQcNVWywNgRUKlqgh3FDcItJDRFREfi8imzALycJlFCZcx6OqWqSqj2NWAB8fJP3FwH2qukdVVwDPYhapedpcVbhqi6VesULBEm1EEt75OEw8n5Mh7BDTg4AlfgvOljjnfXD2NOiEb7ygxYHSWiyNBRs62xJt+ITiroIpqprvOQgzxHQqlSOF7iNwhNhU1/Wq0losjQKrKViijbBDcQObq1F+HpDudy6dAHtJOGk916tKa7E0CqxQsEQbkYR39onxEmaI6WXAEL8w10Oc876Fq+7BhMV2m7MOCZTWYmksWPORJWpwheK+xDlWYLSqzgsnv6qGszHNPMxe09eJyFQqor4Gc1a/BNwlIgswO7D9EbjM1eYEzMuZN1w1UOy3WZDFUm9YTcESTXhDcYtIF4z55pfarMAJc30GZlbRXuB3wBnOec8eEm5N4K/Ar5gw218Af1fV2a7rQcNVWywNgY2Saoka3KG4ReRCYJCq3t7Q7bJYmhJWKFgsFovFizUfWSwWi8WLFQoWi8Vi8WKFgsVisVi8NMopqW3atNEePXo0dDMsFoulybBw4cJdqtq2puU0SqHQo0cPFixY0NDNsFgsliaDiGysjXKs+chisVgsXqxQsFgsFosXKxQsFovF4qVR+hQCUVJSwpYtWzhwIPr3ImnRogVdunQhPj6+oZtisViaGU1GKGzZsoW0tDR69OiBb4DK6EJVycnJYcuWLfTs2bOhm2OxWJoZTcZ8dODAATIzM6NaIACICJmZmc1CI7JYLI2PJiMUgKgXCB6aSz8tFkvjo0kJBYvFYolWvtz4JQ9//XBDN8MKhXDZu3cvTz/9dMT5xo8fz969e2u/QRaLJSrYe2AvV7x/Bce+cCzPLHyG/OL8qjPVIVYohEkwoVBWVhYy36xZs2jZsmUdtcpisTQkecV5PPLNIyzctjDivDvydvD0j08z8KmBPPfzc/z5qD+z5MolpCSk1EFLw6fJzD5qaCZPnsyvv/7K0KFDiY+PJzU1lY4dO7Jo0SKWL1/OGWecwebNmzlw4ADXX389l19+OVARsiMvL49x48YxcuRIvvnmGzp37sy7775LUlJSA/fMYrFUh1lrZnHVh1exad8mYiSG64+8nvtG31floP7W8rd49LtH+WbzNyjKsI7DeP+89xnWaVg9tTw0TVIo3DD7BhbtWFSrZQ7tMJRHxz4a9PpDDz3E0qVLWbRoEfPmzeOUU05h6dKl3mmj06dPp3Xr1hQWFnL44Ydz1llnkZmZ6VPGmjVr+N///sezzz7LOeecw9tvv82FF15Yq/2wWCx1R0lZCfM2zOPZn57lzeVvMqDNAGZfMJsZK2fwr+/+xTsr3mHyyMmc0f8MOqR2qJT/ie+f4LrZ1zGgzQDuGXUPEwdMZGDbgY1qckmTFAqNgSOOOMJnHcHjjz/OjBkzANi8eTNr1qypJBR69uzJ0KFDARg2bBgbNmyor+ZaLFGJqrJ452LeX/U+ndM7c+nQS4mR6lnF9xTu4YPVH/Dlpi8pK69sFs4tzmXuurnsPbCXlPgUphw3hckjJ5MYl8jJvU/mwiEXcs2sa7jqw6u4+sOrObrr0ZzZ/0zOHHAmvVr14qGvHuL2T2/njP5n8NpZr5EYl1jT7tcJTVIohHqjry9SUipUxHnz5vHJJ5/w7bffkpyczKhRowKuM0hMrPgSxMbGUlhYWC9ttVjqm6VZS3l35btMHjmZ2JjYiPJuz93O498/TreMbpzR/ww6pnWslEZV+fs3f2fqgqms37vee/65n57j2QnPMqjdIFZkr2DGyhnsL9rPqX1P5aguR1Vqy/bc7by76l3eWfEOn2/4nNLyUlq1aBXQBBQXE8fp/U5n4oCJnNjrRJLifU2/I7uNZNEVi1iWvYwZK2bw9oq3uXnuzdw892YOanUQv+75lfMPPp8XTn+B+NjGG62gSQqFhiAtLY3c3NyA1/bt20erVq1ITk5m5cqVfPfdd/XcOoul8ZCdn834V8azef9m0hPT+dORfworX7mW89xPz3Hr3FvZX7QfRblm1jWM6DKCW4+5lTP6n+FNd/WHV/PMwmcY03MMd/7mTib0m8DstbO5ac5NHPrMofRo2YM1u9cAEB8Tz9++/hvtU9ozsttI4mLMsLdp3ya+2/IditKndR/+fNSfmThgIsM7Da+2tiEiDG43mMHtBnP3cXezfs96ZqycwYdrPuSsAWfx4JgHIxaS9Y0VCmGSmZnJMcccw+DBg0lKSqJ9+/bea2PHjmXq1KkMGTKEfv36MWLEiAZsqcXScJSWlzLp7Ulk5WcxrOMw7vjsDs4ccCZd0rv4pMvKz+Ldle/y2YbPKCotAmDjvo38tP0nRvcYzTOnPkNxWTEzVs7glV9e4czXz+TM/mfy6NhHueuzu3h5yctMPmYyD4550GuPv/iQixnXexy3f3o7W/Zv4YYRN3B6v9NJS0xj1ppZvLPiHZbsXOJtQ8sWLbl39L2c2f/MOrPr92zVk5uOuombjrqp1suuK0RVG7oNlRg+fLj6b7KzYsUKBgwY0EAtqn+aW38t9UdpeSl3fnonZw88m8M7H16rZd829zYe/uZhpp82neN6HMfgpwdzcu+TmXGu8bd9seEL/jLvL3y16SvKtZwu6V1o1aIVAAmxCVx9+NVcNvQynwG6pKyEf377T6Z8MYXismLKtZz7R9/PncfeWattb+qIyEJVHV7TcqymYLE0M15e/DIPf/MwLyx+gZ8u/4nO6Z3DzltUWsQj3z7C7sLd3H3s3WS0yACMSefJH57k4W8e5ophV3DZoZcB8Nfj/srkTyfzwqIX+HrT1zz383N0z+jO3cfezcQBEzm43cFVvqHHx8Zz28jbOGvgWdz+6e0c3+N4rjr8qurfAEtIrKbQSGlu/bXUD0WlRfR9si8p8Sls2reJIe2HMO/SeSTEJvikKy0v5f7597Mjbwdn9D+D43sez49bf+SP7/+RFbtWIAgd0zry5Lgn6d+mP5d/cDlfbfqKsb3HMvPcmd6ZNSVlJQx/djhLdi4hVmK56aibmDJqCsnxyQ3R/ajGagoWSzNg5sqZfLb+Mx4b+1it2LyfWfgMm/ZtYu5Fc9lTuIdz3jqHm+bcxJPjn/SmKS4r5sJ3LuTN5W+SFJfEMwufIS0hjdziXLpldGPW+bNok9yGP77/Rya+MZEYiSEjMYP/nP4fLjnkEp92xsfG89IZL/HgVw8y+ZjJHNrx0Br3wVK3WKFgsTRSCkoKuOrDq9iRt4OTDjqJU/ueWqPy8orzeODLBxjdYzRjeo5BRPjz1j/zyLePUFBSwLmDzuXorkdz/jvn88HqD/jHif/gmiOu4ZN1n/Duyndpl9KO239zO6kJqQD8+Mcfeez7x1i7ey33jLqH9qntA9Z7SIdDeP3s12vUdkv9EZZQEJGxwGNALPCcqj7kdz0D+C/QzSnzH6r6H+faBiAXKANKa0O9sViaA0/+8CQ78nbQJrkNd352J+P7jA85VVJVeWfFO0xdOJXrj7y+khB5/PvHycrPYua5M71v8w+d8BC5Rbm88ssr/GfRf4iVWMq0jH+f8m+uHH4lAKf2PTWgQIqPjefmo2+uxR5bGgNVCgURiQWeAk4EtgA/ish7qrrclewaYLmqThCRtsAqEXlFVYud66NVdVdtN95iaUqoKld/eDXZBdmc2f9MTul7Ci1btAyYdt+BfTz01UOM7zOeCw6+gAveuYA3lr3BpMGTAqbfsn8L18y6hvdWvUdyfDKfrPuEcwadw2NjH2N77nbeWfEOj33/GBP6TuCorkd588XFxPHMhGd4dOyjfLLuE2avnc2YXmOYOGBiXdwCSxMgnBUaRwBrVXWdM8i/Bpzul0aBNDGvH6nAbqC0VlvaxEhNNSr2tm3bOPvsswOmGTVqFP4OdUvj4MuNX3Lqq6eyq6D23mU+WfcJUxdOZc6vc7hwxoW0+3s7xv53LNMWTmNn3k6ftI98+wh7Duzh/tH3M2nwJA5udzB3f343JWUlPunKtZynfniKgU8NZO6vc3n4hIfJviWb+0bfx8yVM+n8z84cNu0wHvzqQYZ1Gsa/Tv5XwLYlxScxod8EnjrlKSsQmjuqGvIDnI0xGXmOLwKe9EuTBnwObAfygFNc19YDPwELgctD1HM5sABY0K1bN/Vn+fLllc41ZlJSUqpMc9xxx+mPP/4Y8FpT6280kV+crz0f7alMQS+ecXGtlFleXq7Dpw3Xbv/qpgXFBfrNpm/05jk3a6/HeilTUJkiOnL6SP3nN//UH7f+qKkPpupv3/itN/+7K99VpqDPLnzWe27pzqV61HNHKVPQE146QX/d/atPnSuzV+p1s67T5xY+p1l5WbXSD0vjBVigVYzn4XzC8SkEmvLgP4/1ZGARcDxwEDBXRL5U1f3AMaq6TUTaOedXqur8AMJpGjANzJTUMNpVr9x22210796dq6++GoApU6YgIsyfP589e/ZQUlLC/fffz+mn+ypRGzZs4NRTT2Xp0qUUFhZy2WWXsXz5cgYMGGBjHzVS7v3iXtbvXc/4PuN5afFLXDzkYsb0GhMyzwerP+DOz+4kpyAHgNiYWG4acRPXj7geMLOIFmxbwPTTppMUn8RRXY/iqK5H8fCJD/NL1i/MWDGDd1a+w00fm5WvMRLDvaPv9ZY/oe8Ejux8JNfOupYp86YAsDN/JxmJGbx4xotcNOSiSrOT+rXpx2PjHqut22JpJoQjFLYAXV3HXYBtfmkuAx5ypNVaEVkP9Ad+UNVtAKqaJSIzMOaoSkIhEm64ARYtqkkJlRk6FB59NPj1SZMmccMNN3iFwhtvvMHs2bO58cYbSU9PZ9euXYwYMYLTTjst6NTBf//73yQnJ7NkyRKWLFnCYYcdVrudsETMY989xiu/vMI/TvoHx3Y/liU7l/CPb/7BZUMv46nxT3Hwvw/myg+v5JerfqFFXItK+Xfk7eD62dfzxrI3GNBmAGN7jwVgze413DDnBvYe2Mtdx97FXZ/fRb/Mflx0yEU++UWEIe2HMKT9EP466q/8uvtXZqycQZvkNvRv098n3bQJ03jyhycp13IAMpMyufnom2mb0rYO75CluRGOUPgR6CMiPYGtwCTgfL80m4AxwJci0h7oB6wTkRQgRlVznf9PAu6lCXLooYeSlZXFtm3byM7OplWrVnTs2JEbb7yR+fPnExMTw9atW9m5cycdOlSOow4wf/58rrvuOgCGDBnCkCFD6rMLFj8+/vVjbpxzIwmxCRz3wnFcftjlLN65mFZJrfj7iX8nKT6JqadO5cSXT+Tuz+7m8M6HM2PlDD5b/xnFZWYORUFJAQD3jb6PW4+51bsIrLS8lD+89wemfDGFzzZ8xvLs5bxx9hveYGzBOKj1QUFn9AxpP4RpE6bV4h2wWCpTpVBQ1VIRuRaYg5mSOl1Vl4nIlc71qcB9wAsi8gvG3HSbqu4SkV7ADOfNOQ54VVVn17TRod7o65Kzzz6bt956ix07djBp0iReeeUVsrOzWbhwIfHx8fTo0SNgyGw3jWkzjebMhr0bOO/t8xjcbjCfXvwpD3/9MP/87p+Uazkvn/kymclmL4wTep3ARUMu4h/f/gOAtsltGdt7rE+8nt8f9nuft3ows3qmnz6dlPgUnl7wNId2OJSzBp5Vv520WKpBWOsUVHUWMMvv3FTX/9swWoB/vnXAITVsY6Nh0qRJ/PGPf2TXrl188cUXvPHGG7Rr1474+Hg+//xzNm7cGDL/scceyyuvvMLo0aNZunQpS5YsCZm+ObJ4x2LGvzqe7PxswMyFv/ywy7nv+Pu8i6aCkZ2fzRmvn0FKfApPjX+KPpl9AqYrLClk4usTKSsv451z36FtSlv+ftLfOe/g8/hx649ccPAFPukfG/sY/dv0Z2S3kRzT9ZiwQx/HSAxPjn+SIzofwYguI6odjtliqU/siuYIGDRoELm5uXTu3JmOHTtywQUXMGHCBIYPH87QoUPp379/yPxXXXUVl112GUOGDGHo0KEcccQR9dTypkFZeRl/eP8PlJaXek0om/dv5tHvH2XGyhn8+5R/M67PuIB5t+Vu44SXTmD93vUkxiZy8L8P5q/H/ZUbRtxAXEwcivLLzl+YsXIGby5/k9U5q3n/vPfp3bq3t4zDOh7GYR0r+3laJbXijt/cUa0+iQiXDL2kWnktlobABsRrpDSm/qpqULNXqGuR8vj3j3P97Ot5deKrnHfwed7zX2/62huI7eETHuaWY27xybdh7wbGvDSGrPwsPjjvA/pm9uW62dfx1vK3KtURK7Ec1+M4rhh2BecMOqdW2m2xNAZsQDxLvXHCyyeQnpjOqxNf9W5BuKdwDxPfmMiyrGVM6DuBiQMmckKvEyLad7asvMxritm8bzN3fnYnJx90cqVVu8d0O4afr/iZi2ZcxORPTVC1E3qdAMDqnNWc8NIJ5Bbn8slFn3BklyMBePO3bzJn7RwWbKt4ueic3plT+55Km+Q2NbofFks0Y4WCxUu5liOIz5v/zrydfLb+MwDGvzqe9ya9R2FpISe9fBIrdq3glD6n8NaKt5i+aDoHtTqIuRfNpWernlXW9dbyt5j01iSO6XYME/tP5ON1H1NWbmLuBNI8EuMSmX76dJZnL2fSW5NYePlCcotzOeGlEyjXcj6/5HOGdhjqk+fk3idzcu+Ta3ZTLJZmRpPyfDVGU1ddUN/9LC0v5ZFvHiH9/9J57qfnfK59uelLAG4acRNfbvySE18+keNeOI7VOat5b9J7vHPuO2TdbIKs7S7czbEvHMuqXatC1ldSVsJtn9xG14yu7C7czQ1zbmDWmllMGTUlpEBJTUhlxrkzKCkvYcL/JnDcC8cRGxPLF5d+UUkgWCyW6tFkhEKLFi3IycmJesGgquTk5NCiReWFUnXBz9t/ZsRzI7h57s0UlxXz6tJXfa7P3zif5PhkHjrhId787Zv8tP0ntuzfwuwLZ3vfwhPjEjm9/+nMu3QexWXFHPvCsT574foz/efprNuzjifHPckvV/3C6mtX8/rZr4e1j22fzD68fObL/JL1C+mJ6Xx52ZcMaNs4fC8WSzTQZBzNJSUlbNmypcp1ANFAixYt6NKlC/Hx8XVaT1Z+Fj0e7UF6YjpPjHuChdsX8si3j5Bzaw7piekADJ06lLYpbZl70VzACJHk+GT6tekXsMxVu1Yx5qUxlGs5665fV2kVcGFJIb2f6E2Plj346rKvqu2k/mrTV/Rp3SdoDH+LpbnR7BzN8fHx9OxZta3aEj7zNsyjsLSQzy75jBFdRtAupR1/+/pvfLruU84ccCZ7CvewZOcS7hl1jzdPVTtn9WvTj5fOfIkxL43hv0v+yx8O+4PP9ad/fJptudt4deKrNZq1NLLbyGrntVgswWky5iNL7eMxDQ3rOAyAo7seTXpiOh+t/QiArzd/jaIc2/3YiMod3WM0QzsM5Z/f/tMbpwdgf9F+/u+r/+Okg07iuB7H1V5HLBZLrWGFQjPmy01fcnTXo4mPNWaq+Nh4Tuh1Ah+t/QhVZf7G+STEJnBE58gW2YkIfz7qz6zYtYLZayuimtw29zZyCnO4f/T9tdoPi8VSe1ih0EzZXbibX3b+wrHdfLWAcb3HsWX/FpZmLWX+xvkc3ulw79qESDhn0Dl0TuvMI98+AsALi15g6sKp3Hr0rRze+fBa6YPFYql9rFBopny9KbBpyBP6+e0Vb7Nw+8KITUceEmIT+NMRf+Kz9Z/xn5//w5UfXMnxPY/ngTEP1LjtFoul7rBCoZkSzDTUJb0LQ9oP4dHvHqW0vLTaQgHg8mGXkxKfwu/e+x3tUtrx2lmvVRk62mKxNCxWKDRT5m+azxGdjwhoGhrXexz7ivYRIzEc3fXoatfRKqkVVw2/isTYRN465y27GYzF0gSwQqEZklecx0/bf6rkT/AwrreJRHpoh0O96xWqy99O/BubbtwUsbPaYrE0DFYoNEO+2/JdSNPQ0V2PpkNqB69/oSbESAztUtrVuByLxVI/WANvM2T+xvkhTUPxsfGsuGYFKfEp9dwyiz+7d8P27TBoUEO3xNJcsJpCM2T+xvkc2uFQ0hLTgqZp2aKld/2CpeG45RYYMQKaQXQXSyPBCoUoorCkkI9//ThkmqLSIr7f+n2NZhVZ6ofycvjwQ8jLgy+/bOjWWJoLVihEEf/89p+c/N+TWbt7bdA0X2z8ggOlBxjVY1T9NcxSLRYtgp07zf8ffdSgTbE0I6xQiCJmrJwB4LPbmD//W/o/0hPTOemgk+qrWbVOURH86U/w9de1W+4PP8DYsXDiieZz0UWwZ0/Ny73vPvjgg8jzeQTBoYdaoWCpP8ISCiIyVkRWichaEZkc4HqGiLwvIotFZJmIXBZuXkvtsHnfZhZuXwjAT9t/CpjmQOkB3lnxDmcNOKtSSOumgipcfjk8+SS8VXkL5hrx5JMwfz4UFJjP66/DWWdBcXH1y9y8Gf7yF1POV19Flnf2bBg2zAinlSthw4bqt8NiCZcqhYKIxAJPAeOAgcB5IjLQL9k1wHJVPQQYBTwiIglh5rXUAjNXzgSgQ2oHr3DwZ9aaWewv2s95g8+rx5bVLg8+CC+9ZP7Pyqq9csvLYc4cOOMMo4F8/TU89xx8/jlcfbURRtVhzhzzNzPTlL02uGXPh7174dtvjeYyziwbYfbskFksllohnCmpRwBrVXUdgIi8BpwOLHelUSBNTID8VGA3UAocGUZeSy0wc9VMBrQZwLHdj+X1Za+jqpX2K/jf0v/RLqUdo3uOrrd2qRpzT1UbyWVlQWFh6DSffw533QUXXghr1gQWCiUlIAJxEU62/vlnU55nAAa4+GJTz/33Q9++cOutlfMVFEBycvByP/oIunSBzz4zs4hOPdUM9q1ahW7P3LlQVmba068fdO9uyrryysj6VZ+Ul8OWLRUCNCMDWrZs0CZZqkE45qPOwGbX8RbnnJsngQHANuAX4HpVLQ8zryVCVu1axUuLX/Ie5xTk8MWGLziz/5kc1vEw9h7Yy4a9G3zy7C/az/ur3uecgefUa/yhp56Cbt1g377gaebPh/btoUeP0J/LLoORI80bfPv2gYXCSSeZdJHisdmffLLv+XvugXPPhdtug3XrfK9t2WIGvb//PXCZJSXwySdmYO/TB2bONGWEY5L66CNT9pFHGiE3bhx8+mnNTFl1zd13G+HleV5du9auNmepH8IRCoG2x/JXpk8GFgGdgKHAkyKSHmZeU4nI5SKyQEQWZGdnh9Gs5sudn93JJTMvYfrP0wH4cM2HlGkZZ/Q/g8M6HgZU9ivMXDmTorIizj/4/Hpt6+LFkJ0NL7wQPM2MGZCYCM8/D9OnB/+8/LKZopmYCO3aBR5wli6FV1+FTZsia6fHft/Ob/F1TIxxagOsWuV7beVKM/Dfeiu8/XblMr/5Bvbvr9A+fvMb08eqTFKqpj0nnlih8YwbB/n5kfsl6ouCAvj3v2HUKPOsHnvMTKWdNq2hW2aJGFUN+QGOAua4jm8HbvdL8yHwG9fxZxizU5V5A32GDRumlsAUFBdoygMpGndvnCbel6g/bv1Rz3jtDO38SGctLy/XwpJCjbs3Tm//5HaffCe/fLL2eLSHlpeX12t7x41TBdXevVXLygKn6ddP9eSTIyv39ttVY2N9yywqMnWB6uTJ4Ze1e7dqTIzqXXcFvr5hgynz2Wd9z7/wQkXfkpJUf/jB9/rkyapxcar79vmev/tuk+9vfwtc36JF5vr06RXncnNVExJUb745/H7VJ9OmmTZ/8UXFuRNPVO3USbW4uOHa1ZwAFmgVY2s4n3DsCD8CfUSkJ7AVmAT4v25uAsYAX4pIe6AfsA7YG0ZeSwR8su4T8kvyeWXiK9z+6e2c9cZZZOdn87tDf4eI0CKuBYPbDfbRFLLys/hk3SfccvQtNdoXGYwJY968iuNRo2DMmODpt26FlBTjYJ0zx9dmD7B+vXkDj9RW3q6dsbnv3QutW5tzHs0hMRGefdbM+kkKY3+guXONPdy/bR46dqzoixvP8SefmPtw2mnw/ffGXAbGBHTMMZDuF1PwnnuMr+K224wJKiPD9/pPzqMb6wo9lZpqNI1Zs+Dhh41JycOuXeaNPJBPJiXF3NvatO3/8IMJv+Fpnyo88QQMGWLa6OG662DCBKMJnnNO7dVvqWPCkRzAeGA18Ctwp3PuSuBK5/9OwMcYf8JS4MJQeav6WE0hOL+b+TvN+L8MLSot0h+3/qiJ9yUqU9C5v871SdP24bZereD+L+5XpqBLdy6tcf0DBpg3wpgY8zczU7WgIHj61q1Vf/971Q4djNbgz9NPm3JWroysHa+8YvKtWFFx7scfzbkbb6z8ph2Kyy5TbdlStaQkeJp27VT/8Affc1ddpdqqlfl/2TLV9HTVgw82msHWraYNDz0UuLzCQtWTTjL3MdAnkOY0dWrlMgsKVEeMqHgm/h9QHT3aaFG1wc8/q6akmLLff9+cmzcvsCZVWqraq5fqyJG1U7clNNSSplDjAuri0xyEwrMLn9Xvt3wfUZ6SshJt83AbPf/t873nXlnyih7/4vFaXFqhoz/5/ZPKFHTT3k16oOSAdvhHBz3p5ZNq3ObycmMmuekmc/zpp6EH34ICc/3++1WnTDH/r17tm2bCBNWePU3ZkTB3bmVzxfvvm3Pff686eLDq0KFVl1tertqxo+o554ROd9hhlYXaaaeZejx8/LExaY0bV2FOWbw4sn5V1dZJk0y5b75pTGfnnmuO3347cJ6XXjLXf/e7yO+xP1u3qnburNqli+qhhxrhsGiR6llnGeGYn185zyOPmPp//rlmdVuqxgqFJk7rv7XWSW9NiijPFxu+UKagbyx9I2S6bzd/q0xBZ66Yqf/5+T/KFHTO2jk1aa6qqmZlmW/MY4+Z4/Jy1UGDzAARaMBZu9ak/89/VLdvV42PV73++orrBw6YgeXqqyNvy+LFFYOjB89AvGlTxVv1l1+GLieQ/T4QEyaoDhnie27YMNWxY33PPfOMKS8lxdjTa9uFU1ioetRRqi1aqF50kYb0TXioyocRDnl5RjCmppp7tnWrEQ6dOhlBeMstgfPt2aOanGyEkqVuqS2hYENnNxBFpUWszlkdUZ4ZK2aQGJvos8/BJ5/AI4+YMAqxsebckPZDiJEYFm5fyMyVMzm43cGc2OvEGrd540bzt3t381cErr0WrrrKzLQ55hjf9B6be+fO0KED/Pa3ZmbKn/9spit+9ZWZUTO2Gts2tHU2cXPPQNqxw/xt186sZZg82fgJUlODl+Oxw1fVhs6dTR/dbN0KQ4f6nrv8cli92jyTc8/1tf3XBi1amKmtRx5pZmP9/vcmkmoo7rnH+HRuuw3+9a/K12NizL3yzLLyp6zM3M9Fi+C99+CQQ8z5Dz4wU4RVzWyqQLRsaVZkP/us8Yf4k5ZmvhMjRwbOn5UFEyfCr7+G7mO00LYtLFnSsG2wQqGBKCozQkG18iKzQKgqM1fN5IReJ/iEvP78czN9cccOM3ABJMcnM6DNAKYtnMbO/J385/T/1NjBDBVhFjxCASoG3yeeqCwUtmwxfz3t+stfzEBy6qlGIHz0ESQkwPHHR96WNm3MX/fs5R07jNM5MdF8pk8PbxXwwIEVzuRgdO4MOTlGiCQlmamoO3dW9M3N3/5mnM2nnx5+fyKhXTv4+GN45x248caqBY+IuRe9e1cE2HOzfLlxCnfsCGefXfn65MlGED32GJxySsX5Qw4x7fj1V7MuIRh33WWm1paUVL72ySdmpfd335n2uTlwwFz7+WfzPYtpBpHa/CclNAi1oW7U9ifazUdl5WXKFJQp6Nb9W8PK8/P2n5Up6HMLn/M5f/XV6rWju7l4xsXKFLTDPzrogZIDtdLuf/zD1LVnj+/5G280Uy+3+nXl4YdNeveUzNmzjblh/HjjtD7hhOq3p3VrX9PTxImqAwdWv7xQ/Oc/pi9r15rjjRvN8bRpdVNffeI2Sfl/jzzmsGuvrZu616wxkxX69jVTgz34+08sVUMtmY+agextfBSXVSxLDdeENHPlTGIkhgn9Jvic90Tx9J8ueVgHs4jtT0f8icS4xOo31sXGjeZNxn964zXXGBPD1Km+57duNaYb99vPyScbrWLWLFixIvg00HDwX8C2fXvVb/zVxaMReO6z2zTW1GnRAt5919y7004zU0g//NBMc736avOMApmdaoPevU19GzYYM9GHH5rPjTfCa6/BQw8F1l4sdYc1HzUA/kIhnL0NPt/wOcM6Dqu037FHKHhMNR4mDpjIgu0LuPrwIMbearBxo6/pyMNBB5nB/pVX4N57K85v3Rp40LzqKmPjfvJJY0qqLv5CYccOODrwDqM1JpqFAhhb9ocfmvs3cWLF+YMPNoNzpLGkIsGz0vuii3zXwPzud4HjTVnqFisUGoCi0iLv/6t2rQqR0lBSVsKPW3/k8mGXV7oWTFPomtGVl898uUbt9CeYUADjT5g924Q28Dh2t2wJPmg+8gjccYeJHlpd2rUzYS3AODt37DAO7brA0w+P8PX3l0QDAwaYRXXr11ecGzw4vAWANeXCC41AyskxxwkJZjFcbTvqLVVjhUID4KMp7K7afLR452IKSws5umvl1+BgQqEu2Lgx+CwRz8byK1bA4YdXtGl0iICsNREIYN5uPY7m3FzjBK4roZCeboSdW1NITKx5HxobbdpUOPHrm169zMfSsFifQgNQVFahKYTjU/h287cAHNXlqErX9u41f+taKOzbZ+oKpikMHmz+et7cy8uNjb8u36TbtTNvlqWlpi6oO5+CiOmLWyh07mzfZC3RhxUKDYBHU+jZsifr9qyjpCzAXD0X32z5hs5pnema0dXnvGpwn0Jt479GwZ9evYzDctkyc5yVZQbruhYKYGL/eNYo1JWmAIGFgsUSbVih0AB4fAoHtz+Y0vJS1u9dHzL9t5u/DWg6Kigwc79jYswgpdXcHSwcqhIKsbHGJu3RFDxCqkuXumuTRyhkZdWfUHD7FKxQsEQjVig0AB5N4eB2BwOhTUjbcrexcd/GgKYjj5bQu7cREKE2sqkpHqEQapHS4MEVmkJ9zM6pb6HQpYsxU5WVmf7VpcCzWBoKKxQaAI9PIRyh4PEnBNIUPP6Eg00xdWpC2rjRmIf8N6FxM2iQacPevfUjFNyhLrZvh/j4ijDadUHnzsYktmqV2WLUagqWaMQKhQbAYz7qmNaRzKTMkNNSv93yLYmxiRza8dBK1zyagmfmT106mzduNKEbQjlWPc7m5ctNW2JjQwuRmuIpOzu7YjpqXTp+PULg++99jy2WaMIKhQbAYz5KjE2kb2bfkNNSv9n8DcM6DSMhNqHSNY9Q8AzGdSkUNmwI7k/w4BFOS5cajaFTp4ogfXVBq1amfI/5qC5NR1BhLrJCwRLNWKHQAHjMRwmxCUYoBDEfFZUWsXD7Qo7uEniZbn1rClUJhW7dzFz+pUvrZ3ZOTIwxIdWXUPD054cfzF/rU7BEI1YoNABeTSEukX6Z/diWu4284rxK6X7a/hPFZcUc1bWykxkqhEKHDmbBUV35FAoLzcBblVCIiTECatmy+puy6Ql1UR9CoV07o5ksWWLMVHW1JsJiaUjsiuYGwONT8JiPwDibu2V046w3zuLX3b9yWr/TvMIj0MwjqHA0Z2T4zqGvbTZtMn+rEgpghMIHHxhBctJJddMeN23bGidzVlbdD9KxsaaOLVugfXvj2LZYog2rKTQAnsHeYz4CmL9xPqNeGMUPW39gWKdhvLj4RZ7/+Xl6tuxJx7TAo92ePUYgxMYaU0ZdCYWq1ii4GTzYDNC5ufVjXmnXzji2VeteU4CKPlnTkSVasZpCA+DxKSTGJdK7dW8E4aY5N5Ecn8ys82cxuudoCksKmbtuLh1Tg7/+7tlTEca6c+cKW3dtE84aBQ8e/wbUn/koP9/8Xx9CwdMn62S2RCtWKDQAbk0hKT6Jnq16klOQw0cXfOT1HyTFJ3Fav9NClrNnj5mBA2aQys428+cTa2f7BC8bNhhtpFOnqtN6ZkJ52lTXuKe8WqFgsdQcKxQaALdPAeD1s18nIzGDPpl9Iipn715foQCwbRv07FlbLTVs3GjMJeHE1O/Y0Wgve/fWv1CoD8evFQqWaCcsn4KIjBWRVSKyVkQmB7h+i4gscj5LRaRMRFo71zaIyC/OtQW13YGmxObNUFzsqykADO80PGKBAL6agsfGXRd+hXCmo3oQqdAW6mPg9KxqBuP8rWusT8ES7VQpFEQkFngKGAcMBM4TkYHuNKr6d1UdqqpDgduBL1R1tyvJaOf68NpretNC1Wwact99xqcQK7HExtRsZZe/TwFqXygcOGCmmB50UPh5jjjCrFmoj81ZPJpCRkb91Nevn+9fiyXaCEdTOAJYq6rrVLUYeA04PUT684D/1Ubjoon8fGNSefddYz4KtEI5Uvx9ClD7axXeeMPUc/754ee57z747rvabUcwPEKhPvwJAMOGma1ER4yon/oslvomHKHQGdjsOt7inKuEiCQDY4G3XacV+FhEFopI5f0kK/JeLiILRGRBtmc7rSgiN9f8/eUXyNmZRGJczbzBRUVmLYBHKLRsCcnJtaspqMLjj5uQ2GPGhJ8vObn+FnZ5hEJ9LiSLRGuyWJoa4TiaA4UYCxa5fwLwtZ/p6BhV3SYi7YC5IrJSVedXKlB1GjANYPjw4XW4M0DDsH9/xf+//tCHhO410xQ8C9c8QsF/Z7CNG+GBB0xIbYCUFHj4YWNmCZfvvoOFC+GppxrvDmOpqSZ6a31pChZLtBOOUNgCuLf86gJsC5J2En6mI1Xd5vzNEpEZGHNUJaEQ7biFwsaFA0jsVTNNwRPiwiMUoGITmH37YPx4swF7p05mI55Nm+DEE+Hss8Ov44knzN7EF19co6bWKSJw2WVw7LEN3RKLJToIx3z0I9BHRHqKSAJm4H/PP5GIZADHAe+6zqWISJrnf+AkYGltNLyp4TEf9e0L2xYPJJ7kGpXnEQoeRzMYobBpE5xzDqxeDR9+aOzfK1eauERLI7jz27fDm2+aATc1tUZNrXOefhomTWroVlgs0UGVQkFVS4FrgTnACuANVV0mIleKyJWupGcCH6tqvutce+ArEVkM/AB8qKqza6/5jYeqtsL0aArnngslBcmUbTqiRvUF0hS6dDGawscfw7RpMHq0OZ+UZOzgnl3RwuGZZ8yGMtdcU6NmWiyWJkZY6xRUdZaq9lXVg1T1AefcVFWd6krzgqpO8su3TlUPcT6DPHmjjTlzTJTSJUuCp/EIhTPPBIktpXDlcTWq09+nANDVMfJNnmze8N0MGhS+plBcbITCuHHQJ/LlExaLpQljVzTXkKVL4be/NeahtWvNWoRAeMxHnTtDyz7LyVs2skb1BtIUzj/fmJPOO69y+sGD4f33wwuD8dZbJhT1n/5UoyZaLJYmiI2SWgN27IBTTqkwHeXnB0/r0RTS06Hl4O8o2NyP7durX3cgn0KrVnDBBcZ/4M/gwWbD+VXBd/708sQTRkM4+eTqt89isTRNrFCoJoWFcPrpsGsX/M+Zb1WVUIiPN2/p6YO/BozZqbrs2WPWAySEObPVvVVmKBYsMFNRr702sHCxWCzRjf3ZV5NnnzWhql9+GX7zG3MulFDIzYW0NDOFMrbDMuJT99do1a87GF449O1rAtpVJRSeeMLMNrr00uq3zWKxNF2sUKgG5eXw5JNw5JEwcaJZGAYVC8UCsX+/MR0BFJcX0SJjHzk51W+DO8RFOCQkmHg9oWYgZWXBa6/BJZdUtNVisTQvrKO5Gnz8MaxZA//9rzmOizODblWaglcolBWTmJbP7t3B01eFOxheuAwaZMxDwXj2WTPzyE5DtViaL1ZTqAZPPGHCNP/2txXnUlKq9imkpZn/i0qLaJFWUGOhEImmAMbZvH594HaWlMC//w0nnGBiHVksluaJFQoRsnYtfPQRXHGFr5M3HKHg1hSS0wvrXSgMGmRmSq1YUfnazJkmbpKdhmqxNG+sUIiQp54yW1Ne+vsipi2cRll5GVC1UPA4msHsp5CUfqBGPoVIHc1QsflNIGfzE0+YPZhPOaX6bbJYLE0fKxQiIC8Ppk83QeVWFn3GFR9cwbwN84DINYXU9CLy881iskgpKzPlRSoUDjrITIn1dzYvXgxffml8CbE12/fHYrE0caxQiID33jOD8TXXQF5xHgArd60EIhMKRaVFpGSYLTk9i9AiwRPiIlJHc2ys8Rf4awpPPGHiI/3ud5G3xWKxRBdWKETAokXGjzBiBBwoPQDAil3GQJ+cHFwolJWZa2lpoKqUlJeQllECUC2/QqAQF+EyeLCvUMjJgVdegQsvhNatIy/PYrFEF1YoRMCyZdC/v5mCWlhaCISnKeQZpYL0dGM6AkhvVX2hECgYXrgMGlSx5wLA88+bfZitg9lisYBdpxARS5fCSCeOXWFJ+ELBHffIIxQyWhoHdUNoCgB/+ANkZpo9o487Dg4+OPKyLBZL9GGFQpjs3282sPHEEPKYj7bmbiW3KJeUlLSgQsETITUtzcw8ggqhUJ0ZSIGC4YXLiBFG2/nyS3McFwd33hl5ORaLJTqxQiFMli83fz1v2h7zEcCqnFWkpAwPS1MoKjVCoVVrE1q1vjWFNm0Cr1OwWCwWsD6FsPE4Zz1CwaMpAKzIXkFKiomcWl5eOa9bU/Caj9JjiI2tf6FgsVgsobBCIUyWLTMzjHr0MMeFJYWkxKcQFxPHyl0rvUHxCgsr5/XRFBzzUWJcAq1bV18oJCSYaaQWi8VSm1ihECZLl8LAgRV7DBwoPUBaYhq9W/dmZU6FUAhkQgrkaE6MS6y2UNi1y5iBRKrREYvFYgmBFQphsnRphekIjE+hRVwL+rfp76MpBBIKPo5mx6eQEJtAZmb1HM1ZWdCuXeT5LBaLpSqsUAiDnByz9aZn5hEYTSEpLon+mf1Zk7OGFklmNlEoTcHtU0iMrb6mkJ1thYLFYqkbrFAIA0+soGCaQkl5Cbm6AwguFFq0MH4Aj08hIbb6PgWrKVgslroiLKEgImNFZJWIrBWRyQGu3yIii5zPUhEpE5HW4eRtCgQUCiWFJMUn0b9NfwCyijcAwc1HngipteFTyMqCtm0jz2exWCxVUaVQEJFY4ClgHDAQOE9EBrrTqOrfVXWoqg4Fbge+UNXd4eRtCixdapzEnTtXnPOajxyhsKP4VyC4puAOhgcVmkJurtngJlzy883HagoWi6UuCEdTOAJYq6rrVLUYeA04PUT684D/VTNvo8TjZHbP9vGYjzJaZNAxtSNbD6wGgguFSpqC41OAyCKlZmebv1YoWCyWuiAcodAZ2Ow63uKcq4SIJANjgberkfdyEVkgIguyPSNfI0DVmI/cTmZwNIV4s1Cgf5v+bCwwS57dQqGkrITxr4xn6659FZpCme/sI4hsBpIVChaLpS4JRygEmg2vQdJOAL5WVY+lPOy8qjpNVYer6vC2jchgvnOnGbTd/gQwPoUWcS0AIxTW5i0GfIXC9rztfLT2I3bmFFYyH3l8ChCZXyEry/y1QsFisdQF4QiFLUBX13EXYFuQtJOoMB1FmrdREsjJDBU+BTBCYX+56VZBQUWaXQW7ACgsiK9kPvL4FKB6QqERyU2LxRJFhCMUfgT6iEhPEUnADPzv+ScSkQzgOODdSPM2ZjzB4wb6ucc9PgWAAW0GQNwBRNRHU8gpMHahA/kJlcxHbp+C1RQsFktjocooqapaKiLXAnOAWGC6qi4TkSud61OdpGcCH6tqflV5a7sTdUl2tnEw+7+ZuzWFLuldQCAxqZT8/HhvGo+mUFyQ6LM/M1RfU8jONjGYPCuoLRaLpTYJK3S2qs4CZvmdm+p3/ALwQjh5mxK7d5t9C9wb2quqj6O5bYqRGPEtiisLhbI4yooTvOYjt08hKd3EUorE0WwXrlkslrrErmiugt278c4S8uAJm+0xH7VOak2MxBCbWORrPirMgSIjDdyagiDESiwxMUS8gM0KBYvFUpdYoVAFu3dX3tDeIxQ85qMYiSEzKZOYxAIfobCrYBcUGWng1RTKikiMS0ScRQ/VEQrWyWyxWOoKKxSqICenslDw7Lrm0RQA2qW0g/j8ykKhuLKmkBib6E1jNQWLxdKYsEKhCkJqCvEVu9y0TWlLWVxeAPORkQbudQoJsQneNJEIBVUbIdVisdQtzUIolJWXUVZeVq28gYRCYUllTaFtcltKY/dVaT4qLismMc5XU3A7mq+7Dm68MXBb9u+H4mIrFCwWS93RLITC6a+dzp8++lPE+crKYO/eqn0KYIRCSeyeyusU/BzNRWXBNYXCQnj2WXjiCdiypXJ77BoFi8VS1zQLobBm9xpW5ayKON++fcZk4z/7KJBPoW1KW4pj9pCfXxHFw60ppKaVA46j2c+nsH+/iZQ6fz4cOGCE0VSfCb8Gu5rZYrHUNc1CKBSUFLC/aH/E+Txv8MHMRz4+heS2kJBPniMUCkoKKCwtJFnbAxDXwuQpLiv20RQ8AmfvXvjoI7MZz0knwbRpRkC4scHwLBZLXdNshEJuUW7E+Ty2/rDMRyltIT6fwgIz1dQT4iLDE/op0dRfVFpUyacARgB99BGMGgW33GIEwBtv+NZrzUcWi6WuaTZCoVY1hWBTUhPyKS0ViosrQlykaCcjLMrygMqagqfsBQtg9WoYNw7GjIEBA4xvQV0xZa35yGKx1DVRLxTKtZwDpQdqVSgEnJKabDQFMOGzPUIhqbwtJO73aiqBfAoAr75q/o4da2ItXXutERTff19Rb1aWCbmRUCFTLBaLpVaJeqFQUGJiWeeX5Ec8LbUqn4K/o5mECqGQU2jMR/ElmZC4n7zi0JrCnDnQqxf06WOOL77YzFh68smKeu1qZovFUtc0G6EAeAfmcPEIhVatfM8H8ilkJmVCvCOAXJqCFGdAQq637mA+hbIyYzrybPmZmgqTJsG775q1CWAXrlkslrqnWQmF3OLInM2BIqRCYJ9CbEwsaanmdubnVziayw+kGPORU7e/ptCyZYUgGDfOt57x4yEvD77+2hzbEBcWi6WuaVZCIVK/QqC4R1A5SqqHlukmbLZHU2jZoiWF+Qk+5iN/n0JMjNFEEhLMzCM3xx8P8fFmVhJYoWCxWOoeKxRCECjEBVTsz+yJdOqhdboREvn5sKtwF22S21CQFwuJuUF9CgAdOsDo0ZU3zklLg5EjYfZsY17atcsKBYvFUrdEvVDIL66IOxHpWoWgQsG1FaebNhnGx+AxH7VJbkN+Xozv7KNSX00B4PXXTXiLQIwbB7/8Yj7l5dbRbLFY6paoFwp1oSm4t+J0066ledX3mI8ykzLZv1+IaVHgaz6K8xUKgwdD166B2+DxM7z0klOH1RQsFksdEtZ2nE2ZUEJh0SKYObPieOhQOO30cr7f8j0HSg+we/foSnGPILim0L51KgC5ueXsKt7FoNaHUVICSclFQR3NVTFoEHTuDK+8Yo6tULBYLHVJsxIK/rOP/vpXeO+9iuO4Fgdoc18vduRvJ0bjYE8xrVv7+g0An/2Z3XRsbYLfZe8rIIcckoq6A9AizWgKqlppk52qEDHawnPPmWMrFCwWS13SrM1H69fDaaeZUBK/ueo1Sg+04LC08fzpiD9RfiCV8nIJ6Wj2p0umWdCwY89+CkoKKM/pBUB6xyzyivMoKS8BiEhTAN+pqlYoWCyWuqRZCQV/R/PGjdDdvMwTm7kegMkDn+Omo26CQiMNIvEptE9rA7EH2LprDwDF2cZR0KpTDrnFuRSVFgFU8ilUxZgxEBdntIZA7bFYLJbaIiyhICJjRWSViKwVkclB0owSkUUiskxEvnCd3yAivzjXFtRWw8Mlv8TMPmrZoqWPprB3r9nHwCMUYjLXAbBmDXTP6E5KaTcgstlHnqB42/cY4ZO7oz0JCZDZ0ZiPisvM0uRINYWMDDj6aGjTpvJCOovFYqlNqvQpiEgs8BRwIrAF+FFE3lPV5a40LYGngbGquklE/I0co1V1V+01O3wKSgqIi4kzM4GKK4TCxo3mr0colKavQ2JLWbs2DhGhZ4vDWEpwTaF1UuULnvDZ2XuNdpKzJZNevSCtRTLZe3ZQVOZoChH4FDz87W+wbl3E2SwWiyUiwtEUjgDWquo6VS0GXgNO90tzPvCOqm4CUNWs2m1m9SkoKSA5Ppm0xDQf85G/UCgo209S2x2sWWOOO8cdDEDLVuWVyiwsKQxoPspMyoSEfPbsNxrBzk2p9O4NqQmp5BblVltTABgxAs4/P+JsFovFEhHhCIXOwGbX8RbnnJu+QCsRmSciC0XkYtc1BT52zl8erBIRuVxEFojIgmzPFmO1gEcopCem+5iP/IVCXnEe6R2zWLvWHGdKXwByYzdUKjOY+Sg+Np7YxAPk5ZWDwuYNifTpA2kJaeQV51Xbp2CxWCz1RThCofKcTDPQu4kDhgGnACcDd4s4oyoco6qHAeOAa0Tk2ECVqOo0VR2uqsPb1uKy3YKSAlLiUyoJhQ0bICmpYoVwblEurTrnsHatmY2UWmakxcYDiyqVGczRDJDQohQtTobcjhQWSoWmUFwzTcFisVjqg3CEwhbAvd62C7AtQJrZqprv+A7mA4cAqOo2528WMANjjqo3vOajhDSfdQobN0K3bhURSvOK82jbdS95ebBzJ8QXtYfEffyy6+dKZQabkgqQmFQGJSmk5B4K4BUKB0oPeGdCVcenYLFYLPVBOELhR6CPiPQUkQRgEvCeX5p3gd+ISJyIJANHAitEJEVE0gBEJAU4CVhae82vmvyS/KDmox49zP+qSl5xHh27mplKa9fC/r1xxKfmsnjn4kplBlu8BpCcrFCcQnLuEACv+QgqNt6xmoLFYmmsVDn7SFVLReRaYA4QC0xX1WUicqVzfaqqrhCR2cASoBx4TlWXikgvYIYTTTQOeFVVZ9dVZ9xMnWr2OXb7FPwdzYcdZv4/UHqAMi2jSw8TEnvNGhP3KDWjpJJQKNdyisqKgmoKKSlASQpx+/oTH29iGqXuNuEvPHssWJ+CxWJprIQV5kJVZwGz/M5N9Tv+O/B3v3PrcMxI9Ul5Odx0k1mtXHB8AR1TO5KWkEZhaSElZSWUFMWTne3rZAbo2r2MuDijKezeDZmthbX7NrG7cLd3CqrHWRzMp5CWFgPFKeiug+jZ0yw6S0u0moLFYmkaROWK5vXrobDQbF/p1hTAxD/atMmk8wgFj68hIzmFHj2MUMjJgc7tzRv9kp1LvGUH2nXNTUZqHJQkU5Td1bvfcmqC0RR2F5r9Pa1PwWKxNFaiUigsdbwWWVnO7KOEFO/bem5RLhs2mOv+mkJqgllX4DEf9eiYAcDiHRUmJO/+zEF8Cq3SE6A0mdztHejdG2+5UGE+spqCxWJprESlUFi2zPzNyjKb7CTHVWgK+4v2B1yjAMYh3KePEQp79kCX9sm0T2nPop2LvGUXlhhNIZj5qHWG0QJKixK9QsHf0Wx9ChaLpbESlaGzPZrCrl2QUFToYz7yCIW4OOjUyaTzOKA9mkKekRG0bg2HtDvER1OoynzUtmWFsPA3H3mFgjUfWSyWRkpUagoeoVBeDgdyk7zrFMD4DzZuhC5dKoLL+ZuPPLRuDYe0P4Rl2csoKTNhr6syHx3UvqP3f2s+slgsTY2oEwolJbBqVYVpiPx2ATUFzxoFcJmPEtO8b/dghEKf1n0oLitme952oMJ8FNTRnGaUr7i4ijb4zz6y5iOLxdJYiTqhsHYtFBfD8cc7J/LbVXI0u/dRgIrZR6kJqXTvXqFBZGZC+9T2AOzM2wm4NIUgPoUUs02zdzoqQEq8OWk1BYvF0tiJOqHgcTKPHu2c8NMUduflsXWrr1BwO5oTEiqutW4N7VMcoZBvhEJVPoXkZPPXbYaKjYklOT7Zu7eD9SlYLJbGStQJhaVLTTyj445zTjhCweNT2LLFBLzz0RSKcomRGO9A7xnQW7cOoSkE8Sl4NAW3UIAKvwJAXExU+vctFksUEJVCoXdv6NwZRBQK2pIcn+x9W9++xZhu/DWF1IRUnHAcXr9Cq1YBNIUqpqSmOmO/2zcBFUIhMTbRW4/FYrE0NqLulXXZMhg0yPgFMlqXsNfRFADSE9PJ2my0AX+h4NEkAK64Anr1goQEgCTSEtIqaQrBzEd9+sAdd8A55/ie95Rv/QkWi6UxE1VCoajILDw7+2xznNG6qJJQyNluBueurmDgucW5Puadgw82Hw/tU9tX8ikEMx/FxsIDD1Q+79UU7Mwji8XSiIkq89GqVVBWBoMHm+O01gfM7CNn9k9aQhp7d6bTsSMkusbmvOI87+ykQLRPaV/JfBRMUwiGp3yrKVgslsZM1AgFVWXEg78HjPkIIKVlvtfRDEZTyN2Z6bNGASp8CsFon9q+kvko0hlEbp+CxWKxNFaiRiiICJI9BIkto6+zEWhSRp6PUEhLTKNgZ6dKM4P8zUf++GgKzv7MkTqLPeVbTcFisTRmokYoAMTuGkJqx62OgxiSMvbDgVbEqREKyWRSsqdjJaHg72j2p31Ke3YX7qakrCTk/syh8JRvfQoWi6UxE1VCoWR7PxI6rvEeJ6TvA6Bgn7OibHcvoPIagnDMRwBZ+Vkh92cOhdUULBZLUyBqhEJpKSS0KEU6VEQ0jUs3m9rszTEDcfGubkDlNQS5RVWbj8AIhQNlwfdnDoX1KVgslqZA1AiFuDi48N9/o3xkxXzQ2FQTayg729j/C3eaWNldexR505RrOfkl+aHNR6kVC9gKSwqt+chisUQtUSMUANqmtGV34W5Ky0vNieRswGy2A7B/ewdIyiEuJdebJ7/YxCMKR1PYmbeTA6UHrPnIYrFELVElFNoktwEq9kIm1UgDj1DYs7U1tF7D/qL93jzusNnB8NEUSgurZT7ylG/NRxaLpTETllAQkbEiskpE1orI5CBpRonIIhFZJiJfRJK3tmib3BaA7HyjIZTE70JiS8g2h2RvyYDWawMKhVCaQkp8CklxSezM22kdzRaLJaqpUiiISCzwFDAOGAicJyID/dK0BJ4GTlPVQcBvw81bm3g0hV0FuwAoLC0gLm03WVlw4ADs2p4MmWu822+C714KwRARb6iL6k5JtWEuLBZLUyAcTeEIYK2qrlPVYuA14HS/NOcD76jqJgBVzYogb63RNsXRFAqMalBQUkBixj6ysmD9elCVoJpCKEczVCxg8yxeixRvQLwYqylYLJbGSzhCoTOw2XW8xTnnpi/QSkTmichCEbk4grwAiMjlIrJARBZke+w9EeJvPiooKaBFei5ZWSZQHlAt8xFUhLo4UFrDKalWU7BYLI2YcIRCoHgO6nccBwwDTgFOBu4Wkb5h5jUnVaep6nBVHd62bdswmlWZzORMoMJ8lF+cT3LLfLKyzDadALRe4zUZAV5TUpVCwaMpVHNKqvUpWCyWpkA4obO3AK5A03QBtgVIs0tV84F8EZkPHBJm3lojITaBjMQMH/NRaqt8Niw0QqFlK2Vv8p6IZx+BEQq7CnaRHJ9cPfORnX1ksViaAOFoCj8CfUSkp4gkAJOA9/zSvAv8RkTiRCQZOBJYEWbeWqVtSlsfoZDW6gAFBbB4MfR1VjJH6mgGYz4q13LyivOqpSkkxSXRJrkNHdM6RpzXYrFY6osqNQVVLRWRa4E5QCwwXVWXiciVzvWpqrpCRGYDS4By4DlVXQoQKG8d9QUwM5A85qOCkgIyMs3q5QUL4OyzhRUJadXzKTgL2CDyvRTAzGBadvUyWrZoGXFei8ViqS/C2nlNVWcBs/zOTfU7/jvw93Dy1iVtk9uyad8mVJWCkgJaZZrVzcXFJhBeemJ6JaGQEJtQpa3fs4ANgu+6VhXtUtpVK5/FYrHUF1G1ohmMUNhVsIsDpQdQlMw2Zd5rffoY276/o7kqLQFqrilYLBZLUyDqhEKb5DZkF2STX2JiGrVpW+69FlBTKAm9l4IHH02hGj4Fi8ViaQpEnVBom9KW4rJi7/aZ7dpVzIrt3RtaJ7X2OqKh6r0UPGQkZnhNTFZTsFgs0UrUCQVPqItN+zYB0Co9gZQUaNkSMjOhd6verN29FlWzXCJc85GIeE1I1fUpWCwWS2Mn6oSCZ1Xzxn0bARPMrm1boyWIQN/Mvuwv2k9WvonEkVecV+UaBQ8eE5I1H1kslmglrNlHTQlP/COPppAcn8wZZ0CHDuZ638y+AKzKWUX71PbkFuf6+AtC4dEUrPnIYrFEK1EnFDzmI4+mkByfzL/+VXHdIxRW56zm2O7HGk0hDEczYM1HFosl6ola89GGvRsAIxTcdMvoRmJsIqtzVgPhO5qhwnxkNQWLxRKtRJ1QSE1IJTE20cd85CY2JpberXuzKmcVEL6jGVyagvUpWCyWKCXqhIKI0Ca5DdtyTdw9f6EAxoS0Omc1JWUlFJUVhW0+OqbbMQxqO4gu6V1qtc0Wi8XSWIg6oQDG2VyuZtFaSkJKpev9Mvvx6+5f2Ve0D6g67pGH4Z2Gs/TqpWHPVrJYLJamRnQKheSK/RiCaQol5SUszVoKVB0222KxWJoLUSkUPDOQBAm4f4FnBtLCbQuB8DUFi8ViiXaiUih4NIXk+GREKm/+5hUK261QsFgsFjdRKRQ8mkIg05HneqsWrfhp+08AYTuaLRaLJdqJSqHgWdUcyMkMZoaSZwYSWE3BYrFYPESnUHCZj4LRN7MvigmKZ4WCxWKxGKJSKFRlPgIzLdWDnX1ksVgshqgUCh7zUVWaggerKVgsFoshOoVCmOYjDynxgX0PFovF0tyISqHQOqk1goQUCn0y+wBGcMTGxNZX0ywWi6VRE3Whs8EEvWud1DqkUEiOT6ZreleKyorqsWUWi8XSuAlLUxCRsSKySkTWisjkANdHicg+EVnkfP7iurZBRH5xzi+ozcaH4v7j7+f3h/4+ZJq+mX2tP8FisVhcVKkpiEgs8BRwIrAF+FFE3lPV5X5Jv1TVU4MUM1pVd9WsqZFx5fArq0xz2zG3sT1vez20xmKxWJoG4ZiPjgDWquo6ABF5DTgd8BcKTY4TDzqxoZtgsVgsjYpwzEedgc2u4y3OOX+OEpHFIvKRiAxynVfgYxFZKCKXB6tERC4XkQUisiA7OzusxlssFouldglHU6gcUQ5nKXAFPwHdVTVPRMYDM4E+zrVjVHWbiLQD5orISlWdX6lA1WnANIDhw4f7l2+xWCyWeiAcTWEL0NV13AXY5k6gqvtVNc/5fxYQLyJtnONtzt8sYAbGHGWxWCyWRkg4QuFHoI+I9BSRBGAS8J47gYh0ECdGtYgc4ZSbIyIpIpLmnE8BTgKW1mYHLBaLxVJ7VGk+UtVSEbkWmAPEAtNVdZmIXOlcnwqcDVwlIqVAITBJVVVE2gMzHHkRB7yqqrPrqC8Wi8ViqSGi2vjM98OHD9cFC+ptSYPFYrE0eURkoaoOr2k5URnmwmKxWCzVwwoFi8VisXhplOYjEckGNlYzexugXldPNwKaY5+hefa7OfYZmme/I+1zd1VtW9NKG6VQqAkisqA27GpNiebYZ2ie/W6OfYbm2e+G6rM1H1ksFovFixUKFovFYvESjUJhWkM3oAFojn2G5tnv5thnaJ79bpA+R51PwWKxWCzVJxo1BYvFYrFUEysULBaLxeIlaoRCVVuGRgsi0lVEPheRFSKyTESud863FpG5IrLG+duqodta24hIrIj8LCIfOMfNoc8tReQtEVnpPPOjor3fInKj891eKiL/E5EW0dhnEZkuIlkistR1Lmg/ReR2Z3xbJSIn11W7okIouLYMHQcMBM4TkYEN26o6oxT4s6oOAEYA1zh9nQx8qqp9gE+d42jjemCF67g59PkxYLaq9gcOwfQ/avstIp2B64DhqjoYE4RzEtHZ5xeAsX7nAvbT+Y1PAgY5eZ52xr1aJyqEAq4tQ1W1GPBsGRp1qOp2Vf3J+T8XM0h0xvT3RSfZi8AZDdLAOkJEugCnAM+5Tkd7n9OBY4HnAVS1WFX3EuX9xkRUThKROCAZs39L1PXZ2Wxst9/pYP08HXhNVYtUdT2wljramyZahEK4W4ZGFSLSAzgU+B5or6rbwQgOoF0DNq0ueBS4FSh3nYv2PvcCsoH/OGaz55x9SaK236q6FfgHsAnYDuxT1Y+J4j77Eayf9TbGRYtQCGfL0KhCRFKBt4EbVHV/Q7enLhGRU4EsVV3Y0G2pZ+KAw4B/q+qhQD7RYTYJimNDPx3oCXQCUkTkwoZtVaOg3sa4aBEKVW4ZGk2ISDxGILyiqu84p3eKSEfnekcgq6HaVwccA5wmIhswpsHjReS/RHefwXyvt6jq987xWxghEc39PgFYr6rZqloCvAMcTXT32U2wftbbGBctQqHKLUOjBWfb0+eBFar6T9el94BLnP8vAd6t77bVFap6u6p2UdUemGf7mapeSBT3GUBVdwCbRaSfc2oMsJzo7vcmYISIJDvf9TEYv1k099lNsH6+B0wSkUQR6Qn0AX6okxaoalR8gPHAauBX4M6Gbk8d9nMkRm1cAixyPuOBTMxshTXO39YN3dY66v8o4APn/6jvMzAUWOA875lAq2jvN3APsBKzn/vLQGI09hn4H8ZvUoLRBH4fqp/Anc74tgoYV1ftsmEuLBaLxeIlWsxHFovFYqkFrFCwWCwWixcrFCwWi8XixQoFi8VisXixQsFisVgsXqxQsFgsFosXKxQsFovF4uX/AbW+aqZG8lZQAAAAAElFTkSuQmCC)

```
VGGish(
  (features): Sequential(
    (0): Conv2d(1, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (1): ReLU(inplace=True)
    (2): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
    (3): Conv2d(64, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (4): ReLU(inplace=True)
    (5): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
    (6): Conv2d(128, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (7): ReLU(inplace=True)
    (8): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (9): ReLU(inplace=True)
    (10): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
    (11): Conv2d(256, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (12): ReLU(inplace=True)
    (13): Conv2d(512, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (14): ReLU(inplace=True)
    (15): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
  )
  (embeddings): Sequential(
    (0): Linear(in_features=12288, out_features=4096, bias=True)
    (1): ReLU(inplace=True)
    (2): Linear(in_features=4096, out_features=4096, bias=True)
    (3): ReLU(inplace=True)
    (4): Linear(in_features=4096, out_features=128, bias=True)
    (5): ReLU(inplace=True)
  )
  (classfilter): Sequential(
    (0): Linear(in_features=128, out_features=64, bias=True)
    (1): Sigmoid()
    (2): Linear(in_features=64, out_features=5, bias=True)
    (3): Softmax(dim=1)
  )
)
Epoch 1/100
train Loss: 1.0870 Acc: 0.8708
valid Loss: 1.1348 Acc: 0.7824
Epoch 2/100
train Loss: 1.0768 Acc: 0.8708
valid Loss: 1.1258 Acc: 0.7941
Epoch 3/100
train Loss: 1.0683 Acc: 0.8788
valid Loss: 1.1184 Acc: 0.8000
Epoch 4/100
train Loss: 1.0621 Acc: 0.8804
valid Loss: 1.1135 Acc: 0.7941
Epoch 5/100
train Loss: 1.0551 Acc: 0.8836
valid Loss: 1.1096 Acc: 0.7941
Epoch 6/100
train Loss: 1.0510 Acc: 0.8852
valid Loss: 1.1084 Acc: 0.8118
Epoch 7/100
train Loss: 1.0475 Acc: 0.8836
valid Loss: 1.1028 Acc: 0.8000
Epoch 8/100
train Loss: 1.0441 Acc: 0.8884
valid Loss: 1.0999 Acc: 0.8059
Epoch 9/100
train Loss: 1.0411 Acc: 0.8884
valid Loss: 1.0974 Acc: 0.8176
Epoch 10/100
train Loss: 1.0387 Acc: 0.8900
valid Loss: 1.0963 Acc: 0.8059
Epoch 11/100
train Loss: 1.0369 Acc: 0.8868
valid Loss: 1.0931 Acc: 0.8176
Epoch 12/100
train Loss: 1.0345 Acc: 0.8884
valid Loss: 1.0912 Acc: 0.8176
Epoch 13/100
train Loss: 1.0331 Acc: 0.8900
valid Loss: 1.0904 Acc: 0.8412
Epoch 14/100
train Loss: 1.0319 Acc: 0.8915
valid Loss: 1.0880 Acc: 0.8235
Epoch 15/100
train Loss: 1.0304 Acc: 0.8915
valid Loss: 1.0871 Acc: 0.8471
Epoch 16/100
train Loss: 1.0294 Acc: 0.8868
valid Loss: 1.0851 Acc: 0.8176
Epoch 17/100
train Loss: 1.0284 Acc: 0.8884
valid Loss: 1.0850 Acc: 0.8176
Epoch 18/100
train Loss: 1.0271 Acc: 0.8931
valid Loss: 1.0829 Acc: 0.8353
Epoch 19/100
train Loss: 1.0264 Acc: 0.8900
valid Loss: 1.0822 Acc: 0.8235
Epoch 20/100
train Loss: 1.0254 Acc: 0.8884
valid Loss: 1.0811 Acc: 0.8471
Epoch 21/100
train Loss: 1.0239 Acc: 0.8947
valid Loss: 1.0806 Acc: 0.8235
Epoch 22/100
train Loss: 1.0241 Acc: 0.8931
valid Loss: 1.0798 Acc: 0.8294
Epoch 23/100
train Loss: 1.0234 Acc: 0.8884
valid Loss: 1.0789 Acc: 0.8353
Epoch 24/100
train Loss: 1.0227 Acc: 0.8963
valid Loss: 1.0782 Acc: 0.8353
Epoch 25/100
train Loss: 1.0221 Acc: 0.8900
valid Loss: 1.0777 Acc: 0.8412
Epoch 26/100
train Loss: 1.0211 Acc: 0.8963
valid Loss: 1.0775 Acc: 0.8353
Epoch 27/100
train Loss: 1.0208 Acc: 0.8947
valid Loss: 1.0792 Acc: 0.8176
Epoch 28/100
train Loss: 1.0202 Acc: 0.8947
valid Loss: 1.0780 Acc: 0.8118
Epoch 29/100
train Loss: 1.0207 Acc: 0.8963
valid Loss: 1.0759 Acc: 0.8412
Epoch 30/100
train Loss: 1.0196 Acc: 0.8947
valid Loss: 1.0758 Acc: 0.8353
Epoch 31/100
train Loss: 1.0193 Acc: 0.8915
valid Loss: 1.0756 Acc: 0.8353
Epoch 32/100
train Loss: 1.0188 Acc: 0.8931
valid Loss: 1.0758 Acc: 0.8353
Epoch 33/100
train Loss: 1.0185 Acc: 0.8963
valid Loss: 1.0752 Acc: 0.8353
Epoch 34/100
train Loss: 1.0179 Acc: 0.8947
valid Loss: 1.0750 Acc: 0.8353
Epoch 35/100
train Loss: 1.0177 Acc: 0.8931
valid Loss: 1.0745 Acc: 0.8471
Epoch 36/100
train Loss: 1.0168 Acc: 0.8963
valid Loss: 1.0755 Acc: 0.8235
Epoch 37/100
train Loss: 1.0169 Acc: 0.8979
valid Loss: 1.0744 Acc: 0.8529
Epoch 38/100
train Loss: 1.0168 Acc: 0.8947
valid Loss: 1.0745 Acc: 0.8529
Epoch 39/100
train Loss: 1.0166 Acc: 0.8963
valid Loss: 1.0736 Acc: 0.8471
Epoch 40/100
train Loss: 1.0161 Acc: 0.8947
valid Loss: 1.0735 Acc: 0.8471
Epoch 41/100
train Loss: 1.0160 Acc: 0.8963
valid Loss: 1.0737 Acc: 0.8353
Epoch 42/100
train Loss: 1.0157 Acc: 0.8979
valid Loss: 1.0731 Acc: 0.8471
Epoch 43/100
train Loss: 1.0157 Acc: 0.8947
valid Loss: 1.0730 Acc: 0.8471
Epoch 44/100
train Loss: 1.0151 Acc: 0.8963
valid Loss: 1.0727 Acc: 0.8471
Epoch 45/100
train Loss: 1.0149 Acc: 0.8963
valid Loss: 1.0727 Acc: 0.8471
Epoch 46/100
train Loss: 1.0151 Acc: 0.8947
valid Loss: 1.0726 Acc: 0.8471
Epoch 47/100
train Loss: 1.0145 Acc: 0.8995
valid Loss: 1.0726 Acc: 0.8471
Epoch 48/100
train Loss: 1.0145 Acc: 0.8963
valid Loss: 1.0725 Acc: 0.8471
Epoch 49/100
train Loss: 1.0138 Acc: 0.8947
valid Loss: 1.0728 Acc: 0.8353
Epoch 50/100
train Loss: 1.0143 Acc: 0.8947
valid Loss: 1.0723 Acc: 0.8471
Epoch 51/100
train Loss: 1.0139 Acc: 0.8963
valid Loss: 1.0721 Acc: 0.8412
Epoch 52/100
train Loss: 1.0135 Acc: 0.8931
valid Loss: 1.0719 Acc: 0.8471
Epoch 53/100
train Loss: 1.0138 Acc: 0.8963
valid Loss: 1.0719 Acc: 0.8471
Epoch 54/100
train Loss: 1.0134 Acc: 0.8947
valid Loss: 1.0716 Acc: 0.8471
Epoch 55/100
train Loss: 1.0132 Acc: 0.8947
valid Loss: 1.0716 Acc: 0.8471
Epoch 56/100
train Loss: 1.0131 Acc: 0.8963
valid Loss: 1.0712 Acc: 0.8471
Epoch 57/100
train Loss: 1.0121 Acc: 0.8995
valid Loss: 1.0727 Acc: 0.8353
Epoch 58/100
train Loss: 1.0132 Acc: 0.8931
valid Loss: 1.0719 Acc: 0.8294
Epoch 59/100
train Loss: 1.0124 Acc: 0.8979
valid Loss: 1.0710 Acc: 0.8471
Epoch 60/100
train Loss: 1.0126 Acc: 0.8947
valid Loss: 1.0709 Acc: 0.8471
Epoch 61/100
train Loss: 1.0123 Acc: 0.8963
valid Loss: 1.0710 Acc: 0.8471
Epoch 62/100
train Loss: 1.0123 Acc: 0.8947
valid Loss: 1.0707 Acc: 0.8471
Epoch 63/100
train Loss: 1.0119 Acc: 0.8963
valid Loss: 1.0706 Acc: 0.8471
Epoch 64/100
train Loss: 1.0122 Acc: 0.8979
valid Loss: 1.0706 Acc: 0.8471
Epoch 65/100
train Loss: 1.0115 Acc: 0.8979
valid Loss: 1.0714 Acc: 0.8471
Epoch 66/100
train Loss: 1.0121 Acc: 0.8963
valid Loss: 1.0704 Acc: 0.8529
Epoch 67/100
train Loss: 1.0118 Acc: 0.8963
valid Loss: 1.0705 Acc: 0.8412
Epoch 68/100
train Loss: 1.0111 Acc: 0.8979
valid Loss: 1.0702 Acc: 0.8529
Epoch 69/100
train Loss: 1.0112 Acc: 0.8979
valid Loss: 1.0698 Acc: 0.8471
Epoch 70/100
train Loss: 1.0112 Acc: 0.8979
valid Loss: 1.0705 Acc: 0.8471
Epoch 71/100
train Loss: 1.0114 Acc: 0.8995
valid Loss: 1.0699 Acc: 0.8471
Epoch 72/100
train Loss: 1.0113 Acc: 0.8947
valid Loss: 1.0700 Acc: 0.8471
Epoch 73/100
train Loss: 1.0105 Acc: 0.8979
valid Loss: 1.0708 Acc: 0.8353
Epoch 74/100
train Loss: 1.0110 Acc: 0.8979
valid Loss: 1.0699 Acc: 0.8471
Epoch 75/100
train Loss: 1.0107 Acc: 0.8979
valid Loss: 1.0699 Acc: 0.8471
Epoch 76/100
train Loss: 1.0107 Acc: 0.8947
valid Loss: 1.0702 Acc: 0.8471
Epoch 77/100
train Loss: 1.0105 Acc: 0.8963
valid Loss: 1.0700 Acc: 0.8471
Epoch 78/100
train Loss: 1.0104 Acc: 0.8979
valid Loss: 1.0699 Acc: 0.8471
Epoch 79/100
train Loss: 1.0105 Acc: 0.8963
valid Loss: 1.0700 Acc: 0.8471
Epoch 80/100
train Loss: 1.0105 Acc: 0.8963
valid Loss: 1.0696 Acc: 0.8471
Epoch 81/100
train Loss: 1.0101 Acc: 0.8979
valid Loss: 1.0699 Acc: 0.8529
Epoch 82/100
train Loss: 1.0101 Acc: 0.8963
valid Loss: 1.0697 Acc: 0.8471
Epoch 83/100
train Loss: 1.0101 Acc: 0.8979
valid Loss: 1.0699 Acc: 0.8471
Epoch 84/100
train Loss: 1.0099 Acc: 0.8979
valid Loss: 1.0701 Acc: 0.8471
Epoch 85/100
train Loss: 1.0099 Acc: 0.8963
valid Loss: 1.0697 Acc: 0.8412
Epoch 86/100
train Loss: 1.0099 Acc: 0.8963
valid Loss: 1.0698 Acc: 0.8471
Epoch 87/100
train Loss: 1.0100 Acc: 0.8963
valid Loss: 1.0700 Acc: 0.8471
Epoch 88/100
train Loss: 1.0098 Acc: 0.8979
valid Loss: 1.0698 Acc: 0.8471
Epoch 89/100
train Loss: 1.0098 Acc: 0.8963
valid Loss: 1.0694 Acc: 0.8471
Epoch 90/100
train Loss: 1.0098 Acc: 0.8931
valid Loss: 1.0701 Acc: 0.8471
Epoch 91/100
train Loss: 1.0095 Acc: 0.8915
valid Loss: 1.0704 Acc: 0.8353
Epoch 92/100
train Loss: 1.0096 Acc: 0.8963
valid Loss: 1.0702 Acc: 0.8412
Epoch 93/100
train Loss: 1.0098 Acc: 0.8963
valid Loss: 1.0698 Acc: 0.8471
Epoch 94/100
train Loss: 1.0093 Acc: 0.8947
valid Loss: 1.0694 Acc: 0.8471
Epoch 95/100
train Loss: 1.0093 Acc: 0.8963
valid Loss: 1.0694 Acc: 0.8471
Epoch 96/100
train Loss: 1.0094 Acc: 0.8947
valid Loss: 1.0695 Acc: 0.8471
Epoch 97/100
train Loss: 1.0088 Acc: 0.8979
valid Loss: 1.0694 Acc: 0.8529
Epoch 98/100
train Loss: 1.0093 Acc: 0.8979
valid Loss: 1.0692 Acc: 0.8588
Epoch 99/100
train Loss: 1.0092 Acc: 0.8963
valid Loss: 1.0696 Acc: 0.8471
Epoch 100/100
train Loss: 1.0090 Acc: 0.8979
valid Loss: 1.0696 Acc: 0.8471
```

![img](data:image/png;base64,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)

```
VGGish(
  (features): Sequential(
    (0): Conv2d(1, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (1): ReLU(inplace=True)
    (2): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
    (3): Conv2d(64, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (4): ReLU(inplace=True)
    (5): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
    (6): Conv2d(128, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (7): ReLU(inplace=True)
    (8): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (9): ReLU(inplace=True)
    (10): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
    (11): Conv2d(256, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (12): ReLU(inplace=True)
    (13): Conv2d(512, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (14): ReLU(inplace=True)
    (15): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
  )
  (embeddings): Sequential(
    (0): Linear(in_features=12288, out_features=4096, bias=True)
    (1): ReLU(inplace=True)
    (2): Linear(in_features=4096, out_features=4096, bias=True)
    (3): ReLU(inplace=True)
    (4): Linear(in_features=4096, out_features=128, bias=True)
    (5): ReLU(inplace=True)
  )
  (classfilter): Sequential(
    (0): Linear(in_features=128, out_features=64, bias=True)
    (1): Sigmoid()
    (2): Linear(in_features=64, out_features=5, bias=True)
    (3): Softmax(dim=1)
  )
)
Epoch 1/100
train Loss: 1.0153 Acc: 0.8915
valid Loss: 1.0763 Acc: 0.8353
Epoch 2/100
train Loss: 1.0115 Acc: 0.8995
valid Loss: 1.0723 Acc: 0.8353
Epoch 3/100
train Loss: 1.0106 Acc: 0.8963
valid Loss: 1.1253 Acc: 0.7706
Epoch 4/100
train Loss: 1.0139 Acc: 0.8931
valid Loss: 1.0781 Acc: 0.8176
Epoch 5/100
train Loss: 1.0137 Acc: 0.8931
valid Loss: 1.0701 Acc: 0.8294
Epoch 6/100
train Loss: 1.0160 Acc: 0.8868
valid Loss: 1.0740 Acc: 0.8235
Epoch 7/100
train Loss: 1.0121 Acc: 0.8963
valid Loss: 1.0791 Acc: 0.8176
Epoch 8/100
train Loss: 1.0131 Acc: 0.8915
valid Loss: 1.0780 Acc: 0.8294
Epoch 9/100
train Loss: 1.0102 Acc: 0.8947
valid Loss: 1.0700 Acc: 0.8471
Epoch 10/100
train Loss: 1.0116 Acc: 0.8915
valid Loss: 1.1027 Acc: 0.7882
Epoch 11/100
train Loss: 1.0097 Acc: 0.8979
valid Loss: 1.0851 Acc: 0.8059
Epoch 12/100
train Loss: 1.0102 Acc: 0.8947
valid Loss: 1.0850 Acc: 0.8118
Epoch 13/100
train Loss: 1.0080 Acc: 0.8979
valid Loss: 1.1394 Acc: 0.7588
Epoch 14/100
train Loss: 1.0133 Acc: 0.8931
valid Loss: 1.0719 Acc: 0.8235
Epoch 15/100
train Loss: 1.0098 Acc: 0.8947
valid Loss: 1.0718 Acc: 0.8471
Epoch 16/100
train Loss: 1.0095 Acc: 0.8915
valid Loss: 1.0896 Acc: 0.8176
Epoch 17/100
train Loss: 1.0108 Acc: 0.8931
valid Loss: 1.0805 Acc: 0.8118
Epoch 18/100
train Loss: 1.0113 Acc: 0.8931
valid Loss: 1.0697 Acc: 0.8412
Epoch 19/100
train Loss: 1.0106 Acc: 0.8947
valid Loss: 1.0789 Acc: 0.8235
Epoch 20/100
train Loss: 1.0095 Acc: 0.8963
valid Loss: 1.0666 Acc: 0.8471
Epoch 21/100
train Loss: 1.0107 Acc: 0.8963
valid Loss: 1.0703 Acc: 0.8353
Epoch 22/100
train Loss: 1.0084 Acc: 0.8995
valid Loss: 1.0698 Acc: 0.8353
Epoch 23/100
train Loss: 1.0092 Acc: 0.8963
valid Loss: 1.0652 Acc: 0.8471
Epoch 24/100
train Loss: 1.0078 Acc: 0.8979
valid Loss: 1.0856 Acc: 0.8118
Epoch 25/100
train Loss: 1.0074 Acc: 0.8963
valid Loss: 1.0596 Acc: 0.8529
Epoch 26/100
train Loss: 1.0066 Acc: 0.8979
valid Loss: 1.0783 Acc: 0.8176
Epoch 27/100
train Loss: 1.0060 Acc: 0.9027
valid Loss: 1.0826 Acc: 0.8118
Epoch 28/100
train Loss: 1.0088 Acc: 0.8947
valid Loss: 1.0766 Acc: 0.8235
Epoch 29/100
train Loss: 1.0058 Acc: 0.8995
valid Loss: 1.0683 Acc: 0.8353
Epoch 30/100
train Loss: 1.0106 Acc: 0.8915
valid Loss: 1.0796 Acc: 0.8176
Epoch 31/100
train Loss: 1.0086 Acc: 0.8915
valid Loss: 1.0796 Acc: 0.8235
Epoch 32/100
train Loss: 1.0104 Acc: 0.8900
valid Loss: 1.0877 Acc: 0.8118
Epoch 33/100
train Loss: 1.0075 Acc: 0.8979
valid Loss: 1.0574 Acc: 0.8529
Epoch 34/100
train Loss: 1.0086 Acc: 0.8963
valid Loss: 1.0575 Acc: 0.8471
Epoch 35/100
train Loss: 1.0065 Acc: 0.8979
valid Loss: 1.0603 Acc: 0.8471
Epoch 36/100
train Loss: 1.0062 Acc: 0.8995
valid Loss: 1.0656 Acc: 0.8529
Epoch 37/100
train Loss: 1.0063 Acc: 0.8979
valid Loss: 1.0529 Acc: 0.8647
Epoch 38/100
train Loss: 1.0048 Acc: 0.9027
valid Loss: 1.0542 Acc: 0.8588
Epoch 39/100
train Loss: 1.0062 Acc: 0.8979
valid Loss: 1.0507 Acc: 0.8647
Epoch 40/100
train Loss: 1.0094 Acc: 0.8915
valid Loss: 1.0545 Acc: 0.8529
Epoch 41/100
train Loss: 1.0058 Acc: 0.8979
valid Loss: 1.0550 Acc: 0.8588
Epoch 42/100
train Loss: 1.0054 Acc: 0.8979
valid Loss: 1.0525 Acc: 0.8588
Epoch 43/100
train Loss: 1.0055 Acc: 0.8979
valid Loss: 1.0762 Acc: 0.8176
Epoch 44/100
train Loss: 1.0054 Acc: 0.9011
valid Loss: 1.0510 Acc: 0.8647
Epoch 45/100
train Loss: 1.0042 Acc: 0.8995
valid Loss: 1.0547 Acc: 0.8529
Epoch 46/100
train Loss: 1.0055 Acc: 0.8995
valid Loss: 1.0594 Acc: 0.8412
Epoch 47/100
train Loss: 1.0049 Acc: 0.9011
valid Loss: 1.0568 Acc: 0.8471
Epoch 48/100
train Loss: 1.0051 Acc: 0.8995
valid Loss: 1.0618 Acc: 0.8412
Epoch 49/100
train Loss: 1.0035 Acc: 0.9059
valid Loss: 1.0521 Acc: 0.8588
Epoch 50/100
train Loss: 1.0024 Acc: 0.9043
valid Loss: 1.0903 Acc: 0.8176
Epoch 51/100
train Loss: 1.0054 Acc: 0.8995
valid Loss: 1.0657 Acc: 0.8353
Epoch 52/100
train Loss: 1.0033 Acc: 0.9011
valid Loss: 1.0534 Acc: 0.8529
Epoch 53/100
train Loss: 1.0030 Acc: 0.9011
valid Loss: 1.1012 Acc: 0.7941
Epoch 54/100
train Loss: 1.0069 Acc: 0.8963
valid Loss: 1.0552 Acc: 0.8588
Epoch 55/100
train Loss: 1.0052 Acc: 0.8995
valid Loss: 1.0719 Acc: 0.8235
Epoch 56/100
train Loss: 1.0041 Acc: 0.9011
valid Loss: 1.0538 Acc: 0.8529
Epoch 57/100
train Loss: 1.0069 Acc: 0.8979
valid Loss: 1.0549 Acc: 0.8471
Epoch 58/100
train Loss: 1.0035 Acc: 0.8995
valid Loss: 1.0566 Acc: 0.8529
Epoch 59/100
train Loss: 1.0054 Acc: 0.8995
valid Loss: 1.0506 Acc: 0.8588
Epoch 60/100
train Loss: 1.0043 Acc: 0.8995
valid Loss: 1.0516 Acc: 0.8588
Epoch 61/100
train Loss: 1.0022 Acc: 0.9027
valid Loss: 1.0863 Acc: 0.8059
Epoch 62/100
train Loss: 1.0044 Acc: 0.8995
valid Loss: 1.0528 Acc: 0.8529
Epoch 63/100
train Loss: 1.0022 Acc: 0.9043
valid Loss: 1.0600 Acc: 0.8471
Epoch 64/100
train Loss: 1.0052 Acc: 0.8995
valid Loss: 1.0498 Acc: 0.8647
Epoch 65/100
train Loss: 1.0043 Acc: 0.8995
valid Loss: 1.0527 Acc: 0.8529
Epoch 66/100
train Loss: 1.0028 Acc: 0.9027
valid Loss: 1.0626 Acc: 0.8471
Epoch 67/100
train Loss: 1.0029 Acc: 0.9011
valid Loss: 1.0520 Acc: 0.8588
Epoch 68/100
train Loss: 1.0022 Acc: 0.9027
valid Loss: 1.0833 Acc: 0.8059
Epoch 69/100
train Loss: 1.0055 Acc: 0.8979
valid Loss: 1.0616 Acc: 0.8529
Epoch 70/100
train Loss: 1.0048 Acc: 0.8979
valid Loss: 1.0596 Acc: 0.8529
Epoch 71/100
train Loss: 1.0034 Acc: 0.8995
valid Loss: 1.0489 Acc: 0.8647
Epoch 72/100
train Loss: 1.0058 Acc: 0.8979
valid Loss: 1.0498 Acc: 0.8706
Epoch 73/100
train Loss: 1.0063 Acc: 0.8963
valid Loss: 1.0475 Acc: 0.8588
Epoch 74/100
train Loss: 1.0022 Acc: 0.9011
valid Loss: 1.0473 Acc: 0.8588
Epoch 75/100
train Loss: 1.0022 Acc: 0.9027
valid Loss: 1.0662 Acc: 0.8353
Epoch 76/100
train Loss: 1.0048 Acc: 0.8995
valid Loss: 1.0620 Acc: 0.8412
Epoch 77/100
train Loss: 1.0043 Acc: 0.8995
valid Loss: 1.0631 Acc: 0.8471
Epoch 78/100
train Loss: 1.0039 Acc: 0.8995
valid Loss: 1.0495 Acc: 0.8647
Epoch 79/100
train Loss: 1.0019 Acc: 0.9043
valid Loss: 1.0514 Acc: 0.8588
Epoch 80/100
train Loss: 1.0045 Acc: 0.9011
valid Loss: 1.0644 Acc: 0.8412
Epoch 81/100
train Loss: 1.0034 Acc: 0.9027
valid Loss: 1.0662 Acc: 0.8412
Epoch 82/100
train Loss: 1.0036 Acc: 0.8995
valid Loss: 1.0504 Acc: 0.8529
Epoch 83/100
train Loss: 1.0030 Acc: 0.9027
valid Loss: 1.0522 Acc: 0.8588
Epoch 84/100
train Loss: 1.0037 Acc: 0.9011
valid Loss: 1.0515 Acc: 0.8647
Epoch 85/100
train Loss: 1.0031 Acc: 0.9011
valid Loss: 1.0488 Acc: 0.8588
Epoch 86/100
train Loss: 1.0031 Acc: 0.9011
valid Loss: 1.0511 Acc: 0.8588
Epoch 87/100
train Loss: 1.0039 Acc: 0.8995
valid Loss: 1.0554 Acc: 0.8471
Epoch 88/100
train Loss: 1.0031 Acc: 0.9011
valid Loss: 1.0538 Acc: 0.8529
Epoch 89/100
train Loss: 1.0029 Acc: 0.9027
valid Loss: 1.0567 Acc: 0.8529
Epoch 90/100
train Loss: 1.0023 Acc: 0.9027
valid Loss: 1.0525 Acc: 0.8529
Epoch 91/100
train Loss: 1.0034 Acc: 0.9011
valid Loss: 1.0545 Acc: 0.8471
Epoch 92/100
train Loss: 1.0044 Acc: 0.8995
valid Loss: 1.0531 Acc: 0.8471
Epoch 93/100
train Loss: 1.0025 Acc: 0.9027
valid Loss: 1.0596 Acc: 0.8471
Epoch 94/100
train Loss: 1.0034 Acc: 0.8995
valid Loss: 1.0532 Acc: 0.8471
Epoch 95/100
train Loss: 1.0032 Acc: 0.9011
valid Loss: 1.0534 Acc: 0.8471
Epoch 96/100
train Loss: 1.0038 Acc: 0.9011
valid Loss: 1.0578 Acc: 0.8471
Epoch 97/100
train Loss: 1.0034 Acc: 0.9027
valid Loss: 1.0554 Acc: 0.8471
Epoch 98/100
train Loss: 1.0035 Acc: 0.8995
valid Loss: 1.0524 Acc: 0.8529
Epoch 99/100
train Loss: 1.0031 Acc: 0.9011
valid Loss: 1.0521 Acc: 0.8529
Epoch 100/100
train Loss: 1.0044 Acc: 0.8995
valid Loss: 1.0574 Acc: 0.8471
```

![img](data:image/png;base64,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)

```
VGGish(
  (features): Sequential(
    (0): Conv2d(1, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (1): ReLU(inplace=True)
    (2): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
    (3): Conv2d(64, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (4): ReLU(inplace=True)
    (5): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
    (6): Conv2d(128, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (7): ReLU(inplace=True)
    (8): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (9): ReLU(inplace=True)
    (10): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
    (11): Conv2d(256, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (12): ReLU(inplace=True)
    (13): Conv2d(512, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (14): ReLU(inplace=True)
    (15): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
  )
  (embeddings): Sequential(
    (0): Linear(in_features=12288, out_features=4096, bias=True)
    (1): ReLU(inplace=True)
    (2): Linear(in_features=4096, out_features=4096, bias=True)
    (3): ReLU(inplace=True)
    (4): Linear(in_features=4096, out_features=128, bias=True)
    (5): ReLU(inplace=True)
  )
  (classfilter): Sequential(
    (0): Linear(in_features=128, out_features=64, bias=True)
    (1): Sigmoid()
    (2): Linear(in_features=64, out_features=5, bias=True)
    (3): Softmax(dim=1)
  )
)
Epoch 1/100
train Loss: 1.0285 Acc: 0.8804
valid Loss: 1.2175 Acc: 0.6824
Epoch 2/100
train Loss: 1.0740 Acc: 0.8309
valid Loss: 1.3337 Acc: 0.5706
Epoch 3/100
train Loss: 1.0539 Acc: 0.8549
valid Loss: 1.1045 Acc: 0.8000
Epoch 4/100
train Loss: 1.0311 Acc: 0.8708
valid Loss: 1.0796 Acc: 0.8294
Epoch 5/100
train Loss: 1.0284 Acc: 0.8772
valid Loss: 1.0815 Acc: 0.8235
Epoch 6/100
train Loss: 1.0151 Acc: 0.8884
valid Loss: 1.0938 Acc: 0.8118
Epoch 7/100
train Loss: 1.0194 Acc: 0.8852
valid Loss: 1.1609 Acc: 0.7412
Epoch 8/100
train Loss: 1.0327 Acc: 0.8724
valid Loss: 1.1169 Acc: 0.7824
Epoch 9/100
train Loss: 1.0255 Acc: 0.8788
valid Loss: 1.0873 Acc: 0.8176
Epoch 10/100
train Loss: 1.0338 Acc: 0.8708
valid Loss: 1.0844 Acc: 0.8176
Epoch 11/100
train Loss: 1.0110 Acc: 0.8931
valid Loss: 1.1016 Acc: 0.8000
Epoch 12/100
train Loss: 1.0175 Acc: 0.8852
valid Loss: 1.0965 Acc: 0.8059
Epoch 13/100
train Loss: 1.0130 Acc: 0.8931
valid Loss: 1.1114 Acc: 0.7941
Epoch 14/100
train Loss: 1.0108 Acc: 0.8931
valid Loss: 1.0983 Acc: 0.8059
Epoch 15/100
train Loss: 1.0185 Acc: 0.8852
valid Loss: 1.0747 Acc: 0.8294
Epoch 16/100
train Loss: 1.0115 Acc: 0.8931
valid Loss: 1.0685 Acc: 0.8353
Epoch 17/100
train Loss: 1.0273 Acc: 0.8740
valid Loss: 1.0730 Acc: 0.8353
Epoch 18/100
train Loss: 1.0108 Acc: 0.8947
valid Loss: 1.0858 Acc: 0.8176
Epoch 19/100
train Loss: 1.0104 Acc: 0.8947
valid Loss: 1.0787 Acc: 0.8235
Epoch 20/100
train Loss: 1.0057 Acc: 0.8995
valid Loss: 1.0728 Acc: 0.8294
Epoch 21/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0723 Acc: 0.8294
Epoch 22/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0722 Acc: 0.8294
Epoch 23/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0721 Acc: 0.8294
Epoch 24/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0721 Acc: 0.8294
Epoch 25/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0719 Acc: 0.8294
Epoch 26/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0718 Acc: 0.8294
Epoch 27/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0717 Acc: 0.8294
Epoch 28/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0716 Acc: 0.8294
Epoch 29/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0714 Acc: 0.8294
Epoch 30/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0713 Acc: 0.8294
Epoch 31/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0711 Acc: 0.8294
Epoch 32/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0710 Acc: 0.8294
Epoch 33/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0708 Acc: 0.8294
Epoch 34/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0708 Acc: 0.8294
Epoch 35/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0708 Acc: 0.8294
Epoch 36/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0707 Acc: 0.8294
Epoch 37/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0707 Acc: 0.8294
Epoch 38/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0707 Acc: 0.8353
Epoch 39/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0706 Acc: 0.8353
Epoch 40/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0705 Acc: 0.8294
Epoch 41/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0704 Acc: 0.8294
Epoch 42/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0704 Acc: 0.8294
Epoch 43/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0704 Acc: 0.8353
Epoch 44/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0703 Acc: 0.8294
Epoch 45/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0703 Acc: 0.8353
Epoch 46/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0702 Acc: 0.8353
Epoch 47/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0700 Acc: 0.8412
Epoch 48/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0699 Acc: 0.8353
Epoch 49/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0699 Acc: 0.8353
Epoch 50/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0699 Acc: 0.8412
Epoch 51/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0703 Acc: 0.8353
Epoch 52/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0702 Acc: 0.8353
Epoch 53/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0703 Acc: 0.8353
Epoch 54/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0704 Acc: 0.8353
Epoch 55/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0704 Acc: 0.8353
Epoch 56/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0703 Acc: 0.8353
Epoch 57/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0703 Acc: 0.8353
Epoch 58/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0702 Acc: 0.8353
Epoch 59/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0701 Acc: 0.8353
Epoch 60/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0701 Acc: 0.8353
Epoch 61/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0699 Acc: 0.8353
Epoch 62/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0699 Acc: 0.8353
Epoch 63/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0699 Acc: 0.8353
Epoch 64/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0698 Acc: 0.8353
Epoch 65/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0697 Acc: 0.8412
Epoch 66/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0697 Acc: 0.8412
Epoch 67/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0696 Acc: 0.8412
Epoch 68/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0696 Acc: 0.8412
Epoch 69/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0695 Acc: 0.8412
Epoch 70/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0700 Acc: 0.8353
Epoch 71/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0699 Acc: 0.8353
Epoch 72/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0698 Acc: 0.8353
Epoch 73/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0699 Acc: 0.8353
Epoch 74/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0699 Acc: 0.8353
Epoch 75/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0700 Acc: 0.8353
Epoch 76/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0699 Acc: 0.8353
Epoch 77/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0698 Acc: 0.8353
Epoch 78/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0697 Acc: 0.8353
Epoch 79/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0696 Acc: 0.8412
Epoch 80/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0695 Acc: 0.8412
Epoch 81/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0695 Acc: 0.8412
Epoch 82/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0695 Acc: 0.8412
Epoch 83/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0695 Acc: 0.8412
Epoch 84/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0699 Acc: 0.8353
Epoch 85/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0704 Acc: 0.8353
Epoch 86/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0702 Acc: 0.8353
Epoch 87/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0702 Acc: 0.8353
Epoch 88/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0701 Acc: 0.8353
Epoch 89/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0699 Acc: 0.8353
Epoch 90/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0698 Acc: 0.8353
Epoch 91/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0697 Acc: 0.8353
Epoch 92/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0696 Acc: 0.8353
Epoch 93/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0696 Acc: 0.8353
Epoch 94/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0696 Acc: 0.8353
Epoch 95/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0694 Acc: 0.8412
Epoch 96/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0694 Acc: 0.8412
Epoch 97/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0693 Acc: 0.8412
Epoch 98/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0692 Acc: 0.8412
Epoch 99/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0693 Acc: 0.8412
Epoch 100/100
train Loss: 1.0053 Acc: 0.8995
valid Loss: 1.0692 Acc: 0.8412
```

![img](data:image/png;base64,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)

```
VGGish(
  (features): Sequential(
    (0): Conv2d(1, 64, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (1): ReLU(inplace=True)
    (2): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
    (3): Conv2d(64, 128, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (4): ReLU(inplace=True)
    (5): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
    (6): Conv2d(128, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (7): ReLU(inplace=True)
    (8): Conv2d(256, 256, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (9): ReLU(inplace=True)
    (10): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
    (11): Conv2d(256, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (12): ReLU(inplace=True)
    (13): Conv2d(512, 512, kernel_size=(3, 3), stride=(1, 1), padding=(1, 1))
    (14): ReLU(inplace=True)
    (15): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)
  )
  (embeddings): Sequential(
    (0): Linear(in_features=12288, out_features=4096, bias=True)
    (1): ReLU(inplace=True)
    (2): Linear(in_features=4096, out_features=4096, bias=True)
    (3): ReLU(inplace=True)
    (4): Linear(in_features=4096, out_features=128, bias=True)
    (5): ReLU(inplace=True)
  )
  (classfilter): Sequential(
    (0): Linear(in_features=128, out_features=64, bias=True)
    (1): Sigmoid()
    (2): Linear(in_features=64, out_features=5, bias=True)
    (3): Softmax(dim=1)
  )
)
Epoch 1/100
train Loss: 1.0069 Acc: 0.8979
valid Loss: 1.0562 Acc: 0.8529
Epoch 2/100
train Loss: 1.3154 Acc: 0.5901
valid Loss: 1.4342 Acc: 0.4706
Epoch 3/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 4/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 5/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 6/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 7/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 8/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 9/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 10/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 11/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 12/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 13/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 14/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 15/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 16/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 17/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 18/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 19/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 20/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 21/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 22/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 23/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 24/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 25/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 26/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 27/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 28/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 29/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 30/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 31/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 32/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 33/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 34/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 35/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 36/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 37/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 38/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 39/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 40/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 41/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 42/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 43/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 44/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 45/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 46/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 47/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 48/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 49/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 50/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 51/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 52/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 53/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 54/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 55/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 56/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 57/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 58/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 59/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 60/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 61/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 62/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 63/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 64/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 65/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 66/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 67/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 68/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 69/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 70/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 71/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 72/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 73/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 74/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 75/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 76/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 77/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 78/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 79/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 80/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 81/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 82/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 83/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 84/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 85/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 86/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 87/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 88/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 89/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 90/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 91/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 92/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 93/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 94/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 95/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 96/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 97/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 98/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 99/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
Epoch 100/100
train Loss: 1.4104 Acc: 0.4944
valid Loss: 1.4342 Acc: 0.4706
```

![img](data:image/png;base64,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)

入力 [8]:

```
_print=True
```