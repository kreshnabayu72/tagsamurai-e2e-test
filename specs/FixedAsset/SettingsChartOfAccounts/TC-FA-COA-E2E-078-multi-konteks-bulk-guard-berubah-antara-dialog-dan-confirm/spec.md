---
id: TC-FA-COA-E2E-078-multi-konteks-bulk-guard-berubah-antara-dialog-dan-confirm
title: "Multi-Konteks: Bulk Deactivate dan Bulk Delete saat Guard Berubah antara Dialog Dibuka dan Confirm (Dipakai Asset Class atau Diekspor)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-COA-346
  - TC-FA-COA-347
  - TC-FA-COA-348
coverage:
  web: automated
---

# Multi-Konteks: Bulk Deactivate dan Bulk Delete saat Guard Berubah antara Dialog Dibuka dan Confirm (Dipakai Asset Class atau Diekspor)

## Prerequisites

- Mode: FE+BE (backend nyata; tanpa intercept).
- Akun aktor sesi A: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Sesi API aktor: pelaku kedua (sesi B pada TC) hanya memicu perubahan state (ekspor akun, membuat Asset Class pemakai akun) dan memakai sesi API sesuai butir "Sesi API aktor" di `suite.md`.
- Seed dan pemulihan lewat API: mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; jalur ekspor Journal J-06 dan pembuatan Asset Class yang memakai akun sebagai Depreciation Expense disediakan tim FE/BE tanpa endpoint karangan.
- Flag Guided Tooltip halaman Chart of Accounts: di-set true oleh hook `before` suite (lihat `suite.md`).
- Data Pre-setup (akun sekali pakai milik spec, identitas di `Fixture.settings-chart-of-accounts` yang disediakan tim FE; nama kunci ditetapkan tim FE). Semua Active, Used By 0, Last Used in Journal kosong; akun yang akan dihapus belum pernah diekspor dan bukan nilai default company:

  | Akun | Code dan Name | Diubah oleh sesi B | TC |
  |---|---|---|---|
  | P90 | `5-6108` · `Depreciation Expense – Bulk Deactivate Race Used` · Function Depreciation Expense | dipakai Asset Class baru (Used By 1) | TC-FA-COA-346 |
  | P91 | `5-6109` · `Depreciation Expense – Bulk Deactivate Race Eligible` · Function Depreciation Expense | tidak diubah | TC-FA-COA-346 |
  | P92 | `CAP-8301` · `Capitalization Clearing – Bulk Delete Race Export` · Function Capitalization Offset | diekspor lewat J-06 | TC-FA-COA-347 |
  | P93 | `CAP-8302` · `Capitalization Clearing – Bulk Delete Race Eligible` · Function Capitalization Offset | tidak diubah | TC-FA-COA-347 |
  | P94 | `CAP-8303` · `Capitalization Clearing – Bulk Delete Race All Export` · Function Capitalization Offset | diekspor lewat J-06 | TC-FA-COA-348 |
  | P95 | `5-6115` · `Depreciation Expense – Bulk Delete Race All Used` · Function Depreciation Expense | dipakai Asset Class baru (Used By 1) | TC-FA-COA-348 |

- Data Dinamis: Asset Class pemakai P90 dan P95 (dibuat sesi API pada langkah 4 dan 30; Name memuat suffix `{runId}-078`, dihapus di hook `after`; disediakan tim FE).
- Pada TC-FA-COA-346 dan 347 kedua akun target dipilih setelah satu Search dengan awalan Code bersama (`5-610`, `CAP-830`) yang memuat kedua akun pada halaman pertama (asumsi: tidak lebih dari 10 baris). Pada TC-FA-COA-348 kedua akun berawalan Code berbeda sehingga dipilih lewat dua Search berurutan dan spec mengasumsikan seleksi dipertahankan saat Search diganti (lihat Temuan untuk QA).
- Efek pada Pre-setup (S-06): P90 dan P95 terpakai satu Asset Class sampai hook `after` menghapusnya; P91 menjadi Inactive; P93 terhapus; P92 dan P94 terisi Last Used in Journal. Hook `before` dan `after` mengembalikan akun ke state awal lewat seeding (disediakan tim FE/BE). Last Updated akun berubah.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): ekspor akun lewat jalur J-06; membuat dan menghapus Asset Class pemakai akun; membaca jumlah entri log L-03 (Deactivate) dan L-04 (Delete) atas akun tertentu.
- Suite berjalan serial (`parallel: false`): spec mengubah akun Pre-setup bersama dan memakai Used By.
- Env var yang dipakai: `FA_TC_PASSWORD` (terdaftar).

