import os

LINE = "Doorbell+ rings your own doorbell the moment you arrive home, so the house you already own can finally welcome you properly."

out = os.environ["MAKEFUN_OUTPUT_DIR"]
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
