---
id: TC-FA-GRP-E2E-207-sync-tab-assets-policy-transaksi-tag-last-scanned-dan-custom-field-berubah
title: "Sinkron Lintas Modul ke Tab Assets: Policy Transaksi, Pairing/Pelepasan TAG, Pemindaian Audit, dan Nilai/Scope/Status Custom Field"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1250
  - TC-FA-GRP-1251
  - TC-FA-GRP-1252
  - TC-FA-GRP-1253
coverage:
  web: automated
---

# Sinkron Lintas Modul ke Tab Assets: Policy Transaksi, Pairing/Pelepasan TAG, Pemindaian Audit, dan Nilai/Scope/Status Custom Field

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (Pre-setup tambahan No 16 dan 17, di-seed lewat API di hook `before`, dihapus atau dipulihkan di hook `after`; nama bersuffix `{runId}-207`): `Value Sync Node {runId}-207` (Assignable, level 1) berisi hanya aset S1 `Sync Printer - 1 {runId}-207` (Asset Name `Sync Printer`; tanpa tag aktif, belum pernah dipindai, semua policy Off); Custom Field `Sync Field {runId}-207` (General, Text, Scope Specific `Sync Printer`, Active; nilai S1 `SYNC-1`).
- Pemetaan nama: pada Test Steps, `Value Sync Node`, `Sync Printer` (Asset Name; `Sync Printer - 1` untuk S1), dan `Sync Field` menunjuk fixture bersuffix `{runId}-207` di atas.
- State global yang diubah spec: policy transaksi Asset Name `Sync Printer` (Borrow On), pairing Extra TAG S1, pemindaian S1 di Audit, dan nilai, Scope, serta status Custom Field `Sync Field`; dipulihkan di hook `after` (policy Borrow Off, Extra TAG dilepas, Sync Field dikembalikan ke Active dengan Scope semula; pemindaian Audit tidak dapat dibatalkan dan tetap pada S1 milik spec yang dihapus). Suite berjalan serial.
- Kemampuan teknis (disediakan tim FE/BE): membuat pemindaian Audit pada aset (`task_item.scanned_at`) dan pemindaian lewat Search by Scan; General Settings Date Format DD/MM/YYYY, Time 24-hour, Timezone Asia/Jakarta (TC-1252), tidak diubah oleh spec.
- Kolom Transactional Policy, TAG, Last Scanned, dan Sync Field adalah kolom curated Tab Assets yang dicentang lewat Setup Column pada tiap TC; pemulihan: hapus preferensi kolom di browser di hook `after` (kemampuan disediakan tim FE).

## Test Steps

### TC-1250: Policy Transaksi

1. Buka Detail Value Sync Node, klik Tab Assets, centang kolom Transactional Policy
2. Verifikasi sel Transactional Policy S1 `—`
3. Buka Settings > Asset Transactional Policy, ubah policy Borrow Asset Name `Sync Printer` menjadi On
4. Tunggu aksi selesai
5. Kembali ke Detail Value Sync Node (Tab Assets)
6. Verifikasi sel Transactional Policy S1 menampilkan ikon Borrow tanpa penulisan per aset (real-time)

### TC-1251: Pairing atau pelepasan Extra TAG

7. Amati sel TAG S1 pada Tab Assets (centang kolom TAG)
8. Verifikasi sel TAG S1 `—`
9. Pasang Extra TAG tipe RFID pada S1 di modul Asset
10. Tunggu aksi selesai
11. Kembali ke Detail Value Sync Node (Tab Assets)
12. Verifikasi sel TAG S1 menampilkan ikon RFID tanpa Tag Code
13. Lepas (unpair) Extra TAG tersebut di modul Asset
14. Tunggu aksi selesai
15. Kembali ke Detail Value Sync Node (Tab Assets)
16. Verifikasi sel TAG S1 kembali `—`

### TC-1252: Pemindaian Audit memperbarui Last Scanned

17. Centang kolom Last Scanned pada Tab Assets
18. Verifikasi sel Last Scanned S1 `—`
19. Pindai S1 pada Audit
20. Tunggu aksi selesai
21. Kembali ke Detail Value Sync Node (Tab Assets)
22. Verifikasi sel Last Scanned S1 menampilkan waktu pemindaian terbaru sesuai format General Settings
23. Catat nilai sel Last Scanned S1
24. Pindai S1 lewat Search by Scan
25. Kembali ke Detail Value Sync Node (Tab Assets)
26. Verifikasi sel Last Scanned S1 tidak berubah dari nilai yang dicatat (pemindaian Search by Scan tidak mengubah kolom)

### TC-1253: Nilai, Scope, dan status Custom Field

27. Centang kolom Sync Field pada Tab Assets
28. Verifikasi sel Sync Field S1 `SYNC-1`
29. Ubah nilai Sync Field S1 menjadi `SYNC-2` di modul Asset
30. Tunggu aksi selesai
31. Kembali ke Detail Value Sync Node (Tab Assets)
32. Verifikasi sel Sync Field S1 `SYNC-2`
33. Ubah Scope Sync Field ke Asset Name lain (tanpa `Sync Printer`)
34. Tunggu aksi selesai
35. Kembali ke Detail Value Sync Node (Tab Assets)
36. Verifikasi sel Sync Field S1 `—`
37. Nonaktifkan Sync Field
38. Tunggu aksi selesai
39. Kembali ke Detail Value Sync Node (Tab Assets)
40. Verifikasi kolom Name tampil di tabel (anchor)
41. Verifikasi kolom `Sync Field {runId}-207` hilang dari tabel
42. Buka Popup Setup Column
43. Verifikasi Popup Setup Column memuat kolom Name (anchor)
44. Verifikasi kolom `Sync Field {runId}-207` tidak ada di Popup Setup Column
45. Klik (X) untuk menutup popup tanpa menyimpan

## Notes

- Langkah penghubung (S-03): Tunggu aksi selesai (8b butir 8), kembali ke Detail Value Sync Node, mencentang kolom, serta pemindaian Search by Scan dan pencatatan nilai Last Scanned (TC-1252 Expected b memeriksa bahwa Search by Scan tidak mengubah kolom, tetapi TC tidak memberi langkahnya). Asersi tambahan (S-03, 8b butir 2): Verifikasi kolom `Name` tampil di tabel dan di Popup Setup Column sebagai anchor sebelum asersi kolom Sync Field hilang.
- Spec memiliki 45 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik (sinkronisasi lintas modul ke Tab Assets pada fixture Value Sync Node yang sama); tiap TC berdiri sendiri dan Expected memeriksa tiga keadaan (awal, sesudah perubahan, sesudah pemulihan).
- Temuan untuk QA:
  - TC-1250 sampai 1253 memakai nama literal (`Value Sync Node`, `Sync Printer`, `Sync Field`) yang diberi suffix per run untuk node, aset, dan Custom Field (S-12); Asset Name `Sync Printer` (Master data, Pre-setup tambahan No 14) dipakai apa adanya dan policy Borrow-nya dipulihkan.
  - TC-1252 Expected b memuat klausa "pemindaian lewat Search by Scan tidak mengubah kolom" tanpa langkah pemicu; spec menambah langkah penghubung Search by Scan (S-15). Mekanisme pemindaian Audit dan Search by Scan tidak dirinci di TC, PRD, atau LLD; ditulis sebagai kemampuan tim FE/BE (S-13).
