---
id: TC-FA-GRP-E2E-100-wizard-setup-column-geser-drag-dan-pin-kolom
title: "Wizard Setup Column: Geser (Drag) dan Pin Kolom Group, Total Asset, dan Total User"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1099
  - TC-FA-GRP-1100
coverage:
  web: automated
---

# Wizard Setup Column: Geser (Drag) dan Pin Kolom Group, Total Asset, dan Total User

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Total Control client Wizard (Pre-setup No 8: plan dijadwalkan downgrade Professional ke Growth, cap 3, T-30 berjalan, client punya 6 group; email dan `Spectra.env.FA_WIZ_TC_PASSWORD` disediakan tim FE, tidak tertulis di Pre-setup TC); halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE) mengikuti `suite.md`; hook `after` mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).
- Nama data Dinamis di Test Steps ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-NNN` (NNN = nomor spec ini) dan sama di seeding, asersi teks, dan cleanup. Nilai mengacu `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas `fixtures/fixedAssetSettingsGroups.json` belum ada; ditambahkan tim FE).
- Data Dinamis (di-seed lewat API di `before`): enam group `Head Office`, `Warehouse A` (24 aset aktif), `Branch Office` (0 aset), `Warehouse B`, `Disposal Yard`, dan `Global HQ`, dibuat berurutan (urutan pembuatan tercatat). Seleksi Wizard tersimpan dikosongkan dan status belum pernah submit direset oleh hook `before` lewat fixture BE (disediakan tim FE/BE).
- State tenant (kelas h): plan dijadwalkan downgrade. Hook `after` memulihkan plan terjadwal, seleksi tersimpan, dan status Excess lewat fixture BE (disediakan tim FE/BE). Hook uji handler plan-efektif pada T-0 (pemicu, bukan objek uji) disediakan tim FE/BE tanpa endpoint karangan. Suite berjalan serial.
- Pemulihan konfigurasi kolom: preferensi kolom tabel Step Group Consolidation yang disimpan spec dihapus di hook `after` dengan menghapus preferensi kolom di browser (bukan [Reset to Default]); kemampuan disediakan tim FE (bagian 4).
- Lebar viewport 900px sehingga tabel dapat di-scroll horizontal (TC-1100); viewport dipulihkan pada langkah penghubung. Iterasi per kolom (8b butir 7): tabel kolom untuk TC-1099 dan TC-1100:

| Kolom |
|---|
| `Group` |
| `Total Asset` |
| `Total User` |

## Test Steps

### TC-FA-GRP-1099: Geser (drag) kolom

1. Buka Wizard Reconciliation > Step Group Consolidation
2. Untuk setiap baris tabel Kolom pada Prerequisites, lakukan langkah 3 sampai 10
3. Buka Popup Setup Column
4. Drag kolom pada baris tabel ke posisi lain
5. Verifikasi urutan Live Preview mengikuti posisi baru
6. Klik [Save]
7. Verifikasi urutan kolom tabel berubah
8. Refresh F5
9. Verifikasi urutan kolom tabel bertahan setelah F5
10. Buka Popup Setup Column, klik [Reset to Default], lalu klik [Save]

### TC-FA-GRP-1100: Pin kolom

11. Setel lebar viewport 900px
12. Untuk setiap baris tabel Kolom pada Prerequisites, lakukan langkah 13 sampai 22
13. Buka Popup Setup Column
14. Klik icon Pin kolom pada baris tabel
15. Klik [Save]
16. Scroll tabel horizontal
17. Verifikasi kolom tersebut membeku (sticky) saat scroll horizontal
18. Refresh F5
19. Verifikasi pin kolom tersebut bertahan setelah F5
20. Buka Popup Setup Column, unpin kolom tersebut, lalu klik [Save]
21. Scroll tabel horizontal
22. Verifikasi kolom tersebut kembali ikut scroll setelah unpin
23. Pulihkan lebar viewport

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 10 dan 11, 23: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Langkah 3 sampai 10 (TC-1099) dan 13 sampai 22 (TC-1100) diulang untuk setiap baris tabel Kolom; `Verifikasi` tetap satu per klausa. Ekspansi: TC-1099 3 kali 8 langkah dan TC-1100 3 kali 10 langkah.
- Spec berisi lebih dari 35 langkah setelah ekspansi. Alasan: satu kelas dan satu surface; iterasi per kolom sah menurut 8b butir 7; kedua TC berdiri sendiri dan konfigurasi dipulihkan tiap iterasi.
- Temuan untuk QA:
  - TC-1099 dan TC-1100 menyebut "posisi lain" tanpa posisi tujuan; spec memakai posisi lain yang berbeda dari posisi awal.
