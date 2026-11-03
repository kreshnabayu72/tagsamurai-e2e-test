---
id: TC-AC-DC-E2E-078-changelog-isi-berkas-export
title: "Modal Changelog Category: Isi Berkas Export Format Tanggal, Penanda Kosong, dan Kutip Ganda CSV"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-213
  - TC-AC-DC-284
coverage:
  web: automated
---

# Modal Changelog Category: Isi Berkas Export Format Tanggal, Penanda Kosong, dan Kutip Ganda CSV

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Principal `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1, nama tampil `Budi Santoso`, Modified By `Budi S`; password `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca): Pohon Uji Kategori (No 14), Riwayat Changelog Uji (No 17: dua belas entri, Field `Category`, pelaku `Budi S` dan `Maya P`), dan General Settings entitas uji (No 19: Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Nilai persis dibaca dari tabel Pre-setup TC dan tidak ditulis ulang di luar langkah.
- Pemulihan Changelog: kemampuan fixture BE (disediakan tim FE/BE; TC, PRD, dan LLD tidak mendefinisikan mekanismenya) memulihkan Riwayat Changelog entitas uji ke Pre-setup No 17 di hook `before` dan `after`. Jumlah total entri (12) dan pembagian halaman pada asersi bersumber dari No 17.
- Sesi API aktor dan fixture BE pemulihan pohon Category: lihat `suite.md`.
- Data Dinamis (bersuffix `{runId}-078`): node `Pemindai, Kecil {runId}-078` dibuat spec lewat UI di bawah `Rugged Scanner` (node Pre-setup No 14, hanya sebagai induk); dihapus lewat API di hook `after` bila masih ada.
- Kemampuan teknis (disediakan tim FE): menangkap berkas unduhan browser ke direktori bersih, membaca nama berkas, header, jumlah baris, dan nilai sel CSV/XLSX.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-AC-DC-213: Isi sel export: format tanggal dan penanda kosong

1. Klik ikon Changelog pada header Sidebar Category
2. Klik ikon Download, pilih "Download as XLSX"
3. Verifikasi kolom Date pada berkas memakai Date Format `dd/MM/yy` sesuai General Settings
4. Verifikasi kolom Date pada berkas memakai Time Format 24 jam sesuai General Settings
5. Verifikasi sel Old Value pada entri Create berisi `-`
6. Verifikasi sel New Value pada entri Delete berisi `-`

### TC-AC-DC-284: Download CSV membungkus nilai berisi koma dengan tanda kutip ganda

7. Tutup modal lewat icon `[×]`
8. Expand `Hardware` lalu `Handheld Reader`
9. Hover node `Rugged Scanner` lalu klik aksi `+ Subcategory`
10. Ketik `Pemindai, Kecil {runId}-078` pada input inline Add, klik `[Submit]`
11. Tunggu aksi selesai
12. Klik ikon Changelog pada header Sidebar Category
13. Klik ikon Download, pilih "Download as CSV"
14. Verifikasi berkas `Changelog-Category.csv` terunduh
15. Verifikasi nilai kolom Category pada baris Create `Pemindai, Kecil {runId}-078` ditulis dibungkus tanda kutip ganda
16. Verifikasi nilai kolom New Value pada baris itu ditulis dibungkus tanda kutip ganda
17. Verifikasi setiap baris pada berkas tetap memiliki 7 kolom

## Notes

- Sumber: `admin-console/settings-device-category/TestCases/tc-settings-device-category.md` (TC-AC-DC-213, 284). Tidak ada TC hanya-BE di spec ini.
- Kelas f (binary buffer): spec ini memuat isi berkas export (nilai sel, format tanggal, kutip ganda). Nama berkas, header, dan jumlah baris diasersi di spec 077.
- Node tulis memakai nama bersuffix `Pemindai, Kecil {runId}-078` (spec membuat node sendiri; koma tetap ada karena objek uji TC-AC-DC-284); TC memakai nama literal `Pemindai, Kecil`.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah dari TC): langkah 7 dan langkah 11 (Tunggu aksi selesai sesudah `[Submit]` pada langkah 10 yang hasilnya tidak diasersi, karena langkah berikutnya membuka modal Changelog, 8b butir 8).
- Temuan untuk QA:
  - Asersi spec ini bergantung pada isi persis Riwayat Changelog Pre-setup #17 (dua belas entri, termasuk angka total 12 dan pembagian halaman), sedangkan S-12 melarang angka total absolut pada audit trail permanen dan Lampiran A belum punya butir untuk modul ini. Spec mengikuti TC dan mengandalkan kemampuan fixture BE yang memulihkan Changelog entitas uji ke #17 sebelum dan sesudah spec. Perlu keputusan pengecualian Lampiran A (setara A-5) atau entitas uji khusus Changelog.
  - TC-AC-DC-213 tidak menyebut format nilai sel Date pada XLSX (teks atau tipe tanggal); spec mengasersi tampilan format sesuai General Settings.
  - TC-AC-DC-284 menyebut kutip ganda untuk kolom Category dan New Value tanpa menyebut kutip pada kolom Old Value kosong; spec tidak mengasersi kolom lain.
