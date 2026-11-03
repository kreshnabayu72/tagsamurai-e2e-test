---
id: TC-FA-SU-E2E-309-format-tanggal-general-settings-pohon-grup-settings-groups-dan-pembaruan-peran-dari-role-permission
title: "Format Tanggal General Settings, Pohon Grup Settings Groups, dan Pembaruan Peran dari Role & Permission"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-951
  - TC-FA-SU-960
  - TC-FA-SU-961
  - TC-FA-SU-962
coverage:
  web: automated
---

# Format Tanggal General Settings, Pohon Grup Settings Groups, dan Pembaruan Peran dari Role & Permission

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan (#23), dan Changelog (#27). Nama dan atribut Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Pengguna milik spec (dibuat lewat seed API di hook `before` dengan keadaan sama seperti pengguna Pre-setup bernama sama, dihapus di hook `after`; pengguna Pre-setup bersama tidak diubah, S-06; entri log permanen tidak dibersihkan):
  - `Fajar Nugroho {runId}-309`, email `fajar.nugroho+{runId}-309@qwertysystem.net`: Active; Temporary User sampai 31/12/26 (TC-FA-SU-951).
  - `Budi Santoso {runId}-309`, email `budi.santoso+{runId}-309@qwertysystem.net`: Active; sedikitnya satu entri Tab Changelog dari seed Changelog (TC-FA-SU-951).
  - `Hana Kusuma {runId}-309`, email `hana.kusuma+{runId}-309@qwertysystem.net`: Active; Home Group grup milik spec `General Affairs {runId}-309` (TC-FA-SU-960).
  - `Gita Permata {runId}-309`, email `gita.permata+{runId}-309@qwertysystem.net`: Active; 3 roles (Global Role Import Data dan Manage accounting; Group Role Manage group pada Finance & Accounting) (TC-FA-SU-961).
  - `Gita Permata 2 {runId}-309`, email `gita.permata+{runId}-309-2@qwertysystem.net`: Active; tanpa tingkat akses (TC-FA-SU-962).
  - Grup milik spec `General Affairs {runId}-309` (di bawah All Groups) untuk di-rename oleh TC-FA-SU-960; grup `Regional Audit {runId}-309` dibuat oleh TC-FA-SU-960. Kedua grup dihapus lewat seed API di hook `after`.
- Principal Automation (Pre-setup #12) mengubah format tanggal di Global Settings > General Settings (TC-FA-SU-951) dan format sebelumnya dipulihkan di hook `after`. Nilai format baru disediakan tim FE (TC tidak menyebutnya, lihat Temuan untuk QA); jam server dan jam browser sinkron. Principal Automation (Pre-setup #12) memicu perubahan di Global Settings (App Access, identitas, status aktif, email, Custom Field) lewat sesi API; kemampuan ini disediakan tim FE (S-13). Langkah pemicunya ditulis "... hingga ... tersimpan" (R-20) dan bukan konteks UI kedua, sehingga tidak memakai `P-2`.
- Kemampuan menghapus preferensi kolom Setup Column di browser (bagian 4 konvensi) dan kemampuan membaca isi berkas hasil Download (nilai sel, tipe sel, BOM), disediakan tim FE (kelas f, hook H11).
- Kemampuan Principal Automation untuk menetapkan dan melepaskan tingkat akses serta menambah dan menghapus pemegang peran lewat Settings > Role & Permission (TC-FA-SU-961 dan TC-FA-SU-962), disediakan tim FE/BE; langkah UI Role & Permission tidak diuraikan TC.
- Tidak ada intercept, jam server, atau klien HTTP. State global: tidak ada; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-961: Pembaruan peran dari Role & Permission tampil di label Role User List dan Popup Role Count

1. Ketik Search `Gita Permata {runId}-309`, tekan Enter
2. Catat label Role baris Gita Permata {runId}-309
3. Di Settings > Role & Permission, tambahkan Gita Permata {runId}-309 ke Manage files grup General Affairs
4. Tunggu aksi selesai, lalu buka Fixed Asset > Settings > User dan Search `Gita Permata {runId}-309`, tekan Enter
5. Verifikasi label Role baris Gita Permata {runId}-309 naik dari `3 roles` menjadi `4 roles`
6. Klik label `4 roles` untuk membuka Popup Role Count
7. Verifikasi Popup Role Count memuat Manage files
8. Tutup Popup Role Count dengan `[✕]`
9. Di Settings > Role & Permission, hapus Gita Permata {runId}-309 dari Manage files grup General Affairs
10. Tunggu aksi selesai, lalu buka Fixed Asset > Settings > User dan Search `Gita Permata {runId}-309`, tekan Enter
11. Verifikasi label Role baris Gita Permata {runId}-309 turun kembali menjadi `3 roles`

### TC-FA-SU-962: Tingkat akses Total Control dan Read Only dari Role & Permission tampil sebagai badge kolom Role dan banner Tab Role

12. Di Settings > Role & Permission, tetapkan Gita Permata 2 {runId}-309 sebagai Total Control
13. Tunggu aksi selesai, lalu buka Fixed Asset > Settings > User dan Search `Gita Permata 2 {runId}-309`, tekan Enter
14. Verifikasi badge `Total Control` menggantikan label jumlah Role pada baris Gita Permata 2 {runId}-309
15. Klik nama Gita Permata 2 {runId}-309 lalu buka Tab Role
16. Verifikasi banner tingkat akses Total Control tampil di Tab Role
17. Di Settings > Role & Permission, lepaskan tingkat akses Gita Permata 2 {runId}-309
18. Tunggu aksi selesai, lalu muat ulang Tab Role
19. Verifikasi Sub-tab Group Role dan Sub-tab Transaction Role tampil di Tab Role setelah dimuat ulang
20. Verifikasi banner tingkat akses hilang dari Tab Role
21. Kembali ke User List lewat breadcrumb `User` dan Search `Gita Permata 2 {runId}-309`, tekan Enter
22. Verifikasi badge kembali menjadi label jumlah Role pada baris Gita Permata 2 {runId}-309

### TC-FA-SU-960: Sidebar Group Tree dan pemilih grup mengikuti Settings > Groups terbaru

23. Buat grup `Regional Audit {runId}-309` dan ubah nama `General Affairs {runId}-309` menjadi `General Services {runId}-309` di Settings > Groups
24. Tunggu aksi selesai, lalu buka Fixed Asset > Settings > User tanpa muat ulang manual
25. Verifikasi Sidebar Group Tree memuat grup `Regional Audit {runId}-309`
26. Verifikasi badge Group Home Group baris Hana Kusuma {runId}-309 menampilkan nama baru `General Services {runId}-309`
27. Klik ⋯ pada baris Hana Kusuma {runId}-309 dan klik `Edit Home Group`
28. Verifikasi popup Select Home Group memuat grup `Regional Audit {runId}-309` dan `General Services {runId}-309`
29. Tutup popup Select Home Group dengan `[Cancel]`, lalu buka Detail Gita Permata {runId}-309 > Tab Role > Sub-tab Group Role, buka popup Assign Group Role Manage files, dan klik `[+ Assign Group]` untuk membuka popup Select Group
30. Verifikasi popup Select Group memuat grup `Regional Audit {runId}-309` dan `General Services {runId}-309`
31. Tutup popup Select Group dengan `[Cancel]` dan popup Assign Group Role dengan `[✕]`, lalu buka Sub-tab Transaction Role dan klik `[+ Assign]`
32. Verifikasi pohon grup Assign Group Transaction Role memuat grup `Regional Audit {runId}-309` dan `General Services {runId}-309`
33. Tutup modal Assign Transaction Role dengan `[✕]`

### TC-FA-SU-951: Format tanggal dan zona waktu mengikuti General Settings pada kolom Last Updated, Date log, dan Temporary Until

34. Principal Automation mengubah format tanggal di Global Settings > General Settings ke format baru hingga perubahan tersimpan
35. Tunggu aksi selesai, lalu buka Fixed Asset > Settings > User, klik Setup Column, tampilkan kolom Temporary Until, dan klik `[Save]`
36. Ketik Search `Fajar Nugroho {runId}-309`, tekan Enter
37. Verifikasi kolom Last Updated baris Fajar Nugroho {runId}-309 memakai format tanggal baru
38. Verifikasi kolom Temporary Until baris Fajar Nugroho {runId}-309 memakai format tanggal baru
39. Klik `(←)` pada kotak Search, lalu klik nama Budi Santoso {runId}-309 dan buka Tab Changelog, muat ulang sampai entri tampil
40. Verifikasi kolom Date entri Tab Changelog memakai format tanggal baru
41. Kembali ke User List lewat breadcrumb `User`, lalu klik Download dan pilih `Download as CSV`
42. Verifikasi format Date pada berkas hasil Download memakai format tanggal baru
43. Pulihkan format tanggal General Settings ke nilai awal lewat seed API dan hapus preferensi kolom Setup Column di browser

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber diubah: TC-FA-SU-961 dan TC-FA-SU-962 dikerjakan lebih dulu, TC-FA-SU-960 sesudahnya, dan TC-FA-SU-951 terakhir karena mengubah format tanggal yang dipakai asersi lain (S-10).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): 1, 4, 8, 10, 13, 15, 18, 21, 24, 27, 29, 31, 33, 35, 36, 39, 41, 43; langkah baseline jumlah entri (S-12): 2. Langkah 1, 4, 10, 13, 21, dan 36 juga Search untuk menemukan baris target (R-16); langkah 43 adalah pemulihan state (S-09). Langkah 19 adalah anchor positif untuk asersi absence banner pada langkah 20 (8b.2).
- Alasan di atas sekitar 35 langkah: seluruh TC satu topik (sinkronisasi dari modul lain ke Settings > User) dan tiap TC berdiri sendiri dengan pengguna milik spec; kegagalan satu TC tidak membuat TC lain kehilangan makna (43 langkah).
- Pengguna dan grup milik spec bernama sama dengan Pre-setup TC dengan suffix `{runId}-309` (S-06); grup `Regional Audit` memakai suffix per run (S-12).
- Temuan untuk QA (S-15):
  - TC-FA-SU-951 tidak menyebut format baru yang dipilih dan menyebut Temporary Until tanpa lokasinya; spec menampilkan kolom Temporary Until lewat Setup Column pada User List dan mengasersi format pada baris Fajar Nugroho. Butir b (Download) adalah isi berkas (kelas f) dan diasersi lewat kemampuan baca berkas yang disediakan tim FE. Zona waktu pada judul TC tidak punya Expected sendiri dan tidak diasersi.
  - TC-FA-SU-960 menyebut empat surface (Sidebar Group Tree, Select Group, Select Home Group, pohon Assign Group Transaction Role) di Expected, sedangkan Langkah Uji hanya menyebut User List, popup Select Group, dan Sub-tab Group Role; spec membuka keempatnya. Rename `General Affairs` ke `General Services` diterapkan pada grup milik spec bernama `General Affairs {runId}-309` dan diasersi lewat badge Group Home Group.
  - TC-FA-SU-961 butir b ("Role yang dihapus menurunkan label") tidak punya langkah; spec menambah langkah menghapus pemegang peran yang baru ditambahkan lalu mengasersi label kembali `3 roles`.
  - TC-FA-SU-962 butir c ("Modul ini tidak menulis log untuk peristiwa tersebut") bertentangan dengan TC-FA-SU-927 dan TC-FA-SU-928 yang menyatakan entri tingkat akses dari Role & Permission tampil di Tab Changelog dan System Log; spec tidak mengasersi butir c.
