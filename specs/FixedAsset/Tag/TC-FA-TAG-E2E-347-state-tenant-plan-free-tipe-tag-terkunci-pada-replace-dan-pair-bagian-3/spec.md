---
id: TC-FA-TAG-E2E-347-state-tenant-plan-free-tipe-tag-terkunci-pada-replace-dan-pair-bagian-3
title: "State Tenant: Plan yang Mengunci Tag NFC pada Dialog Replace TAG dan Tag Combined (Bagian 3)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-307
  - TC-FA-TAG-308
  - TC-FA-TAG-365
coverage:
  web: automated
---

# State Tenant: Plan yang Mengunci Tag NFC pada Dialog Replace TAG dan Tag Combined (Bagian 3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`), karena spec mengubah plan Client.
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader) yang memindai kode Tag di ButtonScan; (2) perubahan plan Client ke plan yang hanya mengizinkan Tag RFID dan QR (Tag NFC terkunci plan) lewat fixture backend; hook `before` menyetelnya dan hook `after` memulihkan plan awal; (3) seed dan pemulihan idempotent lewat fixture backend untuk aset, Tag Paired, stok Tag per tipe, dan Tag combined. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset NFC dan QR | 'Laptop Pro 14 - 8' (AST-0108, Group Plant A, TAG Type Asset Name NFC dan QR) dengan dua Tag Paired: NFC `NF-00092` dan QR `QR-00300` | `aset108` |
| Aset RFID | 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID) dengan Tag RFID `RF-00130` Paired | `aset220` |
| Stok Global Available | Tag QR `QR-00701`, Tag NFC `NF-00500` | `stokAvailable` |
| Tag combined | NFC+QR `NF-00817` / `QR-00817` | `combined817` |

- State yang diubah dan pemulihannya: Client berada di plan yang mengunci Tag NFC sepanjang spec (diatur hook `before`). Hook `after` memulihkan plan awal Client walau spec gagal di tengah. Tidak ada data aset yang berubah (semua aksi ditolak atau dialog ditutup).

## Test Steps

### TC-FA-TAG-307: Tipe tujuan terkunci plan dihapus dari daftar pasang (V-10)

1. Klik Asset Name 'Laptop Pro 14' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Laptop Pro 14 - 8'
3. Centang baris `NF-00092` dan baris `QR-00300`
4. Verifikasi Alert info berisi "This TAG type is not available on your plan." tampil di atas bagian `Replacement TAG`
5. Verifikasi daftar pasang hanya memuat slot `QR TAG`
6. Verifikasi slot `NFC TAG` dihapus dari daftar pasang
7. Muat ulang halaman (F5)

### TC-FA-TAG-308: Tag NFC pada slot RFID ditolak (V-08)

8. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
9. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
10. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
11. Pindai Tag NFC `NF-00500`
12. Verifikasi error inline "This slot needs a RFID TAG."
13. Verifikasi Tag NFC `NF-00500` tidak diterima pada slot `RFID TAG`
14. Muat ulang halaman (F5)

### TC-FA-TAG-365: Tag combined dengan komponen bertipe terkunci plan

15. Klik Asset Name 'Laptop Pro 14' pada baris grup Plant A untuk membuka Popup Detail
16. Klik row action `Replace TAG` pada baris 'Laptop Pro 14 - 8'
17. Centang baris `NF-00092` dan baris `QR-00300`
18. Klik ButtonScan `Scan NFC` pada slot `NFC TAG` lalu pindai Tag `NF-00817`
19. Verifikasi error inline "This TAG type is not available on your plan." untuk komponen yang gagal
20. Verifikasi slot `NFC TAG` tetap `Not scanned`
21. Verifikasi slot `QR TAG` tetap `Not scanned`
22. Muat ulang halaman (F5)

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-307, 308, 365). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: kasus Free plan (TC-FA-TAG-245, 263, 375 di spec 345; TC-FA-TAG-376, 383, 1154, 1314, 1315 di spec 346) dan kasus Pair TAG pada plan yang mengunci Tag NFC (TC-FA-TAG-425, 1476) di spec 384.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 7, 14, dan 22 (muat ulang halaman untuk menutup Dialog Replace TAG dan Popup Detail).
- Langkah 6 (slot `NFC TAG` dihapus) didahului `Verifikasi` daftar pasang memuat slot `QR TAG` di langkah 5 sebagai anchor positif.
- Temuan untuk QA:
  - TC-FA-TAG-307 menyatakan slot `NFC TAG` dihapus dari daftar pasang saat NFC terkunci plan, sedangkan TC-FA-TAG-365 (juga plan yang mengunci NFC) mengklik ButtonScan `Scan NFC` pada slot `NFC TAG`; spec mengikuti masing-masing TC. Perlu ditegaskan apakah slot `NFC TAG` ada atau tidak pada Dialog Replace TAG untuk Tag combined NFC+QR.
  - Post Condition TC-FA-TAG-308 dan 365 ("Tidak ada data yang berubah") tanpa langkah observasi di TC tidak diasersi.
  - TC-FA-TAG-365 menyebut "dua Tag Paired bertipe sesuai" dan kode combined `NF-00817` / `QR-00817`; spec memakai kode itu seperti tertulis.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*, NF-*, QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
