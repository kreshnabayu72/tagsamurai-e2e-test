---
id: TC-GS-GSET-E2E-036-changelog-download-overlay-nama-file-dan-isi-csv-xlsx
title: "Download Changelog General Settings: Overlay, Nama Berkas, dan Isi Berkas CSV dan XLSX"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-97
  - TC-GS-GSET-98
  - TC-GS-GSET-99
  - TC-GS-GSET-100
  - TC-GS-GSET-159
coverage:
  web: automated
---

# Download Changelog General Settings: Overlay, Nama Berkas, dan Isi Berkas CSV dan XLSX

## Prerequisites

- Mode: FE+BE. Spec ini kelas binary buffer (prinsip 13f konvensi): isi berkas CSV dan XLSX dipisah dari kegagalan export (spec 026).
- Akun aktor: Total Control Client A, Budi Santoso (`Budi S`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup TC baris 1; `Fixture.generalSettings.totalControl`, fixture belum ada), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); halaman General Settings dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Sesi API aktor memakai token yang tidak dihitung sebagai sesi web (pernyataan di `suite.md`).
- Hook suite (`suite.md`, bagian Hook suite): flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` disetel true untuk akun aktor dan record Client A dipulihkan ke baseline sebelum spec; spec ini tidak mengatur flag sendiri.
- Data Pre-setup: record General Settings Client A baseline (Pre-setup 10: `IDR`, `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`, `30 minutes`). Date Format `dd/MM/yy` dan Time Format `HH:mm` tersimpan saat Download; spec tidak mengubah record lewat UI.
- Seeding di hook `before` (lewat 12 PUT `/v2/enterprise-management/general-settings` full-replace, `global-settings/general-settings/API/openapi.yaml`, sesi API Budi Santoso; tiap PUT mengubah tepat satu field sehingga menambah satu baris Changelog): delapan baris Field `Session Idle Timeout` (`sessionIdleTimeout` 30, 60, 120, 240, 60, 120, 240, 480, lalu kembali 30), dua baris Field `Time Format` (`HH:mm` ke `hh:mm a` lalu kembali), dan dua baris Field `Date Format` (`dd/MM/yy` ke `M/d/yy` lalu kembali). Record berakhir pada baseline. Seeding ini menjamin Changelog memuat sedikitnya 11 baris (TC-98 butir d: lebih dari 10 baris halaman aktif) dan memuat baris Field selain `Session Idle Timeout` sehingga hasil Search `Session Idle` (TC-100) berbeda dari seluruh riwayat (S-11). Jumlah total entri tidak disebut sebagai angka tetap (audit trail permanen).
- Kemampuan teknis: (1) menangkap berkas unduhan browser ke direktori bersih per unduhan supaya nama berkas yang sama (`Changelog-General-Settings.csv`) tidak tertimpa atau diberi akhiran `(1)`; (2) membaca isi berkas CSV dan XLSX (nama kolom, jumlah baris data, nilai sel); (3) membaca total entri Changelog General Settings Client A (`N_total`) sebagai pembanding jumlah baris berkas; (2) dan (3) disediakan tim FE/BE karena TC tidak menyebut caranya. Berkas unduhan dihapus di hook `after`.
- State yang diubah dan dipulihkan: Search (dikosongkan di langkah 27) dan visibilitas kolom `Modified By` (dikembalikan tampil di langkah 28); hook `after` (tetap jalan walau spec gagal di tengah) mengembalikan konfigurasi kolom Changelog ke default lewat penghapusan preferensi kolom Changelog di browser (mekanisme disediakan tim FE).
- Suite berjalan serial (`parallel: false`): `N_total` dibaca sekali pada langkah 5 dan harus sama dengan jumlah baris berkas pada langkah 10.

## Test Steps

### TC-GS-GSET-97: Overlay Download Changelog

1. Klik icon Changelog di pojok kanan atas halaman
2. Klik Download di toolbar
3. Verifikasi overlay memuat pilihan `Download as CSV`
4. Verifikasi overlay memuat pilihan `Download as XLSX`

### TC-GS-GSET-98: Download Changelog sebagai CSV

5. Catat total entri Changelog General Settings Client A sebagai `N_total`
6. Klik `Download as CSV`
7. Verifikasi tidak ada toast sukses
8. Verifikasi berkas `Changelog-General-Settings.csv` terunduh
9. Buka isi berkas `Changelog-General-Settings.csv` yang diunduh
10. Verifikasi jumlah baris data berkas sama dengan `N_total` (seluruh riwayat)
11. Verifikasi jumlah baris data berkas lebih dari 10 (melebihi halaman aktif)
12. Verifikasi kolom Date pada setiap baris data memakai pola tanggal Date Format tersimpan `dd/MM/yy`
13. Verifikasi kolom Date pada setiap baris data memakai pola waktu Time Format tersimpan `HH:mm`

### TC-GS-GSET-99: Download Changelog sebagai XLSX

14. Klik Download di toolbar
15. Klik `Download as XLSX`
16. Verifikasi tidak ada toast sukses
17. Verifikasi berkas `Changelog-General-Settings.xlsx` terunduh

### TC-GS-GSET-100: Download Changelog mengikuti Search/Filter dan kolom yang tampil

18. Ketik Search `Session Idle`, tekan Enter
19. Buka Setup Column via header kolom Actions (⋯) > `Setup Column...`, hilangkan centang kolom `Modified By`, klik `[Save]`
20. Klik Download di toolbar
21. Klik `Download as CSV`
22. Buka isi berkas `Changelog-General-Settings.csv` yang diunduh
23. Verifikasi berkas memuat sedikitnya satu baris data
24. Verifikasi setiap baris data berkas bernilai Field `Session Idle Timeout` (hanya baris yang cocok dengan Search)
25. Verifikasi berkas memuat kolom Date, Action, Field, Old Value, dan New Value
26. Verifikasi berkas tidak memuat kolom Modified By

### TC-GS-GSET-159: Kolom yang di-hide lalu di-unhide kembali ikut ter-export

27. Klik `(←)` pada kotak Search
28. Buka Setup Column via header kolom Actions (⋯) > `Setup Column...`, centang kembali kolom `Modified By`, klik `[Save]`
29. Klik Download di toolbar
30. Klik `Download as CSV`
31. Buka isi berkas `Changelog-General-Settings.csv` yang diunduh
32. Verifikasi berkas memuat kolom Modified By

## Notes

- Sumber TC: `global-settings/general-settings/TestCases/tc-general-settings.md` (Section 4b). Mode: FE+BE. Kelas binary buffer: isi berkas dipisah dari kegagalan export (TC-GS-GSET-101, spec 026).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC dalam spec: 97, 98, 99, 100, lalu 159 di akhir karena TC-159 melanjutkan state kolom `Modified By` yang disembunyikan TC-100. Nama berkas mengikuti PRD §4.2b dan §7 S-20 (`Changelog-General-Settings`, ekstensi mengikuti format yang dipilih).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (membuka Modal Changelog), langkah 5 (mencatat `N_total`), langkah 9, 22, dan 31 (membaca isi berkas), serta langkah 27 (menutup Search dan mereset tabel sebelum TC-159). Langkah 6 memakai overlay Download yang masih terbuka dari TC-97 (langkah 1 TC-98 "Klik Download" dipenuhi langkah 2). Langkah 19 dan 28 adalah Save Setup Column (aksi sisi klien tanpa request tulis ke server, tanpa "Tunggu aksi selesai"). Langkah 1 TC-159 ("hilangkan centang `Modified By`, Save") dipenuhi state kolom hidden dari langkah 19 TC-100, sehingga hanya langkah centang kembali (langkah 28) yang ditulis; langkah 28 sekaligus memulihkan visibilitas kolom.
- Asersi absence atas state sementara (toast sukses, langkah 7 dan 16) diletakkan segera sesudah klik pilihan format dan sebelum asersi berkas; klik pilihan format menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas terunduh (langkah 8 dan 17). Urutan Expected a (nama berkas) dan b (tanpa toast) TC-98 dan TC-99 dibalik karena butir 11 bagian 8b konvensi.
- Asersi absence kolom `Modified By` pada berkas (langkah 26) didahului `Verifikasi` berkas memuat sedikitnya satu baris data (langkah 23) dan kolom pembanding pada berkas yang sama (langkah 25). Asersi universal "setiap baris data bernilai Field `Session Idle Timeout`" (langkah 24) didahului langkah 23 dan memakai seeding yang memuat baris Field lain (`Time Format`, `Date Format`), sehingga berkas yang tidak tersaring akan gagal. Langkah 12 dan 13 (universal "setiap baris") didahului langkah 10 dan 11 (berkas memuat lebih dari 10 baris).
- Langkah 5 dan 10 (konkretisasi, S-03): TC-98 butir c ("seluruh baris riwayat") dikonkretkan sebagai jumlah baris berkas sama dengan total entri yang dibaca sebelum unduhan (bagian 8b butir 10: N berasal dari kemampuan baca total, bukan dari tabel satu halaman). Langkah 12 dan 13 memecah Expected d TC-98 (Date Format dan Time Format) menjadi dua `Verifikasi` (S-01).
- Pembagian TC lintas spec: TC-GS-GSET-101 (Download gagal) di spec 026; TC-GS-GSET-84, 87, 89, 94 di spec 034, TC-GS-GSET-92 dan 95 di spec 054, dan TC-GS-GSET-88, 90, 91, 93 di spec 035 (Setup Column); TC-GS-GSET-103 (format Date di Changelog) di spec 040.
- Temuan untuk QA:
  - TC-GS-GSET-98: Date Format `dd/MM/yy` dan Time Format `HH:mm` tersimpan adalah nilai default baseline, sehingga asersi butir d tidak membedakan format yang diikuti dari format default; TC tidak menyebut pengaturan format non-default sebelum Download. Format non-default diuji pada tampilan tabel di spec 040 (TC-GS-GSET-103), bukan pada berkas.
  - TC-GS-GSET-98 butir c, TC-GS-GSET-99, TC-GS-GSET-100, TC-GS-GSET-159: TC tidak menyebut cara menangkap berkas unduhan, membaca isinya, dan membaca total entri Changelog; kemampuan tersebut disediakan tim FE/BE (Prerequisites). TC-GS-GSET-99 tidak mengharapkan asersi isi berkas XLSX; spec hanya mengasersi nama berkas dan tanpa toast.
  - TC-GS-GSET-159: precondition d mengulang precondition c ("berisi baris riwayat"); tidak memengaruhi langkah. Nilai kolom `Modified By` pada berkas (nama singkat atau nama lengkap) tidak disebut TC maupun PRD modul; spec hanya mengasersi keberadaan kolom (header) di berkas.
