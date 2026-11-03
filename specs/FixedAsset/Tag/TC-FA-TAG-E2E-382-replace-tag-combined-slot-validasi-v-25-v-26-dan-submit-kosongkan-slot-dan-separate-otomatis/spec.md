---
id: TC-FA-TAG-E2E-382-replace-tag-combined-slot-validasi-v-25-v-26-dan-submit-kosongkan-slot-dan-separate-otomatis
title: "Replace dengan Tag Combined: Kosongkan Slot Hasil Combined dan Separate Otomatis saat Submit"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-367
  - TC-FA-TAG-368
coverage:
  web: automated
---

# Replace dengan Tag Combined: Kosongkan Slot Hasil Combined dan Separate Otomatis saat Submit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB yang memindai kode Tag (satu reader tersambung, driver terpasang, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader); seed dan pemulihan idempotent lewat fixture backend untuk aset, atribut aset, Tag per status registri, stok Tag, dan laporan Tag; pembacaan status registri Tag dan state backend lewat fixture BE (dipakai hanya untuk butir Expected TC).
- Data: aset 'Excavator 20 Ton - 60' (AST-0060, Group Plant A, TAG Type Asset Name RFID dan QR) dengan satu Tag combined Paired RFID `RF-00800` + QR `QR-00800`; 'Laptop Pro 14 - 8' (AST-0108, TAG Type Asset Name NFC dan QR) dengan Tag NFC `NF-00092` dan Tag QR `QR-00300` Paired; Tag combined NFC+QR `NF-00810` / `QR-00810` Available (satu unit); Tag RFID `RF-00412`, Tag NFC `NF-00500`, dan Tag QR `QR-00701` Available.
- Fixture: `Fixture.fixedAssetTag` belum ada (disediakan tim FE); nilai data pada langkah dibaca dari TC dan dipetakan ke fixture itu oleh tahap script.
- State global: stok Tag per tipe di registri Global dan status Tag (Paired, Available, Damaged/Missing, keluar dari registri) diubah oleh aksi Replace; fixture backend memulihkannya di hook `before`, di langkah penghubung antar-TC, dan di hook `after` yang tetap jalan walau spec gagal di tengah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-367: Memindai ulang salah satu slot hasil combined mengosongkan semua slot hasil combined

1. Klik Asset Name 'Laptop Pro 14' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Laptop Pro 14 - 8'
3. Centang baris `NF-00092` dan baris `QR-00300`
4. Klik ButtonScan `Scan NFC` pada slot `NFC TAG`
5. Pindai Tag `NF-00810` dengan reader
6. Klik ButtonScan `Scan NFC` pada slot `NFC TAG`
7. Pindai Tag `NF-00500` dengan reader
8. Verifikasi slot `QR TAG` kembali `Not scanned` (slot hasil combined dikosongkan)
9. Verifikasi slot `NFC TAG` menampilkan `NF-00500` dengan badge `Verified`
10. Klik [Cancel] pada dialog Replace TAG
11. Verifikasi dialog `Discard Replacement` dengan body "Discard this replacement? Scanned TAGs will not be saved." dan tombol [Cancel] [Discard] tampil
12. Klik [Discard]

### TC-FA-TAG-368: Submit dengan Tag lama combined melepas semua komponen dan Separate otomatis

13. Tutup Popup Detail Assets
14. Klik tombol scan `Replace TAG` di toolbar tab Paired
15. Pindai Tag `RF-00800` dengan reader
16. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
17. Pindai Tag `RF-00412` dengan reader
18. Klik ButtonScan `Scan QR` pada slot `QR TAG`
19. Pindai Tag `QR-00701` dengan reader
20. Klik [Submit]
21. Verifikasi toast "Success, TAG has been replaced."
22. Verifikasi dialog menutup

## Notes

- Langkah penghubung (S-03): dialog TC-FA-TAG-367 yang terisi ditutup lewat [Cancel] (langkah 10), verifikasi dialog `Discard Replacement`, dan [Discard] (langkah 12); TC-FA-TAG-368 (overlay scan) berada di akhir sesudah Popup ditutup (langkah 13).
- Pembagian TC lintas spec: TC-FA-TAG-355 sampai 364 ada di spec 081 dan 082; TC-FA-TAG-366, 369, dan 370 ada di spec 083.
- Data literal Pre-setup (kode aset AST-*, Asset Name, kode Tag) dipakai persis seperti di TC tanpa suffix `{runId}`, karena asersi bergantung pada nama dan kode itu; seeding idempotent dan pemulihan dijamin fixture backend (suite.md).
- Temuan untuk QA:
  - TC tidak menyatakan apakah dialog yang hanya berisi Tag lama terpindai (tanpa Tag pengganti) memunculkan konfirmasi D-09 saat [Cancel]; spec memakai dialog TC-FA-TAG-367 yang sudah terisi sehingga dialog `Discard Replacement` diasersi (selaras TC-FA-TAG-311).
  - Post Condition TC-FA-TAG-368 (`RF-00412` dan `QR-00701` Paired, `RF-00800` Available, `QR-00800` keluar dari registri, Event Log Separate dengan sumber Replace pada tag-combine) tidak punya langkah observasi dan tidak diasersi.
  - Tidak ada Post Condition pada TC-FA-TAG-367.
