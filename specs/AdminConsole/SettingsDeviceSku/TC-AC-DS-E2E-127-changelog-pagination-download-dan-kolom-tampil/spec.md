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
- Data Pre-setup (hanya dibaca, tidak diubah): SKU inti dan seed (#29, #30), riwayat Changelog Principal (#33) dalam keadaan awal 35 entri (18 oleh `Jane S`, 17 oleh `Budi K`), General Settings Date Format `dd/MM/yy`, 24 jam, Asia/Jakarta (#35). Nilai dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Data Dinamis: tidak ada. Berkas unduhan disimpan di folder unduhan runner dan tidak dihapus oleh spec.
- Kemampuan teknis (disediakan tim FE/BE): membaca isi berkas CSV dan XLSX yang diunduh (nama berkas, baris header, jumlah baris data); menghapus preferensi kolom Setup Column modal Changelog di browser (hook `before` dan hook `after`), bukan lewat [Reset to Default]; keadaan awal 35 entri dijamin fixture BE (audit trail permanen).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

### TC-AC-DS-421: Pagination modal Changelog: default 10, opsi ukuran halaman, dan halaman langsung

1. Klik ikon Changelog
2. Verifikasi modal "Changelog: Device SKU" tampil
3. Verifikasi default 10 baris per halaman dengan 4 halaman untuk 35 entri
4. Klik selector jumlah data per halaman
5. Verifikasi opsi ukuran halaman `10`, `25`, `50`, dan `100` tanpa opsi "All"
6. Ketik `3` pada input nomor halaman lalu tekan Enter
7. Verifikasi halaman 3 tampil memuat entri ke-21 sampai ke-30
8. Ubah ukuran halaman menjadi 25
9. Verifikasi tampilan kembali ke halaman 1 dengan 2 halaman
10. Ubah ukuran halaman menjadi 10

### TC-AC-DS-422: Download Changelog tanpa dan dengan filter aktif

11. Klik ikon Download pada modal
12. Klik `Download as CSV`
13. Verifikasi tidak ada toast sukses
14. Verifikasi file bernama `Changelog-Device-SKU.csv` berisi 35 entri (semua halaman)
15. Klik ikon Filter pada modal
16. Pada field Modified By pilih `Budi K`
17. Klik `[Apply]` pada Filter Panel modal
18. Klik ikon Download lalu `Download as XLSX`
19. Verifikasi file bernama `Changelog-Device-SKU.xlsx` berisi 17 entri Modified By `Budi K` saja

### Pemulihan state antar TC

20. Klik ikon Filter, hapus chip `Budi K` dari field Modified By, klik `[Apply]`

### TC-AC-DS-425: Download Changelog dengan hasil nol baris menghasilkan file berisi header saja

21. Klik ikon Search pada modal, ketik Search `tidak-ada-entri`, tekan Enter
22. Klik ikon Download lalu `Download as CSV`
23. Verifikasi tidak ada toast
24. Verifikasi file terunduh berisi hanya baris header kolom yang tampil

### Pemulihan state antar TC

25. Klik `(←)` pada kotak Search

### TC-AC-DS-597: Download Changelog mengikuti kolom yang tampil

26. Klik header kolom Actions (⋯) pada modal, hilangkan centang `Field` dan `Modified By`
27. Verifikasi kolom `Field` dan `Modified By` hilang dari tabel modal
28. Klik ikon Download pada modal lalu `Download as CSV`
29. Verifikasi tidak ada toast dan tidak ada peringatan tentang kolom yang tidak ikut
30. Verifikasi file pertama `Changelog-Device-SKU.csv` memuat kolom `Date`, `Action`, `SKU`, `Old Value`, dan `New Value` tanpa kolom `Field` dan `Modified By`
31. Centang kembali kolom `Field` dan `Modified By`
32. Klik ikon Download pada modal lalu `Download as CSV`
33. Verifikasi tidak ada toast dan tidak ada peringatan tentang kolom yang tidak ikut
34. Verifikasi file kedua memuat kembali ketujuh kolom `Date`, `Action`, `SKU`, `Field`, `Old Value`, `New Value`, dan `Modified By`

### Pemulihan state akhir

35. Tutup modal Changelog

## Notes

- Spec melewati sekitar 35 langkah (35 langkah nominal, sekitar 37 dengan ekspansi) karena empat blok TC berdiri sendiri: pagination dan tiga skenario Download Changelog (satu kelas, permukaan modal Changelog yang sama); kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung tanpa `Verifikasi`: langkah 10, 20, 25, dan 35 (S-03, S-09). Langkah 13, 23, dan 29, 33 (absence toast) diletakkan segera setelah pemicu unduh dan sebelum asersi berkas (8b butir 11); pemicu dan berkas pada langkah berikutnya menjadi anchor positif.
- Expected 597 butir c dipecah: tidak ada toast dan tidak ada peringatan ditulis satu `Verifikasi` per unduhan (langkah 29 dan 33) karena keduanya klausa absence atas pemicu yang sama.
- Temuan untuk QA:
  - S-12: TC menetapkan jumlah absolut (35 entri, 17 entri `Budi K`, 4 halaman) pada audit trail permanen; spec mengikuti TC dan bergantung pada keadaan awal yang dijamin fixture BE. Pengecualian modul belum ada di Lampiran A (butuh keputusan).
  - TC 597 tidak menyebut nama berkas kedua dan tidak menyebut format hasil unduh kedua selain CSV; spec mengikuti TC (CSV, tanpa asersi nama berkas kedua).
  - TC 421 Expected d ("kembali ke halaman 1 dengan 2 halaman") tidak menyebut ukuran halaman 25 secara eksplisit selain pada langkah; spec mengikuti TC.
  - Fixture rancangan Pre-setup #33 belum terverifikasi ada di environment; fixture `settingsDeviceSku` dan 23 env var `AC_DS_*` (termasuk `AC_DS_TC_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
