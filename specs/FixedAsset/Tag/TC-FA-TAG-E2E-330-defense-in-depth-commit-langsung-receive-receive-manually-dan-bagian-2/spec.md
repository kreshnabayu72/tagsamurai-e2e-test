---
id: TC-FA-TAG-E2E-330-defense-in-depth-commit-langsung-receive-receive-manually-dan-bagian-2
title: "Defense-in-Depth: Search dan Filter Return Group To Be Returned Tidak Menjangkau Group di Luar Scope (Bagian 2)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1309
  - TC-FA-TAG-1310
coverage:
  web: automated
---

# Defense-in-Depth: Search dan Filter Return Group To Be Returned Tidak Menjangkau Group di Luar Scope (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Manage asset & TAG (Read) dengan assign group Disposal Center (`manageAssetTagReadDenganAssignGroupDisposalCenter_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TAG_MR_ADC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk Tag To Be Returned lintas Return Group. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Tag To Be Returned | [RFID] RF-00071 (Last Asset 'Excavator 20 Ton - 2', Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.); [RFID] RF-00088 ('Excavator 20 Ton - 5', Disposal Center, Dedi K.); [NFC] NF-00092 ('Laptop Pro 14 - 8', HQ Warehouse, Rina T.) | `tbr` |
| Kata kunci Search | NF-00092 | `kataKunciDiLuarScope` |

- State yang diubah dan pemulihannya: tidak ada (spec hanya membaca).
- Nilai literal Pre-setup (Asset Name, kode Tag RF-*/NF-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15.

## Test Steps

1. Klik tab `To Be Returned`
2. Klik ikon Search, ketik Search `NF-00092`, tekan Enter
3. Verifikasi tabel menampilkan `No results found`
4. Klik `(←)` pada kotak Search
5. Klik ikon Filter
6. Buka Modal Tree Picker pada field "Return Group"
7. Verifikasi tree memuat group dalam scope user (Disposal Center dan descendant)
8. Verifikasi tree tidak memuat HQ Warehouse
9. Tutup Modal Tree Picker
10. Tutup panel Filter

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1309, 1310). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: TC-FA-TAG-1290 s.d. 1295 dan TC-FA-TAG-1306 (commit langsung ke server) ada di spec 329.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 4 (menutup input Search lewat `(←)` agar tabel kembali ke keadaan awal), 9 dan 10 (menutup modal dan panel Filter).
- Langkah 3 memakai empty state `No results found` hasil Search sebagai anchor positif untuk asersi absence Tag NF-00092 (bagian 8b butir 2); langkah 7 menjadi anchor positif bagi langkah 8.
- A-15: nilai literal Pre-setup (Asset Name, kode Tag RF-*/NF-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-1309 dan TC-FA-TAG-1310 memakai Role dengan "assign group Disposal Center" dan Read; TC tidak menyebut Return Group asli NF-00092 ada di luar scope secara eksplisit selain data Pre-setup (HQ Warehouse).
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
