---
id: TC-FA-SU-E2E-482-routing-tab-transaction-admin-log-cancel-report-task-audit-dan-report-tag-tetap-di-sub-tab-audit
title: "Routing Tab Transaction Admin Log: Cancel Report dari Task Audit dan Report TAG Tetap di Sub-tab Audit"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1196
  - TC-FA-SU-1197
coverage:
  web: automated
---

# Routing Tab Transaction Admin Log: Cancel Report dari Task Audit dan Report TAG Tetap di Sub-tab Audit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Pelaku kedua Budi Santoso (Pelapor admin) bertindak lewat sesi API; aktor Lina Marlina mengamati Tab Transaction Admin Log. Sesi pelaku kedua hanya memicu state tanpa asersi di dalamnya. Akun pelaku kedua disediakan tim FE: Budi Santoso `Spectra.env.FA_BUDI_PASSWORD` (nama usulan).
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Damaged, Missing, dan Audit berisi baris sesuai Pre-setup #29 TC (Damaged: `Laptop Dell Latitude - 9`, `Projector Epson - 2`, `Tablet Samsung Tab - 5`, `Camera Sony A7 - 4`; Missing: `Printer HP LaserJet - 3`, `Monitor LG 24 - 5`, `Laptop Dell Latitude - 10`, `Camera Sony A7 - 5`; Audit: `AUD-2026-0042`, `AUD-2026-0041`). Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed aset khusus spec ini (disediakan tim FE lewat seed API di hook `before`, dihapus di hook `after`, tidak memengaruhi Pre-setup #29): task Audit `AUD-2026-0043` berjalan memuat `Monitor LG 24 - 12` (tanpa Missing record), `Laptop Dell Latitude - 14` (tanpa Damage record), dan `Laptop Dell Latitude - 13` (TAG tidak terbaca).
- Kemampuan transaksi lintas modul (disediakan tim FE/BE, tanpa endpoint karangan): Report Missing, Report Damaged, Cancel Report, dan identifikasi manual `I Can't Scan the TAG` (Report TAG) dari Task Detail Audit; dijalankan lewat sesi API, ditulis "... hingga ... tersimpan" (R-20). Entri log yang tercipta pada Tab Transaction Admin Log bersifat permanen dan tidak dibersihkan; hitungan memakai baseline relatif (S-12).
- State global: tidak ada; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-1196: Cancel Report dari Task Detail Audit tercatat sebagai `Report canceled` di sub-tab Damaged dan Missing dengan Source `Audit`

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Audit
2. Catat jumlah baris sub-tab Audit sebagai baseline
3. Lakukan Report Missing atas `Monitor LG 24 - 12` dari Task Detail Audit `AUD-2026-0043` sebagai Budi Santoso lewat sesi API hingga laporan tersimpan
4. Lakukan Report Damaged atas `Laptop Dell Latitude - 14` dari Task Detail Audit `AUD-2026-0043` sebagai Budi Santoso lewat sesi API hingga laporan tersimpan
5. Lakukan Cancel Report atas kedua laporan dari Task Detail Audit yang sama sebagai Budi Santoso lewat sesi API hingga pembatalan tersimpan
6. Tunggu aksi selesai, lalu tekan F5 pada halaman Detail
7. Klik Sub-tab Missing
8. Verifikasi sub-tab Missing menampilkan baris Activity `Report canceled` untuk `Monitor LG 24 - 12` dengan Source `Audit`
9. Verifikasi sub-tab Missing menampilkan baris Activity `Reported missing` untuk `Monitor LG 24 - 12` di samping baris `Report canceled`
10. Klik Sub-tab Damaged
11. Verifikasi sub-tab Damaged menampilkan baris Activity `Report canceled` untuk `Laptop Dell Latitude - 14` dengan Source `Audit`
12. Verifikasi sub-tab Damaged menampilkan baris Activity `Reported damaged` untuk `Laptop Dell Latitude - 14` di samping baris `Report canceled`
13. Klik Sub-tab Audit
14. Verifikasi jumlah baris sub-tab Audit sama dengan baseline (laporan dan pembatalannya tidak menambah baris)

### TC-FA-SU-1197: Report TAG dari task Audit tetap tercatat di sub-tab Audit, tidak di sub-tab Damaged atau Missing

15. Klik Sub-tab Damaged
16. Catat jumlah baris sub-tab Damaged sebagai baseline
17. Klik Sub-tab Missing
18. Catat jumlah baris sub-tab Missing sebagai baseline
19. Lakukan identifikasi manual `I Can't Scan the TAG` (Report TAG) atas `Laptop Dell Latitude - 13` dari Task Detail Audit `AUD-2026-0043` sebagai Budi Santoso (auditor) lewat sesi API hingga laporan tersimpan
20. Tunggu aksi selesai, lalu tekan F5 pada halaman Detail
21. Klik Sub-tab Audit
22. Verifikasi sub-tab Audit menampilkan baris Activity `TAG reported` dengan Transaction ID `AUD-2026-0043` dan Name `Laptop Dell Latitude - 13`
23. Verifikasi Group baris itu adalah grup aset saat tindakan
24. Klik Sub-tab Damaged
25. Verifikasi jumlah baris sub-tab Damaged sama dengan baseline
26. Klik Sub-tab Missing
27. Verifikasi jumlah baris sub-tab Missing sama dengan baseline

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), pencatatan baseline jumlah baris (S-12), pemicuan state lewat sesi API (R-20), pemuatan ulang halaman Detail, pembukaan panel Filter dan dropdown, serta perpindahan sub-tab dan halaman.
- Klausa absence (sub-tab Audit tidak menambah baris pada TC-FA-SU-1196; sub-tab Damaged dan Missing tidak menambah baris pada TC-FA-SU-1197) ditulis sebagai asersi jumlah terhadap baseline yang dicatat sebelum pemicu (S-12); anchor positif adalah baris `Report canceled` dan `Reported ...` pada Damaged dan Missing (TC-FA-SU-1196) serta baris `TAG reported` pada sub-tab Audit (TC-FA-SU-1197), diverifikasi sebelum asersi absence (8b.2).
- Pembagian TC lintas spec: Report Damaged dan Missing dari Borrow, Assignment, dan Transfer (TC-FA-SU-1192 dan 1193) ada di spec 479 dan 480; Cancel Report dari Borrow dan Assignment (TC-FA-SU-1195) ada di spec 481.
- Temuan untuk QA (S-15): (1) TC-FA-SU-1196 langkah 6 membandingkan jumlah baris sub-tab Audit dengan langkah 1; spec membandingkannya dengan baseline yang dicatat sebelum pemicu. (2) TC-FA-SU-1197 menyebut satu baris per aset yang dilaporkan dan Group aset saat tindakan tanpa nilai literal; spec tidak meng-assert nilai Group literal. (3) Task Audit `AUD-2026-0043` dan nama aset seed memakai literal TC dan harus dijamin seed. (4) Aksi dijalankan lewat sesi API (R-20) sebagai Budi Santoso.
