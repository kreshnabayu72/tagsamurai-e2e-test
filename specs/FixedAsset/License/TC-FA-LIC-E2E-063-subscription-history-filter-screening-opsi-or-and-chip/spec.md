---
id: TC-FA-LIC-E2E-063-subscription-history-filter-screening-opsi-or-and-chip
title: "Subscription History: Filter Panel (Screening, Opsi per Kelas Dropdown, OR dan AND, serta Chip)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-199
  - TC-FA-LIC-200
  - TC-FA-LIC-201
  - TC-FA-LIC-202
  - TC-FA-LIC-203
coverage:
  web: automated
---
# Subscription History: Filter Panel (Screening, Opsi per Kelas Dropdown, OR dan AND, serta Chip)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 (`Fixture.fixedAssetLicense.akunTotalControl`; pola email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Spec tidak mengganti akun. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag seen diatur dan dipulihkan hook suite (dinyatakan sekali di `suite.md`).
- Data Pre-setup #13 (Subscription History, hanya dibaca): empat term Subscription lewat `Fixture.fixedAssetLicense.riwayat` (fixture belum ada; disediakan tim FE/BE): SUBS-20270101-00001 (Plan Professional, Type Paid, Status Pending, Plan Owner PT Maju Bersama (Distributor)), SUBS-20260101-00001 (Professional, Paid, Active, PT Maju Bersama (Distributor)), SUBS-20250101-00001 (Professional, Paid, Renewed, PT Maju Bersama (Distributor)), SUBS-20241201-00001 (Enterprise, Trial, Converted, PT ABC (Principal)). Urutan default Start Date terbaru lebih dulu: SUBS-20270101-00001, SUBS-20260101-00001, SUBS-20250101-00001, SUBS-20241201-00001.
- Anggota Filter per kelas dropdown (TC-FA-LIC-200, parameter langkah 13 sampai 18); opsi tiap dropdown berasal dari DISTINCT data tabel saat ini:

  | Field | Opsi dropdown | Opsi yang dipilih | Hasil tabel |
  |---|---|---|---|
  | Plan | Enterprise, Professional | `Enterprise` | SUBS-20241201-00001 |
  | Type | Paid, Trial | `Trial` | SUBS-20241201-00001 |
  | Status | Active, Converted, Pending, Renewed | `Active` | SUBS-20260101-00001 |
  | Plan Owner | PT ABC (Principal), PT Maju Bersama (Distributor) | `PT ABC (Principal)` | SUBS-20241201-00001 |

- Field kedua untuk TC-FA-LIC-201 (irisan AND): `Status` = `Active` (dipilih spec; TC hanya menulis "Tambahkan field kedua").
- State yang diubah dan dipulihkan: Filter Subscription History (dibersihkan dengan `[Clear Field]` dan `[Apply]` di akhir tiap blok TC; panel ditutup di akhir tiap blok).

## Test Steps

1. Klik sub-tab `Subscription History`

### TC-FA-LIC-199: Screening Filter Panel

2. Klik ikon Filter pada toolbar
3. Verifikasi ikon Filter berubah gelap
4. Verifikasi panel tampil di bawah toolbar
5. Verifikasi field berurutan (maksimal 4 per baris): Plan, Type, Status, Start Date, End Date, Plan Owner
6. Verifikasi field Plan: dropdown multi-select searchable, placeholder `All plans`
7. Verifikasi field Type: dropdown multi-select searchable, placeholder `All types`
8. Verifikasi field Status: dropdown multi-select searchable, placeholder `All statuses`
9. Verifikasi field Start Date: date range picker, placeholder `Select date`
10. Verifikasi field End Date: date range picker, placeholder `Select date`
11. Verifikasi field Plan Owner: dropdown multi-select searchable, placeholder `All owners`
12. Verifikasi tombol `[Clear Field]` (kiri, text) dan `[Apply]` (kanan, filled)

### TC-FA-LIC-200: Opsi dan penyaringan per kelas dropdown

Untuk setiap baris tabel "Anggota Filter per kelas dropdown" (langkah 13 sampai 18):

13. Buka dropdown field baris tabel
14. Verifikasi opsi dropdown sesuai kolom `Opsi dropdown` baris tabel
15. Pilih opsi pada kolom `Opsi yang dipilih` baris tabel, lalu klik `[Apply]`
16. Verifikasi tabel menampilkan hasil pada kolom `Hasil tabel` baris tabel
17. Klik `[Clear Field]`
18. Klik `[Apply]`

