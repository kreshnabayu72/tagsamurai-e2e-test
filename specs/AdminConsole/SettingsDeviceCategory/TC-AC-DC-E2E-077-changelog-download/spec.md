---
id: TC-AC-DC-E2E-077-changelog-download
title: "Modal Changelog Category: Download CSV dan XLSX, Nama Berkas, dan Mengikuti Search, Filter, dan Kolom"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-209
  - TC-AC-DC-210
  - TC-AC-DC-211
  - TC-AC-DC-212
  - TC-AC-DC-214
coverage:
  web: automated
---

# Modal Changelog Category: Download CSV dan XLSX, Nama Berkas, dan Mengikuti Search, Filter, dan Kolom

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Principal `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1, nama tampil `Budi Santoso`, Modified By `Budi S`; password `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca): Pohon Uji Kategori (No 14), Riwayat Changelog Uji (No 17: dua belas entri, Field `Category`, pelaku `Budi S` dan `Maya P`), dan General Settings entitas uji (No 19: Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Nilai persis dibaca dari tabel Pre-setup TC dan tidak ditulis ulang di luar langkah.
- Pemulihan Changelog: kemampuan fixture BE (disediakan tim FE/BE; TC, PRD, dan LLD tidak mendefinisikan mekanismenya) memulihkan Riwayat Changelog entitas uji ke Pre-setup No 17 di hook `before` dan `after`. Jumlah total entri (12) dan pembagian halaman pada asersi bersumber dari No 17.
- Sesi API aktor dan fixture BE pemulihan pohon Category: lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE): menangkap berkas unduhan browser ke direktori bersih, membaca nama berkas, header, jumlah baris, dan nilai sel CSV/XLSX.
- State global yang diubah dan dipulihkan: preferensi kolom modal Changelog di browser aktor; hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE, bukan `[Reset to Default]`) dan Changelog dipulihkan ke No 17.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-AC-DC-209: Klik Download membuka pilihan format CSV dan XLSX

1. Klik ikon Changelog pada header Sidebar Category
2. Klik ikon Download
3. Verifikasi overlay menampilkan opsi "Download as CSV"
4. Verifikasi overlay menampilkan opsi "Download as XLSX"

### TC-AC-DC-210: Download CSV tanpa Search atau Filter mengekspor seluruh baris dengan nama file Changelog-Category

5. Pilih "Download as CSV"
6. Verifikasi tidak ada toast sukses
7. Verifikasi berkas `Changelog-Category.csv` terunduh
8. Verifikasi berkas memuat seluruh 12 baris data (bukan hanya 10 baris halaman 1)
9. Verifikasi berkas memuat 7 kolom data yang sedang tampil
10. Verifikasi sel kosong (Old Value pada Create, New Value pada Delete) berisi `-` (hyphen tunggal)

### TC-AC-DC-211: Download XLSX mengikuti Search dan Filter yang aktif

11. Ketik Search `kit`, tekan Enter
12. Klik ikon Filter, buka dropdown Action, centang "Create", klik `[Apply]`
13. Klik ikon Download, pilih "Download as XLSX"
14. Verifikasi tidak ada toast sukses
15. Verifikasi berkas `Changelog-Category.xlsx` terunduh
16. Verifikasi berkas memuat satu sheet bernama `Sheet1`
17. Verifikasi berkas hanya memuat 3 baris yang cocok (`Gateway Kit`, `Kit Lama`, `Kit Lama Anak`), bukan seluruh dataset

### TC-AC-DC-212: Download mengikuti kolom yang sedang tampil: kolom tersembunyi tidak diekspor dan kembali setelah unhide

18. Tutup modal lewat icon `[×]`, lalu klik ikon Changelog pada header Sidebar Category
19. Sembunyikan kolom Field lewat Column Visibility
20. Klik ikon Download, pilih "Download as CSV"
21. Verifikasi tidak ada peringatan tambahan pada layar
22. Verifikasi berkas CSV pertama tidak memuat kolom Field
23. Tampilkan kembali kolom Field lewat Column Visibility
24. Klik ikon Download, pilih "Download as CSV"
25. Verifikasi berkas CSV kedua memuat kembali kolom Field

### TC-AC-DC-214: Download saat hasil nol baris tetap aktif dan menghasilkan file hanya berisi header

26. Ketik Search `zzzz`, tekan Enter
27. Verifikasi tombol Download tetap aktif
28. Klik ikon Download, pilih "Download as CSV"
29. Verifikasi tidak ada toast
30. Verifikasi berkas CSV hanya berisi baris header kolom yang tampil (tanpa baris data)

## Notes

- Sumber: `admin-console/settings-device-category/TestCases/tc-settings-device-category.md` (TC-AC-DC-209, 210, 211, 212, 214). Tidak ada TC hanya-BE di spec ini.
- Pembagian TC lintas spec: TC-AC-DC-213 dan 284 (isi sel export dan kutip ganda) ada di spec 078 (kelas f).
- Kelas f: nama berkas, header, dan jumlah baris diasersi di spec ini sebagai asersi fungsional. TC-AC-DC-210 butir d (nilai sel kosong `-`) adalah isi sel dan tetap berada di sini karena TC-AC-DC-210 satu spec dengan sisa butirnya.
- Absence toast (TC-AC-DC-210 c, 211 c, 212 a, 214 b) diletakkan segera setelah pemicu klik pilihan format dan sebelum Verifikasi berkas terunduh; pemicu menjadi anchor positif yang buktinya menyusul pada berkas terunduh (8b.11).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah dari TC): langkah 18.
- Temuan untuk QA:
  - Asersi spec ini bergantung pada isi persis Riwayat Changelog Pre-setup #17 (dua belas entri, termasuk angka total 12 dan pembagian halaman), sedangkan S-12 melarang angka total absolut pada audit trail permanen dan Lampiran A belum punya butir untuk modul ini. Spec mengikuti TC dan mengandalkan kemampuan fixture BE yang memulihkan Changelog entitas uji ke #17 sebelum dan sesudah spec. Perlu keputusan pengecualian Lampiran A (setara A-5) atau entitas uji khusus Changelog.
  - TC-AC-DC-210 butir d memeriksa nilai sel (`-`) yang termasuk isi berkas (kelas f); duplikat dengan TC-AC-DC-213 butir b. Perlu keputusan QA apakah butir d dipindah ke spec 078.
  - TC-AC-DC-212 butir a 'tanpa peringatan tambahan' tidak menyebut bentuk peringatan; spec mengasersi tidak ada peringatan pada layar.
  - Kolom Field yang disembunyikan di TC-AC-DC-212 dikembalikan tampil pada langkah 23; preferensi kolom tetap dihapus di hook `after` bila masih ada.
