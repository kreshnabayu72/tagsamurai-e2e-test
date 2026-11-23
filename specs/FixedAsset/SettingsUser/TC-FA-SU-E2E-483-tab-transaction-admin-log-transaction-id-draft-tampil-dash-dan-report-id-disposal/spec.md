---
id: TC-FA-SU-E2E-483-tab-transaction-admin-log-transaction-id-draft-tampil-dash-dan-report-id-disposal
title: "Tab Transaction Admin Log: Transaction ID Draft Tampil Dash dan Report ID Disposal"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1198
  - TC-FA-SU-1199
coverage:
  web: automated
---

# Tab Transaction Admin Log: Transaction ID Draft Tampil Dash dan Report ID Disposal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Pelaku kedua Budi Santoso (Pelapor admin) bertindak lewat sesi API; aktor Lina Marlina mengamati Tab Transaction Admin Log. Sesi pelaku kedua hanya memicu state tanpa asersi di dalamnya. Akun pelaku kedua disediakan tim FE: Budi Santoso `Spectra.env.FA_BUDI_PASSWORD` (nama usulan).
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Transfer dan Disposal berisi data atau kosong tanpa asersi nilai (Pre-setup #29). Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed aset khusus spec ini (disediakan tim FE lewat seed API di hook `before`, dihapus di hook `after`, tidak memengaruhi Pre-setup #29): `Camera Sony A7 - 7` (tanpa transaksi Transfer berjalan), `Printer HP LaserJet - 6` (tanpa Disposal berjalan), dan `Laptop Dell Latitude - 15` (berstatus Damaged).
- Kemampuan transaksi lintas modul (disediakan tim FE/BE, tanpa endpoint karangan): membuat Transfer Draft dan men-submit Draft menjadi Transfer, membuat Disposal Draft, dan Report Disposal dari tab Damaged; dijalankan lewat sesi API, ditulis "... hingga ... tersimpan" (R-20). Entri log yang tercipta pada Tab Transaction Admin Log bersifat permanen dan tidak dibersihkan; hitungan memakai baseline relatif (S-12).
- State global: tidak ada; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-1198: Transaction ID sub-tab Transfer: aksi Draft tampil `—`, aksi non-Draft tampil nomor TRF

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Transfer
2. Catat jumlah baris sub-tab Transfer sebagai baseline
3. Buat Transfer Draft berisi `Camera Sony A7 - 7` sebagai Budi Santoso lewat sesi API hingga draft tersimpan
4. Submit Draft itu menjadi Transfer sebagai Budi Santoso lewat sesi API hingga transfer tersimpan
5. Tekan F5 pada halaman Detail dan klik Sub-tab Transfer
6. Verifikasi baris Activity `Draft created` untuk `Camera Sony A7 - 7` menampilkan Transaction ID `—` (bukan sel kosong)
7. Verifikasi baris Activity `Requested` untuk `Camera Sony A7 - 7` menampilkan nomor berawalan `TRF-`
8. Verifikasi Transaction ID baris itu berupa teks biasa, bukan tautan

### TC-FA-SU-1199: Transaction ID sub-tab Disposal: aksi Draft tampil `—`, aksi Report tampil Report ID `DRP-`

9. Klik Sub-tab Disposal
10. Catat jumlah baris sub-tab Disposal sebagai baseline
11. Buat Disposal Draft berisi `Printer HP LaserJet - 6` sebagai Budi Santoso lewat sesi API hingga draft tersimpan
12. Lakukan Report Disposal dari tab Damaged atas `Laptop Dell Latitude - 15` sebagai Budi Santoso lewat sesi API hingga laporan tersimpan
13. Tekan F5 pada halaman Detail dan klik Sub-tab Disposal
14. Verifikasi baris Activity `Draft created` untuk `Printer HP LaserJet - 6` menampilkan Transaction ID `—` (bukan sel kosong)
15. Verifikasi baris Activity `Reported` untuk `Laptop Dell Latitude - 15` menampilkan Report ID berawalan `DRP-`
16. Verifikasi Transaction ID kedua baris itu berupa teks biasa, bukan tautan

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), pencatatan baseline jumlah baris (S-12), pemicuan state lewat sesi API (R-20), pemuatan ulang halaman Detail, pembukaan panel Filter dan dropdown, serta perpindahan sub-tab dan halaman.
- Pembagian TC lintas spec: routing Report Disposal ke sub-tab Disposal (TC-FA-SU-1187) ada di spec 474.
- Temuan untuk QA (S-15): (1) TC-FA-SU-1198 dan 1199 menyebut nomor `TRF-` dan `DRP-` tanpa pola penuh; spec mengasersi awalan saja. (2) Aksi dijalankan lewat sesi API (R-20) sebagai Budi Santoso; nama aset seed memakai literal TC dan harus dijamin seed. (3) Activity `Requested` pada TC-FA-SU-1198 dan `Reported` pada TC-FA-SU-1199 mengikuti Expected TC. (4) Entri log baru bersifat permanen; baseline jumlah dicatat sebagai titik acuan dan asersi mengacu baris berdasarkan Name.
