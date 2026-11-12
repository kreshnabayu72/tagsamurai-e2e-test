---
id: TC-FA-TAG-E2E-336-resilience-sesi-batch-replace-dan-pair-kegagalan-server-satu-bagian-1
title: "Resilience: Kegagalan Server pada Satu Aset dalam Sesi Batch Replace TAG (5xx, Timeout, Retry Failed) (Bagian 1)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-405
  - TC-FA-TAG-406
  - TC-FA-TAG-407
coverage:
  web: automated
---

# Resilience: Kegagalan Server pada Satu Aset dalam Sesi Batch Replace TAG (5xx, Timeout, Retry Failed) (Bagian 1)

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata).
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader) yang memindai kode Tag di ButtonScan; (2) `Spectra.intercept` parsial per aset atas penyimpanan sesi Batch Replace: respons 5xx pada aset tertentu dan tidak ada respons sampai timeout pada aset tertentu; hook `after` melepas semua intercept; (3) seed dan pemulihan idempotent lewat fixture backend untuk aset dan Tag; (4) penanganan dialog `beforeunload` (konfirmasi otomatis saat halaman dimuat ulang dengan dialog dirty terbuka), dipakai untuk menutup dialog dirty lewat muat ulang halaman. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Tiga aset Paired | 'Excavator 20 Ton - 220' (AST-0220, Tag RFID `RF-00330`), 'Excavator 20 Ton - 221' (AST-0221, `RF-00140`), 'Excavator 20 Ton - 23' (AST-0023, `RF-00141`), semuanya Group Plant A dengan satu Tag RFID Paired | `asetBatch` |
| Stok Available | Tag RFID `RF-00412`, `RF-00415`, `RF-00416` | `stokAvailable` |

- State yang diubah dan pemulihannya: penyimpanan aset pertama sukses di langkah 6 (AST-0220 menjadi `RF-00412`) dan dipulihkan lewat fixture backend di langkah 16; hook `after` memulihkan ketiga aset ke Tag awal, ketiga Tag stok ke Available, dan melepas semua intercept. Langkah 30 menyimpan AST-0220 menjadi `RF-00412` dan dipulihkan hook `after`.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 6, 30); entri TAG Log Global (langkah 6, 30). Aksi tulis pada langkah 8, 23 ditolak dan tidak menambah entri.

## Test Steps

### TC-FA-TAG-405: Kegagalan 5xx pada aset kedua

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Centang baris 'Excavator 20 Ton - 220', 'Excavator 20 Ton - 221', dan 'Excavator 20 Ton - 23'
3. Klik Bulk `Batch Replace TAG`
4. Pasang intercept 5xx pada penyimpanan aset 'Excavator 20 Ton - 221'
5. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
6. Klik [Submit & next]
7. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00415`
8. Klik [Submit & next]
9. Verifikasi dialog tetap lanjut ke header `Replace TAG · Asset 3 of 3`
10. Verifikasi tidak ada toast gagal untuk aset 'Excavator 20 Ton - 221'
11. Klik [Skip]
12. Verifikasi ringkasan: 'Excavator 20 Ton - 220' berlabel `Done`
13. Verifikasi ringkasan: 'Excavator 20 Ton - 221' berlabel `Failed` dengan alasan "Error, failed to replace asset."
14. Verifikasi ringkasan: 'Excavator 20 Ton - 23' berlabel `Skipped`
15. Lepas intercept
16. Pulihkan 'Excavator 20 Ton - 220' ke Tag `RF-00330` Paired dan `RF-00412` ke Available lewat fixture BE hingga tersimpan
17. Muat ulang halaman (F5)

### TC-FA-TAG-406: Timeout pada aset pertama

18. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
19. Centang baris 'Excavator 20 Ton - 220', 'Excavator 20 Ton - 221', dan 'Excavator 20 Ton - 23'
20. Klik Bulk `Batch Replace TAG`
21. Pasang intercept: server tidak merespons sampai timeout saat menyimpan aset 'Excavator 20 Ton - 220'
22. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
23. Klik [Submit & next]
24. Klik [Skip]
25. Klik [Skip]
26. Verifikasi ringkasan: 'Excavator 20 Ton - 220' berlabel `Failed` dengan alasan "Connection problem. Please try again."

### TC-FA-TAG-407: Retry Failed menyimpan aset setelah server pulih

27. Lepas intercept
28. Klik `[Retry skipped and failed (3)]`
29. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
30. Klik [Submit & next]
31. Verifikasi aset 1 ('Excavator 20 Ton - 220') tersimpan pada percobaan ulang

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-405 s.d. 407). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: TC-FA-TAG-467 dan TC-FA-TAG-468 (kegagalan server pada sesi Batch Pair) ada di spec 337.
- TC-407 dilanjutkan dari ringkasan sesi TC-406 (aset 1 `Failed`, aset 2 dan 3 `Skipped`, tombol `[Retry skipped and failed (3)]` sama dengan precondition TC-407); TC-407 menulis kegagalan pertama sebagai 5xx sedangkan TC-406 memakai timeout, dan Retry tidak bergantung pada jenis kegagalan sebelumnya.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 15 (melepas intercept), 16 (memulihkan data lewat fixture BE hingga tersimpan), 17 (muat ulang halaman untuk menutup dialog ringkasan; dialog `beforeunload` ditangani sesuai Prerequisites).
- Langkah 10 (tidak ada toast gagal) didahului `Verifikasi` header `Replace TAG · Asset 3 of 3` sebagai anchor positif (respons server sudah diproses).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 6, 30); entri TAG Log Global (langkah 6, 30). Aksi tulis pada langkah 8, 23 ditolak dan tidak menambah entri.
- Temuan untuk QA:
  - Post Condition TC-FA-TAG-405 (Tag `RF-00412` Paired pada aset 1, `RF-00140` tetap Paired pada aset 2) dan TC-FA-TAG-406 (Tag `RF-00330` tetap Paired) tanpa langkah observasi di TC tidak diasersi; TC-FA-TAG-407 Expected menyebut "tersimpan pada percobaan ulang" tanpa indikator UI, sehingga langkah 31 mengikuti kalimat TC.
  - TC-FA-TAG-407 mensyaratkan intercept 5xx pada kegagalan pertama dan tidak menyebut aset mana yang gagal; spec mengikuti TC-FA-TAG-406 (aset 1).
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
