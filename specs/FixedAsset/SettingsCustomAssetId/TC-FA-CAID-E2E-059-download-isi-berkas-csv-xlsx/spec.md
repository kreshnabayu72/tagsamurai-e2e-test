---
id: TC-FA-CAID-E2E-059-download-isi-berkas-csv-xlsx
title: "Download: Isi Berkas CSV dan XLSX Code List dan Changelog"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-150
  - TC-FA-CAID-152
  - TC-FA-CAID-221
  - TC-FA-CAID-222
coverage:
  web: automated
---

# Download: Isi Berkas CSV dan XLSX Code List dan Changelog

## Prerequisites

- Mode: FE+BE (isi Code List dibaca dari backend nyata) dan binary buffer berkas unduhan.
- Akun aktor: Total Control Company Changelog (Pre-setup No 1, pola `totalControl_automated_{namaCompany}@qwertysystem.net`; Company Changelog, Pre-setup No 15). Email akun disediakan tim FE/BE (Pre-setup No 15 hanya menyebut env var). Login di hook `before` spec ini (kredensial `Spectra.env.FA_CHANGELOG_TC_PASSWORD`); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > Custom Asset ID); hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_TC_PASSWORD`).
- Environment variable: `FA_CHANGELOG_TC_PASSWORD` (Total Control Company Changelog) dan `FA_TC_PASSWORD` (akun default suite). Password tidak ditulis di spec atau fixture; kedua nama didaftarkan di tahap script.
- Hook suite (`suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-asset-id` disetel `seen` untuk akun Company Changelog; baseline Company Alpha (Pre-setup No 10 dan 11) tidak dipakai spec ini; layar awal Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka di `beforeEach`. Suite berjalan serial (`parallel: false`).
- Nilai data dirujuk lewat `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Master data Code List pada Company aktor (Company Changelog; nilai dari Pre-setup No 28): Groups `Head Office` (HO), `Head Office > Floor 1` (F1), `Head Office > Floor 2` (F2), `Jakarta Office` (JKT), `Surabaya Branch` (SBY, Excess), `Warehouse` (WH); Categories `IT Equipment` (ITE), `IT Equipment > Laptop` (LAP), `Old Equipment` (OLD, Locked), `Printer` (PRN); Asset Names `Dell, Latitude 14"` (DL14), `LaserJet Pro` (LJP), `ThinkPad T490` (T490); Divisions `Finance` (FIN), `Human Resources` (HR), `Operations` (OPS); Accounts Active `Computer Equipment` (1210) dan `Office Furniture` (1220). Di-seed di hook `before` lewat sesi API aktor Company Changelog (kemampuan disediakan tim FE). Dataset Code List dipakai TC-FA-CAID-150 dan 152.
- Data Pre-setup No 15 (`Company Changelog`): entri seed L1 sampai L7 log Custom Asset ID urut Date terbaru di atas di antara entri seed: L1 `15/09/26, 14:25` Edit Separator Old Value `Dash` New Value `Dot` oleh `Rina P`; L2 `14/09/26, 11:30` Edit Status `Inactive` ke `Active` oleh `Sarah J`; L3 `13/09/26, 09:15` Edit Status `Active` ke `Inactive` oleh `Budi S`; L4 `12/09/26, 16:40` Edit Separator `Slash` ke `Dash` oleh `Sarah J`; L5 `10/09/26, 10:02` Create Segments Formula Old Value `—` New Value `Initial Company (Inactive), Group Code (Active), Category Code (Active), Asset Name Code (Active), Division Code (Inactive), Account Code (Inactive), Purchase Date (Active), Asset Increment (Active)` oleh `Sarah J`; L6 `10/09/26, 10:01` Create Separator `—` ke `Slash` oleh `Sarah J`; L7 `10/09/26, 10:00` Create Status `—` ke `Active` oleh `Sarah J`; pengguna Rina Putri, Sarah Johnson, dan Budi Santoso. Di-seed lewat API di hook `before` pada Company aktor (kemampuan disediakan tim FE/BE). Entri Changelog bersifat permanen; entri baru dari spec lain tidak dihapus.
- Data Pre-setup No 27: General Settings Company aktor Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta` (baseline; spec tidak mengubahnya). Waktu Date entri seed dibandingkan sebagai teks berformat itu.
- Kemampuan teknis (disediakan tim FE): membaca buffer berkas CSV dan XLSX hasil unduhan (nama berkas, baris header, nilai sel, tanda kutip, BOM, nama sheet, jumlah baris data) dan membaca jumlah entri Changelog Custom Asset ID sebelum unduh sebagai baseline N (bagian 8b butir 10). Total entri Changelog tidak diasersi sebagai angka absolut (S-12): jumlah baris data berkas dibandingkan dengan N.
- Data Dinamis: tidak ada. State global: tidak ada yang diubah.

## Test Steps

### TC-FA-CAID-150: Isi CSV Code List

1. Klik tautan `[View Code List]`
2. Klik tab `Asset Name Codes`
3. Klik header `Asset Name` satu kali (Ascending)
4. Klik icon Download, pilih `Download as CSV`
5. Buka berkas hasil unduhan
6. Verifikasi baris pertama header `Asset Name,Code` disusul tiga baris data terurut A-Z
7. Verifikasi nama aset yang memuat koma dan tanda kutip ganda (`Dell, Latitude 14"`) diekspor sebagai satu sel dibungkus tanda kutip ganda dengan tanda kutip di dalamnya digandakan, diikuti kolom Code `DL14`
8. Verifikasi encoding UTF-8 dengan BOM

