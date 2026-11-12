---
id: TC-FA-TAG-E2E-238-modal-changelog-search-per-kolom-bagian-2
title: "Modal Changelog Paired TAG: Search Tidak Mencocokkan Kolom Date dan Tidak Peka Huruf Besar-Kecil (Bagian 2)"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-955
  - TC-FA-TAG-956
coverage:
  web: automated
---

# Modal Changelog Paired TAG: Search Tidak Mencocokkan Kolom Date dan Tidak Peka Huruf Besar-Kecil (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk entri Changelog Paired TAG dengan tanggal dan pelaku persis seperti tabel di bawah; tidak ada endpoint yang dikarang di spec ini. Changelog dalam scope akun Total Control hanya memuat E1 sampai E6 selama spec berjalan; fixture mengembalikan keadaan itu di hook `before` dan `after`.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Entri | Date | Action | Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|---|
| E1 | 26/10/26 10:02 | Replace | Excavator 20 Ton - 50 | TAG | [NFC] NF-00090 | [RFID] RF-00420 | Sari W. |
| E2 | 26/10/26 10:02 | Replace | Excavator 20 Ton - 50 | TAG | [QR] QR-00240 | — | Sari W. |
| E3 | 26/10/26 09:20 | Replace | Excavator 20 Ton - 20 | TAG | [RFID] RF-00130 | [RFID] RF-00415 | Budi S. |
| E4 | 26/10/26 09:14 | Replace | Excavator 20 Ton - 42 | TAG | [QR] QR-00230 | [RFID] RF-00412 | Budi S. |
| E5 | 25/10/26 16:40 | Replace | Forklift Manual - 61 | TAG | [QR] QR-00251 | — | Dedi K. |
| E6 | 25/10/26 08:00 | Report TAG | Excavator 20 Ton - 20 | Report Type | — | Damaged | Rina T. |

  Kunci fixture: `changelogE1E6`.
- State yang diubah: hanya state Search modal; Search dikosongkan lewat `(←)` sesudah tiap kasus. Tidak ada perubahan data bisnis.
- Nilai literal Pre-setup (nama aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Isolasi audit trail (butir A-18 iii): asersi yang bergantung pada isi Changelog atau Event Log lengkap (hanya memuat entri seed) memakai isolasi fixture per scope akun yang dinyatakan di `suite.md` (Kemampuan teknis, 2026-11-05); kemampuan itu disediakan tim FE/BE dan belum dikonfirmasi.

## Test Steps

1. Klik tombol `Changelog` pada Table Tools
2. Verifikasi enam entri E1 sampai E6 tampil
3. Ketik Search `25/10/26 08:00`, tekan Enter
4. Verifikasi `No results found`: kolom Date dikecualikan dari Search
5. Klik `(←)` pada kotak Search
6. Ketik Search `forklift`, tekan Enter
7. Verifikasi baris E5 tampil
8. Klik `(←)` pada kotak Search
9. Klik ikon close untuk menutup modal

## Notes

- Langkah penghubung (S-03): langkah 5 dan 8 (menutup input Search lewat `(←)`), langkah 9 (menutup modal). Langkah 2 adalah `Verifikasi` anchor bahwa data modal sudah termuat sebelum asersi hasil kosong pada langkah 4 (8b butir 2).
- TC-FA-TAG-955 dan TC-FA-TAG-956 langkah "Klik ikon Search di toolbar modal" menyatu dengan langkah "Ketik Search ..., tekan Enter" (bagian 8b butir 9).
- Pembagian TC lintas spec: TC-FA-TAG-940 dan TC-FA-TAG-949 sampai TC-FA-TAG-954 ada di spec 237.
- A-15: nilai literal Pre-setup (nama aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-955 langkah 3 meminta "teks tanggal persis seperti tampil pada kolom Date baris E6" tanpa menuliskan teksnya; spec memakai `25/10/26 08:00` dari Data Uji.
  - Post Condition TC ("tidak ada perubahan data bisnis") tidak punya langkah observasi dan tidak diasersi.
