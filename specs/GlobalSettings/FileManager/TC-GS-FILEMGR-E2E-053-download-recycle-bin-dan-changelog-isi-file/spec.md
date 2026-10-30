---
id: TC-GS-FILEMGR-E2E-053-download-recycle-bin-dan-changelog-isi-file
title: "Download Recycle Bin dan Changelog: Isi File Mengikuti Search, Filter, dan Visibilitas Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-172
  - TC-GS-FILEMGR-220
  - TC-GS-FILEMGR-221
coverage:
  web: automated
---

# Download Recycle Bin dan Changelog: Isi File Mengikuti Search, Filter, dan Visibilitas Kolom

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Sinta Maharani (Tabel A1 TC) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before`; ini akun default suite sehingga hook `after` tidak mengganti sesi.
- Data Pre-setup: Tabel A3 (16 baris Recycle Bin, retensi 30 hari, Deleted Date relatif terhadap waktu uji) dan Tabel A4 (14 entri Changelog). Dataset disiapkan lewat fixture BE di hook `before` (kemampuan "disediakan tim FE/BE"; mekanisme dan endpoint seeding tidak didefinisikan di TC, lihat Temuan untuk QA). Nama file dan entri literal sesuai tabel karena isi file export bergantung pada Search `recycled`, Filter Modified By `System`, dan kolom tersembunyi (pengecualian setara S-12: seeding idempotent, suite serial). Spec hanya membaca data; tidak ada aksi tulis ke data dan tidak ada data dinamis.
- Suite serial (`parallel: false`): hitungan baris file export hanya valid bila tidak ada spec lain yang menambah atau menghapus file Recycle Bin atau entri Changelog bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan di `after` (dinyatakan di `suite.md`).
- Hook `beforeEach`: buka Global Settings > File Manager.
- State global yang dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): konfigurasi kolom Recycle Bin dikembalikan ke default (semua kolom tampil) dan berkas unduhan dihapus.
- Kemampuan teknis (kelas binary buffer, prinsip 13f): menangkap berkas unduhan browser (event download) ke direktori bersih per unduhan supaya nama berkas yang sama tidak tertimpa atau diberi akhiran `(1)`; membaca isi berkas CSV (header, jumlah baris).

## Test Steps

1. Klik tombol Recycle Bin di toolbar

### TC-GS-FILEMGR-220: Download Recycle Bin saat Search aktif hanya mengekspor baris yang cocok

2. Ketik Search `recycled`, tekan Enter
3. Klik ikon Download, lalu klik `Download as CSV`
4. Verifikasi tidak ada toast sukses
5. Verifikasi file CSV memuat 12 baris data (`recycled-photo-01.jpg` s.d. `recycled-photo-12.jpg`)
6. Klik ikon panah (←) pada kotak Search

### TC-GS-FILEMGR-221: Download Recycle Bin tidak memuat kolom yang disembunyikan

7. Sembunyikan kolom `Auto-Purge In` lewat overlay Column Visibility (⋯)
8. Klik ikon Download, lalu klik `Download as CSV`
9. Verifikasi header file CSV pertama tidak memuat `Auto-Purge In`
10. Tampilkan kembali kolom `Auto-Purge In` lewat overlay Column Visibility (⋯)
11. Klik ikon Download, lalu klik `Download as CSV`
12. Verifikasi header file CSV kedua memuat `Auto-Purge In`
13. Tutup modal Recycle Bin

### TC-GS-FILEMGR-172: Download modal Changelog saat Filter aktif hanya mengekspor entri yang cocok

14. Klik ikon Changelog di toolbar
15. Klik ikon Filter di toolbar modal
16. Pilih `System` pada Modified By, klik `[Apply]`
17. Klik ikon Download, lalu klik `Download as CSV`
18. Verifikasi tidak ada toast sukses
19. Verifikasi file CSV memuat 5 baris data

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC dalam spec: 220, 221, 172. Dua TC Recycle Bin dalam satu pembukaan modal, lalu Changelog (surface kedua) di akhir; tidak ada TC yang menghabisi data.
- Absence toast (langkah 4 dan 18) diletakkan segera setelah pemicu unduhan dan sebelum asersi berkas; pemicu unduhan menjadi anchor positif yang buktinya menyusul pada `Verifikasi` isi berkas (butir 11 dan butir 2 bagian 8b).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 6 (mengosongkan Search), langkah 10 (menampilkan kembali kolom), langkah 13 (menutup modal Recycle Bin).
- Pembagian lintas spec: isi file export tabel utama dan ekstensi, encoding, serta nama file ada di spec `TC-GS-FILEMGR-E2E-052-download-tabel-utama-isi-file-csv-xlsx`; kegagalan download Recycle Bin dan Changelog ada di spec `TC-GS-FILEMGR-E2E-016-resilience-download-gagal`.
- Temuan untuk QA:
  - Mekanisme dan endpoint seeding Tabel A3 dan A4 tidak didefinisikan di TC (Q-4); hitungan baris mengasumsikan dataset di-seed ulang per spec dan suite serial (Q-7).
  - TC-GS-FILEMGR-172 memakai "Filter Modified By `System`" tanpa langkah Filter Panel; spec menuliskan langkah membuka Filter dan memilih nilai (langkah 15 dan 16) sebagai penjabaran, dengan asumsi Filter Panel tertutup saat modal dibuka.
