---
id: TC-AC-SU-E2E-074-user-list-search-siklus-box-dan-kelas-teks
title: "User List Search: Siklus Interaksi Search Box dan Search Kelas Teks"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-263
  - TC-AC-SU-264
coverage:
  web: automated
---

# User List Search: Siklus Interaksi Search Box dan Search Kelas Teks

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` dan kemampuan Fixture BE mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (di-seed hook `before` lewat Fixture BE, entitas Principal; nama bersuffix `{runId}-074`): `John Doe {runId}-074`, `Jane Smith {runId}-074` (Position `Finance Manager`, Division `Finance`), `Mike Tan {runId}-074` (Email `mike.tan@{runId}-074.qwertysystem.net`, Division `IT Operations`), `Sarah Lee {runId}-074` (Employee ID `EMP-004-{runId}-074`, tanpa Position), `Rudi Hartono {runId}-074` (TAG `E2801{runId}`). Nilai kolom lain pada tiap user tidak memuat keyword uji milik user lain. Kolom TAG diisi lewat seeding TAG yang sudah paired (disediakan tim FE/BE).
- Tabel keyword TC-264 (parameter langkah 27 sampai 30):
| No | Kolom | Keyword | Baris yang tampil | Baris pembanding yang tidak tampil |
|---|---|---|---|---|
| 1 | Name | `JANE` | `Jane Smith {runId}-074` | `Mike Tan {runId}-074` |
| 2 | Email | `mike.tan@` | `Mike Tan {runId}-074` | `Jane Smith {runId}-074` |
| 3 | Position | `finance man` | `Jane Smith {runId}-074` | `Mike Tan {runId}-074` |
| 4 | Division | `operat` | `Mike Tan {runId}-074` | `Jane Smith {runId}-074` |
| 5 | Employee ID | `emp-004` | `Sarah Lee {runId}-074` | `Jane Smith {runId}-074` |
| 6 | TAG | `E2801` | `Rudi Hartono {runId}-074` | `Jane Smith {runId}-074` |
- Hook `after` menghapus data yang di-seed hook `before` spec ini lewat Fixture BE; pembersihan tidak berasumsi seeding berhasil penuh.
- Pemulihan Setup Column: preferensi kolom yang disimpan spec ini dihapus di hook `after` dengan menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan ini disediakan tim FE.

## Test Steps

### TC-AC-SU-263: Siklus interaksi Search box User List (reveal, ketik, Enter, ✕, ←)

1. Hover icon Search di toolbar
2. Verifikasi tooltip `Search` tampil
3. Klik icon Search
4. Verifikasi input search terbuka dengan kursor auto-focus
5. Verifikasi placeholder input search `Search by name, position, division...`
6. Ketik `john` tanpa menekan Enter
7. Verifikasi icon ✕ muncul di sisi kanan input
8. Verifikasi tabel belum tersaring: baris `Jane Smith {runId}-074` masih tampil
9. Tekan Enter
10. Verifikasi baris `John Doe {runId}-074` tampil
11. Verifikasi baris `Jane Smith {runId}-074` dan `Mike Tan {runId}-074` tidak tampil
12. Klik icon ✕ di input
13. Verifikasi input kosong
14. Verifikasi input tetap terbuka dan fokus
15. Verifikasi tabel tetap menampilkan hasil `john` (baris `John Doe {runId}-074` tampil, baris `Jane Smith {runId}-074` tidak tampil)
16. Tekan Enter pada input kosong
17. Verifikasi tabel kembali menampilkan seluruh baris DS-UL (baris `John Doe {runId}-074` dan `Jane Smith {runId}-074` tampil)
18. Ketik Search `john`, tekan Enter
19. Klik icon ← di kiri input
20. Verifikasi input menutup menjadi icon Search dengan keyword kosong
21. Verifikasi tabel langsung kembali ke seluruh baris (baris `John Doe {runId}-074` dan `Jane Smith {runId}-074` tampil)

### TC-AC-SU-264: Search kelas teks (Name, Email, Position, Division, Employee ID, TAG), partial dan case-insensitive

22. Klik `⋯` pada header Actions
23. Klik `[Setup Column]`
24. Centang kolom `TAG` pada Setup Column
25. Klik `[Save]`
26. Klik icon Search
27. Ketik Search sesuai kolom Keyword pada tabel keyword TC-264, tekan Enter
28. Verifikasi baris pada kolom "Baris yang tampil" tabel keyword TC-264 tampil di tabel
29. Verifikasi baris pada kolom "Baris pembanding" tabel keyword TC-264 tidak tampil
30. Klik `✕` pada Search, tekan Enter
31. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03): klik `(←)` pada kotak Search di akhir spec menutup input dan mereset tabel; langkah Setup Column (TC-264 langkah 1) menyimpan konfigurasi kolom yang dipulihkan hook `after`.
- Langkah 27 sampai 30 diulang untuk tiap baris tabel keyword TC-264 (8b butir 7); parameter ada di Prerequisites, `Verifikasi` tetap satu per klausa.
- Alasan di atas ±35 langkah (ekspansi): kedua TC sama-sama Search User List di dataset yang sama, berdiri sendiri, dan kegagalan satu TC tidak membuat TC lain kehilangan makna.
- Temuan untuk QA:
  - TC menulis nama data DS-UL secara literal (nama user, email, position, division). Spec memakai nama bersuffix ` {runId}-074` (S-12) dan mengasersi baris milik spec; klaim "hanya X yang tampil" pada TC tidak dapat diasersi atas seluruh tabel karena baris Pre-setup bernama sama ikut ada di entitas Principal.
  - TC-264 menulis keyword Email `mike.tan@`; spec men-seed Email bersuffix pada domain (`@{runId}-074.qwertysystem.net`) agar keyword TC tetap cocok tanpa diubah.
  - TC-263 langkah 3 menyebut icon ✕ muncul, sedangkan tabel belum tersaring tanpa baris pembanding; spec memakai baris `Jane Smith {runId}-074` sebagai pembanding (milik spec).
