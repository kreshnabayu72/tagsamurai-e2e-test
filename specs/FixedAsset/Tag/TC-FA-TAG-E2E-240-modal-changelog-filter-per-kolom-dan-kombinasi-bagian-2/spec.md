---
id: TC-FA-TAG-E2E-240-modal-changelog-filter-per-kolom-dan-kombinasi-bagian-2
title: "Modal Changelog Paired TAG: Kombinasi Multi-filter, Kombinasi Search, Filter, Sort, dan Pemulihan Baris (Bagian 2)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-963
  - TC-FA-TAG-964
  - TC-FA-TAG-965
coverage:
  web: automated
---

# Modal Changelog Paired TAG: Kombinasi Multi-filter, Kombinasi Search, Filter, Sort, dan Pemulihan Baris (Bagian 2)

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
- State yang diubah: hanya state Search, Filter, dan Sort modal; semuanya dikosongkan oleh langkah 7 sampai 9, 17 sampai 20, dan 22. Tidak ada perubahan data bisnis.
- Isolasi audit trail (butir A-18 iii): asersi yang bergantung pada isi Changelog atau Event Log lengkap (hanya memuat entri seed) memakai isolasi fixture per scope akun yang dinyatakan di `suite.md` (Kemampuan teknis, 2026-11-05); kemampuan itu disediakan tim FE/BE dan belum dikonfirmasi.
- Nilai literal Pre-setup (nama aset, kode Tag, Modified By) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.

## Test Steps

### Kombinasi multi-filter bersifat AND (TC-FA-TAG-963)

1. Klik tombol `Changelog` pada Table Tools
2. Klik ikon Filter
3. Pilih `Replace` pada field `Action`
4. Pilih `Budi S.` pada field `Modified By`
5. Klik `[Apply]`
6. Verifikasi hanya baris E3 dan E4 tampil
7. Klik `[Clear Field]`
8. Klik `[Apply]`
9. Klik ikon Filter untuk menutup panel

### Kombinasi Search, Filter, dan Sort (TC-FA-TAG-964)

10. Ketik Search `Excavator`, tekan Enter
11. Klik ikon Filter
12. Pilih `Replace` pada field `Action`
13. Klik `[Apply]`
14. Klik header Name sekali
15. Verifikasi hanya baris Replace Excavator 20 Ton (E1 sampai E4) tampil
16. Verifikasi urutan Name menaik: `Excavator 20 Ton - 20` (E3), `Excavator 20 Ton - 42` (E4), `Excavator 20 Ton - 50` (E1, E2)
17. Klik `[Clear Field]`
18. Klik `[Apply]`
19. Klik header Name dua kali lagi hingga sort netral
20. Klik `(←)` pada kotak Search

### Mengosongkan Search memulihkan baris (TC-FA-TAG-965)

21. Ketik Search `zzzzqq`, tekan Enter
22. Kosongkan isi kotak search, tekan Enter
23. Verifikasi enam entri tampil kembali
24. Klik ikon close untuk menutup modal

## Notes

- Langkah penghubung (S-03): langkah 7 sampai 9 (mengosongkan Filter dan menutup panel), 17 sampai 20 (mengosongkan Filter, mengembalikan sort ke netral, dan menutup input Search lewat `(←)` supaya TC-FA-TAG-965 mulai dari enam entri), dan 24 (menutup modal). Filter Panel dianggap tetap terbuka sesudah `[Apply]` (urutan "`[Clear Field]` lalu `[Apply]`" tanpa membuka ulang panel mengikuti TC-FA-TAG-696).
- Pembagian TC lintas spec: screening Filter Panel dan Filter per kolom (TC-FA-TAG-957 sampai TC-FA-TAG-962) ada di spec 239.
- Temuan untuk QA:
  - TC-FA-TAG-964 Expected tidak membedakan urutan E1 dan E2 (Name sama); spec tidak mengasersi urutan di antaranya.
  - Post Condition TC ("tidak ada perubahan data bisnis") tidak punya langkah observasi dan tidak diasersi.
  - Changelog adalah audit trail permanen; asersi "hanya baris Ex tampil" bergantung pada Changelog yang hanya memuat E1 sampai E6, yang dijamin fixture backend (tim FE/BE).
