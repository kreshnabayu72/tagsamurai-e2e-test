---
id: TC-FA-TAG-E2E-251-tabel-to-be-returned-sort-dan-column-visibility-bagian-3
title: "Tabel To Be Returned: Setup Column, Ikon Close Membuang Perubahan dan Reset to Default (Bagian 3)"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1016
  - TC-FA-TAG-1017
coverage:
  web: automated
---

# Tabel To Be Returned: Setup Column, Ikon Close Membuang Perubahan dan Reset to Default (Bagian 3)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env usulan; didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite; tab `To Be Returned` dibuka pada langkah 1. Spec tidak mengganti akun; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci `Fixture.fixedAssetTag.<kunci>` pada tabel data ditandai untuk dibuat tim FE (tahap script).
- Data Pre-setup tab To Be Returned (kunci `Fixture.fixedAssetTag.tbr4`; tanpa suffix `{runId}` karena asersi bergantung pada kode, urutan, dan jumlah; tabel To Be Returned dalam scope akun berisi tepat empat Tag ini; Return Group 'Disposal Center' berada di bawah group induk 'Operations'):

| TAG Code | Last Asset | Reason | Return Group | Current Holder | Since |
|---|---|---|---|---|---|
| RF-00071 (RFID) | Excavator 20 Ton - 2 | Disposal | Disposal Center | Dedi K. | 01 Sep 2026 |
| RF-00088 (RFID) | Excavator 20 Ton - 5 | Disposal | Disposal Center | Dedi K. | 20 Sep 2026 |
| NF-00092 (NFC) | Laptop Pro 14 - 8 | Disposal | HQ Warehouse | Rina T. | 22 Sep 2026 |
| RF-00110 (RFID) | Excavator 20 Ton - 10 | Disposal | Disposal Center | Dedi K. | 10 Sep 2026 |

- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk Tag To Be Returned (kode, Last Asset, Reason, Return Group, Current Holder, Since) dan Return Group; tidak ada endpoint yang dikarang di spec ini.
- Pemulihan preferensi kolom: hook `after` spec ini menghapus preferensi kolom di browser (kemampuan disediakan tim FE; bukan lewat `[Reset to Default]`), sesuai daftar di `suite.md`.
- Pemulihan di hook `after`: dataset To Be Returned dikembalikan ke keadaan Pre-setup empat Tag lewat fixture backend bila seeding mengubahnya. Spec ini menyimpan konfigurasi kolom default pada TC-FA-TAG-1017 (langkah 10).

## Test Steps

### TC-FA-TAG-1016: ikon close membuang perubahan preview

1. Klik tab `To Be Returned`
2. Buka modal "Setup Column"
3. Hilangkan centang kolom "Current Holder"
4. Klik ikon close pada modal
5. Verifikasi modal menutup
6. Verifikasi kolom "Current Holder" tampil kembali di tabel

### TC-FA-TAG-1017: Reset to Default mengembalikan pilihan kolom

7. Buka modal "Setup Column"
8. Hilangkan centang kolom "Reason" dan "Since"
9. Klik [Reset to Default]
10. Klik [Save]
11. Verifikasi kolom "Reason" dan "Since" tampil kembali
12. Verifikasi urutan kolom: TAG Code, Last Asset, Reason, Return Group, Current Holder, Since

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1016 s.d. 1017). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: TC-FA-TAG-1005 s.d. 1009 ada di spec 249, TC-FA-TAG-1010 s.d. 1013 ada di spec 250, dan TC-FA-TAG-1014 dan 1015 ada di spec 269.
- Menutup modal Setup Column lewat ikon close pada TC-FA-TAG-1016 langsung menutup modal dan membuang preview (sesuai Expected TC); modal Setup Column bukan form dengan dialog `Unsaved Changes`.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): 1 (membuka tab).
- Asersi tambahan di luar Expected TC: tidak ada.
- Temuan untuk QA:
  - TC-FA-TAG-1017 Expected tidak menyebut apakah kolom Current Holder, Return Group, dan lainnya tetap tampil sesudah Save; spec mengasersi hanya yang disebut TC (Reason dan Since tampil kembali serta urutan kolom).
  - Nilai literal Pre-setup (kode Tag, Last Asset, Return Group, Current Holder) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada kode, urutan, dan jumlah persis; Lampiran A belum memuat butir modul ini, sehingga seeding idempotent dan pemulihan lewat fixture backend (suite serial) dicatat sebagai kebutuhan.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
