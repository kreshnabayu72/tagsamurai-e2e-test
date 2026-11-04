---
id: TC-AC-DS-E2E-099-sort-list-kolom-curated-dan-photo
title: "Sort List: Kolom Curated Ascending dan Descending serta Kolom Photo Tanpa Ikon Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-339
  - TC-AC-DS-340
  - TC-AC-DS-341
coverage:
  web: automated
---

# Sort List: Kolom Curated Ascending dan Descending serta Kolom Photo Tanpa Ikon Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima, `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup #29 (SKU Principal inti; nilai kosong `—` pada Hardware Type, Range Type, dan TAG Type sesuai tabel #29) dan #30 (`SEED-001` sampai `SEED-119`, TAG Type `Object`; total 129 SKU Principal, 13 halaman pada 10 baris per halaman): hanya dibaca, tidak diubah. Dipasang idempoten oleh seeding di hook `before`. Setiap kolom curated yang diuji memiliki sedikitnya dua nilai distinct di data itu.
- Preferensi kolom List: langkah 5 sampai 7 menampilkan kolom curated (tersimpan di cache browser) dan langkah 34 sampai 36 menyembunyikannya kembali. Hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Nilai data diacu lewat `Fixture.deviceSku.<kunci>`; berkas fixture disediakan tim FE (lihat Temuan untuk QA).
- Tidak ada state global yang diubah dan tidak ada entitas yang dibuat.

## Test Steps

### TC-AC-DS-341: Kolom Photo tidak memiliki ikon sort

1. Hover header kolom Photo
2. Klik header kolom Photo
3. Verifikasi header kolom Photo tidak memiliki ikon sort
4. Verifikasi urutan tabel tidak berubah: baris pertama tetap `BLE-KIN-GW1` (default SKU A-Z)

### Persiapan kolom curated

5. Klik header kolom Actions (⋯), lalu centang `Hardware Type` pada Overlay Column Visibility
6. Klik header kolom Actions (⋯), lalu centang `Range Type` pada Overlay Column Visibility
7. Klik header kolom Actions (⋯), lalu centang `TAG Type` pada Overlay Column Visibility

### TC-AC-DS-339: Sort ascending kolom curated

8. Klik header kolom Hardware Type sekali
9. Verifikasi enam baris pertama berurutan `BLE-KIN-GW1` (BLE Gateway), `HHR-ARC-100`, `HHR-ARC-200`, `HHR-BIG-01` (Handheld Reader), `SFR-VEL-4P`, dan `SFR-ZERO-01` (Smart Fixed Reader)
10. Pindah ke halaman 13
11. Verifikasi halaman 13 memuat sedikitnya satu baris
12. Verifikasi seluruh baris pada halaman 13 bernilai `—` pada Hardware Type
13. Klik header kolom Range Type sekali
14. Pindah ke halaman 1
15. Verifikasi tiga baris pertama `HHR-ARC-100` (Long Range), `HHR-ARC-200` dan `HHR-BIG-01` (Short Range)
16. Verifikasi baris berikutnya pada halaman 1 bernilai `—` pada Range Type
17. Klik header kolom TAG Type sekali
18. Verifikasi baris pertama halaman 1 bernilai `Object` pada TAG Type
19. Pindah ke halaman 13
20. Verifikasi halaman 13 memuat `TAG-ARC-USR` (User) diikuti enam baris bernilai `—`

### TC-AC-DS-340: Sort descending kolom curated

21. Pindah ke halaman 1
22. Klik header kolom Hardware Type dua kali
23. Verifikasi baris bernilai `—` berada di awal: baris pertama `SEED-001`
24. Pindah ke halaman 13
25. Verifikasi `BLE Gateway` (`BLE-KIN-GW1`) menjadi baris terakhir
26. Pindah ke halaman 1
27. Klik header kolom Range Type dua kali
28. Verifikasi baris bernilai `—` berada di awal: baris pertama `BLE-KIN-GW1`
29. Pindah ke halaman 13
30. Verifikasi `Long Range` (`HHR-ARC-100`) menjadi baris terakhir
31. Pindah ke halaman 1
32. Klik header kolom TAG Type dua kali
33. Verifikasi enam baris pertama bernilai `—` (`BLE-KIN-GW1`, `HHR-ARC-100`, `HHR-ARC-200`, `HHR-BIG-01`, `SFR-VEL-4P`, `SFR-ZERO-01`), disusul `User` (`TAG-ARC-USR`), lalu `Object`

### Pemulihan state akhir

34. Klik header kolom Actions (⋯), lalu hilangkan centang `Hardware Type` pada Overlay Column Visibility
35. Klik header kolom Actions (⋯), lalu hilangkan centang `Range Type` pada Overlay Column Visibility
36. Klik header kolom Actions (⋯), lalu hilangkan centang `TAG Type` pada Overlay Column Visibility

## Notes

- Urutan blok: TC-AC-DS-341 dikerjakan lebih dulu karena tidak membutuhkan kolom curated dan asersi urutan tidak berubah memakai default SKU A-Z; sumber memuat 339, 340, lalu 341.
- Langkah penghubung (S-03, S-14): langkah 5 sampai 7 menampilkan kolom curated; langkah 10, 14, 19, 21, 24, 26, 29, dan 31 memindahkan halaman karena mengganti arah sort tetap di halaman yang sama; tanpa asersi.
- Langkah penghubung pemulihan (tanpa `Verifikasi`, S-03, S-09): langkah 34 sampai 36 menyembunyikan kembali kolom curated yang ditampilkan pada langkah 5 sampai 7; hook `after` tetap menghapus preferensi kolom sebagai cadangan.
- Alasan melewati sekitar 35 langkah (36 langkah): tiga blok TC berbagi tiga kolom curated yang sama dan satu dataset 129 SKU; tiga langkah pemulihan kolom (langkah 34 sampai 36) menambah di atas batas, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah 11 adalah anchor positif tambahan (bukan Expected TC) untuk asersi universal langkah 12. Langkah 16 mengasersi baris yang tampil sesudah tiga baris pertama pada halaman 1 sebagai pengamatan atas "diikuti seluruh baris bernilai `—`".
- Temuan untuk QA:
  - S-12: asersi bergantung pada nama literal Pre-setup #29 dan #30 (mis. `BLE-KIN-GW1`, `SEED-001`, total 129 SKU, 13 halaman). Lampiran A tidak memuat butir modul ini. Spec mengikuti TC dengan seeding idempoten dan suite serial; keputusan pengecualian nama literal masih terbuka.
  - Env `AC_DS_TC_PASSWORD` dan berkas fixture `Fixture.deviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - TC-AC-DS-339 Expected b dan c menggunakan "seluruh baris" lintas halaman; spec hanya mengasersi halaman yang teramati (S-14).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag-nya bila menutupi layar belum ditetapkan.
