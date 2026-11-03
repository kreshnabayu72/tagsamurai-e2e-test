---
id: TC-AC-DN-E2E-055-create-berhasil-satu-karakter
title: "Create Device Name Berhasil: Satu Karakter"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DN-585
coverage:
  web: automated
---

# Create Device Name Berhasil: Satu Karakter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (`Budi Santoso`, Default User, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (fixture belum ada, disediakan tim FE); password `Spectra.env.AC_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` (termasuk jaring pengaman `beforeunload` dan dialog `Unsaved Changes`) dan flag Guided Tooltip dinyatakan di `suite.md`; spec ini tidak mengulangnya.
- Data Pre-setup (hanya dibaca): #13 master Measurement `Unit`; #14 Pohon Uji Kategori (leaf `Antenna` di `Hardware` > `Smart Fixed Reader`). Tidak ada Device Name Pre-setup bernama `X`.
- Data Dinamis: Device Name `X` (nama satu karakter literal tanpa suffix karena panjang nama itu objek uji; pengecualian S-12 untuk nama satu karakter): seeding idempotent (hook `before` menghapus Device Name `X` sisa run sebelumnya milik spec ini lewat fixture BE bila ada), hook `after` hanya menghapus record `X` yang dibuat spec ini, suite berjalan serial, dan nama `X` tidak dipakai spec lain pada entitas Device Name. Kemampuan hapus record Device Name disediakan tim FE/BE.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-585: Create Device Name dengan satu karakter berhasil

1. Klik tombol `+ Device Name` pada toolbar
2. Ketik `X` pada field Device Name
3. Verifikasi field Device Name menampilkan `X` dan tidak ada error panjang minimum
4. Klik field Measurement lalu pilih `Unit`
5. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih leaf `Antenna`
6. Klik `[Submit]`
7. Verifikasi toast sukses: "Success, device name has been created."
8. Verifikasi popup form tertutup
9. Ketik Search `X`, tekan Enter
10. Verifikasi List memuat baris dengan Device Name `X` dan Measurement `Unit`
11. Verifikasi baris `X` menampilkan Category badge `Antenna`

## Notes

- Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. TC-AC-DN-585 bertanda FE Test "Need API".
- Pengecualian S-12 untuk nama satu karakter literal dipakai dengan syarat yang dinyatakan di `## Prerequisites`.
- Asersi tidak adanya error panjang minimum (Expected d) diletakkan pada langkah 3, sebelum [Submit], karena popup tertutup setelah sukses (bagian 8b butir 11); nilai `X` yang tampil di field menjadi anchor positifnya.
- Langkah penghubung (S-03, tanpa awalan Verifikasi): langkah 9 (Search untuk menemukan baris target, R-16).
- Temuan untuk QA:
  - TC-AC-DN-585 tidak menyebut cara menemukan baris `X` di List; spec memakai Search.
  - Post Condition "Device Name `X` tersimpan" tidak punya langkah observasi selain List (Expected c), sehingga tidak diasersi terpisah.
