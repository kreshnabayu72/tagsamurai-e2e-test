---
id: TC-FA-CAT-E2E-198-gerbang-kolom-tier-total-control-default-user-dan-read-only
title: "Gerbang Kolom Popup Detail Tier Total Control, Default User, dan Read Only: Seluruh Kolom Bergerbang Berhak Client-wide Tanpa No access"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-684
coverage:
  web: automated
---

# Gerbang Kolom Popup Detail Tier Total Control, Default User, dan Read Only: Seluruh Kolom Bergerbang Berhak Client-wide Tanpa No access

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Role yang diuji (langkah 1 sampai 16 diulang untuk setiap baris tabel; parameter hanya akun dan password):

  | Role | Akun | Env var password |
  |---|---|---|
  | Total Control (Pre-setup #1) | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
  | Default User (Pre-setup #57) | `defaultUser_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_DU_PASSWORD` |
  | Read Only (Pre-setup #2) | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` |

- Env var `FA_DU_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA); `FA_TC_PASSWORD` dan `FA_RO_PASSWORD` sudah terdaftar untuk suite ini.
- Data Pre-setup yang hanya dibaca (tidak diubah): Pre-setup #21 (Asset Name `Laptop Dell` dan `Laptop HP` menunjuk `Laptop`), #22 (aset `Laptop Dell - 1` dan `Laptop HP - 3` pada Group `Region Jawa > Jakarta Selatan Distribution Center`), #55 (Asset Value `Laptop Dell - 1` 15000000.00 dan `Laptop HP - 3` 20000000.00; Warranty Expiry `Laptop Dell - 1` 2027-03-15 dan `Laptop HP - 3` 2027-06-30), #56 (Custom Field Purchasing `Nilai Kontrak`, `Nomor Kontrak Dell`, `Nomor PO` dengan `Laptop Dell - 1` `PO-0001` dan `Laptop HP - 3` `PO-0099`; Accounting `Kode Anggaran` dengan `Laptop Dell - 1` `ANG-01` dan `Laptop HP - 3` tanpa nilai; lisensi FA-7 aktif).
- Kemampuan teknis: pemulihan konfigurasi kolom Setup Column dengan menghapus preferensi kolom di browser (bukan lewat `[Reset to Default]`), dipakai sebagai langkah penghubung dan di hook `after` suite; disediakan tim FE.
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite (termasuk untuk akun Default User dan Read Only).
- Fixture `fixtures/settings-categories.json` disediakan tim FE.

## Test Steps

### TC-FA-CAT-684: Tier berhak client-wide tanpa No access (untuk setiap role pada tabel Role yang diuji, langkah 1 sampai 16)

1. Ganti akun: logout, login sebagai role pada tabel dengan env var passwordnya, lalu buka Fixed Asset > Settings > Categories
2. Pilih node `Electronics` pada sidebar
3. Klik elipsis (⋯) pada baris `Laptop` > `Detail`
4. Klik header Actions (⋯) > `Setup Column...`
5. Verifikasi daftar kolom Custom Field memuat kolom Purchasing (`Nilai Kontrak`, `Nomor Kontrak Dell`, `Nomor PO`) dan Accounting (`Kode Anggaran`)
6. Centang `Asset Value`, `Warranty Expiry`, `Nomor PO`, dan `Kode Anggaran`, lalu klik `[Save]`
7. Verifikasi sel Asset Value `Laptop Dell - 1` menampilkan `15000000.00` (format currency)
8. Verifikasi sel Warranty Expiry `Laptop Dell - 1` menampilkan `2027-03-15`
9. Verifikasi sel `Nomor PO` `Laptop Dell - 1` menampilkan `PO-0001`
10. Verifikasi sel `Kode Anggaran` `Laptop Dell - 1` menampilkan `ANG-01`
11. Verifikasi sel Asset Value `Laptop HP - 3` menampilkan `20000000.00`
12. Verifikasi sel Warranty Expiry `Laptop HP - 3` menampilkan `2027-06-30`
13. Verifikasi sel `Nomor PO` `Laptop HP - 3` menampilkan `PO-0099` walau di luar group mana pun yang ditugaskan (hak client-wide)
14. Verifikasi sel `Kode Anggaran` `Laptop HP - 3` menampilkan `—` karena nilai belum ada
15. Verifikasi tidak ada sel `No access` pada keempat kolom
16. Tutup Popup Detail dan pulihkan konfigurasi kolom tabel Assets dengan menghapus preferensi kolom di browser

## Notes

- Spec melewati sekitar 35 langkah setelah ekspansi (16 langkah nominal x 3 role = 48). Alasan: satu kelas (fungsional gerbang kolom), satu halaman, dan langkah tiap role identik sehingga hanya akun yang berbeda; pengulangan mengikuti bagian 8b butir 7 dengan parameter di tabel `Role yang diuji`. Langkah yang diulang: 1 sampai 16.
- Langkah 1 selalu menjadi Ganti akun eksplisit, termasuk untuk Total Control (akun hook `before` login ulang), agar langkah tiap role identik dan tidak bersyarat.
- Langkah penghubung (S-03, S-09): langkah 2 (memilih node sidebar) dan langkah 16 (menutup popup dan memulihkan konfigurasi kolom); hook `after` mengembalikan sesi ke akun default suite.
- Post Condition TC-FA-CAT-684 ("dikembalikan lewat `[Reset to Default]` lalu `[Save]`") dipenuhi dengan menghapus preferensi kolom di browser sesuai konvensi bagian 4; kemampuan disediakan tim FE.
- Asersi absence pada langkah 15 diawali anchor positif pada surface yang sama (langkah 7 sampai 14: sel bernilai pada baris yang sama).
- Tier Group Manager ada di spec 197; tier Accounting Global dan Tanpa Hak Nilai Sensitif di spec 154.
- Temuan untuk QA:
  - Nama env var password akun Default User tidak tertulis di TC; `FA_DU_PASSWORD` adalah usulan.
  - TC-FA-CAT-684 langkah 5 hanya menyebut "Ulangi langkah 1 sampai 4" tanpa langkah centang kolom dan Save; spec mengulang seluruh langkah.
  - TC-FA-CAT-684 Precondition menyebut Pre-setup #57 tanpa menyebutnya sebagai akun di Role; spec memakai Pre-setup #57 sebagai akun Default User.
