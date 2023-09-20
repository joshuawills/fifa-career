#!/bin/sh

i=0

echo "0" > ~/.fifacareer/careerCount
echo "" > ~/.fifacareer/activeCareer

while [ "$i" -lt "100" ]
do

  if ! [ -d ~/.fifacareer/career${i} ]
  then
    echo "Done"
    exit 0
  fi

  rm -fr ~/.fifacareer/career${i}
  i=$((i + 1))
done
