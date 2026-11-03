---
id: TC-FA-COA-E2E-074-multi-konteks-aksi-single-atas-akun-yang-berubah-oleh-sesi-lain
title: "Multi-Konteks: Aksi Single (Save Edit, Activate, Deactivate) atas Akun yang Dihapus atau Sudah Berubah Status oleh Sesi Lain"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-COA-146
  - TC-FA-COA-147
  - TC-FA-COA-148
  - TC-FA-COA-150
  - TC-FA-COA-151
coverage:
  web: automated
---

# Multi-Konteks: Aksi Single (Save Edit, Activate, Deactivate) atas Akun yang Dihapus atau Sudah Berubah Status oleh Sesi Lain

## Prerequisites

- Mode: FE+BE (backend nyata; tanpa intercept).
- Akun aktor sesi A: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Sesi API aktor: pelaku kedua (sesi B pada TC) hanya memicu perubahan state (hapus, aktifkan, nonaktifkan) dan memakai sesi API sesuai butir "Sesi API aktor" di `suite.md`.
- Seed dan pemulihan lewat API: mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`.
- Flag Guided Tooltip halaman Chart of Accounts: di-set true oleh hook `before` suite (lihat `suite.md`).
- Data Pre-setup (akun sekali pakai milik spec, identitas di `Fixture.settings-chart-of-accounts` yang disediakan tim FE; nama kunci ditetapkan tim FE). Semua Used By 0 dan Last Used in Journal kosong, Function Capitalization Offset:

  | Akun | Code dan Name | Status awal | Diubah oleh sesi B | TC |
  |---|---|---|---|---|
  | P16 | `CAP-6300` · `Capitalization Clearing – Spare A` | Active | dihapus | TC-FA-COA-146 |
  | P17 | `CAP-6400` · `Capitalization Clearing – Spare B` | Inactive | dihapus | TC-FA-COA-147 |
  | P18 | `CAP-6500` · `Capitalization Clearing – Spare C` | Active | dihapus | TC-FA-COA-148 |
  | P20 | `CAP-6710` · `Capitalization Clearing – Spare F` | Inactive | diaktifkan | TC-FA-COA-150 |
  | P21 | `CAP-6720` · `Capitalization Clearing – Spare G` | Active | dinonaktifkan | TC-FA-COA-151 |

- Efek pada Pre-setup (S-06): P16, P17, P18 terhapus; P20 dan P21 berganti status; hook `before` dan `after` mengembalikan kelima akun ke state awal lewat seeding (disediakan tim FE/BE). Last Updated akun berubah.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): menghapus, mengaktifkan, dan menonaktifkan akun lewat sesi API.
- Suite berjalan serial (`parallel: false`): spec mengubah dan menghapus akun Pre-setup bersama.
- Env var yang dipakai: `FA_TC_PASSWORD` (terdaftar).

## Test Steps

### TC-FA-COA-146: Save Edit pada akun yang sudah dihapus user lain menampilkan toast netral T-12

1. Ketik Search `CAP-6300`, tekan Enter
2. Sesi A: klik row action `Edit` pada akun P16
3. Sesi A: ubah Account Name P16 menjadi `Capitalization Clearing – Spare A Revised`
4. Hapus P16 lewat sesi API hingga penghapusan tersimpan
5. Sesi A: klik `[Save]`
6. Verifikasi toast netral "This account is no longer available." (severity Info) tampil
7. Verifikasi tidak ada toast "Success, account has been updated." dan tidak ada dialog blok
8. Verifikasi modal Edit Account tertutup
9. Verifikasi tabel disegarkan tidak memuat P16

### TC-FA-COA-147: Activate single pada akun yang sudah dihapus user lain menampilkan toast netral T-12

10. Ganti isi kotak search dengan `CAP-6400`, tekan Enter
11. Sesi A: klik switch Status akun P17 untuk membuka dialog `Activate Account` (D-14)
12. Hapus P17 lewat sesi API hingga penghapusan tersimpan
13. Sesi A: klik `[Activate]`
14. Verifikasi toast netral "This account is no longer available." (severity Info) tampil
15. Verifikasi tidak ada toast "Success, account has been activated."
16. Verifikasi dialog `Activate Account` tertutup
17. Verifikasi tabel disegarkan tanpa P17

### TC-FA-COA-148: Deactivate single pada akun yang sudah dihapus user lain menampilkan toast netral T-12

18. Ganti isi kotak search dengan `CAP-6500`, tekan Enter
19. Sesi A: klik switch Status akun P18 untuk membuka dialog `Deactivate Account` (D-01)
20. Hapus P18 lewat sesi API hingga penghapusan tersimpan
21. Sesi A: klik `[Deactivate]`
22. Verifikasi toast netral "This account is no longer available." (severity Info) tampil
23. Verifikasi tidak ada toast "Success, account has been deactivated." dan tidak ada dialog blok
24. Verifikasi dialog `Deactivate Account` tertutup
25. Verifikasi tabel disegarkan tanpa P18

### TC-FA-COA-150: Activate single pada akun yang sudah Active oleh user lain: idempotent dengan toast netral T-03

26. Ganti isi kotak search dengan `CAP-6710`, tekan Enter
27. Sesi A: klik switch Status akun P20 untuk membuka dialog `Activate Account` (D-14)
28. Aktifkan P20 lewat sesi API hingga status Active tersimpan
29. Sesi A: klik `[Activate]`
30. Verifikasi toast netral "No changes to save." (severity Info) tampil
31. Verifikasi tidak ada toast "Success, account has been activated."
32. Verifikasi dialog `Activate Account` tertutup
33. Verifikasi baris P20 disegarkan: switch Status Active

### TC-FA-COA-151: Deactivate single pada akun yang sudah Inactive oleh user lain: idempotent dengan toast netral T-03

34. Ganti isi kotak search dengan `CAP-6720`, tekan Enter
35. Sesi A: klik switch Status akun P21 untuk membuka dialog `Deactivate Account` (D-01)
36. Nonaktifkan P21 lewat sesi API hingga status Inactive tersimpan
37. Sesi A: klik `[Deactivate]`
38. Verifikasi toast netral "No changes to save." (severity Info) tampil
39. Verifikasi tidak ada toast "Success, account has been deactivated."
40. Verifikasi dialog `Deactivate Account` tertutup
41. Verifikasi baris P21 disegarkan: switch Status Inactive
42. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (kelas c, multi-konteks). Lima blok berdiri sendiri pada halaman dan tabel yang sama, satu kelas harness (aksi single atas akun yang berubah oleh sesi lain); kegagalan satu blok tidak menghilangkan makna blok lain.
- Spec berisi 42 langkah, melewati sekitar 35 langkah. Alasan: lima blok TC berdiri sendiri dengan akun sekali pakai masing-masing; tiap blok wajib memuat Search akun target (R-23), pemicu sesi API, dan Expected yang dipecah per klausa (S-01), sehingga langkah berulang per blok (butir 8b.7) dan tidak ada langkah yang dapat dihapus tanpa menghilangkan Expected TC.
- Pelaku kedua (sesi B) adalah sesi API yang hanya memicu state, bukan konteks kedua; tidak ada sesi UI kedua.
- Langkah penghubung (S-03, S-09): langkah 1, 10, 18, 26, dan 34 (Search untuk menemukan akun target, R-16, butir 8b.12) dan langkah 42 (mengosongkan Search sebelum spec berikutnya). Langkah 11, 19, 27, dan 35 membuka dialog konfirmasi sesuai langkah TC.
- Asersi absence "tidak ada toast ..." (langkah 7, 15, 23, 31, 39) didahului toast netral sebagai anchor positif (butir 8b.2 dan 8b.11); absence baris P16, P17, P18 (langkah 9, 17, 25) memakai toast netral sebagai anchor.
- Post Condition "tidak ada entri log dari Save/aksi di sesi A" (TC-FA-COA-146, 147, 148, 150, 151) tidak punya langkah observasi di TC dan tidak diasersi (S-01) dan dicatat di Temuan untuk QA.
- Temuan untuk QA:
  - TC-FA-COA-146 sampai 151 menulis Post Condition "tidak ada entri log" tanpa surface dan tanpa langkah observasi; tidak diasersi di spec ini.
  - Pada TC-FA-COA-147 dan 148 Expected b menulis "Dialog tertutup dan tabel disegarkan" sebagai satu butir; spec memecahnya menjadi dua `Verifikasi`. TC-FA-COA-146, 147, 148 tidak memberi metode observasi "Tabel disegarkan"; spec mengasersi baris tidak ada pada hasil Search.
  - TC tidak menyebut kolom yang dicari Search; spec mencari berdasarkan Account Code.
