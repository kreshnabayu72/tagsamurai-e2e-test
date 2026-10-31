---
id: TC-GS-IMPORT-E2E-114-dialog-konfirmasi-backdrop-esc-dan-discard-draft-screening-cancel
title: "Dialog konfirmasi (backdrop, Esc) dan Discard Draft: screening, Cancel, double-submit tombol konfirmasi, halaman basi, hapus draft"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-280
  - TC-GS-IMPORT-281
  - TC-GS-IMPORT-282
  - TC-GS-IMPORT-284
  - TC-GS-IMPORT-666
  - TC-GS-IMPORT-695
coverage:
  web: automated
---

# Dialog konfirmasi (backdrop, Esc) dan Discard Draft: screening, Cancel, double-submit tombol konfirmasi, halaman basi, hapus draft

## Prerequisites

- Mode: FE+BE (backend nyata) dengan intercept parsial untuk menunda respons pada TC-666 (menahan respons hanya untuk mengamati state loading dan jumlah permintaan, bukan kegagalan yang dipaksakan).
- Suite serial (`parallel: false`) karena draft Import dibagikan ke seluruh admin satu client dan hook umur draft mengubah state global (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Penghapus draft kedua (hanya memicu perubahan state, P-2): sesi API dengan akun Total Control Client A yang sama pada konteks terpisah; klien HTTP disediakan tim FE/BE.
- Layar awal: hook `beforeEach` membuka Global Settings > Import > Brand untuk Client A.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini, lihat `suite.md`.
- Data Dinamis (nama literal karena asersi bergantung pada isi dan jumlah baris; pengecualian S-12): D-01 (Draft Brand 12 baris `pending`: #1 `Acme Corp`, #2 `Lenovo`, #3 `Zebra Technologies`, ..., #5 `Dell`, ..., #12 `Asus`) dengan umur draft ≥24 jam (D-76 varian 1: `created_at` job dimundurkan 25 jam lewat fixture timestamp atau jam server, disediakan tim FE/BE; umur hanya pemicu Unsaved Banner, bukan batas yang diuji; dimundurkan oleh langkah 1 untuk blok pertama dan oleh langkah 34, 42, 50 untuk blok berikutnya, bukan oleh hook `beforeEach`), dipulihkan lewat skrip pemulihan sebelum tiap blok (Kontrak Fixture R2). Nilai ubahan: `Acme Corporation`. Hitungan notifikasi lonceng dibaca sebagai baseline pada TC-282.
- Tabel "Dialog backdrop dan Esc" (TC-695):

  | No | Dialog | Cara membuka | Pembersihan sesudah Esc |
  |---|---|---|---|
  | 1 | Delete Row | klik `⋯` baris #3 lalu `Remove` | tidak ada |
  | 2 | Delete Rows | centang baris #2 dan #5 lalu `[Bulk Action ▾]` > `[Delete]` | klik `[×]` pada Bulk Action Bar |
  | 3 | Discard Draft | klik `[Discard]` pada Unsaved Banner | tidak ada |

- Tabel "Double-submit tombol konfirmasi" (TC-666; intercept menunda respons permintaan tombol itu):

  | No | Varian | Persiapan | Tombol konfirmasi | Toast sukses |
  |---|---|---|---|---|
  | 1 | Save sesi Edit | klik `⋯` baris #1, pilih `Edit`, ubah Brand Name menjadi `Acme Corporation` | `[Save]` | Success, row has been updated. |
  | 2 | Remove | klik `⋯` baris #3, pilih `Remove` | `[Delete]` | Success, row has been deleted. |
  | 3 | Bulk Delete | centang baris #2 dan #5, klik `[Bulk Action ▾]` lalu `[Delete]` | `[Delete]` | Success, row has been deleted. |
  | 4 | Discard Draft | klik `[Discard]` pada Unsaved Banner | `[Discard Draft]` | Success, draft has been discarded. |
- Kemampuan teknis: intercept jaringan untuk menunda respons dan mencatat jumlah permintaan (`Spectra.intercept()`; dilepas segera setelah dipakai), hook umur draft D-76, sesi API penghapus draft kedua, pembacaan jumlah notifikasi lonceng, tombol keyboard Esc, klik backdrop dialog (disediakan tim FE/BE).
- State global: `created_at` draft atau jam server diubah oleh D-76; hook `after` memulihkan jam server, melepas intercept, dan memulihkan draft Client A ke D-01.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): pulihkan draft Client A ke D-01, lepas intercept, pulihkan jam server, lepas kunci sesi edit.

## Test Steps

### TC-GS-IMPORT-280: Screening Dialog Discard Draft

1. Mundurkan `created_at` draft D-01 Client A 25 jam (D-76 varian 1) lewat skrip fixture, lalu muat ulang halaman Import > Brand
2. Klik `[Discard]` pada Unsaved Banner
3. Verifikasi dialog dengan Title "Discard Draft" dan Body "Are you sure you want to discard this draft? All uploaded and edited rows will be permanently deleted."
4. Verifikasi dialog memiliki tombol `[Cancel]` dan `[Discard Draft]`

### TC-GS-IMPORT-281: Cancel pada dialog Discard Draft

5. Klik `[Cancel]`
6. Verifikasi dialog tertutup
7. Verifikasi footer `[Import (12)]` (draft tetap 12 baris)
8. Verifikasi Unsaved Banner tetap tampil

### TC-GS-IMPORT-695: Backdrop tidak menutup dialog, Esc setara Cancel

Untuk setiap baris tabel "Dialog backdrop dan Esc" (langkah 9 sampai 15 diulang tiga kali, urutan No 1 sampai 3):

9. Buka dialog sesuai kolom Cara membuka
10. Klik backdrop (area gelap di luar dialog)
11. Verifikasi dialog tetap terbuka
12. Tekan Esc
13. Verifikasi dialog tertutup
14. Verifikasi draft tetap 12 baris dan baris #3 `Zebra Technologies` tetap ada
15. Lakukan Pembersihan sesuai kolom Pembersihan sesudah Esc (aksi tanpa `Verifikasi`)

### TC-GS-IMPORT-695 varian 4: Unsaved Changes

16. Klik `⋯` pada baris #1, pilih `Edit`
17. Ubah Brand Name baris #1 menjadi `Acme Corporation`
18. Klik menu sidebar Global Settings > User
19. Klik backdrop (area gelap di luar dialog)
20. Verifikasi dialog Unsaved Changes tetap terbuka
21. Tekan Esc
22. Verifikasi dialog tertutup
23. Verifikasi pengguna tetap di Import > Brand
24. Verifikasi baris #1 tetap input bernilai `Acme Corporation` dan footer tetap `[Cancel]` dan `[Save]` (sesi edit dan perubahan utuh)
25. Klik `[Cancel]`, lalu klik `[Discard]` pada dialog Discard Changes

### TC-GS-IMPORT-666: Double-submit tombol konfirmasi (varian 1 sampai 3)

Untuk setiap baris No 1 sampai 3 tabel "Double-submit tombol konfirmasi" (langkah 26 sampai 33 diulang tiga kali):

26. Tunggu toast lama hilang otomatis; lakukan Persiapan sesuai tabel sampai tombol konfirmasi siap diklik
27. Atur intercept jaringan agar respons permintaan tombol konfirmasi ditunda
28. Klik tombol konfirmasi dua kali berturut-turut dengan cepat
29. Verifikasi tombol konfirmasi tampil Disabled dengan indikator loading
30. Verifikasi intercept mencatat tepat satu permintaan
31. Lepaskan respons permintaan yang ditunda dan lepas intercept
32. Verifikasi tepat satu toast sukses sesuai kolom Toast sukses
33. Pulihkan draft Brand Client A ke D-01 lewat skrip pemulihan (aksi tanpa `Verifikasi`), lalu muat ulang halaman

### TC-GS-IMPORT-284: Discard Draft dari halaman basi setelah draft dihapus admin lain

34. Mundurkan `created_at` draft 25 jam (D-76 varian 1), lalu muat ulang halaman Import > Brand
35. Verifikasi Unsaved Banner tampil pada halaman (Tab 1)
36. Penghapus draft kedua melakukan Discard Draft lewat sesi API hingga tersimpan
37. Pada halaman yang belum dimuat ulang: klik `[Discard]` pada Unsaved Banner
38. Klik `[Discard Draft]`
39. Verifikasi tidak ada toast yang tampil
40. Verifikasi halaman me-refresh ke state belum ada draft: Dropzone tampil
41. Verifikasi Unsaved Banner tidak tampil

### TC-GS-IMPORT-666 varian 4: Double-submit Discard Draft

42. Seed draft D-01 di Client A lewat skrip fixture, mundurkan `created_at` draft 25 jam (D-76 varian 1), lalu muat ulang halaman Import > Brand
43. Klik `[Discard]` pada Unsaved Banner
44. Atur intercept jaringan agar respons permintaan `[Discard Draft]` ditunda
45. Klik `[Discard Draft]` dua kali berturut-turut dengan cepat
46. Verifikasi tombol `[Discard Draft]` tampil Disabled dengan indikator loading
47. Verifikasi intercept mencatat tepat satu permintaan
48. Lepaskan respons permintaan yang ditunda dan lepas intercept
49. Verifikasi tepat satu toast sukses: "Success, draft has been discarded."

### TC-GS-IMPORT-282: Discard Draft menghapus draft dan tidak menambah notifikasi (paling akhir)

50. Tunggu toast lama hilang otomatis; seed draft D-01 di Client A lewat skrip fixture, mundurkan `created_at` draft 25 jam (D-76 varian 1), lalu muat ulang halaman Import > Brand
51. Catat jumlah notifikasi pada lonceng
52. Klik `[Discard]` pada Unsaved Banner
53. Klik `[Discard Draft]`
54. Verifikasi muncul toast sukses: "Success, draft has been discarded."
55. Verifikasi halaman kembali ke state belum ada draft: Dropzone tampil
56. Verifikasi Unsaved Banner tidak tampil
57. Verifikasi jumlah notifikasi pada lonceng sama dengan sebelum Discard Draft

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fungsional; intercept pada TC-666 hanya menahan respons untuk mengamati loading dan jumlah permintaan (bukan kelas b); penghapus draft kedua hanya pemicu (P-2, sesi API); hook umur draft hanya pemicu Unsaved Banner.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan dari TC: TC-280, TC-281, dan TC-695 (hanya Cancel atau Esc) dijalankan pertama; TC-666 varian 1 sampai 3 sebelum varian 4; TC-284 dan TC-666 varian 4 serta TC-282 (menghapus draft) dijalankan paling akhir (prinsip 5 bagian 3).
- Langkah penghubung (tanpa `Verifikasi`): langkah 1 menyiapkan umur draft (D-76) karena `beforeEach` hanya memulihkan draft dasar Client A (K-7); langkah 15, 25, 33, 42, 50 membersihkan atau memulihkan state (Kontrak Fixture R2, S-09); langkah 36 menjalankan Langkah 2 sampai 4 TC-284 sebagai sesi API (P-2); intercept dilepas pada langkah 31 dan 48 segera setelah dipakai (S-09).
- Spec berisi 57 langkah bernomor dan sekitar 87 langkah dengan ekspansi. Alasan melewati sekitar 35 langkah: semua blok satu kelas (fungsional, dialog konfirmasi), parameter tiap iterasi ada di tabel Prerequisites tanpa langkah bersyarat (langkah 15 membaca kolom Pembersihan), tiap blok berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: TC-GS-IMPORT-258 sampai 260, 686 (Remove satu baris) ada di spec 108; TC-GS-IMPORT-264, 265, 267, 687 (Bulk Delete) ada di spec 110.
- Temuan untuk QA:
  - TC-GS-IMPORT-666 mencakup empat topik (Save, Remove, Bulk Delete, Discard Draft) dalam satu TC; varian 1 sampai 3 diulang pada spec ini dan varian 4 dikerjakan di akhir. Rumah TC ini di spec Save, Remove, Bulk Delete juga mungkin.
  - TC-GS-IMPORT-695 Langkah 5 menyatakan "Esc setara Cancel"; pada varian 4 dialog Unsaved Changes, Esc diasersi menutup dialog dan sesi edit tetap utuh sesuai Expected b.
  - TC-GS-IMPORT-666 tidak menyebut endpoint yang di-intercept; intercept dipasang pada permintaan yang dikirim tombol konfirmasi tanpa menulis endpoint karangan (S-13).
  - Post Condition semua TC ("Draft Brand dihapus permanen" pada TC-282) sudah diasersi pada Expected b.
