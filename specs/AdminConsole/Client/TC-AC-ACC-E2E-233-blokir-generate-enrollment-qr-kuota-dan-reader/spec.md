---
id: TC-AC-ACC-E2E-233-blokir-generate-enrollment-qr-kuota-dan-reader
title: "Blokir Generate Enrollment QR karena Kuota Habis (D-08) dan Tidak Ada Smart Fixed Reader (D-17)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-305
  - TC-AC-ACC-317
  - TC-AC-ACC-940
  - TC-AC-ACC-941
coverage:
  web: automated
---

# Blokir Generate Enrollment QR karena Kuota Habis (D-08) dan Tidak Ada Smart Fixed Reader (D-17)

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (TC-AC-ACC-305). Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite. Akun kedua (langkah ganti akun): Active-Full A-15 `activeFullJakarta_automated_qaTeam1@qwertysystem.net` (Manage active client C/R/U/D pada Area Jakarta dan Cabang Menteng), password `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script). Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup (hanya dibaca): C-02 "PT Teknologi Maju" (kuota Asset Control 0, Tab Asset Control tetap tampil); C-10 "PT Lintas Jaringan" (kuota Asset Control Total 1 / Used 1 / Available 0).
- Data fixture Tabel A3 (hanya dibaca; dialog blok tidak membuat token dan tidak mengubah data): C-W3AST-1 "PT Reader Sudah Terpasang" (Asset Control Total 3 / Used 1 / Available 2; Station "Gerbang Reader Tunggal" Active dari SFR "Reader Tunggal" bertipe Asset Control; SFR "Reader Umum W3" bukan bertipe Asset Control; tidak ada SFR bertipe Asset Control lain; tanpa token Active); C-W3AST-2 "PT Kuota Habis Tanpa Reader" (Asset Control Total 1 / Used 1 / Available 0; SFR "Reader Kuota Habis" bertipe Asset Control dengan station "Gerbang Kuota Habis" Active).
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Detail diatur hook suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-ACC-305: Kuota Asset Control = 0 (Total Control)

1. Ketik Search "PT Teknologi Maju" di List Client, tekan Enter, lalu klik Company Name "PT Teknologi Maju"
2. Verifikasi Tab Asset Control tampil di navigasi tab
3. Klik Tab Asset Control
4. Verifikasi Station Quota: Total 0, Used 0, Available 0
5. Verifikasi empty state Station List: "No stations registered" dengan deskripsi "Stations will appear here once the client sets up their Asset Control readers."
6. Verifikasi tombol [Generate Enrollment QR] tampil dan aktif
7. Klik [Generate Enrollment QR]
8. Verifikasi dialog blok: Title "Cannot Generate Enrollment QR", bullet `• PT Teknologi Maju`, teks "This client has no available station quota. Add more Asset Control station quota before generating an enrollment QR." dan tombol [OK]
9. Verifikasi tidak ada QR yang tampil
10. Klik [OK]
11. Verifikasi dialog tertutup

### Ganti akun

12. Logout, lalu login sebagai Active-Full A-15 (`activeFullJakarta_automated_qaTeam1@qwertysystem.net`)

### TC-AC-ACC-317: Available = 0 pada Client PT Lintas Jaringan

13. Ketik Search "PT Lintas Jaringan" di List Client, tekan Enter, lalu klik Company Name "PT Lintas Jaringan"
14. Klik Tab Asset Control
15. Klik [Generate Enrollment QR]
16. Verifikasi dialog blok: Title "Cannot Generate Enrollment QR", bullet `• PT Lintas Jaringan`, teks "This client has no available station quota. Add more Asset Control station quota before generating an enrollment QR." dan tombol [OK]
17. Verifikasi tidak ada QR yang dibuat
18. Klik [OK]

### TC-AC-ACC-940: Available > 0 tetapi tidak ada Smart Fixed Reader yang dapat dipilih

19. Klik breadcrumb "Client", ketik Search "PT Reader Sudah Terpasang", tekan Enter, lalu klik Company Name "PT Reader Sudah Terpasang"
20. Klik Tab Asset Control
21. Verifikasi Station Quota: Total 3, Used 1, Available 2
22. Verifikasi tombol [Generate Enrollment QR] aktif dan dapat diklik
23. Klik [Generate Enrollment QR]
24. Verifikasi dialog blok: Title "Cannot Generate Enrollment QR", bullet `• PT Reader Sudah Terpasang`, teks "This client has no Smart Fixed Reader available for a new station. Register another Smart Fixed Reader before generating an enrollment QR." dan tombol [OK]
25. Verifikasi dialog dengan Title "Enrollment QR" (QR Code) tidak tampil
26. Klik [OK]
27. Verifikasi dialog blok tertutup
28. Klik [Generate Enrollment QR] sekali lagi
29. Verifikasi dialog blok dengan copy yang sama ("This client has no Smart Fixed Reader available for a new station. Register another Smart Fixed Reader before generating an enrollment QR.") tampil lagi
30. Verifikasi dialog "Active Enrollment QR" tidak tampil
31. Klik [OK]
32. Verifikasi Station Quota tetap Total 3, Used 1, Available 2

### TC-AC-ACC-941: Available = 0 dan tidak ada Smart Fixed Reader (D-08 lebih dulu dari D-17)

33. Klik breadcrumb "Client", ketik Search "PT Kuota Habis Tanpa Reader", tekan Enter, lalu klik Company Name "PT Kuota Habis Tanpa Reader"
34. Klik Tab Asset Control
35. Verifikasi Station Quota: Total 1, Used 1, Available 0
36. Klik [Generate Enrollment QR]
37. Verifikasi dialog blok: Title "Cannot Generate Enrollment QR", bullet `• PT Kuota Habis Tanpa Reader`, teks "This client has no available station quota. Add more Asset Control station quota before generating an enrollment QR." dan tombol [OK]
38. Verifikasi dialog tidak memuat teks "This client has no Smart Fixed Reader available for a new station."
39. Verifikasi dialog dengan Title "Enrollment QR" tidak tampil
40. Klik [OK]
41. Verifikasi dialog blok tertutup

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 13, 19, 33 (Search dan buka Detail Client; hook suite hanya membuka List Client), klik breadcrumb "Client" pada langkah 19 dan 33, langkah 14, 18, 20, 31, 34 (membuka Tab Asset Control dan menutup dialog blok).
- Spec ini melewati sekitar 35 langkah. Alasan: semua blok satu kelas (dialog blok kondisi data tanpa membuat data), tiap blok memakai Client sendiri, dan ganti akun (langkah 12) memakai Step eksplisit; bagian sesudah ganti akun tetap bermakna walau TC-AC-ACC-305 gagal.
- Pembagian TC lintas spec: sisi sukses Generate Enrollment QR ada di spec 234; blokir karena status Suspended, Archived, dan role Read ada di spec 237.
- Temuan untuk QA:
  - TC-AC-ACC-305 dan TC-AC-ACC-317 menyebut kuota Used 1 pada C-10 "PT Lintas Jaringan" tanpa station (Pre-setup C-10 Asset Control Total 1 / Used 1 / Available 0); spec 232 mencatat ketidaksesuaian "Used tanpa station" yang sama.
