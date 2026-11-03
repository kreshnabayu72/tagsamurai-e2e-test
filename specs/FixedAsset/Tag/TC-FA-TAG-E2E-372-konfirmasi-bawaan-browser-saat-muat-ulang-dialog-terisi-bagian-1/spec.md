---
id: TC-FA-TAG-E2E-372-konfirmasi-bawaan-browser-saat-muat-ulang-dialog-terisi-bagian-1
title: "Muat Ulang: Konfirmasi Bawaan Browser Muncul pada Dialog Replace, Pair, dan Sesi Batch Replace yang Sudah Terisi"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1463
  - TC-FA-TAG-1464
  - TC-FA-TAG-1465
coverage:
  web: automated
---

# Muat Ulang: Konfirmasi Bawaan Browser Muncul pada Dialog Replace, Pair, dan Sesi Batch Replace yang Sudah Terisi

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (akan disediakan).
- Kemampuan teknis (disediakan tim FE/BE): penanganan dialog `beforeunload` bawaan browser (mendeteksi kemunculannya, memilih tetap di halaman, dan memilih muat ulang; tercantum juga di `suite.md`); simulator reader RFID/NFC USB satu reader tersambung, driver terpasang, reader aktif, sudah disinkronkan di Global Settings > Handheld Reader; seed idempotent aset dan stok Tag lewat fixture backend.
- Data (tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis): AST-0220 'Excavator 20 Ton - 220' (Group Plant A, TAG Type Asset Name RFID) punya satu Tag RFID `RF-00130` berstatus Paired; AST-0221 'Excavator 20 Ton - 221' (Group Plant A) punya Tag RFID `RF-00140` berstatus Paired; AST-0101 'Server Rack 42U - 101' (Group Plant A, TAG Type Asset Name RFID, NFC, dan QR) belum punya Tag Paired (Not Paired Yet). Stok Global: Tag RFID `RF-00412` dan `RF-00415` berstatus Available. Spec ini tidak menekan [Submit], jadi tidak ada data yang tersimpan.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan stok Tag dan kondisi reader ke keadaan awal lewat fixture backend. Form dirty ditutup dengan memilih muat ulang pada konfirmasi bawaan browser (kemampuan di atas, S-08). Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1463: Dialog Replace TAG terisi

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
3. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
4. Muat ulang halaman (F5)
5. Verifikasi konfirmasi bawaan browser (beforeunload) muncul
6. Pilih tetap di halaman pada konfirmasi bawaan browser
7. Verifikasi Dialog Replace TAG masih terbuka dan slot `RFID TAG` menampilkan `RF-00412` dengan badge `Verified`
8. Muat ulang halaman (F5)
9. Pilih muat ulang pada konfirmasi bawaan browser

### TC-FA-TAG-1464: Dialog Pair TAG terisi

10. Klik Asset Name 'Server Rack 42U' pada baris grup Plant A untuk membuka Popup Detail
11. Klik tombol teks `Show` di samping field `Not Paired Yet`
12. Klik row action `Pair TAG` pada baris 'Server Rack 42U - 101'
13. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
14. Muat ulang halaman (F5)
15. Verifikasi konfirmasi bawaan browser (beforeunload) muncul
16. Pilih tetap di halaman pada konfirmasi bawaan browser
17. Verifikasi Dialog Pair TAG masih terbuka dan slot `RFID TAG` menampilkan `RF-00412` dengan badge `Verified`
18. Muat ulang halaman (F5)
19. Pilih muat ulang pada konfirmasi bawaan browser

### TC-FA-TAG-1465: sesi Batch Replace TAG terisi

20. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
21. Centang baris 'Excavator 20 Ton - 220' dan 'Excavator 20 Ton - 221'
22. Klik Bulk `Batch Replace TAG`
23. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` aset ke-1 lalu pindai Tag `RF-00412`
24. Muat ulang halaman (F5)
25. Verifikasi konfirmasi bawaan browser (beforeunload) muncul
26. Pilih tetap di halaman pada konfirmasi bawaan browser
27. Verifikasi sesi Batch Replace TAG masih berada di aset ke-1 dan slot `RFID TAG` menampilkan `RF-00412` dengan badge `Verified`
28. Muat ulang halaman (F5)
29. Pilih muat ulang pada konfirmasi bawaan browser

## Notes

- Spec muat ulang dengan dialog `beforeunload` (kelas fungsional). Kemampuan menangani dialog itu tertulis di `## Prerequisites` sehingga reload sah menurut S-08.
- Langkah penghubung (tanpa awalan `Verifikasi`): 8 dan 9, 18 dan 19, 28 dan 29 (menutup form dirty dengan memuat ulang dan memilih muat ulang pada konfirmasi bawaan browser, S-08); 1, 2, 10 sampai 12, 20 sampai 22 (membuka popup dan dialog).
- Pembagian TC lintas spec: TC-FA-TAG-1466, TC-FA-TAG-1467, TC-FA-TAG-1468, dan TC-FA-TAG-1484 ada di spec 373.
- Temuan untuk QA:
  - TC-FA-TAG-1463 sampai TC-FA-TAG-1465 tidak menyebut cara menutup dialog yang terisi sesudah memilih tetap di halaman; spec menutupnya dengan memuat ulang halaman dan memilih muat ulang (langkah 8 dan 9, 18 dan 19, 28 dan 29).
  - TC-FA-TAG-1463 sampai TC-FA-TAG-1465 menyebut Post Condition ("Tidak ada data yang berubah", "Tidak ada aset yang berubah") tanpa langkah observasi; tidak diasersi.
  - Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) tidak bisa bersuffix `{runId}` karena asersi bergantung pada nama dan kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
