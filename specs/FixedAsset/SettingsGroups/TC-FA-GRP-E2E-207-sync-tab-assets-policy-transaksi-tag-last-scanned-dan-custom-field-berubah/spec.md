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
- Data Dinamis (Pre-setup tambahan No 16 dan 17, di-seed lewat API di hook `before`, dihapus atau dipulihkan di hook `after`; nama bersuffix `{runId}-207`): `Value Sync Node {runId}-207` (Assignable, level 1) berisi hanya aset S1 `Sync Printer - 1 {runId}-207` (Asset Name `Sync Printer`; tanpa tag aktif, belum pernah dipindai, semua policy Off); Custom Field `Sync Field {runId}-207` (General, Text, Scope Specific `Sync Printer`, Active; nilai S1 `SYNC-1`); Asset Name `Sync Other {runId}-207` (tanpa aset di `Value Sync Node`, di-seed dan dihapus oleh hook yang sama, dipakai sebagai Scope pengganti pada TC-1253).
- Pemetaan nama: pada Test Steps, `Value Sync Node`, `Sync Printer` (Asset Name; `Sync Printer - 1` untuk S1), `Sync Other`, dan `Sync Field` menunjuk fixture bersuffix `{runId}-207` di atas.
- State global yang diubah spec: policy transaksi Asset Name `Sync Printer` (Borrow On), pairing Extra TAG S1, pemindaian S1 di Audit, dan nilai, Scope, serta status Custom Field `Sync Field`; dipulihkan di hook `after` (policy Borrow Off, Extra TAG dilepas, Sync Field dikembalikan ke Active dengan Scope semula; pemindaian Audit tidak dapat dibatalkan dan tetap pada S1 milik spec yang dihapus). Suite berjalan serial.
- Kemampuan teknis (disediakan tim FE/BE): membuat pemindaian Audit pada aset (`task_item.scanned_at`) dan pemindaian lewat Search by Scan; General Settings Date Format DD/MM/YYYY, Time 24-hour, Timezone Asia/Jakarta (TC-1252), tidak diubah oleh spec.
- Kolom Transactional Policy, TAG, Last Scanned, dan Sync Field adalah kolom curated Tab Assets yang dicentang lewat Setup Column pada tiap TC; pemulihan: hapus preferensi kolom di browser di hook `after` (kemampuan disediakan tim FE).

## Test Steps

### TC-1250: Policy Transaksi

1. Ketik Search `Value Sync Node {runId}-207`, tekan Enter
2. Buka Detail Value Sync Node, klik Tab Assets, centang kolom Transactional Policy
3. Verifikasi sel Transactional Policy S1 `—`
4. Buka Settings > Asset Transactional Policy, ubah policy Borrow Asset Name `Sync Printer` menjadi On
5. Tunggu aksi selesai
6. Buka Fixed Asset > Settings > Groups
7. Ketik Search `Value Sync Node {runId}-207`, tekan Enter
8. Kembali ke Detail Value Sync Node (Tab Assets)
9. Verifikasi sel Transactional Policy S1 menampilkan ikon Borrow tanpa penulisan per aset (real-time)

### TC-1251: Pairing atau pelepasan Extra TAG

10. Amati sel TAG S1 pada Tab Assets (centang kolom TAG)
11. Verifikasi sel TAG S1 `—`
12. Pasang Extra TAG tipe RFID pada S1 di modul Asset
13. Tunggu aksi selesai
14. Buka Fixed Asset > Settings > Groups
15. Ketik Search `Value Sync Node {runId}-207`, tekan Enter
16. Kembali ke Detail Value Sync Node (Tab Assets)
17. Verifikasi sel TAG S1 menampilkan ikon RFID tanpa Tag Code
18. Lepas (unpair) Extra TAG tersebut di modul Asset
19. Tunggu aksi selesai
20. Buka Fixed Asset > Settings > Groups
21. Ketik Search `Value Sync Node {runId}-207`, tekan Enter
22. Kembali ke Detail Value Sync Node (Tab Assets)
23. Verifikasi sel TAG S1 kembali `—`

### TC-1252: Pemindaian Audit memperbarui Last Scanned

