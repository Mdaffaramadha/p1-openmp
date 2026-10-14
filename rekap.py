import re, statistics as st
from collections import defaultdict

print("=== Tabel 2: Perkalian matriks ===")
par = defaultdict(list); ben = defaultdict(list); ser_all = []
for line in open("hasil/matmul.txt"):
    m = re.search(r"n=(\d+) thread=(\d+) serial=([\d.]+) paralel=([\d.]+) benar=(\w+)", line)
    if m:
        n, t = m.group(1), int(m.group(2))
        ser_all.append(float(m.group(3)))
        par[t].append(float(m.group(4)))
        ben[t].append(m.group(5))
ser = st.median(ser_all)
print(f"n = {n}, waktu serial acuan (median {len(ser_all)} run) = {ser:.3f} s")
print("Thread | Serial | Paralel | Speedup | Efisiensi | Benar?")
for t in sorted(par):
    p = st.median(par[t])
    sp = ser / p
    ok = "ya" if all(x == "ya" for x in ben[t]) else "TIDAK"
    print(f"{t} | {ser:.3f} | {p:.3f} | {sp:.3f} | {sp/t*100:.2f}% | {ok}")

print("\n=== Tabel 3: Bilangan prima (median detik) ===")
w = defaultdict(list); benar = defaultdict(list)
for line in open("hasil/prima.txt"):
    m = re.match(r"([^;]+);(\d+);(\d+);N=\d+ prima=(\d+) waktu=([\d.]+)", line.strip())
    if m:
        w[(m.group(1), int(m.group(2)))].append(float(m.group(5)))
        benar[m.group(1)].append(int(m.group(4)) == 664579)
print("Kebijakan | 1 | 2 | 4 | 8 | Speedup 8 | 664.579?")
for s in ["static", "dynamic,1000", "guided"]:
    med = {t: st.median(w[(s, t)]) for t in (1, 2, 4, 8)}
    ok = "ya" if all(benar[s]) else "TIDAK"
    print(f"{s} | {med[1]:.3f} | {med[2]:.3f} | {med[4]:.3f} | {med[8]:.3f} | {med[1]/med[8]:.3f}x | {ok}")

