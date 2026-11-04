---
id: TC-FA-TDC-E2E-176-popup-changelog-filter-panel-opsi-multi-select-or-date-dan-and
title: "Popup Changelog Filter Panel: Screening, Opsi, Multi-Select, OR, Date, dan AND"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-629
  - TC-FA-TDC-630
  - TC-FA-TDC-631
  - TC-FA-TDC-632
  - TC-FA-TDC-633
  - TC-FA-TDC-634
coverage:
  web: automated
---

# Popup Changelog Filter Panel: Screening, Opsi, Multi-Select, OR, Date, dan AND

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; disediakan tim FE): `Fixture.fixedAssetTaxDepreciationClass.exampleData` berisi sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL); `Fixture.fixedAssetTaxDepreciationClass.exampleDataChangelog` berisi 16 entri Popup Changelog sesuai Example Data Modal Changelog PRD (6 `Create`, 1 `Delete`, 9 `Edit`; dua entri Edit NB-4 bertanggal 03/03/26). Modified By memuat `Budi` (3 baris) dan `Rina P`. Format tanggal General Settings `dd/MM/yy HH:mm`. Data Dinamis: tidak ada.
- Tabel parameter perulangan TC-FA-TDC-631 (langkah 17 sampai 21), literal TC:

  | Field | Opsi | Hasil |
  |---|---|---|
  | Action | `Delete` | 1 baris |
  | Class Code | `NB-3` dan `NB-OLD` | 2 baris (Delete NB-3 dan Edit Status NB-OLD) |
  | Field | `Status` | 2 baris |
  | Modified By | `Budi` | 3 baris |

- Kemampuan teknis: riwayat Changelog diatur ke 16 entri Example Data lewat Fixture BE (disediakan tim FE/BE; mekanismenya tidak disebut TC, PRD, atau LLD); Filter Panel Popup dianggap tetap terbuka sesudah `[Apply]`, sama dengan tabel utama (8b.9; lihat Temuan untuk QA).
- State global yang diubah: Filter Popup Changelog; dilepas lewat `[Clear Field]` dan `[Apply]` di akhir tiap blok TC (langkah 20 dan 21, 26 dan 27, 32 dan 33, serta 38 dan 39), dan Popup ditutup di langkah 40.

## Test Steps

1. Klik icon Changelog

### TC-FA-TDC-629: Screening Filter Panel Popup Changelog

2. Klik icon Filter pada toolbar Popup
3. Verifikasi field `Date` berupa date range dengan placeholder `Select date`
4. Verifikasi field `Action` berupa multi-select searchable dengan placeholder `All actions`
5. Verifikasi field `Class Code` berupa multi-select searchable dengan placeholder `All tax depreciation classes`
6. Verifikasi field `Field` berupa multi-select searchable dengan placeholder `All fields`
7. Verifikasi field `Modified By` berupa multi-select searchable dengan placeholder `All users`
8. Verifikasi tombol `[Clear Field]` dan `[Apply]` tampil
9. Verifikasi tidak ada field filter untuk Old Value dan New Value

### TC-FA-TDC-630: Opsi filter di-populate dari isi tabel log

10. Buka dropdown Action
11. Verifikasi opsi Action: `Create`, `Delete`, `Edit`
12. Tutup dropdown Action
13. Buka dropdown Field
14. Verifikasi opsi Field (11 opsi): `Allowed Methods`, `Asset Type`, `Class Code`, `Class Name`, `Current Version`, `Effective From`, `Last Posted Tax Year`, `Regulation Reference`, `Scheduled Version`, `Status`, `Useful Life`
15. Tutup dropdown Field
16. Klik `[Apply]` tanpa pilihan

### TC-FA-TDC-631: Filter multi-select Action, Class Code, Field, dan Modified By

Untuk setiap baris tabel parameter TC-FA-TDC-631 pada Prerequisites, lakukan langkah 17 sampai 21.

17. Pilih opsi pada kolom Opsi untuk field pada kolom Field
18. Klik `[Apply]`
19. Verifikasi Popup menampilkan hasil pada kolom Hasil
20. Klik `[Clear Field]`
21. Klik `[Apply]`

### TC-FA-TDC-632: Filter Action dua opsi digabung dengan logika OR

