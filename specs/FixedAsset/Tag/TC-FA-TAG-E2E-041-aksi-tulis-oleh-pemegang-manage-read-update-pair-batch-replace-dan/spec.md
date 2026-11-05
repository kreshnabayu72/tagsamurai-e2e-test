---
id: TC-FA-TAG-E2E-041-aksi-tulis-oleh-pemegang-manage-read-update-pair-batch-replace-dan
title: "Aksi Tulis oleh Pemegang Manage asset & TAG (Read + Update): Pair TAG, Batch Replace TAG, dan Print QR"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1431
  - TC-FA-TAG-1432
  - TC-FA-TAG-1433
coverage:
  web: automated
---

# Aksi Tulis oleh Pemegang Manage asset & TAG (Read + Update): Pair TAG, Batch Replace TAG, dan Print QR

## Prerequisites

- Mode: FE+BE.
- Akun aktor: tabel "Role yang diuji". Login di hook `before` spec ini sebagai akun pertama pada tabel; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.

Role yang diuji:

| Blok | Role (teks `Role:` TC) | Kode | Email | Env password |
|---|---|---|---|---|
| 1 | Manage asset & TAG (Read + Update) dengan Update pada Group Plant A | MU_UPA | `manageAssetTagReadUpdateDenganUpdatePadaGroupPlantA_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MU_UPA_PASSWORD` |

- Password tidak ditulis di spec atau fixture; nama env bersifat usulan dan didaftarkan tim FE di `spectra.config.ts` dan `.env.example`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite (lihat `suite.md`).
- Fixture: `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai Pre-setup ditulis literal seperti di TC.
- Data: Aset 'Excavator 20 Ton - 51' (AST-0051, Group Plant A, TAG Type Asset Name RFID saja) belum punya Tag Paired (Not Paired Yet); tiga aset di Group Plant A masing-masing punya satu Tag RFID Paired: 'Excavator 20 Ton - 220' (AST-0220, `RF-00330`), 'Excavator 20 Ton - 221' (AST-0221, `RF-00140`), 'Excavator 20 Ton - 23' (AST-0023, `RF-00141`); stok Global: Tag RFID `RF-00412`, `RF-00415`, dan `RF-00416`, Tag NFC `NF-00500`, serta Tag QR `QR-00701` berstatus Available; Tag: RF-00412; Tag baru aset 1: RF-00412; Quantity 3; Start position Left.
- Data: satu reader RFID/NFC tersambung, driver terpasang, reader aktif dan sudah disinkronkan di Global Settings > Handheld Reader.
- Seed dan pemulihan data Pre-setup di atas idempotent lewat fixture backend (disediakan tim FE/BE) di hook `before` dan `after`; data bernama literal sesuai TC.
- Kemampuan teknis (disediakan tim FE/BE): memindai kode Tag lewat simulator reader RFID/NFC USB (satu reader, aktif, sudah disinkronkan di Global Settings > Handheld Reader).
- Kemampuan teknis (disediakan tim FE/BE): membaca dialog cetak browser (jumlah label dan posisi label pertama).
- State global (status Tag, aset, dan stok) dipulihkan lewat fixture; efek log dan batch QR tidak terpulihkan (butir A-15).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Nilai literal Pre-setup (nama aset, kode Tag, ID aset, Return Group) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 18); entri Changelog `Pair TAG` per Tag (langkah 8); entri TAG Log Global (langkah 8, 18); batch kode QR dari `Start Print` (sebanyak Quantity, terdaftar `Available` di registri Global) beserta data cetak (langkah 25).

## Test Steps

### Pair TAG (TC-FA-TAG-1431)

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant A untuk membuka Popup Detail
2. Klik tombol teks `Show` di samping field `Not Paired Yet`
3. Klik kebab baris 'Excavator 20 Ton - 51'
4. Klik row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
5. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`, lalu pindai Tag `RF-00412` dengan simulator reader
6. Verifikasi slot `RFID TAG` menampilkan `RF-00412`
7. Verifikasi Badge `Verified` tampil sebelum Submit
8. Klik `[Submit]`
9. Verifikasi toast `Success, TAG has been paired.` tampil
10. Verifikasi dialog menutup
11. Verifikasi tabel Paired dimuat ulang dan baris 'Excavator 20 Ton - 51' tidak lagi muncul saat filter `Show` Not Paired Yet aktif

