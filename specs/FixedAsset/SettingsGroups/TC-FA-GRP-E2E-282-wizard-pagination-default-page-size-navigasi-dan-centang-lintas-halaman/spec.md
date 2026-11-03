---
id: TC-FA-GRP-E2E-282-wizard-pagination-default-page-size-navigasi-dan-centang-lintas-halaman
title: "Wizard: Pagination Step Group Consolidation (Default dan Pilihan Page Size, Navigasi, Reset ke Halaman 1, Centang dan Counter Lintas Halaman)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1065
  - TC-FA-GRP-1066
coverage:
  web: automated
---

# Wizard: Pagination Step Group Consolidation (Default dan Pilihan Page Size, Navigasi, Reset ke Halaman 1, Centang dan Counter Lintas Halaman)

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Total Control client Wizard 25 group (plan dijadwalkan downgrade ke cap 20; email dan `Spectra.env.FA_WIZ25_TC_PASSWORD` disediakan tim FE, tidak tertulis di Pre-setup TC); halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE) mengikuti `suite.md`; hook `after` mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).
- Nama data Dinamis di Test Steps ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-NNN` (NNN = nomor spec ini) dan sama di seeding, asersi teks, dan cleanup. Nilai mengacu `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas `fixtures/fixedAssetSettingsGroups.json` belum ada; ditambahkan tim FE).
- Data Dinamis (di-seed lewat API di `before`): 25 group `Pg 01` sampai `Pg 25` (nama distinct; beberapa memuat kata `Pg 1` sehingga Search `Pg 1` cocok dengan beberapa group). Page size default 10. Seleksi Wizard tersimpan dikosongkan di `before`.
- State tenant (kelas h): plan dijadwalkan downgrade. Hook `after` memulihkan plan terjadwal, seleksi tersimpan, dan status Excess lewat fixture BE (disediakan tim FE/BE). Hook uji handler plan-efektif pada T-0 (pemicu, bukan objek uji) disediakan tim FE/BE tanpa endpoint karangan. Suite berjalan serial.
- Cleanup di `after`: hapus 25 group seed lewat API.

## Test Steps

### TC-FA-GRP-1065: Default dan pilihan page size

1. Buka Wizard Reconciliation > Step Group Consolidation
2. Verifikasi footer pagination menampilkan default 10 baris per halaman
3. Buka pilihan page size
4. Verifikasi pilihan page size 10, 25, 50, dan 100 tanpa opsi All
5. Pilih page size 25
6. Verifikasi jumlah baris tabel 25
7. Pilih page size 50
8. Verifikasi jumlah baris tabel 25 (seluruh group)
9. Pilih page size 100
10. Verifikasi jumlah baris tabel 25 (seluruh group)
11. Pilih page size 10
12. Verifikasi jumlah baris tabel 10

### TC-FA-GRP-1066: Navigasi, reset ke halaman 1, centang dan counter lintas halaman

13. Centang 3 group di halaman 1
14. Klik next ke halaman 2
15. Verifikasi halaman berpindah ke halaman 2
16. Centang 2 group di halaman 2
17. Verifikasi counter "5 of 20 selected" (seluruh halaman)
18. Klik prev
19. Verifikasi halaman berpindah ke halaman 1
20. Ketik nomor halaman `2` di input halaman, tekan Enter
21. Verifikasi halaman berpindah ke halaman 2
22. Verifikasi centang tetap ada saat berpindah halaman
23. Klik Search, ketik `Pg 1`, tekan Enter dari halaman 2
24. Verifikasi tabel menampilkan halaman 1
25. Verifikasi counter tetap "5 of 20 selected" (centang tidak hilang saat hasil disaring)
26. Klik `(←)` pada kotak Search
27. Klik next ke halaman 2
28. Verifikasi halaman berpindah ke halaman 2
29. Buka Filter
30. Pilih opsi `Pg 20` pada dropdown Group, klik [Apply]
31. Verifikasi tabel menampilkan halaman 1
32. Verifikasi counter tetap "5 of 20 selected" (centang tidak hilang saat hasil disaring)
33. Klik icon Filter
34. Klik [Clear Field]
35. Klik [Apply]
36. Uncheck tiga group yang tercentang di halaman 1
37. Klik next ke halaman 2
38. Uncheck dua group yang tercentang di halaman 2 (kembali ke keadaan saat step dibuka: 0 tercentang)
39. Klik [Cancel]
40. Verifikasi step langsung tertutup tanpa dialog Unsaved changes

## Notes

- Spec 40 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 26, 33 sampai 39: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Pindah halaman tidak memicu dialog Unsaved changes; penutupan step pada langkah akhir dijalankan setelah seluruh centang dikembalikan ke keadaan saat step dibuka (perubahan bersih nol) sehingga step langsung tertutup tanpa dialog (FI-06).
- Langkah penghubung (S-03, S-14): `Pg 20` dipilih spec sebagai satu opsi dropdown Group karena TC menulis "pilih satu opsi" tanpa nilai; `[Clear Field]` dan `[Apply]` melepas Filter, dan Apply Filter mereset tabel ke halaman 1 (PRD); sesudahnya tiga centang di halaman 1 dan dua centang di halaman 2 di-uncheck dengan langkah pindah halaman eksplisit.
- Temuan untuk QA:
  - TC-1066 menyebut `[Group Limit]` = 20 tanpa menegaskan cap; spec memakai counter "5 of 20 selected" sesuai cap plan baru 20 pada Precondition.
  - TC-1066 Langkah 4 "kata yang cocok dengan beberapa group" tanpa nilai; spec memakai `Pg 1`.
