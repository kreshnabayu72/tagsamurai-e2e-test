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
- Akun observer dan aktor: Total Control (Pre-setup #1, Admin Alpha), `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Reports & Logs > Activity Log, tab Session). Pengecualian: langkah 20 membuka License > Concurrent User dan langkah 23 kembali ke Activity Log.
- Pelaku (Pre-setup #16), email dari `Fixture.activity-log.<kunci>.email` (fixture belum ada, disediakan tim FE), password lewat env var di butir "Env var" `suite.md`:
  - John Doe: App Access Fixed Asset dan seat subscription tersedia; password `Spectra.env.FA_JOHNDOE_PASSWORD`.
  - Siti Nurbaya: App Access Fixed Asset; password `Spectra.env.FA_SITINURBAYA_PASSWORD`.
  - Mike Tan: sesi-produk Fixed Asset aktif dibuat langkah 25; password `Spectra.env.FA_MIKETAN_PASSWORD`.
  - Ketiga env var terdaftar di butir "Env var" `suite.md` (R-07). Password tidak ditulis di spec atau fixture.
- Kemampuan teknis disediakan tim BE/FE: sesi API aktor (butir "Sesi API aktor" di `suite.md`) untuk John Doe, Siti Nurbaya, Mike Tan, dan Admin Alpha (admin Total Control); kemampuan mencabut dan memulihkan App Access Fixed Asset, menonaktifkan dan mengaktifkan user di Settings > User Fixed Asset, serta Force Logout sesi di License > Concurrent User lewat sesi API aktor.
- State global untuk TC-FA-FAAL-216: limit seat subscription Fixed Asset bernilai 1 dan seat sudah dipakai user lain (disediakan tim BE/FE), diatur pada langkah 15 dan dipulihkan pada langkah 24 serta di hook `after`.
- Baseline (S-12): total baris Tab Session dibaca dari teks pagination `Showing x–y of N entries` sebelum tiap aksi pemicu; Tab Session tidak menyaring dan tidak memakai Search selama spec.
- State yang diubah dan pemulihannya: App Access Fixed Asset John Doe (langkah 7), status John Doe (langkah 14), limit seat (langkah 24), sesi-produk John Doe, Siti Nurbaya, dan Mike Tan ditutup di hook `after`.
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
5. Verifikasi tanpa memuat ulang halaman: tidak ada baris dengan Note `Logged out by admin` untuk sesi-produk yang sama
6. Verifikasi tanpa memuat ulang halaman: total baris Tab Session N0 + 1, yaitu hanya baris Session ended pada langkah 4
7. Pulihkan App Access Fixed Asset milik John Doe lewat sesi API aktor hingga tersimpan

### TC-FA-FAAL-215: Session ended tercatat saat user dinonaktifkan di produk Fixed Asset

8. Pelaku John Doe (sesi API aktor) login dengan password dan membuka produk Fixed Asset hingga Session started tersimpan
9. Catat total baris Tab Session dari teks pagination (N0)
10. Admin Total Control (sesi API aktor, Admin Alpha) menonaktifkan John Doe di Settings > User Fixed Asset hingga status Inactive tersimpan
11. Verifikasi tanpa memuat ulang halaman: baris baru muncul otomatis di baris paling atas: User `John D`, Activity `Session`, Status `—`, Note `Session ended`
12. Verifikasi tanpa memuat ulang halaman: tidak ada baris dengan Note `Logged out by admin` untuk sesi-produk yang sama
13. Verifikasi tanpa memuat ulang halaman: total baris Tab Session N0 + 1, yaitu hanya baris Session ended pada langkah 11
14. Aktifkan kembali John Doe di Settings > User Fixed Asset lewat sesi API aktor hingga status Active tersimpan

### TC-FA-FAAL-216: Concurrent limit reached tercatat dan sesi-produk tidak dibuat

15. Atur limit seat subscription Fixed Asset menjadi 1 dengan seat dipakai user lain hingga tersimpan
16. Catat total baris Tab Session dari teks pagination (N0)
17. Pelaku Siti Nurbaya (sesi API aktor) login dengan password dan mencoba membuka produk Fixed Asset hingga Concurrent limit reached tersimpan
18. Verifikasi baris baru muncul di baris paling atas Tab Session: User `Siti N`, Activity `Session`, Status `—`, Note `Concurrent limit reached`
19. Verifikasi total baris Tab Session N0 + 1
20. Buka License > Concurrent User
21. Verifikasi daftar sesi aktif License > Concurrent User memuat sesi-produk user pemakai seat
22. Verifikasi daftar sesi aktif License > Concurrent User tidak memuat sesi-produk baru untuk Siti Nurbaya
23. Buka Activity Log (tab Session) lewat menu pada sidebar Reports & Logs
24. Pulihkan limit seat subscription Fixed Asset ke nilai awal hingga tersimpan

### TC-FA-FAAL-217: Force-logout admin mencatat Logged out by admin

25. Pelaku Mike Tan (sesi API aktor) login dengan password dan membuka produk Fixed Asset hingga Session started tersimpan
26. Catat total baris Tab Session dari teks pagination (N0)
27. Admin Total Control (sesi API aktor, Admin Alpha) membuka License > Concurrent User dan melakukan Force Logout pada sesi Mike Tan hingga Logged out by admin tersimpan
28. Verifikasi baris baru muncul di baris paling atas Tab Session: User `Mike T`, Activity `Session`, Status `—`, Note `Logged out by admin`
29. Verifikasi total baris Tab Session N0 + 1

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 8, 25 (sesi-produk aktif sebagai precondition TC), langkah 7, 14, 24 (pemulihan state), langkah 20 dan 23 (membuka License > Concurrent User dan kembali ke Activity Log).
- Langkah 21 ditambahkan sebagai anchor positif untuk absence di langkah 22 (bagian 8b butir 2); Expected TC-FA-FAAL-216 butir b hanya menyebut daftar tidak memuat sesi baru.
- Baseline total (langkah 2, 9, 16, 26) dan total N0 + 1 (langkah 6, 13, 19, 29) ditambahkan untuk S-12; kolom Expected TC tidak menyebut hitungan.
- P-1 (TC-FA-FAAL-214 dan 215 butir b): asersi "tidak ada baris dengan Note `Logged out by admin`" bergantung pada sesi-produk aktif yang baru dibangun langkah sebelumnya; baris Session ended dan total N0 + 1 menjadi anchor. Tidak ada spec absence yang memuat aksi nyata untuk TC ini (S-05).
- Aksi admin pada langkah 3, 10, dan 27 dijalankan lewat sesi API aktor Admin Alpha supaya sesi UI observer tetap membuka Tab Session (tanpa butir Notes P-2). Force Logout lewat UI License > Concurrent User diuji di TC-FA-FAAL-246.
- Temuan untuk QA:
  - TC-FA-FAAL-214, 215, 217 menulis "sesi admin Total Control" tanpa menyebut menu atau mekanisme pencabutan App Access (TC-FA-FAAL-214); spec memakai kemampuan "disediakan tim BE/FE".
  - TC-FA-FAAL-216 tidak menyebut user pemakai seat satu-satunya; spec menyebutnya "user pemakai seat" dan data itu disediakan tim BE/FE.
  - Email dan password John Doe, Siti Nurbaya, dan Mike Tan tidak tertulis di Pre-setup TC; email disediakan tim FE dan nama env var password mengikuti `suite.md`.
  - TC-FA-FAAL-217 tidak menyebut asersi jumlah baris; spec menambah total N0 + 1 untuk S-12.
