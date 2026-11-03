---
id: TC-FA-LIC-E2E-072-allocation-history-filter-screening-opsi-or-and-chip
title: "Allocation History: Filter Panel (Screening, Opsi per Kelas Dropdown, OR dan AND, serta Chip)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-241
  - TC-FA-LIC-242
  - TC-FA-LIC-243
  - TC-FA-LIC-244
  - TC-FA-LIC-245
coverage:
  web: automated
---
# Allocation History: Filter Panel (Screening, Opsi per Kelas Dropdown, OR dan AND, serta Chip)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 (`Fixture.fixedAssetLicense.akunTotalControl`; pola email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Spec tidak mengganti akun. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag seen diatur dan dipulihkan hook suite (dinyatakan sekali di `suite.md`).
- Data Pre-setup #13 (Allocation History, hanya dibaca): enam alokasi lewat `Fixture.fixedAssetLicense.riwayat` (fixture belum ada; disediakan tim FE/BE): LALC-20260801-00004, LALC-20260720-00003, LALC-20260515-00002, LALC-20260312-00002, LALC-20260101-00001, LALC-20250210-00001 (urutan default Last Updated terbaru lebih dulu; Plan Owner seluruhnya PT Maju Bersama (Distributor); LALC-20250210-00001 berstatus Expired, SUBS-20250101-00001; Quantity LALC-20260101-00001 = 3000 dan LALC-20260312-00002 = +1500).
- Anggota Filter per kelas dropdown (TC-FA-LIC-242, parameter langkah 15 sampai 20); opsi tiap dropdown berasal dari DISTINCT data tabel saat ini:

  | Field | Opsi dropdown | Opsi yang dipilih | Hasil tabel |
  |---|---|---|---|
  | Subscription ID | SUBS-20250101-00001, SUBS-20260101-00001 | `SUBS-20250101-00001` | LALC-20250210-00001 |
  | License Type | Addon (Audit), Addon (IT Inventory), Asset License | `Asset License` | LALC-20260720-00003, LALC-20260312-00002, LALC-20260101-00001, LALC-20250210-00001 |
  | Status | Active, Expired | `Expired` | LALC-20250210-00001 |
  | Plan Owner | PT Maju Bersama (Distributor) | `PT Maju Bersama (Distributor)` | LALC-20260801-00004, LALC-20260720-00003, LALC-20260515-00002, LALC-20260312-00002, LALC-20260101-00001, LALC-20250210-00001 |

- Field kedua untuk TC-FA-LIC-243 (irisan AND): `Status` = `Expired` (dipilih spec; TC hanya menulis "Tambahkan field kedua").
- State yang diubah dan dipulihkan: Filter Allocation History (dibersihkan dengan `[Clear Field]` dan `[Apply]` di akhir tiap blok TC; panel ditutup di akhir tiap blok).

## Test Steps

1. Klik sub-tab `Allocation History`

### TC-FA-LIC-241: Screening Filter Panel

2. Klik ikon Filter pada toolbar
3. Verifikasi ikon Filter berubah gelap
4. Verifikasi panel tampil di bawah toolbar
5. Verifikasi field berurutan (maksimal 4 per baris): Subscription ID, License Type, Quantity, Status, Date, End Date, Plan Owner, Last Updated
6. Verifikasi field Subscription ID: dropdown multi-select searchable, placeholder `All subscription IDs`
7. Verifikasi field License Type: dropdown multi-select searchable, placeholder `All types`
8. Verifikasi field Quantity: field range Min-Max, placeholder `Min / Max`
9. Verifikasi field Status: dropdown multi-select searchable, placeholder `All statuses`
10. Verifikasi field Date: date range picker, placeholder `Select date`
11. Verifikasi field End Date: date range picker, placeholder `Select date`
12. Verifikasi field Plan Owner: dropdown multi-select searchable, placeholder `All owners`
13. Verifikasi field Last Updated: date range picker, placeholder `Select date`
14. Verifikasi tombol `[Clear Field]` (kiri, text) dan `[Apply]` (kanan, filled)

### TC-FA-LIC-242: Opsi dan penyaringan per kelas dropdown

Untuk setiap baris tabel "Anggota Filter per kelas dropdown" (langkah 15 sampai 20):

15. Buka dropdown field baris tabel
16. Verifikasi opsi dropdown sesuai kolom `Opsi dropdown` baris tabel
17. Pilih opsi pada kolom `Opsi yang dipilih` baris tabel, lalu klik `[Apply]`
18. Verifikasi tabel menampilkan hasil pada kolom `Hasil tabel` baris tabel
19. Klik `[Clear Field]`
20. Klik `[Apply]`

### TC-FA-LIC-243: OR dalam satu field dan AND antar-field

