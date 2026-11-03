---
id: TC-FA-TAG-E2E-342-guard-submit-beruntun-klik-ganda-hanya-satu-efek-bagian-1
title: "Guard Klik Ganda: Pindaian Beruntun, Start Print, dan Receive Ditekan Beruntun Hanya Menghasilkan Satu Efek (Bagian 1)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TAG-257
  - TC-FA-TAG-494
  - TC-FA-TAG-566
coverage:
  web: automated
---

# Guard Klik Ganda: Pindaian Beruntun, Start Print, dan Receive Ditekan Beruntun Hanya Menghasilkan Satu Efek (Bagian 1)

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata).
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader) yang memindai dua kode berurutan tanpa jeda yang dapat diatur dan memindai kode Tag di dialog Receive TAG; (2) `Spectra.intercept` parsial yang menahan respons Start Print dan menghitung request yang terkirim, lalu melepas tahanan respons; hook `after` melepas semua intercept; (3) pengamatan dialog cetak browser (jumlah dialog cetak yang terbuka dan penutupannya); (4) pembacaan jumlah entri Event Log per Tag lewat fixture backend untuk baseline (audit trail permanen, sehingga asersi memakai selisih terhadap baseline); (5) seed dan pemulihan idempotent lewat fixture backend untuk aset, Tag, dan Tag To Be Returned; (6) penanganan dialog `beforeunload` (konfirmasi otomatis saat halaman dimuat ulang dengan dialog terbuka), dipakai untuk menutup dialog lewat muat ulang halaman. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Dua aset Paired | 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID, Tag RFID `RF-00130` Paired) dan 'Excavator 20 Ton - 221' (AST-0221, Group Plant A, Tag RFID `RF-00140` Paired) | `asetPaired` |
| Stok Available | Tag RFID `RF-00412` dan `RF-00415`, Tag NFC `NF-00500` | `stokAvailable` |
| Tag To Be Returned | [RFID] RF-00071 (Last Asset 'Excavator 20 Ton - 2', Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.); [RFID] RF-00088 ('Excavator 20 Ton - 5', Disposal Center, Dedi K.); [NFC] NF-00092 ('Laptop Pro 14 - 8', HQ Warehouse, Rina T.) | `tbr` |
| Quantity Print QR | 2 | `qtyPrint` |

- State yang diubah dan pemulihannya: langkah 21 menerima Tag `RF-00071` (status berubah dari To Be Returned) dan langkah 10 membuat satu batch 2 kode QR; hook `after` memulihkan `RF-00071` ke To Be Returned lewat fixture backend, melepas intercept, dan menutup dialog cetak browser walau spec gagal di tengah.

## Test Steps

### TC-FA-TAG-257: Dua pindaian beruntun cepat di overlay

1. Klik tombol scan `Replace TAG` di toolbar tab Paired
2. Pindai `RF-00130` lalu segera pindai `RF-00140` berurutan tanpa jeda yang dapat diatur
3. Verifikasi hanya satu Dialog Replace TAG terbuka, untuk aset 'Excavator 20 Ton - 220' (pindaian pertama)
4. Verifikasi pindaian kedua diabaikan dan tidak ada dialog ganda
5. Muat ulang halaman (F5)

### TC-FA-TAG-494: Start Print ditekan beruntun

6. Pasang intercept yang menahan respons Start Print beberapa detik dan menghitung request
7. Klik tombol `Print QR` di toolbar tab Paired
8. Isi `Quantity` dengan 2
9. Tunggu toast lama hilang otomatis
10. Klik [Start Print] dua kali beruntun cepat
11. Verifikasi hanya satu request Start Print terkirim
12. Lepas tahanan respons
13. Verifikasi hanya satu Toast "Success, QR labels have been sent to print."
14. Verifikasi hanya satu dokumen cetak (dialog cetak browser terbuka satu kali)
15. Tutup dialog cetak browser
16. Lepas intercept

### TC-FA-TAG-566: Receive ditekan beruntun

17. Buka tab To Be Returned lalu klik tombol "Receive TAG"
18. Pindai Tag RF-00071
19. Catat jumlah entri Event Log untuk RF-00071 sebagai baseline lewat fixture BE
20. Tunggu toast lama hilang otomatis
21. Klik tombol [Receive] dua kali beruntun dengan cepat
22. Verifikasi hanya satu Toast tampil
23. Verifikasi dialog "Receive TAG" menutup
24. Buka Modal "Event Log: To Be Returned"
25. Verifikasi Event Log memuat tepat satu entri baru untuk RF-00071 dibanding baseline
26. Tutup Modal Event Log

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-257, 494, 566). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: Submit Decline Report dan Submit Replace ditekan beruntun (TC-FA-TAG-646, 1344) ada di spec 343; Submit Pair dan Submit & next sesi Batch (TC-FA-TAG-1348, 1349) ada di spec 344; Submit Report TAG dan Cancel Report (TC-FA-TAG-619, 669) ada di spec 351; Submit Receive Manually (TC-FA-TAG-587) ada di spec 383.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 5 (muat ulang halaman untuk menutup Dialog Replace TAG), 9 dan 20 (menunggu toast lama hilang otomatis sebelum hitungan toast), 12 (melepas tahanan respons), 15 (menutup dialog cetak browser), 16 (melepas intercept), 17 (membuka tab To Be Returned), 19 (baseline Event Log, S-12), 26 (menutup Modal Event Log).
- Langkah 11 (hanya satu request) dan langkah 13 (hanya satu toast) diasersi sesudah respons dilepas; langkah 14 (hanya satu dokumen cetak) diasersi sesudah Toast sukses di langkah 13 sebagai anchor positif.
- Temuan untuk QA:
  - TC-FA-TAG-566 menyebut Event Log memuat "tepat satu entri untuk RF-00071"; Event Log adalah audit trail permanen sehingga spec mengasersi tepat satu entri baru terhadap baseline (S-12).
  - Expected TC-FA-TAG-566 butir a ("Toast hanya tampil sekali") tidak menyebut teks toast; spec mengasersi jumlah toast tanpa teks.
  - Post Condition TC-FA-TAG-494 ("Hanya satu batch 2 kode QR dibuat") dan TC-FA-TAG-566 ("Tepat satu entri TAG Log Global "Received" untuk RF-00071") tanpa langkah observasi di TC tidak diasersi.
  - Batch kode QR yang dibuat langkah 10 tidak punya cara pemulihan di TC; spec tidak menghapusnya.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*, NF-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
