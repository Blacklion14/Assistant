# Assistant

## Overview 

This program is created to test CNN model to distinguish between Cat and Dog by image.
In this program we used: 
 - `pyttsx3` library to get the voice of system
 - `speech_recognition` to recognise words in a speech inputed by mic
 - `tensorflow` to load pretrained CNN model
 - `keras` to preprocess image before sending it to CNN model for prediction.

## How to use

 - To run this program clone the repository to your local machine:

    ``` git clone https://github.com/Blacklion14/Assistant ```

 - Then install all the necessary libaries to your local python developement enviorment.

 - Now pick any image of Dog or Cat in png or jpg format and put it in folder  [dataset/single_prediction](/dataset/single_prediction/) and rename it with any integer.

 - Now run [test.py](/test.py) file and give instruction to assistant to test your image and get the results.

## Instructions

 - Firstly when you run the code Assistant wishes you according to time.
 - Now you should say a sentence in which there must be word ` predict ` and at the end of the sentence you should say that integer value with which you renamed the file.
 - For exmple you should say: `Assistant predict image number 5` then it predicts image named with 5 present in the 
 ` dataset/single_prediction ` folder.

## Feedback

You can give your feedback or suggestions for improvement on this Form. It will be really appreciated :)
[https://forms.gle/SmxsNAJSvL2fgRXm7](https://forms.gle/SmxsNAJSvL2fgRXm7)

## Contribute

You can directly create a PR through which you can tell us your intrest and contributing area.