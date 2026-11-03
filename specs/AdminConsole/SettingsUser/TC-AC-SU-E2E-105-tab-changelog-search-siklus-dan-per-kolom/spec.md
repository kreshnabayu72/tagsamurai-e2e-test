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

1. Cari `Jane Smith {runId}-105` di Search pada User List, tekan Enter, lalu buka Detail user tersebut
2. Klik tab `Changelog`
3. Hover icon Search
4. Verifikasi tooltip `Search` tampil
5. Klik icon Search
6. Verifikasi input Search melebar
7. Verifikasi kursor auto-focus di input Search
8. Verifikasi placeholder input Search `Search action, field, or value...`
9. Ketik `Assign` di input Search tanpa menekan Enter
10. Verifikasi icon `(✕)` muncul
11. Verifikasi tabel belum tersaring (jumlah baris sama dengan sebelum mengetik)
12. Tekan Enter
13. Verifikasi sedikitnya satu baris tampil
14. Verifikasi setiap baris yang tampil memuat `Assign`
15. Klik icon `(✕)`
16. Verifikasi input Search kosong
17. Verifikasi search bar tetap terbuka
18. Verifikasi tabel tetap menampilkan hasil search terakhir
19. Tekan Enter pada input kosong
20. Verifikasi tabel kembali menampilkan semua data (jumlah baris sama dengan sebelum Search)
21. Ketik Search `Assign`, tekan Enter
22. Klik icon `(←)`
23. Verifikasi search bar collapse ke icon
24. Verifikasi keyword Search kosong
25. Verifikasi tabel langsung kembali menampilkan semua data

### TC-AC-SU-379: Search Tab Changelog per kolom kelas teks

26. Klik icon Search
27. Ganti isi kotak Search dengan keyword huruf kecil pada baris tabel 'Search per kolom', tekan Enter
28. Verifikasi tabel menampilkan baris yang memuat nilai pada kolom 'Nilai yang cocok' baris tabel itu
29. Ganti isi kotak Search dengan keyword huruf kapital pada baris tabel yang sama, tekan Enter
30. Verifikasi tabel menampilkan baris yang memuat nilai pada kolom 'Nilai yang cocok' baris tabel itu
31. Klik icon `(←)` pada kotak Search

## Notes

- Langkah pembuka yang mencari user target lewat Search pada User List lalu membuka Detail adalah langkah penghubung (R-16, S-03); kotak Search User List tidak dipakai sebagai objek uji.
- Langkah Search per kolom diulang per baris tabel 'Search per kolom': langkah 27 sampai 30 (5 kolom, tiap kolom dua keyword). Search tidak dibersihkan antar-iterasi karena iterasi berikutnya mengganti isi kotak.
- Klik icon Search sebelum iterasi pertama dan klik `(←)` sesudah iterasi terakhir adalah langkah penghubung; Verifikasi tiap iterasi mengasersi baris yang memuat nilai kolom itu tampil.
- Temuan untuk QA:
  - Search diterapkan pada seluruh kolom searchable, sehingga keyword seperti `assi` juga dapat cocok dengan kolom lain (New Value `Assigned`); TC tidak menyatakan apakah hasil harus hanya dari kolom yang disebut. Spec hanya mengasersi bahwa baris yang memuat nilai kolom itu tampil.
  - Pelaku `Admin U` (nama lengkap `Admin Utama`) tidak terpetakan ke akun mana pun di Tabel Data Uji Pre-setup (#1-#7 hanya email aktor, #8 hanya target user). Spec memakai pelaku seeding bernama depan `Admin` dan belakang `Utama`; suffix `{runId}` ditaruh di email pelaku, bukan di nama, karena format Modified By [First Name] [Last Initial] tidak dapat memuat suffix.
  - Cara men-seed entri audit trail (Date, Action, Field, Old Value, New Value, pelaku) tidak dinyatakan di TC, PRD, atau LLD; kemampuan ini ditulis 'disediakan tim FE/BE' tanpa endpoint karangan (S-13).
  - Nama target `Jane Smith` pada TC dipakai sebagai nama bersuffix `Jane Smith {runId}-NNN` per run (S-12); asersi spec memakai nilai kolom log, bukan urutan atau Search atas nama user.
- Spec ini melewati sekitar 35 langkah (31 langkah nominal, sekitar 47 dengan ekspansi blok berulang). Alasan pertahanan: seluruh blok berada pada satu permukaan, satu kelas harness (fungsional biasa), memakai dataset seeding yang sama, dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
