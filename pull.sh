#!/bin/bash

for repo in $1/*.pretty
do
	echo $repo
	(cd $repo && git pull) > /dev/null
done