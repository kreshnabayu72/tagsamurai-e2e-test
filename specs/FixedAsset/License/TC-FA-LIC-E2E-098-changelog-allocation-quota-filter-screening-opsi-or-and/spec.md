---
id: TC-FA-LIC-E2E-098-changelog-allocation-quota-filter-screening-opsi-or-and
title: "Filter Modal Changelog Allocation Quota: Screening Panel, Opsi per Dropdown, Aturan OR dan AND, dan Chip"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-341
  - TC-FA-LIC-342
  - TC-FA-LIC-343
  - TC-FA-LIC-344
coverage:
  web: automated
---

# Filter Modal Changelog Allocation Quota: Screening Panel, Opsi per Dropdown, Aturan OR dan AND, dan Chip

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), client PT Sejahtera plan Paid, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Hook suite (sesi API aktor, fixture BE pemulih Pre-setup): dinyatakan sekali di `suite.md`; spec ini merujuknya.
- Data Pre-setup (hanya dibaca; fixture BE pemulih riwayat memulihkannya di hook `before` dan `after`): riwayat Changelog Allocation Quota #27 (6 entri) lewat `Fixture.fixedAssetLicense.changelogAllocationQuota` (fixture belum ada, disediakan tim FE).

  | Date | Action | Group Name | Field | Old Value | New Value | Modified By |
  |---|---|---|---|---|---|---|
  | 30/09/26 11:15 | Edit | — | Quota Alert Level | Normal | Low | System |
  | 29/09/26 10:05 | Edit | Divisi Logistik | Allocated Quota | 500 | 600 | Rudi H |
  | 28/09/26 15:30 | Edit | Divisi IT | Allocated Quota | — | 100 | Dewi L |
  | 27/09/26 09:00 | Remove Allocation | Gudang A | Allocated Quota | 100 | — | Rudi H |
  | 26/09/26 11:20 | Edit | Divisi Keuangan | Allocated Quota | — | 50 | Dewi L |
  | 25/09/26 08:45 | Remove Allocation | Divisi IT | Allocated Quota | 100 | — | Rudi H |

- Data Uji Filter per dropdown (TC-FA-LIC-342), dipakai langkah 12 sampai 16:

  | Dropdown | Opsi (DISTINCT data tabel saat ini) | Opsi dipilih | Hasil (Date) |
  |---|---|---|---|
  | Action | Edit, Remove Allocation | `Remove Allocation` | 27/09/26 09:00, 25/09/26 08:45 |
  | Group Name | Divisi IT, Divisi Keuangan, Divisi Logistik, Gudang A | `Divisi IT` | 28/09/26 15:30, 25/09/26 08:45 |
  | Field | Allocated Quota, Quota Alert Level | `Quota Alert Level` | 30/09/26 11:15 |
  | Modified By | Dewi L, Rudi H, System | `Dewi L` | 28/09/26 15:30, 26/09/26 11:20 |

- Pengecualian S-12 `[KEPUTUSAN 2026-11-02]`: fixture BE pemulih riwayat Pre-setup #27 dijalankan di hook `before` sebelum asersi absolut; suite serial (`parallel: false`); opsi dropdown dan baris hasil Changelog Allocation Quota (langkah 13, 15, 18, 20, dan 29) diasersi absolut tanpa baseline dan hanya valid tepat setelah pemulihan itu, karena fixture juga menghapus entri baru yang ditambahkan spec lain (A-17, dinyatakan di `suite.md`).
- Spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

### TC-FA-LIC-341: Screening Filter Panel: field, tipe komponen, label, dan placeholder

1. Buka tab Allocation Quota pada node All Groups, klik ikon Changelog pada toolbar Level 1 Groups Quota
2. Klik ikon Filter pada toolbar
3. Verifikasi ikon Filter berubah gelap
4. Verifikasi panel tampil di bawah toolbar
5. Verifikasi field berurutan (maksimal 4 per baris): Date, Action, Group Name, Field, Modified By
6. Verifikasi field Date: date range picker, placeholder `Select date`
7. Verifikasi field Action: dropdown multi-select searchable, placeholder `All actions`
8. Verifikasi field Group Name: dropdown multi-select searchable, placeholder `All groups`
9. Verifikasi field Field: dropdown multi-select searchable, placeholder `All fields`
10. Verifikasi field Modified By: dropdown multi-select searchable, placeholder `All users`
11. Verifikasi tombol `[Clear Field]` (kiri, text) dan `[Apply]` (kanan, filled)

### TC-FA-LIC-342: Opsi dan penyaringan per dropdown (Action, Group Name, Field, Modified By)

Untuk setiap baris tabel "Data Uji Filter per dropdown" (langkah 12 sampai 16):

12. Buka dropdown pada baris tabel
13. Verifikasi opsi dropdown sesuai kolom Opsi pada baris tabel
14. Pilih opsi pada kolom Opsi dipilih, klik `[Apply]`
15. Verifikasi tabel menampilkan Date pada kolom Hasil pada baris tabel yang sama
16. Klik `[Clear Field]`, klik `[Apply]`

### TC-FA-LIC-343: Dua opsi dalam satu field memakai OR, antar-field memakai AND

17. Pada `Modified By` centang `Dewi L` dan `System`, klik `[Apply]`
18. Verifikasi `Modified By` = `Dewi L` atau `System` (OR) menampilkan: 30/09/26 11:15, 28/09/26 15:30, 26/09/26 11:20
19. Pada `Group Name` pilih `Divisi IT`, klik `[Apply]`
20. Verifikasi dua field berbeda yang terisi sekaligus memakai irisan (AND): tabel menampilkan 28/09/26 15:30

### TC-FA-LIC-344: Chip: hapus lewat tombol X pada chip menghapus centang di dropdown

21. Klik `[Clear Field]`, klik `[Apply]`
22. Pada `Action` pilih `Edit` dan `Remove Allocation`
23. Klik `(×)` pada chip `Edit` tanpa membuka dropdown
24. Verifikasi chip `Edit` hilang
25. Buka dropdown `Action`
26. Verifikasi centang `Edit` di dropdown ikut hilang
27. Verifikasi chip `Remove Allocation` tetap
28. Tutup dropdown, klik `[Apply]`
29. Verifikasi tabel menampilkan: 27/09/26 09:00, 25/09/26 08:45
30. Klik `[Clear Field]`, klik `[Apply]`, lalu tutup modal dengan `[×]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Langkah penghubung (tanpa `Verifikasi`): langkah 16, 21, dan 30 membersihkan filter antar kasus (S-09); langkah 28 menutup dropdown sebelum `[Apply]`.
- Langkah yang diulang per baris tabel Data Uji Filter: langkah 12 sampai 16 (4 iterasi) (bagian 8b butir 7).
- Spec ini memuat 30 langkah nominal dan sekitar 45 langkah dengan ekspansi. Alasan: seluruh blok adalah Filter Panel modal yang sama dengan dataset yang sama; tiap blok diakhiri `[Clear Field]` dan `[Apply]`, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-LIC-343 langkah 4 ("Tambahkan field kedua") tidak menyebut field dan nilai kedua serta hasil irisan; spec memakai `Group Name` = `Divisi IT` (langkah 19) dan hasil 28/09/26 15:30 yang dihitung dari Pre-setup #27.
  - TC-FA-LIC-344 langkah 3 meminta pilihan `Edit` dan `Remove Allocation` tanpa menyebut cara menutup dropdown sebelum `[Apply]`; spec menutup dropdown di langkah 28.
