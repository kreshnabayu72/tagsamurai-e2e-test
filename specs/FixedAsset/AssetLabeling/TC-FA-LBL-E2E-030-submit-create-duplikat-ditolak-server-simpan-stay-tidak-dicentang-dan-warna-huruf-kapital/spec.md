---
id: TC-FA-LBL-E2E-030-submit-create-duplikat-ditolak-server-simpan-stay-tidak-dicentang-dan-warna-huruf-kapital
title: "Submit Create: Duplikat Ditolak Server, Simpan dengan Stay Tidak Dicentang, dan Warna Huruf Kapital"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-87
  - TC-FA-LBL-84
  - TC-FA-LBL-85
coverage:
  web: automated
---

# Submit Create: Duplikat Ditolak Server, Simpan dengan Stay Tidak Dicentang, dan Warna Huruf Kapital

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson), `Fixture.assetLabeling.akun.totalControl`, `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec. Fixture `fixtures/asset-labeling.json` (`Fixture.assetLabeling.*`) memuat identitas akun tanpa rahasia; fixture ini belum ada dan disediakan tim FE.
- Env var `FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak mengubah state global kecuali dinyatakan di bawah.
- Suffix nama bersuffix spec ini: `{runId}-030` (`{runId}` hanya digit).
- Data Pre-setup #12: label `High Priority` sudah ada di katalog Company Alpha; hanya dibaca untuk TC-FA-LBL-87.
- Palet Preset (Pre-setup #33): swatch baris 1 kolom 2 bernilai `#F97316`.
- Label yang dibuat: `Support Team {runId}-030`, `Preset Color 85 {runId}-030`, dan `Hex Color 85 {runId}-030`.
- Intercept (`Spectra.intercept()`): menahan respons pengecekan keunikan nama (TC-FA-LBL-87) supaya `[Submit]` diklik sebelum cek selesai; dilepas segera sesudah pemicu selesai.
- Label yang dibuat spec ini (nama bersuffix `{runId}-030`) dihapus di hook `after` lewat sesi API aktor.
- Kemampuan teknis (disediakan tim FE/BE, suite.md): sesi API aktor dan fixture BE untuk membaca state katalog (jumlah label bernama `High Priority`) dan menghapus label.
- Jeda nyata: langkah 13 menunggu 5 detik sungguhan (toast hilang otomatis setelah 4 detik, TC-FA-LBL-84); tidak memakai jam palsu.
- Last Updated pada langkah 22 dibandingkan dengan waktu simpan yang dicatat sesudah `[Submit]` (langkah 16) dengan toleransi satu menit; jam server dan jam browser sinkron (S-12). Modified By berformat `[First Name] [Last Initial]` untuk Sarah Johnson: `Sarah J`.

## Test Steps

### TC-FA-LBL-87: Submit dengan nama duplikat ditolak server dengan inline error

1. Klik `[+ Label]`
2. Tahan respons pengecekan keunikan nama (intercept jaringan)
3. Ketik `High Priority` di Label Name
4. Klik `[Submit]` sebelum 500 ms berlalu
5. Verifikasi inline error `Label name already exists` tampil di bawah Label Name
6. Verifikasi modal tetap terbuka dengan input dipertahankan
7. Verifikasi tidak ada toast
8. Verifikasi tepat satu label `High Priority` di katalog (lewat fixture BE), tidak ada label ganda
9. Lepas tahanan respons pengecekan keunikan

### TC-FA-LBL-84: Submit Create dengan Stay tidak dicentang menyimpan label dan menutup modal

10. Ganti isi Label Name dengan `Support Team {runId}-030`
11. Klik `[Submit]`
12. Verifikasi toast `Success, label has been created.` tampil
13. Tunggu 5 detik tanpa menutup toast
14. Verifikasi toast hilang otomatis setelah 4 detik
15. Verifikasi modal tertutup
16. Catat waktu simpan
17. Ketik Search `Support Team {runId}-030`, tekan Enter
18. Verifikasi baris chip `Support Team {runId}-030` berlatar `#3B82F6` tampil di tabel yang di-refresh
19. Verifikasi Color Hex baris `Support Team {runId}-030` adalah `#3B82F6`
20. Verifikasi Total Asset baris `Support Team {runId}-030` adalah `0`
21. Verifikasi Modified By baris `Support Team {runId}-030` adalah nama aktor `Sarah J`
22. Verifikasi Last Updated baris `Support Team {runId}-030` sesuai waktu simpan (toleransi satu menit)
23. Verifikasi baris `Support Team {runId}-030` tidak memiliki kolom kosong
24. Klik chip `Support Team {runId}-030` untuk membuka Drawer Tagged Asset
25. Verifikasi Drawer menampilkan state kosong `No assets tagged`
26. Tutup Drawer
27. Klik `(←)` pada kotak Search

### TC-FA-LBL-85: Submit Create dengan warna dari preset dan dari kode hex disimpan dalam huruf kapital

28. Klik `[+ Label]`
29. Ketik `Preset Color 85 {runId}-030` di Label Name
30. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
31. Klik swatch baris 1 kolom 2 lalu catat kode di kolom Hex
32. Klik `[Submit]`
33. Verifikasi toast `Success, label has been created.` untuk label `Preset Color 85 {runId}-030`
34. Klik `[+ Label]`
35. Ketik `Hex Color 85 {runId}-030` di Label Name
36. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
37. Kosongkan kolom Hex lalu ketik `#1e3a8a`
38. Klik `[Submit]`
39. Verifikasi toast `Success, label has been created.` untuk label `Hex Color 85 {runId}-030`
40. Ketik Search `Color 85 {runId}-030`, tekan Enter
41. Verifikasi kolom Color Hex `Preset Color 85 {runId}-030` menampilkan kode swatch yang dicatat (`#F97316`)
42. Verifikasi kolom Color Hex `Hex Color 85 {runId}-030` menampilkan `#1E3A8A` huruf kapital
43. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC di spec: 87, 84, 85. TC-FA-LBL-87 (submit ditolak) lebih dulu dan modalnya dipakai TC-FA-LBL-84 (Label Name diganti), sehingga jumlah buka form tidak melebihi jumlah kejadian menutup (S-10).
- Langkah penghubung (tanpa awalan Verifikasi, S-03): langkah 9 (melepas intercept setelah pemicu selesai, S-09), langkah 16 (mencatat waktu simpan untuk Last Updated), langkah 17 dan 40 (Search untuk menemukan baris target, R-16), langkah 26 (menutup Drawer, S-09), serta langkah 27 dan 43 (mengosongkan Search).
- Urutan TC-FA-LBL-84 (bagian 8b butir 5, S-14): `[Submit]` -> Verifikasi toast tampil (langkah 12) -> Tunggu 5 detik (langkah 13) -> Verifikasi toast hilang otomatis (langkah 14) -> Verifikasi modal tertutup (langkah 15); jeda tidak mendahului asersi toast tampil. Langkah 13 mengikuti Langkah TC "Tunggu 5 detik tanpa menutup toast".
- Ukuran spec (43 langkah, di atas smell 35 langkah): ketiga TC satu topik (Submit Create) dan berbagi satu modal dari TC-FA-LBL-87 ke TC-FA-LBL-84 (prinsip 6); langkah membengkak karena Expected d TC-FA-LBL-84 (Color Hex, Total Asset, Modified By, Last Updated, tanpa kolom kosong, Drawer) dan tiap klausa Expected menjadi satu `Verifikasi` (S-01); memisahkannya menggandakan pembukaan form dan seeding.
- Temuan untuk QA:
  - TC-FA-LBL-87 langkah 2 menulis "sebelum 500 ms berlalu (atau saat cek keunikan diblok jaringan)" sebagai dua cara; spec memilih cara kedua (menahan respons cek keunikan) supaya deterministik.
  - TC-FA-LBL-84 Post Condition (entri Create tercatat di tiga surface, detail di Section 5) tidak punya langkah observasi di TC dan tidak diasersi di spec ini; Expected a sampai d diasersi.
  - TC-FA-LBL-84 Expected d menyebut Modified By "nama aktor" dan Last Updated "waktu simpan" tanpa menyatakan cara membacanya; spec memakai format `Sarah J` (R-14) dan waktu yang dicatat sesudah `[Submit]` dengan toleransi satu menit (S-12).
  - TC-FA-LBL-85 Post Condition (warna tersimpan `#RRGGBB` kapital) sudah tercakup Expected b; tidak ada langkah observasi tambahan.
