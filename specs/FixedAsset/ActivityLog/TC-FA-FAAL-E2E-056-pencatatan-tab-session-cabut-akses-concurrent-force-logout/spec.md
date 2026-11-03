---
id: TC-FA-FAAL-E2E-056-pencatatan-tab-session-cabut-akses-concurrent-force-logout
title: "Pencatatan Tab Session: Cabut Akses, Nonaktif, Concurrent Limit, dan Force Logout"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-214
  - TC-FA-FAAL-215
  - TC-FA-FAAL-216
  - TC-FA-FAAL-217
coverage:
  web: automated
---

# Pencatatan Tab Session: Cabut Akses, Nonaktif, Concurrent Limit, dan Force Logout

## Prerequisites

- Mode: FE+BE.
- Akun observer dan aktor: Total Control (Pre-setup #1, Admin Alpha), `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Reports & Logs > Activity Log, tab Session). Pengecualian: langkah 17 membuka License > Concurrent User dan langkah 20 kembali ke Activity Log.
- Pelaku (Pre-setup #16), email dari `Fixture.activity-log.<kunci>.email` (fixture belum ada, disediakan tim FE), password lewat env var yang didaftarkan tim FE (R-07):
  - John Doe: App Access Fixed Asset dan seat subscription tersedia; password `Spectra.env.FA_JOHNDOE_PASSWORD`.
  - Siti Nurbaya: App Access Fixed Asset; password `Spectra.env.FA_SITINURBAYA_PASSWORD`.
  - Mike Tan: sesi-produk Fixed Asset aktif dibuat langkah 22; password `Spectra.env.FA_MIKETAN_PASSWORD`.
  - Ketiga env var tidak tercantum di butir "Env var" `suite.md`; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis disediakan tim BE/FE: sesi API aktor (butir "Sesi API aktor" di `suite.md`) untuk John Doe, Siti Nurbaya, Mike Tan, dan Admin Alpha (admin Total Control); kemampuan mencabut dan memulihkan App Access Fixed Asset, menonaktifkan dan mengaktifkan user di Settings > User Fixed Asset, serta Force Logout sesi di License > Concurrent User lewat sesi API aktor.
- State global untuk TC-FA-FAAL-216: limit seat subscription Fixed Asset bernilai 1 dan seat sudah dipakai user lain (disediakan tim BE/FE), diatur pada langkah 13 dan dipulihkan pada langkah 21 serta di hook `after`.
- Baseline (S-12): total baris Tab Session dibaca dari teks pagination `Showing x–y of N entries` sebelum tiap aksi pemicu; Tab Session tidak menyaring dan tidak memakai Search selama spec.
- State yang diubah dan pemulihannya: App Access Fixed Asset John Doe (langkah 6), status John Doe (langkah 12), limit seat (langkah 21), sesi-produk John Doe, Siti Nurbaya, dan Mike Tan ditutup di hook `after`.
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`). Berlaku untuk akun observer.
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAL-214: Session ended tercatat saat App Access Fixed Asset dicabut admin

1. Pelaku John Doe (sesi API aktor) login dengan password dan membuka produk Fixed Asset hingga Session started tersimpan
2. Catat total baris Tab Session dari teks pagination (N0)
3. Admin Total Control (sesi API aktor, Admin Alpha) mencabut App Access Fixed Asset milik John Doe hingga tersimpan
4. Verifikasi tanpa memuat ulang halaman: baris baru muncul otomatis di baris paling atas: User `John D`, Activity `Session`, Status `—`, Note `Session ended`
5. Verifikasi tanpa memuat ulang halaman: tidak ada baris dengan Note `Logged out by admin` untuk sesi-produk yang sama; total baris Tab Session N0 + 1, yaitu hanya baris Session ended pada langkah 4
6. Pulihkan App Access Fixed Asset milik John Doe lewat sesi API aktor hingga tersimpan

### TC-FA-FAAL-215: Session ended tercatat saat user dinonaktifkan di produk Fixed Asset

7. Pelaku John Doe (sesi API aktor) login dengan password dan membuka produk Fixed Asset hingga Session started tersimpan
8. Catat total baris Tab Session dari teks pagination (N0)
9. Admin Total Control (sesi API aktor, Admin Alpha) menonaktifkan John Doe di Settings > User Fixed Asset hingga status Inactive tersimpan
10. Verifikasi tanpa memuat ulang halaman: baris baru muncul otomatis di baris paling atas: User `John D`, Activity `Session`, Status `—`, Note `Session ended`
11. Verifikasi tanpa memuat ulang halaman: tidak ada baris dengan Note `Logged out by admin` untuk sesi-produk yang sama; total baris Tab Session N0 + 1, yaitu hanya baris Session ended pada langkah 10
12. Aktifkan kembali John Doe di Settings > User Fixed Asset lewat sesi API aktor hingga status Active tersimpan

### TC-FA-FAAL-216: Concurrent limit reached tercatat dan sesi-produk tidak dibuat

13. Atur limit seat subscription Fixed Asset menjadi 1 dengan seat dipakai user lain hingga tersimpan
14. Catat total baris Tab Session dari teks pagination (N0)
15. Pelaku Siti Nurbaya (sesi API aktor) login dengan password dan mencoba membuka produk Fixed Asset hingga Concurrent limit reached tersimpan
16. Verifikasi: baris baru muncul di baris paling atas Tab Session: User `Siti N`, Activity `Session`, Status `—`, Note `Concurrent limit reached`; total baris Tab Session N0 + 1
17. Buka License > Concurrent User
18. Verifikasi daftar sesi aktif License > Concurrent User memuat sesi-produk user pemakai seat
19. Verifikasi daftar sesi aktif License > Concurrent User tidak memuat sesi-produk baru untuk Siti Nurbaya
20. Buka Activity Log (tab Session) lewat menu pada sidebar Reports & Logs
21. Pulihkan limit seat subscription Fixed Asset ke nilai awal hingga tersimpan

### TC-FA-FAAL-217: Force-logout admin mencatat Logged out by admin

22. Pelaku Mike Tan (sesi API aktor) login dengan password dan membuka produk Fixed Asset hingga Session started tersimpan
23. Catat total baris Tab Session dari teks pagination (N0)
24. Admin Total Control (sesi API aktor, Admin Alpha) membuka License > Concurrent User dan melakukan Force Logout pada sesi Mike Tan hingga Logged out by admin tersimpan
25. Verifikasi: baris baru muncul di baris paling atas Tab Session: User `Mike T`, Activity `Session`, Status `—`, Note `Logged out by admin`; total baris Tab Session N0 + 1

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 7, 22 (sesi-produk aktif sebagai precondition TC), langkah 6, 12, 21 (pemulihan state), langkah 17 dan 20 (membuka License > Concurrent User dan kembali ke Activity Log).
- Langkah 18 ditambahkan sebagai anchor positif untuk absence di langkah 19 (bagian 8b butir 2); Expected TC-FA-FAAL-216 butir b hanya menyebut daftar tidak memuat sesi baru.
- Baseline total (langkah 2, 8, 14, 23) dan total N0 + 1 (langkah 5, 11, 16, 25) ditambahkan untuk S-12; kolom Expected TC tidak menyebut hitungan.
- P-1 (TC-FA-FAAL-214 dan 215 butir b): asersi "tidak ada baris dengan Note `Logged out by admin`" bergantung pada sesi-produk aktif yang baru dibangun langkah sebelumnya; baris Session ended dan total N0 + 1 menjadi anchor. Tidak ada spec absence yang memuat aksi nyata untuk TC ini (S-05).
- Aksi admin pada langkah 3, 9, dan 24 dijalankan lewat sesi API aktor Admin Alpha supaya sesi UI observer tetap membuka Tab Session (tanpa butir Notes P-2). Force Logout lewat UI License > Concurrent User diuji di TC-FA-FAAL-246.
- Temuan untuk QA:
  - TC-FA-FAAL-214, 215, 217 menulis "sesi admin Total Control" tanpa menyebut menu atau mekanisme pencabutan App Access (TC-FA-FAAL-214); spec memakai kemampuan "disediakan tim BE/FE".
  - TC-FA-FAAL-216 tidak menyebut user pemakai seat satu-satunya; spec menyebutnya "user pemakai seat" dan data itu disediakan tim BE/FE.
  - Email dan password John Doe, Siti Nurbaya, dan Mike Tan tidak tertulis di Pre-setup TC; nama env var diusulkan di Prerequisites.
  - TC-FA-FAAL-217 tidak menyebut asersi jumlah baris; spec menambah total N0 + 1 untuk S-12.
