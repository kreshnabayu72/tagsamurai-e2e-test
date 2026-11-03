---
id: TC-FA-CAT-E2E-112-modal-changelog-screening-isi-baris-path-snapshot-modified-by-dan-placeholder
title: "Modal Changelog: Screening Tiga Zona, Isi Baris, Path Snapshot, Modified By, Empty State Terfilter, dan Placeholder Search"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-388
  - TC-FA-CAT-389
  - TC-FA-CAT-390
  - TC-FA-CAT-391
  - TC-FA-CAT-393
  - TC-FA-CAT-418
coverage:
  web: automated
---

# Modal Changelog: Screening Tiga Zona, Isi Baris, Path Snapshot, Modified By, Empty State Terfilter, dan Placeholder Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup #20 (CatMain) dan #23 (Changelog CatMain), hanya dibaca dan tidak diubah: 12 baris riwayat sesuai Example Data PRD §4.1 (Create `Electronics`, Create `Electronics › Laptop`, Create `Vehicle`, Edit rename `Laptop` ke `Notebook` dan Code `LAP-01` ke `NBK-01`, Edit Description `Furniture`, Delete `Kunci Locker`, Delete `Peripheral` dan `Accessory` satu batch, Marked/Restored as Excess, Marked as Excess `Heavy Equipment` oleh System). Modified By `John Doe` tampil `John D`. Seed client disediakan tim FE/BE (lihat Hook suite di `suite.md`); fixture `fixtures/settings-categories.json` disediakan tim FE.
- Changelog CatMain bertambah oleh spec lain dan tidak pernah dikosongkan. Asersi isi dan urutan hanya atas baris seed Pre-setup #23, dibatasi Filter Date 20 Jun 2026 sampai 1 Jul 2026 (rentang tanggal Example Data PRD §4.1, tanggal baris spec lain berada di luar rentang itu; S-14). Filter dipasang lewat langkah penghubung.
- Flag Guided Tooltip halaman Categories di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-388: Screening Modal Changelog

1. Klik icon Changelog di Table Tools
2. Verifikasi Zona Header memuat Title `Changelog: Category`
3. Verifikasi Zona Header memuat toolbar Search, Filter, dan Download
4. Verifikasi Zona Header memuat icon Close (✕)
5. Verifikasi Zona Body memuat kolom Date (sortable), Action (sortable), Category Name (sortable), Field (sortable), Old Value (sortable), New Value (sortable), Modified By (sortable), dan Column Visibility (⋯) (unsortable)
6. Verifikasi default sort Date Newest First
7. Verifikasi Category Name berupa plain text, bukan tautan
8. Verifikasi Zona Footer memuat pagination default 10 data per halaman
9. Verifikasi modal selebar `lg` tanpa button teks Close
10. Klik icon Filter di toolbar modal, pilih rentang tanggal 20 Jun 2026 sampai 1 Jul 2026 pada field Date, lalu klik `[Apply]`

### TC-FA-CAT-389: Isi baris mencakup seluruh Action dan Field

11. Ubah jumlah baris per halaman Changelog menjadi 25
12. Baca baris-baris riwayat dan catat nilai Action, Field, Old Value, dan New Value
13. Verifikasi Action yang muncul: `Create`, `Edit`, `Delete`, `Marked as Excess (Category Consolidation)`, dan `Restored from Excess (Category Consolidation)`
14. Verifikasi Action ditulis dalam teks biasa, bukan badge
15. Verifikasi Field yang muncul: `Category Name`, `Code`, `Description`, dan `Excess`
16. Verifikasi baris Create: Old Value `—` dan New Value nama kategori
17. Verifikasi baris Delete: Old Value nama kategori dan New Value `—`
18. Verifikasi baris Marked: Old Value `Usable` dan New Value `Excess`
19. Verifikasi baris Restored: Old Value `Excess` dan New Value `Usable`

### TC-FA-CAT-390: Category Name memuat full path snapshot

20. Cari baris Edit rename `Laptop` ke `Notebook` dan baris Create `Electronics › Laptop`
21. Verifikasi Category Name baris rename menampilkan path setelah commit `Electronics › Notebook`
22. Verifikasi Old Value baris rename `Laptop` dan New Value `Notebook` (nama exact node, bukan path)
23. Verifikasi baris Level 1 menampilkan nama kategori saja pada Category Name
24. Verifikasi seluruh baris dari satu Edit memiliki path yang sama

### TC-FA-CAT-391: Modified By berformat singkat

25. Hover nilai Modified By `John D`
26. Verifikasi teks plain `John D`
27. Verifikasi tooltip nama lengkap `John Doe`
28. Verifikasi baris aksi sistem (fallback T-0) menampilkan `System`

### TC-FA-CAT-393: Search tanpa hasil

29. Ketik Search `tidak-ada-xyz`, tekan Enter
30. Verifikasi Title `No results found` tampil
31. Verifikasi Description `Try adjusting your search or filter.` tampil

### TC-FA-CAT-418: Placeholder Search

32. Klik icon panah (←) di kiri toolbar untuk menutup kotak Search
33. Klik icon Search di toolbar modal
34. Verifikasi placeholder input Search `Search action, category name, field...`
35. Verifikasi input langsung fokus

## Notes

- Langkah penghubung (S-03): langkah 10 (membatasi Changelog ke rentang Date baris seed Pre-setup #23, S-14), 11 (menampilkan seluruh 12 baris riwayat seed pada satu halaman), 12 dan 20 (membaca dan mencari baris), 32 (menutup kotak Search sebelum TC-418).
- Temuan untuk QA:
  - TC-389 menyebut baris "Restored from Excess" dan "Marked as Excess" tetapi TC tidak menyebut jumlah baris per halaman yang dipakai; spec menampilkan 25 baris per halaman (langkah 11).
  - Pre-setup #23 menyebut "rename ancestor setelah Create anak" tanpa tanggal; rentang Filter Date spec memakai tanggal 11 baris Example Data PRD §4.1 (20 Jun 2026 sampai 1 Jul 2026), sehingga baris itu hanya teramati bila tanggalnya berada di rentang tersebut. Mohon QA menambahkan tanggal seed pada Pre-setup #23.
  - TC-391 butir b menyebut baris Fallback T-0 tanpa menyebut Pre-setup #23 memuat baris itu secara eksplisit; spec mengandalkan baris Marked as Excess untuk Heavy Equipment oleh System pada Data Uji #23.
  - TC-390 butir c ("seluruh baris satu Edit memiliki path yang sama") tidak menyebut baris mana yang dibandingkan; spec membandingkan baris rename Category Name dan Code.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
