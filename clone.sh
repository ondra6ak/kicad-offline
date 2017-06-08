#!/bin/bash


(repos=$(./get_gh_repos.py KiCad | grep ".pretty$")
cd $1
for repo in $repos
do
	echo $repo
	git clone $repo > /dev/null
done)