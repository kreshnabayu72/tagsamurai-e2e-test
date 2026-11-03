---
id: TC-FA-LBL-E2E-028-duplikat-nama-label-create-debounce-case-insensitive-dan-cek-keunikan-gagal
title: "Duplikat Nama Label Create (Debounce, Case-Insensitive, dan Cek Keunikan Gagal)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LBL-76
  - TC-FA-LBL-77
  - TC-FA-LBL-78
  - TC-FA-LBL-79
coverage:
  web: automated
---

# Duplikat Nama Label Create (Debounce, Case-Insensitive, dan Cek Keunikan Gagal)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson), password dari `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak mengubah state global kecuali dinyatakan di bawah.
- Data Pre-setup #12: label `High Priority` (`#EF4444`) sudah ada di katalog Company Alpha; hanya dibaca, tidak diubah (S-06, tidak ada aksi tulis yang berhasil).
- Intercept (`Spectra.intercept()`) untuk TC-FA-LBL-79: request pengecekan keunikan nama Label dipaksa gagal. Endpoint request itu tidak disebut di TC (ditentukan tim FE); intercept dilepas segera sesudah pemicu selesai.
- Kemampuan teknis (disediakan tim FE/BE, suite.md): sesi API aktor dan fixture BE untuk membaca state katalog (jumlah label bernama `High Priority`).
- Kemampuan teknis: mengamati inline error pada selisih waktu 300 ms dan 500 ms setelah ketikan terakhir.
- Spec ini tidak membuat data; tidak ada cleanup data.

## Test Steps

1. Klik `[+ Label]`

### TC-FA-LBL-76: Nama duplikat terdeteksi saat mengetik setelah debounce

2. Ketik `High Priority` di Label Name
3. Tunggu lebih dari 500 ms tanpa berpindah fokus
4. Verifikasi inline error `Label name already exists` tampil di bawah Label Name tanpa menunggu blur
5. Hover `[Submit]`
6. Verifikasi `[Submit]` berstatus disabled dengan tooltip `Label name already exists`

### TC-FA-LBL-77: Duplikat tidak membedakan huruf besar-kecil dan spasi tepi

7. Kosongkan Label Name
8. Ketik `high priority` di Label Name dan tunggu lebih dari 500 ms
9. Verifikasi inline error `Label name already exists` tampil untuk varian `high priority`
10. Verifikasi `[Submit]` berstatus disabled untuk varian `high priority`
11. Kosongkan Label Name
12. Ketik `HIGH PRIORITY` dengan dua spasi di awal dan di akhir di Label Name dan tunggu lebih dari 500 ms
13. Verifikasi inline error `Label name already exists` tampil untuk varian `HIGH PRIORITY` dengan spasi tepi
14. Verifikasi `[Submit]` berstatus disabled untuk varian `HIGH PRIORITY` dengan spasi tepi

### TC-FA-LBL-78: Pengecekan keunikan memakai debounce 500 ms, bukan blur

15. Kosongkan Label Name
16. Ketik `High Priority` lalu amati pesan tepat 300 ms setelah ketikan terakhir
17. Verifikasi pada 300 ms belum ada inline error
18. Tunggu hingga lebih dari 500 ms setelah ketikan terakhir tanpa memindahkan fokus
19. Verifikasi inline error `Label name already exists` tampil tanpa blur

### TC-FA-LBL-79: Pengecekan keunikan gagal tidak menampilkan error dan Submit tetap aktif

20. Kosongkan Label Name
21. Paksa request pengecekan keunikan gagal (intercept jaringan)
22. Ketik `High Priority` di Label Name dan tunggu lebih dari 500 ms
23. Verifikasi tidak ada pesan error
24. Verifikasi `[Submit]` berstatus enabled
25. Hentikan intersepsi request pengecekan keunikan
26. Klik `[Submit]`
27. Verifikasi server menolak dengan inline error `Label name already exists`
28. Verifikasi modal tetap terbuka
29. Verifikasi tepat satu label `High Priority` di katalog (lewat fixture BE), tidak ada label ganda
30. Klik icon `[✕]`
31. Verifikasi dialog `Unsaved Changes` dengan teks `You have unsaved changes. Are you sure you want to leave?`, tombol `[Cancel]` dan `[Leave]` tampil
32. Klik `[Leave]`

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Satu pembukaan modal dipakai seluruh TC; Label Name dikosongkan di antara kasus (prinsip 6, R-12): error `Label name already exists` identik antar-TC, sehingga pengosongan Label Name (langkah 7, 11, 15, 20) menjadi pembersih dan hasil kasus berikutnya diamati sesudah ketikan baru.
- Langkah penghubung (tanpa awalan Verifikasi, S-03): langkah 7 sampai 20 (pembersih), langkah 25 (melepas intercept setelah pemicu selesai, S-09), dan langkah 32 (menutup modal; form dirty karena Label Name terisi, jadi ditutup lewat dialog `Unsaved Changes` dengan `[Leave]`, S-08).
- P-5: TC-FA-LBL-79 adalah satu objek-uji ringan kelas b (kegagalan request pengecekan keunikan) di spec fungsional duplikat nama; tidak ada objek-uji kelas a, b, atau h lain di spec ini.
- Submit duplikat yang ditolak server (TC-FA-LBL-87) ada di spec 030.
- Temuan untuk QA:
  - TC-FA-LBL-77 Data Uji menulis `HIGH PRIORITY` "dengan spasi tepi" tanpa jumlah spasi; spec memakai dua spasi di awal dan di akhir.
  - TC-FA-LBL-78 meminta pengamatan "tepat 300 ms"; ketepatan 300 ms bergantung pada kemampuan harness mengatur jam atau mengamati dengan toleransi, yang tidak dijelaskan TC.
  - TC-FA-LBL-79 tidak menyebut endpoint request pengecekan keunikan yang dipaksa gagal; ditentukan tim FE.
