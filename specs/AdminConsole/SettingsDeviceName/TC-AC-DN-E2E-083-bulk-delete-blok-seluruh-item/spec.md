---
id: TC-AC-DN-E2E-083-bulk-delete-blok-seluruh-item
title: "Bulk Delete: Dialog Blok Seluruh Item Diblok dan Seleksi Dipertahankan"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DN-228
  - TC-AC-DN-229
coverage:
  web: automated
---

# Bulk Delete: Dialog Blok Seluruh Item Diblok dan Seleksi Dipertahankan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`; email dirujuk lewat `Fixture.settings-device-name`, belum ada, disediakan tim FE), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (`suite.md`): hook `beforeEach` suite membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip disetel `seen` oleh hook `before` suite dan dipulihkan di `after`.
- Data Pre-setup (baca-saja, nilai dirujuk lewat `Fixture.settings-device-name`): #16 `RFID Reader`, `Field Radio`, `Tag Reel`; #18 Usage by Company (anotasi `RFID Reader` 3 SKUs, `Field Radio` 5 BYO units, `Tag Reel` 3 BYO units); #22 relasi SKU dan unit BYO. Seluruh item ditolak dialog blok sehingga tidak ada data yang diubah (S-06).
- Env var yang dipakai: `AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`).

## Test Steps

### TC-AC-DN-228: Dialog blok Bulk Delete saat seluruh item diblok

1. Ketik Search `Tag Reel`, tekan Enter
2. Centang checkbox baris `Tag Reel`
3. Klik `(←)` pada kotak Search
4. Centang checkbox baris `RFID Reader` dan `Field Radio`
5. Klik `Bulk Action` lalu `Delete`
6. Verifikasi judul dialog blok "Cannot Delete Device Names"
7. Verifikasi body: bullet `RFID Reader` (anotasi "3 SKUs"), `Field Radio` (anotasi "5 BYO units"), dan `Tag Reel` (anotasi "3 BYO units")
8. Verifikasi footer: hanya satu tombol `[OK]`
9. Verifikasi dialog konfirmasi `Delete Device Names` tidak tampil sebelum dialog blok
10. Verifikasi tidak ada toast sukses
11. Verifikasi baris `RFID Reader` dan `Field Radio` tetap ada pada List sehingga tidak ada Device Name yang terhapus

### TC-AC-DN-229: Seleksi dipertahankan setelah dialog blok Bulk Delete ditutup

12. Klik `[OK]` pada dialog blok
13. Verifikasi dialog blok tertutup
14. Verifikasi List tampil tanpa perubahan
15. Verifikasi Bulk Action Bar tetap tampil dengan counter `3 Device Names selected`
16. Verifikasi baris `RFID Reader` dan `Field Radio` tetap tercentang
17. Ketik Search `Tag Reel`, tekan Enter
18. Verifikasi baris `Tag Reel` tetap tercentang
19. Verifikasi tidak ada toast
20. Klik `(←)` pada kotak Search, lalu klik ikon `(X)` pada Bulk Action Bar

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Halaman yang sama dipakai berulang tanpa submit: TC-AC-DN-229 melanjutkan dialog blok yang terbuka pada TC-AC-DN-228.
- Langkah penghubung (S-03, S-09): langkah 1 dan 17 (Search untuk menemukan `Tag Reel`, R-16); langkah 3 (mengosongkan Search; seleksi dipertahankan); langkah 20 (membersihkan Search dan seleksi).
- Temuan untuk QA: TC-AC-DN-228 dan 229 mencentang `Tag Reel` pada daftar default tanpa Search, tetapi urutan alfabetis default menempatkan `Tag Reel` setelah `Seed Device 120` (bukan di halaman 1); spec menemukannya lewat Search dengan seleksi dipertahankan.
