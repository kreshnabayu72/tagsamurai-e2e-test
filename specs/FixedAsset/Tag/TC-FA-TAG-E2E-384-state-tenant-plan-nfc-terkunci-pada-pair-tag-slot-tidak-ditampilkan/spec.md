---
id: TC-FA-TAG-E2E-384-state-tenant-plan-nfc-terkunci-pada-pair-tag-slot-tidak-ditampilkan
title: "State Tenant: Plan yang Mengunci Tag NFC pada Dialog Pair TAG, Slot Tidak Ditampilkan dan Submit Disabled (Bagian 4)"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TAG-425
  - TC-FA-TAG-1476
coverage:
  web: automated
---

# State Tenant: Plan yang Mengunci Tag NFC pada Dialog Pair TAG, Slot Tidak Ditampilkan dan Submit Disabled (Bagian 4)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`), karena spec mengubah plan Client.
- Kemampuan teknis (disediakan tim FE/BE): (1) perubahan plan Client ke plan yang hanya mengizinkan Tag RFID dan QR (Tag NFC terkunci plan) lewat fixture backend; hook `before` menyetelnya dan hook `after` memulihkan plan awal; (2) pencatat request jaringan (untuk memastikan klik [Submit] tidak mengirim permintaan); (3) simulator reader RFID/NFC USB tersambung, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader sebagai precondition TC (tidak diasersi); (4) seed dan pemulihan idempotent lewat fixture backend untuk aset dan Tag; (5) penanganan dialog `beforeunload` (konfirmasi otomatis saat halaman dimuat ulang dengan dialog terbuka), dipakai untuk menutup dialog lewat muat ulang halaman. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset Not Paired Yet NFC dan QR | 'Laptop Pro 14 - 9' (AST-0109, Group Plant A, TAG Type Asset Name NFC dan QR), belum punya Tag Paired | `aset109` |
| Aset Not Paired Yet NFC saja | 'Laptop Pro 14 - 35' (AST-0135, Group Plant A, TAG Type Asset Name NFC saja), belum punya Tag Paired | `aset135` |
| Stok Global Available | Tag NFC `NF-00500` | `stokAvailable` |

- State yang diubah dan pemulihannya: Client berada di plan yang mengunci Tag NFC sepanjang spec (diatur hook `before`). Hook `after` memulihkan plan awal Client walau spec gagal di tengah. Tidak ada data aset yang berubah (tidak ada Pair yang tersimpan).
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag NF-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada; aksi tulis pada langkah 13 ditolak dan tidak menambah entri Changelog, Event Log, maupun TAG Log.

## Test Steps

### TC-FA-TAG-425: Slot bertipe terkunci plan tidak ditampilkan (V-10)

1. Klik Asset Name 'Laptop Pro 14' pada baris grup Plant A untuk membuka Popup Detail
2. Klik tombol teks `Show` di samping field `Not Paired Yet`
3. Klik row action `Pair TAG` pada baris 'Laptop Pro 14 - 9'
4. Verifikasi Alert info berisi "This TAG type is not available on your plan." tampil di atas bagian `TAG to pair`
5. Verifikasi slot `NFC TAG` tidak ditampilkan karena tipe terkunci plan
6. Muat ulang halaman (F5)

### TC-FA-TAG-1476: Semua tipe wajib terkunci plan

7. Klik Asset Name 'Laptop Pro 14' pada baris grup Plant A untuk membuka Popup Detail
8. Klik tombol teks `Show` di samping field `Not Paired Yet`
9. Klik row action `Pair TAG` pada baris 'Laptop Pro 14 - 35'
10. Verifikasi Alert info berisi "This TAG type is not available on your plan." tampil di atas bagian `TAG to pair`
11. Verifikasi bagian `TAG to pair` tidak memuat slot
12. Verifikasi tombol [Submit] tetap tampil dan Disabled
13. Klik [Submit]
14. Verifikasi klik [Submit] tidak mengirim permintaan
15. Muat ulang halaman (F5)

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-425 dan 1476). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: kasus plan yang mengunci Tag NFC pada Dialog Replace TAG dan Tag combined (TC-FA-TAG-307, 308, 365) ada di spec 347; kasus Free plan ada di spec 345 dan 346.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 6 dan 15 (muat ulang halaman untuk menutup Dialog Pair TAG dan Popup Detail; dialog `beforeunload` ditangani sesuai Prerequisites).
- Langkah 5 (slot `NFC TAG` tidak ditampilkan) didahului `Verifikasi` Alert info di langkah 4 sebagai anchor positif; langkah 11 didahului langkah 10.
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag NF-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada; aksi tulis pada langkah 13 ditolak dan tidak menambah entri Changelog, Event Log, maupun TAG Log.
- Temuan untuk QA:
  - Post Condition TC-FA-TAG-1476 ("Aset 'Laptop Pro 14 - 35' tetap Not Paired Yet") tanpa langkah observasi di TC tidak diasersi.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