### TC-FA-CAID-152: Berkas XLSX Code List

9. Klik tab `Group Codes`
10. Klik icon Download, pilih `Download as XLSX`
11. Buka berkas hasil unduhan
12. Verifikasi berkas memuat satu sheet bernama `Sheet1`
13. Verifikasi sheet memuat header `Group Name` dan `Code`
14. Verifikasi sheet memuat enam baris data

### TC-FA-CAID-221: Isi CSV Changelog

15. Klik `[✕]` pada header Modal View Code List
16. Klik tombol `[Changelog]` pada header kartu untuk membuka Modal Changelog
17. Catat jumlah entri Changelog Custom Asset ID sebagai baseline N
18. Klik icon Download, pilih `Download as CSV`
19. Verifikasi tidak ada toast sukses
20. Buka berkas hasil unduhan
21. Verifikasi berkas bernama `Changelog-Custom-Asset-ID.csv`
22. Verifikasi baris header `Date,Action,Field,Old Value,New Value,Modified By`
23. Verifikasi jumlah baris data sama dengan N
24. Verifikasi baris data mengikuti urutan default Date terbaru di atas
25. Verifikasi baris L1: Date `"15/09/26, 14:25"` (dibungkus tanda kutip ganda karena memuat koma), Action `Edit`, Field `Separator`, Old Value `Dash`, New Value `Dot`, dan Modified By `Rina Putri`
26. Verifikasi baris L5: Date `"10/09/26, 10:02"` (dibungkus tanda kutip ganda), Old Value `-` (hyphen tunggal, bukan `—`), New Value `"Initial Company (Inactive), Group Code (Active), Category Code (Active), Asset Name Code (Active), Division Code (Inactive), Account Code (Inactive), Purchase Date (Active), Asset Increment (Active)"` dibungkus tanda kutip ganda karena memuat koma, dan Modified By `Sarah Johnson`
27. Verifikasi encoding UTF-8 dengan BOM

### TC-FA-CAID-222: Berkas XLSX Changelog

28. Klik icon Download, pilih `Download as XLSX`
29. Buka berkas hasil unduhan
30. Verifikasi berkas bernama `Changelog-Custom-Asset-ID.xlsx`
31. Verifikasi berkas memuat satu sheet bernama `Sheet1`
32. Verifikasi sheet memuat header enam kolom
33. Verifikasi jumlah baris data sama dengan N

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. 33 langkah. Kelas harness f (binary buffer): isi sel, escaping, BOM, dan nama sheet berkas diasersi di spec ini; nama berkas, header, dan jumlah baris Code List diasersi juga di spec 058.
- Langkah penghubung (tanpa `Verifikasi`): langkah 15 (menutup Modal View Code List sebelum membuka Modal Changelog, S-09) dan langkah 17 (mencatat baseline N; S-12 melarang angka absolut total entri Changelog).
- S-12 dan S-14: TC-FA-CAID-221 dan 222 relatif terhadap baseline N. Karena Changelog adalah audit trail permanen yang tumbuh, spec mengasersi jumlah baris data sama dengan N (termasuk entri seed L1 sampai L7), urutan Date menurun, serta isi baris L1 dan L5 yang dicari berdasarkan nilai kolomnya, bukan posisi teratas. Nilai Date bergantung pada baseline General Settings (Pre-setup No 27).
- Kolom Modified By pada berkas berisi nama lengkap (`Rina Putri`, `Sarah Johnson`) sesuai keputusan NC-15, bukan format `[First Name] [Last Initial]` tampilan tabel.
- Asersi absence "tidak ada toast sukses" (langkah 19) diletakkan tepat di bawah langkah pemicu (langkah 18) dan sebelum `Verifikasi` berkas (bagian 8b butir 11); pemicu menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas terunduh (langkah 21 dan seterusnya).
- Pembagian TC lintas spec: TC-FA-CAID-148, 149, 151, 153, dan 154 ada di spec 058; TC-FA-CAID-155 dan 226 (download gagal) ada di spec 062.
- Temuan untuk QA:
  - Kolom akun TC-FA-CAID-221 dan 222 menyebut akun #1 (Company Alpha) bersama dataset `Company Changelog` (Pre-setup No 15). Entri L1 sampai L7 hanya berada di urutan teratas Changelog bila Company-nya terpisah dari Company Alpha; spec memakai Company Changelog sebagai Company aktor seperti spec 066 sampai 079 dan tidak mengasersi konfigurasi B1 Company Alpha.
  - TC-FA-CAID-150 dan 152 tidak menyebut Company pemilik master data Code List; karena Company aktor spec ini adalah Company Changelog, spec meng-seed master data Pre-setup No 28 pada Company itu lewat sesi API aktor.
  - TC-FA-CAID-150 Expected b menyebut "Dell, Latitude 14 inci" dengan tanda kutip ganda; nama data Pre-setup No 28 adalah `Dell, Latitude 14"`. Spec memakai nama Pre-setup.
