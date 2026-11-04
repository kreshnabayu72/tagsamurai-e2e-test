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
- Anggota Filter per kelas dropdown (TC-FA-LIC-200, parameter langkah 13 sampai 22); opsi tiap dropdown berasal dari DISTINCT data tabel saat ini:

  | Field | Opsi dropdown | Opsi yang dipilih | Hasil tabel |
  |---|---|---|---|
  | Plan | Enterprise, Professional | `Enterprise` | SUBS-20241201-00001 |
  | Type | Paid, Trial | `Trial` | SUBS-20241201-00001 |
  | Status | Active, Converted, Pending, Renewed | `Active` | SUBS-20260101-00001 |
  | Plan Owner | PT ABC (Principal), PT Maju Bersama (Distributor) | `PT ABC (Principal)` | SUBS-20241201-00001 |

- Field kedua untuk TC-FA-LIC-201 (irisan AND): `Plan` = `Enterprise` (dipilih spec; TC hanya menulis "Tambahkan field kedua"). Pilihan ini membuat irisan dengan `Status` = `Active` atau `Renewed` kosong, karena satu-satunya term Enterprise (SUBS-20241201-00001) berstatus Converted; hanya irisan yang membedakan AND dari OR, sebab kedua term Active dan Renewed memiliki Plan, Type, dan Plan Owner yang sama.
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

Untuk setiap baris tabel "Anggota Filter per kelas dropdown" (langkah 13 sampai 22):

13. Buka dropdown field baris tabel
14. Verifikasi opsi dropdown sesuai kolom `Opsi dropdown` baris tabel
15. Pilih opsi pada kolom `Opsi yang dipilih` baris tabel, lalu klik `[Apply]`
16. Verifikasi tabel menampilkan hasil pada kolom `Hasil tabel` baris tabel
17. Verifikasi Filter Panel tetap terbuka (ikon Filter tetap gelap)
18. Verifikasi badge titik tampil pada ikon Filter
19. Klik `[Clear Field]`
20. Klik `[Apply]`
21. Verifikasi tabel kembali menampilkan keempat term: SUBS-20270101-00001, SUBS-20260101-00001, SUBS-20250101-00001, SUBS-20241201-00001
22. Verifikasi badge titik pada ikon Filter hilang

### TC-FA-LIC-201: OR dalam satu field dan AND antar-field

23. Pada field `Status` centang `Active` dan `Renewed`, lalu klik `[Apply]`
24. Verifikasi tabel menampilkan (OR): SUBS-20260101-00001, SUBS-20250101-00001
25. Verifikasi SUBS-20270101-00001 (Pending) dan SUBS-20241201-00001 (Converted) tidak tampil
26. Pada field `Plan` centang `Enterprise`, lalu klik `[Apply]`
27. Verifikasi tabel menampilkan irisan (AND) kedua field: tidak ada baris (empty state `No results found`)
28. Klik `[Clear Field]`, lalu klik `[Apply]`
29. Klik ikon Filter untuk menutup panel

### TC-FA-LIC-202: Hapus chip lewat tombol X

30. Klik ikon Filter pada toolbar
31. Pada field `Plan` pilih `Enterprise` dan `Professional`
32. Klik `(×)` pada chip `Enterprise` tanpa membuka dropdown
33. Verifikasi chip `Enterprise` hilang
34. Buka dropdown field `Plan`
35. Verifikasi centang `Enterprise` di dropdown ikut hilang
36. Verifikasi chip `Professional` tetap
37. Klik `[Apply]`
38. Verifikasi tabel menampilkan: SUBS-20270101-00001, SUBS-20260101-00001, SUBS-20250101-00001
39. Klik `[Clear Field]`, lalu klik `[Apply]`
40. Klik ikon Filter untuk menutup panel

### TC-FA-LIC-203: Uncheck di dalam dropdown menghapus chip

41. Klik ikon Filter pada toolbar
42. Pada field `Plan` pilih `Enterprise` dan `Professional`
43. Buka dropdown field `Plan`, lalu hapus centang `Enterprise`
44. Verifikasi chip `Enterprise` hilang dari field
45. Verifikasi chip `Professional` tetap
46. Verifikasi tabel masih menampilkan empat baris (perubahan belum berlaku sebelum `[Apply]`)
47. Klik `[Apply]`
48. Verifikasi tabel menampilkan hasil sesuai perubahan: SUBS-20270101-00001, SUBS-20260101-00001, SUBS-20250101-00001
49. Klik `[Clear Field]`, lalu klik `[Apply]`
50. Klik ikon Filter untuk menutup panel

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- Spec ini di atas 35 langkah (50 langkah nominal; 80 langkah setelah ekspansi). Alasan: seluruh blok satu topik (Filter Panel Subscription History), satu dataset Pre-setup #13 yang hanya dibaca, tiap blok berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna), dan langkah 13 sampai 22 diulang per field (empat iterasi) dengan parameter di tabel `## Prerequisites`, tanpa langkah bersyarat dan dengan satu `Verifikasi` per klausa (S-01).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 (klik sub-tab sebagai aksi deterministik), serta `[Clear Field]`, `[Apply]`, dan "Klik ikon Filter untuk menutup panel" di akhir blok TC-FA-LIC-201, 202, dan 203 (pemulihan; S-09). Filter Panel tetap terbuka sesudah `[Apply]` (prd-conventions.md §9.8; TC-FA-LIC-200 klausa f): blok TC-FA-LIC-200 dan 201 memakai panel yang dibuka langkah 2 tanpa membukanya lagi, sedangkan blok TC-FA-LIC-202 dan 203 diawali membuka panel karena panel blok sebelumnya ditutup di akhir blok itu.
- Asersi di luar Expected TC (S-03): pada TC-FA-LIC-201 field kedua `Plan` = `Enterprise` dan hasil irisan kosong (empty state `No results found`) dipilih spec (TC hanya menulis "Tambahkan field kedua"); pada TC-FA-LIC-203 `Verifikasi` tabel masih empat baris sebelum `[Apply]` menjalankan klausa "perubahan berlaku pada hasil setelah `[Apply]` ditekan"; hasil tabel setelah `[Apply]` diturunkan dari data Plan Pre-setup #13.
- Temuan untuk QA:
  - TC-FA-LIC-201 tidak menyebut field kedua dan hasil irisan; spec memilih `Plan` = `Enterprise` dengan hasil irisan kosong, dan teks empty state hasil Filter tidak disebut TC (spec memakai teks empty state tabel `No results found`).
  - TC-FA-LIC-202 menulis centang `Enterprise` di dropdown ikut hilang tanpa menyebut langkah mengamatinya; spec membuka dropdown `Plan` sesudah klik chip `(×)`.
  - TC-FA-LIC-199, 200, 201, 202, dan 203 tidak menyebut Post Condition (`-`); tidak ada yang diasersi.
