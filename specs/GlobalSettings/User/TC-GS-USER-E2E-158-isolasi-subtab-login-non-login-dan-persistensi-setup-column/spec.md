---
id: TC-GS-USER-E2E-158-isolasi-subtab-login-non-login-dan-persistensi-setup-column
title: "Isolasi Sub-tab Login User dan Non-Login User serta Persistensi Setup Column Terpisah"
priority: Low
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-992
  - TC-GS-USER-993
coverage:
  web: automated
---

# Isolasi Sub-tab Login User dan Non-Login User serta Persistensi Setup Column Terpisah

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2), kredensial `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before` lalu membuka Global Settings > User > User List (sub-tab Login User). Spec memakai satu akun tanpa ganti akun. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`.
- Data Pre-setup (Tabel Data Uji Pre-setup) dibaca saja dan tidak diubah: Login User Dewi Lestari (No. 12) dan Non-Login User Agus Prasetyo serta Lina Marlina (No. 21). Spec tidak membuat data.
- State yang diubah: Setup Column sub-tab Login User akun Total Control (kolom `Email` disembunyikan pada TC-GS-USER-993). Pemulihan ditulis sebagai langkah aksi (langkah 16 sampai 20); hook `after` mengembalikan konfigurasi Setup Column sub-tab Login User akun Total Control ke default sebagai cadangan dan tetap jalan walau spec gagal di tengah (kemampuan menghapus penyimpanan Setup Column disediakan tim FE).
- Tidak ada state global lain yang diubah.

## Test Steps

### TC-GS-USER-992: Data user dari sub-tab Login User tidak tampil di sub-tab Non-Login User

1. Klik icon Search, ketik `Dewi`, tekan Enter pada sub-tab Login User
2. Verifikasi `Dewi Lestari` tampil di tabel sub-tab Login User
3. Kosongkan Search lewat `(✕)`, tekan Enter
4. Klik sub-tab `Non-Login User`
5. Verifikasi `Agus Prasetyo` tampil di tabel sub-tab Non-Login User
6. Klik icon Search, ketik `Dewi`, tekan Enter
7. Verifikasi `Dewi Lestari` (Login) tidak tampil di tabel sub-tab Non-Login User

### TC-GS-USER-993: Persistensi Setup Column sub-tab Login User terpisah dari Non-Login User

8. Kosongkan Search lewat `(✕)`, tekan Enter
9. Klik sub-tab `Login User`
10. Buka Setup Column dari header kolom Actions `⋯` > `Setup Column...`
11. Hapus centang kolom `Email`, klik `[Save]`
12. Tunggu aksi selesai
13. Verifikasi kolom `Email` tidak tampil di tabel sub-tab Login User
14. Klik sub-tab `Non-Login User`
15. Verifikasi kolom `Email` tampil di tabel sub-tab Non-Login User

### Pemulihan Setup Column Login User

16. Klik sub-tab `Login User`
17. Buka Setup Column dari header kolom Actions `⋯` > `Setup Column...`
18. Centang kolom `Email`, klik `[Save]`
19. Tunggu aksi selesai
20. Verifikasi kolom `Email` tampil kembali di tabel sub-tab Login User

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`. Tidak ada TC kelas harness.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 6 (Search); langkah 3 dan 8 (mengosongkan Search); langkah 4, 9, 14, 16 (berpindah sub-tab); langkah 10, 11, 12 (aksi TC-GS-USER-993 "Hide kolom Email di Login User", tombol `[Save]` sesuai footer Modal Setup Column); langkah 17 sampai 19 (memulihkan Setup Column; langkah 20 adalah asersi tambahan yang membuktikan pemulihan, tidak ada di Expected TC, S-03).
- Asersi absence (langkah 7) didahului `Verifikasi` pembanding pada surface yang sama (langkah 5: `Agus Prasetyo` tampil di sub-tab Non-Login User) dan pembuktian bahwa Search `Dewi` menemukan `Dewi Lestari` di sub-tab Login User (langkah 2; bagian 8b butir 2).
- Tidak ada TC yang terbelah lintas spec.
- Temuan untuk QA:
  - TC-GS-USER-992: Expected "Dewi Lestari (Login) tidak tampil" tidak menyebut apakah hasil Search kosong atau berisi Non-Login User lain bernama `Dewi`; spec hanya mengasersi `Dewi Lestari` tidak tampil.
  - TC-GS-USER-993: TC tidak menyebut cara menyimpan hasil hide (`[Save]` pada Modal Setup Column) dan tidak menyebut apakah kolom `Email` ada pada sub-tab Non-Login User sebelum aksi; spec mengasersi `Email` tampil pada sub-tab Non-Login User sesudah hide di Login User.
  - TC sumber tidak menyebut apakah Search dipertahankan saat berpindah sub-tab; spec mengosongkan Search sebelum berpindah sub-tab dan membuka Search ulang tiap kunjungan.
