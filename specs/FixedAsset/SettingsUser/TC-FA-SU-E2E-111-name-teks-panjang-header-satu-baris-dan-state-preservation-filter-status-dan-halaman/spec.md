---
id: TC-FA-SU-E2E-111-name-teks-panjang-header-satu-baris-dan-state-preservation-filter-status-dan-halaman
title: "Name Teks Panjang, Header Satu Baris, dan State Preservation Filter Status dan Halaman"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1051
  - TC-FA-SU-1052
  - TC-FA-SU-1057
coverage:
  web: automated
---

# Name Teks Panjang, Header Satu Baris, dan State Preservation Filter Status dan Halaman

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20, plan Enterprise, 25 pengguna). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fa-settings-user.<kunci>` (berkas `fixtures/fa-settings-user.json` belum ada dan disediakan tim FE).
- Spec ini hanya membaca data Pre-setup dan tidak mengubahnya; suite berjalan serial (`parallel: false`).
- Data Pre-setup tambahan: identitas (#42) berisi pengguna ber-Name `Muhammad Abdurrahman Al-Fatih Prasetyo Nugraha Wijaya Kusuma`; atribut User List (#43). Filter Status `Active` menyisakan 21 pengguna (halaman 1 berisi 10, halaman 2 berisi 10, halaman 3 berisi 1); Doni Prasetyo, Fajar Nugroho, Kartika Sari, dan Lukman Hakim berstatus Inactive.
- Preferensi kolom User List (Setup Column) dihapus di browser pada hook `before` dan `after` spec ini (kemampuan disediakan tim FE, bagian 4 konvensi), bukan lewat `[Reset to Default]`.

## Test Steps

### TC-FA-SU-1051: Name teks datar sangat panjang

1. Ketik Search `Muhammad Abdurrahman Al-Fatih Prasetyo Nugraha Wijaya Kusuma`, tekan Enter
2. Verifikasi Name tampil utuh tanpa pemotongan `..`
3. Verifikasi kolom Name melebar mengikuti konten
4. Hover sel Name baris tersebut
5. Verifikasi tidak ada tooltip pada sel Name
6. Verifikasi kolom single-value standar (tanggal, badge atau status, kode) tidak wrap
7. Klik `(←)` pada kotak Search
8. Verifikasi tabel menampilkan sedikitnya satu baris
9. Verifikasi tinggi baris konsisten di semua baris

### TC-FA-SU-1057: State preservation Filter Status dan halaman aktif

10. Klik ikon Filter, buka dropdown Status, centang `Active`
11. Klik `[Apply]`
12. Verifikasi Filter Status `Active` menyisakan 21 pengguna (tiga halaman: 10, 10, 1)
13. Verifikasi `Doni Prasetyo`, `Fajar Nugroho`, dan `Kartika Sari` tidak tampil di halaman 1
14. Pindah ke halaman 2
15. Verifikasi `Lukman Hakim` tidak tampil di halaman 2
16. Klik nama pengguna pertama di halaman 2
17. Klik breadcrumb `User`
18. Verifikasi Filter Status `Active` dipulihkan setelah Back dari Detail
19. Verifikasi halaman aktif 2 dipulihkan setelah Back dari Detail
20. Tekan F5
21. Verifikasi Filter Status `Active` dipulihkan setelah refresh
22. Verifikasi halaman aktif 2 dipulihkan setelah refresh
23. Klik `[Clear Field]` lalu `[Apply]` pada panel Filter

### TC-FA-SU-1052: Header kolom tetap satu baris

24. Klik header kolom Actions (⋯), klik `Setup Column...`
25. Centang `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, dan `Shift`, klik `[Save]`
26. Verifikasi header `Activation Status`, `Temporary User`, `Temporary Until`, dan `Last Updated` tampil satu baris dengan tinggi header tetap tanpa wrap
27. Hover header `Temporary Until`
28. Verifikasi label header yang tidak muat dipotong dengan tooltip penuh `Temporary Until`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 1 (Search untuk menemukan baris target, R-16), 7 (menutup Search), 23 (membersihkan Filter, S-09), 24 dan 25 (menampilkan kolom curated lewat Setup Column).
- Urutan TC diubah: TC-FA-SU-1052 diletakkan terakhir karena menyimpan konfigurasi kolom; urutan TC-FA-SU-1057 tidak bergantung pada kolom curated (S-10).
- Temuan untuk QA (S-15): (1) TC-FA-SU-1052 Expected b tidak menyebut header mana yang tidak muat; spec meng-hover `Temporary Until` dan menganggap labelnya terpotong, sehingga asersi tooltip bergantung pada lebar viewport (S-14). (2) TC-FA-SU-1051 tidak menyebut cara mengukur tinggi baris; spec mengasersi hasil tinggi konsisten tanpa angka piksel.
