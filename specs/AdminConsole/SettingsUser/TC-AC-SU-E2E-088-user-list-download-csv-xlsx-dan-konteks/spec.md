---
id: TC-AC-SU-E2E-088-user-list-download-csv-xlsx-dan-konteks
title: "User List Download: Overlay, CSV, XLSX dengan Search, Filter, Node Sidebar Group, dan Kolom Tampil"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-315
  - TC-AC-SU-316
  - TC-AC-SU-317
  - TC-AC-SU-318
  - TC-AC-SU-661
coverage:
  web: automated
---

# User List Download: Overlay, CSV, XLSX dengan Search, Filter, Node Sidebar Group, dan Kolom Tampil

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` dan kemampuan Fixture BE mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (di-seed hook `before` lewat Fixture BE; nama bersuffix `{runId}-088`): group tree `Region A {runId}-088` > `Branch 1 {runId}-088` > `Floor 1 {runId}-088`; `Region A {runId}-088` > `Branch 3 {runId}-088`; `Region B {runId}-088`. User: `Jane Smith {runId}-088` (Inactive, Group Role aktif di `Floor 1 {runId}-088`), `Mike Tan {runId}-088` (Active, Group Role aktif di `Branch 3 {runId}-088`), `Rudi Hartono {runId}-088` (hanya Global Role), `Sarah Lee {runId}-088` (Group Role tanpa group assignment), `Dedi Kurnia {runId}-088` (Group Manager `Region A {runId}-088`), `Dewi Lestari {runId}-088` dan `Rina Putri {runId}-088` (Total Control), `Andi Wijaya {runId}-088` (Read Only), `John Doe {runId}-088` (Group Role aktif di `Region B {runId}-088`, Active). Baris Default User Principal (Pre-setup #1, Total Control permanen) dipakai apa adanya. Entitas memuat lebih dari 10 user.
- Kemampuan teknis: membaca berkas unduhan (nama berkas, kolom, dan jumlah baris) dan membaca jumlah total user entitas lewat Fixture BE (N), disediakan tim FE/BE.
- Hook `after` menghapus data yang di-seed hook `before` spec ini lewat Fixture BE; pembersihan tidak berasumsi seeding berhasil penuh.
- Pemulihan Setup Column: preferensi kolom yang disimpan spec ini dihapus di hook `after` dengan menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan ini disediakan tim FE.

## Test Steps

### TC-AC-SU-315: Screening overlay Download

1. Hover icon Download
2. Verifikasi tooltip `Download` tampil
3. Klik icon Download
4. Verifikasi overlay Download User List memuat `Download as CSV` dan `Download as XLSX`
5. Tekan Esc untuk menutup overlay

### TC-AC-SU-316: Download CSV tanpa search dan filter mengekspor seluruh baris

6. Ubah page size menjadi 10
7. Catat jumlah total user entitas (N) lewat Fixture BE
8. Klik icon Download, klik `Download as CSV`
9. Verifikasi tidak ada toast sukses
10. Verifikasi berkas `User.csv` terunduh
11. Verifikasi `User.csv` berisi N baris data (tidak terbatas halaman 1)

### TC-AC-SU-317: Download XLSX mengikuti Search dan Filter aktif

12. Klik icon Filter
13. Pilih Status `Active`, klik `[Apply]`
14. Klik icon Search, ketik Search `Doe`, tekan Enter
15. Klik icon Download, klik `Download as XLSX`
16. Verifikasi tidak ada toast sukses
17. Verifikasi berkas `User.xlsx` terunduh
18. Klik `(←)` pada kotak Search
19. Klik icon Filter
20. Klik `[Clear Field]`, klik `[Apply]`

### TC-AC-SU-661: Download User List mengikuti node Sidebar Group yang aktif

21. Klik node `Region A {runId}-088` di Sidebar Group
22. Klik icon Download, klik `Download as XLSX`
23. Verifikasi tidak ada toast sukses
24. Verifikasi berkas `User.xlsx` terunduh
25. Klik node `Region A {runId}-088` agar ter-deselect

### TC-AC-SU-318: Download mengikuti kolom yang tampil (hide lalu unhide)

26. Klik `⋯` pada header Actions
27. Hapus centang kolom Email pada overlay Column Visibility
28. Klik icon Download, klik `Download as CSV`
29. Verifikasi tidak ada toast atau warning
30. Verifikasi berkas CSV pertama terunduh dan memuat kolom `Name`
31. Verifikasi berkas CSV pertama tidak memuat kolom Email
32. Klik `⋯` pada header Actions
33. Centang kolom Email pada overlay Column Visibility
34. Klik icon Download, klik `Download as CSV`
35. Verifikasi berkas CSV kedua memuat kolom Email

## Notes

- Langkah penghubung (S-03): Esc menutup overlay Download; `(←)`, `[Clear Field]` lalu `[Apply]`, dan men-deselect node mengembalikan state List di antara TC (S-09). Kolom Email di TC-318 dipulihkan pada langkah terakhir TC.
- Berkas unduhan hanya diasersi pada nama berkas, kolom, dan jumlah baris (bagian 3 prinsip 13f); keanggotaan baris berkas TC-317 dan TC-661 serta nilai sel TC-319 diasersi di spec 089.
- Langkah 30 adalah asersi tambahan (S-03, dasar 8b.2): berkas CSV pertama terunduh dengan kolom `Name` menjadi anchor positif bagi absence kolom Email pada langkah 31.
- Asersi tidak ada toast sukses diletakkan tepat setelah klik Download dan sebelum Verifikasi berkas (bagian 8b butir 11); klik pilihan format menjadi anchor positif yang buktinya menyusul pada Verifikasi berkas terunduh.
- TC-661 menyalin tree dan penempatan user dari TC-26 (sama dengan TC-283 di spec 080).
- Alasan di atas ±35 langkah: kelima TC adalah Download User List kelas fungsional, dataset sama, berdiri sendiri.
- Temuan untuk QA:
  - TC menulis nama data DS-UL secara literal (nama user, email, position, division). Spec memakai nama bersuffix ` {runId}-088` (S-12) dan mengasersi baris milik spec; klaim "hanya X yang tampil" pada TC tidak dapat diasersi atas seluruh tabel karena baris Pre-setup bernama sama ikut ada di entitas Principal.
  - TC-316 menyebut "DS-UL berisi lebih dari 10 user" tanpa jumlah; spec membaca jumlah total entitas (N) lewat Fixture BE.
  - TC-661 precondition c merujuk "TC-AC-SU-26"; spec menyalin tree dari Langkah TC-26 (S-04).
- Pembagian TC lintas spec: TC-317 dan TC-661 juga ada di `sourceTc` spec 089. Spec ini mengasersi nama berkas, kolom, dan jumlah baris; spec 089 mengasersi identitas dan keanggotaan baris di dalam berkas (kelas f).
