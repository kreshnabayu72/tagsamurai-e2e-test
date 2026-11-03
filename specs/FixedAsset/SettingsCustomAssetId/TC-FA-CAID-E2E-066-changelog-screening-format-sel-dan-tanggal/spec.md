---
id: TC-FA-CAID-E2E-066-changelog-screening-format-sel-dan-tanggal
title: "Modal Changelog: Screening, Format Sel, dan Format Tanggal General Settings"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-164
  - TC-FA-CAID-165
  - TC-FA-CAID-166
  - TC-FA-CAID-341
  - TC-FA-CAID-342
coverage:
  web: automated
---

# Modal Changelog: Screening, Format Sel, dan Format Tanggal General Settings

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Changelog (Pre-setup No 1, pola `totalControl_automated_{namaCompany}@qwertysystem.net`; Company Changelog, Pre-setup No 15). Email akun disediakan tim FE/BE (Pre-setup No 15 hanya menyebut env var). Login di hook `before` spec ini (kredensial `Spectra.env.FA_CHANGELOG_TC_PASSWORD`); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > Custom Asset ID); hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_TC_PASSWORD`).
- Environment variable: `FA_CHANGELOG_TC_PASSWORD` (Total Control Company Changelog) dan `FA_TC_PASSWORD` (akun default suite). Password tidak ditulis di spec atau fixture; kedua nama didaftarkan di tahap script.
- Data Pre-setup (hanya dibaca): No 15 Company Changelog; No 27 General Settings Company Changelog (Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta`). Data Dinamis: tidak ada. Nilai L1 sampai L7 adalah data Pre-setup tetap (bukan data Dinamis) sehingga tidak bersuffix `{runId}`; fixture modul Custom Asset ID untuk nilai ini dan teks UI belum ada; prasyarat tahap script yang disediakan tim FE/BE.
- Entri Changelog seed (Pre-setup No 15, urut Date terbaru di atas, pengguna Rina Putri `Rina P`, Sarah Johnson `Sarah J`, Budi Santoso `Budi S`):

| Id | Date | Action | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|
| L1 | `15/09/26, 14:25` | Edit | Separator | `Dash` | `Dot` | `Rina P` |
| L2 | `14/09/26, 11:30` | Edit | Status | `Inactive` | `Active` | `Sarah J` |
| L3 | `13/09/26, 09:15` | Edit | Status | `Active` | `Inactive` | `Budi S` |
| L4 | `12/09/26, 16:40` | Edit | Separator | `Slash` | `Dash` | `Sarah J` |
| L5 | `10/09/26, 10:02` | Create | Segments Formula | `—` | `Initial Company (Inactive), Group Code (Active), Category Code (Active), Asset Name Code (Active), Division Code (Inactive), Account Code (Inactive), Purchase Date (Active), Asset Increment (Active)` | `Sarah J` |
| L6 | `10/09/26, 10:01` | Create | Separator | `—` | `Slash` | `Sarah J` |
| L7 | `10/09/26, 10:00` | Create | Status | `—` | `Active` | `Sarah J` |

