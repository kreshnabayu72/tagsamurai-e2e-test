---
id: TC-AC-DN-E2E-125-changelog-screening-tooltip-dan-tutup
title: "Modal Changelog: Screening, Tooltip, Tutup X/Esc, dan Backdrop"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-388
  - TC-AC-DN-389
  - TC-AC-DN-390
  - TC-AC-DN-391
  - TC-AC-DN-392
coverage:
  web: automated
---

# Modal Changelog: Screening, Tooltip, Tutup X/Esc, dan Backdrop

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`, entitas Principal, rujukan `Fixture.settings-device-name.akunTotalControl`; fixture belum ada, disediakan tim FE), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Data Pre-setup (dibaca saja, tidak diubah): #16 Device Name inti; #19 Riwayat Changelog Uji (11 entri, tabel di bawah, pelaku `Budi S` = Budi Santoso dan `Maya P` = Maya Putri, nama lengkap pelaku seed #2 `Maya Putri`); #20 General Settings entitas uji (Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta).

  | No | Date | Action | Device Name | Field | Old Value | New Value | Modified By |
  |---|---|---|---|---|---|---|---|
  | 1 | 01/09/26 08:30 | Create | Cable Tester | Device Name | — | Cable Tester | Budi S |
  | 2 | 02/09/26 09:10 | Create | NFC Tag | Device Name | — | NFC Tag | Budi S |
  | 3 | 03/09/26 10:00 | Create | Retired Gateway | Device Name | — | Retired Gateway | Maya P |
  | 4 | 05/09/26 13:15 | Edit | Gate Antenna | Device Name | Gate Antena | Gate Antenna | Maya P |
  | 5 | 06/09/26 09:30 | Edit | Cable Tester | Category | TAG > NFC > Tag | TAG > NFC > Accessory | Budi S |
  | 6 | 07/09/26 14:05 | Edit | NFC Tag | Category | TAG > NFC > Accessory | TAG > NFC > Tag | Maya P |
  | 7 | 08/09/26 15:40 | Edit | NFC Tag | Measurement | Box | Unit | Maya P |
  | 8 | 09/09/26 08:00 | Edit | Cable Tester | Measurement | Unit | Meter | Budi S |
  | 9 | 10/09/26 12:25 | Edit | Cable Tester | Measurement | Meter | Unit | Budi S |
  | 10 | 12/09/26 17:45 | Delete | Retired Gateway | Device Name | Retired Gateway | — | Budi S |
  | 11 | 15/09/26 10:10 | Create | Tag Reel | Device Name | — | Tag Reel | Maya P |

- Isolasi riwayat seed (S-12, S-14): Changelog adalah audit trail permanen yang tumbuh karena spec lain menulis entri bertanggal waktu nyata (lebih baru dari 15/09/26). Asersi isi, jumlah, dan urutan atas riwayat seed dibatasi dengan Filter Date `01/09/26` sampai `15/09/26` sehingga hanya 11 entri seed yang terlihat; jumlah total seluruh entri tidak diasersi.
- Kemampuan teknis (disediakan tim FE/BE): mengetik, mengklik, menyeret, menekan Esc, hover, dan memilih tanggal pada Overlay Date Picker.
- State global: tidak ada yang diubah.
- Spec tidak mengubah record Pre-setup; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-389: Tooltip ikon Changelog, toolbar popup, dan header Column Visibility

1. Arahkan kursor ke ikon Changelog di toolbar List
2. Verifikasi tooltip ikon Changelog di toolbar List `Changelog`
3. Klik ikon Changelog di toolbar List
4. Arahkan kursor ke ikon Search di toolbar popup
5. Verifikasi tooltip ikon Search `Search`
6. Arahkan kursor ke ikon Filter di toolbar popup
7. Verifikasi tooltip ikon Filter `Filter`
8. Arahkan kursor ke ikon Download di toolbar popup
9. Verifikasi tooltip ikon Download `Download`
10. Arahkan kursor ke ikon `⋯` pada header kolom terakhir
11. Verifikasi tooltip header kolom `⋯` `Column Visibility`

### TC-AC-DN-388: Screening popup Changelog: Device Name

12. Verifikasi path header `Settings > Device > Device Name > Popup Changelog: Device Name` tanpa breadcrumb
13. Verifikasi title popup `Changelog: Device Name`
14. Verifikasi tombol close `(X)` tampil di kanan atas
15. Verifikasi Table Tools popup `Search | Filter | Download`
16. Verifikasi kolom tabel `Date (sortable) | Action (sortable) | Device Name (sortable) | Field (sortable) | Old Value (sortable) | New Value (sortable) | Modified By (sortable) | Column Visibility (⋯) (unsortable, header klik membuka overlay Column Visibility, body per baris kosong)`
17. Klik ikon Filter di toolbar popup
18. Klik field `Date`, pilih 01/09/26 sebagai tanggal awal dan 15/09/26 sebagai tanggal akhir
19. Klik `[Apply]`
20. Klik ikon Filter untuk menutup Filter Panel
21. Verifikasi baris data terurut Date terbaru di atas dan baris pertama berasal dari `15/09/26 10:10`
22. Verifikasi footer Pagination default 10 data per halaman

### TC-AC-DN-392: Klik backdrop tidak menutup popup

23. Klik area gelap di luar popup (backdrop)
24. Verifikasi popup `Changelog: Device Name` tetap terbuka
25. Verifikasi tabel tetap tampil

### TC-AC-DN-390: Menutup popup lewat ikon close (X)

26. Klik ikon close `(X)` di kanan atas popup
27. Verifikasi popup `Changelog: Device Name` tertutup
28. Verifikasi halaman `Settings > Device > Device Name` tampil kembali dengan List Device Name

### TC-AC-DN-391: Menutup popup lewat tombol Esc

29. Klik ikon Changelog di toolbar List
30. Tekan tombol `Esc`
31. Verifikasi popup `Changelog: Device Name` tertutup
32. Verifikasi halaman `Settings > Device > Device Name` tampil kembali dengan List Device Name

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Filter Date `01/09/26` sampai `15/09/26` membatasi tampilan pada 11 entri seed karena audit trail tumbuh; TC sumber mengasumsikan hanya 11 entri. Angka total seluruh entri tidak diasersi (S-12).
- Urutan (S-10): TC-AC-DN-389 lebih dulu karena tooltip ikon Changelog List hanya dapat diamati saat popup tertutup; TC-AC-DN-388 memakai popup yang sama; TC-AC-DN-392 (tidak menutup) mendahului TC-AC-DN-390 dan TC-AC-DN-391 (menutup).
- Temuan untuk QA:
  - TC-AC-DN-388 Expected b.ii menyebut baris pertama berasal dari 15/09/26 10:10; angka itu hanya benar untuk riwayat seed, sehingga diasersi setelah pembatas Filter Date.
  - Post Condition TC tanpa langkah observasi tidak diasersi (S-01).
