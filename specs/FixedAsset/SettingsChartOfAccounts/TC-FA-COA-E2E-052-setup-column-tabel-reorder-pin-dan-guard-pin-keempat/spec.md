---
id: TC-FA-COA-E2E-052-setup-column-tabel-reorder-pin-dan-guard-pin-keempat
title: "Setup Column Tabel: Reorder, Pin, dan Guard Pin Keempat"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-190
  - TC-FA-COA-194
  - TC-FA-COA-332
  - TC-FA-COA-333
coverage:
  web: automated
---

# Setup Column Tabel: Reorder, Pin, dan Guard Pin Keempat

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Data: tabel Chart of Accounts client default berisi akun Pre-setup P1 sampai P5 dan akun lain hasil seed (lihat Seed dan pemulihan di `suite.md`); spec hanya memakai kolom tabel.
- Kolom default Visible untuk langkah berulang (langkah 3 dan 4):

  | Kolom |
  |---|
  | `Active` |
  | `Account Code` |
  | `Account Name` |
  | `Function` |
  | `Used By` |
  | `Last Used in Journal` |

- Konfigurasi kolom awal: default modul (Modified By dan Last Updated hidden, tanpa kolom terpin).
- State yang diubah spec: konfigurasi kolom tersimpan lewat `[Save]` pada langkah 23, 28, dan 33; dipulihkan dengan langkah eksplisit 35 sampai 39. Hook `after` menghapus preferensi kolom di browser sebagai cadangan (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Flag Guided Tooltip halaman Chart of Accounts di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-190: Drag and drop reorder kolom default Visible

1. Klik header kolom Actions ⋯
2. Klik `Setup Column...`
3. Seret baris kolom `Active` ke posisi paling bawah daftar modal
4. Verifikasi kolom `Active` menjadi kolom data terakhir sebelum kolom Actions pada pratinjau tabel
5. Ulangi langkah 3 dan 4 untuk setiap kolom lain pada tabel Prerequisites (`Account Code`, `Account Name`, `Function`, `Used By`, `Last Used in Journal`)
6. Verifikasi kolom checkbox tetap di paling kiri dan kolom Actions tetap di paling kanan
7. Tutup modal dengan ikon ✕

### TC-FA-COA-194: Guard pin ke-4

8. Klik header kolom Actions ⋯
9. Klik `Setup Column...`
10. Pin kolom Active, Account Code, dan Account Name
11. Arahkan kursor ke ikon Pin kolom Function, lalu klik ikon itu
12. Verifikasi ikon Pin kolom Function Disabled dengan tooltip "Maximum 3 columns can be pinned at once. Unpin another column first."
13. Verifikasi kolom Function tidak menjadi beku
14. Unpin kolom Active
15. Klik ikon Pin kolom Function
16. Verifikasi ikon Pin kolom Function Enabled
17. Verifikasi kolom Function menjadi beku
18. Tutup modal dengan ikon ✕

### TC-FA-COA-332: Reorder kolom default Hidden

19. Klik header kolom Actions ⋯
20. Klik `Setup Column...`
21. Centang kolom Modified By dan Last Updated
22. Seret baris Modified By ke atas baris Used By
23. Klik `[Save]`
24. Verifikasi Modified By tampil sebelum Used By pada urutan kolom tabel

### TC-FA-COA-333: Pin dan unpin kolom default Hidden

25. Klik header kolom Actions ⋯
26. Klik `Setup Column...`
27. Klik ikon Pin pada baris Last Updated
28. Klik `[Save]`
29. Verifikasi kolom Last Updated terpin
30. Klik header kolom Actions ⋯
31. Klik `Setup Column...`
32. Klik ikon Pin pada baris Last Updated
33. Klik `[Save]`
34. Verifikasi kolom Last Updated tidak lagi terpin

### Pemulihan Setup Column

35. Klik header kolom Actions ⋯
36. Klik `Setup Column...`
37. Seret baris Modified By ke posisi di bawah baris Last Used in Journal
38. Hapus centang kolom Modified By dan Last Updated
39. Klik `[Save]`

## Notes

- Alasan spec di atas sekitar 35 langkah (39 langkah nominal, sekitar 45 dengan ekspansi langkah 5): semua blok memakai satu tabel, satu popup Setup Column, dan satu kelas harness (fungsional Setup Column); langkah 3 dan 4 diulang untuk enam kolom pada tabel Prerequisites (idiom 8b.7), `Verifikasi` tetap satu per klausa, dan tiap blok berdiri sendiri.
- Langkah 5 mengulang langkah 3 dan 4 untuk lima kolom lain.
- Langkah penghubung (S-03): langkah 7 dan 18 (menutup popup tanpa `[Save]`, perubahan dibuang), langkah 21 (menyiapkan precondition TC-332), langkah 35 sampai 39 (pemulihan Setup Column eksplisit, R-24 dan 8b.13).
- Pin dan unpin pada TC-333 mengikuti TC sumber: unpin pada langkah 32 menyusul `[Save]` pada langkah 33.
- Urutan 190, 194, 332, 333 dipilih agar blok yang tidak menyimpan konfigurasi berjalan lebih dulu.
- Pin/unpin kolom default Visible (TC-FA-COA-191) ada di spec 092.
- Temuan untuk QA:
  - TC-190 butir g (kolom checkbox di kiri dan Actions di kanan) tidak menyebut kapan diamati; spec mengasersinya setelah seluruh seret selesai (langkah 6).
  - TC-333 tidak menyebut cara mengamati status terpin selain tampilan tabel; spec mengasersi status terpin dari tabel setelah `[Save]`.