- Seeding (hook `before`, lewat sesi API aktor): ketujuh entri L1 sampai L7 dengan Date, Action, Field, Old Value, New Value, dan Modified By persis tabel di atas (entri L1 tersimpan 15/09/26 07:25 UTC). Cara membuat entri Changelog bertanggal tetap dengan Modified By pengguna lain tidak disebut TC, PRD, atau LLD: disediakan tim FE/BE. Entri log audit lain pada Company Changelog tidak dihapus dan tidak diasersi (audit trail permanen, S-12); spec ini tidak menambah entri Changelog. Entri Changelog tidak bisa dihapus.
- Precondition TC-FA-CAID-164, TC-FA-CAID-165, TC-FA-CAID-166, TC-FA-CAID-341, TC-FA-CAID-342 (kecuali dinyatakan lain di butir berikut): login sebagai Total Control; Company Changelog dengan entri seed L1 sampai L7 (Pre-setup No 15); General Settings Date Format `dd/MM/yy` dan Time Format 24 jam; berada di Fixed Asset > Settings > Asset Master > Custom Asset ID.
- Akun kedua (hanya untuk TC-FA-CAID-342): Total Control Company Alpha (Pre-setup No 1, Sarah Johnson), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Ganti akun lewat langkah eksplisit (33 dan 34); hook `after` mengembalikan sesi ke akun default suite, yaitu akun yang sama.
- Kemampuan teknis: mengubah Date Format, Time Format, dan Time Zone General Settings (UI atau seed; TC dan PRD tidak menyebut caranya, disediakan tim FE/BE); hover sel Modified By untuk membaca tooltip; membaca teks sel Date; memilih rentang tanggal pada date range picker Filter dan membaca teks input `Date`.
- Data TC-FA-CAID-342: aset A1 Company Alpha (Pre-setup No 11, `JKT/LAP/T490/0926/1`) dengan satu entri Histori Aset ber-Changed At 15/09/26 07:25 UTC (seed, disediakan tim FE/BE; TC tidak menyebut cara membuat entri Histori Aset bertanggal tetap). General Settings Company Alpha untuk TC-FA-CAID-342: Date Format `dd MMM yy`, Time Format 12 jam, Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta` (varian Pre-setup No 27), disiapkan hook `before` lewat seed.
- State global yang diubah dan dipulihkan: General Settings Company Changelog (TC-FA-CAID-341 mengubah Time Zone menjadi `(UTC+08:00) Kuala Lumpur, Singapore, Makassar`; TC-FA-CAID-166 mengubah Date Format menjadi `dd MMM yy` dan Time Format menjadi 12 jam) dipulihkan lewat langkah 22 dan 31 ke nilai Pre-setup No 27 (`dd/MM/yy`, 24 jam, `(UTC+07:00) Bangkok, Hanoi, Jakarta`); hook `after` memulihkan lagi walau spec gagal di tengah, termasuk varian General Settings Company Alpha untuk TC-FA-CAID-342 (dikembalikan ke `dd/MM/yy` dan 24 jam).
- Suite serial (`parallel: false`) karena Company Changelog dan preferensi kolom browser dipakai bersama spec Modal Changelog lain dan sebagian spec mengubah state General Settings.
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-asset-id`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.

## Test Steps

### TC-FA-CAID-164: Screening Modal Changelog: Custom Asset ID saat dibuka (3 zona)

1. Klik tombol `[Changelog]` pada header kartu
2. Verifikasi Zona Header: Title `Changelog: Custom Asset ID` dengan ikon close `[✕]`
3. Verifikasi Zona Header: Table Tools `Search | Filter | Download`
4. Verifikasi Zona Body: kolom `Date (sortable) | Action (sortable) | Field (sortable) | Old Value (sortable) | New Value (sortable) | Modified By (sortable) | Actions (⋯) (unsortable)`
5. Verifikasi Zona Body: baris seed L1 sampai L7 tampil dengan urutan relatif Date terbaru di atas (L1 di atas L2 dan seterusnya): L1 `15/09/26, 14:25` Edit Separator `Dash` ke `Dot` oleh `Rina P`; L2 `14/09/26, 11:30` Edit Status `Inactive` ke `Active` oleh `Sarah J`; L3 `13/09/26, 09:15` Edit Status `Active` ke `Inactive` oleh `Budi S`; L4 `12/09/26, 16:40` Edit Separator `Slash` ke `Dash` oleh `Sarah J`; L5 `10/09/26, 10:02` Create Segments Formula oleh `Sarah J`; L6 `10/09/26, 10:01` Create Separator `Slash`; L7 `10/09/26, 10:00` Create Status `Active`
6. Verifikasi Zona Footer: pagination default 10 data per halaman
7. Verifikasi tidak ada kolom `Object` dan tidak ada kolom `Entity` pada tabel