24. Centang kolom Last Scanned pada Tab Assets
25. Verifikasi sel Last Scanned S1 `—`
26. Pindai S1 pada Audit
27. Tunggu aksi selesai
28. Buka Fixed Asset > Settings > Groups
29. Ketik Search `Value Sync Node {runId}-207`, tekan Enter
30. Kembali ke Detail Value Sync Node (Tab Assets)
31. Verifikasi sel Last Scanned S1 menampilkan waktu pemindaian terbaru sesuai format General Settings
32. Catat nilai sel Last Scanned S1
33. Pindai S1 lewat Search by Scan
34. Buka Fixed Asset > Settings > Groups
35. Ketik Search `Value Sync Node {runId}-207`, tekan Enter
36. Kembali ke Detail Value Sync Node (Tab Assets)
37. Verifikasi sel Last Scanned S1 tidak berubah dari nilai yang dicatat (pemindaian Search by Scan tidak mengubah kolom)

### TC-1253: Nilai, Scope, dan status Custom Field

38. Centang kolom Sync Field pada Tab Assets
39. Verifikasi sel Sync Field S1 `SYNC-1`
40. Ubah nilai Sync Field S1 menjadi `SYNC-2` di modul Asset
41. Tunggu aksi selesai
42. Buka Fixed Asset > Settings > Groups
43. Ketik Search `Value Sync Node {runId}-207`, tekan Enter
44. Kembali ke Detail Value Sync Node (Tab Assets)
45. Verifikasi sel Sync Field S1 `SYNC-2`
46. Ubah Scope Sync Field ke Asset Name `Sync Other {runId}-207` (tanpa `Sync Printer`)
47. Tunggu aksi selesai
48. Buka Fixed Asset > Settings > Groups
49. Ketik Search `Value Sync Node {runId}-207`, tekan Enter
50. Kembali ke Detail Value Sync Node (Tab Assets)
51. Verifikasi sel Sync Field S1 `—`
52. Nonaktifkan Sync Field
53. Tunggu aksi selesai
54. Buka Fixed Asset > Settings > Groups
55. Ketik Search `Value Sync Node {runId}-207`, tekan Enter
56. Kembali ke Detail Value Sync Node (Tab Assets)
57. Verifikasi kolom Name tampil di tabel (anchor)
58. Verifikasi kolom `Sync Field {runId}-207` hilang dari tabel
59. Buka Popup Setup Column
60. Verifikasi Popup Setup Column memuat kolom Name (anchor)
61. Verifikasi kolom `Sync Field {runId}-207` tidak ada di Popup Setup Column
62. Klik (X) untuk menutup popup tanpa menyimpan

## Notes

- Langkah penghubung (S-03): Tunggu aksi selesai (8b butir 8), kembali ke Detail Value Sync Node, mencentang kolom, serta pemindaian Search by Scan dan pencatatan nilai Last Scanned (TC-1252 Expected b memeriksa bahwa Search by Scan tidak mengubah kolom, tetapi TC tidak memberi langkahnya). Asersi tambahan (S-03, 8b butir 2): Verifikasi kolom `Name` tampil di tabel dan di Popup Setup Column sebagai anchor sebelum asersi kolom Sync Field hilang.
- Spec memiliki 62 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik (sinkronisasi lintas modul ke Tab Assets pada fixture Value Sync Node yang sama); tiap TC berdiri sendiri dan Expected memeriksa tiga keadaan (awal, sesudah perubahan, sesudah pemulihan).
- Tiap "Kembali ke Detail Value Sync Node" didahului Buka Fixed Asset > Settings > Groups (S-14; langkah sebelumnya meninggalkan halaman Groups) dan Search nama node bersuffix (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan). Langkah Search adalah langkah penghubung (S-03, R-16).
- Temuan untuk QA:
  - TC-1250 sampai 1253 memakai nama literal (`Value Sync Node`, `Sync Printer`, `Sync Field`) yang diberi suffix per run untuk node, aset, dan Custom Field (S-12); Asset Name `Sync Printer` dan `Sync Other` adalah Asset Name milik spec bersuffix `{runId}-207` (Pre-setup tambahan, di-seed di hook `before`, dihapus di hook `after`; S-06), sehingga master data bersama tidak diubah.
  - TC-1252 Expected b memuat klausa "pemindaian lewat Search by Scan tidak mengubah kolom" tanpa langkah pemicu; spec menambah langkah penghubung Search by Scan (S-15). Mekanisme pemindaian Audit dan Search by Scan tidak dirinci di TC, PRD, atau LLD; ditulis sebagai kemampuan tim FE/BE (S-13).
