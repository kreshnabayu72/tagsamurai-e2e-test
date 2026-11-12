---
id: TC-FA-TAG-E2E-241-modal-changelog-pagination-format-isi-dan-download
title: "Modal Changelog Paired TAG: Format Isi Baris Replace, Download CSV, dan Pagination"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-966
  - TC-FA-TAG-967
  - TC-FA-TAG-969
coverage:
  web: automated
---

# Modal Changelog Paired TAG: Format Isi Baris Replace, Download CSV, dan Pagination

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) seed dan pemulihan idempotent lewat fixture backend untuk entri Changelog Paired TAG (dua keadaan di bawah); (2) pembaca berkas unduhan CSV untuk memeriksa nama dan format berkas; tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE). Keadaan 1 (langkah 1 sampai 11): Changelog dalam scope akun Total Control hanya memuat E1 sampai E6; fixture membentuknya di hook `before`.

| Entri | Date | Action | Name | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|---|
| E1 | 26/10/26 10:02 | Replace | Excavator 20 Ton - 50 | TAG | [NFC] NF-00090 | [RFID] RF-00420 | Sari W. |
| E2 | 26/10/26 10:02 | Replace | Excavator 20 Ton - 50 | TAG | [QR] QR-00240 | — | Sari W. |
| E3 | 26/10/26 09:20 | Replace | Excavator 20 Ton - 20 | TAG | [RFID] RF-00130 | [RFID] RF-00415 | Budi S. |
| E4 | 26/10/26 09:14 | Replace | Excavator 20 Ton - 42 | TAG | [QR] QR-00230 | [RFID] RF-00412 | Budi S. |
| E5 | 25/10/26 16:40 | Replace | Forklift Manual - 61 | TAG | [QR] QR-00251 | — | Dedi K. |
| E6 | 25/10/26 08:00 | Report TAG | Excavator 20 Ton - 20 | Report Type | — | Damaged | Rina T. |

  Kunci fixture: `changelogE1E6`. Keadaan 2 (langkah 13 sampai 20): Changelog dalam scope memuat 25 entri Replace (kunci `changelog25Replace`); langkah 12 membentuknya.
- State yang diubah dan pemulihannya: isi Changelog dalam scope diganti dari keadaan 1 ke keadaan 2 pada langkah 12; hook `after` (tetap jalan walau spec gagal) memulihkan Changelog ke keadaan awal lewat fixture backend yang sama. Berkas CSV hasil unduhan dibuang oleh hook `after`. Tidak ada perubahan data bisnis lain.
- Nilai literal Pre-setup (nama aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan hanya mengubah data lewat fixture backend (langkah 12) yang menyiapkan atau memulihkan state.
- Isolasi audit trail (butir A-18 iii): asersi yang bergantung pada isi Changelog atau Event Log lengkap (hanya memuat entri seed) memakai isolasi fixture per scope akun yang dinyatakan di `suite.md` (Kemampuan teknis, 2026-11-05); kemampuan itu disediakan tim FE/BE dan belum dikonfirmasi.

## Test Steps

### Format isi baris Replace (TC-FA-TAG-967)

1. Klik tombol `Changelog` pada Table Tools
2. Verifikasi Action `Replace` pada baris E1 dan E2 berupa teks polos (bukan badge)
3. Verifikasi Name `Excavator 20 Ton - 50` dan Field `TAG` pada baris E1 dan E2
4. Verifikasi baris E1: Old Value `[NFC] NF-00090` dan New Value `[RFID] RF-00420` sebagai teks tanpa badge atau ikon tipe
5. Verifikasi baris E2: Old Value `[QR] QR-00240` dan New Value `—`
6. Verifikasi Modified By `Sari W.` pada baris E1 dan E2

### Download tanpa toast sukses (TC-FA-TAG-969)

7. Klik ikon Download di toolbar modal
8. Klik `Download as CSV`
9. Verifikasi file `Changelog-Paired-TAG` format CSV terunduh
10. Verifikasi tidak ada toast sukses
11. Klik ikon close untuk menutup modal
12. Atur Changelog dalam scope menjadi 25 entri Replace lewat fixture backend hingga tersimpan

### Pagination (TC-FA-TAG-966)

13. Klik tombol `Changelog` pada Table Tools
14. Verifikasi halaman 1 memuat 10 entri
15. Buka selector page size pada pagination
16. Verifikasi opsi page size 10 / 25 / 50 / 100
17. Tutup selector page size dengan memilih `10`
18. Pindah ke halaman 2
19. Verifikasi halaman 2 memuat entri ke-11 sampai ke-20
20. Klik ikon close untuk menutup modal

## Notes

- Urutan TC pada spec: TC-FA-TAG-967, TC-FA-TAG-969, lalu TC-FA-TAG-966, karena TC-FA-TAG-966 memakai Changelog 25 entri Replace sedangkan TC-FA-TAG-967 dan TC-FA-TAG-969 memakai entri E1 sampai E6; keadaan data diganti satu kali (langkah 12).
- Langkah penghubung (S-03): langkah 11 dan 20 (menutup modal), 12 (mengganti keadaan Changelog), 15 sampai 17 (membuka dan menutup selector page size untuk mengamati pilihan), dan 18 (TC-FA-TAG-966 langkah 3).
- Langkah 10 ditulis sesudah `Verifikasi` berkas terunduh (langkah 9) sebagai anchor bahwa respons Download sudah diproses (bagian 8b butir 11).
- A-15: nilai literal Pre-setup (nama aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan hanya mengubah data lewat fixture backend (langkah 12) yang menyiapkan atau memulihkan state.
- Temuan untuk QA:
  - TC-FA-TAG-966 Data Uji "25 entri Replace" tidak menyebut nilai Date, Name, dan pelaku; spec hanya mengasersi jumlah entri per halaman (10 dan entri ke-11 sampai ke-20).
  - TC-FA-TAG-969 mengasersi nama berkas `Changelog-Paired-TAG` tanpa ekstensi; spec memeriksa format CSV dan nama berkas dasar `Changelog-Paired-TAG`. Isi berkas tidak diasersi.
  - Post Condition TC ("tidak ada perubahan data bisnis") tidak punya langkah observasi dan tidak diasersi.
  - Changelog adalah audit trail permanen; asersi isi bergantung pada keadaan Changelog yang dijamin fixture backend (tim FE/BE).
