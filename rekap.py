import re, statistics as st
from collections import defaultdict

print("=== Tabel 2: Perkalian matriks ===")
d = defaultdict(lambda: {"s": [], "p": [], "b": []})
for line in open("hasil/matmul.txt"):
    m = re.search(r"n=(\d+) thread=(\d+) serial=([\d.]+) paralel=([\d.]+) benar=(\w+)", line)
    if m:
        n, t = m.group(1), int(m.group(2))
        d[t]["s"].append(float(m.group(3)))
        d[t]["p"].append(float(m.group(4)))
        d[t]["b"].append(m.group(5))
print(f"n = {n}")
print("Thread | Serial | Paralel | Speedup | Efisiensi | Benar?")
for t in sorted(d):
    s, p = st.median(d[t]["s"]), st.median(d[t]["p"])
    sp = s / p
    ok = "ya" if all(x == "ya" for x in d[t]["b"]) else "TIDAK"
    print(f"{t} | {s:.3f} | {p:.3f} | {sp:.3f} | {sp/t*100:.2f}% | {ok}")

print("\n=== Tabel 3: Bilangan prima (median detik) ===")
w = defaultdict(list); benar = defaultdict(list)
for line in open("hasil/prima.txt"):
    m = re.match(r"([^;]+);(\d+);(\d+);N=\d+ prima=(\d+) waktu=([\d.]+)", line.strip())
    if m:
        k = (m.group(1), int(m.group(2)))
        w[k].append(float(m.group(5)))
        benar[m.group(1)].append(int(m.group(4)) == 664579)
print("Kebijakan | 1 | 2 | 4 | 8 | Speedup 8 | 664.579?")
for s in ["static", "dynamic,1000", "guided"]:
    med = {t: st.median(w[(s, t)]) for t in (1, 2, 4, 8)}
    ok = "ya" if all(benar[s]) else "TIDAK"
    print(f"{s} | {med[1]:.3f} | {med[2]:.3f} | {med[4]:.3f} | {med[8]:.3f} | {med[1]/med[8]:.3f}x | {ok}")
