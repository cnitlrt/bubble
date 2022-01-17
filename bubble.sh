#!/bin/bash
FILE_NAME=$1
LIBC_FILE=$2
if [ "$FILE_NAME" = "" ];then
	printf "Usage <%s> : bubble <file> <libc_file>\n"
	printf "Please input the file\n"
	exit
fi
if [ "$LIBC_FILE" ];then
	sudo chmod +x $1
	touch $1.py
	echo "[+]Touch Successful!"
	sudo subl $1.py
	sudo chmod +777 $1.py
	template $1 --libc $2 > $1.py
	sudo xclibc $1 $2
	echo "Over"
	exit
fi
sudo chmod +x $1
touch $1.py
echo "[+]Touch Successful!"
sudo subl $1.py
sudo chmod +777 $1.py
template $1 > $1.py
echo "Over"
