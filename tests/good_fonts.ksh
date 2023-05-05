#!/bin/bash


#-------------------------------------------------------------------------------
#         Copyright (C) 2023    Steve Price    SuperStevePrice@gmail.com
#
#                       GNU GENERAL PUBLIC LICENSE
#                        Version 3, 29 June 2007
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# PROGRAM:
#	good_fonts.ksh
#	
# PURPOSE:
#	Display a series of xterm windows of differnet fonts and sizes.  Ask the
#	user to accept or reject each font and size. Store good fonts in the 
#	output files.
#	
# USAGE:
#
#-------------------------------------------------------------------------------


# List of font names and sizes to test
fonts=("DejaVu Sans Mono" "Monospace" "Courier New")
sizes=(12 14 16)
# Output file for good fonts
output_file="../docs/good_fonts.txt"

# Iterate over fonts and sizes
for font in "${fonts[@]}"; do
    for size in "${sizes[@]}"; do
		message="Testing font $font size $size"
        # Launch xterm with font and size
        xterm -fa "$font" -fs "$size" -e "echo $message; sleep 2"

        # Check if font is displayed correctly
        read -p "Is font $font size $size displayed correctly? (y/n) " choice
        case "$choice" in 
          y|Y ) echo "$font $size" >> "$output_file";;
          n|N ) echo "Font $font size $size does not work with xterm.";;
          * ) echo "Invalid choice. Skipping font $font size $size.";;
        esac
    done
done

echo "Good fonts written to $output_file."
