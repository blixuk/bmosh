#!/bin/bash
# python build script
# Author: blix

NAME=false
TESTRUN=false

help()
{
	echo ""
	echo "Usage: $0 -n <name>"
	echo -e "-n <name> : name of compiled application"
	echo -e "-r : run application after building"
	echo -e "-h : display help"
	echo ""
	exit 1
}

error()
{
	echo -e "\nplease use -h for help\n"
	exit 1
}

while getopts "n:hr" opt
do
	case "$opt" in
		n ) NAME="$OPTARG" ;; # set name value
		r ) TESTRUN=true ;; # run executable after building
		h ) help ;; # call help function
		? ) error ;; # call error function
	esac
done

if [ -z "$NAME" ]
then
	echo -e "\nplease supply a name value\n"
fi

if [ ! -z "$NAME" ] && [ "$NAME" != false ]
then
	echo -e " - starting build - "
	echo -e "building: $NAME"
	mkdir build # create build directory
	echo -e "created directory: build"
	zip -r ./build/build.zip * -x '*build*' '*temp*' # zip all files excluding build files
	echo -e "created file: build.zip"
	cd build # change to build directory
	echo '#!/usr/bin/env python3' | cat - build.zip > $NAME # add shebang to new file
	chmod +x $NAME # make file executable
	echo -e "created executable: $NAME"
	cd .. # change back to main directory
	echo -e " - build complete - \n"
fi

if [ "$TESTRUN" = true ]
then
	echo -e " - test run - \n"
	cd build # change to build directory
	./$NAME # run executable
	echo -e "\n - test complete - "
fi