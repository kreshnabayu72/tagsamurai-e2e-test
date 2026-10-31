---
id: TC-GS-GSET-E2E-047-lintas-modul-timestamp-mengikuti-entitas-staff-yang-login
title: "Timestamp lintas produk"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-122
coverage:
  web: automated
---

# Timestamp lintas produk

## Prerequisites

- Mode: FE+BE.
- Akun pertama (login di hook `before` spec ini): Total Control staf Distributor `PT Maju Bersama` (Tabel Data Uji Pre-setup No 6), Time Zone entitas `Asia/Jakarta` (UTC+07:00). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE, kredensial `Spectra.env.GS_MAJU_TC_PASSWORD` (nama env baru).
- Akun kedua (login pada langkah 3, ganti akun eksplisit): Total Control staf Client `PT Sentosa Abadi` (Tabel Data Uji Pre-setup No 7), Time Zone entitas UTC+08:00 (Pre-setup No 19). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE, kredensial `Spectra.env.GS_SENTOSA_TC_PASSWORD` (nama env baru).
- Environment variable: `GS_MAJU_TC_PASSWORD` dan `GS_SENTOSA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Kedua nama belum terdaftar di `executionConfig.environmentVariables` dan `.env.example` (didaftarkan pada tahap script).
- Hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `Spectra.env.GS_TC_PASSWORD`), karena spec selesai di akun `PT Sentosa Abadi`.
- Hook suite (flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` dan pemulihan record Client A ke baseline Pre-setup No 10): lihat `suite.md`, bagian Hook suite; spec ini tidak mengatur flag sendiri. Spec ini tidak membuka General Settings dan tidak mengubah record entitas mana pun.
- Layar awal Admin Console > Client List dibuka di hook `beforeEach` (konvensi bagian 4; precondition b TC-GS-GSET-122); langkah 1 dimulai dari layar itu.
- Data Pre-setup (read-only, tidak diubah spec): entitas `PT Maju Bersama` (UTC+07:00) dan `PT Sentosa Abadi` (UTC+08:00) (Pre-setup No 19), dengan baris `PT Sentosa Abadi` pada Admin Console > Client List. Spec tidak membuat data dinamis.
- Kemampuan teknis: (a) login ke Admin Console dan ke FAMS dengan akun staf entitas; (b) membaca nilai timestamp sumber dalam UTC untuk baris `PT Sentosa Abadi` di Client List dan untuk timestamp FAMS yang diamati, lewat sesi API atau fixture BE (mekanisme dan endpoint disediakan tim FE, tidak dikarang); (c) hasil tampilan dihitung sebagai nilai UTC ditambah offset Time Zone entitas staf yang login (+7 jam atau +8 jam). Margin ke tengah malam tidak dipersoalkan karena yang dibandingkan adalah tanggal dan jam hasil penambahan offset.
- Tidak ada state global yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-GSET-122: Format timestamp Admin Console mengikuti entitas staff yang login, bukan entitas yang dilihat

1. Catat timestamp UTC sumber kolom Last Updated baris `PT Sentosa Abadi` sebagai `{tUTC1}`
2. Verifikasi kolom Last Updated baris `PT Sentosa Abadi` menampilkan `{tUTC1}` dalam Time Zone `PT Maju Bersama` (UTC+07:00, yaitu `{tUTC1}` ditambah 7 jam)
3. Logout, lalu login sebagai Total Control staf `PT Sentosa Abadi`
4. Buka FAMS dan amati timestamp pada permukaan FAMS yang ditetapkan QA (lihat Temuan untuk QA), lalu catat timestamp UTC sumbernya sebagai `{tUTC2}`
5. Verifikasi timestamp FAMS pada langkah 4 ditampilkan dalam Time Zone `PT Sentosa Abadi` (UTC+08:00, yaitu `{tUTC2}` ditambah 8 jam)

## Notes

- Sumber TC: `global-settings/general-settings/TestCases/tc-general-settings.md` (TC-GS-GSET-122). Mode: FE+BE.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 3 (mencatat nilai UTC sumber dan ganti akun). Langkah 3 adalah Step ganti akun eksplisit; langkah 4 dan 5 bermakna bahkan bila langkah 2 gagal.
- Dependensi TC-GS-GSET-122 adalah "-" pada TC.
- Temuan untuk QA:
  - TC-GS-GSET-122 langkah 2 ("buka FAMS, amati timestamp") tidak menyebut halaman atau kolom FAMS yang diamati. Spec menunggu ketetapan QA tentang permukaan timestamp FAMS (penjelasan permukaan Admin Console > Client List > Last Updated sudah ada di langkah 1 TC).
  - Email akun staf `PT Maju Bersama` dan `PT Sentosa Abadi` tidak tertulis di Tabel Data Uji Pre-setup (No 6 dan 7 hanya menyebut entitas); spec menuliskannya "disediakan tim FE".
  - Precondition c ("`PT Sentosa Abadi` memakai Time Zone Lain") tidak menyebut opsi Time Zone; Expected b menyebut UTC+08:00 (Pre-setup No 19). Opsi Time Zone dengan offset itu tidak termasuk dua opsi yang labelnya dikunci PRD §4.3a (NC-09), sehingga ketersediaannya ditetapkan programmer.
