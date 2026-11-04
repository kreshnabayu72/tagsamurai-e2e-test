---
id: TC-FA-COA-E2E-077-multi-konteks-bulk-sebagian-dihapus-sesi-lain
title: "Multi-Konteks: Bulk Deactivate, Activate, dan Delete saat Sebagian Akun Terpilih Dihapus Sesi Lain, Akun Lain Tetap Diproses"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-COA-114
  - TC-FA-COA-171
  - TC-FA-COA-172
  - TC-FA-COA-353
coverage:
  web: automated
---

# Multi-Konteks: Bulk Deactivate, Activate, dan Delete saat Sebagian Akun Terpilih Dihapus Sesi Lain, Akun Lain Tetap Diproses

## Prerequisites

- Mode: FE+BE (backend nyata; tanpa intercept).
- Akun aktor sesi A: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Sesi API aktor: pelaku kedua (sesi B pada TC) hanya memicu penghapusan akun dan memakai sesi API sesuai butir "Sesi API aktor" di `suite.md`.
- Seed dan pemulihan lewat API: mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`.
- Flag Guided Tooltip halaman Chart of Accounts: di-set true oleh hook `before` suite (lihat `suite.md`).
- Data Pre-setup (akun Pre-setup sekali pakai, identitas di `Fixture.settingsChartOfAccounts.<kunci>` yang disediakan tim FE; nama kunci ditetapkan tim FE). Semua Used By 0 dan Last Used in Journal kosong:

  | Akun | Code dan Name | State awal | Diubah oleh | TC |
  |---|---|---|---|---|
  | P67 (`Fixture.settingsChartOfAccounts.p67`) | `5-6106` · `Depreciation Expense – Deleted Race Keep` · Function Depreciation Expense | Active | dinonaktifkan sesi A | TC-FA-COA-114 |
  | P68 (`Fixture.settingsChartOfAccounts.p68`) | `CAP-8107` · `Capitalization Clearing – Deleted Race` · Function Capitalization Offset | Active | dihapus sesi B | TC-FA-COA-114 |
  | P35 (`Fixture.settingsChartOfAccounts.p35`) | `CAP-7040` · `Capitalization Clearing – Bulk Activate A` · Function Capitalization Offset | Inactive | diaktifkan sesi A | TC-FA-COA-171 |
  | P36 (`Fixture.settingsChartOfAccounts.p36`) | `CAP-7050` · `Capitalization Clearing – Bulk Activate B` · Function Capitalization Offset | Inactive | dihapus sesi B | TC-FA-COA-171 |
  | P37 (`Fixture.settingsChartOfAccounts.p37`) | `CAP-7060` · `Capitalization Clearing – Bulk Delete A` · Function Capitalization Offset | Active, belum pernah diekspor, bukan nilai default company | dihapus sesi A | TC-FA-COA-172 |
  | P38 (`Fixture.settingsChartOfAccounts.p38`) | `CAP-7070` · `Capitalization Clearing – Bulk Delete B` · Function Capitalization Offset | Active, belum pernah diekspor, bukan nilai default company | dihapus sesi B | TC-FA-COA-172 |
  | P103 (`Fixture.settingsChartOfAccounts.p103`) | `CAP-8306` · `Capitalization Clearing – Deleted Race Delete A` · Function Capitalization Offset | Active, belum pernah diekspor, bukan nilai default company | dihapus sesi B | TC-FA-COA-353 |
  | P104 (`Fixture.settingsChartOfAccounts.p104`) | `CAP-8307` · `Capitalization Clearing – Deleted Race Delete B` · Function Capitalization Offset | Active, belum pernah diekspor, bukan nilai default company | dihapus sesi B | TC-FA-COA-353 |

- Pada TC-FA-COA-114 dua akun target berawalan Code berbeda sehingga dipilih lewat dua Search berurutan; spec mengasumsikan seleksi dipertahankan saat Search diganti (lihat Temuan untuk QA). Pada TC lain kedua akun dipilih setelah satu Search dengan awalan Code bersama (`CAP-70`, `CAP-830`) yang memuat kedua akun pada halaman pertama (asumsi: tidak lebih dari 10 baris).
- Efek pada Pre-setup (S-06): P67 menjadi Inactive, P35 menjadi Active; P68, P36, P37, P38, P103, P104 terhapus. Last Updated akun berubah.
- Pengecualian A-18 (lihat butir "Pengecualian A-18" di `suite.md`): P67, P68, P35, P36, P37, P38, P103, dan P104 adalah akun Pre-setup sekali pakai yang menjadi target hapus atau ubah status. Seed idempotent dan pemulihan akun ke state awal dijalankan di hook `before` dan `after` spec ini (disediakan tim FE/BE); satu akun dan satu Account Code literal (`5-6106`, `CAP-8107`, `CAP-7040`, `CAP-7050`, `CAP-7060`, `CAP-7070`, `CAP-8306`, `CAP-8307`) hanya dipakai spec ini.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): menghapus akun lewat sesi API; membaca jumlah entri log L-03 (Deactivate dan Activate) dan L-04 (Delete) atas akun tertentu.
- Suite berjalan serial (`parallel: false`): spec mengubah dan menghapus akun Pre-setup bersama.
- Env var yang dipakai: `FA_TC_PASSWORD` (terdaftar).

## Test Steps

### TC-FA-COA-114: Bulk Deactivate: salah satu akun terpilih sudah dihapus user lain saat Confirm dan akun lain tetap diproses

1. Ketik Search `Fixture.settingsChartOfAccounts.p67.code`, tekan Enter
2. Sesi A: centang akun P67 (`Fixture.settingsChartOfAccounts.p67.code`)
3. Ganti isi kotak search dengan `Fixture.settingsChartOfAccounts.p68.code`, tekan Enter
4. Sesi A: centang akun P68 (`Fixture.settingsChartOfAccounts.p68.code`)
5. Sesi A: klik Bulk `Deactivate` untuk membuka dialog `Deactivate Accounts` (D-02)
6. Hapus P68 lewat sesi API hingga penghapusan tersimpan
7. Catat baseline jumlah entri log L-03 atas P67 dan P68 (kemampuan baca disediakan tim FE/BE)
8. Sesi A: klik `[Deactivate]`
9. Verifikasi toast "Success, account has been deactivated." (T-05a) tampil
10. Verifikasi toast parsial T-05b tidak tampil
11. Verifikasi toast netral "This account is no longer available." (T-12) tidak tampil
12. Verifikasi tidak ada dialog blok
13. Verifikasi P68 dilewati tanpa log dan P67 tercatat: jumlah entri log L-03 atas P67 dan P68 bertambah tepat 1 dibanding baseline langkah 7 (entri milik P67)
14. Ganti isi kotak search dengan `Fixture.settingsChartOfAccounts.p67.code`, tekan Enter
15. Verifikasi switch Status P67 Inactive
16. Ganti isi kotak search dengan `Fixture.settingsChartOfAccounts.p68.code`, tekan Enter
17. Verifikasi P68 tidak tampil di tabel

### TC-FA-COA-171: Bulk Activate: sebagian akun terpilih sudah dihapus user lain dan akun lain diaktifkan menampilkan hanya toast sukses penuh (NC-10)

18. Ganti isi kotak search dengan `CAP-70`, tekan Enter
19. Sesi A: centang kedua akun P35 (`Fixture.settingsChartOfAccounts.p35.code`) dan P36 (`Fixture.settingsChartOfAccounts.p36.code`)
20. Sesi A: klik Bulk `Activate` untuk membuka dialog `Activate Accounts` (D-15)
21. Hapus P36 lewat sesi API hingga penghapusan tersimpan
22. Catat baseline jumlah entri log L-03 atas P35 dan P36
23. Sesi A: klik `[Activate]`
24. Verifikasi toast "Success, account has been activated." (T-04) tampil
25. Verifikasi toast netral "This account is no longer available." (T-12) tidak tampil
26. Verifikasi tidak ada toast parsial
27. Verifikasi P36 dilewati tanpa log dan P35 tercatat: jumlah entri log L-03 atas P35 dan P36 bertambah tepat 1 dibanding baseline langkah 22 (entri milik P35)
28. Verifikasi switch Status P35 Active
29. Verifikasi P36 tidak tampil di tabel

### TC-FA-COA-172: Bulk Delete: sebagian akun terpilih sudah dihapus user lain dan akun lain dihapus menampilkan hanya toast sukses penuh (NC-10)

30. Ganti isi kotak search dengan `CAP-70`, tekan Enter
31. Sesi A: centang kedua akun P37 (`Fixture.settingsChartOfAccounts.p37.code`) dan P38 (`Fixture.settingsChartOfAccounts.p38.code`)
32. Sesi A: klik Bulk `Delete` untuk membuka dialog `Delete Accounts` (D-08)
33. Hapus P38 lewat sesi API hingga penghapusan tersimpan
34. Catat baseline jumlah entri log L-04 atas P37 dan P38
35. Sesi A: klik `[Delete]`
36. Verifikasi toast "Success, account has been deleted." (T-06a) tampil
37. Verifikasi toast parsial T-06b tidak tampil
38. Verifikasi toast netral "This account is no longer available." (T-12) tidak tampil
39. Verifikasi P38 dilewati tanpa log dan P37 tercatat: jumlah entri log L-04 atas P37 dan P38 bertambah tepat 1 dibanding baseline langkah 34 (entri milik P37)
40. Verifikasi P37 dan P38 tidak tampil di tabel

### TC-FA-COA-353: Bulk Delete saat seluruh akun terpilih sudah dihapus user lain hanya menampilkan toast netral T-12 dan mereset seleksi

41. Ganti isi kotak search dengan `CAP-830`, tekan Enter
42. Sesi A: centang kedua akun P103 (`Fixture.settingsChartOfAccounts.p103.code`) dan P104 (`Fixture.settingsChartOfAccounts.p104.code`)
43. Sesi A: klik Bulk `Delete` untuk membuka dialog D-08
44. Hapus P103 dan P104 lewat sesi API hingga penghapusan tersimpan
45. Sesi A: klik `[Delete]`
46. Verifikasi toast netral "This account is no longer available." (severity Info) tampil
47. Verifikasi tidak ada toast "Success, account has been deleted."
48. Verifikasi tidak ada toast parsial
49. Verifikasi dialog konfirmasi menutup
50. Verifikasi tabel disegarkan tanpa kedua akun P103 dan P104
51. Verifikasi seleksi di-reset: Bulk Action Bar tidak tampil
52. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (kelas c, multi-konteks). Empat blok berdiri sendiri pada halaman dan tabel yang sama, satu kelas harness (bulk dengan sebagian atau seluruh akun terpilih sudah dihapus sesi lain).
- Spec berisi 52 langkah, melewati sekitar 35 langkah. Alasan: empat blok TC berdiri sendiri dengan akun sekali pakai masing-masing; tiap blok wajib memuat Search akun target (R-23), centang dua akun, pemicu sesi API, baseline log, dan Expected yang dipecah per klausa (S-01), sehingga langkah berulang per blok (butir 8b.7) dan tidak ada langkah yang dapat dihapus tanpa menghilangkan Expected TC.
- Pelaku kedua adalah sesi API yang hanya memicu state, bukan konteks kedua; tidak ada sesi UI kedua.
- `A-18`: TC-FA-COA-114, 171, 172, dan 353 memakai akun Pre-setup sekali pakai P67, P68, P35, P36, P37, P38, P103, dan P104 sebagai target ubah status atau hapus, dengan Account Code literal `5-6106`, `CAP-8107`, `CAP-7040`, `CAP-7050`, `CAP-7060`, `CAP-7070`, `CAP-8306`, dan `CAP-8307`; pemulihan di hook `before` dan `after`.
- Langkah penghubung (S-03, S-09): langkah 1, 3, 14, 16, 18, 30, dan 41 (Search untuk menemukan akun target, R-16, butir 8b.13) dan langkah 52 (mengosongkan Search); langkah 5, 20, 32, dan 43 membuka dialog bulk sesuai langkah TC; langkah 7, 22, dan 34 mencatat baseline log (S-12). Seleksi sesi A di-reset oleh aksi pada tiap blok sehingga blok berikutnya tidak mewarisi seleksi (S-09).
- Butir `P-1`: asersi "dilewati tanpa log" (langkah 13, 27, 39; Expected a TC-FA-COA-114, 171, 172) ditulis di spec asal dengan baseline karena bergantung pada state yang dibangun langkah sebelumnya (penghapusan oleh sesi API sesudah dialog dibuka) dan tidak ada spec absence yang memuat aksi nyata untuk TC itu (S-05).
- "Tabel disegarkan" pada TC-FA-COA-353 dan "setelah disegarkan" pada TC-FA-COA-114, 171, 172 tidak punya metode observasi di TC; spec mengasersi isi baris atau ketiadaannya setelah toast sebagai anchor (butir 8b.2).
- Post Condition TC-FA-COA-353 ("tidak ada entri log tambahan dari sesi A") tidak punya langkah observasi dan tidak diasersi (S-01).
- Temuan untuk QA:
  - TC-FA-COA-114, 171, 172 Expected a ("dilewati tanpa log", "log L-03/L-04 hanya untuk P67/P35/P37") tidak menyebut surface log; spec memakai selisih jumlah entri log L-03 atau L-04 atas kedua akun lewat kemampuan baca yang disediakan tim FE/BE sebagai asumsi. Selisih 1 mengasumsikan satu entri per akun yang diproses.
  - TC-FA-COA-114 memilih dua akun berawalan Code berbeda (`5-6106` dan `CAP-8107`) yang tidak dapat berada pada satu hasil Search; spec memakai dua Search berurutan dan mengasumsikan seleksi P67 dipertahankan saat Search diganti (TC tidak menyatakan perilaku seleksi). Tanpa asumsi itu TC tidak dapat dieksekusi pada tabel dengan lebih dari satu halaman.
  - TC-FA-COA-114 Expected a dan b dipecah menjadi `Verifikasi` per klausa (toast sukses, absence toast parsial dan netral, log, switch P67, absence P68).
  - TC tidak menyebut kolom yang dicari Search; spec mencari berdasarkan Account Code.
