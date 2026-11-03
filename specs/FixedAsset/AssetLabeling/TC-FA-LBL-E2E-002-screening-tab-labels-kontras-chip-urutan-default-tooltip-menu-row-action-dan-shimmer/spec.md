---
id: TC-FA-LBL-E2E-002-screening-tab-labels-kontras-chip-urutan-default-tooltip-menu-row-action-dan-shimmer
title: "Screening Tab Labels: Kontras Chip, Urutan Default, Tooltip, Menu Row Action, Shimmer, dan Chip Panjang (bagian 2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-8
  - TC-FA-LBL-9
  - TC-FA-LBL-10
  - TC-FA-LBL-13
  - TC-FA-LBL-14
  - TC-FA-LBL-15
  - TC-FA-LBL-16
coverage:
  web: automated
---

# Screening Tab Labels: Kontras Chip, Urutan Default, Tooltip, Menu Row Action, Shimmer, dan Chip Panjang (bagian 2/2)

## Prerequisites

- Mode: FE+BE.
- Hook suite: `before`, `beforeEach`, dan `after` berlaku sesuai `suite.md` (termasuk flag Guided Tooltip `seen`); spec ini tidak menulis ulang isinya.
- Akun aktor TC-FA-LBL-8, 9, 15, 16, 14, dan 10: Total Control Company Alpha (Pre-setup #1, Sarah Johnson), `Fixture.assetLabeling.akun.totalControl`, `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels).
- Akun aktor TC-FA-LBL-13: Total Control Company Extra (Pre-setup #56), `Fixture.assetLabeling.akun.totalControlExtra`, `Spectra.env.FA_TC_EXTRA_PASSWORD`. Akun, nilai `{namaCompany}`, dan Company Extra belum ada, disediakan tim FE (Pre-setup #56 menunggu konfirmasi tim FE). Dipakai lewat langkah Ganti akun (langkah 31); hook `after` mengembalikan sesi ke akun default suite.
- Environment variable: `FA_LBL_TC_PASSWORD` dan `FA_TC_EXTRA_PASSWORD` (nama mengikuti pola `FA_TC_<COMPANY>_PASSWORD` di `suite.md`; `FA_TC_EXTRA_PASSWORD` belum terdaftar dan disediakan tim FE). Password tidak ditulis di spec atau fixture.
- Fixture: `Fixture.assetLabeling.*` (`fixtures/asset-labeling.json`) memuat identitas akun dan nama data tanpa rahasia; fixture ini belum ada dan disediakan tim FE.
- Data Pre-setup (dibaca saja, tidak diubah spec): #12 (katalog Company Alpha 9 label; dipakai: `Night Shift` `#1E3A8A`, `High Priority` `#EF4444` Modified By `Sarah J` dengan nama lengkap `Sarah Johnson`, `Seasonal Event`) dan #13. Nilai Pre-setup dipakai literal karena Population Company Alpha bernama literal (lihat `suite.md`).
- Data Dinamis: label panjang (Pre-setup #22, berada di Company Extra) `Fixture.assetLabeling.labelPanjang120`: kata `Alpha` dipisah spasi tunggal dan ditutup akhiran unik per run `{runId}-002` (`{runId}` hanya digit), disusun supaya total tepat 120 karakter termasuk akhiran (nilai dihitung di script). Disiapkan di hook `before` lewat sesi API aktor Company Extra (tidak menambah label di katalog Company Alpha, sehingga TC-FA-LBL-9 tetap melihat tepat 9 label Pre-setup #12) dan dihapus di hook `after`. Aset `Laptop Dell - 8` yang terpasang pada label itu di Pre-setup #22 tidak dipakai asersi dan tidak di-seed.
- Kemampuan teknis: sesi API aktor (Company Extra untuk seeding label panjang) dan fixture BE untuk seeding label (lihat `suite.md`); `Spectra.intercept()` untuk menahan respons List Labels (TC-FA-LBL-10) dan melepasnya di langkah 29; intercept dilepas di hook `after` bila spec gagal di tengah.
- Format Last Updated dan Modified By mengikuti General Settings Company Alpha (nilai awal, tidak diubah spec).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-FA-LBL-8: Warna teks chip otomatis kontras terhadap warna latar label

1. Verifikasi teks chip `Night Shift` (latar `#1E3A8A`) berwarna putih `#FFFFFF` karena rasio kontras terhadap latar lebih tinggi daripada hitam
2. Verifikasi teks chip `High Priority` (latar `#EF4444`) berwarna hitam `#000000` karena rasio kontras terhadap latar lebih tinggi daripada putih

### TC-FA-LBL-9: Urutan default Labels List adalah kolom Label A-Z

3. Verifikasi baris berurutan alfabetis menaik tanpa membedakan huruf besar-kecil: `Audit Ready`, `Executive Asset`, `Field Kit`, `Finance Department`, `High Priority`, `Maintenance Due`, `Night Shift`, `Seasonal Event`, `Warehouse Priority`
4. Verifikasi indikator sort aktif tampil pada header kolom `Label`

### TC-FA-LBL-15: Kolom Modified By: format tampil dan tooltip nama lengkap

5. Verifikasi sel Modified By baris `High Priority` menampilkan teks polos `Sarah J`
6. Verifikasi sel Modified By baris `High Priority` tanpa badge
7. Hover sel Modified By baris `High Priority`
8. Verifikasi tooltip menampilkan nama lengkap `Sarah Johnson`

### TC-FA-LBL-16: Menu row action Labels List: urutan, icon, dan severity

9. Klik `⋯` pada baris `Seasonal Event`
10. Verifikasi menu memuat berurutan `Detail` (icon FileInfoLine, dark), `Edit` (icon Edit2Line, dark), `Delete` (icon DeleteBin6Line, danger)
11. Verifikasi aksi dark mendahului aksi danger
12. Verifikasi opsi `View Tagged Assets` tidak ada di menu
13. Tutup menu row action dengan Esc

### TC-FA-LBL-14: Tooltip icon Table Tools dan header kolom Actions

14. Hover icon Search
15. Verifikasi tooltip `Search` tampil
16. Hover icon Filter
17. Verifikasi tooltip `Filter` tampil
18. Hover icon Download
19. Verifikasi tooltip `Download` tampil
20. Hover icon Changelog
21. Verifikasi tooltip `Changelog` tampil
22. Hover header kolom Actions (⋯)
23. Verifikasi tooltip `Column Visibility` tampil
24. Fokuskan icon Changelog memakai keyboard Tab
25. Verifikasi tooltip `Changelog` juga tampil saat icon menerima fokus keyboard

### TC-FA-LBL-10: State loading Labels List menampilkan Shimmer

26. Tahan respons List Labels lewat `Spectra.intercept()` (delay jaringan)
27. Muat ulang tab Labels dengan F5
28. Verifikasi area tabel menampilkan Shimmer selama respons ditahan
29. Lepas tahanan respons List Labels
30. Verifikasi Shimmer diganti baris data

### TC-FA-LBL-13: Label bernama 120 karakter tampil penuh di kolom Label tanpa dipotong

31. Ganti akun: Logout, login sebagai Total Control Company Extra `Fixture.assetLabeling.akun.totalControlExtra` (`Spectra.env.FA_TC_EXTRA_PASSWORD`), buka Fixed Asset > Settings > Asset Master > tab `Labels`
32. Ketik Search `Alpha Alpha Alpha`, tekan Enter
33. Hover chip label panjang `Fixture.assetLabeling.labelPanjang120`
34. Verifikasi chip menampilkan nama penuh 120 karakter (termasuk akhiran `{runId}-002`) tanpa penggalan `..`
35. Verifikasi kolom Label menyesuaikan isi dan nama panjang membungkus natural
36. Verifikasi tidak muncul tooltip hover pada chip
37. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03): langkah 13 (menutup menu row action), langkah 26 sampai 27 dan 29 (menahan dan melepas respons sebagai pemicu Shimmer), langkah 31 (Ganti akun ke Company Extra, sesuai Precondition TC-FA-LBL-13), langkah 32 (Search untuk menemukan baris target, R-16), dan langkah 37 (mengosongkan Search).
- Ukuran spec (37 langkah, di atas smell 35 langkah): ketujuh TC satu kelas (fungsional, Screening tab Labels) dan satu halaman; TC-FA-LBL-9 mengharapkan tepat 9 label Pre-setup #12 di Company Alpha sehingga TC-FA-LBL-8, 9, 14, 15, 16, dan 10 berbagi sesi dan katalog yang sama, dan TC-FA-LBL-13 (Company Extra) ditaruh terakhir supaya ganti akun hanya satu kali; memisahkannya ke spec lain menggandakan login dan pembukaan tab Labels; langkah membengkak karena tiap klausa Expected menjadi satu `Verifikasi` (S-01).
- Urutan TC: TC-FA-LBL-9 ditulis sebelum TC-FA-LBL-13 dan label panjang berada di Company Extra, jadi katalog Company Alpha tetap tepat 9 label; TC-FA-LBL-13 terakhir karena memakai akun Company Extra (S-10).
- Absence tooltip pada langkah 36: hover pada langkah 33 menjadi anchor tooltip dan chip penuh diverifikasi pada langkah 34 sebelumnya (bagian 8b butir 2, 5).
- Temuan untuk QA:
  - Akun, `{namaCompany}`, dan penyediaan Company Extra (Pre-setup #56) menunggu konfirmasi tim FE; spec memakai kunci `Fixture.assetLabeling.akun.totalControlExtra` dan env `FA_TC_EXTRA_PASSWORD` sebagai tempat penampung yang disediakan tim FE, bukan nilai karangan.
  - TC-FA-LBL-14 meminta hover header kolom Actions dan Expected tooltip `Column Visibility`; TC tidak menyebut apakah tooltip itu muncul pada fokus keyboard, hanya `Changelog`; spec hanya mengasersi `Changelog` pada fokus.
