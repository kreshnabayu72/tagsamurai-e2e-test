---
id: TC-AC-DS-E2E-120-changelog-kombinasi-penuh-dan-kosongkan-search
title: "Changelog: Kombinasi Penuh Search, Filter, Sort, Pagination dan Mengosongkan Search saat Filter dan Sort Aktif"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-566
  - TC-AC-DS-567
coverage:
  web: automated
---

# Changelog: Kombinasi Penuh Search, Filter, Sort, Pagination dan Mengosongkan Search saat Filter dan Sort Aktif

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca, tidak diubah): SKU inti dan seed (#29, #30), riwayat Changelog Principal (#33) berupa seed 35 entri (18 oleh `Jane S`, 17 oleh `Budi K`; 33 entri Edit, 1 Create, 1 Delete; total pada modal dapat lebih besar karena entri yang ditulis spec lain, sehingga jumlah entri diasersi relatif terhadap E yang dibaca dari info pagination), General Settings Date Format `dd/MM/yy`, 24 jam, Asia/Jakarta (#35). Nilai dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Data Dinamis: tidak ada; spec tidak membuat atau mengubah data. Entri buatan spec lain dipulihkan baseline data uji yang disediakan tim FE/BE (suite serial); E dibaca dari UI, bukan diturunkan dari seeding.
- Kemampuan teknis (disediakan tim FE/BE): seeding dan pemulihan Pre-setup #29, #30, #33, #35 ke keadaan awal sebelum spec.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

### TC-AC-DS-566: Kombinasi penuh Search, Filter, Sort, dan Pagination pada Changelog

1. Klik ikon Changelog
2. Verifikasi modal "Changelog: Device SKU" tampil
3. Klik ikon Search pada modal, ketik Search `HHR-ARC`, tekan Enter
4. Klik ikon Filter pada modal
5. Verifikasi Filter Panel modal tampil
6. Pada field Action pilih `Edit`
7. Verifikasi chip `Edit` tampil di dalam field Action
8. Klik [Apply] pada Filter Panel modal
9. Klik header kolom Date sekali
10. Ubah jumlah data per halaman menjadi 25
11. Verifikasi dua baris pertama tabel berurutan Oldest First: Edit `HHR-ARC-200` (28/09/26 14:40) lalu Edit `HHR-ARC-100` (01/10/26 09:15)
12. Verifikasi setiap baris pada tabel ber-Action `Edit` dan memuat `HHR-ARC`
13. Verifikasi entri Delete `HHR-ARC-300` tidak tampil karena Action `Edit`
14. Verifikasi keempat kontrol tetap aktif tanpa saling menimpa: Search `HHR-ARC`, Filter Action `Edit`, Sort Date Oldest First, dan 25 data per halaman

### Pemulihan state antar TC

15. Klik `(←)` pada kotak Search; klik ikon Filter, hapus chip `Edit` dari field Action, klik [Apply]; klik header kolom Date sekali lagi (Newest First) dan sekali lagi (netral); ubah jumlah data per halaman menjadi 10

### TC-AC-DS-567: Mengosongkan Search pada Changelog saat Filter dan Sort aktif hanya melepas Search

16. Klik ikon Filter pada modal
17. Verifikasi Filter Panel modal tampil
18. Pada field Action pilih `Edit`
19. Verifikasi chip `Edit` tampil di dalam field Action
20. Klik [Apply] pada Filter Panel modal
21. Catat jumlah entri total pada info pagination sebagai E
22. Klik header kolom Date sekali
23. Klik ikon Search pada modal, ketik Search `HHR-ARC`, tekan Enter
24. Klik `✕` pada Search, tekan Enter pada input kosong
25. Verifikasi Search dilepas dan Filter Action `Edit` tetap aktif: jumlah entri total sama dengan E yang dicatat pada langkah 21 dan jumlah halaman sama dengan pembulatan ke atas E/10
26. Verifikasi tabel tidak memuat entri Create dan Delete
27. Verifikasi Sort Date Oldest First tetap aktif: baris pertama Edit Model/Type `HHR-BIG-01` tanggal 01/09/26 08:00

### Pemulihan state akhir

28. Klik ikon Filter, hapus chip `Edit` dari field Action, klik [Apply]; klik header kolom Date sekali lagi (Newest First) dan sekali lagi (netral); tutup modal Changelog

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 15 dan 28 (membersihkan Search, Filter, Sort, dan ukuran halaman agar TC berikutnya tidak bergantung pada state sebelumnya, S-09). Langkah 21 mencatat E; langkah 24 memakai idiom "klik `✕` pada Search, tekan Enter".
- Expected 566 butir a dipecah per klausa: dua baris pertama berurutan Oldest First (langkah 11) dan setiap baris ber-Action `Edit` serta memuat `HHR-ARC` (langkah 12, didahului langkah 11 yang membuktikan baris pembanding tampil); butir b langkah 13; butir c langkah 14 (daftar keempat kontrol disebut utuh).
- Expected 567 butir a dipecah: langkah 25 (Search dilepas, Filter tetap, jumlah entri sama dengan E dan halaman = pembulatan ke atas E/10) dan langkah 26 (tanpa Create dan Delete, anchor positif: baris pada langkah 25); butir b langkah 27.
- Temuan untuk QA:
  - S-12: TC-AC-DS-567 memakai E (jumlah entri Edit yang dicatat setelah Filter, dibaca dari info pagination) dan tidak lagi memakai jumlah absolut; asersi bergantung pada nama literal Pre-setup #29 dan #33 (pengecualian S-12 A-11, `suite.md`).
  - S-11/S-13: fixture rancangan Pre-setup #33 belum terverifikasi ada di environment; fixture `settingsDeviceSku`, 23 env var `AC_DS_*` (termasuk `AC_DS_TC_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - TC 566 langkah 8 ("tabel dicek") menyebut jumlah per halaman 25 tanpa Expected untuk kontrol pagination selain butir c; spec mengikuti TC.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
