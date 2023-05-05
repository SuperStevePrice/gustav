#!/usr/bin/env ksh

say_what() {
    if [ "$file" = "exrc" ]
    then
        print "if $file"
    elif [ "$file" = "crazy" ]
    then
        print "elif $file"
    elif echo "$file" | grep -q "bin"
    then
        print "bin $file"
    else
        print "else $file"
    fi
}

for file in exrc crazy ~/bin/train
do
    say_what "$file"
done
