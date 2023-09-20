#!/bin/sh

set +x

if ! [ -d ~/.fifacareer ] 
then

  mkdir ~/.fifacareer
  echo "0" > ~/.fifacareer/careerCount
  echo "" > ~/.fifacareer/activeCareer
  exit 0

else

  echo "You already have a fifacareer directory, please delete before running the career script"
  exit 1

fi
