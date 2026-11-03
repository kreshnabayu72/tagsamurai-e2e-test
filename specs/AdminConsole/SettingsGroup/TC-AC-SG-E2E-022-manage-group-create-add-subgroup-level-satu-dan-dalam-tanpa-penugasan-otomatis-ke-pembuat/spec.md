---
id: TC-AC-SG-E2E-022-manage-group-create-add-subgroup-level-satu-dan-dalam-tanpa-penugasan-otomatis-ke-pembuat
title: "Manage group Create: Add Subgroup Level 1 dan Dalam, tanpa Penugasan Otomatis ke Pembuat"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-73
  - TC-AC-SG-97
coverage:
  web: automated
---

# Manage group Create: Add Subgroup Level 1 dan Dalam, tanpa Penugasan Otomatis ke Pembuat

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Manage group Create saja (akun aktor pertama); halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Akun aktor:

| TC | Role | Akun (Pre-setup) | Env password |
|---|---|---|---|
| TC-AC-SG-73 | Manage group Create saja | #4 `manageGroupC_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_SG_MGC_PASSWORD` |
| TC-AC-SG-97 (membuat group) | Manage group Create, Update, Delete | #3 `manageGroupCUD_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_SG_MGCUD_PASSWORD` |
| TC-AC-SG-97 (membaca popup Users) | Total Control entitas Principal | #1 `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (`Budi Santoso`) | `Spectra.env.AC_TC_PASSWORD` |

- Data seed milik spec (entitas Principal, di-seed Fixture BE di hook `before`): group level 1 `Region Dasar-{runId}-022` dengan anak `Room 301-{runId}-022` (target aksi level dalam TC-AC-SG-73; nama `Room 301` pada TC diganti nama milik spec karena target aksi tulis tidak memakai node Pre-setup bersama, S-06). Data Pre-setup `Rina Wijaya` (Read Only) dan `Budi Santoso` (Total Control) dibaca saja pada TC-AC-SG-97.
- Data Dinamis (nama dari TC diberi suffix per run, S-12):

| TC | Nama di TC | Nama di spec |
|---|---|---|
| TC-AC-SG-73 | `Region Create Only` | `Region Create Only-{runId}-022` |
| TC-AC-SG-73 | `Ruang 302` | `Ruang 302-{runId}-022` |
| TC-AC-SG-97 | `Region Pembuat` | `Region Pembuat-{runId}-022` |

- Kemampuan teknis: Fixture BE (seeding dan penghapusan data milik spec) disediakan tim FE/BE (lihat `suite.md`).
- Pemulihan: hook `after` menghapus seluruh group milik spec (seed dan hasil Create) lewat Fixture BE.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### Blok akun Manage group Create saja: TC-AC-SG-73

1. Klik `[+] Group` di Sidebar Group Tree
2. Ketik `Region Create Only-{runId}-022` pada Group Name, klik `[Submit]`
3. Verifikasi toast sukses: "Success, group has been created."
4. Verifikasi group level 1 `Region Create Only-{runId}-022` tampil di Sidebar Group Tree
5. Klik ikon `⋯` pada node `Room 301-{runId}-022` di sidebar, lalu pilih "+ Add Subgroup"
6. Ketik `Ruang 302-{runId}-022` pada Group Name, klik `[Submit]`
7. Verifikasi subgroup `Ruang 302-{runId}-022` tampil di bawah `Room 301-{runId}-022` di Sidebar Group Tree
8. Verifikasi toast sukses: "Success, group has been created."

### Blok akun Manage group CUD membuat group: TC-AC-SG-97

9. Ganti akun: logout, lalu login sebagai Manage group Create, Update, Delete (`manageGroupCUD_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_SG_MGCUD_PASSWORD`)
10. Buka halaman `Settings > Group` lewat sidebar
11. Klik `[+] Group` di Sidebar Group Tree
12. Ketik `Region Pembuat-{runId}-022` pada Group Name, klik `[Submit]`
13. Tunggu aksi selesai (popup tertutup)

### Blok akun Total Control membaca popup Users: TC-AC-SG-97

14. Ganti akun: logout, lalu login sebagai Total Control entitas Principal (`totalControlGroup_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD`)
15. Buka halaman `Settings > Group` lewat sidebar
16. Ketik Search `Region Pembuat-{runId}-022`, tekan Enter
17. Klik angka Total User baris `Region Pembuat-{runId}-022`
18. Verifikasi popup Users untuk `Region Pembuat-{runId}-022` berisi hanya `Budi Santoso` dan `Rina Wijaya`
19. Verifikasi akun pembuat (`manageGroupCUD_automated_{namaCompany}@qwertysystem.net`) tidak tercantum dan tidak ada baris Group Role "1 role" baru
20. Tutup popup Users
21. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Spec ditulis per blok akun karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`). Akun ketiga (Total Control) diperlukan karena TC-AC-SG-97 langkah 4 meminta membuka popup Users sebagai Total Control.
- Langkah penghubung (S-03): langkah 13 (tunggu aksi selesai sebelum ganti akun, bagian 8b butir 8), langkah 16 (Search untuk menemukan baris target, R-16), langkah 20 dan 21 (tutup popup dan reset Search).
- Pada sisi Create-Only TC-AC-SG-73, "level dalam" memakai anak `Room 301-{runId}-022` milik spec; kesimpulan "aksi tidak dibatasi per node" tidak teramati terpisah dari langkah 7 (S-03).
- Temuan untuk QA:
  - Nama tampil akun Manage group Create, Update, Delete (#3) tidak tertulis di Pre-setup; langkah 19 mengidentifikasi akun pembuat lewat email.
  - Kolom popup Users (penanda "Group Role 1 role") tidak dijabarkan di TC; spec mengasersi hanya berdasarkan teks Expected.