### TC-FA-LIC-201: OR dalam satu field dan AND antar-field

19. Pada field `Plan` centang `Enterprise` dan `Professional`, lalu klik `[Apply]`
20. Verifikasi tabel menampilkan (OR): SUBS-20270101-00001, SUBS-20260101-00001, SUBS-20250101-00001, SUBS-20241201-00001
21. Pada field `Status` centang `Active`, lalu klik `[Apply]`
22. Verifikasi tabel menampilkan irisan (AND) kedua field: SUBS-20260101-00001
23. Klik `[Clear Field]`, lalu klik `[Apply]`
24. Klik ikon Filter untuk menutup panel

### TC-FA-LIC-202: Hapus chip lewat tombol X

25. Klik ikon Filter pada toolbar
26. Pada field `Plan` pilih `Enterprise` dan `Professional`
27. Klik `(×)` pada chip `Enterprise` tanpa membuka dropdown
28. Verifikasi chip `Enterprise` hilang
29. Buka dropdown field `Plan`
30. Verifikasi centang `Enterprise` di dropdown ikut hilang
31. Verifikasi chip `Professional` tetap
32. Klik `[Apply]`
33. Verifikasi tabel menampilkan: SUBS-20270101-00001, SUBS-20260101-00001, SUBS-20250101-00001
34. Klik `[Clear Field]`, lalu klik `[Apply]`
35. Klik ikon Filter untuk menutup panel

### TC-FA-LIC-203: Uncheck di dalam dropdown menghapus chip

36. Klik ikon Filter pada toolbar
37. Pada field `Plan` pilih `Enterprise` dan `Professional`
38. Buka dropdown field `Plan`, lalu hapus centang `Enterprise`
39. Verifikasi chip `Enterprise` hilang dari field
40. Verifikasi chip `Professional` tetap
41. Verifikasi tabel masih menampilkan empat baris (perubahan belum berlaku sebelum `[Apply]`)
42. Klik `[Apply]`
43. Verifikasi tabel menampilkan hasil sesuai perubahan: SUBS-20270101-00001, SUBS-20260101-00001, SUBS-20250101-00001
44. Klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- Spec ini di atas 35 langkah (44 langkah nominal; 62 langkah setelah ekspansi). Alasan: seluruh blok satu topik (Filter Panel Subscription History), satu dataset Pre-setup #13 yang hanya dibaca, tiap blok berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna), dan langkah 13 sampai 18 diulang per field (empat iterasi) dengan parameter di tabel `## Prerequisites`, tanpa langkah bersyarat dan dengan satu `Verifikasi` per klausa (S-01).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 (klik sub-tab sebagai aksi deterministik), langkah 17 dan 18 (membersihkan Filter antar anggota; S-09), dan `[Clear Field]` serta `[Apply]` serta "Klik ikon Filter untuk menutup panel" di akhir tiap blok (pemulihan; S-09). Panel diasumsikan tetap terbuka sesudah `[Apply]` (TC-FA-LIC-200 menulis `[Apply]` lalu `[Clear Field]` dan `[Apply]`), sehingga blok berikutnya diawali menutup dan membuka panel secara eksplisit.
- Asersi di luar Expected TC (S-03): pada TC-FA-LIC-201 field kedua `Status` = `Active` dan hasil irisan SUBS-20260101-00001 dipilih spec (TC hanya menulis "Tambahkan field kedua"); pada TC-FA-LIC-203 `Verifikasi` tabel masih empat baris sebelum `[Apply]` menjalankan klausa "perubahan berlaku pada hasil setelah `[Apply]` ditekan"; hasil tabel setelah `[Apply]` diturunkan dari data Plan Pre-setup #13.
- Temuan untuk QA:
  - TC-FA-LIC-201 tidak menyebut field kedua dan hasil irisan; spec memilih `Status` = `Active`.
  - TC-FA-LIC-202 menulis centang `Enterprise` di dropdown ikut hilang tanpa menyebut langkah mengamatinya; spec membuka dropdown `Plan` sesudah klik chip `(×)`.
  - TC tidak menyebut apakah Filter Panel tetap terbuka sesudah `[Apply]`; spec menutupnya secara eksplisit di akhir blok.
  - TC-FA-LIC-199, 200, 201, 202, dan 203 tidak menyebut Post Condition (`-`); tidak ada yang diasersi.
