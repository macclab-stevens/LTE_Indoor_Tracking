#!/bin/bash

# Check if the file is provided as an argument
if [ "$#" -ne 1 ]; then
	echo "Usage: $0 <file>"
	exit 1
fi

file="$1"

# Check if the file exists
if [ ! -f "$file" ]; then
	echo "Error: File not found!"
	exit 1
fi

# Insert [ at the beginning of the file
sed -i '1s/^/[/' "$file"

# Append ] at the end of the file
echo "]" >> "$file"


echo "Brackets added to $file."


echo "Arrayifing $file."
sed -i 's/^}/},/g' $file
sed -i ':a;$!{N;ba};s/},\([^}]*\)$/}\1/' enb_report.json
