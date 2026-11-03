---
id: TC-FA-TAG-E2E-237-modal-changelog-search-per-kolom-bagian-1
title: "Modal Changelog Paired TAG: Search Tanpa Hasil dan Search per Kolom Action, Name, Field, Old Value, New Value, Modified By (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-940
  - TC-FA-TAG-949
  - TC-FA-TAG-950
  - TC-FA-TAG-951
  - TC-FA-TAG-952
  - TC-FA-TAG-953
  - TC-FA-TAG-954
coverage:
  web: automated
---

# Modal Changelog Paired TAG: Search Tanpa Hasil dan Search per Kolom Action, Name, Field, Old Value, New Value, Modified By (Bagian 1)

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

## Test Steps

### Search tanpa hasil (TC-FA-TAG-940)

1. Klik tombol `Changelog` pada Table Tools
2. Verifikasi enam entri E1 sampai E6 tampil
3. Ketik Search `zzzzqq`, tekan Enter
4. Verifikasi ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`
5. Klik `(←)` pada kotak Search

### Search kolom Action (TC-FA-TAG-949)

6. Ketik Search `Report`, tekan Enter
7. Verifikasi hanya baris E6 tampil
8. Klik `(←)` pada kotak Search

### Search kolom Name (TC-FA-TAG-950)

9. Ketik Search `Forklift`, tekan Enter
10. Verifikasi hanya baris E5 tampil
11. Klik `(←)` pada kotak Search

### Search kolom Field (TC-FA-TAG-951)

12. Ketik Search `Report Type`, tekan Enter
13. Verifikasi hanya baris E6 tampil
14. Klik `(←)` pada kotak Search

### Search kolom Old Value (TC-FA-TAG-952)

15. Ketik Search `NF-00090`, tekan Enter
16. Verifikasi hanya baris E1 tampil
17. Klik `(←)` pada kotak Search

### Search kolom New Value (TC-FA-TAG-953)

18. Ketik Search `RF-00415`, tekan Enter
19. Verifikasi hanya baris E3 tampil
20. Klik `(←)` pada kotak Search

### Search kolom Modified By (TC-FA-TAG-954)

21. Ketik Search `Dedi`, tekan Enter
22. Verifikasi hanya baris E5 tampil
23. Klik `(←)` pada kotak Search
24. Klik ikon close untuk menutup modal

## Notes

- Langkah penghubung (S-03): langkah 5, 8, 11, 14, 17, 20, dan 23 (menutup input Search lewat `(←)` yang mereset tabel, supaya tiap kasus mulai dari enam entri) dan langkah 24 (menutup modal). Langkah 2 adalah `Verifikasi` anchor bahwa data modal sudah termuat sebelum asersi hasil kosong dan asersi "hanya" pada kasus berikutnya (8b butir 2).
- TC-FA-TAG-940 langkah 2 ("Klik ikon Search di toolbar modal") dan tiap langkah "Klik ikon Search" TC-FA-TAG-949 sampai TC-FA-TAG-954 menyatu dengan langkah "Ketik Search ..., tekan Enter" (membuka input bila tertutup, bagian 8b butir 9).
- Pembagian TC lintas spec: TC-FA-TAG-955 dan TC-FA-TAG-956 ada di spec 238.
- Temuan untuk QA:
  - Post Condition TC ("tidak ada perubahan data bisnis") tidak punya langkah observasi dan tidak diasersi.
  - Changelog adalah audit trail permanen; asersi "hanya baris Ex tampil" bergantung pada Changelog yang hanya memuat E1 sampai E6, yang dijamin fixture backend (tim FE/BE).
