---
id: TC-FA-TAG-E2E-383-guard-submit-receive-manually-ditekan-beruntun-hanya-satu-entri
title: "Guard Klik Ganda: Submit Receive Manually Ditekan Beruntun Hanya Menulis Satu Entri Event Log (Bagian 5)"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TAG-587
coverage:
  web: automated
---

# Guard Klik Ganda: Submit Receive Manually Ditekan Beruntun Hanya Menulis Satu Entri Event Log (Bagian 5)

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata).
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) `Spectra.intercept` parsial yang menahan respons Submit Receive Manually beberapa detik dan menghitung request yang terkirim, lalu melepas tahanan respons (TC-FA-TAG-587 tidak menyebutnya; spec memakainya agar state loading dan jumlah request teramati); hook `after` melepas intercept; (2) pembacaan jumlah entri Event Log per Tag lewat fixture backend untuk baseline (audit trail permanen, sehingga asersi memakai selisih terhadap baseline); (3) seed dan pemulihan idempotent lewat fixture backend untuk Tag To Be Returned. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Tag To Be Returned | [RFID] RF-00071 (Last Asset 'Excavator 20 Ton - 2', Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.); [RFID] RF-00088 ('Excavator 20 Ton - 5', Disposal Center, Dedi K.); [NFC] NF-00092 ('Laptop Pro 14 - 8', HQ Warehouse, Rina T.) | `tbr` |
| Note | Tag rusak saat serah terima | `noteReceiveManually` |

- State yang diubah dan pemulihannya: langkah 6 menandai `RF-00071` sebagai Damaged/Missing (keluar dari To Be Returned). Hook `after` memulihkan `RF-00071` ke To Be Returned lewat fixture backend dan melepas intercept walau spec gagal di tengah.
- Nilai literal Pre-setup (kode Tag RF-*, NF-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Event Log To Be Returned (Method `Manual`) (langkah 6); entri TAG Log Global `Marked Damaged/Missing` (langkah 6). Jumlah entri Event Log dibaca sebagai baseline pada langkah 4; log itu permanen dan tidak dipulihkan fixture, dan asersi entri baru memakai selisih terhadap baseline: butir A-18.

## Test Steps

### TC-FA-TAG-587: Submit Receive Manually ditekan beruntun

1. Buka tab To Be Returned lalu buka menu aksi baris RF-00071
2. Klik "Receive Manually"
3. Isi Textarea "Note" dengan "Tag rusak saat serah terima"
4. Catat jumlah entri Event Log untuk RF-00071 sebagai baseline lewat fixture BE
5. Pasang intercept yang menahan respons Receive Manually beberapa detik dan menghitung request
6. Klik tombol [Submit] dua kali beruntun dengan cepat
7. Verifikasi tombol [Submit] tetap tampil dan Disabled dengan state loading
8. Verifikasi penekanan ulang tidak mengirim permintaan kedua (hanya satu request terkirim)
9. Lepas tahanan respons dan intercept
10. Buka Modal "Event Log: To Be Returned"
11. Verifikasi Event Log memuat tepat satu entri baru untuk RF-00071 dibanding baseline
12. Tutup Modal Event Log

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-587). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: klik ganda pada pindaian, Start Print, dan Receive (TC-FA-TAG-257, 494, 566) ada di spec 342; Submit Decline Report dan Submit Replace (TC-FA-TAG-646, 1344) ada di spec 343; Submit Pair dan Submit & next sesi Batch (TC-FA-TAG-1348, 1349) ada di spec 344; Submit Report TAG dan Cancel Report (TC-FA-TAG-619, 669) ada di spec 351. Receive Manually gagal (TC-FA-TAG-583 s.d. 585) ada di spec 340.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 (membuka tab To Be Returned), 4 (baseline Event Log, S-12), 5 (memasang intercept penahan respons), 9 (melepas tahanan respons dan intercept), 12 (menutup Modal Event Log).
- Langkah 8 (hanya satu request) diasersi sebelum respons dilepas, mengikuti urutan state (bagian 8b butir 5).
- A-15: nilai literal Pre-setup (kode Tag RF-*, NF-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Event Log To Be Returned (Method `Manual`) (langkah 6); entri TAG Log Global `Marked Damaged/Missing` (langkah 6).
- Temuan untuk QA:
  - TC-FA-TAG-587 menyebut Event Log memuat "tepat satu entri untuk RF-00071"; Event Log adalah audit trail permanen sehingga spec mengasersi tepat satu entri baru terhadap baseline (S-12).
  - TC-FA-TAG-587 tidak menyebut respons Submit ditahan, padahal Expected butir a (Disabled dengan state loading) hanya teramati saat respons tertahan; spec menahan respons.
  - Post Condition TC-FA-TAG-587 ("Tepat satu entri TAG Log Global "Marked Damaged/Missing" untuk RF-00071") tanpa langkah observasi di TC tidak diasersi.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