22. Pilih Action `Create` dan `Delete`
23. Klik `[Apply]`
24. Verifikasi Popup menampilkan 7 baris
25. Verifikasi 7 baris terdiri atas 6 baris `Create` dan 1 baris `Delete`
26. Klik `[Clear Field]`
27. Klik `[Apply]`

### TC-FA-TDC-633: Filter Date satu hari

28. Pilih rentang Date 03/03/26 sampai 03/03/26
29. Klik `[Apply]`
30. Verifikasi Popup menampilkan 2 baris Edit NB-4 (Useful Life dan Effective From)
31. Verifikasi kedua baris bertanggal 03/03/26
32. Klik `[Clear Field]`
33. Klik `[Apply]`

### TC-FA-TDC-634: Kombinasi Filter AND

34. Pilih Action `Edit`
35. Pilih Modified By `Rina P`
36. Klik `[Apply]`
37. Verifikasi Popup menampilkan 3 baris: Edit BLD-NP Status, Edit NB-OLD Status, dan Edit NB-SL Class Name
38. Klik `[Clear Field]`
39. Klik `[Apply]`
40. Tutup Popup Changelog lewat ikon Close `(X)`

## Notes

- Langkah berulang (8b.7): langkah 17 sampai 21 diulang empat kali (satu iterasi per baris tabel parameter TC-FA-TDC-631); parameter tiap iterasi hanya Field, Opsi, dan Hasil, tanpa langkah bersyarat, dan `Verifikasi` tetap satu per klausa (S-01). Dengan ekspansi spec ini 55 langkah (40 langkah nominal dan 3 x 5 langkah ulangan).
- Alasan lebih dari sekitar 35 langkah (dengan ekspansi): satu topik (Filter Panel Popup Changelog), satu kelas harness, dan data Pre-setup yang sama (16 entri Example Data); keenam TC hanya membuka Filter Panel dan menyaring tanpa mengubah data, sehingga satu pembukaan Popup dipakai bersama (prinsip 13, halaman yang sama dipakai berulang). Tiap blok TC diakhiri `[Clear Field]` dan `[Apply]` sehingga blok berikutnya tidak bergantung pada hasil blok sebelumnya.
- Langkah 1 TC-FA-TDC-630 sampai TC-FA-TDC-634 ("Klik icon Changelog") tidak diulang karena Popup Changelog tetap terbuka sejak langkah 1.
- Filter Panel dibuka sekali di langkah 2 dan diasumsikan tetap terbuka sesudah `[Apply]`, sama dengan tabel utama (8b.9); langkah berikutnya memilih atau melepas Filter tanpa membuka panel lagi.
- Langkah penghubung (S-03): langkah 12 dan 15 (menutup dropdown), langkah 20 dan 21, 26 dan 27, 32 dan 33, serta 38 dan 39 (melepas Filter lewat `[Clear Field]` dan `[Apply]`), langkah 40 (menutup Popup).
- Temuan untuk QA:
  - Email akun Total Control tidak tertulis di TC.
  - Isi Popup Changelog memakai jumlah entri absolut (7, 2, dan 3 baris hasil Filter) pada audit trail permanen; Lampiran A konvensi tidak memuat pengecualian untuk modul ini. Spec mengikuti TC dan membutuhkan kemampuan Fixture BE yang menimpa riwayat Changelog dengan 16 entri Example Data (tidak disebut TC, PRD, atau LLD).
  - TC-FA-TDC-629 sampai 634 tidak menyebut apakah Filter Panel Popup tetap terbuka atau menutup sesudah `[Apply]`; spec menganggapnya tetap terbuka, sama dengan tabel utama (8b.9), sehingga tidak ada klik icon Filter sesudah `[Apply]`. Menunggu konfirmasi FE.
  - TC-FA-TDC-630 tidak menyebut cara menutup dropdown dan mengakhiri pengecekan opsi tanpa memilih; spec menutup dropdown dan memakai `[Apply]` tanpa pilihan.
  - TC-FA-TDC-631 langkah 5 tidak melepas Filter Modified By `Budi` di akhir TC; spec melepasnya (S-09).
  - TC-FA-TDC-633 tidak menyebut cara memilih rentang tanggal pada date range picker.
