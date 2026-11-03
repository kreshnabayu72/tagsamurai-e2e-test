---
id: TC-FA-LIC-E2E-064-subscription-history-filter-date-range-satu-hari
title: "Subscription History: Filter Date Range (Inklusif, Satu Hari, Tutup Panel Tanpa Apply, dan Independen dari Column Visibility)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-204
  - TC-FA-LIC-205
  - TC-FA-LIC-523
  - TC-FA-LIC-524
coverage:
  web: automated
---
# Subscription History: Filter Date Range (Inklusif, Satu Hari, Tutup Panel Tanpa Apply, dan Independen dari Column Visibility)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 (`Fixture.fixedAssetLicense.akunTotalControl`; pola email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Spec tidak mengganti akun. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag seen diatur dan dipulihkan hook suite (dinyatakan sekali di `suite.md`).
- Data Pre-setup #13 (Subscription History, hanya dibaca): empat term Subscription lewat `Fixture.fixedAssetLicense.riwayat` (fixture belum ada; disediakan tim FE/BE): SUBS-20270101-00001 (Plan Professional, Type Paid, Status Pending, Plan Owner PT Maju Bersama (Distributor)), SUBS-20260101-00001 (Professional, Paid, Active, PT Maju Bersama (Distributor)), SUBS-20250101-00001 (Professional, Paid, Renewed, PT Maju Bersama (Distributor)), SUBS-20241201-00001 (Enterprise, Trial, Converted, PT ABC (Principal)). Urutan default Start Date terbaru lebih dulu: SUBS-20270101-00001, SUBS-20260101-00001, SUBS-20250101-00001, SUBS-20241201-00001.
- Pemulihan konfigurasi kolom: konfigurasi Setup Column atau Column Visibility yang disimpan spec ini didaftarkan di `suite.md`; hook `after` menghapus preferensi kolom di browser (bukan `[Reset to Default]`; kemampuan disediakan tim FE).
- Anggota date range (TC-FA-LIC-204, parameter langkah 5 sampai 9):

  | Field | Rentang tanggal | Hasil tabel |
  |---|---|---|
  | Start Date | 01/01/26–31/12/26 | SUBS-20260101-00001 |
  | End Date | 01/01/25–31/12/25 | SUBS-20250101-00001 |

- State yang diubah dan dipulihkan: Filter Subscription History (dibersihkan di akhir tiap blok TC) dan visibilitas kolom `Plan` (dipulihkan pada langkah 36).

## Test Steps

1. Klik sub-tab `Subscription History`

### TC-FA-LIC-204: Filter date range inklusif

2. Klik ikon Filter pada toolbar
3. Verifikasi placeholder field Start Date `Select date`
4. Verifikasi placeholder field End Date `Select date`

Untuk setiap baris tabel "Anggota date range" (langkah 5 sampai 9):

5. Pilih rentang tanggal baris tabel pada field baris tabel
6. Verifikasi teks tanggal terpilih mengikuti Date Format General Settings (`dd/MM/yy`)
7. Klik `[Apply]`
8. Verifikasi tabel menampilkan hasil baris tabel
9. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-FA-LIC-205: Satu hari saja (Start = End) inklusif

10. Pada field `Start Date` pilih tanggal 01/01/26 sebagai awal dan akhir, lalu klik `[Apply]`
11. Verifikasi baris dengan Start Date tepat 01/01/26 tampil: SUBS-20260101-00001
12. Klik `[Clear Field]`, lalu klik `[Apply]`
13. Klik ikon Filter untuk menutup panel

### TC-FA-LIC-523: Menutup panel tanpa Apply membuang draft

14. Klik ikon Filter pada toolbar
15. Pada field `Plan` pilih `Professional`, lalu klik `[Apply]`
16. Verifikasi tabel menampilkan: SUBS-20270101-00001, SUBS-20260101-00001, SUBS-20250101-00001
17. Klik ikon Filter untuk menutup panel, lalu klik ikon Filter untuk membuka panel
18. Ganti `Plan` menjadi `Enterprise` tanpa klik `[Apply]`
19. Tutup panel dengan klik di luar panel
20. Verifikasi tabel tidak berubah (tiga baris yang sama: SUBS-20270101-00001, SUBS-20260101-00001, SUBS-20250101-00001)
21. Buka kembali Filter Panel
22. Verifikasi field `Plan` menampilkan chip `Professional` (nilai ter-Apply terakhir), bukan draft `Enterprise`
23. Ganti `Plan` menjadi `Enterprise` tanpa klik `[Apply]`
24. Tutup panel dengan klik ulang ikon Filter
25. Verifikasi tabel tetap menampilkan tiga baris yang sama: SUBS-20270101-00001, SUBS-20260101-00001, SUBS-20250101-00001
26. Buka Filter Panel, klik `[Clear Field]`, lalu klik `[Apply]`
27. Klik ikon Filter untuk menutup panel

### TC-FA-LIC-524: Filter independen dari Column Visibility

28. Klik ikon Filter pada toolbar
29. Pada field `Plan` pilih `Enterprise`, lalu klik `[Apply]`
30. Verifikasi tabel menampilkan: SUBS-20241201-00001
31. Klik header kolom Actions `⋯`, hilangkan centang kolom `Plan`, lalu tutup overlay Column Visibility
32. Verifikasi kolom `Plan` tidak tampil
33. Verifikasi tabel tetap menampilkan SUBS-20241201-00001 (filter tetap ter-Apply)
34. Buka Filter Panel
35. Verifikasi field `Plan` tetap ada di Filter Panel dengan chip `Enterprise`
36. Klik header kolom Actions `⋯`, centang kembali kolom `Plan`, lalu tutup overlay Column Visibility
37. Verifikasi kolom `Plan` tampil kembali
38. Verifikasi tabel tetap menampilkan SUBS-20241201-00001
39. Klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 (klik sub-tab sebagai aksi deterministik), langkah 9 dan `[Clear Field]` serta `[Apply]` di akhir tiap blok (pemulihan Filter; S-09), "Klik ikon Filter untuk menutup panel" di akhir blok (pemulihan), serta langkah 36 (memulihkan kolom `Plan`; S-09). Panel diasumsikan tetap terbuka sesudah `[Apply]`.
- Spec ini di atas 35 langkah (39 langkah nominal; 44 langkah setelah ekspansi). Alasan: seluruh blok satu topik (Filter Panel Subscription History), satu dataset Pre-setup #13 yang hanya dibaca, tiap blok berdiri sendiri, dan langkah 5 sampai 9 diulang per field (dua iterasi) dengan parameter di tabel `## Prerequisites`.
- Temuan untuk QA:
  - TC-FA-LIC-523 (langkah TC 3 dan 5) menulis "Buka Filter Panel" setelah `[Apply]` tanpa menyebut apakah panel tetap terbuka; spec menutup dan membuka panel secara eksplisit.
  - TC-FA-LIC-204, 205, 523, dan 524 tidak menyebut Post Condition (`-`); tidak ada yang diasersi.
