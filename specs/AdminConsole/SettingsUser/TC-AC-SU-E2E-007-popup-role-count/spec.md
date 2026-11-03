---
id: TC-AC-SU-E2E-007-popup-role-count
title: "Popup Role Count: Screening, Tanpa Section Group Role, Penutupan, dan Role Switch OFF"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-21
  - TC-AC-SU-22
  - TC-AC-SU-23
  - TC-AC-SU-24
coverage:
  web: automated
---

# Popup Role Count: Screening, Tanpa Section Group Role, Penutupan, dan Role Switch OFF

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-21, 23 | `Region A` | `Region A {runId}-007` | - | Group (induk) |
| TC-AC-SU-21 | `Branch 1` | `Branch 1 {runId}-007` | - | Group, anak `Region A {runId}-007` |
| TC-AC-SU-21, 23 | `Jane Smith` | `Jane Smith {runId}-007` | `janesmith+{runId}-007@qwertysystem.net` | Global Role aktif `Manage group` dan `Manage device master data`; Group Role aktif `Manage allocation` di `Region A {runId}-007` dan `Branch 1 {runId}-007`, `Manage partner` di `Region A {runId}-007` |
| TC-AC-SU-22 | `Mike Tan` | `Mike Tan {runId}-007` | `miketan+{runId}-007@qwertysystem.net` | hanya Global Role aktif `Manage group` |
| TC-AC-SU-24 | `Budi Santoso` | `Budi Santoso {runId}-007` | `budisantoso+{runId}-007@qwertysystem.net` | Global Role `Manage group` ON dan `Manage TAG stock` OFF (CRUD tersimpan inactive) |

- Seeding di hook `before`, penghapusan data milik spec di hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-21: Screening Popup Role Count

1. Ketik Search `{runId}-007`, tekan Enter
2. Klik label `5 roles` pada `Jane Smith {runId}-007`
3. Verifikasi popup kecil terbuka
4. Verifikasi Title popup `Active Roles (5)`
5. Verifikasi section `Global Role`: bullet `Manage device master data`, `Manage group` (urut A-Z)
6. Verifikasi Divider tampil
7. Verifikasi section `Group Role`: bullet `Manage allocation — 2 groups`, `Manage partner — 1 group` (urut A-Z)
8. Verifikasi tidak ada nama group pada bullet
9. Hover bullet section `Group Role`
10. Verifikasi tidak ada tooltip hover pada bullet
11. Verifikasi angka header (5) lebih besar dari jumlah bullet Group Role (2) karena konsolidasi
12. Tutup popup dengan Esc

### TC-AC-SU-22: Popup Role Count tanpa section Group Role

13. Klik `1 role` pada `Mike Tan {runId}-007`
14. Verifikasi Title popup `Active Roles (1)`
15. Verifikasi section `Global Role` dengan bullet `Manage group`
16. Verifikasi section `Group Role` dan Divider tidak tampil
17. Tutup popup dengan Esc

### TC-AC-SU-23: Popup Role Count ditutup dengan Esc atau [✕]; klik di luar tidak menutup

18. Klik label jumlah Role pada `Jane Smith {runId}-007`
19. Klik area di luar popup
20. Verifikasi popup tetap terbuka
21. Tekan Esc
22. Verifikasi popup tertutup
23. Klik label jumlah Role pada `Jane Smith {runId}-007` untuk membuka popup lagi
24. Klik `[✕]` pada popup
25. Verifikasi popup tertutup
26. Verifikasi tabel tetap pada kondisi sebelumnya

### TC-AC-SU-24: Role Count tidak menghitung role switch OFF

27. Amati kolom Role baris `Budi Santoso {runId}-007`
28. Verifikasi label kolom Role `1 role`
29. Klik label `1 role` pada `Budi Santoso {runId}-007`
30. Verifikasi popup `Active Roles (1)`
31. Verifikasi popup hanya memuat `Manage group`
32. Tutup popup dengan Esc
33. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search atas suffix spec, R-16), langkah 12, 17, dan 32 (tutup popup), langkah 33 (reset Search). Layar awal dibuka hook `beforeEach` suite.
- Temuan untuk QA:
  - TC-AC-SU-23 menyebut "≥1 role aktif" untuk `Jane Smith`; spec memakai seed TC-AC-SU-21 (5 role aktif).
  - TC-AC-SU-24: popup "hanya memuat `Manage group`" diasersi sebagai satu klausa (isi bullet).
  - Nama user TC (`Region A`, `Branch 1`, `Jane Smith`, `Mike Tan`, `Budi Santoso`) dipakai sebagai nama bersuffix `{runId}-007` sesuai S-12 (Lampiran A tidak memuat pengecualian modul Settings > User).
