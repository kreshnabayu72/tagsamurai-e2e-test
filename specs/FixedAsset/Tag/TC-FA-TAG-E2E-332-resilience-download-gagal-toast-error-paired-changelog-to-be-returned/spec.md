---
id: TC-FA-TAG-E2E-332-resilience-download-gagal-toast-error-paired-changelog-to-be-returned
title: "Resilience: Download Gagal Menampilkan Toast Error pada Paired, Changelog, To Be Returned, dan Event Log"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-230
  - TC-FA-TAG-970
  - TC-FA-TAG-1026
  - TC-FA-TAG-1069
coverage:
  web: automated
---

# Resilience: Download Gagal Menampilkan Toast Error pada Paired, Changelog, To Be Returned, dan Event Log

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata).
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) `Spectra.intercept` parsial yang memaksa respons 5xx pada request pengunduhan tiap surface (Paired-TAGs, Changelog-Paired-TAG, To-Be-Returned-TAGs, Event-Log-To-Be-Returned) dan melepas intercept; hook `after` melepas semua intercept; (2) pembaca berkas unduhan browser untuk memastikan tidak ada berkas terunduh; (3) seed dan pemulihan idempotent lewat fixture backend untuk dataset Paired, entri Changelog Paired TAG, Tag To Be Returned, dan entri Event Log. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Grup tab Paired | 'Excavator 20 Ton' / Plant A / RFID / Total 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; 'Excavator 20 Ton' / Plant B / RFID / 20 / 2 / 5 / 0; 'Laptop Pro 14' / HQ / NFC, QR / 25 / 1 / 0 / 2; 'Forklift Manual' / Plant A / Non TAG / 10 / 0 / 3 / 0 | `grupPaired` |
| Changelog Paired TAG | E1 26/10/26 10:02 Replace / 'Excavator 20 Ton - 50' / TAG / [NFC] NF-00090 / [RFID] RF-00420 / Sari W.; E2 26/10/26 10:02 Replace / 'Excavator 20 Ton - 50' / TAG / [QR] QR-00240 / — / Sari W.; E3 26/10/26 09:20 Replace / 'Excavator 20 Ton - 20' / TAG / [RFID] RF-00130 / [RFID] RF-00415 / Budi S.; E4 26/10/26 09:14 Replace / 'Excavator 20 Ton - 42' / TAG / [QR] QR-00230 / [RFID] RF-00412 / Budi S.; E5 25/10/26 16:40 Replace / 'Forklift Manual - 61' / TAG / [QR] QR-00251 / — / Dedi K.; E6 25/10/26 08:00 Report TAG / 'Excavator 20 Ton - 20' / Report Type / — / Damaged / Rina T. | `changelogPaired` |
| Tag To Be Returned | [RFID] RF-00071 (Last Asset 'Excavator 20 Ton - 2', Reason Disposal, Return Group Disposal Center, Current Holder Dedi K., Since 01 Sep 2026); [RFID] RF-00088 ('Excavator 20 Ton - 5', Disposal Center, Dedi K., Since 20 Sep 2026); [NFC] NF-00092 ('Laptop Pro 14 - 8', HQ Warehouse, Rina T., Since 22 Sep 2026); [RFID] RF-00110 (Last Asset 'Excavator 20 Ton - 10', Reason Disposal, Return Group Disposal Center, Current Holder Dedi K., Since 10 Sep 2026) | `tbr` |
| Event Log | 27 Okt 2026 14:15 [RFID] RF-00093, 'Excavator 20 Ton - 5', Disposal Center, Dedi K., Budi S., Assigned, Paired; 26 Okt 2026 10:02 [RFID] RF-00071, Last Asset 'Excavator 20 Ton - 2', Return Group Disposal Center, Handed Over By Dedi K., Received By Budi S., Method Scan, Final Status Available; 26 Okt 2026 09:40 [NFC] NF-00092, 'Laptop Pro 14 - 8', HQ Warehouse, Rina T., Sari W., Manual, Damaged/Missing | `eventLog` |

- State yang diubah dan pemulihannya: intercept 5xx dipasang di langkah 1, 8, 16, dan 23 dan dilepas di langkah 6, 13, dan 21; intercept terakhir (langkah 23) dilepas hook `after`, yang juga melepas semua intercept walau spec gagal di tengah.

## Test Steps

1. Pasang intercept 5xx pada pengunduhan Paired-TAGs
2. Klik ikon Download
3. Klik `Download as CSV`
4. Verifikasi muncul toast error: "Error, failed to download Paired-TAGs."
5. Verifikasi tidak ada berkas terunduh
6. Lepas intercept
7. Klik tombol `Changelog` pada Table Tools
8. Pasang intercept 5xx pada pengunduhan Changelog-Paired-TAG
9. Tunggu toast lama hilang otomatis
10. Klik ikon Download
11. Klik `Download as CSV`
12. Verifikasi muncul toast error: "Error, failed to download Changelog-Paired-TAG."
13. Lepas intercept
14. Tutup Modal Changelog
15. Klik tab `To Be Returned`
16. Pasang intercept 5xx pada pengunduhan To-Be-Returned-TAGs
17. Tunggu toast lama hilang otomatis
18. Klik ikon Download
19. Klik "Download as CSV"
20. Verifikasi toast "Error, failed to download To-Be-Returned-TAGs." tampil
21. Lepas intercept
22. Klik tombol "Event Log"
23. Pasang intercept 5xx pada pengunduhan Event-Log-To-Be-Returned
24. Tunggu toast lama hilang otomatis
25. Klik ikon Download
26. Klik "Download as CSV"
27. Verifikasi toast "Error, failed to download Event-Log-To-Be-Returned." tampil

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-230, 970, 1026, 1069). Tidak ada TC hanya-BE.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 6, 13, 21 (melepas intercept), 9, 17, 24 (menunggu toast sebelumnya hilang agar toast berikutnya adalah toast baru, R-12), 14 (menutup Modal Changelog).
- Langkah 5 memakai pembaca berkas unduhan untuk Expected "Tidak ada file terunduh" sesudah `Verifikasi` toast sebagai anchor positif; TC-FA-TAG-970, 1026, dan 1069 tidak menulis Expected itu sehingga tidak diasersi.
- Temuan untuk QA:
  - TC-FA-TAG-970, 1026, dan 1069 tidak menyebut format unduhan lain; spec memakai `Download as CSV` sesuai langkah TC.
  - TC-FA-TAG-1026 dan TC-FA-TAG-1069 menulis langkah memasang kegagalan sebagai "Gagalkan request download dengan respons 5xx" tanpa mekanisme; spec memakai intercept 5xx.
  - Nama dan kode literal Pre-setup (Asset Name, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
