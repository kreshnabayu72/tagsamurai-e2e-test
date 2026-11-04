---
id: TC-AC-SU-E2E-031-seleksi-checkbox-header-select-all-unselect-dan-uncheck-baris
title: "Seleksi Checkbox: Checkbox Header, Select All Lintas Halaman, Unselect All, dan Uncheck Satu Baris"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-110
  - TC-AC-SU-111
  - TC-AC-SU-112
coverage:
  web: automated
---

# Seleksi Checkbox: Checkbox Header, Select All Lintas Halaman, Unselect All, dan Uncheck Satu Baris

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-111, 112 | (user generik, TC tidak menyebut nama) | `User Seleksi 01 {runId}-031` sampai `User Seleksi 12 {runId}-031` | `userseleksiNN+{runId}-031@qwertysystem.net` | 12 user Activated, Active (eligible); ≥12 user, page size 10 |

- TC-AC-SU-110 memakai akun aktor Pre-setup (Search atas `AdminConsole_automated_{namaCompany}` menampilkan Default User, baris aktor sendiri, dan akun aktor lain pada satu halaman); tidak ada data dinamis untuk blok itu dan data Pre-setup tidak diubah. N dari seeding: N = 12 untuk Search atas suffix spec (bagian 8b butir 10).
- Seeding di hook `before`, penghapusan data milik spec di hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-110: Checkbox header, select all halaman, indeterminate, deselect

1. Ketik Search `AdminConsole_automated_{namaCompany}`, tekan Enter
2. Centang 1 baris selain Default User dan baris aktor sendiri
3. Amati checkbox header
4. Verifikasi checkbox header Indeterminate `[-]`
5. Verifikasi counter `1 User selected`
6. Klik checkbox header
7. Verifikasi semua baris ber-checkbox enabled di halaman aktif checked
8. Verifikasi baris Default User dan baris aktor sendiri tetap unchecked dan disabled
9. Klik checkbox header lagi
10. Verifikasi semua baris unchecked
11. Verifikasi Bulk Action Bar hilang

### TC-AC-SU-111: Select All ([N] records) lintas halaman lalu Unselect All

12. Ganti isi kotak search dengan `{runId}-031`, tekan Enter
13. Centang 1 baris
14. Klik `[Select All (12 records)]`
15. Verifikasi semua baris eligible lintas halaman terseleksi
16. Verifikasi counter `12 Users selected`
17. Verifikasi tombol berubah menjadi `[Unselect All]`
18. Pindah ke halaman 2
19. Verifikasi baris halaman 2 tetap checked
20. Klik `[Unselect All]`
21. Verifikasi seleksi kosong
22. Verifikasi Bulk Action Bar tertutup

### TC-AC-SU-112: Uncheck 1 baris dari kondisi 100% terseleksi, tombol kembali Select All

23. Kembali ke halaman 1
24. Centang 1 baris
25. Klik `[Select All (12 records)]`
26. Batalkan centang 1 baris
27. Verifikasi Bulk Action Bar tetap tampil
28. Verifikasi tombol kembali `[Select All (12 records)]`
29. Verifikasi counter `11 Users selected` (N - 1)
30. Klik icon `×` pada Bulk Action Bar untuk membatalkan seleksi
31. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 dan 12 (Search untuk membatasi baris, R-16; 1 memunculkan akun aktor Pre-setup termasuk Default User dan self), langkah 23 (kembali ke halaman 1 karena TC-AC-SU-111 berakhir di halaman 2), langkah 24 (centang 1 baris agar `[Select All (12 records)]` tampil; seleksi TC-AC-SU-111 sudah dibatalkan di langkah 20 dan Bulk Action Bar tertutup), langkah 30 dan 31 (batalkan seleksi dan reset Search, S-09).
- Temuan untuk QA:
  - TC-AC-SU-110 butir b menuntut baris Default User dan self terlihat pada halaman aktif; spec membatasi tabel dengan Search atas email akun aktor Pre-setup supaya kedua baris tampil, bukan dengan 12 user seed.
  - TC-AC-SU-111 dan TC-AC-SU-112 menyebut "≥12 user" tanpa nama; spec men-seed 12 user generik bersuffix (N = 12) dan memakai Search atas suffix.
  - Nama user generik `User Seleksi NN` dipilih penulis karena TC tidak menyebut nama.
