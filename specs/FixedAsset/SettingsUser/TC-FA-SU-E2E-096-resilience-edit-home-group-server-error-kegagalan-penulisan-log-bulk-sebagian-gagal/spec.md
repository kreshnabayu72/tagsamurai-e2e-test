---
id: TC-FA-SU-E2E-096-resilience-edit-home-group-server-error-kegagalan-penulisan-log-bulk-sebagian-gagal
title: "Resilience Edit Home Group: Server Error, Kegagalan Penulisan Log, Bulk Sebagian Gagal, dan Seluruh Gagal"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-301
  - TC-FA-SU-303
  - TC-FA-SU-310
  - TC-FA-SU-311
coverage:
  web: automated
---

# Resilience Edit Home Group: Server Error, Kegagalan Penulisan Log, Bulk Sebagian Gagal, dan Seluruh Gagal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), changelog (#27). Pengguna target: Gita Permata (Home Group Finance & Accounting), Hana Kusuma, Kartika Sari, Mira Anggraini, Eka Wulandari. Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis: `Spectra.intercept()` atas respons HTTP Edit Home Group tunggal dan bulk (5xx, kegagalan sebagian per item, kegagalan seluruh item). Intercept dilepas segera setelah pemicu selesai (S-09).
- Kemampuan teknis (disediakan tim FE/BE): memicu kegagalan penulisan log di sisi server (layanan log terkendali, Pre-setup #37) dan memulihkannya. TC-FA-SU-303 berlabel `Manual Only — BE`; tetap dimasukkan karena tidak ada `tc-settings-user-backend.md`.
- Kemampuan baca jumlah entri (disediakan tim FE/BE): entri `Edit Home Group` pada Tab Changelog pengguna target, Tab System Log aktor, dan Activity Log, dibaca sebelum dan sesudah aksi. Audit trail bersifat permanen sehingga asersi hanya memakai selisih terhadap baseline (S-12), bukan angka absolut.
- Kemampuan seed API (disediakan tim BE/FE): memulihkan Home Group dan penugasan peran pengguna Pre-setup ke kondisi Tabel Data Uji Pre-setup TC. Pemulihan dijalankan sebagai langkah penghubung dan di hook `after` (cadangan). Pemulihan Home Group item bulk yang berhasil pada langkah 35 dan di hook `after`. Efek pada Pre-setup: Home Group item bulk yang berhasil berubah (Last Updated, Modified By) dan entri log permanen bertambah.

## Test Steps

1. Catat jumlah entri `Edit Home Group` pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log sebagai baseline

### TC-FA-SU-301: Edit Home Group gagal karena server error

2. Ketik Search `Gita Permata`, tekan Enter
3. Intercept respons Edit Home Group menjadi 5xx
4. Klik ⋯ pada baris Gita Permata lalu klik `Edit Home Group`
5. Klik node IT Infrastructure lalu klik `[Select]`
6. Lepas intercept Edit Home Group
7. Verifikasi toast error "Error, failed to update home group." tampil
8. Verifikasi popup tetap terbuka
9. Verifikasi Home Group Gita Permata di tabel tidak berubah
10. Klik `[Cancel]`

### TC-FA-SU-303: Kegagalan penulisan log membatalkan perubahan

11. Picu kegagalan penulisan log di sisi server
12. Klik ⋯ pada baris Gita Permata, klik `Edit Home Group`, klik node IT Infrastructure, lalu klik `[Select]`
13. Verifikasi toast gagal tampil
14. Verifikasi Home Group Gita Permata tidak berubah
15. Klik `[Cancel]` pada popup Select Home Group
16. Pulihkan layanan penulisan log
17. Baca jumlah entri `Edit Home Group` pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log
18. Verifikasi jumlah entri sama dengan baseline pada Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log

### TC-FA-SU-310: Bulk sebagian gagal

19. Intercept respons bulk Edit Home Group sehingga satu item gagal
20. Ganti isi kotak search dengan `Hana Kusuma`, tekan Enter
21. Centang Hana Kusuma
22. Ganti isi kotak search dengan `Kartika Sari`, tekan Enter
23. Centang Kartika Sari
24. Ganti isi kotak search dengan `Mira Anggraini`, tekan Enter
25. Centang Mira Anggraini lalu klik Bulk Action > `Edit Home Group`
26. Klik node IT Infrastructure lalu klik `[Select]`
27. Lepas intercept bulk Edit Home Group
28. Verifikasi toast "Success, home group has been updated. Some items failed." tampil
29. Verifikasi daftar di-refresh
30. Verifikasi item Mira Anggraini yang sudah ter-apply tetap tersimpan
31. Ganti isi kotak search dengan `Hana Kusuma`, tekan Enter
32. Verifikasi item Hana Kusuma yang sudah ter-apply (bila ada) tetap tersimpan
33. Ganti isi kotak search dengan `Kartika Sari`, tekan Enter
34. Verifikasi item Kartika Sari yang sudah ter-apply (bila ada) tetap tersimpan
35. Pulihkan Home Group Hana Kusuma, Kartika Sari, dan Mira Anggraini ke kondisi Pre-setup lewat seed API

### TC-FA-SU-311: Bulk seluruh item gagal

36. Catat jumlah entri `Edit Home Group` pada Tab Changelog Hana Kusuma, Tab Changelog Eka Wulandari, Tab System Log aktor, dan Activity Log sebagai baseline
37. Intercept respons bulk Edit Home Group sehingga seluruh item gagal
38. Ganti isi kotak search dengan `Hana Kusuma`, tekan Enter
39. Centang Hana Kusuma
40. Ganti isi kotak search dengan `Eka Wulandari`, tekan Enter
41. Centang Eka Wulandari lalu klik Bulk Action > `Edit Home Group`
42. Klik node IT Infrastructure lalu klik `[Select]`
43. Lepas intercept bulk Edit Home Group
44. Verifikasi toast error "Error, failed to update home group." tampil
45. Klik `[Cancel]` pada popup Select Home Group
46. Verifikasi tidak ada Home Group yang berubah pada Eka Wulandari
47. Ganti isi kotak search dengan `Hana Kusuma`, tekan Enter
48. Verifikasi tidak ada Home Group yang berubah pada Hana Kusuma
49. Baca jumlah entri `Edit Home Group` pada Tab Changelog Hana Kusuma, Tab Changelog Eka Wulandari, Tab System Log aktor, dan Activity Log
50. Verifikasi jumlah entri sama dengan baseline langkah sebelum intercept pada Tab Changelog Hana Kusuma, Tab Changelog Eka Wulandari, Tab System Log aktor, dan Activity Log

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec berisi satu kelas harness (b, fault injection) dengan intercept di atas backend nyata; modenya FE+BE (bagian 6).
- Langkah penghubung (tanpa awalan `Verifikasi`): langkah 1 dan langkah baseline TC-FA-SU-311 (baseline), menutup popup dengan `[Cancel]`, melepas intercept dan layanan log (S-09), dan langkah 35 (pemulihan).
- Langkah penghubung Search (R-16, bagian 8b butir 9 dan 13): langkah 2, 20, 22, 24, 38, dan 40 mencari baris target sebelum membuka menu ⋯ atau mencentang, karena User List memuat 3 halaman; baris bulk dicentang satu per satu dengan Search per baris. Langkah 31, 33, dan 47 menyempitkan tabel ke satu pengguna sebelum asersi atas pengguna itu (Search menyempitkan tabel, bagian 8b butir 13 dan 9); popup Select Home Group ditutup lebih dulu (langkah 45) supaya kotak Search dapat dipakai. Popup Select Home Group yang tetap terbuka sesudah kegagalan ditutup dengan `[Cancel]` pada langkah 15 dan 45 sebelum aksi berikutnya (S-09, S-03).
- Jumlah langkah 50, di atas smell 35 langkah; semua blok satu kelas harness (kegagalan yang dipaksakan, kelas b) dan satu topik (resilience Edit Home Group); tiap blok memakai pengguna Pre-setup sendiri dan berdiri sendiri; kelebihan berasal dari Search per baris target (R-16) dan satu Verifikasi per klausa Expected (S-01).
- Pembagian log: TC-FA-SU-301, TC-FA-SU-303, dan TC-FA-SU-311 "tidak ada entri log" ditulis sebagai asersi jumlah dengan baseline (S-12), bukan kelas g. Baseline langkah 1 dipakai untuk Gita Permata (TC-FA-SU-301 dan TC-FA-SU-303); TC-FA-SU-311 memakai baseline sendiri karena TC-FA-SU-310 menambah entri. Post Condition TC-FA-SU-310 "satu entri log per item" tidak punya langkah observasi dan tidak diasersi.
- Temuan untuk QA (S-15): (1) TC-FA-SU-303 tidak menyebut teks toast gagal; spec memverifikasi toast error tampil tanpa teks. (2) TC-FA-SU-303 berlabel `Manual Only — BE` dengan PIC FE `-`; kemampuan memicu kegagalan penulisan log di sisi server disediakan tim FE/BE (S-13). (3) TC-FA-SU-310 dan TC-FA-SU-311 tidak menyebut baris yang dicentang; spec memakai Hana Kusuma, Kartika Sari, Mira Anggraini (TC-FA-SU-310) dan Hana Kusuma, Eka Wulandari (TC-FA-SU-311) serta node IT Infrastructure. (4) TC-FA-SU-310 tidak menyebut item mana yang gagal; ditentukan oleh intercept. (5) Post Condition TC-FA-SU-311 ("item yang berhasil tersimpan") bertentangan dengan Expected (seluruh item gagal); spec mengikuti Expected. (6) TC-FA-SU-303 dan TC-FA-SU-311 tidak menyebut keadaan popup Select Home Group sesudah kegagalan; spec menutupnya dengan `[Cancel]` mengikuti TC-FA-SU-301 (popup tetap terbuka pada kegagalan). TC-FA-SU-310 dan TC-FA-SU-311 mencentang beberapa baris tanpa menyebut cara menemukan baris; spec memakai Search per baris dan mengasumsikan seleksi bertahan saat isi Search berganti. Bila seleksi tidak bertahan, QA perlu menyebut cara lain.
