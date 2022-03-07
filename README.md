### Smart-India-Hackathon-2022
This repository is for the project for the upcoming Smart India Hackathon 2022.

## Problem Statement:
Automate frequently used tasks of a pc using gestures, provided users are *authenticate by face recognition*. Tasks to automate:
* save
* exit
* print
* screen-lock
* screen-unlock
* system shut down
* system restart

## Prototype:
Divided into three parts
* Face recognition module
* Finger recognition to detect count of finger raised module
* Automation module

## Face Recognition Module
Stages:-
* Detection
    Using opencv and haar cascade classifier, worked for detecting face for the user. This module is trained with certain number of input data.
* Recognition
    After training, using Local Binary Pattern algorithm for recognizing faces for furhter operations.

## Finger Count Module
Stages:-
* Detection
    Using opencv and haar cascade classifier, worked for detecting hands for the user. This module is trained with certain number of input data for finding position.
* Recognition of fingers
    Detecting number of fingers raised and returns the count of fingers.

## Automation Module
Results recieved from *Face Recognition Module* and *Finger Count Module*, We map the autohot keys(shortcut keys) for performing the operations.