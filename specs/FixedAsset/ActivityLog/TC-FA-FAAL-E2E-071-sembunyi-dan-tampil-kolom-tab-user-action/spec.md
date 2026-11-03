---
id: TC-FA-FAAL-E2E-071-sembunyi-dan-tampil-kolom-tab-user-action
title: "Setup Column Tab User Action: Sembunyikan dan Tampilkan Kolom"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-149
coverage:
  web: automated
---
# Setup Column Tab User Action: Sembunyikan dan Tampilkan Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Admin Alpha; General Settings `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (butir "Env var" di `suite.md`); password tidak ditulis di spec atau fixture.
- Data Log Tab User Action UA-01 sampai UA-15 (Pre-setup #12), seluruhnya bertanggal 18/06/26 (Asia/Jakarta), urutan default Date terbaru dahulu. Format: Date; Action; Object; Name; Field; Old Value; New Value; Modified By.
  - UA-01: 14:30; Assign; Total Control; Budi Santoso; Access Level; `—`; Total Control; Admin Alpha
  - UA-02: 14:25; Edit; Groups; Gedung A > Lantai 3 - Renovasi; Group Name; Lantai 3; Lantai 3 - Renovasi; Admin Alpha
  - UA-03: 13:00; Delete; Categories; Electronic Devices; Category Name; Electronic Devices; `—`; Admin Beta
  - UA-04: 12:45; Report Disposal; Disposal; Kendaraan Operasional (AST-2024-0088); Status; In Use; In Disposal Process; Admin Alpha
  - UA-05: 12:30; Report Damaged; Damaged; Kamera DSLR (AST-2024-0141); Status; Borrowed; Damaged; Ahmad Dahlan
  - UA-06: 12:00; Finish Audit; Audit; Task Audit Q3-Gedung A; Status; In Audit; Waiting for Approval; Admin Beta
  - UA-07: 11:30; Assign; Group Role; Citra Lestari; Manage asset & TAG — Gedung A; `—`; Assigned; Admin Alpha
  - UA-08: 11:00; Edit; Transactions; `—`; Default Loan Duration; 7 days; 14 days; Admin Beta (seed BE)
  - UA-09: 10:30; Auto-Revert; Total Control; Dewi Lestari; Access Level; Total Control; `—`; Admin Alpha
  - UA-10: 10:00; Activate; User; Citra Lestari; Status; Inactive; Active; Admin Alpha
  - UA-11: 09:30; Create; Groups; Default Group; Group Name; `—`; Default Group; System (seed BE)
  - UA-12: 09:00; Remove; Group Role; Citra Lestari; Manage asset & TAG — Gedung A; Assigned; `—`; Admin Alpha
  - UA-13: 08:30; Edit; Groups; Gedung B; Group Name; Gedung B1; Gedung B; Hendra Pratama #1
  - UA-14: 08:00; Edit; Groups; Gedung C; Group Name; Gedung C1; Gedung C; Hendra Pratama #2
  - UA-15: 07:30; Create; Groups; `Gedung Serbaguna` + nama 120 karakter; Group Name; `—`; nama sama; Admin Alpha
- Seed dan pemulihan data log lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`). Identitas data dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Spec hanya membaca baris log seed dan tidak membuat, mengubah, atau menghapus baris log maupun data Pre-setup.
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Parameter iterasi (kolom Tab User Action, urutan default): `Date`, `Action`, `Object`, `Name`, `Field`, `Old Value`, `New Value`, `Modified By`.
- Pemulihan Setup Column: hook `after` spec ini menghapus preferensi kolom di browser (butir "Pemulihan Setup Column" di `suite.md`; kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

1. Klik tab User Action

### TC-FA-FAAL-149: Sembunyikan dan tampilkan kolom lewat Popup Setup Column

2. Untuk setiap kolom pada parameter iterasi (langkah 3 sampai 18):
3. Klik header kolom Actions (⋯)
4. Klik `Setup Column...`
5. Hilangkan centang kolom
6. Verifikasi kolom-kolom selain kolom ini tampil di Live Preview
7. Verifikasi kolom hilang dari Live Preview
8. Klik `[Save]`
9. Verifikasi kolom-kolom selain kolom ini tampil di tabel
10. Verifikasi kolom hilang dari tabel
11. Muat ulang halaman (F5)
12. Verifikasi kolom tersisa pertama tampil di tabel
13. Verifikasi kolom tetap hilang dari tabel setelah muat ulang
14. Klik header kolom Actions (⋯)
15. Klik `Setup Column...`
16. Centang kembali kolom
17. Klik `[Save]`
18. Verifikasi kolom tampil kembali di tabel

## Notes

- Langkah penghubung (S-03): klik tab User Action di awal; popup dibuka ulang sesudah muat ulang karena muat ulang menutup popup. Setiap iterasi diawali dan diakhiri dengan konfigurasi default (semua kolom tampil), sehingga iterasi tidak bergantung pada hasil iterasi sebelumnya.
- Langkah 3 sampai 18 diulang untuk delapan kolom; parameter iterasi ada di Prerequisites. Tiap iterasi memuat `Verifikasi` per klausa Expected (S-01); `Verifikasi` kolom lain tampil (langkah 6 dan 9) dan kolom tersisa pertama tampil (langkah 12, klausa "kolom tersisa pertama tampil" Expected TC-FA-FAAL-149) adalah anchor positif untuk asersi absence kolom (bagian 8b butir 2).
- Ukuran spec 18 langkah nominal (130 langkah setelah ekspansi iterasi), melewati sekitar 35 karena TC-FA-FAAL-149 satu TC berupa delapan iterasi identik per kolom ("Untuk tiap kolom pada Data Uji") dengan empat klausa Expected per kolom; satu TC satu spec sehingga iterasinya tidak dapat dipecah. Blok satu kelas harness (fungsional), satu dataset (Pre-setup #12), tanpa menulis baris log.
- Pembagian TC lintas spec: TC-FA-FAAL-147, 148, dan 154 ada di spec 041.

