---
id: TC-FA-SU-E2E-033-resilience-bulk-status-aktif-pemeriksaan-gagal-sebagian-gagal-dan-seluruh-item-gagal
title: "Resilience Bulk Status Aktif: Pemeriksaan Gagal, Sebagian Gagal, dan Seluruh Item Gagal"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-107
  - TC-FA-SU-118
  - TC-FA-SU-119
  - TC-FA-SU-134
coverage:
  web: automated
---

# Resilience Bulk Status Aktif: Pemeriksaan Gagal, Sebagian Gagal, dan Seluruh Item Gagal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Lina Marlina`), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip `seen`, sesi API aktor, pemulihan) mengikuti `suite.md`. Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Client `FaUserMain` (#20) dan layanan terkendali (#37: layanan pemeriksaan aset dan approval dapat di-intercept). Target memakai pengguna milik spec (S-06).
- Pengguna milik spec (seed API di hook `before`, dihapus di hook `after`; dirujuk lewat `Fixture.fa-settings-user.<kunci>`, fixture belum ada dan disediakan tim FE). Nama tampil `<alias> {runId}-033`, email `<alias>+{runId}-033@qwertysystem.net` dengan alias huruf kecil:
  - TC-FA-SU-107: `U107A` dan `U107B`, keduanya Active.
  - TC-FA-SU-118: `U118A`, `U118B`, `U118C` Active dan `U118D` Inactive.
  - TC-FA-SU-119: `U119A` dan `U119B`, keduanya Active.
  - TC-FA-SU-134: `U134A` dan `U134B` Inactive dan `U134C` Active.
- Kemampuan teknis:
  - `Spectra.intercept()` atas respons HTTP di atas backend nyata: respons pemeriksaan aset dan approval dibuat timeout; respons request bulk dibuat gagal untuk satu item (`U118A` pada TC-FA-SU-118, `U134A` pada TC-FA-SU-134) atau untuk seluruh item (TC-FA-SU-119). Tiap intercept dilepas segera setelah pemicunya (S-09).
  - Pencatat request jaringan Spectra untuk memastikan daftar dimuat ulang sesudah respons bulk.
  - Kemampuan baca log (disediakan tim FE/BE, tanpa endpoint karangan): baseline dicatat per TC pada langkah 24 (TC-FA-SU-119) dan 36 (TC-FA-SU-134), tepat sebelum pemicunya, bukan sekali di hook `before`, karena aksi TC sebelumnya menambah entri System Log aktor dan Activity Log; asersi memakai selisih terhadap baseline TC itu sendiri (S-12).
- State global: tidak ada; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-107: Dialog Bulk Deactivate saat pemeriksaan gagal

1. Ketik Search `U107`, tekan Enter
2. Centang `U107A {runId}-033` dan `U107B {runId}-033`
3. Pasang intercept: respons pemeriksaan aset aktif dan approval tertunda menjadi timeout
4. Klik Bulk Action > `[Deactivate]`
5. Verifikasi dialog menampilkan satu baris `We couldn't check this user's active assets or pending approvals. You can still continue.` (bukan per pengguna)
6. Lepas intercept pemeriksaan aset aktif dan approval tertunda
7. Verifikasi tombol `[Deactivate]` Enabled
8. Klik `[Deactivate]`
9. Verifikasi sakelar Active `U107A {runId}-033` dan `U107B {runId}-033` berpindah ke OFF

### TC-FA-SU-118: Bulk Deactivate sebagian gagal di server

10. Ganti isi kotak search dengan `U118`, tekan Enter
11. Centang `U118A {runId}-033`, `U118B {runId}-033`, dan `U118C {runId}-033` (Active) serta `U118D {runId}-033` (Inactive)
12. Pasang intercept: respons request bulk gagal untuk item `U118A {runId}-033`
13. Klik Bulk Action > `[Deactivate]`
14. Klik `[Continue]`
15. Verifikasi toast "Success, user has been deactivated. Some items failed." tampil
16. Lepas intercept request bulk
17. Verifikasi sakelar Active `U118B {runId}-033` dan `U118C {runId}-033` OFF (item yang sudah ter-commit tetap tersimpan)
18. Verifikasi sakelar `U118A {runId}-033` tetap ON dan `U118D {runId}-033` tetap OFF
19. Verifikasi daftar di-refresh (request daftar ulang tercatat sesudah respons bulk)
20. Verifikasi seleksi dan Bulk Actions Bar dipertahankan

