# Data uji <Group><SubModul>

Sumber PRD: `<path PRD inti>` · PRD sha256 `<16 hex pertama>`

<!--
Template data uji alur PRD → E2E (`docs/e2e-conventions-prd.md` bagian 5). Salin ke `docs/data/<Group><SubModul>.md`.
Spec hanya merujuk data lewat `DU-nn`; `scripts/check-suite-prd.py` T9 menolak DU-nn yang tidak ada di tabel ini.
Kolom Sumber: Example Data PRD (§4.1.x), ID aturan PRD, role matrix §2 (akun), atau "turunan planner" untuk data yang
tidak diberikan PRD (akun, volume, data dinamis); baris "turunan planner" disetujui di gate plan. Password dan email
akun hanya lewat env `<PREFIX>_<ROLE>_…`, tidak pernah literal. Hapus komentar ini di file nyata.
-->

| ID | Data | Nilai | Sumber | Lifecycle | Dipakai spec |
|---|---|---|---|---|---|
| `DU-01` | Akun Principal Total Control | env `AC_PRINCIPAL_TC_EMAIL` / `AC_PRINCIPAL_TC_PASSWORD` | §2 Role Matrix | pre-setup | 001–010 |
| `DU-02` | SKU stok 0 | `UHF Handheld Reader (HHR-ARC-100)`, Current Stock 0 | Example Data §4.1 (Device SKU List) | pre-setup | 004, 012 |
| `DU-03` | SKU baru dari form Register | SKU `E2E-SKU-<timestamp>` | turunan planner | dibuat spec 003 | 003, 005 |
