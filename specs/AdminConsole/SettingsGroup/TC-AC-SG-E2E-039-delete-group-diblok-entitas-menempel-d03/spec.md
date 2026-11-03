---
id: TC-AC-SG-E2E-039-delete-group-diblok-entitas-menempel-d03
title: "Delete Group Diblok karena Entitas Menempel (D-03): Langsung, Descendant, Archived, Partner, dan Distributor Principal"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SG-136
  - TC-AC-SG-137
  - TC-AC-SG-138
  - TC-AC-SG-139
  - TC-AC-SG-398
coverage:
  web: automated
---

# Delete Group Diblok karena Entitas Menempel (D-03): Langsung, Descendant, Archived, Partner, dan Distributor Principal

## Prerequisites

- Mode: FE+BE.
- Akun aktor (login pertama di hook `before`) dan akun ganti akun:

| Blok TC | Akun | Email | Env var password |
|---|---|---|---|
| TC-136 sampai TC-139 | Total Control Distributor Hapus Utama (Pre-setup #21) | `totalControlDistHapus_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_SG_HAPUS_PASSWORD` |
| TC-398 | Total Control Principal (Pre-setup #1; tree `Pohon Uji Utama`, Pre-setup #16 dan #19) | `totalControlGroup_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login di hook `before` spec ini sebagai Total Control Distributor Hapus Utama; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default spec (Distributor Hapus Utama).
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-group` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup #21 (entitas `Distributor Hapus Utama`, dibaca saja):
  - `Hapus Member A`: `Client Mawar` (Active) menempel langsung.
  - `Hapus Member B` > `Hapus Member B1` > `Hapus Member B2` > `Hapus Member B3`: `Partner Nusantara` (Active) menempel di `Hapus Member B3`.
  - `Hapus Arsip`: `Client Lama` (Archived) menempel; Total Member 0.
  - `Hapus Partner`: `Partner Suspensi` (Suspended) menempel langsung.
- Data Pre-setup #16 dan #19 (entitas Principal, dibaca saja): node `Region B` dengan `Distributor Kencana` (Active) yang di-assign langsung.
- Seluruh aksi Delete di spec ini ditolak guard (dialog blok); tidak ada node yang dihapus atau diubah, sehingga Pre-setup dipakai langsung sebagai target yang hanya dibaca dan Last Updated tidak berubah (S-06). Hook `before` dan `after` memastikan baseline Pre-setup #21 lewat Fixture BE.
- Kemampuan teknis: Fixture BE (pemulihan baseline entitas uji), disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SG-136: Delete diblok bila ada entitas yang menempel langsung pada node (D-03)

1. Ketik Search `Hapus Member A`, tekan Enter
2. Klik ikon `⋯` pada baris `Hapus Member A`, lalu pilih "Delete"
3. Verifikasi dialog blok tampil: title "Cannot Delete Group", body bullet `Hapus Member A` dan "This group or its subgroups still have members. Remove all members before deleting." dengan satu tombol `[OK]` (tidak ada tombol lanjut)
4. Klik `[OK]`
5. Verifikasi `Hapus Member A` tetap ada di tabel

### TC-AC-SG-137: Delete diblok bila entitas menempel pada descendant tiga level di bawah node

6. Ganti isi kotak search dengan `Hapus Member B`, tekan Enter
7. Klik ikon `⋯` pada baris `Hapus Member B`, lalu pilih "Delete"
8. Verifikasi dialog blok "Cannot Delete Group" tampil dengan body "This group or its subgroups still have members. Remove all members before deleting." walau `Partner Nusantara` hanya menempel di `Hapus Member B3` (tiga level di bawah)
9. Klik `[OK]`
10. Verifikasi dialog blok tertutup
11. Verifikasi `Hapus Member B` tetap ada di tabel

### TC-AC-SG-138: Delete diblok bila Client berstatus Archived menempel walau tidak dihitung di Total Member

12. Ganti isi kotak search dengan `Hapus Arsip`, tekan Enter
13. Verifikasi Total Member baris `Hapus Arsip` adalah 0
14. Klik ikon `⋯` pada baris `Hapus Arsip`, lalu pilih "Delete"
15. Verifikasi dialog blok "Cannot Delete Group" tampil karena `Client Lama` (Archived) menempel
16. Klik `[OK]`
17. Verifikasi dialog blok tertutup
18. Verifikasi `Hapus Arsip` tetap ada di tabel

### TC-AC-SG-139: Delete diblok bila Partner yang di-assign langsung menempel

19. Ganti isi kotak search dengan `Hapus Partner`, tekan Enter
20. Klik ikon `⋯` pada baris `Hapus Partner`, lalu pilih "Delete"
21. Verifikasi dialog blok "Cannot Delete Group" dengan body "This group or its subgroups still have members. Remove all members before deleting." tampil untuk `Hapus Partner` walau `Partner Suspensi` berstatus Suspended
22. Verifikasi tidak ada jalur lanjut pada dialog (hanya tombol `[OK]`)
23. Klik `[OK]`

### TC-AC-SG-398: Delete diblok bila Distributor yang di-assign langsung menempel pada tree Principal

24. Ganti akun: logout, lalu login sebagai Total Control Principal (`totalControlGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`)
25. Buka Settings > Group lewat sidebar
26. Ketik Search `Region B`, tekan Enter
27. Klik ikon `⋯` pada baris `Region B`, lalu pilih "Delete"
28. Verifikasi dialog blok tampil: title "Cannot Delete Group", body bullet `Region B` dan "This group or its subgroups still have members. Remove all members before deleting." dengan satu tombol `[OK]` (tidak ada tombol lanjut) karena `Distributor Kencana` menempel di `Region B`
29. Klik `[OK]`
30. Verifikasi `Region B` tetap ada di tabel
31. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1, 6, 12, 19, dan 26 (Search untuk menemukan baris target, R-16); langkah 4, 9, 16, 23, dan 29 (`[OK]` menutup dialog blok; hasil penutupan diasersi di langkah 5, 10, 11, 17, 18, dan 30); langkah 24 dan 25 (ganti akun dan buka halaman, S-07); langkah 31 (reset Search).
- Urutan TC dalam spec mengikuti blok akun: TC-398 memakai akun Principal sehingga ditempatkan terakhir.
- Temuan untuk QA:
  - TC-AC-SG-138 menyebut "Client berstatus apa pun memblok Delete" sebagai alasan; yang diasersi hanya Expected (Total Member 0 dan dialog blok).
  - Akun Total Control Principal tertulis di Pre-setup #1 sedangkan kolom ACC TC-398 menunjuk #16 (entitas uji); spec memakai akun #1 dengan tree #16 dan #19.
