---
id: TC-AC-DN-E2E-086-fokus-dialog-bulk-delete-dua-kelompok-dan-blok
title: "Aksesibilitas Dialog Bulk Delete: Fokus Terkunci dan Label Aksi Eksplisit (Dua Kelompok D-04 dan Blok D-05)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-643
coverage:
  web: automated
---

# Aksesibilitas Dialog Bulk Delete: Fokus Terkunci dan Label Aksi Eksplisit (Dua Kelompok D-04 dan Blok D-05)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`; email dirujuk lewat `Fixture.settings-device-name`, belum ada, disediakan tim FE), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (`suite.md`): hook `beforeEach` suite membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip disetel `seen` oleh hook `before` suite dan dipulihkan di `after`.
- Data Pre-setup (baca-saja, nilai dirujuk lewat `Fixture.settings-device-name`): #16 `Cable Tester` (tanpa SKU), `RFID Reader` (tiga SKU), `Field Radio` (unit BYO Hardware); #22 relasi SKU dan unit BYO. Kedua dialog ditutup dengan Esc sehingga tidak ada data Pre-setup yang diubah (S-06).
- Env var yang dipakai: `AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`).

## Test Steps

### TC-AC-DN-643: Dialog dua kelompok D-04 dan dialog blok bulk D-05 mengunci fokus dan memakai label aksi eksplisit

1. Centang baris `Cable Tester`, `RFID Reader`, dan `Field Radio`
2. Klik `Bulk Action` lalu `Delete`
3. Tekan `Tab` berulang sampai fokus berputar
4. Verifikasi fokus Tab berputar di dalam dialog dua kelompok dan tidak keluar ke halaman di belakangnya
5. Verifikasi dialog dua kelompok memuat tombol berlabel `[Cancel]` dan `[Continue]`
6. Tekan `Esc`
7. Verifikasi `Esc` menutup dialog dua kelompok tanpa menghapus apa pun
8. Verifikasi seleksi tiga baris dipertahankan
9. Hilangkan centang baris `Cable Tester`
10. Klik `Bulk Action` lalu `Delete`
11. Tekan `Tab` berulang sampai fokus berputar
12. Verifikasi fokus Tab berputar di dalam dialog blok bulk
13. Verifikasi dialog blok bulk memuat hanya satu tombol berlabel `[OK]`
14. Tekan `Esc`
15. Verifikasi `Esc` menutup dialog blok bulk
16. Verifikasi seleksi dua baris dipertahankan
17. Klik ikon `(X)` pada Bulk Action Bar

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 17 (membatalkan seleksi agar state bersih, S-09).
- Pembagian TC lintas spec: TC-AC-DN-621 (dialog single) ada di spec 074.
- Temuan untuk QA: TC-AC-DN-643 mengasersi seleksi "dipertahankan" tanpa menyebut counter; spec memakai baris yang tetap tercentang.
