---
id: TC-FA-GRP-E2E-095-wizard-sort-default-sort-kolom-dan-search-nama-angka-centang-dipertahankan
title: "Wizard: Sort Default dan Sort Kolom Group/Total Asset/Total User serta Search Nama dan Angka dengan Centang Dipertahankan"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-957
  - TC-FA-GRP-958
  - TC-FA-GRP-1043
  - TC-FA-GRP-1044
coverage:
  web: automated
---

# Wizard: Sort Default dan Sort Kolom Group/Total Asset/Total User serta Search Nama dan Angka dengan Centang Dipertahankan

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Total Control client Wizard (Pre-setup No 8: plan dijadwalkan downgrade Professional ke Growth, cap 3, T-30 berjalan, client punya 6 group; email dan `Spectra.env.FA_WIZ_TC_PASSWORD` disediakan tim FE, tidak tertulis di Pre-setup TC); halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE) mengikuti `suite.md`; hook `after` mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).
- Nama data Dinamis di Test Steps ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-NNN` (NNN = nomor spec ini) dan sama di seeding, asersi teks, dan cleanup. Nilai mengacu `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas `fixtures/fixedAssetSettingsGroups.json` belum ada; ditambahkan tim FE).
- State tenant (kelas h): plan dijadwalkan downgrade. Hook `after` memulihkan plan terjadwal, seleksi tersimpan, dan status Excess lewat fixture BE (disediakan tim FE/BE). Hook uji handler plan-efektif pada T-0 (pemicu, bukan objek uji) disediakan tim FE/BE tanpa endpoint karangan. Suite berjalan serial.
- Data Dinamis (di-seed lewat API di `before`; enam group client Wizard dengan nilai berikut; nilai Total Asset dan Total User memiliki sedikitnya dua nilai distinct dan 2 sebelum 10 untuk urutan numerik natural, S-11). Urutan default Group A-Z case-insensitive: `anggur`, `Apel`, `Branch Office`, `Cherry`, `Warehouse A`, `Warehouse B`. Seleksi Wizard tersimpan dikosongkan di `before` (fixture BE).

| Group | Total Asset | Total User |
|---|---|---|
| `anggur` | 2 | 10 |
| `Apel` | 10 | 0 |
| `Branch Office` | 0 | 2 |
| `Cherry` | 2 | 2 |
| `Warehouse A` | 24 | 5 |
| `Warehouse B` | 0 | 0 |

## Test Steps

### TC-FA-GRP-957: Sort default dan sort kolom Total Asset dan Total User

1. Buka Wizard Reconciliation > Step Group Consolidation
2. Verifikasi urutan default Group A-Z case-insensitive: `anggur`, `Apel`, `Branch Office`, `Cherry`, `Warehouse A`, `Warehouse B`
3. Klik header Total Asset
4. Verifikasi Total Asset terurut numerik ascending: 0, 0, 2, 2, 10, 24
5. Klik header Total User
6. Verifikasi Total User terurut numerik ascending: 0, 0, 2, 2, 5, 10
7. Klik header Total User dua kali lagi sampai urutan kembali ke default

### TC-FA-GRP-1043: Sort kolom Group, siklus Asc, Desc, Netral

8. Klik header Group sekali
9. Verifikasi urutan ascending A-Z case-insensitive (`anggur` sebelum `Apel`)
10. Klik header Group untuk kedua kalinya
11. Verifikasi urutan descending Z-A
12. Klik header Group untuk ketiga kalinya
13. Verifikasi urutan kembali ke default step (Group A-Z)

### TC-FA-GRP-1044: Sort kolom Total Asset dan Total User, siklus Asc, Desc, Netral

14. Klik header Total Asset sekali
15. Verifikasi Total Asset ascending numerik natural: 0, 0, 2, 2, 10, 24 (2 sebelum 10)
16. Klik header Total Asset untuk kedua kalinya
17. Verifikasi Total Asset descending: 24, 10, 2, 2, 0, 0
18. Klik header Total Asset untuk ketiga kalinya
19. Verifikasi urutan kembali ke default step (Group A-Z)
20. Klik header Total User sekali
21. Verifikasi Total User ascending numerik natural: 0, 0, 2, 2, 5, 10 (2 sebelum 10)
22. Klik header Total User untuk kedua kalinya
23. Verifikasi Total User descending: 10, 5, 2, 2, 0, 0
24. Klik header Total User untuk ketiga kalinya
25. Verifikasi urutan kembali ke default step (Group A-Z)

### TC-FA-GRP-958: Search nama dan angka, centang dipertahankan

26. Centang `Branch Office`
27. Ketik Search `Warehouse`, tekan Enter
28. Verifikasi sedikitnya satu baris tampil
29. Verifikasi hanya baris yang cocok (`Warehouse A` dan `Warehouse B`) tampil dan `Branch Office` tidak tampil
30. Verifikasi counter tetap "1 of 3 selected" (centang dipertahankan walau barisnya tidak tampil)
31. Klik `✕` pada Search, tekan Enter
32. Verifikasi `Branch Office` tampil kembali dalam keadaan tercentang
33. Uncheck `Branch Office` (kembali ke keadaan saat step dibuka)
34. Klik [Cancel]
35. Verifikasi step langsung tertutup tanpa dialog Unsaved changes

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 7, 33, 34: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Penutupan step pada TC-958 (langkah 33 sampai 35) mengembalikan centang `Branch Office` ke keadaan saat step dibuka (perubahan bersih nol) sehingga step langsung tertutup tanpa dialog Unsaved changes (FI-06).
- Kosongkan Search memakai `✕` lalu Enter (8b butir 9). Klik berulang header sampai netral adalah langkah penghubung reset sort (S-03).
- Spec berisi sekitar 35 langkah. Alasan: empat TC sort dan search pada satu surface dan satu dataset, tiap blok berdiri sendiri; urutan numerik dan siklus tiga tahap diasersi per kolom.
- Temuan untuk QA:
  - TC-957 Expected b menyebut "siklus 3 tahap PC §9.7" tetapi Langkah hanya satu klik per header; siklus penuh diasersi pada TC-1044.
  - TC-958 Langkah 2 menyebut Search "nama group dan angka" tetapi hanya memberi keyword nama; pencarian angka tidak diasersi.
  - TC-958 Langkah 3 "Amati" tidak menyebut baris selain `Branch Office`; spec mengasersi baris `Warehouse A` dan `Warehouse B` sebagai baris yang cocok.
