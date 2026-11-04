---
id: TC-AC-SU-E2E-105-tab-changelog-search-siklus-dan-per-kolom
title: "Tab Changelog: Siklus Search Box dan Search per Kolom Teks"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-378
  - TC-AC-SU-379
coverage:
  web: automated
---

# Tab Changelog: Siklus Search Box dan Search per Kolom Teks

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal), `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Suite berjalan serial (`parallel: false`). Flag Guided Tooltip disetel `seen` oleh hook suite; sesi API aktor dan Fixture BE disediakan tim FE/BE (lihat `suite.md`). Spec tidak memakai endpoint karangan.
- General Settings (Date Format, Time Format, Time Zone) entitas Principal tidak diubah spec ini; format tanggal yang diasersi dibaca dari General Settings tersebut.
- Data seeding (Fixture BE): user `Jane Smith {runId}-105` (email `janesmith+{runId}-105@qwertysystem.net`) dengan 3 entri Changelog: (1) Action `Assign`, Field `Manage group`, Old Value `Inactive`, New Value `Assigned`, Modified By `Admin U`; (2) Action `Edit`, Field `Status`, Old Value `9`, New Value `7`, Modified By `Budi S`; (3) Action `Remove`, Field `Access Level`, Old Value `2`, New Value `—`, Modified By `Cici A`. Keyword `Assign` (TC-378) hanya memuat entri (1).

| Search per kolom | Keyword huruf kecil | Keyword huruf kapital | Nilai yang cocok |
|---|---|---|---|
| Action | `assi` | `ASSI` | `Assign` |
| Field | `manage gr` | `MANAGE GR` | `Manage group` |
| Old Value | `inact` | `INACT` | `Inactive` |
| New Value | `assig` | `ASSIG` | `Assigned` |
| Modified By | `admin` | `ADMIN` | `Admin U` |

- Kemampuan teknis: kemampuan seed entri Changelog disediakan tim FE/BE.
- Hook `before` men-seed data milik spec ini lewat Fixture BE; hook `after` menghapus user seeding di atas lewat Fixture BE. Entri audit trail yang dibuat sistem tidak dihapus. Fixture `settingsUser` (berkas belum ada; dibuat tim FE) menyimpan nama dan email user seeding; password tidak disimpan di fixture.

## Test Steps

### TC-AC-SU-378: Siklus interaksi Search box Tab Changelog

1. Ketik Search `Jane Smith {runId}-105`, tekan Enter
2. Klik Name `Jane Smith {runId}-105`
3. Klik tab `Changelog`
4. Hover icon Search
5. Verifikasi tooltip `Search` tampil
6. Klik icon Search
7. Verifikasi input Search melebar
8. Verifikasi kursor auto-focus di input Search
9. Verifikasi placeholder input Search `Search action, field, or value...`
10. Catat jumlah baris tabel Changelog
11. Ketik `Assign` di input Search tanpa menekan Enter
12. Verifikasi icon `(✕)` muncul
13. Verifikasi tabel belum tersaring (jumlah baris sama dengan jumlah yang dicatat sebelum mengetik)
14. Tekan Enter
15. Verifikasi sedikitnya satu baris tampil
16. Verifikasi setiap baris yang tampil memuat `Assign`
17. Klik icon `(✕)`
18. Verifikasi input Search kosong
19. Verifikasi search bar tetap terbuka
20. Verifikasi tabel tetap menampilkan hasil search terakhir
21. Tekan Enter pada input kosong
22. Verifikasi tabel kembali menampilkan semua data (jumlah baris sama dengan jumlah yang dicatat)
23. Ketik Search `Assign`, tekan Enter
24. Klik icon `(←)`
25. Verifikasi search bar collapse ke icon
26. Verifikasi keyword Search kosong
27. Verifikasi tabel langsung kembali menampilkan semua data

### TC-AC-SU-379: Search Tab Changelog per kolom kelas teks

28. Untuk setiap baris tabel "Search per kolom" di Prerequisites, lakukan langkah 29 sampai 33
29. Ketik Search keyword huruf kecil pada baris tabel 'Search per kolom', tekan Enter
30. Verifikasi tabel menampilkan baris yang memuat nilai pada kolom 'Nilai yang cocok' baris tabel itu
31. Ganti isi kotak Search dengan keyword huruf kapital pada baris tabel yang sama, tekan Enter
32. Verifikasi tabel menampilkan baris yang memuat nilai pada kolom 'Nilai yang cocok' baris tabel itu
33. Klik icon `(←)` pada kotak Search

## Notes

- Langkah 1 dan 2 (Ketik Search nama user target, lalu Klik Name untuk membuka Detail) adalah langkah penghubung (R-16, S-03); kotak Search User List tidak dipakai sebagai objek uji.
- Langkah Search per kolom diulang per baris tabel 'Search per kolom': langkah 29 sampai 33 (5 kolom, tiap kolom dua keyword).
- Klik `(←)` pada akhir tiap iterasi menutup dan mengosongkan Search sehingga iterasi berikutnya mulai dari kotak kosong; langkah itu adalah langkah penghubung, sedangkan Verifikasi tiap iterasi mengasersi baris yang memuat nilai kolom itu tampil.
- Temuan untuk QA:
  - Search diterapkan pada seluruh kolom searchable, sehingga keyword seperti `assi` juga dapat cocok dengan kolom lain (New Value `Assigned`); TC tidak menyatakan apakah hasil harus hanya dari kolom yang disebut. Spec hanya mengasersi bahwa baris yang memuat nilai kolom itu tampil.
  - Pelaku `Admin U` (nama lengkap `Admin Utama`) tidak terpetakan ke akun mana pun di Tabel Data Uji Pre-setup (#1-#7 hanya email aktor, #8 hanya target user). Spec memakai pelaku seeding bernama depan `Admin` dan belakang `Utama`; suffix `{runId}` ditaruh di email pelaku, bukan di nama, karena format Modified By [First Name] [Last Initial] tidak dapat memuat suffix.
  - Cara men-seed entri audit trail (Date, Action, Field, Old Value, New Value, pelaku) tidak dinyatakan di TC, PRD, atau LLD; kemampuan ini ditulis 'disediakan tim FE/BE' tanpa endpoint karangan (S-13).
  - Nama target `Jane Smith` pada TC dipakai sebagai nama bersuffix `Jane Smith {runId}-NNN` per run (S-12); asersi spec memakai nilai kolom log, bukan urutan atau Search atas nama user.
- Spec ini melewati sekitar 35 langkah (33 langkah nominal, sekitar 53 dengan ekspansi blok berulang). Alasan pertahanan: seluruh blok berada pada satu permukaan, satu kelas harness (fungsional biasa), memakai dataset seeding yang sama, dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
