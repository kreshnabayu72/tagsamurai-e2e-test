---
id: TC-FA-TAG-E2E-235-modal-changelog-sort-tiga-tahap-per-kolom-bagian-1
title: "Modal Changelog Paired TAG: Urutan Bawaan dan Sort Tiga Tahap Kolom Date, Action, Name, Field (Bagian 1)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-941
  - TC-FA-TAG-942
  - TC-FA-TAG-943
  - TC-FA-TAG-944
  - TC-FA-TAG-945
coverage:
  web: automated
---

# Modal Changelog Paired TAG: Urutan Bawaan dan Sort Tiga Tahap Kolom Date, Action, Name, Field (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk entri Changelog Paired TAG dengan tanggal dan pelaku persis seperti tabel di bawah; tidak ada endpoint yang dikarang di spec ini. Changelog dalam scope akun Total Control hanya memuat E1 sampai E6 selama spec berjalan; fixture mengembalikan keadaan itu di hook `before` dan `after`, sehingga seluruh entri tampil pada halaman 1 (page size 10).
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
- State yang diubah: hanya state sort modal; tiap kolom dikembalikan ke netral oleh klik ketiga. Tidak ada perubahan data bisnis.

## Test Steps

### Urutan bawaan (TC-FA-TAG-941)

1. Klik tombol `Changelog` pada Table Tools
2. Verifikasi baris E1 dan E2 (26/10/26 10:02) di atas, diikuti E3, E4, E5, dan E6 (25/10/26 08:00) paling bawah

### Sort kolom Date (TC-FA-TAG-942)

3. Klik header Date sekali
4. Verifikasi Klik 1 (Oldest First): urutan E6, E5, E4, E3, lalu E1 dan E2
5. Klik header Date sekali lagi
6. Verifikasi Klik 2 (Newest First): urutan E1 dan E2, E3, E4, E5, E6
7. Klik header Date sekali lagi
8. Verifikasi Klik 3 netral: kembali ke urutan bawaan Date terbaru di atas

### Sort kolom Action (TC-FA-TAG-943)

9. Klik header Action sekali
10. Verifikasi Klik 1 (A-Z): lima baris `Replace` (E1 sampai E5, urutan sama dengan bawaan) lalu `Report TAG` (E6), karena `Replace` mendahului `Report TAG` secara alfabet
11. Klik header Action sekali lagi
12. Verifikasi Klik 2 (Z-A): `Report TAG` (E6) lalu lima baris `Replace`
13. Klik header Action sekali lagi
14. Verifikasi Klik 3 netral: kembali ke urutan bawaan

### Sort kolom Name (TC-FA-TAG-944)

15. Klik header Name sekali
16. Verifikasi Klik 1 (A-Z, tidak peka huruf besar-kecil): `Excavator 20 Ton - 20` (E3, E6), `Excavator 20 Ton - 42` (E4), `Excavator 20 Ton - 50` (E1, E2), `Forklift Manual - 61` (E5)
17. Klik header Name sekali lagi
18. Verifikasi Klik 2 (Z-A): `Forklift Manual - 61`, `Excavator 20 Ton - 50`, `Excavator 20 Ton - 42`, `Excavator 20 Ton - 20`
19. Klik header Name sekali lagi
20. Verifikasi Klik 3 netral: kembali ke urutan bawaan

### Sort kolom Field (TC-FA-TAG-945)

21. Klik header Field sekali
22. Verifikasi Klik 1 (A-Z): `Report Type` (E6) lalu `TAG` (E1 sampai E5)
23. Klik header Field sekali lagi
24. Verifikasi Klik 2 (Z-A): `TAG` (E1 sampai E5) lalu `Report Type` (E6)
25. Klik header Field sekali lagi
26. Verifikasi Klik 3 netral: kembali ke urutan bawaan
27. Klik ikon close untuk menutup modal

## Notes

- Langkah penghubung (S-03): langkah 27 (menutup modal). Klik ketiga tiap kolom (langkah 7, 13, 19, 25) mengembalikan sort ke netral, sehingga tiap blok kolom mulai dari urutan bawaan (S-09).
- Pembagian TC lintas spec: sort kolom Old Value, New Value, dan Modified By (TC-FA-TAG-946 sampai TC-FA-TAG-948) ada di spec 236.
- Temuan untuk QA:
  - Baris dengan nilai kolom sama (misalnya E1 dan E2 pada Date 26/10/26 10:02; E1 sampai E5 pada Action `Replace`) tidak punya urutan pasti menurut TC selain "urutan sama dengan bawaan"; spec mengasersi kelompok nilai, bukan urutan antar baris bernilai sama, kecuali TC menyebut urutannya.
  - TC-FA-TAG-944 Expected a menyebut `Excavator 20 Ton - 20` untuk E3 dan E6 sekaligus; urutan E3 dan E6 dalam kelompok itu tidak ditentukan.
  - Post Condition TC ("tidak ada perubahan data bisnis") tidak punya langkah observasi dan tidak diasersi.
  - Changelog adalah audit trail permanen; asersi urutan bergantung pada Changelog yang hanya memuat E1 sampai E6, yang dijamin fixture backend (tim FE/BE).
