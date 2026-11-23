---
id: TC-FA-SU-E2E-481-routing-tab-transaction-admin-log-pelapor-non-admin-waiting-for-confirmation-dan-cancel-report-borrow-assignment
title: "Routing Tab Transaction Admin Log: Pelapor Non-admin Waiting for Confirmation dan Cancel Report dari Borrow dan Assignment"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1194
  - TC-FA-SU-1195
coverage:
  web: automated
---

# Routing Tab Transaction Admin Log: Pelapor Non-admin Waiting for Confirmation dan Cancel Report dari Borrow dan Assignment

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Pelaku kedua Budi Santoso (Pelapor admin) bertindak lewat sesi API; aktor Lina Marlina mengamati Tab Transaction Admin Log. Sesi pelaku kedua hanya memicu state tanpa asersi di dalamnya. Akun pelaku kedua disediakan tim FE: Budi Santoso `Spectra.env.FA_BUDI_PASSWORD` (nama usulan).
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Damaged berisi 4 baris sesuai Pre-setup #29 TC (Damaged: `Laptop Dell Latitude - 9`, `Projector Epson - 2`, `Tablet Samsung Tab - 5`, `Camera Sony A7 - 4`). Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Pelaku Pelapor umum (Aktor Borrow tanpa hak Update Group aset) bertindak lewat sesi API; nama dan akun pengguna Pelapor umum disediakan tim FE (kunci fixture usulan `pelaporUmum`, env password usulan `Spectra.env.FA_PELAPOR_PASSWORD`).
- Seed aset khusus spec ini (disediakan tim FE lewat seed API di hook `before`, dihapus di hook `after`, tidak memengaruhi Pre-setup #29): `Projector Epson - 4` (Borrow berjalan, tanpa Damage record, untuk Pelapor umum), `Projector Epson - 5` (Borrow berjalan), dan `Monitor LG 24 - 11` (Assignment berjalan), tanpa Damage record.
- Kemampuan transaksi lintas modul (disediakan tim FE/BE, tanpa endpoint karangan): Report Damaged dan Cancel Report dari halaman Borrow dan Assignment; dijalankan lewat sesi API, ditulis "... hingga ... tersimpan" (R-20). Entri log yang tercipta pada Tab Transaction Admin Log bersifat permanen dan tidak dibersihkan; hitungan memakai baseline relatif (S-12).
- State global: tidak ada; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-1194: Pelapor umum dari halaman Borrow berstatus Waiting for Confirmation tetap tercatat di sub-tab Damaged pelapor

1. Lakukan Report Damaged atas `Projector Epson - 4` sebagai pengguna Pelapor umum dari halaman Borrow lewat sesi API hingga laporan tersimpan
2. Buka halaman Damaged dan cari `Projector Epson - 4`
3. Verifikasi record `Projector Epson - 4` berstatus `Waiting for Confirmation`
4. Cari pengguna Pelapor umum lewat Search di User List, buka Detail User Pelapor umum, klik Tab Transaction Admin Log, lalu klik Sub-tab Damaged
5. Verifikasi sub-tab Damaged pelapor menampilkan satu baris Activity `Reported damaged` dengan Name `Projector Epson - 4` dan Source `Borrowed asset`
6. Verifikasi Group baris itu adalah grup aset saat tindakan
7. Klik Sub-tab Borrow
8. Verifikasi sub-tab Borrow tidak memuat baris laporan Damaged untuk `Projector Epson - 4`

### TC-FA-SU-1195: Cancel Report dari halaman Borrow dan Assignment tercatat sebagai `Report canceled` di sub-tab Damaged

9. Lakukan Report Damaged atas `Projector Epson - 5` sebagai Budi Santoso dari halaman Borrow lewat sesi API, lalu Cancel Report dari halaman Borrow yang sama hingga pembatalan tersimpan
10. Lakukan Report Damaged atas `Monitor LG 24 - 11` sebagai Budi Santoso dari halaman Assignment lewat sesi API, lalu Cancel Report dari halaman Assignment yang sama hingga pembatalan tersimpan
11. Kembali ke User List, cari Budi Santoso lewat Search, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Damaged
12. Verifikasi sub-tab Damaged menampilkan baris Activity `Report canceled` untuk `Projector Epson - 5` dengan Source `Borrowed asset`
13. Verifikasi sub-tab Damaged menampilkan baris Activity `Report canceled` untuk `Monitor LG 24 - 11` dengan Source `Assigned asset`
14. Verifikasi sub-tab Damaged menampilkan baris Activity `Reported damaged` untuk `Projector Epson - 5` dan `Monitor LG 24 - 11` di samping baris `Report canceled`
15. Klik Sub-tab Borrow
16. Verifikasi sub-tab Borrow tidak memuat baris `Report canceled` untuk `Projector Epson - 5`
17. Klik Sub-tab Assignment
18. Verifikasi sub-tab Assignment tidak memuat baris `Report canceled` untuk `Monitor LG 24 - 11`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), pencatatan baseline jumlah baris (S-12), pemicuan state lewat sesi API (R-20), pemuatan ulang halaman Detail, pembukaan panel Filter dan dropdown, serta perpindahan sub-tab dan halaman.
- Klausa absence (sub-tab Borrow dan Assignment tidak memuat baris laporan atau `Report canceled`) didahului `Verifikasi` positif baris `Reported damaged` dan `Report canceled` pada sub-tab Damaged sebagai anchor pada pengguna yang sama (8b.2).
- Pembagian TC lintas spec: Report Damaged dan Report Missing admin (TC-FA-SU-1192 dan 1193) ada di spec 479 dan 480; Cancel Report dari Task Detail Audit dan Report TAG (TC-FA-SU-1196 dan 1197) ada di spec 482.
- Temuan untuk QA (S-15): (1) TC-FA-SU-1194 menyebut pengguna Pelapor umum tanpa nama, akun, atau kredensial; spec memakai kunci fixture dan env password usulan dan memicu aksi lewat sesi API (R-20). (2) TC-FA-SU-1194 langkah 4 meminta mengamati baris Borrow untuk `Projector Epson - 4`; spec mengasersi ketiadaan baris laporan Damaged pada sub-tab Borrow pelapor. (3) Pada TC-FA-SU-1195 Expected a menyebut baris `Reported damaged` di samping `Report canceled`; spec mengasersi keberadaannya tanpa urutan. (4) Nama aset seed memakai literal TC dan harus dijamin seed.
