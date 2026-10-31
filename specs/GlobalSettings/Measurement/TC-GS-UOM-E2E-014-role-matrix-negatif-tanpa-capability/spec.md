---
id: TC-GS-UOM-E2E-014-role-matrix-negatif-tanpa-capability
title: "Role Matrix Negatif: Tanpa Capability dan Satu Capability Men-gate Brand serta Measurement"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-UOM-23
  - TC-GS-UOM-30
  - TC-GS-UOM-31
coverage:
  web: automated
---

# Role Matrix Negatif: Tanpa Capability dan Satu Capability Men-gate Brand serta Measurement

## Prerequisites

- Mode: FE+BE (backend nyata). Pencabutan dan pemulihan capability dilakukan lewat API oleh admin Total Control, bukan lewat UI aktor.
- Hook suite (login akun default, flag Guided Tooltip `guided_tooltip_seen_gs-measurement`): lihat `suite.md`. Layar awal: spec ini dikecualikan dari pembukaan layar oleh hook `beforeEach` suite (lihat `suite.md`, bagian Hook suite) karena akun Tanpa Capability tidak dapat membuka Tab Measurement; layar awal spec ini adalah Global Settings.
- Role yang diuji:

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-GS-UOM-23, TC-GS-UOM-30 | Tanpa Capability (bukan Total Control dan bukan Read Only) | Fajar Nugroho | `noCapability_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_NOCAP_PASSWORD` |
| TC-GS-UOM-31 | System Role: Read saja | Tono Hartono | `readCapability_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_READ_PASSWORD` |

- Login akun Tanpa Capability dilakukan di hook `before` spec ini. Langkah ganti akun ke System Role: Read saja ditulis eksplisit (langkah 10). Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `Spectra.env.GS_TC_PASSWORD`).
- Aktor admin pencabut dan pemulih capability: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (`Spectra.env.GS_TC_PASSWORD`), lewat API admin untuk mengubah capability role (kemampuan disediakan tim FE, tanpa endpoint karangan).
- Environment variable: `GS_NOCAP_PASSWORD`, `GS_READ_PASSWORD`, `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; nama env didaftarkan di `executionConfig.environmentVariables`.
- Data Pre-setup Client A (8 unit, data baca) tersedia sehingga ketiadaan baris Measurement di layar disebabkan izin, bukan data kosong. Spec tidak membuat, mengubah, atau menghapus data.
- Fixture `fixtures/measurement.json` (belum ada, disiapkan tim FE):

| Kunci | Isi | Dipakai di |
|---|---|---|
| `urlTabMeasurement` | URL langsung Tab Measurement (Global Settings > Master Reference > Measurement) | TC-GS-UOM-30 (Data Uji) |

- State global yang diubah dan dipulihkan: capability Manage master reference role System Role: Read saja (dicabut di langkah 15, dipulihkan di langkah 19 dan di hook `after` sebagai cadangan walau spec gagal di tengah). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-UOM-23: Aktor tanpa capability dan bukan Total Control/Read Only tidak melihat Tab Measurement

1. Buka Global Settings
2. Cari menu Master Reference / Tab Measurement
3. Verifikasi Tab `Measurement` Hidden
4. Verifikasi data Measurement tidak dapat dilihat

### TC-GS-UOM-30: Akses langsung URL Tab Measurement tanpa capability ditolak

5. Ketik langsung URL Tab Measurement (`urlTabMeasurement`) di address bar browser
6. Verifikasi toast: "You don't have permission to do this."
7. Verifikasi UI di-refresh sehingga Tab `Measurement` tidak tampil
8. Verifikasi tidak ada redirect ke halaman lain
9. Verifikasi tidak ada baris Measurement yang termuat

### TC-GS-UOM-31: Satu capability Manage master reference men-gate Brand dan Measurement sekaligus

10. Logout, lalu login sebagai System Role: Read saja
11. Buka Global Settings > Master Reference
12. Periksa Tab Brand dan Tab Measurement
13. Verifikasi sebelum capability dicabut, Tab `Brand` tampil
14. Verifikasi sebelum capability dicabut, Tab `Measurement` tampil
15. Admin (Total Control) mencabut capability Manage master reference dari role aktor lewat API
16. Muat ulang halaman
17. Verifikasi setelah capability dicabut, Tab `Brand` tidak tampil
18. Verifikasi setelah capability dicabut, Tab `Measurement` tidak tampil
19. Admin memulihkan capability Manage master reference role System Role: Read saja lewat API

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix negatif (bagian 3a konvensi). Role negatif lain tidak ditulis di sini karena tidak ada TC sumbernya; visibilitas elemen per role lain diuji di `TC-GS-UOM-E2E-013-role-matrix-visibilitas-elemen-per-role`. Spec ini memakai dua akun (Tanpa Capability dan Read saja) dengan langkah ganti akun eksplisit (langkah 10); bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal, dan keduanya satu kelas harness.
- TC-GS-UOM-31 berdiri terpisah dari TC-GS-UOM-30 pada akun karena mengubah capability (kelas state izin); ia satu-satunya TC di spec ini yang mengubah capability. Capability dicabut di spec lain (TC-GS-UOM-92, 260, 397) ada di `TC-GS-UOM-E2E-016-capability-dicabut-saat-aksi-berjalan`.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 10 (ganti akun), 16 (muat ulang agar capability yang dicabut terbaca), dan 19 (pemulihan capability).
- Pengecekan Hidden pada langkah 3, 17, dan 18 memakai halaman Global Settings yang sudah termuat sebagai anchor permukaan (butir 2 bagian 8b).
- Temuan untuk QA:
  - TC-GS-UOM-31 menulis "Admin mencabut capability" tanpa menyebut akun admin dan cara pencabutan; spec memakai Total Control Client A lewat API (kemampuan disediakan tim FE).
  - Hook `beforeEach` suite yang membuka Tab Measurement tidak dapat dipakai untuk akun Tanpa Capability (TC-GS-UOM-23 dan 30); `suite.md` mengecualikan spec ini dari hook itu.
  - Di TC-GS-UOM-31 hanya Expected Result "kedua Tab tidak tampil" yang ada untuk kondisi sesudah dicabut; apa yang tampil di halaman Global Settings saat tidak ada tab tidak diasersi.
