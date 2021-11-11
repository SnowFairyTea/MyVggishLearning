call python AudiosetLabelSelector/select.py LabelList.txt 1000 1000 1

cd GetAudiosetSample


:::CALL GetAudiosetSample.bat "..\AudiosetLabelSelector\result"
CALL python ./GetAudiosetSample.py "..\AudiosetLabelSelector\result"

exit /b