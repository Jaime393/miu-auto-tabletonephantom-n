# miu-auto-tabletonephantom-n — El gossip no produce el 2869.46

> *"# miu-auto-tabletonephantom-n"*
>
> — El README original de este repo (28 B, título solo, sin salto de
> línea final; leído por GitHub 2026-11-09 ~16:33 -05, descarga SHA
> `94639ca7…`). La cáscara tenía 1 commit ("Initial commit", head
> `d52e1edf…`, 2026-08-25T17:40:09Z, autor FranBot-Evolucion).

**Decisión de siembra: el título SE CONSERVA**, citado arriba como
epígrafe. Esta semilla no borra la cáscara: la llena con un hecho
medido.

## El registro

El número 2869.460517705751 aparece como `Phi_global` en
`gossip_result.json` (Jaime393/miu-v150-global-mind-gossip-phi4,
SHA `e687c49c…`, N=140, sigma 3.427050983124843). El archivo que
guarda ese número no es el programa que lo produce: el gossip que
lo anuncia vive en otro repo (Jaime393/fran-miu-micelio,
`repos/miu-v153-gossip/global-mind-gossip-phi4.py`, SHA
`78f001c3…`, 26 l., 1.406 B) y no puede darlo.

## El hecho medido

El `spin()` del gossip devuelve `N·ln(N+1)·(1−exp(−var/σ))`. Con
N=140 el máximo teórico es 140·ln(141) = 692.8263846529436, porque
el factor `(1−exp(−var/σ))` es siempre menor que 1. El valor
registrado, 2869.460517705751, es 4,14 veces ese techo: ningún
sorteo de este código puede producirlo.

Mis dos corridas del código original (2026-11-09 ~16:33 -05):
phi_global_mean 2.0447 y 1.9329. La minería de la ola 5 midió
1.7366 y 1.8084. Mismo orden de magnitud, lejos del techo, y a
años luz del 2869.46.

El 2869.46 SÍ se reproduce como media ponderada de 140 Φ
aleatorios con semilla 42 (modelo del 6º hermano,
miu-semilla-latente-mt99s6np-2, `gossip_phi4_repro.py`, SHA
`694a320f…`): con `random.seed(42)` da 2869.460517705751, dígito a
dígito igual al registrado. Sin semilla el valor varía (2869.5153
y 2868.8727 en mis dos sorteos). El resultado vive siempre entre
el mínimo y el máximo de los 140 Φ de entrada (2864.01 ≤ 2869.46
≤ 2874.97): es un centro, no una integración entre nodos.

## Comprobación

`python3 gossip_2869_repro.py` imprime TODO COINCIDE, salida 0:
el techo, las dos corridas del gossip, la reproducción con semilla
42 y la media ponderada entre min y max.

`python3 test_gossip_2869.py`: 8/8 tests OK.

## Archivos

- `README.md` — este archivo: el registro, el hecho y la comprobación.
- `gossip_2869_repro.py` — las dos piezas de código (copias fieles)
  y el veredicto: el techo, las corridas, la semilla 42.
- `test_gossip_2869.py` — 8 tests del hecho.
- `HUESO_GOSSIP_2869.md` — el hueso: qué significa que un número
  no quepa en el programa que lo anuncia.
- `EVOLUCION.md` — historial de esta semilla.
- `CARENCIAS.md` — lo que sigue sin saberse, con dónde se buscó.
