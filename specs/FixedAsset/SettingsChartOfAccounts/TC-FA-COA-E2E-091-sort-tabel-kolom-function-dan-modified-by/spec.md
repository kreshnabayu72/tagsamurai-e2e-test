---
id: TC-FA-COA-E2E-091-sort-tabel-kolom-function-dan-modified-by
title: "Sort Tabel: Siklus Tiga Tahap pada Kolom Function dan Modified By"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-173
coverage:
  web: automated
---

# Sort Tabel: Siklus Tiga Tahap pada Kolom Function dan Modified By

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Data milik spec (di-seed hook `before` lewat API, dihapus hook `before` dan `after`; kemampuan seed dan hapus disediakan tim FE/BE, butir "Seed dan pemulihan lewat API" di `suite.md`). Empat akun Active, Used By 0, dengan Function berbeda sebagai padanan P4, P3, P1, dan P2 pada precondition c TC-FA-COA-173. Account Code maksimal 15 karakter sehingga bernilai literal dan memuat nomor spec; urutan Account Code A-Z sama dengan urutan default yang diasersi (padanan P4, P3, P1, P2). Account Name bersuffix `{runId}-091`:

  | Akun | Account Code | Account Name | Function | Modified By |
  |---|---|---|---|---|
  | Padanan P4 | `DID091A` | `Sort Aset {runId}-091` | Asset Cost | user pengubah A |
  | Padanan P3 | `DID091B` | `Sort Gain {runId}-091` | Gain on Disposal | user pengubah B |
  | Padanan P1 | `DID091C` | `Sort Depresiasi {runId}-091` | Depreciation Expense | user pengubah A |
  | Padanan P2 | `DID091D` | `Sort Offset {runId}-091` | Capitalization Offset | user pengubah B |

- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): seed akun dengan dua user pengubah berbeda yang nama lengkapnya berbeda (S-11); identitas user pengubah tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Pengecualian A-18 (butir "Pengecualian A-18" di `suite.md`): Account Code literal `DID091A` sampai `DID091D` hanya dipakai spec ini; seed idempotent dan penghapusan sisa akun dijalankan di hook `before` dan `after`.
- Search `{runId}-091` dipakai agar hanya empat akun milik spec yang tampil pada tabel; urutan relatif diasersi atas empat baris itu, tidak bergantung pada ukuran halaman.
- Kolom Modified By tidak tampil secara default dan ditampilkan lewat Setup Column pada langkah 1 sampai 2 (precondition TC-FA-COA-173); langkah 22 sampai 23 memulihkannya (R-24).
- Urutan relatif yang diasersi pada sort Function (label): Asset Cost (`DID091A`), Capitalization Offset (`DID091D`), Depreciation Expense (`DID091C`), Gain on Disposal (`DID091B`).
- State yang diubah spec: kolom Modified By (ditampilkan lalu disembunyikan lagi), isi kotak Search (dikosongkan langkah 24), dan sort (tiap siklus berakhir netral). Hook `after` menghapus preferensi kolom dan tabel di browser sebagai cadangan (kemampuan disediakan tim FE).
- Flag Guided Tooltip halaman Chart of Accounts di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-173: Sort siklus tiga tahap pada kolom Function dan Modified By

1. Klik header Actions ⋯ > `Setup Column...`
2. Centang kolom `Modified By`, klik `[Save]`
3. Ketik Search `{runId}-091`, tekan Enter
4. Klik header Function satu kali
5. Verifikasi indikator naik (↑) aktif pada header Function
6. Verifikasi baris urut A-Z menurut label: Asset Cost (`DID091A`), Capitalization Offset (`DID091D`), Depreciation Expense (`DID091C`), Gain on Disposal (`DID091B`)
7. Klik header Function kedua kali
8. Verifikasi indikator turun (↓) aktif pada header Function
9. Verifikasi urutan Z-A: Gain on Disposal (`DID091B`), Depreciation Expense (`DID091C`), Capitalization Offset (`DID091D`), Asset Cost (`DID091A`)
10. Klik header Function ketiga kali
11. Verifikasi indikator header Function netral
12. Verifikasi urutan kembali ke default Account Code A-Z: urutan relatif `DID091A`, `DID091B`, `DID091C`, `DID091D`
13. Klik header Modified By satu kali
14. Verifikasi indikator naik (↑) aktif pada header Modified By
15. Verifikasi baris urut A-Z tanpa membedakan huruf besar-kecil menurut nama lengkap user pengubah (nama yang mendasari tampilan `[First Name] [Last Initial]`)
16. Klik header Modified By kedua kali
17. Verifikasi indikator turun (↓) aktif pada header Modified By
18. Verifikasi urutan Z-A menurut nama lengkap user pengubah
19. Klik header Modified By ketiga kali
20. Verifikasi indikator header Modified By netral
21. Verifikasi urutan kembali ke default Account Code A-Z: urutan relatif `DID091A`, `DID091B`, `DID091C`, `DID091D`
22. Klik header Actions ⋯ > `Setup Column...`
23. Hilangkan centang kolom `Modified By`, klik `[Save]`
24. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03, S-09): langkah 1 dan 2 (menampilkan kolom Modified By, precondition d TC-FA-COA-173); langkah 3 (Search `{runId}-091` supaya hanya empat akun milik spec tampil dan urutan relatif tidak bergantung pada ukuran halaman; R-16, R-23, 8b butir 13); langkah 22 dan 23 (pemulihan Setup Column eksplisit, R-24 dan 8b.14); langkah 24 (`(←)` mengosongkan Search dan mereset tabel).
- Kotak Search tetap berisi `{runId}-091` selama kedua siklus sort sehingga tidak diulang sebelum siklus Modified By; klik header sort tidak mengubah isi kotak Search.
- `A-18`: TC-FA-COA-173 memakai Account Code literal `DID091A` sampai `DID091D` (akun milik spec, Name bersuffix `{runId}-091`); seed idempotent dan penghapusan sisa di hook `before` dan `after`. Akun ini dipakai sebagai padanan P1 sampai P4 pada precondition c TC (Function sama, urutan Account Code sama).
- Tiap siklus sort berakhir netral sehingga tidak ada langkah reset sort tambahan.
- Kolom Modified By ditampilkan `[First Name] [Last Initial]` (R-14); sortingnya menurut nama lengkap sesuai Expected d TC-FA-COA-173, sehingga langkah 15 dan 18 mengasersi urutan menurut nama lengkap.
- Spec ini hanya memuat TC-FA-COA-173.
- Temuan untuk QA:
  - TC-FA-COA-173 precondition c menyebut P1 sampai P4 yang berada di antara lebih dari seratus akun Pre-setup; spec memakai empat akun milik spec sebagai padanan agar keempat akun pasti tampil bersama, tanpa mengubah Expected TC.
  - TC-FA-COA-173 tidak menyebut identitas user pengubah akun; spec mengasumsikan dua user pengubah dengan nama lengkap berbeda tersedia (S-11).
  - Butir d dan e TC-FA-COA-173 tidak memberi urutan konkret nama; spec mengasersi urutan menurut nama lengkap tanpa nama literal.
