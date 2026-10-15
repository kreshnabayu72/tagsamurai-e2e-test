---
id: TC-AC-PP-E2E-034-filter-screening-dropdown-dan-chip
title: "Filter Panel: Screening, Dropdown Published By, dan Penghapusan Chip"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PP-106
  - TC-AC-PP-108
  - TC-AC-PP-109
  - TC-AC-PP-110
coverage:
  web: automated
---

# Filter Panel: Screening, Dropdown Published By, dan Penghapusan Chip

## Prerequisites

- Mode: FE+BE (TC-AC-PP-106 bertanda UI Only, tetapi spec berbagi dataset dengan TC-AC-PP-108 sampai 110 yang membutuhkan data dari backend).
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Andi Wijaya), password dari `Spectra.env.AC_TC_PASSWORD`. Login dilakukan di hook `before`; hook `after` mengembalikan sesi ke akun default suite (akun yang sama). Nama env `AC_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Dataset: Riwayat A (Version 3 Active `John Doe`, Version 2 `John Doe`, Version 1 `Jane Smith` akun sudah dihapus). Hook `before` men-seed lewat Fixture BE; hook `after` mengembalikan ke Riwayat A. Spec ini hanya membaca data.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC. Spec tidak mengubahnya.
- Kemampuan teknis: Fixture BE untuk membuat ulang dataset Riwayat A.
- State UI yang diubah spec: draft isian panel Filter (tidak pernah di-Apply) dikosongkan lewat `[Clear Field]` di antara TC dan panel ditutup tanpa Apply di akhir spec.
- Suite berjalan serial (`parallel: false`) karena dokumen Privacy Policy bersifat tunggal platform-wide; spec ini sendiri tidak mengubah data.
- Tidak ada fixture file yang dibutuhkan; halaman dibuka lewat menu Settings > Privacy Policy.

## Test Steps

### TC-AC-PP-106: Screening Filter Panel: dua field filter dengan tombol Clear Field dan Apply

1. Hover icon Filter di toolbar
2. Verifikasi tooltip "Filter" tampil
3. Klik icon Filter
4. Verifikasi icon Filter berwarna gelap
5. Verifikasi panel tampil di bawah toolbar
6. Verifikasi field berurutan `Published At` (date range picker) lalu `Published By` (multi-select searchable)
7. Verifikasi label field "Published At" dan "Published By"
8. Verifikasi placeholder field `Published By` "All users"
9. Verifikasi tombol berurutan `[Clear Field]` (kiri, Text) lalu `[Apply]` (kanan, filled)
10. Verifikasi placeholder field `Published At` "Select date"

### TC-AC-PP-108: Search di dalam dropdown Published By mempersempit opsi

11. Klik field `Published By`
12. Ketik "jo" pada kotak search di dalam dropdown
13. Verifikasi hanya opsi `John Doe` yang tampil di dalam dropdown
14. Ganti isi kotak search dengan "zz"
15. Verifikasi tidak ada opsi yang tampil di dalam dropdown
16. Verifikasi tabel Version History tidak berubah selama pencarian di dalam dropdown (tetap 3 baris)
17. Kosongkan kotak search dropdown dan tutup dropdown

### TC-AC-PP-109: Menghapus chip lewat (X) meng-uncheck opsi terkait dan chip lain tetap

18. Klik field `Published By`
19. Centang `John Doe` dan `Jane Smith`
20. Tutup dropdown
21. Verifikasi dua chip `John Doe` dan `Jane Smith` tampil di dalam field `Published By`
22. Klik (X) pada chip `John Doe`
23. Verifikasi chip `John Doe` hilang
24. Verifikasi chip `Jane Smith` tetap ada
25. Buka kembali dropdown `Published By`
26. Verifikasi checkbox `John Doe` tidak tercentang
27. Verifikasi checkbox `Jane Smith` tetap tercentang
28. Tutup dropdown lalu klik `[Clear Field]` pada panel Filter untuk mengosongkan field `Published By` (tanpa Apply)

### TC-AC-PP-110: Menghapus chip lewat uncheck di dalam dropdown yang terbuka menghapus chip terkait dan chip lain tetap

29. Klik field `Published By`
30. Centang `John Doe` dan `Jane Smith` (dropdown tetap terbuka)
31. Uncheck `Jane Smith` dari dalam dropdown
32. Verifikasi chip `Jane Smith` hilang dari field `Published By`
33. Verifikasi chip `John Doe` tetap ada
34. Verifikasi checkbox `John Doe` tetap tercentang
35. Tutup dropdown, klik `[Clear Field]` untuk mengosongkan field, lalu tutup panel Filter dengan klik di luar panel (tanpa Apply)

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (tanpa awalan Verifikasi): langkah membersihkan kotak search dropdown dan menutup dropdown di akhir blok TC-AC-PP-108; langkah `[Clear Field]` tanpa Apply di akhir blok TC-AC-PP-109 dan 110 agar draft panel tidak terbawa ke TC berikutnya (panel tetap terbuka antar TC sesuai precondition TC-AC-PP-108 sampai 110 "panel Filter terbuka"); langkah menutup dropdown setelah memilih opsi di blok TC-AC-PP-109.
- Perilaku Apply (logika OR, AND, rentang tanggal) ada di spec `TC-AC-PP-E2E-035` dan `TC-AC-PP-E2E-037`; opsi dropdown dari Riwayat S ada di `TC-AC-PP-E2E-002` (TC-AC-PP-107).
- Temuan untuk QA:
  - TC-AC-PP-106 Expected c menyebut placeholder `Published By` "All users" dan Expected e menyebut placeholder `Published At` "Select date", dua butir Expected tentang placeholder dipisah dari label di butir c; spec mengasersi masing-masing.
  - TC-AC-PP-108 Expected c ("Tabel Version History tidak berubah selama pencarian di dalam dropdown") tidak menyebut jumlah baris; spec memakai 3 baris Riwayat A.
  - TC-AC-PP-108 langkah 3 ("Ketik zz pada kotak search yang sama") tidak menyebut apakah "jo" dihapus lebih dulu; spec mengganti isi kotak search dengan "zz".
