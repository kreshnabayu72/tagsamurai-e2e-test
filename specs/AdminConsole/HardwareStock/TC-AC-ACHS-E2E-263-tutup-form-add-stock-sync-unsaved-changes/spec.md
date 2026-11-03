---
id: TC-AC-ACHS-E2E-263-tutup-form-add-stock-sync-unsaved-changes
title: "Tutup Form Add Stock Sync dan Dialog Unsaved Changes"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-156
  - TC-AC-ACHS-157
coverage:
  web: automated
---

# Tutup Form Add Stock Sync dan Dialog Unsaved Changes

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API).
- Akun aktor: Total Control Principal {accTc} `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (Pre-setup #1; `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Hardware > Stock (Stock List) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): flag Guided Tooltip halaman Stock List, sesi API aktor, seeding Population Stock Pre-setup #16 s.d. #20 dan #27. Suite serial (`parallel: false`).
- Kelas harness: d (simulator reader USB, Pre-setup #25).
- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<jalur>` pada kolom Fixture key; spec tidak menulis nilainya mentah, dan tiap parameter `{...}` di `## Test Steps` dibaca sebagai nilai kunci itu):

| Parameter | Pre-setup item | Peran/atribut | Fixture key |
|---|---|---|---|
| `{accTc}` | #1 | Akun Principal Total Control | `Fixture.hardwareStock.account.p01.totalControl.email`, `Fixture.hardwareStock.account.p01.totalControl.fullName`, `Fixture.hardwareStock.account.p01.totalControl.shortName` |
| `{skuRfd}` | #16, #17, #18 (Tabel A baris 4) | kode SKU Handheld Reader Long Range dengan 18 Available dan 7 In Use | `Fixture.hardwareStock.p16.a[4].sku` |

- Data Pre-setup: SKU `{skuRfd}` (Pre-setup #16); service driver mock Handheld Reader (Pre-setup #25).
- Data Dinamis: perangkat simulasi `SN-ZEBRA-RFD40-100151-{runId}-263`; tidak pernah disimpan (dibuang lewat `[Leave]`).
- Kemampuan teknis (disediakan tim FE): simulator reader USB Pre-setup #25 dengan Serial Number yang dapat diatur; mode simulator dipulihkan di hook `after`.

## Test Steps

### TC-AC-ACHS-156: Cancel dengan tabel Synced Units kosong

1. Ketik Search `{skuRfd}`, tekan Enter
2. Klik `(⋯)` pada baris SKU `{skuRfd}`
3. Klik opsi `Add Stock`
4. Klik `[Cancel]`
5. Verifikasi halaman berpindah ke Stock Detail > Tab Available SKU `{skuRfd}`
6. Verifikasi dialog Unsaved Changes tidak tampil

### TC-AC-ACHS-157: Cancel dengan tabel berisi baris

7. Klik `[Add Stock]` pada toolbar Tab Available (form baru)
8. Atur simulator: perangkat `SN-ZEBRA-RFD40-100151-{runId}-263` terhubung
9. Klik `[Sync]`
10. Klik `[Cancel]`
11. Verifikasi dialog Unsaved Changes tampil dengan pesan "You have unsaved changes. Are you sure you want to leave?"
12. Klik `[Cancel]` pada dialog
13. Verifikasi dialog tertutup dan form tetap terbuka dengan satu baris di tabel Synced Units
14. Klik `[Cancel]` halaman lagi
15. Verifikasi dialog Unsaved Changes tampil
16. Klik `[Leave]`
17. Verifikasi halaman berpindah ke Stock Detail > Tab Available
18. Klik `[Add Stock]` pada toolbar Tab Available (form baru)
19. Verifikasi tabel Synced Units menampilkan empty state `No units synced yet. Connect a device and click Sync.` (baris sebelumnya dibuang)
20. Klik `[Cancel]`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-156, 157). Tidak ada TC hanya-BE di spec ini.
- Menutup form: TC-156 (form bersih) lebih dulu, TC-157 (form dirty) kemudian. Buka form 3 kali (langkah 3, 7, 18) untuk kejadian menutup form pada langkah 4, 10 sampai 16, dan 20.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search (langkah 1), `[Add Stock]` toolbar sebagai pembuka form baru (langkah 7, 18), pengaturan simulator (langkah 8), dan langkah 18 sampai 20 untuk membuktikan Expected "membuang seluruh Synced Units". Langkah 20 menutup form kosong tanpa dialog.
- Temuan untuk QA:
  - TC-157 butir c ("`[Leave]` membuang seluruh Synced Units") tidak punya langkah observasi di TC; spec membuktikannya lewat form baru yang kosong.
  - TC-156 dan TC-157 tidak memuat Post Condition.
