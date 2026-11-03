---
id: TC-AC-DN-E2E-084-bulk-delete-satu-item-diblok
title: "Bulk Delete: Satu Item Diblok Memakai Dialog Blok Single (SKU dan Unit BYO)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DN-230
  - TC-AC-DN-614
coverage:
  web: automated
---

# Bulk Delete: Satu Item Diblok Memakai Dialog Blok Single (SKU dan Unit BYO)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`; email dirujuk lewat `Fixture.settings-device-name`, belum ada, disediakan tim FE), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (`suite.md`): hook `beforeEach` suite membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip disetel `seen` oleh hook `before` suite dan dipulihkan di `after`.
- Data Pre-setup (baca-saja, nilai dirujuk lewat `Fixture.settings-device-name`): #16 `RFID Reader` (tiga SKU) dan `Field Radio` (unit BYO Hardware di Company E); #22 relasi SKU dan unit BYO. Dialog blok menolak aksi sehingga tidak ada data yang diubah (S-06).
- Env var yang dipakai: `AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`).

## Test Steps

### TC-AC-DN-230: Bulk Action Bar dengan satu item diblok memakai dialog blok single

1. Centang checkbox baris `RFID Reader`
2. Klik `Bulk Action` lalu `Delete`
3. Verifikasi judul dialog blok "Cannot Delete Device Name" dalam bentuk singular
4. Verifikasi body: satu bullet `RFID Reader`
5. Verifikasi body: pesan alasan blok SKU "This device name still has SKUs."
6. Verifikasi footer: hanya satu tombol `[OK]`
7. Verifikasi dialog blok bulk `Cannot Delete Device Names` tidak tampil
8. Klik `[OK]`
9. Klik ikon `(X)` pada Bulk Action Bar

### TC-AC-DN-614: Bulk Action Bar dengan satu item diblok unit BYO memakai dialog blok single

10. Centang checkbox baris `Field Radio`
11. Klik `Bulk Action` lalu `Delete`
12. Verifikasi judul dialog blok "Cannot Delete Device Name" dalam bentuk singular
13. Verifikasi body: satu bullet `Field Radio`
14. Verifikasi body: pesan alasan blok unit BYO "This device name still has registered devices."
15. Verifikasi footer: hanya satu tombol `[OK]`
16. Verifikasi dialog blok bulk "Cannot Delete Device Names" tidak tampil
17. Verifikasi tidak ada toast
18. Klik `[OK]`
19. Verifikasi Bulk Action Bar tetap tampil dengan `1 Device Name selected`
20. Verifikasi baris `Field Radio` tetap tercentang
21. Klik ikon `(X)` pada Bulk Action Bar

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, S-09): langkah 8 (menutup dialog blok TC-AC-DN-230); langkah 9 dan 21 (membersihkan seleksi).
- Temuan untuk QA: TC-AC-DN-230 tidak menyebut state sesudah dialog blok ditutup dan tidak punya Expected tentang toast; spec hanya mengasersi Expected yang tertulis.
