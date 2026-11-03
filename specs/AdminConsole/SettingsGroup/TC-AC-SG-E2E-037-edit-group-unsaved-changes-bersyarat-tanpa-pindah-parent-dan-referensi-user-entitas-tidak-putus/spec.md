---
id: TC-AC-SG-E2E-037-edit-group-unsaved-changes-bersyarat-tanpa-pindah-parent-dan-referensi-user-entitas-tidak-putus
title: "Edit Group: Unsaved Changes Bersyarat, Tanpa Pindah Parent, dan Referensi User/Entitas Tidak Putus"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SG-126
  - TC-AC-SG-129
  - TC-AC-SG-130
coverage:
  web: automated
---

# Edit Group: Unsaved Changes Bersyarat, Tanpa Pindah Parent, dan Referensi User/Entitas Tidak Putus

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data: `Pohon Uji Utama` entitas Principal (Pre-setup #16 sampai #19). TC-AC-SG-126 membaca `Region B` tanpa menyimpan. TC-AC-SG-129 menjalankan rename pada node milik spec (di-seed Fixture BE di hook `before`, entitas Principal): `Induk A-{runId}-037` (level 1) dengan anak `Branch 1-{runId}-037` yang memiliki anak `Floor 1-{runId}-037` dan `Room 301-{runId}-037`; nama TC diganti nama bersuffix karena target aksi tulis tidak memakai node Pre-setup bersama (S-06). TC-AC-SG-130 menuntut angka node Pre-setup `Region A` (Total User 5 dan Total Member 4), sehingga rename dijalankan pada node Pre-setup itu (pengecualian S-06).
- Komposisi `Region A` (Pre-setup #18 dan #19): Total User 5 (`Budi Santoso`, `Rina Wijaya`, `Andi Pratama`, `Sari Dewi`, `Dewi Lestari`) dan Total Member 4 (`Distributor Alpha`, `Distributor Beta`, `Distributor Delta`, `Distributor Gamma`).
- Data Dinamis:

| TC | Nama di TC | Nama awal di spec | Nama baru di spec |
|---|---|---|---|
| TC-AC-SG-126 | `Region B` (Pre-setup) | `Region B` | `Region B2` (tidak disimpan) |
| TC-AC-SG-129 | `Branch 1` | `Branch 1-{runId}-037` (milik spec) | `Branch 1 Edit-{runId}-037` |
| TC-AC-SG-130 | `Region A` (Pre-setup) | `Region A` | `Region A Baru` |

- Pemulihan: hook `after` menghapus seluruh group milik spec lewat Fixture BE. Fixture BE (disediakan tim FE/BE, lihat `suite.md`) memulihkan `Pohon Uji Utama` ke baseline Pre-setup di hook `before` dan `after` dan sebagai langkah penghubung setelah TC-AC-SG-130. Efek: Last Updated dan Modified By node yang diubah dipulihkan oleh baseline Fixture BE; entri Changelog Group yang bertambah adalah audit trail permanen dan tidak dihapus.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SG-126: Unsaved Changes pada Edit hanya bila nilai berbeda

1. Ketik Search `Region B`, tekan Enter
2. Klik ikon `⋯` pada baris `Region B`, lalu pilih "Edit"
3. Klik `[✕]` tanpa mengubah apa pun
4. Verifikasi popup tertutup langsung tanpa dialog
5. Klik ikon `⋯` pada baris `Region B`, lalu pilih "Edit"
6. Ubah nama menjadi `Region B2`
7. Klik `[✕]`
8. Verifikasi dialog Unsaved Changes tampil dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` serta `[Leave]`
9. Klik `[Leave]`
10. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### TC-AC-SG-129: Tidak ada perpindahan parent saat Edit

11. Ketik Search `Branch 1-{runId}-037`, tekan Enter
12. Klik ikon `⋯` pada baris `Branch 1-{runId}-037`, lalu pilih "Edit"
13. Verifikasi popup hanya memiliki field Group Name
14. Verifikasi tidak ada field parent atau opsi Move Group
15. Ubah nama menjadi `Branch 1 Edit-{runId}-037`, klik `[Save]`
16. Verifikasi `Branch 1 Edit-{runId}-037` tetap berada di bawah `Induk A-{runId}-037` di sidebar
17. Verifikasi `Floor 1-{runId}-037` dan `Room 301-{runId}-037` tetap menjadi turunan `Branch 1 Edit-{runId}-037` di sidebar
18. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### TC-AC-SG-130: Rename tidak memutus referensi user dan entitas

19. Ketik Search `Region A`, tekan Enter
20. Klik ikon `⋯` pada baris `Region A`, lalu pilih "Edit"
21. Ubah nama menjadi `Region A Baru`, klik `[Save]`
22. Klik angka Total User baris `Region A Baru`
23. Verifikasi popup Users node `Region A Baru` memuat 5 user yang sama (Total User 5)
24. Tutup popup Users
25. Klik angka Total Member baris `Region A Baru`
26. Verifikasi popup Members node `Region A Baru` memuat 4 entitas yang sama (Total Member 4)
27. Tutup popup Members
28. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel
29. Pulihkan baseline `Pohon Uji Utama` lewat Fixture BE (nama `Region A` dikembalikan)

## Notes

- Langkah penghubung (S-03): langkah 1, 11, dan 19 (Search untuk menemukan baris target, R-16), langkah 10, 18, dan 28 (reset Search, S-09), langkah 29 (pemulihan baseline Pre-setup `Region A`), langkah 24 dan 27 (menutup popup).
- Langkah 9 menutup form dirty sesuai S-08 setelah Verifikasi dialog pada langkah 8.
- Langkah 16 dan 17 membaca posisi `Branch 1 Edit` dan turunannya langsung dari sidebar sebagai bukti tidak ada perpindahan parent.
- Temuan untuk QA: TC-AC-SG-130 langkah 4 hanya menyebut "popup Users dan Members node itu"; spec memverifikasi jumlah dan identitas sesuai Pre-setup #18 dan #19 (Total User 5, Total Member 4).