## Test Steps

### TC-FA-COA-346: Bulk Deactivate: salah satu akun menjadi dipakai Asset Class antara dialog dibuka dan Confirm: akun itu dilewati dan toast parsial tampil tanpa dialog blok

1. Ketik Search `5-610`, tekan Enter
2. Sesi A: centang kedua akun P90 (`5-6108`) dan P91 (`5-6109`)
3. Sesi A: klik Bulk `Deactivate` untuk membuka dialog D-02
4. Buat Asset Class baru dengan P90 sebagai Depreciation Expense lewat sesi API hingga tersimpan (Used By P90 menjadi 1)
5. Catat baseline jumlah entri log L-03 atas P90 dan P91 (kemampuan baca disediakan tim FE/BE)
6. Sesi A: klik `[Deactivate]`
7. Verifikasi toast parsial "Success, account has been deactivated. Some items were skipped (still in use)." (T-05b) tampil
8. Verifikasi tidak ada dialog blok
9. Verifikasi P90 dilewati tanpa log dan P91 tercatat: jumlah entri log L-03 atas P90 dan P91 bertambah tepat 1 dibanding baseline langkah 5 (entri milik P91)
10. Verifikasi setelah tabel disegarkan, P91 Inactive
11. Verifikasi P90 tetap Active
12. Verifikasi seleksi di-reset: Bulk Action Bar tidak tampil

### TC-FA-COA-347: Bulk Delete: salah satu akun menjadi diekspor antara dialog dibuka dan Confirm: akun itu dilewati dan toast parsial tampil tanpa dialog blok

13. Ganti isi kotak search dengan `CAP-830`, tekan Enter
14. Sesi A: centang kedua akun P92 (`CAP-8301`) dan P93 (`CAP-8302`)
15. Sesi A: klik Bulk `Delete` untuk membuka dialog D-08
16. Ekspor P92 melalui jalur API J-06 lewat sesi API hingga Last Used in Journal P92 tersimpan
17. Catat baseline jumlah entri log L-04 atas P92 dan P93
18. Sesi A: klik `[Delete]`
19. Verifikasi toast parsial "Success, account has been deleted. Some items were skipped (still in use, used in a journal, or default company)." (T-06b) tampil
20. Verifikasi tidak ada dialog blok
21. Verifikasi P92 dilewati tanpa log dan P93 tercatat: jumlah entri log L-04 atas P92 dan P93 bertambah tepat 1 dibanding baseline langkah 17 (entri milik P93)
22. Verifikasi setelah tabel disegarkan, P93 hilang dari tabel
23. Verifikasi P92 tetap tampil di tabel
24. Verifikasi seleksi di-reset: Bulk Action Bar tidak tampil

### TC-FA-COA-348: Bulk Delete: seluruh akun terpilih ditolak pada cek ulang saat Confirm: Dialog Blok memuat semua akun, tanpa perubahan data, seleksi dipertahankan

