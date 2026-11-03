---
id: TC-FA-CF-E2E-100-filter-semantik-modified-by-date-or-and-apply
title: "Filter: Modified By, Date Range, OR, AND, Apply, dan Draft"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-378
  - TC-FA-CF-379
  - TC-FA-CF-380
  - TC-FA-CF-381
  - TC-FA-CF-382
  - TC-FA-CF-383
  - TC-FA-CF-384
coverage:
  web: automated
---

# Filter: Modified By, Date Range, OR, AND, Apply, dan Draft

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan namaCompany Company Alpha. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` oleh tim FE.
- Data Pre-setup (tetap di environment, tidak diubah spec ini, bernama literal tanpa suffix karena asersi bergantung pada nama, Modified By, dan Last Updated seed; fixture baru belum ada, `Fixture.faCustomFields.alphaGeneral`): Company Alpha (Pre-setup #11), General Settings Date Format `dd/MM/yy`, baseline tab General (Pre-setup #12) delapan field:
  - `Asset Serial Tag`: Text; Required Yes; Modified By `Budi S` (Budi Santoso); Last Updated 17/10/26 10:45.
  - `Storage Capacity`: Numeric; Required No; Modified By `Siti A` (Siti Amelia); Last Updated 16/10/26 14:20.
  - `Equipment Class`: Dropdown; Modified By `Siti A`; Last Updated 15/10/26 11:30.
  - `Operating Voltage`: Text; Required Yes; Modified By `Budi S`; Last Updated 14/10/26 09:05.
  - `Total Cost`: Formula; Modified By `Joko W` (Joko Widodo); Last Updated 13/10/26 16:30.
  - `Depreciated Ratio`: Percentage; Inactive; Modified By `Joko W`; Last Updated 10/10/26 11:15.
  - `Compliance File`: Document; Modified By `Budi S`; Last Updated 03/10/26 08:50.
  - `Legacy Tag`: Text; Modified By `Joko W`; Last Updated 02/10/26 15:10.
- Data Dinamis: tidak ada; spec ini tidak membuat atau mengubah data.
- Hook suite yang berlaku (lihat `suite.md`): seed reset baseline Company Alpha di hook `before`, flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis: pembacaan opsi dropdown, chip filter, badge titik pada icon Filter, dan baris hasil tabel; pemilihan rentang tanggal pada input Last Updated.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-CF-378: Opsi Filter Modified By berlabel singkat dan menyaring dengan nama lengkap

1. Klik ikon Filter
2. Buka dropdown Modified By
3. Verifikasi opsi berlabel `Budi S`, `Joko W`, dan `Siti A`
4. Pilih `Budi S`, klik `[Apply]`
5. Verifikasi tabel hanya menampilkan baris `Asset Serial Tag`, `Compliance File`, dan `Operating Voltage`

### TC-FA-CF-379: Filter Last Updated date range inklusif dan satu hari Start sama dengan End

6. Klik `[Clear Field]`, pilih Last Updated 13/10/26 sampai 16/10/26, klik `[Apply]`
7. Verifikasi tabel hanya menampilkan baris `Storage Capacity`, `Equipment Class`, `Operating Voltage`, dan `Total Cost`
8. Klik `[Clear Field]`, pilih Last Updated 17/10/26 sampai 17/10/26, klik `[Apply]`
9. Verifikasi tabel hanya menampilkan baris `Asset Serial Tag`

### TC-FA-CF-380: Beberapa opsi dalam satu field filter digabung dengan OR

10. Klik `[Clear Field]`, pilih Data Type `Text` dan `Numeric`, klik `[Apply]`
11. Verifikasi tabel hanya menampilkan baris `Asset Serial Tag`, `Legacy Tag`, `Operating Voltage`, dan `Storage Capacity`

### TC-FA-CF-381: Beberapa field filter digabung dengan AND

12. Klik `[Clear Field]`, pilih Data Type `Text` dan Required `Yes`, klik `[Apply]`
13. Verifikasi tabel hanya menampilkan baris `Asset Serial Tag` dan `Operating Voltage`

### TC-FA-CF-382: Pilihan filter baru berlaku hanya setelah klik Apply

14. Klik `[Clear Field]`, klik `[Apply]`
15. Pilih Data Type `Text` tanpa klik `[Apply]`
16. Verifikasi tabel belum tersaring (seluruh delapan baris tab General tampil)

### TC-FA-CF-383: Menutup Filter Panel tanpa Apply membuang draft dan memulihkan nilai ter-Apply terakhir

17. Klik `[Clear Field]`, pilih Data Type `Text`, klik `[Apply]`
18. Ubah Data Type menjadi `Numeric` tanpa klik `[Apply]`
19. Klik ikon Filter untuk menutup Filter Panel
20. Klik ikon Filter untuk membuka Filter Panel
21. Verifikasi panel menampilkan nilai ter-Apply terakhir `Text`, bukan draft `Numeric`
22. Verifikasi tabel tetap menampilkan hasil Text (baris `Asset Serial Tag`, `Legacy Tag`, dan `Operating Voltage`)

### TC-FA-CF-384: Badge titik pada icon Filter muncul saat filter ter-Apply dan hilang saat dibersihkan

23. Klik `[Clear Field]`, pilih Data Type `Text`, klik `[Apply]`
24. Verifikasi badge titik tampil pada icon Filter saat panel terbuka
25. Klik ikon Filter untuk menutup Filter Panel
26. Verifikasi badge titik tampil pada icon Filter saat panel tertutup
27. Klik ikon Filter untuk membuka Filter Panel
28. Klik `[Clear Field]`, klik `[Apply]`
29. Verifikasi badge titik pada icon Filter hilang

## Notes

- Spec memuat 29 langkah, di bawah ambang sekitar 35 langkah. Satu topik (semantik Filter Panel tabel utama tab General), satu dataset, satu akun.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 6, 8, 10, 12, 14, 17, dan 23 memuat `[Clear Field]` sebagai langkah "Bersihkan" antar TC (S-09; cara membersihkan tidak disebut TC, dipilih `[Clear Field]`); langkah 14 juga melepas filter ter-Apply agar tabel belum tersaring saat langkah 16; langkah 19 dan 20 menutup dan membuka kembali panel (bagian dari TC-FA-CF-383).
- Asersi hasil filter ditulis "hanya menampilkan baris X" dengan menyebut nama baris; daftar baris pada Expected TC diperlakukan sebagai himpunan lengkap hasil.
- Temuan untuk QA:
  - TC-FA-CF-382 tidak menyebut keadaan awal tabel; spec membersihkan filter lebih dulu (langkah 14) agar "belum tersaring" dapat diamati terhadap seluruh delapan baris baseline.
  - TC-FA-CF-383 Expected b menyebut "hasil Text" tanpa nama baris; spec memakai nama baris hasil Data Type `Text` dari TC-FA-CF-376 (`Asset Serial Tag`, `Legacy Tag`, `Operating Voltage`).
  - TC-FA-CF-384 Expected a ("baik panel terbuka maupun tertutup") dipecah menjadi dua `Verifikasi` (langkah 24 dan 26).
  - TC-FA-CF-379 tidak menyebut cara memilih rentang tanggal pada input `Select date`; langkah ditulis mengikuti TC.
  - Spec mengasumsikan Filter Panel tetap terbuka setelah `[Apply]` (TC tidak menyatakannya secara eksplisit).
  - Seluruh TC pada spec ini tidak memiliki Post Condition (kolom `-`); tidak ada yang diasersi.
