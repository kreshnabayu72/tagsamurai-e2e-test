---
id: TC-AC-SU-E2E-107-tab-changelog-filter-panel-screening-opsi-dan-satu-opsi
title: "Tab Changelog: Filter Panel (Screening, Isi Opsi, Satu Opsi per Field, Date Inklusif)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-382
  - TC-AC-SU-383
  - TC-AC-SU-384
  - TC-AC-SU-385
coverage:
  web: automated
---

# Tab Changelog: Filter Panel (Screening, Isi Opsi, Satu Opsi per Field, Date Inklusif)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal), `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Suite berjalan serial (`parallel: false`). Flag Guided Tooltip disetel `seen` oleh hook suite; sesi API aktor dan Fixture BE disediakan tim FE/BE (lihat `suite.md`). Spec tidak memakai endpoint karangan.
- General Settings (Date Format, Time Format, Time Zone) entitas Principal tidak diubah spec ini; format tanggal yang diasersi dibaca dari General Settings tersebut.
- Data seeding (Fixture BE): user `Jane Smith {runId}-107` (email `janesmith+{runId}-107@qwertysystem.net`) dengan 6 entri Changelog (Date relatif terhadap hari uji: R1 T-10, R2 T-7, R3 T-4, R4 sampai R6 tanggal bebas; T-N berarti N hari sebelum hari uji):

| Entri | Date | Action | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|
| R1 | T-10 | Assign | Manage group | Inactive | Assigned | Admin U |
| R2 | T-7 | Edit | Manage group | 9 | 7 | Budi S |
| R3 | T-4 | Remove | Access Level | 2 | — | Admin U |
| R4 | bebas | Activate | Status | — | 4 | Cici A |
| R5 | bebas | Remove | Manage group | Active | Inactive | Budi S |
| R6 | bebas | Edit | Activation Email | Inactive | Active | Cici A |

| Opsi dropdown | Opsi yang tampil (nilai DISTINCT seeding) |
|---|---|
| Action | Assign, Edit, Remove, Activate |
| Field | Manage group, Access Level, Status, Activation Email |
| Modified By | Admin U, Budi S, Cici A |

| Filter satu opsi | Opsi dipilih |
|---|---|
| Action | Assign |
| Field | Status |
| Modified By | Admin U |

- Kemampuan teknis: kemampuan seed entri Changelog dengan Date tertentu disediakan tim FE/BE.
- Hook `before` men-seed data milik spec ini lewat Fixture BE; hook `after` menghapus user seeding di atas lewat Fixture BE. Entri audit trail yang dibuat sistem tidak dihapus. Fixture `settingsUser` (berkas belum ada; dibuat tim FE) menyimpan nama dan email user seeding; password tidak disimpan di fixture.

## Test Steps

### TC-AC-SU-382: Screening Filter Panel Tab Changelog

1. Ketik Search `Jane Smith {runId}-107`, tekan Enter
2. Klik Name `Jane Smith {runId}-107`
3. Klik tab `Changelog`
4. Hover icon Filter
5. Verifikasi tooltip `Filter` tampil
6. Klik icon Filter
7. Verifikasi Filter Panel terbuka di bawah toolbar
8. Verifikasi field Filter Panel berurutan `Date`, `Action`, `Field`, `Modified By`
9. Verifikasi field `Date` berupa date range picker dengan placeholder `Select date`
10. Verifikasi field `Action` berupa multi-select searchable dengan placeholder `All actions`
11. Verifikasi field `Field` berupa multi-select searchable dengan placeholder `All fields`
12. Verifikasi field `Modified By` berupa multi-select searchable dengan placeholder `All users`
13. Verifikasi footer panel menampilkan link `[Clear Field]` di kiri dan `[Apply]` di kanan

### TC-AC-SU-383: Isi opsi dropdown Filter Tab Changelog

