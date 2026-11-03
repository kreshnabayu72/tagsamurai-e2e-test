---
id: TC-AC-SU-E2E-104-tab-changelog-sort
title: "Tab Changelog: Sort 3-state Kelas Teks, Campuran, dan Tanggal"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-374
  - TC-AC-SU-375
  - TC-AC-SU-376
coverage:
  web: automated
---

# Tab Changelog: Sort 3-state Kelas Teks, Campuran, dan Tanggal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal), `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Suite berjalan serial (`parallel: false`). Flag Guided Tooltip disetel `seen` oleh hook suite; sesi API aktor dan Fixture BE disediakan tim FE/BE (lihat `suite.md`). Spec tidak memakai endpoint karangan.
- General Settings (Date Format, Time Format, Time Zone) entitas Principal tidak diubah spec ini; format tanggal yang diasersi dibaca dari General Settings tersebut.
- Data seeding (Fixture BE): user `Jane Smith {runId}-104` (email `janesmith+{runId}-104@qwertysystem.net`) dengan 6 entri Changelog (Date berbeda, urutan seeding dari tertua R1 ke terbaru R6; semua pada satu halaman):

| Entri | Action | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|
| R1 | Assign | Manage group | Inactive | Assigned | Admin U |
| R2 | Edit | Manage group | 9 | 7 | Budi S |
| R3 | Remove | Access Level | 2 | — | Admin U |
| R4 | Activate | Status | — | 4 | Cici A |
| R5 | Remove | Manage group | Active | Inactive | Budi S |
| R6 | Edit | Activation Email | Inactive | Active | Cici A |

- Kolom sort kelas teks (TC-374): `Action` (A–Z: Activate, Assign, Edit, Remove), `Field` (A–Z: Access Level, Activation Email, Manage group, Status), `Modified By` (A–Z: Admin U, Budi S, Cici A).
- Kolom sort kelas campuran (TC-375): `Old Value` (naik: 2, 9, Active, Inactive, —) dan `New Value` (naik: 4, 7, Active, Assigned, Inactive, —).
- Kemampuan teknis: kemampuan seed entri Changelog dengan Date dan pelaku tertentu disediakan tim FE/BE.
- Hook `before` men-seed data milik spec ini lewat Fixture BE; hook `after` menghapus user seeding di atas lewat Fixture BE. Entri audit trail yang dibuat sistem tidak dihapus. Fixture `settingsUser` (berkas belum ada; dibuat tim FE) menyimpan nama dan email user seeding; password tidak disimpan di fixture.

## Test Steps

### TC-AC-SU-374: Sort 3-state kelas teks

1. Cari `Jane Smith {runId}-104` di Search pada User List, tekan Enter, lalu buka Detail user tersebut
2. Klik tab `Changelog`
3. Klik header kolom pada baris tabel 'Kolom sort kelas teks'
4. Verifikasi urutan baris A–Z menurut nilai seeding kolom itu
5. Verifikasi ikon sort `↑` tampil
6. Klik header kolom yang sama untuk kedua kalinya
7. Verifikasi urutan baris Z–A menurut nilai seeding kolom itu
8. Verifikasi ikon sort `↓` tampil
9. Klik header kolom yang sama untuk ketiga kalinya
10. Verifikasi urutan baris kembali ke sort default (Date Newest First)

### TC-AC-SU-375: Sort 3-state kelas campuran

11. Klik header kolom pada baris tabel 'Kolom sort kelas campuran'
12. Verifikasi nilai numerik tampil lebih dulu lalu nilai teks
13. Verifikasi nilai kosong `—` berada di akhir
14. Verifikasi ikon sort `↑` tampil
15. Klik header kolom yang sama untuk kedua kalinya
16. Verifikasi urutan kebalikannya dengan nilai kosong `—` berada di awal
17. Verifikasi ikon sort `↓` tampil
18. Klik header kolom yang sama untuk ketiga kalinya
19. Verifikasi urutan baris kembali ke sort default (Date Newest First)

### TC-AC-SU-376: Sort 3-state kelas tanggal

20. Klik header `Date` untuk pertama kalinya
21. Verifikasi urutan baris Oldest First
22. Verifikasi ikon sort `↑` tampil
23. Klik header `Date` untuk kedua kalinya
24. Verifikasi urutan baris Newest First
25. Verifikasi ikon sort `↓` tampil
26. Klik header `Date` untuk ketiga kalinya
27. Verifikasi urutan baris kembali ke sort default (Date Newest First)

## Notes

- Langkah pembuka yang mencari user target lewat Search pada User List lalu membuka Detail adalah langkah penghubung (R-16, S-03); kotak Search User List tidak dipakai sebagai objek uji.
- Langkah klik header kolom dilakukan per baris pada tabel Prerequisites ('Kolom sort kelas teks' dan 'Kolom sort kelas campuran'): langkah 3 sampai 10 (3 kolom) dan langkah 11 sampai 19 (2 kolom). Klik ketiga tiap kolom mengembalikan sort ke default sehingga kolom berikutnya mulai dari keadaan yang sama (S-09).
- Temuan untuk QA:
  - Pada TC-376 klik 2 (Newest First) dan klik 3 (kembali ke sort default Date Newest First) menghasilkan urutan baris yang sama; pembeda keadaan header (ikon sort) pada klik 3 tidak dinyatakan. Spec hanya mengasersi urutan baris pada klik 3.
  - Tie-breaker antara dua entri bernilai sama pada kolom yang di-sort tidak dinyatakan di TC; spec mengasersi urutan nilai distinct, bukan urutan antar-baris bernilai sama.
  - Pelaku `Admin U` (nama lengkap `Admin Utama`) tidak terpetakan ke akun mana pun di Tabel Data Uji Pre-setup (#1-#7 hanya email aktor, #8 hanya target user). Spec memakai pelaku seeding bernama depan `Admin` dan belakang `Utama`; suffix `{runId}` ditaruh di email pelaku, bukan di nama, karena format Modified By [First Name] [Last Initial] tidak dapat memuat suffix.
  - Cara men-seed entri audit trail (Date, Action, Field, Old Value, New Value, pelaku) tidak dinyatakan di TC, PRD, atau LLD; kemampuan ini ditulis 'disediakan tim FE/BE' tanpa endpoint karangan (S-13).
  - Nama target `Jane Smith` pada TC dipakai sebagai nama bersuffix `Jane Smith {runId}-NNN` per run (S-12); asersi spec memakai nilai kolom log, bukan urutan atau Search atas nama user.
- Spec ini melewati sekitar 35 langkah (27 langkah nominal, sekitar 52 dengan ekspansi blok berulang). Alasan pertahanan: seluruh blok berada pada satu permukaan, satu kelas harness (fungsional biasa), memakai dataset seeding yang sama, dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