### TC-FA-CAID-165: Format sel Changelog: Action plain text, strip untuk Create, Modified By dengan tooltip nama lengkap, tanggal ikut General Settings

8. Verifikasi kolom Action menampilkan teks polos `Create` dan `Edit` tanpa badge berwarna
9. Verifikasi baris L7: Old Value `—` dan New Value `Active`
10. Verifikasi baris L1: Old Value `Dash` dan New Value `Dot`
11. Verifikasi kolom Date baris L1 menampilkan `15/09/26, 14:25` mengikuti Date Format dan Time Format General Settings
12. Verifikasi kolom Modified By baris L1 menampilkan `Rina P` sebagai teks polos
13. Hover sel Modified By baris L1
14. Verifikasi tooltip hover menampilkan `Rina Putri`

### TC-FA-CAID-341: Kolom Date Modal Changelog mengikuti Time Zone General Settings

15. Verifikasi kolom Date baris L1 menampilkan `15/09/26, 14:25` (Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta`)
16. Klik `[✕]` pada Modal Changelog
17. Ubah Time Zone General Settings menjadi `(UTC+08:00) Kuala Lumpur, Singapore, Makassar`
18. Tunggu aksi selesai (General Settings tersimpan)
19. Klik tombol `[Changelog]` pada header kartu
20. Verifikasi kolom Date baris L1 menampilkan `15/09/26, 15:25`
21. Klik `[✕]` pada Modal Changelog
22. Pulihkan Time Zone General Settings ke `(UTC+07:00) Bangkok, Hanoi, Jakarta`

### TC-FA-CAID-166: Tanggal Changelog dan input filter Date mengikuti Date Format General Settings yang diubah

23. Atur General Settings: Date Format `dd MMM yy` dan Time Format 12 jam
24. Tunggu aksi selesai (General Settings tersimpan)
25. Klik tombol `[Changelog]` pada header kartu
26. Verifikasi kolom Date baris L1 menampilkan `15 Sep 26, 02:25 PM` mengikuti format General Settings
27. Klik icon Filter, lalu pilih rentang tanggal 12 sampai 13 September 2026 pada field `Date`
28. Verifikasi teks tanggal terpilih pada input field `Date` memakai format `dd MMM yy` yang sama
29. Klik icon Filter untuk menutup panel tanpa menekan `[Apply]`
30. Klik `[✕]` pada Modal Changelog
31. Pulihkan General Settings: Date Format `dd/MM/yy` dan Time Format 24 jam

### TC-FA-CAID-342: Kolom Changed At tab Histori Aset mengikuti Date Format dan Time Format General Settings

32. Tunggu aksi selesai (General Settings tersimpan)
33. Ganti akun: Logout dari akun Total Control Company Changelog
34. Login sebagai Total Control Company Alpha (`totalControl_automated_{namaCompany}@qwertysystem.net`)
35. Buka Fixed Asset > Assets > All Assets > Detail A1 > tab `Histori Aset`
36. Verifikasi Changed At entri Histori Aset A1 yang tersimpan 15/09/26 07:25 UTC menampilkan `15 Sep 26, 02:25 PM`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. 36 langkah, sedikit di atas 35 langkah. Alasan: semua blok memakai satu dataset Company Changelog dan satu state General Settings yang diubah lalu dipulihkan, dan tiap blok berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna); dua langkah `Tunggu aksi selesai` (langkah 18 dan 24) dan dua langkah pemulihan General Settings berasal dari bagian 8b butir 8 dan S-09.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-FA-CAID-164, 165, 341, 166, 342. Alasan: screening dan format sel pada state baseline lebih dulu (164, 165); TC-FA-CAID-341 (Time Zone) sebelum TC-FA-CAID-166 supaya Date Format dan Time Format General Settings hanya diubah satu kali dan dipulihkan satu kali; TC-FA-CAID-342 di akhir karena berpindah akun dan surface (Histori Aset). Modal Changelog dibuka di langkah 1 untuk TC-FA-CAID-164 dan 165, lalu dibuka kembali tiap kali General Settings berubah.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): langkah 16, 21, 30 (menutup Modal Changelog sebelum General Settings diubah), langkah 17 dan 23 (mengatur General Settings sesuai precondition TC-FA-CAID-341 dan 166; langkah 17 juga langkah TC-FA-CAID-341), langkah 18 dan 24 (`Tunggu aksi selesai`: General Settings tersimpan sebelum Modal Changelog dibuka, bagian 8b butir 8), langkah 22 dan 31 (memulihkan General Settings; hook `after` sebagai cadangan), langkah 29 (membuang draft rentang tanggal yang tidak di-Apply), dan langkah 32, 33, 34, 35 (menunggu pemulihan General Settings selesai, ganti akun dan membuka tab `Histori Aset`; akun pertama login di hook `before`, S-07). Pemulihan Time Zone sebelum TC-FA-CAID-166 dan pemulihan format sebelum ganti akun mencegah state TC sebelumnya terbawa.
- Rentang tanggal Filter pada TC-FA-CAID-166 tidak disebut konkret oleh TC; spec memakai 12 sampai 13 September 2026 (rentang yang sama dengan TC-FA-CAID-178). Asersi hanya pada format teks tanggal terpilih.
- Kelas harness: state global General Settings (format tanggal) untuk TC-FA-CAID-166, 341, dan 342; TC-FA-CAID-164 dan 165 adalah screening dan format sel pada state baseline. P-5 butir (b): TC-FA-CAID-166 dan 341 adalah objek uji ringan (format tanggal General Settings tanpa harness eksternal dan tanpa state berat) yang berada di spec Modal Changelog; TC-FA-CAID-342 memakai state General Settings yang sama pada surface Histori Aset sehingga tidak butuh state baru. Batas P-5 butir (b) adalah dua TC objek-uji ringan per spec; spec ini memuat tiga TC format tanggal General Settings (TC-FA-CAID-166, 341, 342). Pemindahan TC-FA-CAID-342 ke spec sendiri membutuhkan nomor spec baru dan menunggu keputusan; sampai saat itu ketiganya tetap di spec ini.
- Pembagian TC lintas spec: Search Modal Changelog ada di spec 067 dan 068; Filter di spec 069 sampai 072; Sort di spec 073; Setup Column di spec 074 sampai 077; Pagination di spec 078; Download di spec 079 dan 080; isi berkas Download Changelog (TC-FA-CAID-221, 222) ada di spec 059.
- Temuan untuk QA: (1) TC-FA-CAID-164 Expected b.ii menyebut baris seed L1 sampai L7 tampil tanpa menyebut cara menemukannya di audit trail permanen yang tumbuh; spec mengikuti TC (tanpa Filter Date) dan baris seed hanya tampil di halaman pertama bila tidak ada entri Changelog lain yang lebih baru pada Company Changelog. (2) TC-FA-CAID-164 Expected d "tidak ada kolom Object dan tidak ada kolom Entity" diasersi sebagai satu `Verifikasi` daftar elemen yang sama-sama tidak ada. (3) Kolom ACC TC-FA-CAID-164 sampai 166 dan 341 memuat akun #1 dan precondition b menyebut Company Alpha baseline B1 bersama Company Changelog; entri L1 sampai L7 bertanggal September 2026 hanya berada di urutan teratas Changelog bila Company-nya terpisah dari Company Alpha yang menerima entri baru dari spec lain, sehingga spec memakai Company Changelog sebagai Company aktor dan tidak mengasersi konfigurasi B1. (4) Cara membuat entri Changelog bertanggal tetap oleh `Rina P` dan `Budi S` tidak tertulis di Pre-setup TC. (5) TC-FA-CAID-166 dan 341 tidak menyebut cara mengubah General Settings (UI atau seed). (6) Perilaku panel Filter sesudah `[Apply]` tidak konsisten antar TC (lihat spec 070 sampai 072); TC-FA-CAID-342 hanya menyebut entri seed, bukan entri Histori Aset lain milik A1.
