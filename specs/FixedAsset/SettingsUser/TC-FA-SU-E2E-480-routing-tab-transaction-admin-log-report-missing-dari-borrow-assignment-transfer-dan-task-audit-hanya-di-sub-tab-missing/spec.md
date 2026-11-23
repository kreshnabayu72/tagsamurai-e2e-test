---
id: TC-FA-SU-E2E-480-routing-tab-transaction-admin-log-report-missing-dari-borrow-assignment-transfer-dan-task-audit-hanya-di-sub-tab-missing
title: "Routing Tab Transaction Admin Log: Report Missing dari Borrow, Assignment, Transfer, dan Task Audit Hanya di Sub-tab Missing dengan Source Asal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1193
coverage:
  web: automated
---

# Routing Tab Transaction Admin Log: Report Missing dari Borrow, Assignment, Transfer, dan Task Audit Hanya di Sub-tab Missing dengan Source Asal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Pelaku kedua Budi Santoso (Pelapor admin) bertindak lewat sesi API; aktor Lina Marlina mengamati Tab Transaction Admin Log. Sesi pelaku kedua hanya memicu state tanpa asersi di dalamnya. Akun pelaku kedua disediakan tim FE: Budi Santoso `Spectra.env.FA_BUDI_PASSWORD` (nama usulan).
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Missing berisi 4 baris sesuai Pre-setup #29 TC (Missing: `Printer HP LaserJet - 3`, `Monitor LG 24 - 5`, `Laptop Dell Latitude - 10`, `Camera Sony A7 - 5`). Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed aset khusus spec ini (disediakan tim FE lewat seed API di hook `before`, dihapus di hook `after`, tidak memengaruhi Pre-setup #29): `Camera Sony A7 - 6` (Borrow berjalan), `Laptop Dell Latitude - 12` (Assignment berjalan), `Tablet Samsung Tab - 7` (Transfer berjalan), dan `Monitor LG 24 - 10` (task Audit `AUD-2026-0043` berjalan), masing-masing tanpa Missing record.
- Kemampuan transaksi lintas modul (disediakan tim FE/BE, tanpa endpoint karangan): Report Missing dari halaman Borrow, Assignment, Transfer, dan Task Detail Audit; dijalankan lewat sesi API, ditulis "... hingga ... tersimpan" (R-20). Entri log yang tercipta pada Tab Transaction Admin Log bersifat permanen dan tidak dibersihkan; hitungan memakai baseline relatif (S-12).
- State global: tidak ada; suite berjalan serial (`parallel: false`).

## Test Steps

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Borrow
2. Catat jumlah baris sub-tab Borrow sebagai baseline
3. Klik Sub-tab Assignment
4. Catat jumlah baris sub-tab Assignment sebagai baseline
5. Klik Sub-tab Transfer
6. Catat jumlah baris sub-tab Transfer sebagai baseline
7. Klik Sub-tab Audit
8. Catat jumlah baris sub-tab Audit sebagai baseline
9. Klik Sub-tab Missing
10. Catat jumlah baris sub-tab Missing sebagai baseline
11. Lakukan Report Missing atas `Camera Sony A7 - 6` sebagai Budi Santoso dari halaman Borrow lewat sesi API hingga laporan tersimpan
12. Lakukan Report Missing atas `Laptop Dell Latitude - 12` sebagai Budi Santoso dari halaman Assignment lewat sesi API hingga laporan tersimpan
13. Lakukan Report Missing atas `Tablet Samsung Tab - 7` sebagai Budi Santoso dari halaman Transfer lewat sesi API hingga laporan tersimpan
14. Lakukan Report Missing atas `Monitor LG 24 - 10` sebagai Budi Santoso dari Task Detail Audit `AUD-2026-0043` lewat sesi API hingga laporan tersimpan
15. Buka halaman Missing tab Active dan catat nilai Source keempat aset (`Camera Sony A7 - 6`, `Laptop Dell Latitude - 12`, `Tablet Samsung Tab - 7`, `Monitor LG 24 - 10`)
16. Kembali ke User List, cari Budi Santoso lewat Search, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Missing
17. Verifikasi empat baris baru tampil dengan Activity `Reported missing` untuk `Camera Sony A7 - 6`, `Laptop Dell Latitude - 12`, `Tablet Samsung Tab - 7`, dan `Monitor LG 24 - 10`
18. Verifikasi Source baris `Monitor LG 24 - 10` adalah `Audit`
19. Verifikasi Source baris `Camera Sony A7 - 6`, `Laptop Dell Latitude - 12`, dan `Tablet Samsung Tab - 7` sama dengan nilai Source pada halaman Missing yang dicatat
20. Verifikasi Group keempat baris itu adalah grup aset saat tindakan
21. Verifikasi jumlah baris sub-tab Missing bertambah tepat empat dari baseline
22. Verifikasi keempat baris Pre-setup #29 sub-tab Missing tidak berubah: `Printer HP LaserJet - 3`, `Monitor LG 24 - 5`, `Laptop Dell Latitude - 10`, `Camera Sony A7 - 5`
23. Klik Sub-tab Borrow
24. Verifikasi jumlah baris sub-tab Borrow sama dengan baseline
25. Klik Sub-tab Assignment
26. Verifikasi jumlah baris sub-tab Assignment sama dengan baseline
27. Klik Sub-tab Transfer
28. Verifikasi jumlah baris sub-tab Transfer sama dengan baseline
29. Klik Sub-tab Audit
30. Verifikasi jumlah baris sub-tab Audit sama dengan baseline

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), pencatatan baseline jumlah baris (S-12), pemicuan state lewat sesi API (R-20), pemuatan ulang halaman Detail, pembukaan panel Filter dan dropdown, serta perpindahan sub-tab dan halaman.
- Pembagian TC lintas spec: Report Damaged (TC-FA-SU-1192) ada di spec 479; pelapor non-admin dan Cancel Report (TC-FA-SU-1194 sampai 1196) ada di spec 481 dan 482.
- Klausa absence ("tidak menambah baris" pada Borrow, Assignment, Transfer, dan Audit) ditulis sebagai asersi jumlah terhadap baseline yang dicatat sebelum pemicu (S-12); anchor positif adalah empat baris `Reported missing` di sub-tab Missing yang diverifikasi sebelumnya (8b.2).
- Temuan untuk QA (S-15): (1) TC-FA-SU-1193 menyatakan nilai Source tiga baris selain Audit sebagai nilai Source record yang sama dengan kolom Source di halaman Missing (tidak di-assert literal); spec membandingkannya dengan nilai yang dicatat dari halaman Missing tab Active. (2) Aksi dijalankan lewat sesi API (R-20); nama aset seed memakai literal TC dan harus dijamin seed. (3) Task Audit `AUD-2026-0043` dipakai bersama spec 481 dan 482; seed harus menyediakan task berjalan yang memuat aset terkait. (4) Seed khusus TC menulis empat baris baru ke log Budi Santoso yang juga dibaca spec lain; asersi jumlah memakai baseline relatif.
