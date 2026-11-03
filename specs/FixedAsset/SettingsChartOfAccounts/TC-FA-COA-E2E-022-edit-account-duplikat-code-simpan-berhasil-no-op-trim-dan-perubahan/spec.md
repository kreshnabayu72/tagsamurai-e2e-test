---
id: TC-FA-COA-E2E-022-edit-account-duplikat-code-simpan-berhasil-no-op-trim-dan-perubahan
title: "Edit Account: Duplikat Code, Simpan Berhasil, No-Op, Trim, dan Perubahan Huruf"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-COA-37
  - TC-FA-COA-38
  - TC-FA-COA-39
  - TC-FA-COA-40
  - TC-FA-COA-144
  - TC-FA-COA-259
coverage:
  web: automated
---

# Edit Account: Duplikat Code, Simpan Berhasil, No-Op, Trim, dan Perubahan Huruf

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`); halaman Chart of Accounts dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (identitas dibaca dari `Fixture.settingsChartOfAccounts.<kunci>`; fixture belum ada, disediakan tim FE):

  | Kode | Akun | Kondisi | Dipakai |
  |---|---|---|---|
  | P1 | `5-6001 – Depreciation Expense – Admin` | Active, Used By 0, belum pernah diekspor; hanya dibaca (TC-40 diblokir, TC-38 No-Op) | TC-40, TC-38 |
  | P2 | `6-2001 – Repairs & Maintenance Expense` | Ada sebagai akun dengan Account Code pembanding duplikat; hanya dibaca | TC-40 |
  | P45 | `6-2101 – Repairs & Maintenance Expense – Rename`, Function Capitalization Offset | Active, Used By 0, Last Used in Journal `Aug 2026`; sekali pakai | TC-37 |
  | P63 | `CAP-8106 – Capitalization Clearing – Case Change`, Function Capitalization Offset | Active, Used By 0, Last Used in Journal kosong; sekali pakai | TC-39 |
  | P81 | `CAP-8211 – Capitalization Clearing – Trim Edit`, Function Capitalization Offset | Active, Used By 0, Last Used in Journal kosong; sekali pakai | TC-259 |
  | P27 | `CAP-6800 – Capitalization Clearing – Edit Function`, Function Capitalization Offset | Active, Used By 0, belum pernah diekspor; sekali pakai | TC-144 |

- Akun sekali pakai (P45, P63, P81, P27) diubah spec ini; kondisi awalnya disediakan ulang (seed/pemulihan) oleh tim FE/BE di hook `before` dan `after`, termasuk Last Updated. Nilai Account Code literal dengan batas 15 karakter tidak memakai suffix `{runId}`.
- Kemampuan teknis: kemampuan baca jumlah entri Changelog sebelum aksi (TC-144), disediakan tim FE/BE (8b.10).
- Jam server dan jam browser disinkronkan; tidak ada asersi waktu pada spec ini.
- Tabel akun memuat lebih dari satu halaman (ukuran halaman default 10); baris target dibuka lewat Search.
- Flag Guided Tooltip halaman Chart of Accounts disetel true oleh hook suite `before` (butir "Flag Guided Tooltip" di `suite.md`).
- Seed akun Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-COA-40: Edit Account Code ke kode akun lain yang sudah ada ditolak

1. Ketik Search `5-6001`, tekan Enter
2. Klik row action `Edit` pada akun P1 (`5-6001`)
3. Ganti isi Account Code dengan `6-2001`
4. Klik `[Save]`
5. Verifikasi caption "Account code already exists"
6. Verifikasi modal Edit Account tetap terbuka
7. Klik `[✕]` di header modal
8. Verifikasi dialog Unsaved Changes tampil
9. Klik `[Leave]`
10. Verifikasi baris P1 pada tabel tetap menampilkan Account Code `5-6001` sehingga tidak ada perubahan tersimpan

### TC-FA-COA-38: Save tanpa perubahan nilai menjadi No-Op

11. Klik row action `Edit` pada akun P1 (`5-6001`)
12. Klik `[Save]`
13. Verifikasi toast "No changes to save." dengan severity Info
14. Verifikasi modal Edit Account tertutup

### TC-FA-COA-37: Ubah Account Name akun terkunci berhasil disimpan

15. Ganti isi kotak search dengan `6-2101`, tekan Enter
16. Klik row action `Edit` pada akun P45 (`6-2101`)
17. Ganti isi Account Name dengan `Repairs & Maintenance – Expense`
18. Klik `[Save]`
19. Verifikasi toast "Success, account has been updated."
20. Verifikasi modal Edit Account tertutup
21. Verifikasi tabel menampilkan Account Name baru `Repairs & Maintenance – Expense` pada akun P45

### TC-FA-COA-39: Perubahan huruf besar-kecil saja pada Account Code dicatat sebagai perubahan

22. Ganti isi kotak search dengan `CAP-8106`, tekan Enter
23. Tunggu toast lama hilang otomatis
24. Klik row action `Edit` pada akun P63 (`CAP-8106`)
25. Ganti isi Account Code dengan `cap-8106`
26. Klik `[Save]`
27. Verifikasi toast "Success, account has been updated."
28. Verifikasi perubahan tersimpan: baris P63 pada tabel menampilkan Account Code `cap-8106`

### TC-FA-COA-259: Spasi di ujung Account Code dan Account Name dibuang saat disimpan

29. Ganti isi kotak search dengan `CAP-8211`, tekan Enter
30. Tunggu toast lama hilang otomatis
31. Klik row action `Edit` pada akun P81 (`CAP-8211`)
32. Ganti isi Account Code dengan `CAP-8211A  ` (spasi di ujung)
33. Ganti isi Account Name dengan `  Capitalization Clearing – Trim Edit  ` (spasi di awal dan akhir)
34. Klik `[Save]`
35. Verifikasi toast "Success, account has been updated."
36. Verifikasi tabel menampilkan Account Code `CAP-8211A` dan Account Name `Capitalization Clearing – Trim Edit` tanpa spasi di ujung pada akun P81

### TC-FA-COA-144: Edit Account Function pada akun yang tidak terkunci berhasil disimpan

37. Ganti isi kotak search dengan `CAP-6800`, tekan Enter
38. Tunggu toast lama hilang otomatis
39. Buka Changelog, catat jumlah entri sebagai baseline, lalu tutup Changelog
40. Klik row action `Edit` pada akun P27 (`CAP-6800`)
41. Verifikasi Account Function Enabled
42. Ubah Account Function menjadi Depreciation Expense
43. Klik `[Save]`
44. Verifikasi toast "Success, account has been updated."
45. Verifikasi modal Edit Account tertutup
46. Verifikasi baris P27 menampilkan Function `Depreciation Expense`
47. Buka Changelog
48. Verifikasi jumlah entri Changelog bertambah tepat satu dari baseline langkah 39
49. Verifikasi baris teratas Changelog: Action Edit, Account Code `CAP-6800`, Field Account Function, Old Value `Capitalization Offset`, New Value `Depreciation Expense`
50. Tutup Changelog

## Notes

- Spec 50 langkah, di atas ambang 35 langkah. Alasan: seluruh blok satu topik aksi (Edit akun, kasus ditolak dahulu lalu kasus sukses, S-10) dengan akun sekali pakai milik blok masing-masing; pola Search, buka Edit, ubah field, `[Save]`, lalu `Verifikasi` berulang per akun (8b.7), dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Penutupan form dirty TC-40 (langkah 7 sampai 9) dan baca Changelog TC-144 (langkah 39, 47 sampai 50) menambah langkah.
- Urutan blok: TC-40 (diblokir) lebih dulu, lalu TC-38 (No-Op), TC-37, TC-39, TC-259, dan TC-144 (S-10); dua langkah pertama TC-38 memakai Search `5-6001` dari langkah 1 yang masih berlaku.
- Langkah penghubung (S-03, R-16): Search Account Code untuk membuka baris target (langkah 1, 15, 22, 29, 37); "Tunggu toast lama hilang otomatis" (langkah 23, 30, 38) mencegah toast sebelumnya dengan teks sama lolos sebagai asersi (R-12); langkah 7 sampai 9 menutup form dirty TC-40 deterministik (S-08); langkah 39 mencatat baseline Changelog sebelum aksi pemicu (S-12) dan Changelog ditutup sebelum membuka form Edit; langkah 50 menutup Changelog.
- Cara baca Changelog TC-144 (S-14): entri baru dibaca pada baris teratas urutan default Date terbaru setelah selisih satu dari baseline dibuktikan (langkah 48).
- Asersi "tidak ada perubahan tersimpan" TC-40 (langkah 10) dibaca dari baris P1 sesudah modal ditutup lewat `[Leave]`.
- Asersi tidak ada pencatatan atau log tidak ada di spec ini (S-05).
- Temuan untuk QA:
  - Post Condition TC-37 (Name tersimpan, log L-02 satu baris Account Name, dampak di Asset Class dan Preferences), TC-38 ("Tidak ada entri log"), TC-39 (log L-02 Old `CAP-8106` New `cap-8106`), TC-259 (nilai ter-trim di log L-02), dan TC-144 butir b (log di System Log dan Activity Log) tidak punya langkah observasi di TC sehingga tidak diasersi; hanya Changelog TC-144 yang punya Expected (butir d).
  - TC-144 Post Condition butir c (Alert dependensi di halaman Accounting, §9.7 S-14) ditandai TC "tanpa asersi detail di TC ini" dan tidak diasersi.
