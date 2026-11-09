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
            f"1. Klik [+ Demo]\n2. Verifikasi form Register tampil\n{extra_steps}"
            + "".join(f"### {r}: Demo\n" for r in rules[1:]) + "\n## Notes\n- -\n")


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

    def test_a_cross_system_reason_for_a_surface_the_suite_can_read_is_a_review_lead(self):
        """C32 (run 9, DA F-1 and RP F-5): «lintas sistem» for the Activity Log or a token while suite.md says the suite reads them."""
        notes = "## Notes\n- Klausa di luar E2E: `DEMO:V-01` entri Activity Log ditulis lintas sistem (efek server murni)\n- -\n"
        text = spec_text(self.folder, ["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"]).replace("## Notes\n- -\n", notes)
        (self.suite / self.folder / "spec.md").write_text(text, encoding="utf-8")
        self.assertNotIn("C32", self.run_check()[1])
        (self.suite / "suite.md").write_text("# Suite\n\nKemampuan: membaca Activity Log dan System Log aktor lewat sesi API.\n", encoding="utf-8")
        self.assertIn("[REVIEW] C32", self.run_check()[1])
        (self.suite / "suite.md").write_text("# Suite\n\nKemampuan: menggeser jam server.\n", encoding="utf-8")
        self.assertNotIn("C32", self.run_check()[1])

    def test_at_least_one_row_on_a_permanent_audit_trail_and_a_pointer_without_rule_id_are_review_leads(self):
        """C33 (DA F-8): constant-value «sedikitnya satu baris» on a log; T14 REVIEW: «spec NNN» with no rule id before it cannot be checked."""
        self.write_spec(["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"], extra_steps="3. Verifikasi Wallet Transaction List memuat sedikitnya satu baris Qty `1`\n")
        self.assertIn("[REVIEW] C33", self.run_check()[1])
        self.write_spec(["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"], extra_steps="3. Verifikasi jumlah baris Wallet Transaction List bertambah satu dari baseline\n")
        self.assertNotIn("C33", self.run_check()[1])
        notes = "## Notes\n- Pembagian klausa lintas spec: klausa log ada di spec 002\n- -\n"
        text = spec_text(self.folder, ["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"]).replace("## Notes\n- -\n", notes)
        (self.suite / self.folder / "spec.md").write_text(text, encoding="utf-8")
        self.assertIn("[REVIEW] T24", self.run_check()[1])

    def test_delegation_naming_a_data_id_the_destination_never_uses_is_a_review_lead(self):
        """T25 (RP F-1): the vehicle rule is cited by the destination but the data id the pointer names (DU-16) is only in the pointing spec."""
        other = "TC-GS-DEMO-E2E-002-other"
        (self.suite / other).mkdir()
        (self.suite / other / "spec.md").write_text(spec_text(other, ["DEMO:V-01"]), encoding="utf-8")
        note = "- Pembagian klausa lintas spec: `DEMO:V-01` klausa Log untuk akun DU-16 ada di spec 002\n"
        text = spec_text(self.folder, ["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"]).replace("## Notes\n- -\n", "## Notes\n" + note)
        (self.suite / self.folder / "spec.md").write_text(text, encoding="utf-8")
        out = self.run_check()[1]
        self.assertIn("[REVIEW] T25", out)
        self.assertNotIn("T14", out)
        (self.suite / other / "spec.md").write_text(spec_text(other, ["DEMO:V-01"]).replace("## Notes\n", "## Notes\n- Akun DU-16 dipakai di sini\n", 1), encoding="utf-8")
        self.assertNotIn("T25", self.run_check()[1])

    def test_log_read_without_wait_and_repeated_caption_without_reset_are_review_leads(self):
        """C34: a Verifikasi on a permanent log with no wait/polling nearby; C35: the same message asserted again with no reset between."""
        ids = ["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"]
        self.write_spec(ids, extra_steps="3. Klik `[Submit]`\n4. Verifikasi Allocation Log memuat entri `Allocation created by X`\n")
        self.assertIn("[REVIEW] C34", self.run_check()[1])
        self.write_spec(ids, extra_steps="3. Verifikasi Allocation Log memuat entri `Allocation created by X`\n")
        self.assertNotIn("C34", self.run_check()[1])                      # entries seeded in `before`: no write of this spec to wait for
        self.write_spec(ids, extra_steps="3. Tutup dan buka modal tiap 5 detik sampai entri tampil (maks 2 menit)\n4. Verifikasi Allocation Log memuat entri `Allocation created by X`\n")
        self.assertNotIn("C34", self.run_check()[1])
        msg = 'Verifikasi caption "Passwords do not match" tampil di bawah field'
        self.write_spec(ids, extra_steps=f"3. {msg}\n4. Ganti isi Confirm\n5. {msg}\n6. Ganti isi Confirm\n7. {msg}\n")
        self.assertIn("[REVIEW] C35", self.run_check()[1])
        self.write_spec(ids, extra_steps=f"3. {msg}\n4. Muat ulang halaman\n5. {msg}\n6. Muat ulang halaman\n7. {msg}\n")
        self.assertNotIn("C35", self.run_check()[1])

    def test_delegation_duty_nobody_names_is_a_review_lead_and_the_new_widget_duties_are_enforced(self):
        """T26: `Delegasi: <doc> §<n>` must be named under the rule's `###`; T18: the three widget duties added from the M* classification."""
        ids = ["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"]
        rules = json.loads(json.dumps(RULES))
        for r in rules["rules"]:
            if r["qid"] == "F-DEMO-02a1":
                r["text"] = "Peringatan mengikuti approval-foundation"
                r["duties"] = [{"duty": "Delegasi: approval-foundation §1.7", "pillar": "P0", "ref": "approval-foundation.md §1.7", "text": "x"},
                               {"duty": "Form: Esc pada dialog Unsaved Changes", "pillar": "P3", "ref": "prd-conventions §24.5", "text": "x"}]
        self.rules.write_text(json.dumps(rules), encoding="utf-8")
        self.write_spec(ids)
        out = self.run_check()[1]
        self.assertIn("[REVIEW] T26 F-DEMO-02a1", out)
        self.assertIn("[FINDING] T18 F-DEMO-02a1: klausa «Form: Esc pada dialog Unsaved Changes»", out)
        self.write_spec(ids, extra_steps="3. Tekan Esc pada dialog Unsaved Changes; dialog tertutup dan form tetap terbuka\n"
                                         "4. Verifikasi peringatan sesuai approval-foundation §1.7 tampil\n")
        out = self.run_check()[1]
        self.assertNotIn("T26", out)
        self.assertNotIn("Esc pada dialog Unsaved Changes", out)
        self.assertNotIn("T13", out)

    def test_function_literal_only_in_an_action_step_conditional_step_and_owner_module_reason(self):
        """T19: a `Klausa fungsi:` literal typed in an action but never verified; C24: a branching action step; «dimiliki modul lain» stays no reason (R-28)."""
        ids = ["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"]
        rules = json.loads(json.dumps(RULES))
        for r in rules["rules"]:
            if r["qid"] == "F-DEMO-02a1":
                r["text"] = "Register"
                r["duties"] = [{"duty": "Klausa fungsi: Halaman Email Sent! tampil", "pillar": "P0", "ref": "F", "text": 'Halaman "Email Sent!" tampil tanpa toast'}]
        self.rules.write_text(json.dumps(rules), encoding="utf-8")
        self.write_spec(ids, extra_steps='3. Klik [Lanjut] menuju halaman "Email Sent!"\n')
        out = self.run_check()[1]
        self.assertIn("[FINDING] T19 F-DEMO-02a1", out)
        self.write_spec(ids, extra_steps='3. Klik [Lanjut]\n4. Verifikasi halaman "Email Sent!" tampil tanpa toast\n')
        self.assertNotIn("T19", self.run_check()[1])
        self.write_spec(ids, extra_steps="3. Centang checkbox bila belum tercentang\n")
        self.assertIn("[REVIEW] C24", self.run_check()[1])
        self.assertFalse(check.VALID_REASON.search("dimiliki modul lifecycle-settings, diuji di suite LifecycleSettings"))   # R-28: «modul lain» is not a reason

    def test_cell_duty_match_is_a_word_set_and_may_be_met_under_an_owner_rule(self):
        """T18 on `match` duties: «Wallet Balance» is met by «Wallet ... Balance Card»; a toast owned by another rule counts under that rule's block."""
        ids = ["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"]
        rules = json.loads(json.dumps(RULES))
        for r in rules["rules"]:
            if r["qid"] == "F-DEMO-02a1":
                r["text"] = "Approve"
                r["duties"] = [{"duty": "Sync Permukaan: Wallet Balance", "match": ["Wallet Balance"], "pillar": "P6", "ref": "L1", "text": "x"},
                               {"duty": "Resiliensi On Failure: toast", "match": ["Error, failed to approve transaction."], "owners": ["DEMO:V-01"],
                                "pillar": "P9", "ref": "L2", "text": "x"}]
        self.rules.write_text(json.dumps(rules), encoding="utf-8")
        self.write_spec(ids)
        out = self.run_check()[1]
        self.assertIn("«Sync Permukaan: Wallet Balance»", out)
        self.assertIn("«Resiliensi On Failure: toast»", out)
        text = spec_text(self.folder, ids, extra_steps="3. Buka Wallet\n4. Verifikasi Balance Card menampilkan $375.00\n").replace(
            "### DEMO:V-01: Demo\n", "### DEMO:V-01: Demo\n5. Verifikasi toast `Error, failed to approve transaction.` tampil\n")
        (self.suite / self.folder / "spec.md").write_text(text, encoding="utf-8")
        out = self.run_check()[1]
        self.assertNotIn("Wallet Balance»", out)
        self.assertNotIn("«Resiliensi On Failure: toast»", out)

    def test_run11_audit_leads_email_count_top_row_log_search_by_email_and_stacked_error_toasts(self):
        """C36-C39 [REVIEW]: the four shapes of the run 11 audit."""
        ids = ["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"]
        self.write_spec(ids, extra_steps="3. Klik [Kirim]\n4. Verifikasi tepat satu email baru diterima dibanding baseline\n")
        self.assertIn("[REVIEW] C36", self.run_check()[1])
        self.write_spec(ids, extra_steps="3. Klik [Kirim]\n4. Tunggu hingga kotak menerima email baru terhadap baseline (polling 5 detik, batas 2 menit)\n"
                                         "5. Verifikasi tepat satu email baru diterima dibanding baseline\n")
        self.assertNotIn("C36", self.run_check()[1])
        self.write_spec(ids, extra_steps="3. Mundurkan jam server: waktu nyata dikurangi 10 menit\n4. Verifikasi tiga baris teratas memuat entri Failed\n")
        self.assertIn("[REVIEW] C37", self.run_check()[1])
        self.write_spec(ids, extra_steps="3. Verifikasi tiga baris teratas memuat entri Failed\n")
        self.assertNotIn("C37", self.run_check()[1])                      # no backward clock in this spec
        self.write_spec(ids, extra_steps="3. Buka Global Settings > Activity Log > Session, ketik Search ayu@example.com, tekan Enter.\n")
        self.assertIn("[REVIEW] C38", self.run_check()[1])
        self.write_spec(ids, extra_steps="3. Buka Global Settings > Activity Log > Session, ketik Search nama depan `Rstpwd{runId}-097i`, tekan Enter.\n")
        self.assertNotIn("C38", self.run_check()[1])
        self.write_spec(ids, extra_steps="3. Verifikasi toast Error `Error, failed to send` tampil\n4. Klik [Kirim] lagi\n5. Verifikasi toast Error `Error, failed to send` tampil\n")
        self.assertIn("[REVIEW] C39", self.run_check()[1])
        self.write_spec(ids, extra_steps="3. Verifikasi toast Error `Error, failed to send` tampil\n4. Tutup toast\n5. Klik [Kirim] lagi\n6. Verifikasi toast Error `Error, failed to send` tampil\n")
        self.assertNotIn("C39", self.run_check()[1])

    def test_state_duties_need_a_verifikasi_line_that_reads_the_state(self):
        """`Mutasi: …` and `Penolakan: …` are met by a Verifikasi line, not by a word in an action step of the block."""
        rules = json.loads(json.dumps(RULES))
        target = next(r for r in rules["rules"] if r["qid"] == "F-DEMO-02a1")
        target["text"] = "Register: record disimpan; Register ditolak server bila nama sudah ada"
        target["duties"] = [{"duty": "Mutasi: data backend dan efek samping", "ref": "testcase-conventions §4", "text": "x"},
                                       {"duty": "Penolakan: state tidak berubah", "ref": "P8", "text": "x"}]
        self.rules.write_text(json.dumps(rules), encoding="utf-8")
        ids = ["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"]
        self.write_spec(ids, extra_steps="3. Klik [Simpan] lalu buka ulang token dan password tetap\n")      # words in an action step only
        out = self.run_check()[1]
        self.assertIn("«Mutasi: data backend dan efek samping»", out)
        self.assertIn("«Penolakan: state tidak berubah»", out)
        self.write_spec(ids, extra_steps="3. Klik [Simpan]\n4. Verifikasi status token menjadi consumed lewat fixture\n"
                                         "5. Kirim ulang dengan password kosong\n6. Verifikasi password lama tetap berlaku: login dengan password lama berhasil\n")
        out = self.run_check()[1]
        self.assertNotIn("«Mutasi: data backend dan efek samping»", out)
        self.assertNotIn("«Penolakan: state tidak berubah»", out)

    def test_accepted_side_and_status_restore_duties(self):
        rules = json.loads(json.dumps(RULES))
        target = next(r for r in rules["rules"] if r["qid"] == "F-DEMO-02a1")
        target["text"] = "Register: Name maks. 120 karakter; akun inactive ditolak dengan caption"
        target["duties"] = [{"duty": "Batas: sisi lolos", "ref": "P2", "text": "x"}, {"duty": "Status: pulihkan lalu ulangi", "ref": "P8", "text": "x"}]
        self.rules.write_text(json.dumps(rules), encoding="utf-8")
        ids = ["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"]
        self.write_spec(ids, extra_steps="3. Ketik 121 karakter\n4. Verifikasi caption Max. 120 characters tampil\n")
        out = self.run_check()[1]
        self.assertIn("«Batas: sisi lolos»", out)
        self.assertIn("«Status: pulihkan lalu ulangi»", out)
        self.write_spec(ids, extra_steps="3. Ketik tepat 120 karakter, klik [Register]\n4. Verifikasi Register diterima tanpa caption dan record tersimpan\n"
                                         "5. Aktifkan kembali akun lewat Global Settings > User\n6. Klik [Register] lagi\n7. Verifikasi Register berhasil diproses\n")
        out = self.run_check()[1]
        self.assertNotIn("«Batas: sisi lolos»", out)
        self.assertNotIn("«Status: pulihkan lalu ulangi»", out)

    def test_run12_false_positives_and_the_intercept_state_lead(self):
        """Run 12: C36 read «Halaman 2 Email Sent!» and «S + 25 jam» as counts, C39 flagged the persistence check, T22 flagged the S-14 sentence; C40 is new."""
        ids = ["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"]
        self.write_spec(ids, extra_steps="3. Verifikasi Halaman 2 Email Sent! tampil\n4. Verifikasi tombol `Resend email` tampil (hitung mundur selesai pada S + 25 jam)\n")
        self.assertNotIn("C36", self.run_check()[1])
        self.write_spec(ids, extra_steps="3. Verifikasi toast Error `Error, failed to send` tampil\n4. Tunggu 6 detik.\n5. Verifikasi toast Error `Error, failed to send` masih tampil\n")
        self.assertNotIn("C39", self.run_check()[1])
        self.write_spec(ids, extra_steps="3. Pasang intercept yang membalas Submit dengan status 500.\n4. Klik [Submit]\n5. Tutup toast, lalu lepas intercept.\n"
                                         "6. Verifikasi lewat fixture BE: token tetap active\n")
        self.assertIn("[REVIEW] C40", self.run_check()[1])
        self.write_spec(ids, extra_steps="3. Pasang intercept yang menahan Submit sampai batas waktu.\n4. Klik [Submit]\n5. Lepas intercept.\n"
                                         "6. Klik [Submit] tanpa intercept\n7. Verifikasi lewat fixture BE: token consumed\n")
        self.assertNotIn("C40", self.run_check()[1])              # a real request reached the server before the read
        spec = self.suite / self.folder / "spec.md"
        spec.write_text(spec.read_text(encoding="utf-8").replace("## Notes\n- -", "## Notes\n- Urutan baris log tidak diasersi; yang diasersi keanggotaannya (S-14)."), encoding="utf-8")
        self.assertNotIn("T22", self.run_check()[1])

    def test_a_delegated_clause_label_must_be_in_the_target_steps(self):
        """T27 (run 12 F-2): the target cites the rule but asserts another clause; the label of the delegated clause is not in its steps."""
        out = []
        rules = {"F-DEMO-04": {"duties": [{"duty": "Klausa fungsi: Rate limit per IP Submit"}]}}
        target = "## Test Steps\n### F-DEMO-04: x\n1. Verifikasi rollback lewat fixture\n## Notes\n- Rate limit per IP Submit ada di spec 144\n"
        check.label_check("A", "139", "`F-DEMO-04` Rate limit per IP Submit: spec 139", {"F-DEMO-04"}, rules, target, set(), lambda *a: out.append(a))
        self.assertEqual([o[1] for o in out], ["T27"])
        out.clear()
        target = "## Test Steps\n1. Verifikasi Submit ke-21 per IP ditolak: rate limit\n"
        check.label_check("A", "144", "`F-DEMO-04` Rate limit per IP Submit: spec 144", {"F-DEMO-04"}, rules, target, set(), lambda *a: out.append(a))
        self.assertEqual(out, [])

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
        self.assertIn("[FINDING] T10 TC-GS-DEMO-E2E-001-register: «Klausa di luar E2E» tanpa salah satu dari tiga alasan sah", out)  # the data hurdle
        self.assertEqual(out.count("T10"), 4 + 1)   # four lines plus the per-code summary; the V-01 server bullet is clean

    def test_a_klausa_di_luar_e2e_bullet_needs_one_of_the_three_legitimate_reasons(self):
        bullets = {"data": ("- Klausa di luar E2E: `F-DEMO-02a1` (default sort); tidak ada baris data uji yang membedakannya\n", True),
                   "volume": ("- Klausa di luar E2E: `F-DEMO-02a1` (Selection Limit); nilai ambang milik modul lain dan baru teramati pada volume besar\n", True),
                   "client": ("- Klausa di luar E2E: `F-DEMO-02a1` (unduhan di Android); perilaku klien yang sama seperti web\n", True),
                   "server": ("- Klausa di luar E2E: `F-DEMO-02a1` (retry otomatis); perilaku murni server, TC-DEMO-BE-007\n", False),
                   "visual": ("- Klausa di luar E2E: `F-DEMO-02a1` (bayangan modal); visual yang tidak deterministik\n", False),
                   "cross": ("- Klausa di luar E2E: `F-DEMO-02a1` (email notifikasi); lintas sistem, kotak masuk di luar aplikasi\n", False),
                   "transient": ("- Klausa di luar E2E: `F-DEMO-02a1` (spinner berhenti); keadaan sementara hilang sebelum teramati (8b.8)\n", False)}
        path = self.suite / self.folder / "spec.md"
        for name, (bullet, flagged) in bullets.items():
            text = spec_text(self.folder, ["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"]).replace("## Notes\n- -\n", "## Notes\n" + bullet)
            path.write_text(text, encoding="utf-8")
            out = self.run_check()[1]
            self.assertEqual("tanpa salah satu dari tiga alasan sah" in out, flagged, (name, out))

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

    def test_subheadings_are_one_per_source_rule_and_none_outside(self):
        text = spec_text(self.folder, ["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"])
        text = text.replace("### DEMO-LOGIC-01a: Demo\n", "").replace("### DEMO:V-01: Demo\n", "### F-DEMO-02a1: Dobel\n### DEMO:V-02: Luar\n")
        (self.suite / self.folder / "spec.md").write_text(text, encoding="utf-8")
        rc, out = self.run_check()
        self.assertIn("[FINDING] T12 TC-GS-DEMO-E2E-001-register: sourceRules DEMO-LOGIC-01a tanpa subjudul", out)
        self.assertIn("[FINDING] T12 TC-GS-DEMO-E2E-001-register: sourceRules DEMO:V-01 tanpa subjudul", out)
        self.assertIn("[FINDING] T13 TC-GS-DEMO-E2E-001-register: subjudul «### F-DEMO-02a1» muncul 2 kali", out)
        self.assertIn("[FINDING] T13 TC-GS-DEMO-E2E-001-register: subjudul «### DEMO:V-02» menyebut aturan yang tidak ada di sourceRules", out)

    def test_clause_delegation_must_land_in_a_spec_that_cites_the_rule(self):
        other = "TC-GS-DEMO-E2E-002-other"
        (self.suite / other).mkdir()
        (self.suite / other / "spec.md").write_text(spec_text(other, ["DEMO:V-02"]), encoding="utf-8")
        note = ("- Pembagian klausa lintas spec: `DEMO:V-01` klausa Sort ada di spec 002 dan 009; `DEMO-LOGIC-01a` klausa Tipe di spec ini. "
                "`DEMO:V-02` klausa Format di spec 002.\n")
        text = spec_text(self.folder, ["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"]).replace("## Notes\n- -\n", "## Notes\n" + note)
        (self.suite / self.folder / "spec.md").write_text(text, encoding="utf-8")
        rc, out = self.run_check()
        self.assertIn("[FINDING] T14 TC-GS-DEMO-E2E-001-register: klausa DEMO:V-01 dilimpahkan ke spec 002, tetapi spec itu tidak mengutip aturan itu", out)
        self.assertIn("[FINDING] T14 TC-GS-DEMO-E2E-001-register: «Pembagian klausa lintas spec» menyebut spec 009 yang tidak ada di suite", out)
        self.assertNotIn("klausa DEMO:V-02 dilimpahkan", out)          # spec 002 cites DEMO:V-02: a valid delegation
        self.assertNotIn("klausa DEMO-LOGIC-01a dilimpahkan", out)

    def test_shorthand_sibling_ids_in_a_delegation_are_expanded(self):
        rules = json.loads(json.dumps(RULES))
        rules["rules"] += [{"qid": "DEMO:col/name", "priority": "P2", "spectra_priority": "Medium"},
                           {"qid": "DEMO:col/role", "priority": "P2", "spectra_priority": "Medium"}]
        self.rules.write_text(json.dumps(rules), encoding="utf-8")
        other = "TC-GS-DEMO-E2E-002-other"
        (self.suite / other).mkdir()
        (self.suite / other / "spec.md").write_text(spec_text(other, ["DEMO:col/role"]), encoding="utf-8")
        note = "- Pembagian klausa lintas spec: `DEMO:col/name`, `/role` klausa Hover di spec 002.\n"
        text = spec_text(self.folder, ["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"]).replace("## Notes\n- -\n", "## Notes\n" + note)
        (self.suite / self.folder / "spec.md").write_text(text, encoding="utf-8")
        rc, out = self.run_check()
        self.assertNotIn("T14", out)        # spec 002 cites DEMO:col/role, which the shorthand `/role` names

    def test_wildcard_delegation_needs_a_spec_citing_some_matching_rule(self):
        other = "TC-GS-DEMO-E2E-002-other"
        (self.suite / other).mkdir()
        (self.suite / other / "spec.md").write_text(spec_text(other, ["DEMO:V-02"]), encoding="utf-8")
        note = "- Pembagian klausa lintas spec: `DEMO:V-*` dan `DEMO:V-/*` klausa Sort di spec 002.\n"
        text = spec_text(self.folder, ["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"]).replace("## Notes\n- -\n", "## Notes\n" + note)
        (self.suite / self.folder / "spec.md").write_text(text, encoding="utf-8")
        rc, out = self.run_check()
        self.assertNotIn("T14", out)                                    # no usable token: nothing to judge, no false finding

    def with_text(self, text):
        rules = json.loads(json.dumps(RULES))
        for r in rules["rules"]:
            if r["qid"] == "F-DEMO-02a1":
                r["text"] = text
        self.rules.write_text(json.dumps(rules), encoding="utf-8")

    def test_a_clause_naming_several_surfaces_needs_each_one_under_the_rule_heading(self):
        self.with_text("Badge menampilkan tooltip umur di User List dan Detail User.")
        self.write_spec(["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"], extra_steps="3. Buka halaman Detail User\n4. Verifikasi badge Invited tampil\n")
        rc, out = self.run_check()
        self.assertIn("[REVIEW] T15 F-DEMO-02a1: klausa menyebut permukaan «User List»", out)
        self.assertNotIn("«Detail User» tetapi", out)             # named in a step of the same block
        self.assertNotIn("[FINDING] T15", out)                    # a lead for the auditor, never a finding

    def test_a_value_in_the_rule_text_must_appear_under_the_rule_heading(self):
        self.with_text("Tooltip berubah setelah 24 jam dan 48 jam sejak undangan.")
        self.write_spec(["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"], extra_steps="3. Verifikasi tooltip pada umur 24 jam tepat\n")
        rc, out = self.run_check()
        self.assertIn("[REVIEW] T16 F-DEMO-02a1: nilai «48 jam»", out)
        self.assertNotIn("nilai «24 jam»", out)

    def test_an_exclusive_clause_needs_an_absence_assertion_but_not_a_negated_hanya(self):
        self.with_text("Tombol Resend hanya tampil untuk status Invited.")
        rc, out = self.run_check()
        self.assertIn("[REVIEW] T17 F-DEMO-02a1: klausa «hanya/selain/kecuali»", out)
        self.write_spec(["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"], extra_steps="3. Verifikasi tombol Resend tidak ada pada status Active\n")
        self.assertNotIn("T17", self.run_check()[1])
        self.with_text("Status tidak hanya dibedakan lewat warna.")
        self.write_spec(["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"])
        self.assertNotIn("T17", self.run_check()[1])

    def test_a_column_row_clause_needs_a_verifikasi_under_the_row_heading(self):
        rules = json.loads(self.rules.read_text(encoding="utf-8"))
        for r in rules["rules"]:
            if r["qid"] == "F-DEMO-02a1":
                r["text"] = "Kolom Date | Visible"
                r["duties"] = [{"duty": "Sort", "pillar": "P5", "text": "Sort kolom Date", "was": "DEMO:obl/T-1/sort/date"},
                               {"duty": "Nilai kosong", "pillar": "P11", "text": "Nilai kosong", "was": "DEMO:obl/T-1/empty-value/date"}]
        self.rules.write_text(json.dumps(rules), encoding="utf-8")
        # the keyword may sit on an action step: the clause is named under the row heading
        self.write_spec(["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"], extra_steps="3. Klik header Date\n4. Verifikasi baris terurut\n")
        rc, out = self.run_check()
        self.assertIn("[FINDING] T18 F-DEMO-02a1: klausa baris «Nilai kosong»", out)   # clauses that were rules gated by T1 stay gated
        self.assertNotIn("klausa baris «Sort»", out)
        self.write_spec(["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"], extra_steps="3. Verifikasi sort naik\n4. Verifikasi sel kosong tampil\n")
        self.assertNotIn("T18", self.run_check()[1])
        # «turunan» is not «turun»; an em dash alone is not «nilai kosong»
        self.write_spec(["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"], extra_steps="3. Verifikasi data turunan — selesai\n")
        out = self.run_check()[1]
        self.assertIn("klausa baris «Sort»", out)
        self.assertIn("klausa baris «Nilai kosong»", out)
        # a waiver: the Notes name the row rule and the clause
        text = (self.suite / self.folder / "spec.md").read_text(encoding="utf-8").replace(
            "## Notes\n- -\n", "## Notes\n- Klausa di luar E2E: F-DEMO-02a1 klausa Sort dan Nilai kosong, visual non-deterministik pada data seed.\n")
        (self.suite / self.folder / "spec.md").write_text(text, encoding="utf-8")
        self.assertNotIn("T18", self.run_check()[1])

    def test_a_widget_clause_of_an_obligation_needs_a_verifikasi_or_a_waiver(self):
        """Platform clauses of a table widget (testcase-conventions P5) are `duties` of its obligation; same T18, no `was`."""
        rules = json.loads(self.rules.read_text(encoding="utf-8"))
        for r in rules["rules"]:
            if r["qid"] == "F-DEMO-02a1":
                r["text"] = "Filter Panel tabel Demo"
                r["duties"] = [{"duty": "Filter: OR dalam field", "pillar": "P5", "text": "Dua opsi dalam satu field digabung OR", "ref": "P5 5o"},
                               {"duty": "Filter: hapus chip", "pillar": "P5", "text": "Klik ✕ pada chip menghapus centang", "ref": "P5 5p.2"},
                               {"duty": "Setup Column: simpan dan F5", "pillar": "P5", "text": "Bertahan setelah F5", "ref": "P5 5j"}]
        self.rules.write_text(json.dumps(rules), encoding="utf-8")
        steps = "3. Verifikasi dua opsi Action terpilih menampilkan gabungan OR\n4. Klik ✕ pada chip kedua\n5. Verifikasi centang opsi itu hilang\n"
        self.write_spec(["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"], extra_steps=steps)
        out = self.run_check()[1]
        self.assertIn("[FINDING] T18 F-DEMO-02a1: klausa «Setup Column: simpan dan F5» (P5 5j: Bertahan setelah F5)", out)
        self.assertNotIn("«Filter: OR dalam field»", out)
        self.assertNotIn("«Filter: hapus chip»", out)
        # «Search» in a step does not satisfy a chip clause, and a waiver names the rule and the clause label
        self.write_spec(["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"], extra_steps="3. Verifikasi pencarian mengembalikan baris\n")
        out = self.run_check()[1]
        self.assertIn("«Filter: OR dalam field»", out)
        self.assertIn("«Filter: hapus chip»", out)
        text = (self.suite / self.folder / "spec.md").read_text(encoding="utf-8").replace(
            "## Notes\n- -\n", "## Notes\n- Klausa di luar E2E: F-DEMO-02a1 klausa Filter: OR dalam field, Filter: hapus chip, Setup Column: simpan dan F5, "
                               "cross-system pada layanan sinkron.\n")
        (self.suite / self.folder / "spec.md").write_text(text, encoding="utf-8")
        self.assertNotIn("T18", self.run_check()[1])

    def test_a_clause_admitted_as_not_asserted_needs_a_legitimate_disposition(self):
        """T22: «belum diasersi» in a spec's Notes is a silent gap unless the bullet is also a «Klausa di luar E2E», a «Temuan PRD» or a held rule."""
        self.write_spec(["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"])
        path = self.suite / self.folder / "spec.md"
        base = path.read_text(encoding="utf-8")
        silent = base.replace("## Notes\n- -\n", "## Notes\n- Klausa Selection Limit pada F-DEMO-02a1 belum diasersi, menunggu data dari pemilik.\n")
        path.write_text(silent, encoding="utf-8")
        out = self.run_check()[1]
        self.assertIn("[FINDING] T22", out)
        # a Temuan PRD without the rule, and phrasing variants, are still silent gaps
        for bad in ("Temuan PRD: klausa Selection Limit belum diasersi karena PRD diam.", "Klausa Selection Limit pada F-DEMO-02a1 tidak diasersi.",
                    "1. Klausa Selection Limit belum diverifikasi, kebutuhan terbuka pemilik."):
            path.write_text(base.replace("## Notes\n- -\n", f"## Notes\n- {bad}\n"), encoding="utf-8")
            self.assertIn("[FINDING] T22", self.run_check()[1], bad)
        for ok in ("Temuan PRD: F-DEMO-02a1 klausa Selection Limit belum diasersi karena PRD diam.",
                   "Klausa di luar E2E: F-DEMO-02a1 klausa Selection Limit belum diasersi, efek server murni.",
                   "Klausa Selection Limit belum diasersi di spec ini, dibagi ke spec 041 (Pembagian klausa lintas spec)."):
            path.write_text(base.replace("## Notes\n- -\n", f"## Notes\n- {ok}\n"), encoding="utf-8")
            self.assertNotIn("T22", self.run_check()[1], ok)

    def test_a_clause_with_no_object_on_the_surface_is_waived_by_a_tidak_berlaku_bullet_with_a_prd_reference(self):
        """R-11 of the 2026-11-06 review: a clause the table has no object for needs a home that is not a faked reason: «Tidak berlaku» naming the rule, the clause and a PRD line."""
        rules = json.loads(self.rules.read_text(encoding="utf-8"))
        for r in rules["rules"]:
            if r["qid"] == "F-DEMO-02a1":
                r["text"] = "Filter Panel tabel Demo"
                r["duties"] = [{"duty": "Setup Column: batas pin", "pillar": "P5", "text": "Pin ke-4 ditolak", "ref": "P5 5j"}]
        self.rules.write_text(json.dumps(rules), encoding="utf-8")
        self.write_spec(["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"], extra_steps="3. Verifikasi batas karakter Name 120\n")
        self.assertIn("«Setup Column: batas pin»", self.run_check()[1])            # «batas karakter» no longer satisfies the pin limit
        path = self.suite / self.folder / "spec.md"
        text = path.read_text(encoding="utf-8")
        path.write_text(text.replace("## Notes\n- -\n", "## Notes\n- Tidak berlaku: F-DEMO-02a1 klausa Setup Column: batas pin, tabel hanya dua kolom data (PRD L243).\n"), encoding="utf-8")
        self.assertNotIn("T18", self.run_check()[1])
        path.write_text(text.replace("## Notes\n- -\n", "## Notes\n- Tidak berlaku: F-DEMO-02a1 klausa Setup Column: batas pin, tabel hanya dua kolom data.\n"), encoding="utf-8")
        self.assertIn("T18", self.run_check()[1])                                    # no PRD reference: not a disposition

    def test_prose_not_applicable_clause_is_a_finding_and_the_fixed_sentence_is_not(self):
        """T23: a clause with no object is written with the fixed sentence `Tidak berlaku: <aturan> klausa <label> (PRD L<n>)`; free prose is not validated by T18/T22."""
        self.write_spec(["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"])
        path = self.suite / self.folder / "spec.md"
        base = path.read_text(encoding="utf-8")
        for bad in ("Klausa batas pin tidak berlaku karena tabel hanya dua kolom.", "Klausa checkbox Disabled tidak ada permukaan di tabel ini."):
            path.write_text(base.replace("## Notes\n- -\n", f"## Notes\n- {bad}\n"), encoding="utf-8")
            self.assertIn("[FINDING] T23", self.run_check()[1], bad)
        for ok in ("Tidak berlaku: F-DEMO-02a1 klausa batas pin, tabel hanya dua kolom data (PRD L243).",
                   "Pembagian klausa lintas spec: F-DEMO-02a1: klausa batas pin tidak berlaku (lihat spec 002).",
                   "Temuan PRD: klausa batas pin tidak berlaku karena PRD diam."):
            path.write_text(base.replace("## Notes\n- -\n", f"## Notes\n- {ok}\n"), encoding="utf-8")
            self.assertNotIn("T23", self.run_check()[1], ok)

    def test_a_long_spec_cannot_justify_its_length_with_block_dependency(self):
        """C25: above 35 steps the Notes reason must not admit that a block uses an earlier block's state (that is the reason to split); a claim of independence passes."""
        steps = "".join(f"{n}. Klik tombol {n}\n" for n in range(3, 40))
        self.write_spec(["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"], extra_steps=steps)
        path = self.suite / self.folder / "spec.md"
        base = path.read_text(encoding="utf-8")
        reasons = {"- Alasan di atas 35 langkah: blok kedua memakai hasil blok sebelumnya.": True,
                   "- Spec melewati 35 langkah karena walkthrough masih terbuka dari langkah 12.": True,
                   "- Spec melewati 35 langkah karena klausanya banyak; tidak ada blok yang memakai data blok lain.": False}
        for reason, flagged in reasons.items():
            path.write_text(base.replace("## Notes\n- -\n", f"## Notes\n{reason}\n"), encoding="utf-8")
            out = self.run_check()[1]
            self.assertEqual("[FINDING] C25" in out, flagged, reason)

    def test_step_limit_c6_accepts_a_real_reason_and_c26_only_flags_the_length(self):
        """Run 6: C6 only accepted the literal phrase «35 langkah» (an owner added it to seven specs to pass); C26 is a [REVIEW] lead above 50 steps, never a limit (decision 2026-11-06: the spec is still written)."""
        steps = "".join(f"{n}. Klik tombol {n}\n" for n in range(3, 40))
        self.write_spec(["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"], extra_steps=steps)
        path = self.suite / self.folder / "spec.md"
        base = path.read_text(encoding="utf-8")
        path.write_text(base, encoding="utf-8")
        self.assertIn("[FINDING] C6", self.run_check()[1])                       # no reason at all
        path.write_text(base.replace("## Notes\n- -\n", "## Notes\n- Panjang spek ini karena jumlah klausa aturan; tiap blok menyiapkan state sendiri.\n"), encoding="utf-8")
        out = self.run_check()[1]
        self.assertNotIn("C6", out)
        self.assertNotIn("C26", out)                                             # 39 steps: a reason is enough
        long_steps = "".join(f"{n}. Klik tombol {n}\n" for n in range(3, 56))
        self.write_spec(["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"], extra_steps=long_steps)
        path.write_text(path.read_text(encoding="utf-8").replace("## Notes\n- -\n", "## Notes\n- Panjang spek ini karena jumlah klausa aturan; tiap blok menyiapkan state sendiri.\n"), encoding="utf-8")
        out = self.run_check()[1]
        self.assertIn("[REVIEW] C26", out)
        self.assertNotIn("[FINDING] C26", out)

    def test_nothing_changed_assertion_after_an_intercepted_failure_is_vacuous(self):
        """C27 [REVIEW]: the request never reaches the backend after an intercept answers 500, so «tidak ada entri» passes whatever the backend does."""
        vacuous = ("3. Pasang `Spectra.intercept` yang menjawab status 500 pada request hapus\n4. Klik tombol `[Delete]` pada dialog\n"
                   "5. Verifikasi toast `Error, failed to delete division.`\n6. Verifikasi tidak ada item terhapus dari daftar\n")
        self.write_spec(["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"], extra_steps=vacuous)
        self.assertIn("[REVIEW] C27", self.run_check()[1])
        passthrough = vacuous.replace("yang menjawab status 500", "pass-through yang menjawab status 500 sekali lalu meneruskan request")
        self.write_spec(["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"], extra_steps=passthrough)
        self.assertNotIn("C27", self.run_check()[1])

    def test_a_clause_moved_to_a_spec_with_plain_words_is_checked_like_a_delegation(self):
        """T14 also reads «ada di spec NNN» bullets that lack the heading (Position 076 → 064): the destination must cite the rule."""
        self.write_spec(["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"])
        path = self.suite / self.folder / "spec.md"
        base = path.read_text(encoding="utf-8")
        path.write_text(base.replace("## Notes\n- -\n", "## Notes\n- Klausa 5xx dari `DEMO:V-01` ada di spec 099.\n"), encoding="utf-8")
        self.assertIn("[FINDING] T14", self.run_check()[1])
        path.write_text(base.replace("## Notes\n- -\n", "## Notes\n- `DEMO:V-01` dikutip hanya di spec ini; opsi lain ada di spec 099.\n"), encoding="utf-8")
        self.assertNotIn("T14", self.run_check()[1])

    def test_a_delegation_with_words_between_the_verb_and_the_spec_number_is_checked(self):
        """Run 8 Position: «diasersi oleh aturan FI masing-masing ... di spec 033 dan 043» moved the assertions away and the destination did not cite the rule."""
        self.write_spec(["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"])
        path = self.suite / self.folder / "spec.md"
        base = path.read_text(encoding="utf-8")
        path.write_text(base.replace("## Notes\n- -\n", "## Notes\n- Perilaku `DEMO:V-01` diasersi oleh aturan FI masing-masing, yaitu di spec 099.\n"), encoding="utf-8")
        self.assertIn("[FINDING] T14", self.run_check()[1])
        path.write_text(base.replace("## Notes\n- -\n", "## Notes\n- Perilaku `DEMO:V-01` diuji pada langkah 3; yang lain tidak dipindah.\n"), encoding="utf-8")
        self.assertNotIn("T14", self.run_check()[1])

    def test_role_loop_steps_count_once_per_role_toward_the_length_limits(self):
        """Run 7: «Untuk setiap role …» steps run once per role, so 32 nominal steps with 20 loop steps and 2 roles are 52 steps (C26)."""
        loop = "".join(f"{n}. Untuk setiap role pada tabel Role yang diuji: buka halaman {n}\n" for n in range(3, 24))
        rest = "".join(f"{n}. Klik tombol {n}\n" for n in range(24, 35))
        self.write_spec(["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"], extra_steps=loop + rest)
        path = self.suite / self.folder / "spec.md"
        text = path.read_text(encoding="utf-8")
        table = "- Role yang diuji:\n\n| Role | Akun | Env password |\n|---|---|---|\n| Total Control | DU-01 | `a` |\n| Read Only | DU-03 | `b` |\n\n"
        text = text.replace("## Test Steps", table + "## Test Steps", 1).replace("## Notes\n- -\n", "## Notes\n- Panjang spek ini karena jumlah klausa aturan; tiap blok menyiapkan state sendiri.\n")
        path.write_text(text, encoding="utf-8")
        out = self.run_check()[1]
        self.assertIn("[REVIEW] C26", out)
        self.assertIn("setelah ekspansi perulangan role", out)
        path.write_text(text.replace("| Read Only | DU-03 | `b` |\n", ""), encoding="utf-8")      # one role: no expansion
        self.assertNotIn("C26", self.run_check()[1])

    def test_waiting_for_an_error_toast_to_disappear_never_finishes(self):
        """C28 [REVIEW]: a Toast Error stays until closed by hand; «Tunggu toast … hilang otomatis» after one is a step that cannot finish. A step asserting that it stays is fine."""
        bad = "3. Klik tombol `[Submit]`\n4. Verifikasi toast error `Error, failed to create division.`\n5. Tunggu toast lama hilang otomatis.\n"
        self.write_spec(["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"], extra_steps=bad)
        self.assertIn("[REVIEW] C28", self.run_check()[1])
        good = bad.replace("5. Tunggu toast lama hilang otomatis.", "5. Verifikasi toast error bertahan dan tidak hilang otomatis setelah 5 detik.")
        self.write_spec(["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"], extra_steps=good)
        self.assertNotIn("C28", self.run_check()[1])

    def test_clicking_delete_straight_on_the_bulk_action_bar_is_the_obsolete_pattern(self):
        """C29 [FINDING]: prd-conventions §8 has one `Bulk Action` button with an overlay; a direct `[Delete]` click cannot run, with or without a spec that uses the overlay."""
        self.write_spec(["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"], extra_steps="3. Klik tombol `Bulk Action`\n4. Pilih `Delete` dari overlay\n")
        self.assertNotIn("C29", self.run_check()[1])
        for step in ("3. Klik `[Delete]` pada Bulk Action Bar", "3. Klik tombol `[Delete]` pada bar aksi massal", "3. Pilih Delete di Bulk Action Bar"):
            self.write_spec(["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"], extra_steps=step + "\n")
            self.assertIn("[FINDING] C29", self.run_check()[1], step)
        # asserting the control is visible is not clicking it
        self.write_spec(["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"], extra_steps="3. Verifikasi tombol Bulk Action tampil di Bulk Action Bar\n")
        self.assertNotIn("C29", self.run_check()[1])

    def test_a_data_row_id_typed_as_text_and_an_invented_http_verb_are_flagged(self):
        """C30 [FINDING] (Brand audit F-13): «Ketik `DU-20`» types five characters, not the 120-character value; C31 [REVIEW] (F-14): an HTTP verb and endpoint no PRD states."""
        ok = "3. Ketik nilai 121 karakter (DU-20) di field Brand Name\n"
        self.write_spec(["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"], extra_steps=ok)
        self.assertNotIn("C30", self.run_check()[1])
        self.write_spec(["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"], extra_steps="3. Ketik `DU-20` (121 karakter) di field Brand Name\n")
        self.assertIn("[FINDING] C30", self.run_check()[1])
        self.write_spec(["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"], extra_steps="3. Intercept PATCH ke endpoint Brand dan tahan respons\n")
        self.assertIn("[REVIEW] C31", self.run_check()[1])
        self.write_spec(["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"], extra_steps="3. Intercept permintaan simpan Brand dan tahan respons\n")
        self.assertNotIn("C31", self.run_check()[1])

    def test_a_toast_absence_written_while_the_response_is_held_tests_nothing(self):
        steps = ("3. Tahan respons export\n4. Klik `[Download]`\n5. Verifikasi Loading screen tampil\n6. Verifikasi tidak ada toast sukses yang tampil\n"
                 "7. Lepas tahanan respons\n8. Verifikasi berkas terunduh\n9. Verifikasi tidak ada toast sukses yang tampil\n")
        self.write_spec(["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"], extra_steps=steps)
        out = self.run_check()[1]
        self.assertEqual(out.count("[FINDING] C23"), 1, out)
        self.assertIn("langkah 6 «tidak ada toast» saat respons masih ditahan (ditahan di langkah 3)", out)
        self.assertNotIn("langkah 5 «tidak ada toast»", out)           # a Loading screen during the hold is fine
        self.assertNotIn("langkah 9 «tidak ada toast»", out)           # after the release it is a real assertion

    def test_walking_tab_until_a_target_is_flagged_as_non_deterministic(self):
        self.write_spec(["F-DEMO-02a1", "DEMO-LOGIC-01a", "DEMO:V-01"], extra_steps="3. Tekan Tab hingga fokus pada Badge Invited\n4. Klik tab Info\n")
        rc, out = self.run_check()
        self.assertIn("[REVIEW] C22", out)
        self.assertEqual(out.count("[REVIEW] C22 "), 1)                  # the UI tab «Klik tab Info» is not a keyboard walk


if __name__ == "__main__":
    unittest.main()
