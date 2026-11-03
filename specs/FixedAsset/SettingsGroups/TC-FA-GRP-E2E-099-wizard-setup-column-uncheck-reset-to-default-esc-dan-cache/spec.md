---
id: TC-FA-GRP-E2E-099-wizard-setup-column-uncheck-reset-to-default-esc-dan-cache
title: "Wizard Setup Column: Uncheck Kolom Group/Total Asset/Total User, [Reset to Default], (X) dan Esc Membatalkan, dan Cache Tidak Memengaruhi Tabel Lain"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1098
  - TC-FA-GRP-1102
  - TC-FA-GRP-1103
  - TC-FA-GRP-1104
coverage:
  web: automated
---

# Wizard Setup Column: Uncheck Kolom Group/Total Asset/Total User, [Reset to Default], (X) dan Esc Membatalkan, dan Cache Tidak Memengaruhi Tabel Lain

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Total Control client Wizard (Pre-setup No 8: plan dijadwalkan downgrade Professional ke Growth, cap 3, T-30 berjalan, client punya 6 group; email dan `Spectra.env.FA_WIZ_TC_PASSWORD` disediakan tim FE, tidak tertulis di Pre-setup TC); halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE) mengikuti `suite.md`; hook `after` mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).
- Nama data Dinamis di Test Steps ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-NNN` (NNN = nomor spec ini) dan sama di seeding, asersi teks, dan cleanup. Nilai mengacu `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas `fixtures/fixedAssetSettingsGroups.json` belum ada; ditambahkan tim FE).
- Data Dinamis (di-seed lewat API di `before`): enam group `Head Office`, `Warehouse A` (24 aset aktif), `Branch Office` (0 aset), `Warehouse B`, `Disposal Yard`, dan `Global HQ`, dibuat berurutan (urutan pembuatan tercatat). Seleksi Wizard tersimpan dikosongkan dan status belum pernah submit direset oleh hook `before` lewat fixture BE (disediakan tim FE/BE).
- State tenant (kelas h): plan dijadwalkan downgrade. Hook `after` memulihkan plan terjadwal, seleksi tersimpan, dan status Excess lewat fixture BE (disediakan tim FE/BE). Hook uji handler plan-efektif pada T-0 (pemicu, bukan objek uji) disediakan tim FE/BE tanpa endpoint karangan. Suite berjalan serial.
- Pemulihan konfigurasi kolom: preferensi kolom tabel Step Group Consolidation yang disimpan spec dihapus di hook `after` dengan menghapus preferensi kolom di browser (bukan [Reset to Default]); kemampuan disediakan tim FE (bagian 4).
- Iterasi per kolom (8b butir 7): tabel kolom untuk TC-1098:

| Kolom |
|---|
| `Group` |
| `Total Asset` |
| `Total User` |

## Test Steps

### TC-FA-GRP-1098: Uncheck kolom Group, Total Asset, dan Total User

1. Buka Wizard Reconciliation > Step Group Consolidation
2. Untuk setiap baris tabel Kolom pada Prerequisites, lakukan langkah 3 sampai 11
3. Buka Popup Setup Column
4. Uncheck kolom pada baris tabel
5. Verifikasi Live Preview langsung menyembunyikan kolom tersebut
6. Klik [Save]
7. Verifikasi kolom tersebut hilang dari tabel
8. Refresh F5
9. Verifikasi kolom selain kolom pada baris tabel tetap tampil di tabel setelah F5
10. Verifikasi kolom tersebut tetap hilang dari tabel setelah F5 (konfigurasi bertahan)
11. Buka Popup Setup Column, check kolom kembali, lalu klik [Save]

### TC-FA-GRP-1102: [Reset to Default]

12. Ubah urutan (drag Group ke posisi lain), hide Total User, dan pin Total Asset, lalu klik [Save]
13. Buka Popup Setup Column
14. Klik [Reset to Default]
15. Verifikasi Live Preview kembali ke susunan default (ketiga kolom tampil, tanpa pin)
16. Klik [Save]
17. Verifikasi tabel kembali ke susunan default
18. Refresh F5
19. Verifikasi susunan default bertahan setelah F5

### TC-FA-GRP-1103: (X) dan Esc membatalkan perubahan

20. Buka Popup Setup Column
21. Uncheck satu kolom (Total User)
22. Klik (X)
23. Verifikasi popup tertutup tanpa menerapkan perubahan
24. Verifikasi tabel tetap memakai konfigurasi tersimpan terakhir (ketiga kolom tampil)
25. Buka Popup Setup Column
26. Drag satu kolom (Group) ke posisi lain
27. Tekan Esc
28. Verifikasi popup tertutup tanpa menerapkan perubahan
29. Verifikasi tabel tetap memakai konfigurasi tersimpan terakhir (urutan default)

### TC-FA-GRP-1104: Cache tidak memengaruhi tabel lain

30. Buka Popup Setup Column
31. Hide satu kolom (Total User)
32. Klik [Save]
33. Buka Fixed Asset > Settings > Groups
34. Verifikasi Groups List tetap memakai konfigurasi kolomnya sendiri
35. Buka Wizard Reconciliation > Step Group Consolidation
36. Verifikasi kolom Total User tetap tersembunyi (konfigurasi tabel Step Group Consolidation tetap tersimpan)
37. Buka Popup Setup Column, check Total User kembali, lalu klik [Save]

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 11 dan 12, 33, 35, 37: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Langkah 3 sampai 11 diulang untuk setiap baris tabel Kolom (Group, Total Asset, Total User); `Verifikasi` tetap satu per klausa. Asersi absence kolom setelah F5 (langkah 10) didahului `Verifikasi` kolom lain tampil (langkah 9, anchor 8b butir 2). Alur ekspansi: 3 iterasi dari 9 langkah.
- Spec berisi lebih dari 35 langkah setelah ekspansi. Alasan: satu kelas dan satu surface (Setup Column Step Group Consolidation); iterasi per kolom sah menurut 8b butir 7 dan blok tiap TC berdiri sendiri; konfigurasi dipulihkan oleh langkah penghubung dan hook `after`.
- Temuan untuk QA:
  - TC-1098 Langkah 6 mengubah dua kolom berurutan (check Group, uncheck Total Asset); spec memulihkan kolom pada akhir tiap iterasi sehingga tiap kolom diuji terisolasi.
  - TC-1102 Langkah 2 "ubah urutan, hide, dan pin beberapa kolom" tanpa kolom tertentu; spec memakai drag Group, hide Total User, pin Total Asset.
