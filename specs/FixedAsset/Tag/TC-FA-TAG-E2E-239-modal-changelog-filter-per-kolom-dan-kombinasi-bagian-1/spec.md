---
id: TC-FA-TAG-E2E-239-modal-changelog-filter-per-kolom-dan-kombinasi-bagian-1
title: "Modal Changelog Paired TAG: Screening Filter Panel dan Filter per Kolom (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-957
  - TC-FA-TAG-958
  - TC-FA-TAG-959
  - TC-FA-TAG-960
  - TC-FA-TAG-961
  - TC-FA-TAG-962
coverage:
  web: automated
---

# Modal Changelog Paired TAG: Screening Filter Panel dan Filter per Kolom (Bagian 1)

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
- State yang diubah: hanya state Filter modal; Filter dikosongkan lewat `[Clear Field]` dan `[Apply]` sesudah tiap kasus. Tidak ada perubahan data bisnis.
- Nilai literal Pre-setup (nama aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Isolasi audit trail (butir A-18 iii): asersi yang bergantung pada isi Changelog atau Event Log lengkap (hanya memuat entri seed) memakai isolasi fixture per scope akun yang dinyatakan di `suite.md` (Kemampuan teknis, 2026-11-05); kemampuan itu disediakan tim FE/BE dan belum dikonfirmasi.

## Test Steps

### Screening Filter Panel (TC-FA-TAG-957)

1. Klik tombol `Changelog` pada Table Tools
2. Klik ikon Filter di toolbar modal
3. Verifikasi Filter Panel tampil di bawah toolbar modal
4. Verifikasi field Filter Panel: `Date` ("Select date"), `Action` ("All actions"), `Name` (multi-select searchable), `Field` ("All fields"), `Modified By` ("All users")
5. Verifikasi footer panel `[Clear Field]` dan `[Apply]`

### Filter Date (TC-FA-TAG-958)

6. Pilih rentang 25 Okt 2026 sampai 25 Okt 2026 pada field `Date`
7. Klik `[Apply]`
8. Verifikasi hanya baris E5 dan E6 tampil
9. Klik `[Clear Field]`
10. Klik `[Apply]`

### Filter Action (TC-FA-TAG-959)

11. Pilih `Report TAG` pada field `Action`
12. Klik `[Apply]`
13. Verifikasi hanya baris E6 tampil
14. Klik `[Clear Field]`
15. Klik `[Apply]`

### Filter Name (TC-FA-TAG-960)

16. Pilih `Excavator 20 Ton - 42` pada field `Name`
17. Klik `[Apply]`
18. Verifikasi hanya baris E4 tampil
19. Klik `[Clear Field]`
20. Klik `[Apply]`

### Filter Field (TC-FA-TAG-961)

21. Pilih `Report Type` pada field `Field`
22. Klik `[Apply]`
23. Verifikasi hanya baris E6 tampil
24. Klik `[Clear Field]`
25. Klik `[Apply]`

### Filter Modified By (TC-FA-TAG-962)

26. Pilih `Budi S.` pada field `Modified By`
27. Klik `[Apply]`
28. Verifikasi hanya baris E3 dan E4 tampil
29. Klik `[Clear Field]`
30. Klik `[Apply]`
31. Klik ikon close untuk menutup modal

## Notes

- Langkah penghubung (S-03): langkah 9 dan 10, 14 dan 15, 19 dan 20, 24 dan 25, serta 29 dan 30 (`[Clear Field]` lalu `[Apply]` mengembalikan enam entri sebelum kasus berikutnya) dan langkah 31 (menutup modal). Filter Panel dianggap tetap terbuka sesudah `[Apply]` (urutan "`[Clear Field]` lalu `[Apply]`" tanpa membuka ulang panel mengikuti TC-FA-TAG-696).
- Pembagian TC lintas spec: kombinasi multi-filter serta kombinasi Search, Filter, dan Sort (TC-FA-TAG-963 sampai TC-FA-TAG-965) ada di spec 240.
- A-15: nilai literal Pre-setup (nama aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-958 menyebut rentang tanggal "25 Okt 2026 sampai 25 Okt 2026" tanpa menjelaskan cara memilih rentang pada date picker; spec menulis satu langkah pilih rentang.
  - TC-FA-TAG-957 Expected a tidak menyebut apakah ikon Filter berubah (indikator) ketika panel terbuka; tidak diasersi.
  - Post Condition TC ("tidak ada perubahan data bisnis") tidak punya langkah observasi dan tidak diasersi.
  - Changelog adalah audit trail permanen; asersi "hanya baris Ex tampil" bergantung pada Changelog yang hanya memuat E1 sampai E6, yang dijamin fixture backend (tim FE/BE).
