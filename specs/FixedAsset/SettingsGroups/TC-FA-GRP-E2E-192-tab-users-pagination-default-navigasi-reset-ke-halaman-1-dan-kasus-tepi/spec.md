---
id: TC-FA-GRP-E2E-192-tab-users-pagination-default-navigasi-reset-ke-halaman-1-dan-kasus-tepi
title: "Tab Users Pagination: Default dan Page Size, Navigasi, Reset ke Halaman 1 Saat Search/Filter, dan Kasus Tepi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1045
  - TC-FA-GRP-1046
  - TC-FA-GRP-1139
coverage:
  web: automated
---

# Tab Users Pagination: Default dan Page Size, Navigasi, Reset ke Halaman 1 Saat Search/Filter, dan Kasus Tepi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Warehouse A (Pre-setup No 9) dibaca dan tidak diubah; memuat >= 25 user (page size default 10). N = jumlah user Warehouse A dari angka Total User Warehouse A pada Groups List. Search memakai `Fixture.groupsTabUsers.pageKeyword` (kata yang cocok dengan beberapa user di halaman 1) dan Filter memakai satu opsi Position `Fixture.groupsTabUsers.pagePosition` (disediakan tim FE; fixture baru).
- Nilai input nomor halaman tidak valid: `0`, `99`, `abc` (nilai TC-1139).

## Test Steps

1. Klik angka Total User Warehouse A

### TC-1045: Default dan pilihan page size

2. Amati footer pagination
3. Verifikasi default 10 baris per halaman
4. Buka dropdown page size
5. Verifikasi pilihan page size 10, 25, 50, dan 100 tanpa opsi All
6. Ubah page size ke 25
7. Verifikasi jumlah baris sebanyak min(25, N)
8. Ubah page size ke 50
9. Verifikasi jumlah baris sebanyak min(50, N)
10. Ubah page size ke 100
11. Verifikasi jumlah baris sebanyak min(100, N)
12. Ubah page size kembali ke 10
13. Verifikasi jumlah baris 10

### TC-1046: Navigasi, input nomor halaman, dan reset ke halaman 1

14. Klik next
15. Verifikasi halaman 2 terbuka
16. Klik prev
17. Verifikasi halaman 1 terbuka
18. Ketik nomor halaman 2 di input halaman, tekan Enter
19. Verifikasi halaman 2 langsung terbuka
20. Ketik Search `Fixture.groupsTabUsers.pageKeyword`, tekan Enter
21. Verifikasi tabel menampilkan halaman 1 dari hasil search
22. Klik `(←)` pada kotak Search
23. Pindah ke halaman 2
24. Klik icon Filter, pilih `Fixture.groupsTabUsers.pagePosition` pada Position, klik [Apply]
25. Verifikasi tabel menampilkan halaman 1
26. Buka Filter, klik [Clear Field], klik [Apply]

### TC-1139: Kasus tepi

27. Ketik `0` di input nomor halaman, tekan Enter
28. Verifikasi input tidak valid diabaikan (halaman tidak berubah)
29. Ketik `99` di input nomor halaman, tekan Enter
30. Verifikasi input tidak valid diabaikan (halaman tidak berubah)
31. Ketik `abc` di input nomor halaman, tekan Enter
32. Verifikasi input tidak valid diabaikan (halaman tidak berubah)
33. Pindah ke halaman 2
34. Ubah page size ke 25, lalu kembali ke 10
35. Verifikasi mengganti page size mengembalikan tabel ke halaman 1
36. Pindah ke halaman 2
37. Klik header Name 1x
38. Verifikasi mengganti sort tetap di halaman 2
39. Klik header Name 2x lalu 3x agar sort kembali netral

## Notes

- Spec memiliki 39 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik (Pagination Tab Users pada dataset yang sama) dan tiap TC berdiri sendiri; TC-1045 menguji empat ukuran halaman yang masing-masing punya Expected.
- Langkah penghubung (S-03, S-09): `(←)` pada kotak Search, Buka Filter [Clear Field] [Apply], dan klik header Name sampai sort netral di akhir spec.
- Temuan untuk QA:
  - Tabel Data Uji untuk variasi baris Tab Users tidak punya tabel konkret di TC (hanya `>= 12 user variasi role`); spec mendefinisikan kebutuhan nilai distinct di Prerequisites.
  - TC-1139 Expected d berupa catatan (tidak ada baris yang bisa dihapus di tabel ini) tanpa asersi; spec tidak menulis Verifikasi untuk catatan itu. TC-1045 "jumlah baris menyesuaikan pilihan" memakai min(ukuran, N) karena N Warehouse A tidak ditetapkan di TC.
