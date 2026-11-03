---
id: TC-FA-RP-E2E-089-volume-data-company-volume-seleksi-bulk-selection-limit-dan-3
title: "Volume data Company Volume: seleksi Bulk, Selection Limit, dan pagination Detail Role (3/4)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-658
  - TC-FA-RP-659
  - TC-FA-RP-660
  - TC-FA-RP-792
coverage:
  web: automated
---

# Volume data Company Volume: seleksi Bulk, Selection Limit, dan pagination Detail Role (3/4)

## Prerequisites

- Mode: FE+BE.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Halaman: Fixed Asset > Settings > Role & Permission pada tab awal Total Control dibuka hook `beforeEach` suite (lihat suite.md).
- Akun aktor: Total Control `Company Volume` (Pre-setup #23, `Total Control Volume`), akun disediakan tim FE (email tidak tertulis di Pre-setup TC, lihat Temuan untuk QA), `Spectra.env.FA_VOLUME_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Environment variable: `FA_VOLUME_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Data Pre-setup: #23 `Company Volume` (120 pengguna `Bulk User 1` sampai `Bulk User 120`; 120 penugasan Group Role `Manage files` di `Head Office`), #39, dan #18. Selection Limit pada nilai default; seluruh data hanya dibaca (tidak ada aksi tulis).
- Tabel pagination dan pilihan ukuran halaman 10, 25, 50, 100 mengikuti PRD §4.1.4; ukuran halaman diubah ke 25 pada langkah 7 dan dikembalikan oleh klik ulang menu (langkah 14 dan 27).

## Test Steps

### TC-FA-RP-658: Pagination Detail Role: navigasi halaman dan ganti ukuran kembali ke halaman 1

1. Klik Tab `System`, klik Role Name `Manage files` pada section Group Role
2. Klik `All Groups` di Sidebar Group Tree
3. Catat nama baris pertama halaman 1
4. Pindah ke halaman 2, lalu catat nama baris pertama halaman 2
5. Pindah ke halaman 3, lalu catat nama baris pertama halaman 3
6. Verifikasi data tiap halaman berbeda dan berurutan: nama baris pertama halaman 1, 2, dan 3 berbeda satu sama lain
7. Ganti ukuran halaman menjadi 25
8. Verifikasi tabel kembali ke halaman 1
9. Catat nama baris pertama sebelum sort
10. Klik header kolom Name dua kali (Name descending)
11. Verifikasi baris diurutkan menurun menurut Name (Z-A, collation `en-US`)
12. Verifikasi nama baris pertama berbeda dari baris pertama sebelum sort
13. Verifikasi sort tetap pada halaman yang sedang dibuka

### TC-FA-RP-659: State Detail Role dipertahankan saat F5, reset saat klik ulang menu

14. Klik menu Settings > Role & Permission di sidebar untuk mereset state halaman
15. Klik Tab `System`, klik Role Name `Manage files` pada section Group Role
16. Klik `All Groups` di Sidebar Group Tree
17. Ketik Search `Bulk User 1`, tekan Enter
18. Terapkan Filter Activation Status `Activated`
19. Klik header kolom Name dua kali (Name descending)
20. Pindah ke halaman 2
21. Muat ulang halaman (F5)
22. Verifikasi Search `Bulk User 1` tetap sama setelah F5
23. Verifikasi Filter Activation Status `Activated` tetap sama setelah F5
24. Verifikasi Sort Name descending tetap sama setelah F5
25. Verifikasi halaman aktif tetap halaman 2 setelah F5
26. Verifikasi ukuran halaman tetap sama setelah F5
27. Klik menu Settings > Role & Permission di sidebar
28. Verifikasi Search kembali kosong
29. Verifikasi Filter kembali tanpa saringan
30. Verifikasi Sort kembali ke default
31. Verifikasi halaman aktif kembali halaman 1
32. Verifikasi ukuran halaman kembali ke default

### TC-FA-RP-660: Pagination Detail Role: kasus tepi nomor halaman

33. Klik Tab `System`, klik Role Name `Manage files` pada section Group Role
34. Klik `All Groups` di Sidebar Group Tree
35. Masukkan nomor halaman `0`
36. Verifikasi nomor halaman `0` diabaikan: halaman aktif tidak berubah
37. Masukkan nomor halaman yang melebihi jumlah halaman
38. Verifikasi nomor halaman yang melebihi jumlah halaman diabaikan: halaman aktif tidak berubah
39. Masukkan nomor halaman berupa teks bukan angka
40. Verifikasi nomor halaman berupa teks bukan angka diabaikan: halaman aktif tidak berubah

### TC-FA-RP-792: Berpindah node mengembalikan paginasi ke halaman 1 sambil mempertahankan Search dan Sort

41. Klik Tab `System`, klik Role Name `Manage files` pada section Group Role
42. Ketik Search `Bulk`, tekan Enter
43. Klik header kolom Name dua kali (Name descending)
44. Pindah ke halaman 3
45. Klik node `Head Office` di Sidebar Group Tree
46. Verifikasi tabel kembali ke halaman 1
47. Verifikasi Search `Bulk` tetap aktif
48. Verifikasi Sort Name descending tetap aktif

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-658, TC-FA-RP-659, TC-FA-RP-660, TC-FA-RP-792).
- Kelas e (volume data, bagian 3 prinsip 13e): ambang 120 baris pada Detail Role `Manage files`.
- Langkah penghubung (S-03): membuka Tab System dan Detail Role; mencatat nama baris pertama sebagai baseline pembanding (langkah 3 sampai 5 dan 9); klik menu Settings > Role & Permission untuk mereset state sebelum blok berikutnya (langkah 14 dan 27, S-09; klik sidebar mereset Search, Sort, dan Filter).
- Langkah 28 sampai 32 memecah "seluruh state kembali ke default" menjadi satu `Verifikasi` per state (Search, Filter, Sort, halaman, ukuran halaman) karena tiap state bisa gagal sendiri (S-01).
- Temuan untuk QA:
  - TC-FA-RP-659 menyebut ukuran halaman diasersi "tetap sama" tanpa menyebut nilai non-default; spec tidak mengubah ukuran halaman di blok ini sehingga nilai yang sama adalah ukuran default.
  - TC-FA-RP-660 tidak menyebut nilai nomor halaman "melebihi jumlah halaman" dan teks bukan angka; spec memakai nilai berurutan 0, angka di atas jumlah halaman, dan teks sembarang non-angka.
  - TC-FA-RP-658 sampai TC-FA-RP-660 mencantumkan Pre-setup #39 sementara Company Volume adalah #23; spec memakai Company Volume.
- Spec ini 48 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu kelas (e, volume data) dan murni baca pada Detail Role `Manage files` yang sama; tiap blok mereset state lewat klik ulang menu dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