25. Ganti isi kotak search dengan `CAP-8303`, tekan Enter
26. Sesi A: centang akun P94 (`CAP-8303`)
27. Ganti isi kotak search dengan `5-6115`, tekan Enter
28. Sesi A: centang akun P95 (`5-6115`)
29. Sesi A: klik Bulk `Delete` untuk membuka dialog D-08
30. Ekspor P94 melalui jalur API J-06 lewat sesi API hingga Last Used in Journal P94 tersimpan, lalu buat Asset Class baru dengan P95 sebagai Depreciation Expense lewat sesi API hingga tersimpan
31. Sesi A: klik `[Delete]`
32. Verifikasi dialog blok `Cannot Delete Accounts` (D-12) tampil
33. Verifikasi tidak ada toast tambahan
34. Verifikasi teks "The following were last used in a journal and cannot be deleted:" memuat `• CAP-8303 – Capitalization Clearing – Bulk Delete Race All Export`
35. Verifikasi teks "The following are in use and cannot be deleted:" memuat `• 5-6115 – Depreciation Expense – Bulk Delete Race All Used`
36. Verifikasi tombol `[OK]` tampil pada dialog
37. Klik `[OK]`
38. Verifikasi seleksi P95 dipertahankan (checkbox P95 tercentang pada hasil Search `5-6115`)
39. Ganti isi kotak search dengan `CAP-8303`, tekan Enter
40. Verifikasi seleksi P94 dipertahankan (checkbox P94 tercentang)
41. Verifikasi Bulk Action Bar tetap tampil
42. Klik `Unselect All` pada Bulk Action Bar
43. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (kelas c, multi-konteks). Tiga blok berdiri sendiri pada halaman dan tabel yang sama, satu kelas harness (guard akun berubah antara dialog dibuka dan Confirm pada aksi bulk).
- Spec berisi 43 langkah, melewati sekitar 35 langkah. Alasan: tiga blok TC berdiri sendiri dengan akun sekali pakai masing-masing; tiap blok wajib memuat Search akun target (R-23), centang dua akun, pemicu sesi API, dan Expected yang dipecah per klausa (S-01); TC-FA-COA-348 memuat dialog blok berisi dua daftar sehingga ada lima `Verifikasi` dialog dan tiga `Verifikasi` seleksi. Langkah berulang per blok (butir 8b.7); tidak ada langkah yang dapat dihapus tanpa menghilangkan Expected TC.
- Pelaku kedua adalah sesi API yang hanya memicu state, bukan konteks kedua; tidak ada sesi UI kedua.
- Langkah penghubung (S-03, S-09): langkah 1, 13, 25, 27, dan 39 (Search untuk menemukan akun target, R-16, butir 8b.12); langkah 43 (mengosongkan Search) dan 42 (membersihkan seleksi dari TC-FA-COA-348); langkah 3, 15, dan 29 membuka dialog bulk sesuai langkah TC; langkah 5 dan 17 mencatat baseline log (S-12); langkah 37 menutup dialog blok sesuai langkah 5 TC-FA-COA-348. Seleksi di-reset oleh aksi pada TC-FA-COA-346 dan 347 sehingga blok berikutnya tidak mewarisi seleksi.
- Butir `P-1`: asersi "dilewati tanpa log" (langkah 9 dan 21; Expected a TC-FA-COA-346 dan 347) ditulis di spec asal dengan baseline karena bergantung pada state yang dibangun langkah sebelumnya (perubahan guard oleh sesi API sesudah dialog dibuka) dan tidak ada spec absence yang memuat aksi nyata untuk TC itu (S-05).
- Post Condition TC-FA-COA-348 ("tidak ada data berubah dan tidak ada log untuk P94 dan P95") tidak punya langkah observasi di TC dan tidak diasersi (S-01).
- Temuan untuk QA:
  - TC-FA-COA-346 dan 347 Expected a tidak menyebut surface log; spec memakai selisih jumlah entri log L-03 atau L-04 atas kedua akun lewat kemampuan baca yang disediakan tim FE/BE sebagai asumsi (satu entri per akun yang diproses).
  - TC-FA-COA-348 memilih dua akun berawalan Code berbeda (`CAP-8303` dan `5-6115`) yang tidak dapat berada pada satu hasil Search; spec memakai dua Search berurutan dan mengasumsikan seleksi dipertahankan saat Search diganti (TC tidak menyatakan perilaku seleksi). Expected d "seleksi P94 dan P95 dipertahankan" tidak menyebut metode observasi; spec memakai status checkbox per baris dan Bulk Action Bar.
  - TC-FA-COA-348 langkah 3 menyebut ekspor P94 dan pemilihan P95 pada Asset Class baru oleh sesi B sebagai satu langkah; spec memicu keduanya lewat sesi API pada langkah 30.
  - TC tidak menyebut kolom yang dicari Search; spec mencari berdasarkan Account Code.
