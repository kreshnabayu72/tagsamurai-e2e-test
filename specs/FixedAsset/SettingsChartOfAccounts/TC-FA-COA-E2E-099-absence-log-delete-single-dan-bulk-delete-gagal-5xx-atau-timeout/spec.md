---
id: TC-FA-COA-E2E-099-absence-log-delete-single-dan-bulk-delete-gagal-5xx-atau-timeout
title: "Absence Log: Delete Single dan Bulk Delete Gagal 5xx atau Timeout Tidak Menulis Log"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-COA-65
  - TC-FA-COA-305
  - TC-FA-COA-71
coverage:
  web: automated
---

# Absence Log: Delete Single dan Bulk Delete Gagal 5xx atau Timeout Tidak Menulis Log

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; respons Delete dipaksa lewat `Spectra.intercept()`, jumlah entri log dibaca dari backend nyata).
- Kelas harness g (asersi absence log). Pemicu adalah kegagalan 5xx atau timeout yang dipaksa (kelas b) dan hanya membentuk kondisi yang diasersi tidak tercatat, bukan objek uji (P-5). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` sudah terdaftar.
- Data milik spec (di-seed hook `before` lewat API, dihapus hook `before` dan `after`; kemampuan seed disediakan tim FE/BE):
  - Akun A: Code `DID099A`, Account Name `Akun Hapus A {runId}-099`, Function Gain on Disposal, Inactive, Used By 0, Last Used in Journal kosong (padanan P3 pada TC-FA-COA-65, 305, dan 71).
  - Akun B: Code `DID099B`, Account Name `Akun Hapus B {runId}-099`, Function Gain on Disposal, Inactive, Used By 0, Last Used in Journal kosong (padanan P5 pada TC-FA-COA-71, eligible untuk Delete).
  - Account Code dibatasi 15 karakter sehingga tidak dapat bersuffix `{runId}`; Code literal `DID099A` dan `DID099B` memuat nomor spec supaya unik per spec dan dibersihkan di hook `before` dan `after` (R-13).
- Kebutuhan intercept (kelas b; `Spectra.intercept()`, tanpa endpoint karangan): TC-FA-COA-65 respons Delete single dipaksa 5xx; TC-FA-COA-305 respons Delete single tidak diberikan (timeout); TC-FA-COA-71 respons Bulk Delete dipaksa 5xx. Intercept dilepas segera setelah pemicu diasersi dan dipulihkan di hook `after` bila spec gagal di tengah.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): kemampuan membaca dari server jumlah entri Changelog (per Account Code), System Log milik user aktor (Detail User > Tab System Log, kolom Name), dan Activity Log FAMS (kolom Name) untuk objek Chart of Accounts per Account Code, dibaca sebagai baseline sebelum aksi pemicu tiap TC (S-12).
- Seed dan pemulihan mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`.

## Test Steps

### TC-FA-COA-65: Delete single gagal 5xx

1. Catat baseline jumlah entri Account Code `DID099A` pada Changelog, System Log aktor, dan Activity Log dari server
2. Ketik Search `{runId}-099`, tekan Enter
3. Klik row action `Delete` pada baris akun `DID099A` sehingga dialog Delete (D-07) terbuka
4. Paksa respons Delete menjadi 5xx lewat intercept jaringan
5. Klik `[Delete]` pada dialog D-07
6. Verifikasi toast `Error, failed to delete account.` tampil
7. Lepas intercept respons Delete
8. Klik `[Cancel]` pada dialog D-07
9. Verifikasi jumlah entri `DID099A` pada Changelog sama dengan baseline langkah 1
10. Verifikasi jumlah entri `DID099A` pada System Log aktor sama dengan baseline langkah 1
11. Verifikasi jumlah entri `DID099A` pada Activity Log sama dengan baseline langkah 1

### TC-FA-COA-305: Timeout saat Delete single

