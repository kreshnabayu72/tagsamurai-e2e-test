---
id: TC-AC-PF-E2E-154-setup-column-default-archive-custom-archive-modal
title: Setup Column Default Archive, Custom Archive, dan Modal Changelog Custom Reset, Tutup, Guard, dan Batas Pin
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-625
  - TC-AC-PF-626
  - TC-AC-PF-627
  - TC-AC-PF-628
coverage:
  web: automated
---

# Setup Column Default Archive, Custom Archive, dan Modal Changelog Custom Reset, Tutup, Guard, dan Batas Pin

## Prerequisites

- Mode: FE+BE
- Akun: `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, Total Control, Principal), password dari env `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Halaman awal: Plans & Licensing > Plans & Features > Default > Active.
- Data Pre-setup: Dataset Plan A (Pre-setup #21; Default Archive `Growth Plus (old)`, custom archived `Enterprise Reseller`), Dataset Plan R (Pre-setup #30; Default Archive `Plan Arsip Lama`, `Plan Arsip Tengah`, `Plan Arsip Baru`), dan Dataset Log C (Pre-setup #41; Changelog Custom Principal 6 entri).
- General Settings (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- Tabel "Surface yang diuji" (langkah berulang untuk tiap baris):

| Kode | Surface | Cara membuka | Kolom disembunyikan atau tersisa | Kolom di-drag ke awal | Pin 1 sampai 3 | Pin ke-4 | Daftar kolom default |
|---|---|---|---|---|---|---|---|
| DR | Default > Archive | klik tab Default, lalu sub-tab Archive | `Clients` | `Last Modified` | `Plan Name`, `Product`, `Pricing Type` | `Version` | `Plan Name | Product | Pricing Type | Version | Clients | Last Modified` |
| CR | Custom > Archive | klik tab Custom, lalu sub-tab Archive | `Clients` | `Last Modified` | `Plan Name`, `Product`, `Pricing Type` | `Version` | `Plan Name | Product | Pricing Type | Version | Clients | Last Modified` (kolom Created By tetap tersembunyi) |
| MC | Modal Changelog Custom | klik tab Custom, lalu klik ikon Changelog | `Old Value` | `Modified By` | `Date`, `Action`, `Plan Name` | `Field` | `Date | Action | Plan Name | Field | Old Value | New Value | Modified By` |

- Kemampuan teknis: fixture BE idempoten untuk memulihkan Dataset Pre-setup ke keadaan awal (disediakan tim FE/BE, dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` spec ini. Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12).
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup tanpa suffix; suite serial. Spec ini tidak mengubah data Pre-setup.
- State sementara: konfigurasi kolom yang disimpan spec (cache browser per tabel) dihapus di hook `after` (kemampuan menghapus preferensi kolom di browser disediakan tim FE, bagian 4).
- Flag Guided Tooltip: sesuai pernyataan di `suite.md` (hook suite `before` dan `after`).

## Test Steps

### TC-AC-PF-625 Reset to Default

Untuk setiap baris tabel "Surface yang diuji" (langkah 1 sampai 7):

1. Buka surface sesuai kolom "Cara membuka".
2. Buka Popup Setup Column, uncheck kolom pada "Kolom disembunyikan atau tersisa", drag kolom pada "Kolom di-drag ke awal" ke posisi awal, klik `[Save]`.
3. Buka Popup Setup Column lagi, klik `[Reset to Default]`, klik `[Save]`.
4. Verifikasi kolom tabel surface pulih sesuai kolom "Daftar kolom default".
5. Tekan F5.
6. Buka kembali surface sesuai kolom "Cara membuka".
7. Verifikasi kolom tabel surface sesuai kolom "Daftar kolom default" bertahan setelah F5.

### TC-AC-PF-626 Tutup popup lewat (X) atau Esc

Untuk baris DR dan CR pada tabel "Surface yang diuji" (langkah 8 sampai 14):

8. Buka surface sesuai kolom "Cara membuka".
9. Buka Popup Setup Column, uncheck kolom pada "Kolom disembunyikan atau tersisa", klik icon close `(X)`.
10. Verifikasi Popup Setup Column tertutup.
11. Verifikasi kolom pada "Kolom disembunyikan atau tersisa" tetap tampil.
12. Buka Popup Setup Column lagi, uncheck kolom yang sama, tekan Esc.
13. Verifikasi Popup Setup Column tertutup.
14. Verifikasi kolom pada "Kolom disembunyikan atau tersisa" tetap tampil.

Untuk baris MC:

15. Buka modal Changelog Custom (klik tab Custom, lalu klik ikon Changelog).
16. Buka Popup Setup Column, uncheck `Old Value`, klik icon close `(X)`.
17. Verifikasi Popup Setup Column tertutup.
18. Verifikasi modal Changelog Custom di bawahnya tetap terbuka.
19. Verifikasi kolom `Old Value` tetap tampil.
20. Buka Popup Setup Column lagi, uncheck `Old Value`, tekan Esc.
21. Verifikasi Popup Setup Column tertutup.
22. Verifikasi modal Changelog Custom di bawahnya tetap terbuka.
23. Verifikasi kolom `Old Value` tetap tampil.

### TC-AC-PF-627 Guard satu kolom tersisa

Untuk setiap baris tabel "Surface yang diuji" (langkah 24 sampai 30):

24. Buka surface sesuai kolom "Cara membuka".
25. Buka Popup Setup Column dan uncheck semua kolom kecuali kolom pada "Kolom disembunyikan atau tersisa".
26. Hover checkbox kolom pada "Kolom disembunyikan atau tersisa".
27. Coba uncheck kolom pada "Kolom disembunyikan atau tersisa".
28. Verifikasi checkbox kolom tersebut Disabled.
29. Verifikasi tooltip "At least one column must remain visible.".
30. Klik icon close `(X)` untuk menutup popup tanpa Save.

### TC-AC-PF-628 Batas pin tiga kolom

Untuk setiap baris tabel "Surface yang diuji" (langkah 31 sampai 38):

31. Buka surface sesuai kolom "Cara membuka".
32. Buka Popup Setup Column dan Pin kolom pada "Pin 1 sampai 3".
33. Hover icon Pin kolom pada "Pin ke-4".
34. Klik icon Pin kolom pada "Pin ke-4".
35. Verifikasi icon Pin kolom pada "Pin ke-4" Disabled.
36. Verifikasi tooltip "Maximum 3 columns can be pinned at once. Unpin another column first.".
37. Verifikasi klik tidak membekukan kolom pada "Pin ke-4".
38. Klik icon close `(X)` untuk menutup popup tanpa Save.

## Notes

- Langkah berulang: "Untuk setiap baris tabel" mengulang langkah 1 sampai 7, 24 sampai 30, dan 31 sampai 38 untuk baris DR, CR, dan MC; langkah 8 sampai 14 untuk baris DR dan CR. Parameter tiap iterasi ada di tabel "Surface yang diuji", tanpa langkah bersyarat, dan tiap `Verifikasi` tetap satu per klausa. Langkah 15 sampai 23 (baris MC) ditulis terpisah karena TC-AC-PF-626 butir c memuat asersi modal di bawah popup yang hanya berlaku untuk MC.
- Langkah penghubung (S-03), ditulis tanpa `Verifikasi`: langkah 1, 6, 8, 15, 24, dan 31 membuka (kembali) surface karena F5 menutup modal Changelog dan dapat mengembalikan halaman ke tab awal; langkah 30 dan 38 menutup popup tanpa Save.
- Alasan di atas sekitar 35 langkah: TC sumber masing-masing mencakup tiga surface (Default Archive, Custom Archive, modal Changelog Custom) dalam satu TC dengan langkah identik dan parameter berbeda; hasil ekspansi iterasi sekitar 100 langkah, dan semua blok adalah jenis aksi yang sama (Setup Column) dengan dataset yang sama. Estimasi langkah semula lebih rendah karena tiap TC menghitung satu surface.
- Temuan untuk QA: (1) TC-AC-PF-627 menyebut "hover dan coba uncheck" tanpa Expected untuk hasil percobaan uncheck selain Disabled dan tooltip; spec hanya mengasersi dua hal itu. (2) TC-AC-PF-625 tidak menyatakan apakah F5 mempertahankan tab dan sub-tab aktif dan membuka kembali modal Changelog; spec menambah langkah membuka kembali surface. (3) TC-AC-PF-628 tidak menyebut kolom ke-4 pada Custom Archive selain `Version` (disamakan dengan Default Archive).
