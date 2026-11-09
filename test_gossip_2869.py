#!/usr/bin/env python3
"""Tests del hecho: el gossip de fran-miu-micelio NO produce 2869.46.

Solo-stdlib. Se corre con: python3 test_gossip_2869.py
"""

import math
import unittest

import gossip_2869_repro as R

TECHO = 692.8263846529436  # 140·ln(141)
REGISTRADO = 2869.460517705751  # Phi_global de gossip_result.json, N=140


class TestGossipNoProduce2869(unittest.TestCase):
    def test_max_teorico(self):
        # El techo es N·ln(N+1): el factor (1−exp(−var/σ)) es siempre < 1.
        self.assertAlmostEqual(R.max_teorico(), TECHO, places=9)
        self.assertAlmostEqual(R.max_teorico(140), 140 * math.log(141), places=12)

    def test_spin_acotado(self):
        # Cada spin() vive en [0, techo): var ≥ 0 ⇒ 0 ≤ 1−exp(−var/σ) < 1.
        g = R.GossipPhi4()
        for _ in range(5):
            v = g.spin()
            self.assertGreaterEqual(v, 0.0)
            self.assertLess(v, TECHO)

    def test_gossip_no_alcanza_registrado(self):
        # Dos corridas completas (100 ciclos): medias ~2, muy por debajo
        # del techo y del valor registrado.
        for _ in range(2):
            r = R.GossipPhi4().run()
            self.assertLess(r["phi_global_mean"], TECHO)
            self.assertLess(r["phi_global_mean"], REGISTRADO)

    def test_registrado_supera_el_techo(self):
        # El valor registrado es 4,14 veces el techo: imposible para este código.
        self.assertGreater(REGISTRADO, TECHO)
        self.assertAlmostEqual(REGISTRADO / TECHO, 4.14, places=2)

    def test_semilla_42_reproduce_registrado(self):
        # La media ponderada con seed 42 da el valor registrado dígito a dígito.
        r = R.gossip_phi4(R.construir_nodos(semilla=42))
        self.assertEqual(r, REGISTRADO)

    def test_media_ponderada_entre_min_y_max(self):
        # Es un centro, no una integración: vive entre min y max de entrada.
        nodos = R.construir_nodos(semilla=42)
        r = R.gossip_phi4(nodos)
        lo = min(n.Phi for n in nodos)
        hi = max(n.Phi for n in nodos)
        self.assertGreaterEqual(r, lo)
        self.assertLessEqual(r, hi)

    def test_semillas_distintas_dan_distinto_valor(self):
        # El valor depende del sorteo: sin semilla fija no es reproducible.
        a = R.gossip_phi4(R.construir_nodos(semilla=1))
        b = R.gossip_phi4(R.construir_nodos(semilla=42))
        self.assertNotEqual(a, b)

    def test_sigma_con_distinta_precision(self):
        # Dato documentado: el gossip usa sigma = 3.427051 (6 decimales)
        # y el repro del hermano SIGMA = 3.427050983124843. El techo no
        # depende de sigma, así que no cambia el veredicto.
        self.assertEqual(R.GossipPhi4().sigma, 3.427051)
        self.assertEqual(R.SIGMA, 3.427050983124843)
        self.assertAlmostEqual(R.GossipPhi4().sigma, R.SIGMA, places=5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