12. Catat baseline jumlah entri Account Code `DID099A` pada Changelog, System Log aktor, dan Activity Log dari server
13. Klik row action `Delete` pada baris akun `DID099A` sehingga dialog D-07 terbuka
14. Putus respons Delete lewat intercept jaringan (tidak ada respons)
15. Klik `[Delete]` pada dialog D-07
16. Verifikasi toast `Connection problem. Please try again.` tampil
17. Lepas intercept respons Delete
18. Klik `[Cancel]` pada dialog D-07
19. Verifikasi jumlah entri `DID099A` pada Changelog sama dengan baseline langkah 12
20. Verifikasi jumlah entri `DID099A` pada System Log aktor sama dengan baseline langkah 12
21. Verifikasi jumlah entri `DID099A` pada Activity Log sama dengan baseline langkah 12

### TC-FA-COA-71: Bulk Delete gagal 5xx

22. Catat baseline jumlah entri Account Code `DID099A` dan `DID099B` pada Changelog, System Log aktor, dan Activity Log dari server
23. Centang baris akun `DID099A`
24. Centang baris akun `DID099B`
25. Klik `Delete` pada Bulk Action Bar sehingga dialog Delete bulk (D-08) terbuka
26. Paksa respons Bulk Delete menjadi 5xx lewat intercept jaringan
27. Klik `[Delete]` pada dialog D-08
28. Verifikasi toast `Error, failed to delete account.` tampil
29. Lepas intercept respons Bulk Delete
30. Klik `[Cancel]` pada dialog D-08
31. Lepas seleksi akun terpilih
32. Klik `(←)` pada kotak Search
33. Verifikasi jumlah entri `DID099A` dan `DID099B` pada Changelog sama dengan baseline langkah 22
34. Verifikasi jumlah entri `DID099A` dan `DID099B` pada System Log aktor sama dengan baseline langkah 22
35. Verifikasi jumlah entri `DID099A` dan `DID099B` pada Activity Log sama dengan baseline langkah 22

## Notes

- Pembagian TC lintas spec (S-05): TC-FA-COA-65, TC-FA-COA-305, dan TC-FA-COA-71 ada di spec 068 (toast, dialog, dan data tetap ada) dan di spec ini (asersi "tidak ada entri log" dan "tidak ada log untuk akun yang tidak terhapus"). Spec ini memuat pemicu Delete yang sama dengan baseline sendiri per TC (S-12); spec 068 tidak mengasersi log.
- Langkah 6, 16, dan 28 (toast kegagalan hasil server) menjadi anchor positif bahwa respons sudah diproses sebelum asersi absence pada tiap surface log (bagian 8b butir 2 dan 11); tiga surface disebut satu per satu. Asersi absence ditulis sesudah intercept dilepas dan dialog ditutup.
- Langkah penghubung (S-03, S-09, R-16, R-23): langkah 2 (Search sufiks `{runId}-099` menampilkan kedua akun milik spec sebagai penemu baris target; langkah 32 mengosongkannya); langkah 7, 17, 29 (melepas intercept); langkah 8, 18, 30 (menutup dialog dengan `[Cancel]`); langkah 31 (melepas seleksi); langkah 1, 12, 22 mencatat baseline sebelum aksi pemicu tiap TC dan bukan asersi. Pemilihan `DID099A` dan `DID099B` pada langkah 23 dan 24 adalah precondition TC-FA-COA-71.
- Temuan untuk QA:
  - TC-FA-COA-65, 305, dan 71 menyebut "tidak ada log" tanpa surface; spec mengasersi Changelog, System Log aktor, dan Activity Log (PRD §8).
  - TC-FA-COA-71 menyebut P3 dan P5 "eligible" sedangkan Pre-setup mencatat P5 Active; spec memakai dua akun Inactive milik spec agar Delete tidak terblokir sebelum dialog D-08.
  - TC-FA-COA-71 Expected a "sebagian akun mungkin sudah terhapus" tidak diasersi karena respons dipaksa 5xx.
  - Search sufiks `{runId}-099` mengasumsikan Search mencocokkan sebagian Account Name; perlu dikonfirmasi tim FE.
