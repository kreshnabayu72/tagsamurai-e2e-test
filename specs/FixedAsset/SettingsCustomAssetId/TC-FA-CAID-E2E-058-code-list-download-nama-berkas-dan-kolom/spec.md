---
id: TC-FA-CAID-E2E-058-code-list-download-nama-berkas-dan-kolom
title: "Modal View Code List: Download Overlay, Nama Berkas, Search Aktif, dan Kolom Tersembunyi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-148
  - TC-FA-CAID-149
  - TC-FA-CAID-151
  - TC-FA-CAID-153
  - TC-FA-CAID-154
coverage:
  web: automated
---

# Modal View Code List: Download Overlay, Nama Berkas, Search Aktif, dan Kolom Tersembunyi

## Prerequisites

- Mode: FE+BE (isi Code List dibaca dari backend nyata).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun aktor: Total Control Company Alpha (Pre-setup No 1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Hook suite (`suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-asset-id` disetel `seen`; konfigurasi Company Alpha baseline B1 (Pre-setup No 10) dan aset A1 sampai A5 (Pre-setup No 11) dipulihkan lewat seed API sesi aktor; layar awal Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka di `beforeEach`. Suite berjalan serial (`parallel: false`).
- Nilai data dirujuk lewat `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Master data Code List Company Alpha (Pre-setup No 28): Groups `Head Office` (HO), `Head Office > Floor 1` (F1), `Head Office > Floor 2` (F2), `Jakarta Office` (JKT), `Surabaya Branch` (SBY, Excess), `Warehouse` (WH); Categories `IT Equipment` (ITE), `IT Equipment > Laptop` (LAP), `Old Equipment` (OLD, Locked), `Printer` (PRN); Asset Names `Dell, Latitude 14"` (DL14), `LaserJet Pro` (LJP), `ThinkPad T490` (T490); Divisions `Finance` (FIN), `Human Resources` (HR), `Operations` (OPS); Accounts Active `Computer Equipment` (1210) dan `Office Furniture` (1220). Di-seed di hook `before` lewat sesi API aktor (kemampuan disediakan tim FE). Spec hanya membaca.
- Kemampuan teknis: membaca berkas hasil unduhan (nama berkas, baris header, jumlah baris data) disediakan tim FE; isi sel dan encoding berkas diasersi di spec 059. Pemantauan toast dilakukan pada halaman.
- Data Dinamis: tidak ada. State global: visibilitas kolom `Code` tab `Group Codes` diubah pada TC-FA-CAID-154 lalu ditampilkan kembali; hook `after` spec ini menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan itu disediakan tim FE.

## Test Steps

### TC-FA-CAID-148: Overlay Download

1. Klik tautan `[View Code List]`
2. Hover icon Download
3. Verifikasi tooltip `Download` tampil
4. Klik icon Download
5. Verifikasi overlay memuat opsi `Download as CSV` dan `Download as XLSX`

### TC-FA-CAID-149: Nama berkas Download per tab

6. Pilih `Download as CSV` (tab `Group Codes`)
7. Klik tab `Category Codes`
8. Klik icon Download, pilih `Download as CSV`
9. Klik tab `Asset Name Codes`
10. Klik icon Download, pilih `Download as CSV`
11. Klik tab `Division Codes`
12. Klik icon Download, pilih `Download as CSV`
13. Klik tab `Account Codes`
14. Klik icon Download, pilih `Download as CSV`
15. Verifikasi berkas CSV bernama `Code-List-Group-Codes.csv`, `Code-List-Category-Codes.csv`, `Code-List-Asset-Name-Codes.csv`, `Code-List-Division-Codes.csv`, dan `Code-List-Account-Codes.csv` untuk kelima tab
16. Klik tab `Group Codes`
17. Klik icon Download, pilih `Download as XLSX`
18. Verifikasi tidak ada toast sukses
19. Verifikasi berkas XLSX tab `Group Codes` bernama `Code-List-Group-Codes.xlsx`

### TC-FA-CAID-151: Download mengikuti Search aktif

20. Ketik Search `floor`, tekan Enter
21. Klik icon Download, pilih `Download as CSV`
22. Verifikasi berkas berisi header dan hanya dua baris data `Head Office > Floor 1,F1` dan `Head Office > Floor 2,F2`

### TC-FA-CAID-153: Download dengan hasil Search nol baris

23. Ganti isi kotak search dengan `zzzzz`, tekan Enter
24. Verifikasi tombol Download tetap aktif
25. Klik icon Download, pilih `Download as CSV`
26. Verifikasi tidak ada toast
27. Verifikasi berkas CSV hanya berisi baris header `Group Name,Code`

### TC-FA-CAID-154: Kolom tersembunyi tidak ikut diekspor

28. Klik `(←)` pada kotak Search
29. Sembunyikan kolom `Code` melalui overlay Column Visibility, lalu tutup overlay
30. Klik icon Download, pilih `Download as CSV`
31. Verifikasi berkas pertama hanya berisi kolom `Group Name`
32. Tampilkan kembali kolom `Code` melalui overlay Column Visibility, lalu tutup overlay
33. Klik icon Download, pilih `Download as CSV`
34. Verifikasi berkas kedua berisi kolom `Group Name` dan `Code`

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. 34 langkah.
- Subjudul `###` memetakan langkah ke id TC granular. Modal tetap terbuka dari TC-FA-CAID-148 sampai akhir spec.
- Pada TC-FA-CAID-149 Expected a menyebut kelima nama berkas CSV dalam satu butir; kelima unduhan dilakukan berurutan lalu satu `Verifikasi` memeriksa kelima nama (langkah di antara tab adalah langkah TC "Ulangi pada tab ...").
- Asersi absence "tidak ada toast" (langkah 18 dan 26) diletakkan tepat di bawah langkah pemicu (langkah 17 dan 25) dan sebelum `Verifikasi` berkas (langkah 19 dan 27); pemicu menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas terunduh (bagian 8b butir 11).
- Langkah penghubung (tanpa `Verifikasi`): langkah 28 (klik `(←)` mengosongkan Search `zzzzz` sebelum TC-FA-CAID-154, S-09) dan langkah menutup overlay Column Visibility pada TC-FA-CAID-154.
- Urutan TC di dalam spec: TC-FA-CAID-148, 149, 151, 153, lalu 154. TC-FA-CAID-154 mengubah visibilitas kolom sehingga ditaruh paling akhir.
- Pembagian TC lintas spec: isi sel, escaping, dan encoding berkas Code List (TC-FA-CAID-150 dan 152) ada di spec 059; TC-FA-CAID-155 (download gagal) ada di spec 062.
- Temuan untuk QA:
  - TC-FA-CAID-151 menyebut dua baris data (`Head Office > Floor 1,F1` dan `Head Office > Floor 2,F2`) sebagai Expected; spec memeriksanya sebagai jumlah dan isi baris hasil Search tanpa membuka encoding berkas.
