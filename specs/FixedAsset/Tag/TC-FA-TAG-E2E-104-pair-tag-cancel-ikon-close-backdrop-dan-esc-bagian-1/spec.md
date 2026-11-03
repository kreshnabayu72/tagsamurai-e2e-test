---
id: TC-FA-TAG-E2E-104-pair-tag-cancel-ikon-close-backdrop-dan-esc-bagian-1
title: "Pair TAG: Cancel dan Konfirmasi Discard Pairing D-11 (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-444
  - TC-FA-TAG-445
  - TC-FA-TAG-446
  - TC-FA-TAG-447
coverage:
  web: automated
---

# Pair TAG: Cancel dan Konfirmasi Discard Pairing D-11 (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader) yang memindai kode Tag di ButtonScan; (2) seed dan pemulihan idempotent lewat fixture backend untuk aset Not Paired Yet dan stok Available per tipe; tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset tiga tipe | 'Server Rack 42U - 101' (AST-0101, Group Plant A, TAG Type Asset Name RFID, NFC, dan QR), Not Paired Yet | `aset101` |
| Stok Available | Tag RFID `RF-00412`, `RF-00415`, Tag NFC `NF-00500`, Tag QR `QR-00701` | `stokAvailable` |

- State yang diubah dan pemulihannya: spec tidak menyimpan perubahan (dialog dibuang dengan [Discard]).

## Test Steps

### Cancel pada dialog tanpa kode (TC-FA-TAG-444)

1. Klik Asset Name 'Server Rack 42U' pada baris grup Plant A untuk membuka Popup Detail
2. Klik tombol teks `Show` di samping field `Not Paired Yet`
3. Klik row action `Pair TAG` pada baris 'Server Rack 42U - 101'
4. Klik [Cancel]
5. Verifikasi dialog menutup tanpa konfirmasi D-11
6. Verifikasi user tetap di tab Paired

### Cancel pada dialog yang sudah berisi kode (TC-FA-TAG-445)

7. Klik row action `Pair TAG` pada baris 'Server Rack 42U - 101'
8. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
9. Klik [Cancel]
10. Verifikasi dialog judul "Discard Pairing", body "Discard this pairing? Scanned TAGs will not be saved.", tombol [Cancel] [Discard]
11. Verifikasi Dialog Pair TAG masih terbuka di bawah konfirmasi

### Konfirmasi D-11 dengan [Cancel] (TC-FA-TAG-446)

12. Klik [Cancel] pada dialog `Discard Pairing`
13. Verifikasi dialog konfirmasi menutup
14. Verifikasi slot `RFID TAG` tetap menampilkan `RF-00412` dengan badge `Verified`

### Konfirmasi D-11 dengan [Discard] (TC-FA-TAG-447)

15. Klik [Cancel] pada dialog Pair TAG
16. Klik [Discard]
17. Verifikasi dialog konfirmasi dan Dialog Pair TAG menutup

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-444 s.d. 447). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik penutupan Dialog Pair TAG dilanjutkan di spec 105 (TC-FA-TAG-448, 1439, 1442).
- Urutan TC di dalam spec: TC-445, TC-446, dan TC-447 berbagi satu dialog Pair TAG yang berisi `RF-00412` (precondition dan langkah pembuka identik), sehingga langkah 9 sampai 11 menjadi keadaan awal TC-446 dan langkah 12 sampai 14 menjadi keadaan awal TC-447 (langkah 15 adalah langkah TC-447 yang memunculkan konfirmasi D-11 yang sama dengan langkah 10).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 7 (membuka ulang dialog Pair TAG pada popup yang masih terbuka sesudah TC-444).
- Temuan untuk QA:
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; butir pengecualian modul ini belum ada di konvensi (Lampiran A). Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
  - Simulator reader dipakai sebagai langkah rutin (bukan kelas d); mekanisme memindai kode di ButtonScan tidak didefinisikan di TC, PRD, atau LLD dan diminta dari tim FE/BE.
  - Post Condition TC-444 ("Aset tetap Not Paired Yet") dan TC-447 ("Aset tetap Not Paired Yet", "Tag `RF-00412` tetap Available") tanpa langkah observasi di TC tidak diasersi.