### TC-FA-SU-119: Bulk Deactivate seluruh item gagal

21. Klik `[Unselect All]`
22. Ganti isi kotak search dengan `U119`, tekan Enter
23. Centang `U119A {runId}-033` dan `U119B {runId}-033`
24. Catat baseline lewat kemampuan baca log: jumlah entri Tab Changelog `U119A {runId}-033` dan `U119B {runId}-033`, total entri Tab System Log aktor, dan total entri Activity Log
25. Pasang intercept: respons request bulk gagal untuk seluruh item
26. Klik Bulk Action > `[Deactivate]`
27. Klik `[Deactivate]` pada dialog
28. Verifikasi toast "Error, failed to deactivate user." tampil
29. Lepas intercept request bulk
30. Verifikasi seleksi dan Bulk Actions Bar tetap ada
31. Verifikasi sakelar Active `U119A {runId}-033` dan `U119B {runId}-033` tetap ON
32. Verifikasi jumlah entri Tab Changelog kedua pengguna, total entri Tab System Log aktor, dan total entri Activity Log sama dengan baseline langkah 24

### TC-FA-SU-134: Bulk Activate sebagian gagal di server

33. Klik `[Unselect All]`
34. Ganti isi kotak search dengan `U134`, tekan Enter
35. Centang `U134A {runId}-033` dan `U134B {runId}-033` (Inactive) serta `U134C {runId}-033` (Active)
36. Catat baseline lewat kemampuan baca log: jumlah entri `Activate` pada Tab Changelog `U134A {runId}-033`, `U134B {runId}-033`, dan `U134C {runId}-033`
37. Pasang intercept: respons request bulk Activate gagal untuk item `U134A {runId}-033`
38. Klik Bulk Action > `[Activate]`
39. Klik `[Continue]`
40. Verifikasi toast "Success, user has been activated. Some items failed." tampil
41. Lepas intercept request bulk
42. Verifikasi sakelar Active `U134B {runId}-033` ON (item yang sudah ter-apply tetap aktif)
43. Verifikasi sakelar `U134A {runId}-033` tetap OFF (item gagal tetap Inactive)
44. Verifikasi daftar di-refresh (request daftar ulang tercatat sesudah respons bulk)
45. Verifikasi seleksi dipertahankan
46. Verifikasi entri `Activate` hanya bertambah satu untuk `U134B {runId}-033` pada Tab Changelog ketiga pengguna, dan tidak bertambah untuk `U134A {runId}-033` dan `U134C {runId}-033`, terhadap baseline langkah 36

## Notes

- Alasan di atas 35 langkah (46): semua blok satu kelas harness (kegagalan yang dipaksakan, kelas b) dan satu topik (bulk Activate dan Deactivate dengan intercept); tiap blok memakai pengguna milik spec sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target, R-16), langkah 10, 22, dan 34 (mengganti isi kotak search yang masih berisi nilai sebelumnya, bagian 8b butir 9), langkah 21 dan 33 (membersihkan seleksi dari blok sebelumnya, S-09), langkah 6, 16, 29, dan 41 (melepas intercept, S-09), serta langkah 24 dan 36 (mencatat baseline per TC lewat kemampuan baca log, S-12).
- Pembagian TC lintas spec: TC-FA-SU-95, TC-FA-SU-101, TC-FA-SU-102, dan TC-FA-SU-103 (resilience single) ada di spec 032.
- Temuan untuk QA:
  - TC-FA-SU-119 mencantumkan petunjuk absence (tanpa entri log) pada Expected butir b; spec mengasersinya sebagai jumlah terhadap baseline pada langkah 32 (bukan spec absence).
  - Post Condition TC-FA-SU-118 butir a dan TC-FA-SU-134 butir a ("satu entri log per item yang berhasil; item gagal dan di-skip tidak berubah") tidak punya langkah observasi di TC-FA-SU-118 sehingga tidak diasersi; pada TC-FA-SU-134 langkah 4 TC membuka Tab Changelog, sehingga Expected butir c diasersi pada langkah 46.
  - TC-FA-SU-118 memakai tiga pengguna Active dan satu Inactive serta menyebut "baris di-skip" tanpa menyebut pengguna yang di-skip; spec menafsirkan pengguna Inactive sebagai yang di-skip.
  - Target TC adalah pengguna Pre-setup bersama dan nama generik; spec memakai pengguna milik spec dengan suffix (S-06).
