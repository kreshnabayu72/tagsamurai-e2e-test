---
id: TC-AC-DS-E2E-127-changelog-pagination-download-dan-kolom-tampil
title: "Changelog: Pagination, Download Tanpa dan Dengan Filter, Nol Baris, dan Mengikuti Kolom Tampil"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-421
  - TC-AC-DS-422
  - TC-AC-DS-425
  - TC-AC-DS-597
coverage:
  web: automated
---

# Changelog: Pagination, Download Tanpa dan Dengan Filter, Nol Baris, dan Mengikuti Kolom Tampil

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca, tidak diubah): SKU inti dan seed (#29, #30), riwayat Changelog Principal (#33) berupa seed 35 entri bertanggal 01/09/26 sampai 03/10/26 (18 oleh `Jane S`, 17 oleh `Budi K`; total pada modal dapat lebih besar karena entri yang ditulis spec lain, sehingga jumlah entri memakai N yang dicatat pada langkah 3 dari info pagination, bukan angka absolut), General Settings Date Format `dd/MM/yy`, 24 jam, Asia/Jakarta (#35). Nilai dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Data Dinamis: tidak ada. Berkas unduhan disimpan di folder unduhan runner dan tidak dihapus oleh spec.
- Kemampuan teknis (disediakan tim FE/BE): membaca isi berkas CSV dan XLSX yang diunduh (nama berkas, baris header, jumlah baris data); menghapus preferensi kolom Setup Column modal Changelog di browser (hook `before` dan hook `after`), bukan lewat [Reset to Default]; entri buatan spec lain dipulihkan baseline data uji yang disediakan tim FE/BE (audit trail permanen).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

### TC-AC-DS-421: Pagination modal Changelog: default 10, opsi ukuran halaman, dan halaman langsung

1. Klik ikon Changelog
2. Verifikasi modal "Changelog: Device SKU" tampil
3. Catat jumlah entri total pada info pagination modal sebagai N
4. Verifikasi default 10 baris per halaman dan jumlah halaman sama dengan pembulatan ke atas N/10, dengan N total entri pada info pagination
5. Klik selector jumlah data per halaman
6. Verifikasi opsi ukuran halaman `10`, `25`, `50`, dan `100` tanpa opsi "All"
7. Ketik `3` pada input nomor halaman lalu tekan Enter
8. Verifikasi halaman 3 tampil memuat entri ke-21 sampai ke-30
9. Ubah ukuran halaman menjadi 25
10. Verifikasi tampilan kembali ke halaman 1 dengan jumlah halaman sama dengan pembulatan ke atas N/25
11. Ubah ukuran halaman menjadi 10

### TC-AC-DS-422: Download Changelog tanpa dan dengan filter aktif

12. Klik ikon Download pada modal
13. Klik `Download as CSV`
14. Verifikasi tidak ada toast sukses
15. Verifikasi file bernama `Changelog-Device-SKU.csv` berisi N entri (semua halaman) yang dicatat pada langkah 3
16. Klik ikon Filter pada modal
17. Pada field Modified By pilih `Budi K`
18. Klik `[Apply]` pada Filter Panel modal
19. Klik ikon Download lalu `Download as XLSX`
20. Verifikasi file bernama `Changelog-Device-SKU.xlsx` berisi hanya entri Modified By `Budi K` dengan jumlah baris sama dengan total hasil filter pada info pagination

### Pemulihan state antar TC

21. Klik ikon Filter, hapus chip `Budi K` dari field Modified By, klik `[Apply]`

### TC-AC-DS-425: Download Changelog dengan hasil nol baris menghasilkan file berisi header saja

22. Klik ikon Search pada modal, ketik Search `tidak-ada-entri`, tekan Enter
23. Klik ikon Download lalu `Download as CSV`
24. Verifikasi tidak ada toast
25. Verifikasi file terunduh berisi hanya baris header kolom yang tampil

### Pemulihan state antar TC

26. Klik `(←)` pada kotak Search

### TC-AC-DS-597: Download Changelog mengikuti kolom yang tampil

27. Klik header kolom Actions (⋯) pada modal, hilangkan centang `Field` dan `Modified By`
28. Verifikasi kolom `Field` dan `Modified By` hilang dari tabel modal
29. Klik ikon Download pada modal lalu `Download as CSV`
30. Verifikasi tidak ada toast dan tidak ada peringatan tentang kolom yang tidak ikut
31. Verifikasi file pertama `Changelog-Device-SKU.csv` memuat kolom `Date`, `Action`, `SKU`, `Old Value`, dan `New Value` tanpa kolom `Field` dan `Modified By`
32. Centang kembali kolom `Field` dan `Modified By`
33. Klik ikon Download pada modal lalu `Download as CSV`
34. Verifikasi tidak ada toast dan tidak ada peringatan tentang kolom yang tidak ikut
35. Verifikasi file kedua memuat kembali ketujuh kolom `Date`, `Action`, `SKU`, `Field`, `Old Value`, `New Value`, dan `Modified By`

### Pemulihan state akhir

36. Tutup modal Changelog

## Notes

- Spec melewati sekitar 35 langkah (36 langkah nominal, sekitar 38 dengan ekspansi) karena empat blok TC berdiri sendiri: pagination dan tiga skenario Download Changelog (satu kelas, permukaan modal Changelog yang sama); kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung tanpa `Verifikasi`: langkah 11, 21, 26, dan 36 (S-03, S-09), serta langkah 3 (mencatat N). Langkah 14, 24, 30, dan 34 (absence toast) diletakkan segera setelah pemicu unduh dan sebelum asersi berkas (8b butir 11); pemicu dan berkas pada langkah berikutnya menjadi anchor positif.
- Expected 597 butir c dipecah: tidak ada toast dan tidak ada peringatan ditulis satu `Verifikasi` per unduhan (langkah 30 dan 34) karena keduanya klausa absence atas pemicu yang sama.
- Temuan untuk QA:
  - S-12: TC-AC-DS-421 dan TC-AC-DS-422 memakai N dari info pagination dan jumlah hasil filter dari info pagination, bukan jumlah absolut; spec mengikuti TC. Asersi bergantung pada nama literal Pre-setup #29 dan #33 (pengecualian S-12 A-11, `suite.md`).
  - TC 597 tidak menyebut nama berkas kedua dan tidak menyebut format hasil unduh kedua selain CSV; spec mengikuti TC (CSV, tanpa asersi nama berkas kedua).
  - Fixture rancangan Pre-setup #33 belum terverifikasi ada di environment; fixture `settingsDeviceSku` dan 23 env var `AC_DS_*` (termasuk `AC_DS_TC_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