21. Pada field `Subscription ID` centang `SUBS-20250101-00001` dan `SUBS-20260101-00001`, lalu klik `[Apply]`
22. Verifikasi tabel menampilkan (OR): LALC-20260801-00004, LALC-20260720-00003, LALC-20260515-00002, LALC-20260312-00002, LALC-20260101-00001, LALC-20250210-00001
23. Pada field `Status` centang `Expired`, lalu klik `[Apply]`
24. Verifikasi tabel menampilkan irisan (AND) kedua field: LALC-20250210-00001
25. Klik `[Clear Field]`, lalu klik `[Apply]`
26. Klik ikon Filter untuk menutup panel

### TC-FA-LIC-244: Hapus chip lewat tombol X

27. Klik ikon Filter pada toolbar
28. Pada field `Subscription ID` pilih `SUBS-20250101-00001` dan `SUBS-20260101-00001`
29. Klik `(×)` pada chip `SUBS-20250101-00001` tanpa membuka dropdown
30. Verifikasi chip `SUBS-20250101-00001` hilang
31. Buka dropdown field `Subscription ID`
32. Verifikasi centang `SUBS-20250101-00001` di dropdown ikut hilang
33. Verifikasi chip `SUBS-20260101-00001` tetap
34. Klik `[Apply]`
35. Verifikasi tabel menampilkan: LALC-20260801-00004, LALC-20260720-00003, LALC-20260515-00002, LALC-20260312-00002, LALC-20260101-00001
36. Klik `[Clear Field]`, lalu klik `[Apply]`
37. Klik ikon Filter untuk menutup panel

### TC-FA-LIC-245: Uncheck di dalam dropdown menghapus chip

38. Klik ikon Filter pada toolbar
39. Pada field `Subscription ID` pilih `SUBS-20250101-00001` dan `SUBS-20260101-00001`
40. Buka dropdown field `Subscription ID`, lalu hapus centang `SUBS-20250101-00001`
41. Verifikasi chip `SUBS-20250101-00001` hilang dari field
42. Verifikasi chip `SUBS-20260101-00001` tetap
43. Verifikasi tabel masih menampilkan enam baris (perubahan belum berlaku sebelum `[Apply]`)
44. Klik `[Apply]`
45. Verifikasi tabel menampilkan hasil sesuai perubahan: LALC-20260801-00004, LALC-20260720-00003, LALC-20260515-00002, LALC-20260312-00002, LALC-20260101-00001
46. Klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- Spec ini di atas 35 langkah (46 langkah nominal; 64 langkah setelah ekspansi). Alasan: seluruh blok satu topik (Filter Panel Allocation History), satu dataset Pre-setup #13 yang hanya dibaca, tiap blok berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna), dan langkah 15 sampai 20 diulang per field (empat iterasi) dengan parameter di tabel `## Prerequisites`, tanpa langkah bersyarat dan dengan satu `Verifikasi` per klausa (S-01).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 (klik sub-tab sebagai aksi deterministik), langkah 19 dan 20 (membersihkan Filter antar anggota; S-09), serta `[Clear Field]`, `[Apply]`, dan "Klik ikon Filter untuk menutup panel" di akhir tiap blok (pemulihan; S-09). Panel diasumsikan tetap terbuka sesudah `[Apply]`.
- Asersi di luar Expected TC (S-03): pada TC-FA-LIC-243 field kedua `Status` = `Expired` dan hasil irisan LALC-20250210-00001 dipilih spec; pada TC-FA-LIC-245 `Verifikasi` tabel masih enam baris sebelum `[Apply]` menjalankan klausa "perubahan berlaku pada hasil setelah `[Apply]` ditekan"; hasil tabel setelah `[Apply]` diturunkan dari TC-FA-LIC-244.
- Temuan untuk QA:
  - TC-FA-LIC-243 tidak menyebut field kedua dan hasil irisan; spec memilih `Status` = `Expired`.
  - TC-FA-LIC-244 menulis centang di dropdown ikut hilang tanpa menyebut langkah mengamatinya; spec membuka dropdown sesudah klik chip `(×)`.
  - TC-FA-LIC-241, 242, 243, 244, dan 245 tidak menyebut Post Condition (`-`); tidak ada yang diasersi.
  - Pre-setup #13 memuat satu nilai Plan Owner (`PT Maju Bersama (Distributor)`) untuk keenam alokasi, sedangkan asersi Filter per kelas dropdown memerlukan sedikitnya dua nilai distinct pada kolom yang disaring (S-11): dropdown Plan Owner hanya memuat satu opsi dan Apply atasnya mengembalikan seluruh baris sehingga tidak membuktikan penyaringan. TC tidak diubah dan spec tidak menambah baris milik spec ber-Plan Owner lain, karena Expected TC menyebut enam baris Pre-setup #13 dan opsi dropdown berasal dari DISTINCT data tabel.
