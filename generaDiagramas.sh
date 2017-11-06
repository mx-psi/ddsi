for f in ./*;
do
    dia $f --export $f.png;
done
