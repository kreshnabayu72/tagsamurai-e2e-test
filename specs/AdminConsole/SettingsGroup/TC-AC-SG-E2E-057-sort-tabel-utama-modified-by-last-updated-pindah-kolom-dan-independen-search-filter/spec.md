---
id: TC-AC-SG-E2E-057-sort-tabel-utama-modified-by-last-updated-pindah-kolom-dan-independen-search-filter
title: "Sort Tabel Utama: Modified By, Last Updated, Pindah Kolom, dan Independen dari Search dan Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-205
  - TC-AC-SG-206
  - TC-AC-SG-207
  - TC-AC-SG-208
  - TC-AC-SG-209
coverage:
  web: automated
---

# Sort Tabel Utama: Modified By, Last Updated, Pindah Kolom, dan Independen dari Search dan Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1, nama tampil `Budi Santoso`) `totalControlGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak ditulis spec ini): `Pohon Uji Utama` entitas Principal (Pre-setup #16, #17, #20), node `All Groups` terpilih, 14 group, urutan bawaan Group A-Z. Modified By distinct: `Admin A`, `Admin B`, `Admin C`, `System` (sort berdasarkan nama lengkap pengubah `Admin Alpha`, `Admin Bravo`, `Admin Charlie`, `System`). Last Updated: `Default Group` 10 Jul 2026 (terlama), `Region A` dan `Region B` 14 Jul 2026 (terbaru). `Region A` Modified By `Admin A`, Total User 5; `Region B` Modified By `Admin A`, Total User 2 (S-11).
- Page size diubah ke 25 pada langkah 1 supaya seluruh 14 baris berada pada satu halaman.
- Kelima kolom data tampil secara default; preferensi kolom di browser bersih.
- Kemampuan teknis: Fixture BE untuk baseline `Pohon Uji Utama`, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Pilih page size 25

### TC-AC-SG-205: Sort tabel utama kolom Modified By: siklus tiga klik

2. Klik header kolom Modified By sekali
3. Verifikasi ascending (↑): urutan `Admin A` sebelum `Admin B` sebelum `Admin C` sebelum `System`
4. Klik header Modified By kedua kali
5. Verifikasi descending (↓): `System` di baris pertama
6. Klik header Modified By ketiga kali
7. Verifikasi indikator sort hilang
8. Verifikasi urutan kembali ke bawaan Group A-Z (`Branch 1` di baris pertama)

### TC-AC-SG-206: Sort tabel utama kolom Last Updated: siklus tiga klik

9. Klik header kolom Last Updated sekali
10. Verifikasi ascending (↑) Oldest First: `Default Group` (10 Jul 2026) di baris pertama
11. Klik header Last Updated kedua kali
12. Verifikasi descending (↓) Newest First: baris ber-Last Updated 14 Jul 2026 di baris pertama
13. Klik header Last Updated ketiga kali
14. Verifikasi indikator sort hilang
15. Verifikasi urutan kembali ke bawaan Group A-Z (`Branch 1` di baris pertama)

### TC-AC-SG-207: Berpindah kolom sort mereset kolom sebelumnya ke netral

16. Klik header kolom Total User sekali (ascending)
17. Klik header kolom Modified By sekali
18. Verifikasi indikator sort Total User kembali netral
19. Verifikasi Modified By memulai siklus dari ascending (↑)

### TC-AC-SG-208: Sort tidak mereset Search dan Filter

20. Klik menu `Settings > Group` pada sidebar navigasi untuk mereset Search, Sort, dan Filter
21. Ketik Search `Region`, tekan Enter
22. Klik ikon Filter pada toolbar
23. Pilih `Admin A` pada Modified By, klik `[Apply]`
24. Klik header kolom Total User dua kali (descending)
25. Verifikasi kotak Search tetap berisi `Region`
26. Verifikasi kriteria Filter tetap aktif (indikator filter aktif pada ikon Filter dan `Admin A` terpilih di field Modified By)
27. Verifikasi hanya urutan baris yang berubah: indikator sort Total User descending (↓) dan `Region A` (5) di atas `Region B` (2)

### TC-AC-SG-209: Kolom Checkbox dan Actions tidak memiliki ikon sort

28. Verifikasi tidak ada ikon sort pada header kolom Checkbox maupun Actions
29. Pilih page size 10

## Notes

- Langkah penghubung (S-03): langkah 1 (page size 25 supaya baris pertama/terakhir berada pada satu halaman, S-14), langkah 20 (klik menu `Settings > Group` pada sidebar navigasi mereset Search, Sort, dan Filter; dasar TC-AC-SG-230 dan bagian 4 konvensi, S-09), dan langkah 29 (memulihkan page size bawaan 10 sesudah blok terakhir, S-09).
- TC-AC-SG-209 diamati pada halaman yang sama sesudah blok sebelumnya; header Checkbox dan Actions tidak berubah oleh Search, Filter, atau Sort.
- Temuan untuk QA:
  - TC-AC-SG-208: "hanya urutan baris yang berubah" tidak memiliki nilai pembanding sebelum sort; langkah 27 mengasersi indikator dan urutan hasil sort pada hasil gabungan Search dan Filter.
  - TC-AC-SG-205: urutan sort Modified By memakai nama lengkap (`Admin Alpha` sampai `System`) menurut keterangan Sumber PRD TC; tabel menampilkan label `Admin A`, `Admin B`, `Admin C` (R-14).
