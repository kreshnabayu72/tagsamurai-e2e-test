---
id: TC-AC-RP-E2E-058-resilience-tulis-remove-role-detail-dan-approver
title: "Resilience Tulis: Remove Role Single dan Bulk Remove (Role Detail, Approver) Gagal 5xx atau Jaringan"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-RP-198
  - TC-AC-RP-199
  - TC-AC-RP-419
  - TC-AC-RP-420
coverage:
  web: automated
---

# Resilience Tulis: Remove Role Single dan Bulk Remove (Role Detail, Approver) Gagal 5xx atau Jaringan

## Prerequisites

- Mode: FE+BE.
- Mode memakai intercept respons parsial di atas backend nyata (bagian 6), bukan mock.
- Akun aktor pertama: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`, Pre-setup #1), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Data Pre-setup: #11, #12 (`Jane Smith`, `John Dohan`), #15 (`Manage device master data` memuat baris `John Dohan` dan `Jane Smith`), #17 (approver `Manage allocation` `Region Jawa` = `Dewi Anggraini` dan `Dewi Anggreni`), #23 (failure injection).
- Data Dinamis: spec ini tidak membuat entitas baru; semua target aksi adalah data Pre-setup bersama, sehingga nama literal Tabel Data Uji Pre-setup TC dipakai tanpa suffix `{runId}-NNN`.
- Fixture `fixtures/settings-role-permission.json` belum ada (ditandai); nama user, role, dan group di langkah mengikuti Tabel Data Uji Pre-setup TC.
- Flag Guided Tooltip halaman ini disetel hook suite (lihat `suite.md`).
- Kemampuan teknis: `Spectra.intercept()` untuk respons submit Remove di browser: 5xx (TC-AC-RP-198, 199) dan timeout atau koneksi terputus (TC-AC-RP-419, 420). Endpoint yang di-intercept ditentukan dari openapi atau LLD modul pada tahap script; TC tidak menyebut path. Intercept dilepas segera setelah asersi tiap blok. Tidak ada perubahan state server karena semua submit gagal, sehingga pemulihan baseline tidak diperlukan.
- Env var `AC_RP_TC_PASSWORD` baru dan belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; pendaftaran dilakukan di tahap script atau oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`

### TC-AC-RP-199: Remove Role single gagal 5xx

3. Pasang intercept: respons 5xx pada submit Remove
4. Klik `⋯` baris `John Dohan` lalu `Remove`
5. Klik `[Remove]`
6. Verifikasi toast "Error, failed to remove user."
7. Tutup toast error
8. Verifikasi dialog tetap terbuka tanpa perubahan
9. Verifikasi tombol `[Remove]` aktif kembali
10. Lepas intercept
11. Klik `[Cancel]`

### TC-AC-RP-198: Bulk Remove gagal 5xx mempertahankan seleksi

12. Pasang intercept: respons 5xx pada submit Remove
13. Centang `Jane Smith` dan `John Dohan`
14. Klik `Bulk Action` > `Remove` pada Bulk Action Bar lalu klik `[Remove]`
15. Verifikasi toast "Error, failed to remove user."
16. Verifikasi seleksi 2 baris dipertahankan untuk retry
17. Verifikasi Bulk Action Bar dipertahankan untuk retry
18. Lepas intercept
19. Muat ulang halaman (F5) untuk menutup dialog dan mereset seleksi

### TC-AC-RP-419: Bulk Remove Role Detail gagal jaringan atau timeout

20. Pasang intercept: timeout atau koneksi terputus pada submit Remove
21. Centang `Jane Smith` dan `John Dohan`
22. Klik `Bulk Action` > `Remove` pada Bulk Action Bar lalu klik `[Remove]`
23. Verifikasi toast "Connection problem. Please try again." tanpa tombol aksi
24. Verifikasi toast bukan "Error, failed to remove user."
25. Tutup toast error
26. Verifikasi dialog tetap terbuka tanpa perubahan
27. Verifikasi tombol `[Remove]` aktif kembali
28. Verifikasi seleksi 2 baris dipertahankan untuk retry
29. Verifikasi Bulk Action Bar dipertahankan untuk retry
30. Verifikasi tidak ada baris terhapus
31. Lepas intercept
32. Klik `[Cancel]`

### TC-AC-RP-420: Bulk Remove Approver gagal jaringan atau timeout

33. Klik menu `Settings > Role & Permission` di sidebar
34. Klik tab `System`
35. Pada section Group Role, klik `⋯` pada baris `Manage allocation` lalu klik `Detail`
36. Klik node `Region Jawa`
37. Pasang intercept: timeout atau koneksi terputus pada submit Remove
38. Centang kedua approver lalu klik `Bulk Action` > `Remove` pada Bulk Action Bar
39. Klik `[Remove]`
40. Verifikasi toast "Connection problem. Please try again." tanpa tombol aksi
41. Verifikasi toast bukan "Error, failed to remove approver."
42. Verifikasi dialog tetap terbuka tanpa perubahan
43. Verifikasi seleksi dan Bulk Action Bar dipertahankan
44. Verifikasi kedua approver tetap ada di tabel
45. Lepas intercept
46. Klik `[Cancel]`

## Notes

- Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan menyimpang dari nomor TC: TC-AC-RP-199 lebih dulu (dialog tetap terbuka sehingga dapat ditutup dengan `[Cancel]`), TC-AC-RP-198 berikutnya, lalu TC-AC-RP-419 dan TC-AC-RP-420 yang memakai kegagalan jaringan.
- Langkah penghubung (tanpa `Verifikasi`, S-03): pemasangan dan pelepasan intercept per blok, klik `[Cancel]` yang menutup dialog yang tetap terbuka, langkah 19 (muat ulang halaman karena TC-AC-RP-198 tidak menyatakan keadaan dialog sesudah 5xx; tidak ada form dirty), klik sidebar dan klik tab (menuju Detail `Manage allocation`), langkah 7 dan 25 (tutup toast error identik yang muncul berulang pada blok berikutnya sebelum diasersi lagi, R-12; langkah 25 diletakkan sesudah asersi toast bukan "Error, failed to remove user." agar asersi itu tetap membaca toast yang sama).
- Alasan spec berada di atas sekitar 35 langkah: seluruh blok memakai satu kelas harness (kelas b, intercept respons submit Remove) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna karena tiap blok memasang dan melepas intercept sendiri dan memulai dari state bersih.
- Temuan untuk QA:
  - TC-AC-RP-198 Expected tidak menyatakan keadaan dialog sesudah 5xx (TC-AC-RP-199 dan TC-AC-RP-419 menyatakan dialog tetap terbuka); spec tidak mengasersinya untuk TC-AC-RP-198 dan memuat ulang halaman sebagai langkah penghubung.
  - TC-AC-RP-420 langkah 5 "Centang kedua approver" mengasumsikan dua approver di `Manage allocation` `Region Jawa` (Pre-setup #17: `Dewi Anggraini` dan `Dewi Anggreni`).
  - TC-AC-RP-198, 199, 419, 420: kegagalan dipaksa lewat intercept (Pre-setup #23); asersi "tidak ada baris terhapus" dan "kedua approver tetap" membaca state UI sesudah kegagalan, bukan state server terpisah.
  - Mekanisme "dipulihkan automation baseline" (bagian Catatan dan Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
