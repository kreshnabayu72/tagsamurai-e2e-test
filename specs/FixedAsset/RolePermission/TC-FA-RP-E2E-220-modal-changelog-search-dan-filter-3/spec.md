---
id: TC-FA-RP-E2E-220-modal-changelog-search-dan-filter-3
title: "Modal Changelog: Search dan Filter (3/6)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-714
  - TC-FA-RP-715
  - TC-FA-RP-716
  - TC-FA-RP-717
  - TC-FA-RP-718
coverage:
  web: automated
---

# Modal Changelog: Search dan Filter (3/6)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #42 (Changelog Tab Total Control, enam entri seed, urutan seeding dari terlama ke terbaru: Assign Rina Wulandari (`—` ke `Total Control`, Modified By `Siti R`); Assign Ahmad Fauzi (`—` ke `Total Control`, `Siti R`); Assign Budi Santoso (`—` ke `Total Control`, `Prasetyo H`); Remove Budi Santoso (`Total Control` ke `—`, `Rina W`); Auto-Revert Fitri Handayani (`Total Control` ke `—`, `Siti R`); Assign Maya Anggraeni (`Read Only` ke `Total Control`, `Rina W`); seluruh entri Field `Access Level`; tanggal entri berselang sedikitnya satu hari sehingga rentang TC 718 dapat memisahkan entri). Pre-setup #24 disebut Precondition TC dan dipakai sebagai precondition TC, tidak diasersi. Entri seed #42 ditambahkan fixture backend yang disediakan tim FE/BE di hook `before`. Changelog adalah audit trail permanen (S-12): spec tidak mengasumsikan total entri tetap dan tidak mengasersi total seluruh entri; entri seed dikenali lewat kombinasi Action, User Name, Old Value, dan New Value. Spec ini tidak mengubah data.
- Konfigurasi kolom Setup Column disimpan di browser dan dipulihkan di langkah 4 sampai 5; hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE).
- Tabel Filter multi-select (TC 717):

| Field | Opsi | Hasil yang tampil |
|---|---|---|
| Action | `Auto-Revert` | hanya entri Auto-Revert Fitri Handayani |
| User Name | `Ahmad Fauzi` | hanya entri Assign Ahmad Fauzi |
| Modified By | `Prasetyo Hadi` | hanya entri Assign Budi Santoso |

## Test Steps

### Search terikat visibilitas kolom: kolom ditampilkan kembali (TC 714)

1. Klik ikon Changelog pada toolbar.
2. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`.
3. Hapus centang kolom `Modified By`, lalu klik `[Save]`.
4. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`.
5. Centang kembali kolom `Modified By`, lalu klik `[Save]`.
6. Ketik Search `prasetyo`, tekan Enter.
7. Verifikasi pencarian kembali mencocokkan entri Assign Budi Santoso.
8. Klik ikon `(←)` pada kotak Search.

### Placeholder Search (TC 715)

9. Klik ikon Search.
10. Verifikasi placeholder `Search action, user, or value...` pada modal Tab Total Control.
11. Klik ikon `(←)` pada kotak Search.

### Screening Filter Panel (TC 716)

12. Klik ikon Filter.
13. Verifikasi panel Filter memuat `Date` (date range picker, `Select date`), `Action` (multi-select searchable, `All actions`), `User Name` (multi-select searchable, `All users`), dan `Modified By` (multi-select searchable, `All users`).
14. Verifikasi tidak ada field `Field` karena varian Tab Total Control hanya memiliki satu nilai Field (Single-Value Guard).
15. Verifikasi footer panel memuat `[Clear Field]` dan `[Apply]`.

### Filter per kelas multi-select searchable (TC 717)

16. Untuk setiap baris pada tabel Filter multi-select, lakukan langkah 17 sampai 19.
17. Pilih opsi pada field, lalu klik `[Apply]`.
18. Verifikasi baris yang tampil sesuai kolom Hasil yang tampil pada tabel.
19. Klik `[Clear Field]`, lalu klik `[Apply]`.

### Filter per kelas date range (TC 718)

20. Catat teks tanggal sel Date entri Remove Budi Santoso dan entri Auto-Revert Fitri Handayani.
21. Pilih rentang tanggal field Date dari tanggal entri Remove Budi Santoso sampai tanggal entri Auto-Revert Fitri Handayani, lalu klik `[Apply]`.
22. Verifikasi hanya entri dengan Date di dalam rentang yang tampil: entri Remove Budi Santoso dan entri Auto-Revert Fitri Handayani.
23. Klik `[Clear Field]`, lalu klik `[Apply]`.
24. Klik ikon Filter untuk menutup panel.

## Notes

- Langkah penghubung (S-03): langkah 4 dan 5 (menampilkan kembali kolom `Modified By` sesuai TC 714), 8, 11, 16 (kepala perulangan), 19 dan 23 (membersihkan Filter, sesuai TC), 20 (mencatat tanggal untuk rentang TC 718), dan 24.
- Halaman dan Tab `Total Control` dibuka hook `beforeEach` suite, sehingga langkah TC `Klik Tab Total Control` tidak diulang di Test Steps.
- Temuan untuk QA:
  - TC 717 dan 718 tidak menyatakan apakah panel Filter tetap terbuka sesudah `[Apply]`; spec mengikuti urutan TC (`[Clear Field]` tanpa membuka ulang panel) dan mengasumsikan panel tetap terbuka.
  - TC 718 tidak menyebut nilai rentang tanggal; spec memakai tanggal entri Remove dan Auto-Revert yang dibaca dari tabel, dengan asumsi tanggal entri #42 berselang sedikitnya satu hari.
