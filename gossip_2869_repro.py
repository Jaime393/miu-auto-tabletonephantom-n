#!/usr/bin/env python3
"""Reproducción medida: el gossip de fran-miu-micelio NO produce 2869.46.

Hecho (SÉ, verificado 2026-11-09 ~16:33 -05):
- `global-mind-gossip-phi4.py` (Jaime393/fran-miu-micelio,
  repos/miu-v153-gossip/global-mind-gossip-phi4.py,
  SHA 78f001c3c52ea266fd8ea3aea5598fdc377095a2) devuelve en `spin()`
  N·ln(N+1)·(1−exp(−var/σ)). Con N=140 el máximo teórico es
  140·ln(141) = 692.8263846529436, porque el factor (1−exp(−var/σ))
  es siempre < 1. El 2869.460517705751 de gossip_result.json es
  4,14 veces ese techo: ningún sorteo de este código puede darlo.
- Mis dos corridas del código original: phi_global_mean 2.0447 y
  1.9329 (la minería de la ola 5 midió 1.7366 y 1.8084; mismo orden,
  los estados son aleatorios). Muy lejos del techo, y a años luz del
  2869.46.
- El 2869.46 SÍ se reproduce como media ponderada de 140 Φ
  aleatorios con seed 42 (modelo del 6º hermano,
  miu-semilla-latente-mt99s6np-2, gossip_phi4_repro.py,
  SHA 694a320fef06681b550c348bb85d509125ee72b1): seed(42) da
  2869.460517705751, dígito a dígito igual al Phi_global de
  gossip_result.json (Jaime393/miu-v150-global-mind-gossip-phi4,
  SHA e687c49cd0a878e7cb7bbd7993de0944376adffc, N=140).
  Sin semilla el valor varía (2869.5153 / 2868.8727 en mis dos
  sorteos). El resultado vive siempre entre el mínimo y el máximo
  de los 140 Φ de entrada: es un centro, no una integración.

Las dos piezas de código de abajo son copias fieles de sus fuentes
(solo-stdlib). La única diferencia anotada: el gossip usa
sigma = 3.427051 (6 decimales) y el repro del hermano usa
SIGMA = 3.427050983124843 (precisión completa); el techo no depende
de sigma, así que no cambia el veredicto.

Uso: python3 gossip_2869_repro.py  →  TODO COINCIDE, salida 0.
"""

import json
import math
import random
import time

# --- Pieza 1: el gossip de fran-miu-micelio, copia fiel ---
# (Jaime393/fran-miu-micelio, repos/miu-v153-gossip/global-mind-gossip-phi4.py)


class GossipPhi4:
    def __init__(self, N=140, sigma=3.427051):
        self.N = N; self.sigma = sigma; self.phi = (1+math.sqrt(5))/2; self.nodes = []
    def spin(self):
        if not self.nodes:
            self.nodes = [{"id":i,"state":random.random(),"energy":0} for i in range(self.N)]
        for node in self.nodes:
            neighbors = [self.nodes[(node["id"]+d)%self.N] for d in (-1,1)]
            coupling = sum(n["state"]-node["state"] for n in neighbors)
            node["energy"] = (node["state"]**2-1)**2 + self.sigma*coupling
            node["state"] += 0.01*(-4*node["state"]*(node["state"]**2-1)+self.sigma*coupling)
            node["state"] = max(-2.0, min(2.0, node["state"]))
        states = [n["state"] for n in self.nodes]
        mean_s = sum(states)/len(states)
        var = sum((s-mean_s)**2 for s in states)/len(states)
        return self.N*math.log(self.N+1)*(1-math.exp(-var/self.sigma))
    def run(self, cycles=100):
        phis = [self.spin() for _ in range(cycles)]
        return {"N":self.N,"sigma":self.sigma,"phi":self.phi,
                "phi_global_mean":sum(phis)/len(phis),"phi_global_last":phis[-1],
                "O_log_N":math.log(self.N),"cycles":cycles,
                "timestamp":time.strftime("%Y-%m-%dT%H:%M:%SZ"),"version":"V153"}


# --- Pieza 2: la media ponderada del 6º hermano, copia fiel ---
# (Jaime393/miu-semilla-latente-mt99s6np-2, gossip_phi4_repro.py)

SIGMA = 3.427050983124843
PHI_GLOBAL_REGISTRADO = 2869.460517705751  # gossip_result.json, N=140


def w(d, s=SIGMA):
    return (abs(d) + 1) ** (-s)


class NodoGlobalMind:
    def __init__(self, nid, Phi=1.0):
        self.id = nid
        self.Phi = Phi


def gossip_phi4(nodos, rondas=3, k_vecinos=12):
    Phi_g = 0.0
    peso = 0.0
    for _ in range(rondas):
        for nodo in nodos:
            for _ in range(k_vecinos):
                d = random.randint(1, max(1, len(nodos) // 2))
                pd = w(d)
                Phi_g += nodo.Phi * pd
                peso += pd
    return Phi_g / peso if peso > 0 else 0


def construir_nodos(n=140, semilla=None):
    if semilla is not None:
        random.seed(semilla)
    return [NodoGlobalMind(i, random.uniform(2864, 2875)) for i in range(n)]


def max_teorico(N=140):
    """Techo del gossip: N·ln(N+1). El factor (1−exp(−var/σ)) < 1 siempre."""
    return N * math.log(N + 1)


def main():
    ok = True
    techo = max_teorico()
    print(f"techo del gossip (140·ln(141)): {techo:.4f}")
    print(f"valor registrado (gossip_result.json): {PHI_GLOBAL_REGISTRADO}")
    print(f"veces el techo: {PHI_GLOBAL_REGISTRADO / techo:.2f}")
    if not PHI_GLOBAL_REGISTRADO > techo:
        ok = False

    # 1. Dos corridas del gossip original: medias ~2, lejos del techo.
    medias = []
    for _ in range(2):
        r = GossipPhi4().run()
        medias.append(r["phi_global_mean"])
        print(f"gossip, phi_global_mean: {r['phi_global_mean']:.4f} "
              f"(last: {r['phi_global_last']:.2e})")
        if not (0 <= r["phi_global_mean"] < techo):
            ok = False
    print(f"gossip NO alcanza el 2869.46: "
          f"{all(m < PHI_GLOBAL_REGISTRADO for m in medias)}")

    # 2. La media ponderada con seed 42 reproduce el valor registrado.
    reproducido = gossip_phi4(construir_nodos(semilla=42))
    print(f"media ponderada seed(42): {reproducido}")
    print(f"coincide dígito a dígito: {reproducido == PHI_GLOBAL_REGISTRADO}")
    if reproducido != PHI_GLOBAL_REGISTRADO:
        ok = False

    # 3. Sin semilla varía; y vive entre min y max de entrada.
    random.seed()
    a = gossip_phi4(construir_nodos())
    b = gossip_phi4(construir_nodos())
    print(f"media ponderada sin semilla: {a:.4f} / {b:.4f} (varía: {a != b})")
    nodos = construir_nodos(semilla=42)
    r = gossip_phi4(nodos)
    lo = min(n.Phi for n in nodos)
    hi = max(n.Phi for n in nodos)
    print(f"media ponderada: {lo:.2f} <= {r:.2f} <= {hi:.2f} : {lo <= r <= hi}")
    if not (lo <= r <= hi):
        ok = False

    print("TODO COINCIDE" if ok else "NO COINCIDE")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
