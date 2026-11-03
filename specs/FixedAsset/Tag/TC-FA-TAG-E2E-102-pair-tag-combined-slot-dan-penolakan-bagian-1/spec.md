---
id: TC-FA-TAG-E2E-102-pair-tag-combined-slot-dan-penolakan-bagian-1
title: "Pair TAG: Tag Combined Mengisi Slot dan Penolakan (Bagian 1)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-435
  - TC-FA-TAG-436
  - TC-FA-TAG-437
  - TC-FA-TAG-438
  - TC-FA-TAG-439
coverage:
  web: automated
---

# Pair TAG: Tag Combined Mengisi Slot dan Penolakan (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`; nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader) yang memindai kode Tag di ButtonScan; (2) seed dan pemulihan idempotent lewat fixture backend untuk aset Not Paired Yet dan Tag combined Available; tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset RFID saja | 'Excavator 20 Ton - 51' (AST-0051, Group Plant A, TAG Type Asset Name RFID saja), Not Paired Yet | `aset51` |
| Aset NFC dan QR | 'Laptop Pro 14 - 9' (AST-0109, Group Plant A, TAG Type Asset Name NFC dan QR), Not Paired Yet | `aset109` |
| Aset tiga tipe | 'Server Rack 42U - 101' (AST-0101, Group Plant A, TAG Type Asset Name RFID, NFC, dan QR), Not Paired Yet | `aset101` |
| Combined NFC+QR | `NF-00810` / `QR-00810` Available (satu unit) | `combined810` |
| Combined RFID+QR | `RF-00811` / `QR-00811` Available (satu unit) | `combined811` |
| Combined RFID+NFC+QR | `RF-00812` / `NF-00812` / `QR-00812` Available (satu unit) | `combined812` |

- State yang diubah dan pemulihannya: Tag combined `NF-00810` / `QR-00810` dipasangkan pada 'Laptop Pro 14 - 9' di langkah terakhir; hook `after` memulihkan aset ke Not Paired Yet dan Tag combined ke Available lewat fixture backend.

## Test Steps

### Tag combined ditolak pada satu slot (TC-FA-TAG-437)

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik tombol teks `Show` di samping field `Not Paired Yet`
3. Klik row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
4. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00811`
5. Verifikasi error inline "This TAG is combined. It can only fill multiple slots."
6. Verifikasi slot `RFID TAG` tetap kosong
7. Klik [Cancel]

### Pola dan komponen combined tidak sesuai slot (TC-FA-TAG-438, TC-FA-TAG-439)

8. Tutup Popup Detail
9. Klik Asset Name 'Laptop Pro 14' pada baris grup Plant A untuk membuka Popup Detail
10. Klik tombol teks `Show` di samping field `Not Paired Yet`
11. Klik row action `Pair TAG` pada baris 'Laptop Pro 14 - 9'
12. Klik ButtonScan `Scan NFC` pada slot `NFC TAG` lalu pindai Tag `RF-00811`
13. Verifikasi error inline "This combined TAG doesn't match the open slots."
14. Verifikasi slot `NFC TAG` dan `QR TAG` tetap `Not scanned`
15. Klik [Cancel] untuk membersihkan error inline sebelum kasus berikutnya
16. Klik row action `Pair TAG` pada baris 'Laptop Pro 14 - 9'
17. Klik ButtonScan `Scan NFC` pada slot `NFC TAG` lalu pindai Tag `RF-00812`
18. Verifikasi error inline "This combined TAG doesn't match the open slots."
19. Klik [Cancel]

### Tag combined tiga komponen mengisi tiga slot (TC-FA-TAG-436)

20. Tutup Popup Detail
21. Klik Asset Name 'Server Rack 42U' pada baris grup Plant A untuk membuka Popup Detail
22. Klik tombol teks `Show` di samping field `Not Paired Yet`
23. Klik row action `Pair TAG` pada baris 'Server Rack 42U - 101'
24. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00812`
25. Verifikasi slot `RFID TAG`, `NFC TAG`, dan `QR TAG` terisi dan berbadge `Verified`
26. Klik ikon close dialog Pair TAG
27. Verifikasi dialog judul "Discard Pairing", body "Discard this pairing? Scanned TAGs will not be saved.", tombol [Cancel] [Discard]
28. Klik [Discard]

### Tag combined NFC+QR berhasil dipasangkan (TC-FA-TAG-435)

29. Tutup Popup Detail
30. Klik Asset Name 'Laptop Pro 14' pada baris grup Plant A untuk membuka Popup Detail
31. Klik tombol teks `Show` di samping field `Not Paired Yet`
32. Klik row action `Pair TAG` pada baris 'Laptop Pro 14 - 9'
33. Klik ButtonScan `Scan NFC` pada slot `NFC TAG` lalu pindai Tag `NF-00810`
34. Verifikasi slot `NFC TAG` dan `QR TAG` terisi dan berbadge `Verified` dari satu pindaian
35. Klik [Submit]
36. Verifikasi toast "Success, TAG has been paired."

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-435 s.d. 439). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik Tag combined pada Pair TAG dilanjutkan di spec 103 (TC-FA-TAG-440 s.d. 443).
- Urutan TC di dalam spec: penolakan tanpa perubahan dahulu (TC-437, TC-438, TC-439), lalu TC-436 (pindaian terisi lalu dibuang), dan TC-435 terakhir karena menyimpan perubahan.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 7, 19 ([Cancel] pada dialog tanpa isian, tanpa konfirmasi D-11), 15 dan 16 (membersihkan error inline identik antara TC-438 dan TC-439 dengan menutup dan membuka ulang dialog), serta 8, 20, 29 (menutup Popup Detail sebelum membuka popup grup lain).
- Spec di atas smell 35 langkah (36 langkah). Alasan: seluruh blok satu topik (Tag combined pada dialog Pair TAG) dengan reader yang sama, satu kelas, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-TAG-437 butir b ("slot `RFID TAG` tetap kosong") tidak menyebut label slot; spec mengasersinya sebagaimana tertulis.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; butir pengecualian modul ini belum ada di konvensi (Lampiran A). Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
  - Simulator reader dipakai sebagai langkah rutin (bukan kelas d); mekanisme memindai kode di ButtonScan tidak didefinisikan di TC, PRD, atau LLD dan diminta dari tim FE/BE.
  - Post Condition TC-435 ("Tag combined Paired pada 'Laptop Pro 14 - 9'") dan TC-437 ("Tidak ada perubahan data") tanpa langkah observasi di TC tidak diasersi.
