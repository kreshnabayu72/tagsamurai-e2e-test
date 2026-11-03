---
id: TC-FA-TAG-E2E-335-resilience-submit-pair-gagal-timeout-dan-layanan-global-tidak-terjangkau
title: "Resilience: Submit Pair Gagal (5xx, Timeout, Layanan Global Tidak Terjangkau) Mempertahankan Dialog dan Slot"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1345
  - TC-FA-TAG-1346
  - TC-FA-TAG-1347
coverage:
  web: automated
---

# Resilience: Submit Pair Gagal (5xx, Timeout, Layanan Global Tidak Terjangkau) Mempertahankan Dialog dan Slot

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata).
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader) yang memindai kode Tag di ButtonScan; (2) `Spectra.intercept` parsial atas Submit Pair: respons 5xx, tidak ada respons sampai timeout, dan layanan Global tidak terjangkau; hook `after` melepas semua intercept; (3) seed dan pemulihan idempotent lewat fixture backend untuk aset Not Paired Yet dan stok Global; (4) penanganan dialog `beforeunload` (konfirmasi otomatis saat halaman dimuat ulang dengan dialog dirty terbuka), dipakai untuk menutup dialog dirty lewat muat ulang halaman. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset tiga tipe | 'Server Rack 42U - 101' (AST-0101, Group Plant A, TAG Type Asset Name RFID, NFC, dan QR), Not Paired Yet | `aset101` |
| Aset RFID | 'Excavator 20 Ton - 51' (AST-0051, Group Plant A, TAG Type Asset Name RFID saja), Not Paired Yet | `aset51` |
| Aset NFC dan QR | 'Laptop Pro 14 - 9' (AST-0109, Group Plant A, TAG Type Asset Name NFC dan QR), Not Paired Yet | `aset109` |
| Stok Available | Tag RFID `RF-00412`, Tag NFC `NF-00500`, Tag QR `QR-00701` | `stokAvailable` |

- State yang diubah dan pemulihannya: intercept dipasang di langkah 7, 18, dan 29 dan dilepas di langkah 12, 22, dan 32; hook `after` melepas semua intercept dan memastikan ketiga aset Not Paired Yet dan ketiga Tag Available.

## Test Steps

### TC-FA-TAG-1345: Submit Pair gagal 5xx

1. Klik Asset Name 'Server Rack 42U' pada baris grup Plant A
2. Klik `Show` di samping `Not Paired Yet`
3. Klik row action `Pair TAG` pada baris 'Server Rack 42U - 101'
4. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
5. Klik ButtonScan `Scan NFC` pada slot `NFC TAG` lalu pindai Tag `NF-00500`
6. Klik ButtonScan `Scan QR` pada slot `QR TAG` lalu pindai Tag `QR-00701`
7. Pasang intercept 5xx pada Submit Pair
8. Klik [Submit]
9. Verifikasi toast "Error, failed to pair TAG."
10. Verifikasi Dialog Pair TAG tetap terbuka dengan ketiga slot tetap `Verified`
11. Verifikasi tombol [Submit] kembali dapat ditekan
12. Lepas intercept
13. Muat ulang halaman (F5)

### TC-FA-TAG-1346: Submit Pair timeout

14. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A
15. Klik `Show` di samping `Not Paired Yet`
16. Klik row action `Pair TAG` pada baris 'Excavator 20 Ton - 51'
17. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
18. Pasang intercept: server tidak merespons Submit Pair sampai timeout
19. Klik [Submit]
20. Verifikasi toast "Error, failed to pair TAG."
21. Verifikasi Dialog Pair TAG tetap terbuka
22. Lepas intercept
23. Muat ulang halaman (F5)

### TC-FA-TAG-1347: Layanan Global tidak terjangkau

24. Klik Asset Name 'Laptop Pro 14' pada baris grup Plant A
25. Klik `Show` di samping `Not Paired Yet`
26. Klik row action `Pair TAG` pada baris 'Laptop Pro 14 - 9'
27. Klik ButtonScan `Scan NFC` pada slot `NFC TAG` lalu pindai Tag `NF-00500`
28. Klik ButtonScan `Scan QR` pada slot `QR TAG` lalu pindai Tag `QR-00701`
29. Pasang intercept: layanan Global tidak terjangkau saat Submit
30. Klik [Submit]
31. Verifikasi toast "Error, failed to pair TAG."
32. Lepas intercept

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1345 s.d. 1347). Tidak ada TC hanya-BE.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 12, 22, dan 32 (melepas intercept), 13 dan 23 (muat ulang halaman untuk menutup dialog dirty dan Popup Detail; dialog `beforeunload` ditangani sesuai Prerequisites).
- Temuan untuk QA:
  - Post Condition TC-FA-TAG-1345 s.d. 1347 (aset tetap Not Paired Yet, Tag tetap Available, tidak ada pairing sebagian) tanpa langkah observasi di TC tidak diasersi.
  - TC-FA-TAG-1347 tidak menyebut cara membuat layanan Global tidak terjangkau; spec menuliskannya sebagai kemampuan intercept yang disediakan tim FE/BE. Expected TC hanya toast; dialog tidak diasersi.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
