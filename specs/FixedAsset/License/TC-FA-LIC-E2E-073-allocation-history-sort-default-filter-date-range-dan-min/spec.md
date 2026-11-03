---
id: TC-FA-LIC-E2E-073-allocation-history-sort-default-filter-date-range-dan-min
title: "Allocation History: Sort Default, Berpindah Kolom Sort, Filter Date Range, dan Range Min-Max Quantity"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-239
  - TC-FA-LIC-240
  - TC-FA-LIC-246
  - TC-FA-LIC-247
  - TC-FA-LIC-248
coverage:
  web: automated
---
# Allocation History: Sort Default, Berpindah Kolom Sort, Filter Date Range, dan Range Min-Max Quantity

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 (`Fixture.fixedAssetLicense.akunTotalControl`; pola email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Spec tidak mengganti akun. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag seen diatur dan dipulihkan hook suite (dinyatakan sekali di `suite.md`).
- Data Pre-setup #13 (Allocation History, hanya dibaca): enam alokasi lewat `Fixture.fixedAssetLicense.riwayat` (fixture belum ada; disediakan tim FE/BE): LALC-20260801-00004, LALC-20260720-00003, LALC-20260515-00002, LALC-20260312-00002, LALC-20260101-00001, LALC-20250210-00001 (urutan default Last Updated terbaru lebih dulu; Plan Owner seluruhnya PT Maju Bersama (Distributor); LALC-20250210-00001 berstatus Expired, SUBS-20250101-00001; Quantity LALC-20260101-00001 = 3000 dan LALC-20260312-00002 = +1500).
- Anggota date range (TC-FA-LIC-246, parameter langkah 17 sampai 21):

  | Field | Rentang tanggal | Hasil tabel |
  |---|---|---|
  | Date | 01/01/26–30/06/26 | LALC-20260515-00002, LALC-20260312-00002, LALC-20260101-00001 |
  | End Date | 01/01/25–31/12/25 | LALC-20250210-00001 |
  | Last Updated | 01/08/26–01/08/26 | LALC-20260801-00004 |

- Anggota range Min-Max (TC-FA-LIC-248, parameter langkah 28 sampai 31):

  | Min | Max | Hasil tabel |
  |---|---|---|
  | 500 | 1500 | LALC-20260720-00003, LALC-20260312-00002, LALC-20250210-00001 |
  | 1500 | (kosong) | LALC-20260312-00002, LALC-20260101-00001 |
  | (kosong) | 30 | LALC-20260801-00004, LALC-20260515-00002 |

- State yang diubah dan dipulihkan: Sort kolom `Allocation ID` dan `Last Updated` (dinetralkan pada langkah 12), Search (dikosongkan pada langkah 11), dan Filter (dibersihkan di akhir tiap blok TC).

## Test Steps

1. Klik sub-tab `Allocation History`

### TC-FA-LIC-239: Sort default

2. Verifikasi urutan baris awal: LALC-20260801-00004, LALC-20260720-00003, LALC-20260515-00002, LALC-20260312-00002, LALC-20260101-00001, LALC-20250210-00001
3. Verifikasi indikator sort aktif pada kolom `Last Updated`

### TC-FA-LIC-240: Berpindah kolom sort

4. Klik header `Allocation ID` sekali
5. Klik header `Last Updated` sekali
6. Verifikasi kolom `Allocation ID` kembali netral (tanpa indikator sort)
7. Verifikasi kolom `Last Updated` memulai dari Ascending
8. Ketik Search `Audit`, tekan Enter
9. Klik header `Last Updated` sekali lagi (mengubah arah sort)
10. Verifikasi kata kunci Search `Audit` tetap aktif dan tabel tetap menampilkan LALC-20260515-00002
11. Klik `(←)` pada kotak Search
12. Klik header `Last Updated` sekali lagi hingga netral

### TC-FA-LIC-246: Filter date range inklusif

13. Klik ikon Filter pada toolbar
14. Verifikasi placeholder field Date `Select date`
15. Verifikasi placeholder field End Date `Select date`
16. Verifikasi placeholder field Last Updated `Select date`

Untuk setiap baris tabel "Anggota date range" (langkah 17 sampai 21):

17. Pilih rentang tanggal baris tabel pada field baris tabel
18. Verifikasi teks tanggal terpilih mengikuti Date Format General Settings (`dd/MM/yy`)
19. Klik `[Apply]`
20. Verifikasi tabel menampilkan hasil baris tabel
21. Klik `[Clear Field]`, lalu klik `[Apply]`

### TC-FA-LIC-247: Satu hari saja (Start = End) inklusif

22. Pada field `Date` pilih tanggal 01/01/26 sebagai awal dan akhir, lalu klik `[Apply]`
23. Verifikasi baris dengan Date tepat 01/01/26 tampil: LALC-20260101-00001
24. Klik `[Clear Field]`, lalu klik `[Apply]`
25. Klik ikon Filter untuk menutup panel

### TC-FA-LIC-248: Range Min-Max Quantity inklusif

26. Klik ikon Filter pada toolbar
27. Verifikasi placeholder kedua input range Quantity `Min` dan `Max`

Untuk setiap baris tabel "Anggota range Min-Max" (langkah 28 sampai 31):

28. Isi field `Quantity` dengan Min dan atau Max baris tabel
29. Klik `[Apply]`
30. Verifikasi tabel menampilkan hasil baris tabel
31. Klik `[Clear Field]`, lalu klik `[Apply]`

32. Klik ikon Filter untuk menutup panel

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- Urutan TC dalam spec: 239, 240, 246, 247, 248 (sort default diamati sebelum state diubah). TC-FA-LIC-236, 237, dan 238 (siklus sort per kelas kolom) ada di spec 137.
- Spec ini di atas 35 langkah (32 langkah nominal; 50 langkah setelah ekspansi). Alasan: seluruh blok satu topik (sort dan Filter Allocation History), satu dataset Pre-setup #13 yang hanya dibaca, tiap blok berdiri sendiri, dan langkah 17 sampai 21 (tiga iterasi) serta 28 sampai 31 (tiga iterasi) diulang dengan parameter di tabel `## Prerequisites`, tanpa langkah bersyarat dan dengan satu `Verifikasi` per klausa (S-01).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 (klik sub-tab sebagai aksi deterministik), langkah 11 dan 12 (pemulihan Search dan Sort; S-09), langkah 21 dan 31 serta `[Clear Field]` dan `[Apply]` di akhir blok (pemulihan Filter; S-09), dan "Klik ikon Filter untuk menutup panel" (pemulihan). Panel diasumsikan tetap terbuka sesudah `[Apply]`.
- Asersi di luar Expected TC (S-03): hasil Search `Audit` pada TC-FA-LIC-240 (LALC-20260515-00002, satu-satunya alokasi `Addon (Audit)`) diturunkan dari Pre-setup #13 dan dipakai untuk membuktikan Search tidak direset.
- Temuan untuk QA:
  - TC-FA-LIC-240 menulis "Terapkan Search `Audit`; ubah arah sort pada kolom `Last Updated`" tanpa menyebut arah akhir; spec tidak mengasersi arah akhir karena tidak ada di Expected.
  - TC-FA-LIC-246 tidak menyebut cara menutup panel sebelum TC-FA-LIC-248; spec menutup panel secara eksplisit.
  - TC-FA-LIC-239, 240, 246, 247, dan 248 tidak menyebut Post Condition (`-`); tidak ada yang diasersi.
