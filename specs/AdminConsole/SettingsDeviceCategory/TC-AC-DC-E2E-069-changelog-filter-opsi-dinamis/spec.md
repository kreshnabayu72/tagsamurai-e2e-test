---
id: TC-AC-DC-E2E-069-changelog-filter-opsi-dinamis
title: "Modal Changelog Category: Loading Dropdown Filter dan Opsi Category Bertambah Setelah Add"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-278
  - TC-AC-DC-277
coverage:
  web: automated
---

# Modal Changelog Category: Loading Dropdown Filter dan Opsi Category Bertambah Setelah Add

## Prerequisites

- Mode: FE+BE (backend nyata; respons data opsi dropdown Filter ditahan sebagian lewat intercept sehingga state server tetap nyata).
- Akun aktor: Total Control Principal `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1, nama tampil `Budi Santoso`, Modified By `Budi S`; password `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca): Pohon Uji Kategori (No 14), Riwayat Changelog Uji (No 17: dua belas entri, Field `Category`, pelaku `Budi S` dan `Maya P`), dan General Settings entitas uji (No 19: Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Nilai persis dibaca dari tabel Pre-setup TC dan tidak ditulis ulang di luar langkah.
- Pemulihan Changelog: kemampuan fixture BE (disediakan tim FE/BE; TC, PRD, dan LLD tidak mendefinisikan mekanismenya) memulihkan Riwayat Changelog entitas uji ke Pre-setup No 17 di hook `before` dan `after`. Jumlah total entri (12) dan pembagian halaman pada asersi bersumber dari No 17.
- Sesi API aktor dan fixture BE pemulihan pohon Category: lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE): intercept yang menahan respons HTTP data opsi dropdown Filter Changelog selama 3 detik (nilai data uji TC-AC-DC-278), lalu melepas tahanan; intercept dilepas segera setelah asersi (S-09).
- Data Dinamis (bersuffix `{runId}-069`): node `Pemindai Opsi {runId}-069` dibuat spec lewat UI di bawah `Rugged Scanner` (node Pre-setup No 14, hanya sebagai induk); dihapus lewat API di hook `after` bila masih ada.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-AC-DC-278: Dropdown Filter menampilkan indikator loading saat opsi sedang dimuat

1. Pasang intercept yang menahan respons data opsi dropdown Filter selama 3 detik
2. Klik ikon Changelog pada header Sidebar Category
3. Klik ikon Filter, buka dropdown Category
4. Verifikasi dropdown Category menampilkan indikator loading (skeleton atau spinner) selama opsi belum diterima, bukan daftar kosong
5. Lepas intercept data opsi dropdown Filter
6. Verifikasi dropdown Category menampilkan 9 opsi setelah respons diterima

### TC-AC-DC-277: Opsi dropdown Filter Category bertambah saat entri baru tercatat tanpa reload

7. Tutup modal lewat icon `[×]`
8. Expand `Hardware` lalu `Handheld Reader`
9. Klik ikon Changelog pada header Sidebar Category
10. Klik ikon Filter, buka dropdown Category
11. Verifikasi dropdown Category berisi 9 opsi
12. Tutup modal lewat icon `[×]`
13. Hover node `Rugged Scanner` lalu klik aksi `+ Subcategory`
14. Ketik `Pemindai Opsi {runId}-069` pada input inline Add, klik `[Submit]`
15. Tunggu aksi selesai
16. Klik ikon Changelog pada header Sidebar Category
17. Klik ikon Filter, buka dropdown Category
18. Verifikasi dropdown Category berisi 10 opsi termasuk `Pemindai Opsi {runId}-069`

## Notes

- Sumber: `admin-console/settings-device-category/TestCases/tc-settings-device-category.md` (TC-AC-DC-277, 278). Tidak ada TC hanya-BE di spec ini.
- Urutan TC di spec: 278 lalu 277 (aksi tulis di akhir); 278 mengasersi 9 opsi sehingga harus mendahului Add pada 277 (S-10, S-14).
- Node tulis memakai nama bersuffix `Pemindai Opsi {runId}-069` (spec membuat node sendiri); TC memakai nama literal `Pemindai Opsi`. Induk `Rugged Scanner` adalah node Pre-setup No 14 yang hanya diberi anak.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah dari TC): langkah 1, 5, 7, 12, dan langkah 15 (Tunggu aksi selesai sesudah `[Submit]` pada langkah 14 yang hasilnya tidak diasersi, karena langkah berikutnya membuka modal Changelog, 8b butir 8).
- Temuan untuk QA:
  - Asersi spec ini bergantung pada isi persis Riwayat Changelog Pre-setup #17 (dua belas entri, termasuk angka total 12 dan pembagian halaman), sedangkan S-12 melarang angka total absolut pada audit trail permanen dan Lampiran A belum punya butir untuk modul ini. Spec mengikuti TC dan mengandalkan kemampuan fixture BE yang memulihkan Changelog entitas uji ke #17 sebelum dan sesudah spec. Perlu keputusan pengecualian Lampiran A (setara A-5) atau entitas uji khusus Changelog.
  - Menyiapkan induk milik spec lewat API di hook `before` akan menambah opsi Category sebelum asersi 9 opsi; karena itu induk memakai node Pre-setup `Rugged Scanner` dan hanya anaknya yang bernama bersuffix.
  - Penundaan 3 detik pada TC-AC-DC-278 adalah nilai data uji TC (bukan aturan PRD); spec memakainya sebagai pilihan spec.
