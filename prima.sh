#!/bin/bash
rm -f hasil/prima.txt
for s in "static" "dynamic,1000" "guided"; do
  for t in 1 2 4 8; do
    for r in 1 2 3; do
      echo -n "$s;$t;$r;" >> hasil/prima.txt
      OMP_SCHEDULE="$s" OMP_NUM_THREADS=$t ./prima >> hasil/prima.txt
      echo "selesai: scheduling=$s thread=$t percobaan=$r"
    done
  done
done
echo "Pengujian prima selesai. Hasil ada di hasil/prima.txt"