### Batch Replace TAG (TC-FA-TAG-1432)

12. Pulihkan Tag `RF-00412` ke keadaan awal (belum Paired) lewat fixture backend (kemampuan disediakan tim FE/BE)
13. Tutup Popup Detail
14. Klik Asset Name `Excavator 20 Ton` pada baris Plant A untuk membuka Popup Detail
15. Centang baris 'Excavator 20 Ton - 220', 'Excavator 20 Ton - 221', dan 'Excavator 20 Ton - 23'
16. Klik Bulk `Batch Replace TAG`
17. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`, lalu pindai Tag `RF-00412` dengan simulator reader
18. Klik `[Submit & next]`
19. Verifikasi dialog berganti ke header `Replace TAG · Asset 2 of 3` untuk 'Excavator 20 Ton - 221'
20. Verifikasi isian aset 1 tidak terbawa ke aset 2 (slot `RFID TAG` `Not scanned`)
21. Tutup dialog `Replace TAG` lewat `✕`, lalu tutup Popup Detail

### Start Print Print QR (TC-FA-TAG-1433)

22. Klik tombol `Print QR` di toolbar tab Paired
23. Isi `Quantity` dengan 3
24. Pilih Start position `Left`
25. Klik `[Start Print]`
26. Verifikasi State loading tampil pada `[Start Print]` selama proses
27. Verifikasi dialog cetak browser terbuka dengan 3 label
28. Verifikasi Label pertama berada di kolom kiri baris pertama
29. Verifikasi dialog `Print QR` menutup
30. Verifikasi toast `Success, QR labels have been sent to print.` tampil

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md`. Tidak ada TC hanya-BE.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 2, 12, 13, 21.
- Aset 'Excavator 20 Ton - 51' dan 'Excavator 20 Ton - 220' sampai 'Excavator 20 Ton - 23' adalah data Pre-setup yang diubah spec ini (Pair TAG, Batch Replace TAG aset 1); fixture backend memulihkannya ke keadaan awal di hook `after`.
- Langkah 12 memulihkan `RF-00412` ke keadaan awal sebelum dipindai lagi di langkah 17; tanpa pemulihan, Pair di langkah 8 membuat Tag itu sudah Paired (S-09).
- Simulator reader dipakai sebagai langkah rutin untuk memindai Tag; spec ini tidak menguji kondisi reader.
- A-15: nilai literal Pre-setup (nama aset, kode Tag, ID aset, Return Group) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 18); entri Changelog `Pair TAG` per Tag (langkah 8); entri TAG Log Global (langkah 8, 18); batch kode QR dari `Start Print` (sebanyak Quantity, terdaftar `Available` di registri Global) beserta data cetak (langkah 25).
- Temuan untuk QA:
  - Role Matrix memakai satu akun Pre-setup per Role; TC tidak menyebut kunci akun, sehingga akun dipilih dari baris Pre-setup bernama dasar sama.
  - Post Condition TC tanpa langkah observasi tidak diasersi (S-01). Post Condition TC-1431 sampai TC-1433 (Tag Paired, data cetak tersimpan, tidak ada entri Changelog, Activity Log, atau System Log) tidak punya langkah observasi di TC dan tidak diasersi.
  - TC-1432 tidak menyebut cara menutup sesi Batch Replace setelah aset 1 disimpan; spec menutup dialog lewat `✕` sebagai langkah penghubung dan tidak mengasumsikan dialog Unsaved Changes (isian aset 2 belum diubah).
  - TC-1431 memakai filter `Show` Not Paired Yet pada Popup Detail yang tetap terbuka sesudah Submit; spec menutup Popup Detail sebelum TC-1432 sebagai langkah penghubung.
