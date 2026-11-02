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
2. Untuk setiap baris tabel Kolom pada Prerequisites, lakukan langkah 3 sampai 10
3. Buka Popup Setup Column
4. Uncheck kolom pada baris tabel
5. Verifikasi Live Preview langsung menyembunyikan kolom tersebut
6. Klik [Save]
7. Verifikasi kolom tersebut hilang dari tabel
8. Refresh F5
9. Verifikasi kolom tersebut tetap hilang dari tabel setelah F5 (konfigurasi bertahan)
10. Buka Popup Setup Column, check kolom kembali, lalu klik [Save]

### TC-FA-GRP-1102: [Reset to Default]

11. Ubah urutan (drag Group ke posisi lain), hide Total User, dan pin Total Asset, lalu klik [Save]
12. Buka Popup Setup Column
13. Klik [Reset to Default]
14. Verifikasi Live Preview kembali ke susunan default (ketiga kolom tampil, tanpa pin)
15. Klik [Save]
16. Verifikasi tabel kembali ke susunan default
17. Refresh F5
18. Verifikasi susunan default bertahan setelah F5

### TC-FA-GRP-1103: (X) dan Esc membatalkan perubahan

19. Buka Popup Setup Column
20. Uncheck satu kolom (Total User)
21. Klik (X)
22. Verifikasi popup tertutup tanpa menerapkan perubahan
23. Verifikasi tabel tetap memakai konfigurasi tersimpan terakhir (ketiga kolom tampil)
24. Buka Popup Setup Column
25. Drag satu kolom (Group) ke posisi lain
26. Tekan Esc
27. Verifikasi popup tertutup tanpa menerapkan perubahan
28. Verifikasi tabel tetap memakai konfigurasi tersimpan terakhir (urutan default)

### TC-FA-GRP-1104: Cache tidak memengaruhi tabel lain

29. Buka Popup Setup Column
30. Hide satu kolom (Total User)
31. Klik [Save]
32. Buka Fixed Asset > Settings > Groups
33. Verifikasi Groups List tetap memakai konfigurasi kolomnya sendiri
34. Buka Wizard Reconciliation > Step Group Consolidation
35. Verifikasi kolom Total User tetap tersembunyi (konfigurasi tabel Step Group Consolidation tetap tersimpan)
36. Buka Popup Setup Column, check Total User kembali, lalu klik [Save]

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 10 dan 11, 32, 34, 36: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Langkah 3 sampai 10 diulang untuk setiap baris tabel Kolom (Group, Total Asset, Total User); `Verifikasi` tetap satu per klausa. Alur ekspansi: 3 iterasi dari 8 langkah.
- Spec berisi lebih dari 35 langkah setelah ekspansi. Alasan: satu kelas dan satu surface (Setup Column Step Group Consolidation); iterasi per kolom sah menurut 8b butir 7 dan blok tiap TC berdiri sendiri; konfigurasi dipulihkan oleh langkah penghubung dan hook `after`.
- Temuan untuk QA:
  - TC-1098 Langkah 6 mengubah dua kolom berurutan (check Group, uncheck Total Asset); spec memulihkan kolom pada akhir tiap iterasi sehingga tiap kolom diuji terisolasi.
  - TC-1102 Langkah 2 "ubah urutan, hide, dan pin beberapa kolom" tanpa kolom tertentu; spec memakai drag Group, hide Total User, pin Total Asset.
