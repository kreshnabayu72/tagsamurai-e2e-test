---
id: TC-FA-GRP-E2E-085-bulk-delete-would-empty-dan-scope-aktor-jadi-kosong
title: "Bulk Delete: Would-Empty Dicek Paling Awal dan Scope Aktor Menjadi Kosong"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-259
  - TC-FA-GRP-260
coverage:
  web: automated
---

# Bulk Delete: Would-Empty Dicek Paling Awal dan Scope Aktor Menjadi Kosong

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Total Control client khusus tiga group (email dan `Spectra.env.FA_THREEGRP_TC_PASSWORD` disediakan tim FE, tidak tertulis di Pre-setup TC); halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE) mengikuti `suite.md`; hook `after` mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).
- Nama data Dinamis di Test Steps ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-NNN` (NNN = nomor spec ini) dan sama di seeding, asersi teks, dan cleanup. Nilai mengacu `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas `fixtures/fixedAssetSettingsGroups.json` belum ada; ditambahkan tim FE).
- Akun ganti (langkah 7): Manage Group R+D dengan scope hanya `Scope A` dan `Scope B` (email dan `Spectra.env.FA_MGRD_AB_PASSWORD` disediakan tim FE, tidak tertulis di Pre-setup TC). Hook `after` mengembalikan sesi ke akun default suite.
- Data: client khusus tiga group, sebagian beraset (Pre-setup, hanya dibaca; dialog blokir tidak menghapus apa pun). `Scope A` dan `Scope B` adalah group kosong milik spec (di-seed lewat API di `before` pada client yang dipakai akun Manage Group R+D) dan scope akun ditetapkan seeding API (disediakan tim FE/BE).
- Cleanup di `after`: hapus data seed lewat API dan lepas assignment scope.

## Test Steps

### TC-FA-GRP-259: Would-empty dicek paling awal

1. Centang 1 baris, lalu klik Select All ([N] records) dengan N = 3
2. Buka Bulk Action, pilih `Delete`
3. Verifikasi dialog dengan title "Cannot Delete Groups", isi "You've selected all remaining groups. At least one group must always exist — deselect at least one group and try again.", dan tombol [OK]
4. Klik [OK]
5. Verifikasi ketiga group tetap ada di tabel (tidak ada proses parsial)
6. Klik (X)

### TC-FA-GRP-260: Scope aktor menjadi kosong

7. Logout, lalu login sebagai Manage Group R+D scope `Scope A` dan `Scope B`
8. Buka Fixed Asset > Settings > Groups
9. Verifikasi `Scope A` dan `Scope B` tampil di tabel (group dalam scope aktor)
10. Centang `Scope A` dan `Scope B`
11. Buka Bulk Action, pilih `Delete`
12. Verifikasi dialog dengan title "Cannot Delete Groups", isi "You can't delete every group you're assigned to. Ask an admin to assign you another group first.", dan tombol [OK]
13. Klik [OK]
14. Verifikasi `Scope A` dan `Scope B` tetap ada di tabel (tidak ada yang terhapus)

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 6 sampai 8: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Ganti akun ke Manage Group R+D ditulis eksplisit (langkah 7, S-07). Langkah 9 adalah anchor positif untuk asersi "tidak ada yang terhapus" (8b butir 2).
- Temuan untuk QA:
  - TC-259 Precondition "Client hanya punya 3 group (sebagian beraset)" tidak menyebut akun client tersebut; disediakan tim FE.
  - TC-260 tidak menyebut client tempat `Scope A` dan `Scope B` berada dan cara scope akun ditetapkan.
