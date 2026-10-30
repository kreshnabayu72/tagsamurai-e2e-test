---
id: TC-GS-GSET-E2E-030-changelog-filter-apply-field-modified-by-date-dan-kombinasi
title: "Modal Changelog: Filter Apply berdasarkan Field, Modified By, Rentang Date, dan Kombinasi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-73
  - TC-GS-GSET-74
  - TC-GS-GSET-76
  - TC-GS-GSET-77
  - TC-GS-GSET-78
coverage:
  web: automated
---

# Modal Changelog: Filter Apply berdasarkan Field, Modified By, Rentang Date, dan Kombinasi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Budi Santoso (`Budi S`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; akun ini adalah akun default suite sehingga hook `after` tidak mengganti sesi. Halaman General Settings dibuka di hook `beforeEach`. Password tidak ditulis di spec atau fixture.
- Akun pelaku seeding lewat sesi API (tidak login UI): Total Control Client A, Andi Wijaya (`Andi W`), `totalControlGlobalSettingsB_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 2), password `Spectra.env.GS_TCB_PASSWORD` (nama env baru; pendaftaran di `spectra.config.ts` dan `.env.example` dilakukan pada tahap script).
- Environment variable: `GS_TC_PASSWORD`, `GS_TCB_PASSWORD`.
- Sesi API aktor memakai token yang tidak dihitung sebagai sesi web (pernyataan di `suite.md`).
- Seeding minimal (S-11, S-12; hook `before`, sesudah record Client A berada di baseline Pre-setup baris 10 dan pada tanggal yang sama dengan eksekusi langkah), tiga `PUT /v2/enterprise-management/general-settings` (`global-settings/general-settings/API/openapi.yaml`) berurutan, payload mengacu ke `Fixture.generalSettings.payloadIdle60TzUtc`, `Fixture.generalSettings.payloadIdle120TzUtcDateMdy`, dan `Fixture.generalSettings.payloadBaseline` (fixture belum ada; dibuat pada tahap script):
  - `PUT` oleh Budi Santoso dengan `sessionIdleTimeout` 60 dan `timezone` `UTC` (nilai lain baseline): baris Field `Session Idle Timeout` (`30 minutes` menjadi `1 hour`) dan baris Field `Time Zone` (`(UTC+07:00) Bangkok, Hanoi, Jakarta` menjadi `(UTC+00:00) UTC, Reykjavik, Accra`), Modified By `Budi S`.
  - `PUT` oleh Andi Wijaya dengan `sessionIdleTimeout` 120 dan `dateFormat` `M/d/yy`: baris Field `Session Idle Timeout` (`1 hour` menjadi `2 hours`) dan baris Field `Date Format` (`dd/MM/yy` menjadi `M/d/yy`), Modified By `Andi W`.
  - `PUT` oleh Budi Santoso kembali ke baseline: tiga baris balik (Field `Session Idle Timeout`, `Time Zone`, `Date Format`), Modified By `Budi S`.
  - Hasil: tujuh baris terbaru di halaman pertama. Field `Session Idle Timeout`: Modified By `Budi S` dan `Andi W`; Field `Time Zone`: `Budi S`; Field `Date Format`: `Budi S` dan `Andi W`. Setiap kolom yang difilter (Field, Modified By) memiliki sedikitnya dua nilai distinct, dan kombinasi Field `Session Idle Timeout` dengan Modified By `Andi W` serta Field `Time Zone` dengan Modified By `Budi S` ada sebagai baris yang dikecualikan oleh irisan di langkah 31.
- Rentang Date: hari ini dihitung dari tanggal klien saat langkah dijalankan; jam server dan jam browser sinkron (S-12). Kemarin tidak memiliki baris Changelog untuk Client A (kebutuhan TC-GS-GSET-77 b); Changelog adalah audit trail permanen sehingga tim FE memastikan environment Client A tidak memuat entri bertanggal kemarin (lihat Temuan untuk QA).
- Changelog General Settings tidak pernah diasersi sebagai jumlah entri absolut (S-12); asersi memakai pola baris. Entri tidak dihapus.
- Kemampuan teknis: memilih rentang tanggal pada date range picker (hari ini dan kemarin); membaca teks input Date.
- Pemulihan di hook `after` (tetap jalan walau spec gagal di tengah): Modal Changelog ditutup; record Client A di baseline (hook suite).
- Flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` dan pemulihan baseline record: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-GSET-73: Filter Changelog berdasarkan Field

