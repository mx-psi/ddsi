for f in ./Diagramas/*.dia;
do
    dia $f --export $f.png;
done
