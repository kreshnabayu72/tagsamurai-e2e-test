---
id: TC-FA-TAG-E2E-345-state-tenant-plan-free-tipe-tag-terkunci-pada-replace-dan-pair-bagian-1
title: "State Tenant: Free Plan Mengunci Seluruh Tipe Pengganti pada Scan Replace dan Row Action Replace TAG (Bagian 1)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-245
  - TC-FA-TAG-263
  - TC-FA-TAG-375
coverage:
  web: automated
---

# State Tenant: Free Plan Mengunci Seluruh Tipe Pengganti pada Scan Replace dan Row Action Replace TAG (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`), karena spec mengubah plan Client dan stok Tag di registri Global.
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader) yang memindai kode Tag di overlay scan; (2) perubahan plan Client (Free plan: hanya Tag QR yang dikelola) lewat fixture backend atau pelaku kedua (Admin) lewat sesi API (login API password, tidak dihitung sebagai sesi web; lihat `suite.md`); akun Admin disediakan tim FE; hook `before` menyetel Client ke Free plan dan hook `after` memulihkan plan awal; (3) seed dan pemulihan idempotent lewat fixture backend untuk aset dan stok Tag per tipe di registri Global. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset Paired | 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID) dengan satu Tag RFID `RF-00330` Paired | `aset220` |
| Stok Global Available | Tag RFID `RF-00412` dan `RF-00415`, Tag NFC `NF-00500` | `stokAvailable` |

- State yang diubah dan pemulihannya: Client berada di Free plan sepanjang spec (diatur hook `before`); langkah 6 mengosongkan stok Tag RFID Available dan dipulihkan di langkah 12. Hook `after` memulihkan plan awal Client dan stok Tag RFID walau spec gagal di tengah. Tidak ada data aset yang berubah (semua aksi ditolak atau hanya membaca).
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*, NF-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan hanya mengubah data lewat fixture backend (langkah 6, 12) yang menyiapkan atau memulihkan state.

## Test Steps

### TC-FA-TAG-245: Scan Tag saat seluruh tipe pengganti terkunci plan (D-12)

1. Klik tombol scan `Replace TAG` di toolbar tab Paired
2. Pindai Tag `RF-00330`
3. Verifikasi dialog judul "Cannot Replace TAG", body "This TAG type is not available on your plan.", tombol [OK]
4. Verifikasi Dialog Replace TAG tidak terbuka
5. Klik [OK]

### TC-FA-TAG-263: Urutan pemeriksaan stok 0 sebelum plan (D-08 sebelum D-12)

6. Kosongkan stok Tag RFID berstatus Available di registri Global lewat fixture BE hingga tersimpan
7. Klik tombol scan `Replace TAG` di toolbar tab Paired
8. Pindai Tag `RF-00330`
9. Verifikasi dialog judul "Cannot Replace TAG", body "No available RFID TAG in stock. Activate TAG in Global Settings > TAG.", tombol [OK]
10. Verifikasi dialog D-12 dengan body "This TAG type is not available on your plan." tidak tampil
11. Klik [OK]
12. Pulihkan stok Tag RFID `RF-00412` dan `RF-00415` ke Available lewat fixture BE hingga tersimpan

### TC-FA-TAG-375: Row action Replace TAG Disabled dengan tooltip (S-08)

13. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
14. Arahkan kursor ke row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
15. Verifikasi row action `Replace TAG` tetap tampil (visible) namun berstatus Disabled
16. Verifikasi tooltip "This TAG type is not available on your plan."
17. Klik row action `Replace TAG`
18. Verifikasi Dialog Replace TAG tidak terbuka

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-245, 263, 375). Tidak ada TC hanya-BE.
- Urutan TC di spec: TC-FA-TAG-245, 263, lalu 375, supaya kedua TC scan toolbar berurutan sebelum Popup Detail dibuka, dan stok RFID dikosongkan hanya untuk TC-FA-TAG-263 lalu dipulihkan sebelum TC-FA-TAG-375 (precondition stok tersedia).
- Pembagian TC lintas spec: kasus Free plan lain (TC-FA-TAG-376, 383, 1154, 1314, 1315) ada di spec 346; kasus plan yang mengunci Tag NFC (TC-FA-TAG-307, 308, 365) ada di spec 347 dan (TC-FA-TAG-425, 1476) di spec 384.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 5 dan 11 (menutup dialog dengan [OK]), 6 dan 12 (mengosongkan dan memulihkan stok Tag RFID lewat fixture BE).
- Langkah 4 (Dialog Replace TAG tidak terbuka) didahului `Verifikasi` dialog "Cannot Replace TAG" di langkah 3 sebagai anchor positif; langkah 10 didahului langkah 9 dan langkah 18 didahului langkah 15 dan 16.
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*, NF-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan hanya mengubah data lewat fixture backend (langkah 6, 12) yang menyiapkan atau memulihkan state.
- Temuan untuk QA:
  - Post Condition TC-FA-TAG-245 ("Tidak ada data yang berubah") tanpa langkah observasi di TC tidak diasersi.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
