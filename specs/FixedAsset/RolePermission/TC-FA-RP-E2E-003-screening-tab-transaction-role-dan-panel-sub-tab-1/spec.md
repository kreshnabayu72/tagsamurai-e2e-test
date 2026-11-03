---
id: TC-FA-RP-E2E-003-screening-tab-transaction-role-dan-panel-sub-tab-1
title: "Screening Tab Transaction Role dan panel sub-tab (1/2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-7
  - TC-FA-RP-8
  - TC-FA-RP-9
coverage:
  web: automated
---

# Screening Tab Transaction Role dan panel sub-tab (1/2)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control Company Alpha (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `FA_TC_PASSWORD`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati), Company Alpha | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |
| Total Control pada `Client Addon On` (lisensi Addon Audit, Maintenance, Tracking aktif) | #31 | disediakan tim FE (email tidak tertulis di Pre-setup TC; lihat Temuan untuk QA) | `Spectra.env.FA_ADDON_ON_TC_PASSWORD` |

- Data Pre-setup: #18 (pohon group Company Alpha dan, untuk TC-FA-RP-8, struktur group yang sama pada `Client Addon On`), #19 (seed Role Transaksi pada `IT Infrastructure` sub-tab Disposal: Asset Admin Nadia Putri, Monitoring & Report Oscar Pratama, Staff Putri Wulandari, Approver Pandu Wijaya; Require Approval OFF di semua node), #31 (`Client Addon On`).
- Tabel iterasi sub-tab untuk TC-FA-RP-8 (sub-tab bersection Staff; urutan baris = urutan iterasi): `Disposal`, `Audit`, `Repair Ticketing`, `Tracking`, `Maintenance Routine`.
- Tabel iterasi sub-tab untuk TC-FA-RP-9 (sub-tab tanpa section Staff): `Borrowing & Assignment`, `Damaged`, `Missing`.
- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun, nama group, dan nama pengguna ditambahkan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): akun Total Control pada `Client Addon On`; struktur group (#18) dan seed Role Transaksi (#19) tersedia pada company itu.
- Spec tidak mengubah data; tidak ada pemulihan selain sesi akun di hook `after`.

## Test Steps

### TC-FA-RP-7: Screening Tab Transaction Role saat belum ada node group terpilih

1. Klik Tab `Transaction Role`
2. Verifikasi Breadcrumb tampil `Settings > Role & Permission > Transaction Role`
3. Verifikasi ikon `[Changelog]` tampil rata kanan di baris sub-tab (bukan tombol global di header halaman)
4. Verifikasi sub-tab tampil berurutan `Borrowing & Assignment | Transfer | Disposal | Damaged | Missing | Audit | Repair Ticketing | Tracking | Maintenance Routine` dengan sub-tab `Borrowing & Assignment` aktif
5. Verifikasi Sidebar Group Tree tampil dengan `All Groups` aktif
6. Verifikasi area kerja memuat card prompt `Select a group from the sidebar to view and manage its approval settings.`
7. Verifikasi toggle, radio, tabel role, dan `[+ Assign]` tidak tampil (Hidden)

### TC-FA-RP-9: Screening panel sub-tab tanpa section Staff

8. Klik node `IT Infrastructure` di Sidebar Group Tree
9. Untuk setiap baris tabel iterasi sub-tab TC-FA-RP-9 (langkah 9 sampai 13): klik sub-tab pada baris tabel
10. Verifikasi tiga section role tampil berurutan Asset Admin, Monitoring & Report, Approver pada sub-tab itu
11. Verifikasi section Staff tidak tampil pada sub-tab itu
12. Verifikasi kartu Approval Rule tampil dengan toggle `Require Approval for [Transaction Type]` OFF (nama sub-tab)
13. Verifikasi radio OR/AND tidak tampil pada sub-tab itu

### TC-FA-RP-8: Screening panel sub-tab bersection Staff (Disposal, Audit, Repair Ticketing, Tracking, Maintenance Routine)

14. Logout dari akun Total Control Company Alpha, lalu login sebagai Total Control `Client Addon On` dengan `Spectra.env.FA_ADDON_ON_TC_PASSWORD`
15. Buka menu Settings > Role & Permission dari sidebar
16. Klik Tab `Transaction Role`
17. Klik node `IT Infrastructure` di Sidebar Group Tree
18. Untuk setiap baris tabel iterasi sub-tab TC-FA-RP-8 (langkah 18 sampai 21): klik sub-tab pada baris tabel
19. Verifikasi kartu Approval Rule dengan toggle `Require Approval for [Transaction Type]` (nama sub-tab) tampil OFF
20. Verifikasi empat section role tampil berurutan Asset Admin, Monitoring & Report, Staff, Approver
21. Verifikasi tiap tabel berkolom `Name (sortable) | Position (sortable) | Division (sortable) | Column Visibility (⋯)` dengan toolbar `Search | Filter | [+ Assign]`
22. Klik sub-tab `Disposal`
23. Verifikasi baris seed tampil: Nadia Putri (Asset Admin), Oscar Pratama (Monitoring & Report), Putri Wulandari (Staff), Pandu Wijaya (Approver)
24. Verifikasi tidak ada kolom Checkbox dan tidak ada bulk action pada kelima sub-tab

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-7, 8, 9). Urutan di spec: TC-FA-RP-7, TC-FA-RP-9, lalu TC-FA-RP-8, karena TC-FA-RP-8 berjalan pada `Client Addon On` sehingga ganti akun diletakkan terakhir (langkah 18 didahului ganti akun); TC-FA-RP-7 dan 9 berjalan pada akun hook `before`.
- Spec Role Matrix tidak berlaku (bukan matriks per role). Spec ditulis per blok akun karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Langkah penghubung (tanpa awalan `Verifikasi`): klik tab, node, dan sub-tab; ganti akun (langkah 14); buka menu dan Tab `Transaction Role` setelah ganti akun; klik sub-tab `Disposal` untuk memeriksa baris seed.
- Pengulangan (bagian 8b butir 7): langkah 9 sampai 13 diulang untuk 3 sub-tab TC-FA-RP-9; langkah 18 sampai 21 diulang untuk 5 sub-tab TC-FA-RP-8. Parameter tiap iterasi ada di tabel iterasi pada Prerequisites.
- Alasan di atas sekitar 35 langkah setelah ekspansi (24 langkah nominal; 3 iterasi 5 langkah dan 5 iterasi 4 langkah menjadi 50 langkah setelah ekspansi): seluruh blok satu topik (screening panel sub-tab Tab Transaction Role) dan satu kelas fungsional, hanya aksi klik tanpa mengubah data; kegagalan satu iterasi tidak membuat iterasi lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-RP-8 precondition d meminta company `Client Addon On` (Pre-setup #31), sedangkan TC itu juga merujuk #18 dan #19 (struktur group dan seed Role Transaksi Company Alpha); Pre-setup #31 hanya menyebut lisensi Addon dan Total Control. Spec mengasumsikan struktur group dan seed Disposal yang sama tersedia pada `Client Addon On` dan akun Total Control company itu disediakan tim FE.
  - TC-FA-RP-8 expected d menyebut "tidak ada kolom Checkbox dan tidak ada bulk action"; spec memeriksanya pada kelima sub-tab yang sudah dibuka.
  - Post Condition TC-FA-RP-7, 8, dan 9 tidak memberi langkah observasi tambahan; tidak diasersi.
