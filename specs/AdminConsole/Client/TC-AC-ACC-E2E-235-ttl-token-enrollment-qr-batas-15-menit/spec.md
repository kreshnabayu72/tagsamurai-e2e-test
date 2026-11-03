---
id: TC-AC-ACC-E2E-235-ttl-token-enrollment-qr-batas-15-menit
title: "TTL Token Enrollment QR 15 Menit: Expiry, Batas 14:59, 15:00, dan 15:01"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-321
  - TC-AC-ACC-897
  - TC-AC-ACC-898
  - TC-AC-ACC-899
coverage:
  web: automated
---

# TTL Token Enrollment QR 15 Menit: Expiry, Batas 14:59, 15:00, dan 15:01

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Active-Full A-15 `activeFullJakarta_automated_qaTeam1@qwertysystem.net` (Manage active client C/R/U/D pada Area Jakarta dan Cabang Menteng), password `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script). Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data fixture Tabel A3 (skrip seed, bukan lewat UI; di-seed ulang lewat reset data uji): C-AST-8 "PT Uji Token QR" (Asset Control Total 5 / Used 1; SFR "Reader Token 1" bertipe Asset Control tanpa station aktif; tanpa token Enrollment QR Active).
- General Settings: Time Format 24-hour (tidak diubah).
- Kemampuan teknis (kelas harness d, objek uji adalah TTL token): jam server uji dapat dibekukan dan diubah ke waktu absolut. Acuan waktu T0 dibaca dari waktu terbit token lewat kemampuan baca fixture BE (disediakan tim FE/BE), bukan diperkirakan dari waktu hook; jam server diset absolut ke T0 + durasi (14:59, 15:00, 15:01), margin batas kurang dari 5 menit. Hanya jam server yang diatur karena TTL dihitung di server dan tidak diamati lewat countdown UI; jam server dipulihkan di akhir tiap blok TC dan di hook `after`. Token Active dikembalikan ke Expired dengan memajukan jam server 15 menit.
- Sesi UI dan sesi API aktor tetap valid selama jam digeser (suite.md > Kemampuan teknis > Sesi tetap valid saat jam digeser)
- State global: jam server dibekukan, diubah, lalu dipulihkan; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Detail diatur hook suite.
- Env var `AC_CLIENT_ACTIVE_FULL_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

1. Ketik Search "PT Uji Token QR" di List Client, tekan Enter, klik Company Name "PT Uji Token QR", lalu klik Tab Asset Control

### TC-AC-ACC-899: Expiry menunjukkan 15 menit setelah QR dibuat

2. Bekukan jam server uji pada pukul 10:00 tanggal hari ini
3. Klik [Generate Enrollment QR]
4. Verifikasi dropdown "Select Smart Fixed Reader" terisi "Reader Token 1" tanpa dipilih manual dan QR Code tampil
5. Verifikasi teks "This QR can only be used once and expires in 15 minutes."
6. Verifikasi baris `Expiry:` menampilkan pukul 10:15 pada tanggal yang sama, dalam Date Format dan Time Format General Settings
7. Klik [Close]
8. Pulihkan jam server uji, lalu majukan jam server 15 menit hingga token Active menjadi Expired dan pulihkan lagi

### TC-AC-ACC-321: Token tepat pada batas 15:00 sudah Expired

9. Bekukan jam server uji pada pukul 10:00:00 tanggal hari ini
10. Catat Station Quota
11. Klik [Generate Enrollment QR]
12. Verifikasi dropdown "Select Smart Fixed Reader" terisi "Reader Token 1" tanpa dipilih manual dan QR Code tampil
13. Verifikasi baris `Expiry:` menampilkan pukul 10:15 pada tanggal yang sama, dalam Date Format dan Time Format General Settings
14. Klik [Close]
15. Ubah jam server uji menjadi pukul 10:15:00 pada tanggal yang sama (T0 + 15 menit 0 detik)
16. Verifikasi Station Quota sama dengan nilai yang dicatat (Used dan Available tidak berubah)
17. Klik [Generate Enrollment QR]
18. Verifikasi dialog "Active Enrollment QR" tidak muncul
19. Verifikasi dialog dengan Title "Enrollment QR" langsung tampil
20. Klik [Close]
21. Verifikasi dialog tertutup
22. Pulihkan jam server uji, lalu majukan jam server 15 menit hingga token Active hasil langkah 17 menjadi Expired dan pulihkan lagi

### TC-AC-ACC-897: Generate ulang pada menit ke-14:59 memunculkan warning token aktif

23. Klik [Generate Enrollment QR]
24. Verifikasi dropdown "Select Smart Fixed Reader" terisi "Reader Token 1" tanpa dipilih manual dan QR Code tampil
25. Klik [Close]
26. Ubah jam server uji menjadi waktu terbit token + 14 menit 59 detik (absolut, T0 dibaca lewat fixture BE)
27. Klik [Generate Enrollment QR]
28. Verifikasi dialog warning: Title "Active Enrollment QR", teks "A previous QR is still active and hasn't been used yet. Generating a new one will invalidate the previous QR. Are you sure you want to generate a new one?", tombol [Cancel] dan [Generate New QR]
29. Klik [Cancel]
30. Verifikasi dialog tertutup tanpa membuat QR baru (dialog "Enrollment QR" tidak tampil)
31. Pulihkan jam server uji, lalu majukan jam server 15 menit hingga token Active menjadi Expired dan pulihkan lagi

### TC-AC-ACC-898: Generate ulang 15 menit 1 detik membuka dialog tanpa warning dan kuota tidak berkurang

32. Catat Station Quota
33. Klik [Generate Enrollment QR]
34. Verifikasi dropdown "Select Smart Fixed Reader" terisi "Reader Token 1" tanpa dipilih manual dan QR Code tampil
35. Klik [Close]
36. Ubah jam server uji menjadi waktu terbit token + 15 menit 1 detik (absolut, T0 dibaca lewat fixture BE)
37. Verifikasi Station Quota sama dengan nilai yang dicatat (Used dan Available tidak berubah)
38. Klik [Generate Enrollment QR]
39. Verifikasi dialog "Active Enrollment QR" tidak muncul
40. Verifikasi dialog dengan Title "Enrollment QR" langsung tampil
41. Klik [Close]
42. Pulihkan jam server uji, lalu majukan jam server 15 menit hingga token Active hasil langkah 38 menjadi Expired dan pulihkan lagi

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 (Search dan buka Detail Client; hook suite hanya membuka List Client), langkah 7, 14, 20, 25, 35, 41 (menutup dialog), langkah 8, 22, 31, 42 (memulihkan jam server dan mengembalikan token Active ke Expired, mengikuti Post Condition TC-AC-ACC-899/321/897/898 dan melayani precondition "tanpa token Active" TC berikutnya).
- Urutan TC di spec (899, 321, 897, 898) berbeda dari urutan nomor TC agar pembekuan jam 10:00 dikerjakan lebih dulu; tiap blok memulai dari keadaan tanpa token Active.
- Spec ini melewati sekitar 35 langkah. Alasan: semua blok satu kelas harness (d, TTL sebagai batas yang diuji) pada satu Client; tiap blok dimulai dari keadaan tanpa token Active sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-ACC-899 membekukan jam server pada "pukul 10:00" tanpa tanggal; spec memakai tanggal hari ini. Browser uji tidak diatur jamnya karena Expiry dihitung dari timestamp server dan tidak berasal dari countdown klien.
  - TC-AC-ACC-897 mensyaratkan Cancel pada menit ke-14:59 tanpa menyebut apakah token lama tetap Active sesudahnya; tidak diasersi.
