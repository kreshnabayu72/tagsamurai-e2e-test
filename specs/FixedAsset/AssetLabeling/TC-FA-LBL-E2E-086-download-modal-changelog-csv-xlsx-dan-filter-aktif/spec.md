---
id: TC-FA-LBL-E2E-086-download-modal-changelog-csv-xlsx-dan-filter-aktif
title: "Download Modal Changelog: CSV, XLSX, dan Filter Aktif"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-319
  - TC-FA-LBL-320
  - TC-FA-LBL-321
coverage:
  web: automated
---

# Download Modal Changelog: CSV, XLSX, dan Filter Aktif

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Changelog (Pre-setup #17; pengguna Sarah Johnson), email dari `Fixture.assetLabeling.akun.totalControlChangelog` (pola `totalControl_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_CHANGELOG_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`). Email lengkap Company Changelog tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Hook suite (`before`, `beforeEach`, `after` pada `suite.md`) berlaku, termasuk flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan state global. Fixture `fixtures/asset-labeling.json` (identitas akun dan nilai seed, tanpa rahasia) belum ada dan disediakan tim FE. Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.totalControlChangelog` (belum ada; disediakan tim FE, S-12).
- Data Pre-setup #17 (Company Changelog, hanya dibaca): log Changelog Labels memuat tujuh baris seed (Date 08 sampai 15 Sep 2026): Create `High Priority` (15 Sep 2026 14:20, Sarah J), Edit `High Priority` Color `#DC2626` ke `#EF4444` (15 Sep 2026 14:25, Sarah J), Create `Finance Department` (14 Sep 2026 11:15, David K), Edit `Finance Department` Label Name `Finance Dept` ke `Finance Department` (14 Sep 2026 11:30, David K), Create `Audit Ready` (12 Sep 2026 09:40, Sarah J), Create `Executive Asset` (10 Sep 2026 16:30, Michael W), Delete `Old Tag` (08 Sep 2026 13:00, David K).. Entri TC lain (mis. Delete bertanggal hari run dari TC-FA-LBL-325) menambah entri permanen bertanggal hari run sehingga ketujuh baris seed dapat bergeser ke luar halaman pertama (pagination default 10 per halaman). Karena itu spec menerapkan Filter Date `08 Sep 2026` sampai `15 Sep 2026` (rentang inklusif) di Filter Panel Modal Changelog sebelum unduh TC-FA-LBL-319, dan hasil unduh dinilai atas hasil filter itu: tepat tujuh baris seed (entri TC lain berada di luar rentang) (S-12).
- Data Pre-setup #17 dibaca sebagai bagian baris yang diunduh. Jumlah entri N dalam rentang Filter Date `08 Sep 2026` sampai `15 Sep 2026` dibaca sebelum Modal Changelog dibuka lewat kemampuan baca yang disediakan tim FE/BE (N tidak diturunkan dari seeding karena Changelog adalah audit trail permanen dan spec lain menambah entri bertanggal hari run; bagian 8b butir 10).
- Kemampuan teknis: pembaca berkas CSV dan XLSX hasil unduhan (nama berkas, kolom header, jumlah baris, nama sheet); pemantauan tidak ada toast saat unduh.
- State global yang diubah: konfigurasi kolom Setup Column Modal Changelog pada TC-FA-LBL-321 (kolom `Field` disembunyikan lewat `[Save]`). Dipulihkan oleh hook `after` suite (hapus preferensi kolom di browser; kemampuan disediakan tim FE). Spec tidak membuat atau mengubah data backend.

## Test Steps

### Membuka Modal Changelog

1. Baca jumlah entri N Changelog Labels dengan Date `08 Sep 2026` sampai `15 Sep 2026` lewat pembacaan BE
2. Klik icon Changelog di Table Tools

### TC-FA-LBL-319: Download Changelog CSV memakai nama Changelog-Labels

3. Klik icon Filter di toolbar modal
4. Pilih rentang `08 Sep 2026` sampai `15 Sep 2026` lalu klik `[Apply]`
5. Klik icon Download di toolbar modal
6. Klik `Download as CSV`
7. Verifikasi tidak ada toast sukses
8. Verifikasi berkas terunduh bernama `Changelog-Labels.csv`
9. Verifikasi berkas memuat N baris data hasil Filter Date, tepat tujuh baris seed
10. Tutup Modal Changelog dengan `[✕]`
11. Klik icon Changelog di Table Tools

### TC-FA-LBL-320: Download Changelog XLSX memakai nama Changelog-Labels

12. Klik icon Download di toolbar modal
13. Klik `Download as XLSX`
14. Verifikasi tidak ada toast sukses
15. Verifikasi berkas terunduh bernama `Changelog-Labels.xlsx`
16. Verifikasi berkas memiliki satu sheet `Sheet1`

### TC-FA-LBL-321: Download Changelog mengikuti Search, Filter, dan kolom visible

17. Ketik Search `Finance`, tekan Enter
18. Klik header kolom Actions (⋯) modal lalu klik `Setup Column...`, sembunyikan kolom `Field`, lalu klik `[Save]`
19. Klik icon Download di toolbar modal
20. Klik `Download as CSV`
21. Verifikasi berkas terunduh bernama `Changelog-Labels.csv`
22. Verifikasi berkas hanya memuat dua baris `Finance Department`
23. Verifikasi berkas tidak memuat kolom `Field`
24. Verifikasi nilai kosong pada Old Value baris `Create Finance Department` ditulis `-`
25. Klik header kolom Actions (⋯) modal lalu klik `Setup Column...`, klik `[Reset to Default]`, lalu klik `[Save]`
26. Klik `(←)` pada kotak Search
27. Tutup Modal Changelog dengan `[✕]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` (bagian 4b).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Asersi "tidak ada toast sukses" diletakkan segera sesudah pemicu unduh dan sebelum asersi berkas; pemicu menjadi anchor yang buktinya menyusul pada `Verifikasi` berkas terunduh (bagian 8b butir 11).
- Langkah penghubung (tanpa awalan `Verifikasi`): membaca jumlah entri N dalam rentang Filter Date sebelum Modal Changelog dibuka, menutup lalu membuka kembali Modal Changelog sesudah TC-FA-LBL-319 (langkah 10 dan 11) supaya Filter Date rentang seed tidak terbawa ke TC-FA-LBL-320 dan TC-FA-LBL-321 (S-09), `[Reset to Default]` lalu `[Save]` untuk memulihkan kolom `Field`, `(←)` pada kotak Search, dan menutup Modal Changelog di akhir spec.
- Asersi nilai sel tunggal `-` pada TC-FA-LBL-321 ada di spec ini karena merupakan bagian Expected TC yang sama; isi berkas lain (tipe sel, BOM, gaya XLSX) tidak diasersi di sini.
- Temuan untuk QA:
  - TC-FA-LBL-321 menyatakan nilai kosong ditulis `-` di berkas, sedangkan UI menampilkan `—`; perbedaan simbol ini sesuai TC dan tidak diubah.
  - TC-FA-LBL-321 tidak menyatakan apakah `[Save]` pada Setup Column menutup popup; asersi kolom dibaca dari berkas unduhan, bukan dari tabel.
  - Email akun Total Control Company Changelog tidak tertulis lengkap di Pre-setup #17 (hanya pola dengan `{namaCompany}`); akun disediakan tim FE.