1. Klik icon Changelog di pojok kanan atas halaman
2. Klik Filter di toolbar
3. Pilih Field `Session Idle Timeout`
4. Klik `[Apply]`
5. Verifikasi tabel menampilkan baris Field `Session Idle Timeout`
6. Verifikasi tabel hanya menampilkan baris Field `Session Idle Timeout` (baris Field `Time Zone` dan `Date Format` tidak tampil)

### TC-GS-GSET-74: Filter Field dengan dua opsi menggabungkan hasil (OR dalam field)

7. Klik Filter, lalu klik `[Clear Field]`
8. Pilih Field `Session Idle Timeout` dan `Time Zone`
9. Klik `[Apply]`
10. Verifikasi tabel menampilkan baris Field `Session Idle Timeout` dan baris Field `Time Zone`
11. Verifikasi baris Field `Date Format` tidak tampil
12. Klik Filter
13. Verifikasi chip `Session Idle Timeout` dan chip `Time Zone` tampil di dalam field Field

### TC-GS-GSET-76: Filter Changelog berdasarkan Modified By

14. Klik `[Clear Field]`
15. Pilih Modified By `Budi S`
16. Klik `[Apply]`
17. Verifikasi tabel menampilkan baris Modified By `Budi S`
18. Verifikasi tabel hanya menampilkan baris Modified By `Budi S` (baris Modified By `Andi W` tidak tampil)

### TC-GS-GSET-77: Filter Changelog berdasarkan rentang Date

19. Klik Filter, lalu klik `[Clear Field]`
20. Pilih rentang tanggal hari ini pada field Date
21. Verifikasi teks tanggal di input Date mengikuti Date Format General Settings tersimpan (pola `dd/MM/yy`)
22. Klik `[Apply]`
23. Verifikasi tabel menampilkan baris yang dibuat hari ini (baris Field `Session Idle Timeout`, Modified By `Budi S`)
24. Klik Filter, lalu pilih rentang tanggal kemarin saja pada field Date
25. Klik `[Apply]`
26. Verifikasi empty state `No results found` dengan deskripsi `Try adjusting your search or filter.`

### TC-GS-GSET-78: Kombinasi filter Field dan Modified By (AND antar field)

27. Klik Filter, lalu klik `[Clear Field]`
28. Pilih Field `Session Idle Timeout` dan Modified By `Budi S`
29. Klik `[Apply]`
30. Verifikasi tabel menampilkan baris Field `Session Idle Timeout` dengan Modified By `Budi S`
31. Verifikasi tabel hanya menampilkan irisan: baris Field `Session Idle Timeout` dengan Modified By `Andi W` dan baris Field `Time Zone` dengan Modified By `Budi S` tidak tampil

## Notes

- Mode: FE+BE. Sumber: `global-settings/general-settings/TestCases/tc-general-settings.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-73, 74, 76, 77, 78 (urutan TC). Tiap blok dimulai dengan `[Clear Field]` agar kriteria blok sebelumnya tidak ikut (S-09); `[Clear Field]` pada panel yang diikuti pilihan baru dan `[Apply]` mengganti seluruh kriteria. Modal Changelog dibuka sekali di langkah 1.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7, 14, 19, 27 (`[Clear Field]` untuk pembersih state antar blok), langkah 12 (membuka kembali Filter agar chip dapat diamati; Expected TC-74 menyebut chip tampil di dalam field filter), dan langkah 24 (membuka Filter sebelum memilih rentang tanggal kemarin).
- Langkah 5, 10, 17, 23, dan 30 `Verifikasi` baris yang seharusnya tampil adalah pembanding positif sebelum asersi universal atau absence pada langkah 6, 11, 18, 26 (empty state), dan 31 (bagian 8b butir 2); Expected TC-73, 76, dan 78 menyebut "hanya" tanpa pembanding.
- Asersi memakai pola baris (bukan jumlah baris), sehingga entri Changelog dari run atau spec lain tidak memengaruhi hasil.
- Temuan untuk QA:
  - TC-GS-GSET-77 b mengasumsikan rentang kemarin tidak memiliki baris; Changelog adalah audit trail permanen dan run pada hari sebelumnya meninggalkan entri, sehingga asersi bergantung pada environment yang tidak memiliki entri bertanggal kemarin. TC tidak menyebut cara menjamin kondisi itu.
  - TC-GS-GSET-77 a tidak menyebut contoh teks tanggal pada input Date; spec mengasersi kesesuaian dengan pola Date Format tersimpan (`dd/MM/yy`, baseline Pre-setup baris 10).
  - TC-GS-GSET-74 tidak menyebut baris pembanding yang tidak ikut hasil; spec memakai baris Field `Date Format` hasil seeding sebagai penanda OR.
