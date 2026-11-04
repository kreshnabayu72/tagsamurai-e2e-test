"""Tests for check-suite-prd.py (stdlib only): `python -m unittest scripts/test_check_suite_prd.py`."""
import importlib.util
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

SPEC = importlib.util.spec_from_file_location("check_suite_prd", Path(__file__).with_name("check-suite-prd.py"))
check = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(check)

SHA = "ab12cd34ef56ab78" + "0" * 48
RULES = {"schema": "prd-rules/v1", "prefix": "DEMO", "sha256": SHA,
         "parents": ["DEMO-LOGIC-01", "F-DEMO-02"],
         "held": {"DEMO:V-02": ["IGAP-0001"]},
         "rules": [
             {"qid": "DEMO-LOGIC-01a", "priority": "P2", "spectra_priority": "Medium"},
             {"qid": "F-DEMO-02a1", "priority": "P0", "spectra_priority": "Critical"},
             {"qid": "DEMO:V-01", "priority": "P2", "spectra_priority": "Medium"},
             {"qid": "DEMO:V-02", "priority": "P2", "spectra_priority": "Medium"},
             {"qid": "DEMO-LOGIC-02", "priority": "P2", "spectra_priority": "Medium"}]}


def spec_text(folder, rules, priority="Critical", extra_steps=""):
    listed = "\n".join(f"  - {r}" for r in rules)
    return (f"---\nid: {folder}\ntitle: Demo\npriority: {priority}\ncaseType: Positive\nsourceRules:\n{listed}\n---\n"
            "## Prerequisites\n- Mode: FE+BE\n- Akun DU-01\n\n## Test Steps\n### F-DEMO-02a1: Register\n"
            f"1. Klik [+ Demo]\n2. Verifikasi form Register tampil\n{extra_steps}\n## Notes\n- -\n")


COVERAGE = """# Coverage GlobalSettingsDemo

Sumber: `global-settings/demo/PRD/demo.md` · PRD sha256 `ab12cd34ef56ab78` · 5 aturan leaf · 1 spec

## Aturan → spec

| Aturan | Spec | Mode |
|---|---|---|
| `F-DEMO-02a1` | `TC-GS-DEMO-E2E-001` | FE+BE |

## Di luar E2E

| Aturan | Alasan | Rujukan tc-backend |
|---|---|---|
| `DEMO-LOGIC-02` | perilaku server murni | `TC-DEMO-BE-007` |

## Ditahan

| Aturan | Temuan | Catatan |
|---|---|---|
| `DEMO:V-02` | `IGAP-0001` | menunggu keputusan |

## Spec

| Spec | Mode | Langkah | Aturan |
|---|---|---|---|
| `TC-GS-DEMO-E2E-001-register` | FE+BE | 2 | `F-DEMO-02a1` |

## Catatan
"""

DATA = "# Data uji\n\n| ID | Data | Nilai | Sumber | Lifecycle | Dipakai spec |\n|---|---|---|---|---|---|\n" \
       "| `DU-01` | Akun | env `GS_A_EMAIL` | §2 | pre-setup | 001 |\n"


class CheckSuitePrdTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.base = Path(tmp.name)
        self.suite = self.base / "specs" / "GlobalSettings" / "Demo"
        self.folder = "TC-GS-DEMO-E2E-001-register"
        (self.suite / self.folder).mkdir(parents=True)
        self.write_spec(["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"])
        self.rules = self.base / "rules.json"
        self.rules.write_text(json.dumps(RULES), encoding="utf-8")
        self.coverage = self.base / "coverage.md"
        self.coverage.write_text(COVERAGE, encoding="utf-8")
        self.data = self.base / "data.md"
        self.data.write_text(DATA, encoding="utf-8")
        self.backend = self.base / "tc-demo-backend.md"
        self.backend.write_text("### 7. TC-DEMO-BE-007 server rule\n", encoding="utf-8")

    def write_spec(self, rules, **kw):
        (self.suite / self.folder / "spec.md").write_text(spec_text(self.folder, rules, **kw), encoding="utf-8")

    def run_check(self, *extra, coverage=True, data=True, backend=True):
        argv = [str(self.suite), "--rules", str(self.rules)]
        argv += ["--coverage", str(self.coverage)] if coverage else []
        argv += ["--data", str(self.data)] if data else []
        argv += ["--tc-backend", str(self.backend)] if backend else []
        out = io.StringIO()
        with redirect_stdout(out):
            rc = check.main([*argv, *extra])
        return rc, out.getvalue()

    def codes(self, text):
        return sorted({line.split()[1] for line in text.splitlines() if line.startswith("[")})

    def test_a_complete_suite_is_clean(self):
        rc, out = self.run_check()
        self.assertEqual(rc, 0, out)
        self.assertIn("5 aturan leaf (0 kewajiban turunan), 3 tercakup spec, 1 di luar E2E, 1 ditahan, "
                      "0 tidak berlaku, 0 temuan", out)

    def test_not_applicable_accepts_only_obligations_with_a_prd_reference(self):
        rules = json.loads(json.dumps(RULES))
        rules["rules"] += [{"qid": "DEMO:obl/T-DEMO-01/pagination", "obligation": True, "priority": "P2"},
                           {"qid": "DEMO:obl/T-DEMO-01/download", "obligation": True, "priority": "P2"}]
        self.rules.write_text(json.dumps(rules), encoding="utf-8")
        rc, out = self.run_check()
        self.assertIn("[FINDING] T1 DEMO:obl/T-DEMO-01/pagination tidak tercakup spec mana pun, tidak di Di luar E2E, "
                      "tidak di Ditahan, tidak di Tidak berlaku", out)
        block = ("\n## Tidak berlaku\n\n| Kewajiban | Alasan (rujukan PRD) |\n|---|---|\n"
                 "| `DEMO:obl/T-DEMO-01/pagination` | §5 L40: tabel memuat paling banyak 5 baris |\n"
                 "| `DEMO:obl/T-DEMO-01/download` | tidak ada tombol |\n"
                 "| `DEMO-LOGIC-01a` | §4 L12 |\n")
        self.coverage.write_text(COVERAGE.replace("\n## Spec", block + "\n## Spec"), encoding="utf-8")
        rc, out = self.run_check()
        self.assertNotIn("T1 DEMO:obl/T-DEMO-01/pagination", out)
        self.assertIn("[FINDING] T11 Tidak berlaku: DEMO:obl/T-DEMO-01/download tanpa rujukan baris atau § PRD", out)
        self.assertIn("[FINDING] T11 Tidak berlaku: DEMO-LOGIC-01a aturan PRD, bukan kewajiban turunan", out)
        self.assertIn("(2 kewajiban turunan)", out)

    def test_uncovered_unknown_parent_and_held_rules(self):
        self.write_spec(["F-DEMO-02a1", "DEMO:V-02", "F-DEMO-02", "DEMO:V-99"])
        rc, out = self.run_check()
        self.assertEqual(rc, 1)
        self.assertIn("[FINDING] T1 DEMO-LOGIC-01a tidak tercakup", out)
        self.assertIn("[FINDING] T1 DEMO:V-01 tidak tercakup", out)
        self.assertIn("[FINDING] T2 TC-GS-DEMO-E2E-001-register: sourceRules DEMO:V-99 tidak ada di PRD", out)
        self.assertIn("[FINDING] T3 TC-GS-DEMO-E2E-001-register: sourceRules F-DEMO-02 adalah aturan induk", out)
        self.assertIn("[FINDING] T5 TC-GS-DEMO-E2E-001-register: sourceRules DEMO:V-02 ditahan temuan IGAP-0001", out)
        self.assertIn("per kode: T1 2, T2 1, T3 1, T5 1", out)

    def test_outside_e2e_entries_must_be_justified_and_exist_in_the_backend_tc(self):
        self.coverage.write_text(COVERAGE.replace("perilaku server murni", " ").replace("BE-007", "BE-999"),
                                 encoding="utf-8")
        rc, out = self.run_check()
        self.assertIn("[FINDING] T4 Di luar E2E: DEMO-LOGIC-02 tanpa alasan", out)
        self.assertIn("[FINDING] T4 Di luar E2E: DEMO-LOGIC-02 merujuk TC-DEMO-BE-999 yang tidak ada", out)
        rc, out = self.run_check(backend=False)
        self.assertIn("[REVIEW] T4 Di luar E2E: DEMO-LOGIC-02 merujuk TC-DEMO-BE-999 tetapi --tc-backend tidak diberikan", out)
        self.write_spec(["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01", "DEMO-LOGIC-02"])
        rc, out = self.run_check()
        self.assertIn("[FINDING] T4 Di luar E2E: DEMO-LOGIC-02 sekaligus dikutip TC-GS-DEMO-E2E-001-register", out)

    def test_priority_counts_hash_and_data(self):
        self.write_spec(["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"], priority="Medium",
                        extra_steps="3. Isi data DU-07\n")
        self.coverage.write_text(COVERAGE.replace("5 aturan leaf", "4 aturan leaf")
                                 .replace("ab12cd34ef56ab78", "ffffffffffffffff"), encoding="utf-8")
        rc, out = self.run_check()
        self.assertIn("[FINDING] T6 TC-GS-DEMO-E2E-001-register: priority Medium != Critical", out)
        self.assertIn("[FINDING] T7 coverage menyebut 4 aturan leaf, PRD berisi 5", out)
        self.assertIn("[FINDING] T8 PRD sha256 coverage ffffffffffffffff != PRD sekarang ab12cd34ef56ab78", out)
        self.assertIn("[FINDING] T9 TC-GS-DEMO-E2E-001-register: DU-07 tidak ada di data.md", out)

    def test_missing_coverage_and_held_rule_absent_from_ditahan(self):
        rc, out = self.run_check(coverage=False)
        self.assertIn("[FINDING] T7 halaman coverage tidak diberikan atau tidak ada", out)
        self.coverage.write_text(COVERAGE.replace("| `DEMO:V-02` | `IGAP-0001` | menunggu keputusan |\n", ""),
                                 encoding="utf-8")
        rc, out = self.run_check()
        self.assertIn("[FINDING] T5 DEMO:V-02 ditahan temuan IGAP-0001 tetapi tidak tercantum di Ditahan", out)
        self.assertIn("[FINDING] T1 DEMO:V-02 tidak tercakup", out)

    def test_klausa_di_luar_e2e_bullets_are_checked_for_rule_id_and_reason(self):
        notes = ("## Notes\n- Klausa di luar E2E: tanpa id aturan sama sekali\n"
                 "- Klausa di luar E2E: `DEMO-LOGIC-02` (klausa server); sourceRules spec ini tidak memuatnya\n"
                 "- Klausa di luar E2E: `F-DEMO-02a1` pada group kedua tidak ada di data uji\n"
                 "- Klausa di luar E2E: `DEMO:V-01` (efek murni server)\n- -\n")
        path = self.suite / self.folder / "spec.md"
        text = spec_text(self.folder, ["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"]).replace("## Notes\n- -\n", notes)
        path.write_text(text, encoding="utf-8")
        rc, out = self.run_check()
        self.assertIn("[FINDING] T10 TC-GS-DEMO-E2E-001-register: butir «Klausa di luar E2E» tanpa ID aturan", out)
        self.assertIn("[FINDING] T10 TC-GS-DEMO-E2E-001-register: «Klausa di luar E2E» menyebut DEMO-LOGIC-02 "
                      "yang tidak ada di sourceRules spec ini", out)
        self.assertIn("[REVIEW] T10 TC-GS-DEMO-E2E-001-register: «Klausa di luar E2E» beralasan «tidak ada di data»", out)
        self.assertEqual(out.count("T10"), 3 + 1)   # three lines plus the per-code summary; V-01 bullet is clean

    def test_write_action_followed_by_surface_change_needs_a_wait_step(self):
        steps = ("1. Klik `[Save]`\n2. Buka Asset Detail aset `DU-01`\n"
                 "3. Pilih label `DU-01` dari dropdown\n4. Buka tab Labels\n"
                 "5. Klik `[Delete]` pada dialog, konfirmasi aksi pada dialog\n6. Verifikasi toast tampil\n"
                 "7. Klik `[Save]`\n8. Verifikasi toast tampil\n9. Klik `[Save]` Setup Column\n10. Buka Asset Detail\n")
        path = self.suite / self.folder / "spec.md"
        path.write_text(spec_text(self.folder, ["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"], extra_steps=steps),
                        encoding="utf-8")
        rc, out = self.run_check()
        c21 = [l for l in out.splitlines() if "C21" in l and l.startswith("[REVIEW]")]
        self.assertEqual(len(c21), 2, out)           # `[Save]` then `Buka`, and `Pilih label` then `Buka`; the rest is exempt
        self.assertTrue(all("«Tunggu aksi selesai»" in l for l in c21))

    def test_style_codes_are_kept(self):
        (self.suite / self.folder / "spec.md").write_text(
            spec_text("TC-GS-DEMO-E2E-009-other", ["F-DEMO-02a1"]).replace("- Mode: FE+BE\n", ""), encoding="utf-8")
        rc, out = self.run_check()
        self.assertIn("[FINDING] C4", out)
        self.assertIn("[FINDING] C5", out)


if __name__ == "__main__":
    unittest.main()
