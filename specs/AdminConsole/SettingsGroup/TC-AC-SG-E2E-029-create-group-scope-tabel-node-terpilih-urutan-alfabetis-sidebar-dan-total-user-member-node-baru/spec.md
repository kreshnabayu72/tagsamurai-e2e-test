---
id: TC-AC-SG-E2E-029-create-group-scope-tabel-node-terpilih-urutan-alfabetis-sidebar-dan-total-user-member-node-baru
title: "Create Group: Scope Tabel Node Terpilih, Urutan Alfabetis Sidebar, dan Total User/Member Node Baru"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-94
  - TC-AC-SG-95
  - TC-AC-SG-96
coverage:
  web: automated
---

# Create Group: Scope Tabel Node Terpilih, Urutan Alfabetis Sidebar, dan Total User/Member Node Baru

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data seed milik spec (entitas Principal, di-seed Fixture BE di hook `before`): `Region B-{runId}-029` (level 1, tanpa anak) dan `Region A-{runId}-029` (level 1) dengan anak `Branch 1-{runId}-029`. Nama TC `Region B` dan `Region A` diganti nama bersuffix milik spec karena target aksi tulis tidak memakai node Pre-setup bersama (S-06). Anak `Branch 1-{runId}-029` dipakai sebagai baris pembanding bagi asersi absence pada tabel node `Region A-{runId}-029`.
- Data Pre-setup dibaca saja: `Budi Santoso` (Total Control) dan `Rina Wijaya` (Read Only) sebagai Total User node baru (Pre-setup #17).
- Data Dinamis (nama dari TC diberi suffix per run, S-12):

| TC | Nama di TC | Nama di spec |
|---|---|---|
| TC-AC-SG-94 | `Branch 5` (anak `Region B`) | `Branch 5-{runId}-029` |
| TC-AC-SG-94 | `Branch 6` (anak `Region B`) | `Branch 6-{runId}-029` |
| TC-AC-SG-95 | `Aaa Pertama` (level 1) | `Aaa Pertama-{runId}-029` |
| TC-AC-SG-96 | `Region Kosong` (level 1) | `Region Kosong-{runId}-029` |

- Kemampuan teknis: Fixture BE (seeding dan penghapusan data milik spec) disediakan tim FE/BE (lihat `suite.md`).
- Pemulihan: hook `after` menghapus seluruh group milik spec lewat Fixture BE.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SG-94: Group baru muncul di tabel hanya bila dalam scope node terpilih

1. Klik node `Region B-{runId}-029` di sidebar
2. Klik ikon `⋯` pada node `Region B-{runId}-029` di sidebar, lalu pilih "+ Add Subgroup"
3. Ketik `Branch 5-{runId}-029` pada Group Name, klik `[Submit]`
4. Verifikasi `Branch 5-{runId}-029` langsung tampil sebagai baris pada tabel node `Region B-{runId}-029`
5. Klik node `Region A-{runId}-029` di sidebar
6. Klik ikon `⋯` pada node `Region B-{runId}-029` di sidebar, lalu pilih "+ Add Subgroup"
7. Ketik `Branch 6-{runId}-029` pada Group Name, klik `[Submit]`
8. Verifikasi baris `Branch 1-{runId}-029` tampil pada tabel node `Region A-{runId}-029`
9. Verifikasi `Branch 6-{runId}-029` tidak tampil pada tabel node `Region A-{runId}-029`
10. Verifikasi `Branch 6-{runId}-029` tampil di sidebar sebagai anak `Region B-{runId}-029`

### TC-AC-SG-95: Urutan alfabetis sidebar

11. Klik `[+] Group` di Sidebar Group Tree
12. Ketik `Aaa Pertama-{runId}-029` pada Group Name, klik `[Submit]`
13. Verifikasi node `Aaa Pertama-{runId}-029` tampil di posisi alfabetis pertama di antara group level 1 sidebar

### TC-AC-SG-96: Total User dan Total Member node baru

14. Klik `[+] Group` di Sidebar Group Tree
15. Ketik `Region Kosong-{runId}-029` pada Group Name, klik `[Submit]`
16. Klik node `Region A-{runId}-029` di sidebar sekali lagi untuk melepas pilihan node
17. Ketik Search `Region Kosong-{runId}-029`, tekan Enter
18. Klik angka Total User baris `Region Kosong-{runId}-029`
19. Verifikasi Total User node baru adalah 2: `Budi Santoso` (Total Control) dan `Rina Wijaya` (Read Only)
20. Tutup popup Users
21. Verifikasi Total Member baris `Region Kosong-{runId}-029` adalah 0
22. Verifikasi tidak ada Group Role yang terpasang otomatis pada node baru `Region Kosong-{runId}-029`
23. Verifikasi tidak ada Group Manager yang terpasang otomatis pada node baru `Region Kosong-{runId}-029`
24. Verifikasi tidak ada Group Role maupun Group Manager yang diwarisi dari ancestor pada node baru `Region Kosong-{runId}-029`
25. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 16 (melepas pilihan node `Region A-{runId}-029` yang dipilih sejak langkah 5, supaya Search langkah 17 menyaring tabel All Groups; S-03 dan S-09), langkah 17 dan 25 (Search untuk menemukan baris target dan reset Search, R-16 dan S-09), langkah 20 (menutup popup Users).
- Langkah 8 adalah anchor positif bagi asersi absence langkah 9 pada permukaan tabel yang sama (bagian 8b butir 2).
- Langkah 22 sampai 24 diamati dari isi popup Users pada langkah 19 (hanya dua user tanpa Group Role atau Group Manager); node baru berada di level 1 sehingga tidak ada ancestor non-root yang dapat mewariskan penugasan.
- Temuan untuk QA: TC-AC-SG-96 langkah 4 menyebut "klik angka Total User di tabel parent atau lihat popup lewat All Groups" (dua cara); spec memakai baris node baru pada tabel All Groups lewat Search.
