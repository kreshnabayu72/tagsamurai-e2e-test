---
id: TC-GS-USER-E2E-173-user-list-paginasi-kembali-ke-halaman-1-saat-search-filter-page-size
title: "User List: Paginasi Kembali ke Halaman 1 saat Search, Filter, atau Page Size Berubah dan Sort Tetap di Halaman"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-1131
coverage:
  web: automated
---

# User List: Paginasi Kembali ke Halaman 1 saat Search, Filter, atau Page Size Berubah dan Sort Tetap di Halaman

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini (akun default suite); halaman dibuka hook `beforeEach` suite; tidak ada ganti akun. Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data: populasi Login User sedikitnya 25 baris pada User List (Tabel Data Uji Pre-setup No. 29, fixture BE idempotent yang menyediakan tepat 25 user di client; disediakan tim FE/BE). Dengan 10 baris per halaman (default), halaman 2 ada; dengan 25 baris per halaman, halaman 1 memuat 25 baris. Spec tidak membuat atau mengubah data user. Spec lain yang menghapus data berjalan sesudah spec ini atau memakai data milik spec sendiri, sehingga populasi tidak berkurang di bawah 25 baris.
- Data Pre-setup yang dipakai: Division `Finance` (Tabel Data Uji Pre-setup No. 23) sebagai nilai Filter Division; dibaca saja, tidak diubah.
- State global yang diubah: tidak ada. State UI (Search, Sort, Filter, ukuran halaman) dipulihkan oleh langkah eksplisit di akhir tiap blok; sidebar pada `beforeEach` suite mereset sisanya.

## Test Steps

### TC-GS-USER-1131: Search kembali ke halaman 1

1. Pindah ke halaman 2
2. Verifikasi User List berada di halaman 2
3. Klik icon Search, ketik `a`, tekan Enter
4. Verifikasi User List berada di halaman 1
5. Klik icon panah `(←)` untuk menutup Search dan mereset tabel

### TC-GS-USER-1131: Sort tetap di halaman yang sama

6. Pindah ke halaman 2
7. Verifikasi User List berada di halaman 2
8. Klik header kolom Name
9. Klik header kolom Name
10. Verifikasi indikator sort Name Z-A aktif pada header Name
11. Verifikasi User List tetap berada di halaman 2
12. Klik header kolom Name

### TC-GS-USER-1131: Filter kembali ke halaman 1

13. Pindah ke halaman 2
14. Verifikasi User List berada di halaman 2
15. Klik icon Filter
16. Pilih opsi `Finance` pada Division
17. Klik `[Apply]`
18. Verifikasi User List berada di halaman 1
19. Klik icon Filter
20. Klik `[Clear Field]`
21. Klik `[Apply]`

### TC-GS-USER-1131: Page size kembali ke halaman 1

22. Pindah ke halaman 2
23. Verifikasi User List berada di halaman 2
24. Pilih 25 baris per halaman pada Pagination
25. Verifikasi User List berada di halaman 1
26. Verifikasi halaman 1 menampilkan 25 baris
27. Pilih 10 baris per halaman pada Pagination

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`. Satu TC, satu kelas (fungsional), satu layar (User List); tidak ada TC kelas harness.
- Subjudul `###` memetakan langkah ke langkah Uji TC-GS-USER-1131 (Search, Sort, Filter, page size) untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`) untuk memulihkan state: langkah 5 (menutup Search dan mereset tabel), langkah 12 (klik ketiga header Name mengembalikan default sort Name A-Z), langkah 19 sampai 21 (membersihkan Filter Division), dan langkah 27 (mengembalikan 10 baris per halaman). Langkah 1, 3, 6, 8, 9, 13, 15 sampai 17, 22, dan 24 adalah aksi dari langkah Uji TC.
- Asersi tambahan di luar Expected TC: langkah 2, 7, 14, dan 23 membuktikan User List berada di halaman 2 sebelum pemicu, sehingga "kembali ke halaman 1" dan "tetap di halaman 2" bermakna (S-14); langkah 10 membuktikan sort berubah sebelum asersi "tetap di halaman 2".
- Search, Sort, dan Filter dibersihkan di antara blok (S-09) supaya halaman 2 selalu ada pada tabel penuh (populasi sedikitnya 25 baris, 10 baris per halaman).
- Tidak ada TC yang terbelah lintas spec.
- Temuan untuk QA:
  - TC-GS-USER-1131 langkah 4 "Apply satu Filter" tidak menyebut filter; spec memakai Filter Division `Finance` (filter yang tersedia di User List dan nilai Division Pre-setup No. 23). Perlu dikonfirmasi tim FE bila filter lain yang dimaksud.
  - TC-GS-USER-1131 tidak menyebut apakah Search, Sort, dan Filter dari langkah sebelumnya tetap aktif pada langkah berikutnya; spec membersihkannya di antara blok agar halaman 2 selalu ada, sehingga tiap blok menguji satu pemicu.
  - TC-GS-USER-1131 precondition d ("User List memuat lebih dari 20 baris") bergantung pada populasi bersama (Tabel Pre-setup No. 29 = 25 baris); jumlah baris pada ukuran halaman 25 diasersi 25 dan perlu populasi tidak kurang dari itu. Pengadaan populasi oleh tim FE/BE.
  - TC-GS-USER-1131 langkah 3 "urutkan Name Z-A" tidak menyebut jumlah klik; spec mengklik header Name dua kali (asc lalu desc) dan sekali lagi untuk kembali ke default.