14. Untuk setiap baris tabel "Opsi dropdown" di Prerequisites, lakukan langkah 15 sampai 18
15. Buka dropdown field pada baris tabel 'Opsi dropdown'
16. Verifikasi opsi dropdown sama dengan nilai DISTINCT pada kolom 'Opsi yang tampil' baris tabel itu
17. Verifikasi jumlah opsi sama dengan jumlah nilai DISTINCT itu (tidak ada opsi di luar daftar)
18. Tutup dropdown
19. Klik icon Filter untuk menutup Filter Panel

### TC-AC-SU-384: Filter field multi-select, satu opsi per field

20. Untuk setiap baris tabel "Filter satu opsi" di Prerequisites, lakukan langkah 21 sampai 31
21. Catat jumlah baris tabel Changelog
22. Klik icon Filter
23. Pilih opsi pada kolom 'Opsi dipilih' di field pada baris tabel 'Filter satu opsi'
24. Klik `[Apply]`
25. Verifikasi sedikitnya satu baris tampil
26. Verifikasi setiap baris yang tampil memiliki nilai field itu sama dengan opsi yang dipilih
27. Verifikasi icon Filter menampilkan badge titik
28. Klik icon Filter
29. Klik `[Clear Field]`, lalu klik `[Apply]`
30. Verifikasi tabel kembali menampilkan semua baris (jumlah baris sama dengan jumlah yang dicatat sebelum Filter)
31. Verifikasi badge titik pada icon Filter hilang

### TC-AC-SU-385: Date range Date inklusif

32. Klik icon Filter
33. Klik field `Date`
34. Pilih tanggal awal T-10 dan tanggal akhir T-7
35. Verifikasi isi field `Date` tampil sesuai Date Format General Settings
36. Klik `[Apply]`
37. Verifikasi baris Date T-10 dan T-7 tampil (batas inklusif)
38. Verifikasi baris Date T-4 tidak tampil
39. Klik icon Filter
40. Klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Langkah 1 dan 2 (Ketik Search nama user target, lalu Klik Name untuk membuka Detail) adalah langkah penghubung (R-16, S-03); kotak Search User List tidak dipakai sebagai objek uji.
- Langkah berulang per baris tabel: langkah 15 sampai 18 (tabel 'Opsi dropdown', 3 field) dan langkah 21 sampai 31 (tabel 'Filter satu opsi', 3 field). Menutup dropdown dan membuka-menutup Filter Panel adalah langkah penghubung; `[Clear Field]` lalu `[Apply]` mengosongkan Filter (S-09).
- Temuan untuk QA:
  - TC-384 meminta `[Clear Field]` + `[Apply]` tanpa menyatakan apakah dilakukan pada panel yang dibuka ulang; spec membuka ulang panel.
  - TC-383 'nilai yang tidak ada di baris tabel tidak muncul' tidak menyebut contoh nilai; spec mengasersi jumlah opsi sama dengan jumlah nilai DISTINCT.
  - Nilai Date Format General Settings tidak tertulis di TC; asersi format tanggal dibaca dari General Settings entitas Principal.
  - Pelaku `Admin U` (nama lengkap `Admin Utama`) tidak terpetakan ke akun mana pun di Tabel Data Uji Pre-setup (#1-#7 hanya email aktor, #8 hanya target user). Spec memakai pelaku seeding bernama depan `Admin` dan belakang `Utama`; suffix `{runId}` ditaruh di email pelaku, bukan di nama, karena format Modified By [First Name] [Last Initial] tidak dapat memuat suffix.
  - Cara men-seed entri audit trail (Date, Action, Field, Old Value, New Value, pelaku) tidak dinyatakan di TC, PRD, atau LLD; kemampuan ini ditulis 'disediakan tim FE/BE' tanpa endpoint karangan (S-13).
  - Nama target `Jane Smith` pada TC dipakai sebagai nama bersuffix `Jane Smith {runId}-NNN` per run (S-12); asersi spec memakai nilai kolom log, bukan urutan atau Search atas nama user.
- Spec ini melewati sekitar 35 langkah (40 langkah nominal, sekitar 70 dengan ekspansi blok berulang). Alasan pertahanan: seluruh blok berada pada satu permukaan, satu kelas harness (fungsional biasa), memakai dataset seeding yang sama, dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
