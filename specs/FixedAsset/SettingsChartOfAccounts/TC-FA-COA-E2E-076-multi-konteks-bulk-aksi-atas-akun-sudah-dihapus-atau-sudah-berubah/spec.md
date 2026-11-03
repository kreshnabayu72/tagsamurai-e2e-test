---
id: TC-FA-COA-E2E-076-multi-konteks-bulk-aksi-atas-akun-sudah-dihapus-atau-sudah-berubah
title: "Multi-Konteks: Bulk Activate dan Deactivate saat Seluruh Akun Terpilih Sudah Dihapus atau Sudah Berstatus Target oleh Sesi Lain"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-COA-149
  - TC-FA-COA-152
  - TC-FA-COA-351
  - TC-FA-COA-352
coverage:
  web: automated
---

# Multi-Konteks: Bulk Activate dan Deactivate saat Seluruh Akun Terpilih Sudah Dihapus atau Sudah Berstatus Target oleh Sesi Lain

## Prerequisites

- Mode: FE+BE (backend nyata; tanpa intercept).
- Akun aktor sesi A: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Sesi API aktor: pelaku kedua (sesi B pada TC) hanya memicu perubahan state (hapus, aktifkan, nonaktifkan) dan memakai sesi API sesuai butir "Sesi API aktor" di `suite.md`.
- Seed dan pemulihan lewat API: mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`.
- Flag Guided Tooltip halaman Chart of Accounts: di-set true oleh hook `before` suite (lihat `suite.md`).
- Data Pre-setup (akun sekali pakai milik spec, identitas di `Fixture.settings-chart-of-accounts` yang disediakan tim FE; nama kunci ditetapkan tim FE). Semua Used By 0:

  | Akun | Code dan Name | Status awal | Diubah oleh sesi B | TC |
  |---|---|---|---|---|
  | P19 | `CAP-6600` · `Capitalization Clearing – Spare D` dan `CAP-6610` · `Capitalization Clearing – Spare E` (Function Capitalization Offset) | Active | keduanya dihapus | TC-FA-COA-149 |
  | P22 | `CAP-6730` · `Capitalization Clearing – Spare H` dan `CAP-6740` · `Capitalization Clearing – Spare I` (Function Capitalization Offset) | Inactive | keduanya diaktifkan | TC-FA-COA-152 |
  | P99 dan P100 | `5-6111` · `Depreciation Expense – Stale Deactivate A` dan `5-6112` · `Depreciation Expense – Stale Deactivate B` (Function Depreciation Expense) | Active | keduanya dinonaktifkan | TC-FA-COA-351 |
  | P101 dan P102 | `4-7111` · `Gain on Disposal – Deleted Race Activate A` dan `4-7112` · `Gain on Disposal – Deleted Race Activate B` (Function Gain on Disposal) | Inactive | keduanya dihapus | TC-FA-COA-352 |

- Search pada langkah 1, 10, 19, dan 29 memakai awalan Account Code (`CAP-66`, `CAP-67`, `5-611`, `4-711`) supaya kedua akun target berada pada halaman pertama hasil (asumsi: hasil tiap awalan tidak lebih dari 10 baris; lihat Temuan untuk QA). Seleksi dilakukan pada dua baris itu dengan nama persis.
- Efek pada Pre-setup (S-06): P19, P101, P102 terhapus; P22 menjadi Active; P99 dan P100 menjadi Inactive. Hook `before` dan `after` mengembalikan akun ke state awal lewat seeding (disediakan tim FE/BE). Last Updated akun berubah.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): menghapus, mengaktifkan, dan menonaktifkan akun lewat sesi API.
- Suite berjalan serial (`parallel: false`): spec mengubah dan menghapus akun Pre-setup bersama.
- Env var yang dipakai: `FA_TC_PASSWORD` (terdaftar).

## Test Steps

### TC-FA-COA-149: Bulk Deactivate saat seluruh akun terpilih sudah dihapus user lain hanya menampilkan toast netral T-12

1. Ketik Search `CAP-66`, tekan Enter
2. Sesi A: centang kedua akun P19 (`CAP-6600` dan `CAP-6610`)
3. Sesi A: klik Bulk `Deactivate` untuk membuka dialog `Deactivate Accounts` (D-02)
4. Hapus kedua akun P19 lewat sesi API hingga penghapusan tersimpan
5. Sesi A: klik `[Deactivate]`
6. Verifikasi toast netral "This account is no longer available." (severity Info) tampil
7. Verifikasi tidak ada toast "Success, account has been deactivated." dan tidak ada toast parsial
8. Verifikasi tabel disegarkan tanpa kedua akun P19
9. Verifikasi seleksi di-reset: Bulk Action Bar tidak tampil

### TC-FA-COA-152: Bulk Activate saat setiap akun terpilih sudah Active oleh user lain hanya menampilkan toast netral T-03

10. Ganti isi kotak search dengan `CAP-67`, tekan Enter
11. Sesi A: centang kedua akun P22 (`CAP-6730` dan `CAP-6740`)
12. Sesi A: klik Bulk `Activate` untuk membuka dialog `Activate Accounts` (D-15)
13. Aktifkan kedua akun P22 lewat sesi API hingga status Active tersimpan
14. Sesi A: klik `[Activate]`
15. Verifikasi toast netral "No changes to save." (severity Info) tampil
16. Verifikasi tidak ada toast "Success, account has been activated."
17. Verifikasi seleksi di-reset: Bulk Action Bar tidak tampil
18. Verifikasi baris kedua akun P22 disegarkan: switch Status Active

### TC-FA-COA-351: Bulk Deactivate saat seluruh akun terpilih sudah Inactive (data usang) hanya menampilkan toast netral T-03 dan mereset seleksi

19. Ganti isi kotak search dengan `5-611`, tekan Enter
20. Sesi A: centang P99 (`5-6111`) dan P100 (`5-6112`)
21. Sesi A: klik Bulk `Deactivate` untuk membuka dialog D-02
22. Nonaktifkan P99 dan P100 lewat sesi API hingga status Inactive tersimpan
23. Sesi A: klik `[Deactivate]`
24. Verifikasi toast netral "No changes to save." (T-03, severity Info) tampil
25. Verifikasi tidak ada toast "Success, account has been deactivated."
26. Verifikasi dialog konfirmasi menutup
27. Verifikasi tabel disegarkan: P99 dan P100 tampil Inactive
28. Verifikasi seleksi di-reset: Bulk Action Bar tidak tampil

### TC-FA-COA-352: Bulk Activate saat seluruh akun terpilih sudah dihapus user lain hanya menampilkan toast netral T-12 dan mereset seleksi

29. Ganti isi kotak search dengan `4-711`, tekan Enter
30. Sesi A: centang P101 (`4-7111`) dan P102 (`4-7112`)
31. Sesi A: klik Bulk `Activate` untuk membuka dialog D-15
32. Hapus P101 dan P102 lewat sesi API hingga penghapusan tersimpan
33. Sesi A: klik `[Activate]`
34. Verifikasi toast netral "This account is no longer available." (severity Info) tampil
35. Verifikasi tidak ada toast "Success, account has been activated." dan tidak ada toast parsial
36. Verifikasi dialog konfirmasi menutup
37. Verifikasi tabel disegarkan tanpa kedua akun P101 dan P102
38. Verifikasi seleksi di-reset: Bulk Action Bar tidak tampil
39. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (kelas c, multi-konteks). Empat blok berdiri sendiri pada halaman dan tabel yang sama, satu kelas harness (bulk atas akun yang berubah oleh sesi lain).
- Spec berisi 39 langkah, melewati sekitar 35 langkah. Alasan: empat blok TC berdiri sendiri dengan akun sekali pakai masing-masing; tiap blok wajib memuat Search akun target (R-23), centang dua akun, pemicu sesi API, dan Expected yang dipecah per klausa (S-01), sehingga langkah berulang per blok (butir 8b.7) dan tidak ada langkah yang dapat dihapus tanpa menghilangkan Expected TC.
- Pelaku kedua adalah sesi API yang hanya memicu state, bukan konteks kedua; tidak ada sesi UI kedua.
- Langkah penghubung (S-03, S-09): langkah 1, 10, 19, dan 29 (Search awalan Account Code agar kedua akun target tampil, R-16, butir 8b.12) dan langkah 39 (mengosongkan Search); langkah 3, 12, 21, dan 31 membuka dialog bulk sesuai langkah TC. Seleksi sesi A di-reset oleh aksi pada tiap blok sehingga blok berikutnya tidak mewarisi seleksi (S-09).
- "Tabel disegarkan" pada TC-FA-COA-149, 351, dan 352 tidak punya metode observasi di TC; spec mengasersi isi baris atau ketiadaannya setelah toast sebagai anchor (butir 8b.2).
- Post Condition "tidak ada entri log tambahan/dari aksi di sesi A" (TC-FA-COA-149, 152, 351, 352) tidak punya langkah observasi di TC dan tidak diasersi (S-01); dicatat di Temuan untuk QA.
- Temuan untuk QA:
  - TC-FA-COA-149, 152, 351, 352 menulis Post Condition tanpa surface log dan tanpa langkah observasi; tidak diasersi di spec ini.
  - TC menyebut dua akun target (mis. `CAP-6600` dan `CAP-6610`) tanpa menyatakan kolom yang dicari Search maupun jumlah baris awalan; spec mencari berdasarkan awalan Account Code dan mengasumsikan kedua akun berada pada halaman pertama hasil. Jika hasil awalan melebihi 10 baris atau akun lain berawalan sama, langkah Search perlu diganti dengan Search per akun.
  - TC-FA-COA-351 Expected c ("Dialog konfirmasi menutup dan tabel disegarkan: P99 dan P100 tampil Inactive") dan TC-FA-COA-352 Expected c dipecah menjadi `Verifikasi` dialog dan `Verifikasi` tabel.
