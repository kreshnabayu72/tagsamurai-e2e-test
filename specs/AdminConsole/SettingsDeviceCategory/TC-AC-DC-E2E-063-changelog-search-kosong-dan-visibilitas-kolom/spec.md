---
id: TC-AC-DC-E2E-063-changelog-search-kosong-dan-visibilitas-kolom
title: "Modal Changelog Category: Search Tanpa Hasil dan Keterikatan Visibilitas Kolom"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DC-163
  - TC-AC-DC-164
  - TC-AC-DC-165
coverage:
  web: automated
---

# Modal Changelog Category: Search Tanpa Hasil dan Keterikatan Visibilitas Kolom

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Principal `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1, nama tampil `Budi Santoso`, Modified By `Budi S`; password `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca): Pohon Uji Kategori (No 14), Riwayat Changelog Uji (No 17: dua belas entri, Field `Category`, pelaku `Budi S` dan `Maya P`), dan General Settings entitas uji (No 19: Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Nilai persis dibaca dari tabel Pre-setup TC dan tidak ditulis ulang di luar langkah.
- Pemulihan Changelog: kemampuan fixture BE (disediakan tim FE/BE; TC, PRD, dan LLD tidak mendefinisikan mekanismenya) memulihkan Riwayat Changelog entitas uji ke Pre-setup No 17 di hook `before` dan `after`. Jumlah total entri (12) dan pembagian halaman pada asersi bersumber dari No 17.
- Sesi API aktor dan fixture BE pemulihan pohon Category: lihat `suite.md`.
- State global yang diubah dan dipulihkan: preferensi kolom modal Changelog di browser aktor; hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE, bukan `[Reset to Default]`) dan Changelog dipulihkan ke No 17.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-AC-DC-163: Search tanpa hasil menampilkan empty state tidak ada hasil

1. Klik ikon Changelog pada header Sidebar Category
2. Ketik Search `zzzz`, tekan Enter
3. Verifikasi empty state menampilkan ilustrasi
4. Verifikasi empty state menampilkan judul "No results found"
5. Verifikasi empty state menampilkan deskripsi "Try adjusting your search or filter."

### TC-AC-DC-164: Search terikat visibilitas kolom: kolom yang di-hide tidak dicari

6. Klik icon panah `(←)` di kiri toolbar untuk mereset pencarian
7. Klik ikon `⋯` pada header kolom Actions, uncheck kolom Modified By
8. Ketik Search `scan`, tekan Enter
9. Verifikasi tabel menampilkan 3 baris yang cocok dengan "scan" (kolom lain yang tampil tetap dapat dicari)
10. Ganti isi kotak search dengan `maya`, tekan Enter
11. Verifikasi tidak ada baris yang cocok karena kolom Modified By yang di-hide tidak ikut dicari

### TC-AC-DC-165: Search kembali mencakup kolom setelah di-unhide

12. Klik icon panah `(←)` di kiri toolbar untuk mereset pencarian
13. Klik ikon `⋯` pada header kolom Actions, check kembali kolom Modified By
14. Ketik Search `maya`, tekan Enter
15. Verifikasi tabel menampilkan 6 baris yang dilakukan Maya P karena kolom Modified By kembali masuk cakupan Search

## Notes

- Sumber: `admin-console/settings-device-category/TestCases/tc-settings-device-category.md` (TC-AC-DC-163, 164, 165). Tidak ada TC hanya-BE di spec ini.
- Langkah Search `scan` pada TC-AC-DC-164 menjadi anchor positif absence (8b.2): baris hasil tampil sebelum Search `maya` diasersi kosong.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah dari TC): langkah 6, 8, 12.
- Temuan untuk QA:
  - Asersi spec ini bergantung pada isi persis Riwayat Changelog Pre-setup #17 (dua belas entri, termasuk angka total 12 dan pembagian halaman), sedangkan S-12 melarang angka total absolut pada audit trail permanen dan Lampiran A belum punya butir untuk modul ini. Spec mengikuti TC dan mengandalkan kemampuan fixture BE yang memulihkan Changelog entitas uji ke #17 sebelum dan sesudah spec. Perlu keputusan pengecualian Lampiran A (setara A-5) atau entitas uji khusus Changelog.
  - TC-AC-DC-164 menyebut 'kolom lain yang tampil tetap bisa dicari' dalam kurung; spec mengasersinya lewat Search `scan` (data No 17).
  - TC tidak menyebut apakah perubahan Column Visibility tersimpan di browser; spec memulihkan preferensi kolom di hook `after`.
