---
id: TC-AC-SU-E2E-089-user-list-download-isi-berkas-per-tipe-kolom
title: "User List Download: Isi Berkas XLSX (Nilai Sel per Tipe Kolom dan Keanggotaan Baris, Binary Buffer)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-319
  - TC-AC-SU-317
  - TC-AC-SU-661
coverage:
  web: automated
---

# User List Download: Isi Berkas XLSX (Nilai Sel per Tipe Kolom dan Keanggotaan Baris, Binary Buffer)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` dan kemampuan Fixture BE mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (di-seed hook `before` lewat Fixture BE; nama bersuffix `{runId}-089`): group tree `Region A {runId}-089` > `Branch 1 {runId}-089` > `Floor 1 {runId}-089`; `Region A {runId}-089` > `Branch 3 {runId}-089`; `Region B {runId}-089`. User: `Jane Smith {runId}-089` (Inactive, 2 role aktif, dengan foto, Group Role aktif di `Floor 1 {runId}-089`), `Mike Tan {runId}-089` (Active, Group Role aktif di `Branch 3 {runId}-089`), `Rudi Hartono {runId}-089` (hanya Global Role), `Sarah Lee {runId}-089` (tanpa Position, Employee ID, dan TAG; Pending Activation; Temporary User `No`; Group Role tanpa group assignment), `Dedi Kurnia {runId}-089` (Group Manager `Region A {runId}-089`), `Dewi Lestari {runId}-089` (Total Control) dan `Rina Putri {runId}-089` (Total Control), `Andi Wijaya {runId}-089` (Read Only, Temporary User `Yes`, TAG `E2801{runId}`), `John Doe {runId}-089` (Group Role aktif di `Region B {runId}-089`, Active). Baris Default User Principal (Pre-setup #1, Total Control permanen) dipakai apa adanya.
- General Settings Date Format dan Time Format mengikuti nilai entitas (tidak diubah); nilai pembanding Last Updated dibaca dari tampilan tabel.
- Kemampuan teknis: membaca isi berkas XLSX (nilai sel, tipe sel, dan keanggotaan baris) dan menghapus preferensi kolom di browser, disediakan tim FE.
- Hook `after` menghapus data yang di-seed hook `before` spec ini lewat Fixture BE; pembersihan tidak berasumsi seeding berhasil penuh.
- Pemulihan Setup Column: preferensi kolom yang disimpan spec ini dihapus di hook `after` dengan menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan ini disediakan tim FE.

## Test Steps

### TC-AC-SU-319: Transformasi data Download per tipe kolom

1. Klik `⋯` pada header Actions
2. Klik `[Setup Column]`
3. Centang kolom Activation Status, Temporary User, dan TAG pada Setup Column
4. Klik `[Save]`
5. Klik icon Download, klik `Download as XLSX`
6. Buka berkas `User.xlsx`
7. Verifikasi kolom Active baris `Jane Smith {runId}-089` berisi `Inactive`
8. Verifikasi kolom Name baris `Jane Smith {runId}-089` berisi teks nama tanpa foto atau avatar
9. Verifikasi kolom Role baris `Jane Smith {runId}-089` berisi `2 roles` dan baris `Dewi Lestari {runId}-089` berisi `Total Control`
10. Verifikasi kolom Activation Status baris `Sarah Lee {runId}-089` dan kolom Temporary User baris `Andi Wijaya {runId}-089` berisi label badge tanpa warna
11. Verifikasi sel kosong baris `Sarah Lee {runId}-089` (Position, Employee ID, TAG yang `—` di tabel) berisi `-`
12. Verifikasi kolom Last Updated memakai format tanggal dan jam General Settings

### TC-AC-SU-317: Download XLSX mengikuti Search dan Filter aktif

13. Klik icon Filter
14. Pilih Status `Active`, klik `[Apply]`
15. Klik icon Search, ketik Search `Doe`, tekan Enter
16. Klik icon Download, klik `Download as XLSX`
17. Verifikasi tidak ada toast sukses
18. Verifikasi berkas `User.xlsx` terunduh
19. Verifikasi `User.xlsx` memuat baris `John Doe {runId}-089` (Active, cocok Search)
20. Verifikasi `User.xlsx` tidak memuat baris `Mike Tan {runId}-089` (Active, tidak cocok Search)
21. Klik `(←)` pada kotak Search
22. Klik icon Filter
23. Klik `[Clear Field]`, klik `[Apply]`

### TC-AC-SU-661: Download User List mengikuti node Sidebar Group yang aktif

24. Klik node `Region A {runId}-089` di Sidebar Group
25. Klik icon Download, klik `Download as XLSX`
26. Verifikasi tidak ada toast sukses
27. Verifikasi berkas `User.xlsx` terunduh
28. Verifikasi `User.xlsx` hanya memuat user dalam `Region A {runId}-089` dan descendant-nya: `Jane Smith {runId}-089`, `Mike Tan {runId}-089`, `Dedi Kurnia {runId}-089`, `Dewi Lestari {runId}-089`, `Rina Putri {runId}-089`, `Andi Wijaya {runId}-089`, dan Default User
29. Verifikasi `User.xlsx` tidak memuat `Rudi Hartono {runId}-089`, `Sarah Lee {runId}-089`, dan `John Doe {runId}-089`
30. Klik node `Region A {runId}-089` agar ter-deselect

## Notes

- Berkas XLSX diasersi pada nilai sel, tipe sel, dan keanggotaan baris (kelas f); spec ini satu-satunya yang menilai isi berkas Download User List. Spec 088 menjalankan alur Download yang sama dan hanya menilai nama berkas, kolom, dan jumlah baris.
- Langkah penghubung (S-03, S-09): `(←)`, `[Clear Field]` lalu `[Apply]`, dan men-deselect node mengembalikan state List di antara TC.
- Asersi tidak ada toast sukses diletakkan tepat setelah klik Download dan sebelum Verifikasi berkas (bagian 8b butir 11).
- Langkah Setup Column menampilkan kolom curated sebelum Download (langkah 1 TC); konfigurasi kolom dipulihkan hook `after`.
- Temuan untuk QA:
  - TC-661 precondition c merujuk "TC-AC-SU-26"; spec menyalin tree dari Langkah TC-26 (S-04).
  - TC menulis nama data DS-UL secara literal (nama user, email, position, division). Spec memakai nama bersuffix ` {runId}-089` (S-12) dan mengasersi baris milik spec; klaim "hanya X yang tampil" pada TC tidak dapat diasersi atas seluruh tabel karena baris Pre-setup bernama sama ikut ada di entitas Principal.
  - TC-317 memakai Search `Doe`; spec memakai `John Doe {runId}-089` (Active, cocok Search) sebagai baris yang harus ada dan `Mike Tan {runId}-089` (Active, tidak cocok Search) sebagai baris yang harus tidak ada. Sisi Filter belum terdiskriminasi karena seed tidak punya user non-Active yang cocok `Doe`.
  - TC-319 tidak menyebut baris mana yang dibaca; spec membaca baris milik spec (`Jane Smith {runId}-089`, `Dewi Lestari {runId}-089`, `Sarah Lee {runId}-089`, `Andi Wijaya {runId}-089`).
- Pembagian TC lintas spec: TC-317 dan TC-661 juga ada di `sourceTc` spec 088. Spec ini mengasersi identitas dan keanggotaan baris di dalam berkas (kelas f); spec 088 mengasersi nama berkas, kolom, dan jumlah baris.
