---
id: TC-AC-PP-E2E-040-search-dan-sort-dataset-besar
title: "Search dan Sort Version History pada Dataset Besar (Riwayat B)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PP-99
  - TC-AC-PP-104
  - TC-AC-PP-122
  - TC-AC-PP-126
coverage:
  web: automated
---

# Search dan Sort Version History pada Dataset Besar (Riwayat B)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, nama tampil Andi Wijaya, env var `AC_TC_PASSWORD`). Login dilakukan di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Dataset: Riwayat B (Version 1 sampai 120; Published By bergantian, ganjil `John Doe` dan genap `Jane Smith`; Published At Version 1 pada 01 Jan 2026 dan tiap versi berikutnya satu hari lebih akhir; Version 120 Active). Hook `before` men-seed Riwayat B lewat Fixture BE (kemampuan teknis: membuat ulang dataset Riwayat; riwayat append-only sehingga tidak bisa dihapus lewat UI). Hook `after` mengembalikan dataset ke Riwayat A.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah spec ini).
- Suite berjalan serial (`parallel: false`) karena dokumen Privacy Policy bersifat tunggal platform-wide; spec ini tidak membuat atau mengubah versi.
- Tidak ada fixture nilai tetap: halaman dibuka lewat sidebar (Settings > Privacy Policy).

## Test Steps

### TC-AC-PP-99: Search kolom Version mencocokkan teks tampil `Version [N]`

1. Buka Settings > Privacy Policy lewat sidebar
2. Klik icon Search di toolbar
3. Ketik "Version 12" lalu tekan Enter
4. Verifikasi tabel hanya menampilkan baris `Version 12` dan `Version 120`
5. Verifikasi footer menampilkan `1–2 of 2`
6. Ganti keyword dengan "version" lalu tekan Enter
7. Verifikasi seluruh baris cocok (tidak peka huruf besar-kecil)
8. Verifikasi footer menampilkan `1–10 of 120`
9. Ganti keyword dengan "Active" lalu tekan Enter
10. Verifikasi tabel menampilkan Title "No results found"
11. Verifikasi tabel menampilkan Description "Try adjusting your search or filter."

### TC-AC-PP-104: Menjalankan Search saat berada di halaman lebih dari 1 mereset paginasi ke halaman 1

12. Klik icon `(←)` pada search bar untuk menutup dan mereset Search
13. Klik halaman 3 pada pagination
14. Verifikasi halaman 3 aktif
15. Verifikasi footer menampilkan `21–30 of 120`
16. Klik icon Search, ketik "doe", lalu tekan Enter
17. Verifikasi tabel kembali ke halaman 1
18. Verifikasi footer menampilkan `1–10 of 60`
19. Verifikasi seluruh baris Published By `John D`

### TC-AC-PP-126: Sort tidak mereset Search dan tetap berada di halaman yang sama

20. Klik halaman 2 pada hasil Search "doe"
21. Klik header `Version` satu kali
22. Verifikasi input Search tetap `doe`
23. Verifikasi nomor halaman tetap 2
24. Verifikasi footer menampilkan `11–20 of 60`
25. Verifikasi baris halaman 2 berurutan menaik dari `Version 21`, `Version 23`, sampai `Version 39` (hanya Version ganjil karena hasil Search `doe`)

### TC-AC-PP-122: Sort kolom Version mengikuti siklus tiga klik dengan urutan numerik natural

26. Klik header `Version` dua kali lagi sampai indikator sort pada header `Version` hilang
27. Klik icon `(←)` pada search bar untuk menutup dan mereset Search
28. Ubah page size menjadi 25
29. Klik halaman 1
30. Klik header `Version` satu kali
31. Verifikasi ikon `↑` aktif pada header `Version`
32. Verifikasi baris halaman 1 berurutan `Version 1`, `Version 2`, `Version 3`, `Version 4`, `Version 5`, `Version 6`, `Version 7`, `Version 8`, `Version 9`, `Version 10`
33. Verifikasi baris berikutnya `Version 11` sampai `Version 25` berurutan naik (urutan numerik natural, bukan `Version 1`, `Version 10`, `Version 100`)
34. Klik header `Version` kedua kali
35. Verifikasi ikon `↓` aktif pada header `Version`
36. Verifikasi baris halaman 1 dari atas `Version 120`, `Version 119`, sampai `Version 96`
37. Klik header `Version` ketiga kali
38. Verifikasi indikator sort pada header `Version` hilang
39. Verifikasi urutan kembali ke default Published At Newest First (`Version 120` di atas)

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC di spec ini 99, 104, 126, 122 (TC sumber 99, 104, 122, 126). TC-122 dipindah ke akhir karena memakai page size 25 dan memulai siklus sort dari kondisi netral, sedangkan TC-126 memakai page size default 10 (`11–20 of 60`); memindahkannya menghindari perubahan page size bolak-balik (S-05).
- Langkah penghubung (tanpa `Verifikasi`; S-03, S-09): langkah 12 (tutup dan reset Search), langkah 26 (kembalikan sort Version ke netral lewat dua klik tambahan), langkah 27 (tutup Search), langkah 28 dan 29 (page size 25 dan halaman 1 sebagai precondition TC-122).
- Spec tidak membuat data dan tidak mengubah Pre-setup; hook `after` hanya mengembalikan dataset ke Riwayat A dan sesi ke akun default.
- Temuan untuk QA: tidak ada.
- Panjang spec (39 langkah) melewati perkiraan 35 langkah. Alasan: TC dalam spec satu topik, satu akun, dan satu dataset; tiap bagian dipisah subjudul TC dan tetap bermakna walau bagian sebelumnya gagal karena state dikembalikan di langkah penghubung (batas ukuran konvensi bagian 3 bukan jumlah langkah).
