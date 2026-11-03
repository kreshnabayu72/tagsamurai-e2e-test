---
id: TC-FA-RP-E2E-088-volume-data-company-volume-seleksi-bulk-selection-limit-dan-2
title: "Volume data Company Volume: seleksi Bulk, Selection Limit, dan pagination Detail Role (2/4)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-289
  - TC-FA-RP-290
  - TC-FA-RP-291
  - TC-FA-RP-420
  - TC-FA-RP-657
coverage:
  web: automated
---

# Volume data Company Volume: seleksi Bulk, Selection Limit, dan pagination Detail Role (2/4)

## Prerequisites

- Mode: FE+BE.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Halaman: Fixed Asset > Settings > Role & Permission pada tab awal Total Control dibuka hook `beforeEach` suite (lihat suite.md).
- Akun aktor: Total Control `Company Volume` (Pre-setup #23, `Total Control Volume`), akun disediakan tim FE (email tidak tertulis di Pre-setup TC, lihat Temuan untuk QA), `Spectra.env.FA_VOLUME_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Environment variable: `FA_VOLUME_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Data Pre-setup: #23 `Company Volume` (120 pengguna `Bulk User 1` sampai `Bulk User 120`; 120 penugasan Global Role `Import data`; 120 penugasan Group Role `Manage files` di `Head Office`), #39 (Detail Role `Manage files` terisi, dipakai sebagai konteks pagination), dan #18.
- State global yang diubah spec ini: Selection Limit di System Limits (Pre-setup #34) diturunkan ke 5 (langkah 1), diubah ke 100 (langkah 16), dan dikembalikan ke nilai default (langkah 23). Nilai awal dicatat di hook `before`; hook `after` memulihkannya walau spec gagal di tengah. Karena state ini dipakai bersama, suite berjalan serial (`parallel: false`, lihat suite.md).
- Kemampuan teknis: menyetel dan memulihkan Selection Limit di System Limits (disediakan tim FE/BE, tanpa endpoint karangan).

## Test Steps

### TC-FA-RP-289: Selection Limit: checkbox ke-(N+1) diblok live dengan tooltip batas seleksi

1. Setel Selection Limit menjadi 5 di System Limits (kemampuan pengaturan disediakan tim FE/BE)
2. Klik Tab `System`, klik Role Name `Import data` pada section Global Role
3. Centang lima baris pertama
4. Hover checkbox baris keenam, lalu klik checkbox baris keenam
5. Verifikasi checkbox baris keenam Disabled dengan tooltip `You've reached the maximum selection of 5 rows.`
6. Verifikasi baris pertama sampai kelima tetap tercentang
7. Verifikasi Bulk Action Bar tetap aktif
8. Klik ikon `(✕)` pada bar untuk membatalkan seluruh seleksi

### TC-FA-RP-291: Selection Limit pada popup Assign: checkbox ke-(N+1) diblok

9. Klik Tab `System`, klik Role Name `Manage Open API` pada section Global Role
10. Klik `[+ Assign]`
11. Centang lima kandidat
12. Klik checkbox kandidat keenam
13. Verifikasi checkbox kandidat keenam Disabled dengan tooltip `You've reached the maximum selection of 5 rows.`
14. Verifikasi counter `5 Users selected`
15. Tutup popup Assign

### TC-FA-RP-290: Selection Limit: Select All lintas halaman di-cap ke batas dengan toast error

16. Setel Selection Limit menjadi 100 di System Limits (kemampuan pengaturan disediakan tim FE/BE)
17. Klik Tab `System`, klik Role Name `Import data` pada section Global Role
18. Centang satu baris, lalu klik `Select All (120 records)`
19. Verifikasi seleksi di-cap ke 100 baris pertama: counter `100 Users selected`
20. Verifikasi muncul toast error persisten: `Error, only the first 100 of 120 rows were selected. Narrow your filter to include the rest.`
21. Verifikasi Bulk Action Bar tetap muncul dan dapat dipakai untuk 100 baris itu
22. Klik ikon `(✕)` pada bar untuk membatalkan seluruh seleksi

### TC-FA-RP-420: Select All pada popup Assign hanya memilih baris di halaman aktif

23. Pulihkan Selection Limit ke nilai default (kemampuan pengaturan disediakan tim FE/BE)
24. Klik Tab `System`, klik Role Name `Manage Open API` pada section Global Role
25. Klik `[+ Assign]`
26. Klik checkbox header Select All
27. Verifikasi counter `10 Users selected`
28. Pindah ke halaman 2
29. Verifikasi baris halaman 2 tidak tercentang
30. Tutup popup Assign

### TC-FA-RP-657: Pagination Detail Role: default 10 per halaman dan pilihan ukuran

31. Klik Tab `System`, klik Role Name `Manage files` pada section Group Role
32. Klik `All Groups` di Sidebar Group Tree
33. Verifikasi default 10 data per halaman
34. Buka Overlay Page Size
35. Verifikasi pilihan ukuran 10, 25, 50, dan 100 tanpa opsi All

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-289, TC-FA-RP-290, TC-FA-RP-291, TC-FA-RP-420, TC-FA-RP-657).
- Kelas e (volume data, bagian 3 prinsip 13e): ambang 120 baris; batas seleksi diturunkan lewat Pre-setup #34 sesuai Catatan TC.
- Urutan TC dikelompokkan menurut nilai Selection Limit (5, lalu 100, lalu default) sehingga pengubahan state global hanya tiga kali: TC-FA-RP-289, TC-FA-RP-291 (limit 5), TC-FA-RP-290 (limit 100), TC-FA-RP-420 dan TC-FA-RP-657 (default). Perubahan urutan ini menyimpang dari urutan nomor TC (S-05).
- Langkah penghubung (S-03): menyetel dan memulihkan Selection Limit; membuka Tab System dan Detail Role; membatalkan seleksi dan menutup popup antar blok (S-09).
- Temuan untuk QA:
  - TC-FA-RP-289 dan TC-FA-RP-291 menyebut "Selection Limit diturunkan ke 5" tanpa menyebut siapa atau bagaimana; spec menulisnya sebagai kemampuan yang disediakan tim FE/BE (S-13).
  - TC-FA-RP-420 tidak menyebut Selection Limit; spec memakai nilai default sehingga Select All halaman aktif memilih 10 baris.
  - TC-FA-RP-657 mencantumkan Pre-setup #39 sementara Company Volume adalah #23; spec memakai Company Volume (akun Total Control `Company Volume`, "disediakan tim FE") dan Detail Role `Manage files` pada `All Groups`.
