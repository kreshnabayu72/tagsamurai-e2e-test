---
id: TC-AC-DN-E2E-019-mobile-bulk-bar-dan-detail
title: "Mobile: Ketuk Card pada Mode Seleksi, Tutup Bulk Bar, Nol Terpilih, dan Detail Bottom Sheet"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-50
  - TC-AC-DN-51
  - TC-AC-DN-52
  - TC-AC-DN-53
coverage:
  mobile: automated
---

# Mobile: Ketuk Card pada Mode Seleksi, Tutup Bulk Bar, Nol Terpilih, dan Detail Bottom Sheet

## Prerequisites

- Mode: FE+BE (mobile Android).
- Akun aktor: Total Control (Pre-setup #1) `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini pada aplikasi mobile Android; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `beforeEach` suite membuka `Settings > Device > Device Name` pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes` (bukan pengganti langkah pemulihan di spec ini); hook `before` suite menyetel flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` ke `seen` dan hook `after` suite memulihkannya.
- Perangkat Android uji bersama untuk spec mobile (disediakan tim FE/BE); `parallel: false`. Aplikasi mobile Android dijalankan pada perangkat itu; kemampuan long press sekitar 500 ms dan ketuk disediakan harness mobile.
- Suite berjalan serial (`parallel: false`) karena memakai state global bersama (lihat `suite.md`). Spec ini tidak mengubah Pre-setup bersama: data Device Name inti (Pre-setup #16), seed 120 baris (#17), dan nama panjang (#23) hanya dibaca.
- Nilai data Pre-setup dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE); teks yang diasersi ditulis persis seperti di TC.
- Data Pre-setup: Device Name inti (#16: `Cable Tester`, `Door Antenna`) dan seed 120 Device Name (#17); baca-saja. Tidak ada data Dinamis dan tidak ada aksi tulis.

## Test Steps

### TC-AC-DN-50: Ketuk card saat mode seleksi aktif menukar status terpilih dan tidak membuka Detail

1. Gunakan aplikasi mobile Android pada perangkat uji dan buka halaman `Settings > Device > Device Name`
2. Long press selama sekitar 500 ms pada card `Cable Tester`
3. Ketuk card `Door Antenna`
4. Verifikasi ketukan pertama: card `Door Antenna` terpilih
5. Verifikasi ketukan pertama: penghitung `2 Selected`
6. Ketuk kembali card `Door Antenna`
7. Verifikasi ketukan kedua: card `Door Antenna` tidak terpilih
8. Verifikasi ketukan kedua: penghitung `1 Selected`
9. Verifikasi tidak ada bottom sheet Detail yang terbuka selama mode seleksi
10. Ketuk tombol tutup `[✕]` pada Bulk Bar

### TC-AC-DN-51: Tombol tutup pada Bulk Bar membatalkan seleksi dan keluar dari mode seleksi

11. Long press selama sekitar 500 ms pada card `Cable Tester`
12. Ketuk tombol `[✕]` pada Bulk Bar
13. Verifikasi seleksi dibatalkan: tidak ada card terpilih
14. Verifikasi kotak seleksi pada semua card hilang
15. Verifikasi Bulk Bar tidak tampil

### TC-AC-DN-52: Menghapus centang hingga nol terpilih keluar dari mode seleksi

16. Long press selama sekitar 500 ms pada card `Cable Tester`
17. Ketuk card `Cable Tester`
18. Verifikasi penghitung mencapai `0 Selected`
19. Verifikasi kotak seleksi pada semua card hilang
20. Verifikasi Bulk Bar tidak tampil

### TC-AC-DN-53: Ketuk card di luar mode seleksi membuka Detail sebagai bottom sheet

21. Ketuk card `Cable Tester`
22. Verifikasi Detail tampil sebagai bottom sheet dengan judul "Device Name Detail"
23. Verifikasi bottom sheet Detail tanpa breadcrumb
24. Verifikasi mode seleksi tidak aktif
25. Tutup bottom sheet Detail

## Notes

- Mode: FE+BE (mobile Android). Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. `coverage.mobile: automated` (tanpa `coverage.web`).
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah 1: tampilan mobile diaktifkan dengan menjalankan aplikasi mobile Android; halaman dibuka hook `beforeEach` suite pada aplikasi tersebut.
- Langkah penghubung (S-03, S-09): langkah 10 membatalkan mode seleksi sesudah TC-AC-DN-50; langkah 25 menutup bottom sheet Detail.
- TC-AC-DN-52: Expected menyebut penghitung `0 Selected`, kotak seleksi hilang, dan Bulk Bar tidak tampil sebagai satu kalimat; spec memecahnya menjadi tiga `Verifikasi` (S-01).
- Temuan untuk QA: tidak ada temuan sumber untuk TC dalam spec ini (precondition, Expected, dan data konsisten).
