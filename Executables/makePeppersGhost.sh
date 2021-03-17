#!/bin/bash

for ((i=1; i < 751; i++)); do
    if [[ $i -lt 10 ]]; then
        f="peppersmars-00"${i}
    elif [[ $i -ge 10 && $i -lt 100 ]]; then
        f="peppersmars-0"${i}
    else
        f="peppersmars-"${i}
    fi
    convert -crop 310x310+170+20 -resize 50% ${f}.jpeg ${f}_c.jpeg
    convert ${f}_c.jpeg -rotate 90 ${f}_l.jpeg
    convert ${f}_c.jpeg -rotate 180 ${f}_u.jpeg
    convert ${f}_c.jpeg -rotate 270 ${f}_r.jpeg

    convert black_c.jpeg ${f}_c.jpeg black_c.jpeg +append ${f}_t.jpeg
    convert ${f}_r.jpeg black_c.jpeg ${f}_l.jpeg +append ${f}_m.jpeg
    convert black_c.jpeg ${f}_u.jpeg black_c.jpeg +append ${f}_b.jpeg

    convert ${f}_t.jpeg ${f}_m.jpeg ${f}_b.jpeg -append ${f}_ghosted.jpeg
done
rm -f *_c.jpeg *_l.jpeg *_u.jpeg *_r.jpeg *_t.jpeg *_m.jpeg *_b.jpeg *_ghosted.jpeg
