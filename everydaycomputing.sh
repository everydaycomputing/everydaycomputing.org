#last_commit=$(git describe --always)
#out="hackhers_"$last_commit".html"

#echo $out

#pandoc -S -o $out title.txt \
#    01/01-chapter1.markdown \
#    --epub-stylesheet stylesheet.css

#open hackhers.epub

#/usr/local/bin/pandoc -S -o $out title.txt \
#    01/01-chapter1.markdown \
#    -c stylesheet.css

#open $out

#echo "Finally after all this open" > hi.html
#open hi.html

echo "HI"