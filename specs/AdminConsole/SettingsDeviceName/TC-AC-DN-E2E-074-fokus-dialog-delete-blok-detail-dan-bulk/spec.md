---
id: TC-AC-DN-E2E-074-fokus-dialog-delete-blok-detail-dan-bulk
title: "Aksesibilitas Dialog: Fokus Terkunci dan Label Aksi Eksplisit (Delete, Blok, Detail, dan Unsaved Changes)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-621
coverage:
  web: automated
---

# Aksesibilitas Dialog: Fokus Terkunci dan Label Aksi Eksplisit (Delete, Blok, Detail, dan Unsaved Changes)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`; email dirujuk lewat `Fixture.settings-device-name`, belum ada, disediakan tim FE), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (`suite.md`): hook `beforeEach` suite membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip disetel `seen` oleh hook `before` suite dan dipulihkan di `after`.
- Data Pre-setup (baca-saja, nilai dirujuk lewat `Fixture.settings-device-name`): #16 `Cable Tester` (tanpa SKU), `RFID Reader` (tiga SKU), `Gate Antenna`; #22 relasi SKU. Dialog Delete hanya ditutup dengan Esc, dialog blok ditolak, dan form Create yang dirty ditinggalkan dengan `[Leave]`, sehingga tidak ada data Pre-setup yang diubah (S-06).
- Nilai uji yang diketik: "Draft Gateway" pada field Device Name form Create (tidak disimpan).
- Env var yang dipakai: `AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`).

## Test Steps

### TC-AC-DN-621: Dialog Delete, blok, Detail, dan Unsaved Changes mengunci fokus di dalam dialog dan memakai label aksi eksplisit

1. Ketik Search `Cable Tester`, tekan Enter
2. Klik ikon aksi pada kolom Actions baris `Cable Tester` lalu klik `Delete`
3. Tekan `Tab` berulang sampai fokus berputar
4. Verifikasi fokus Tab berputar di dalam dialog Delete dan tidak keluar ke halaman di belakangnya
5. Verifikasi dialog Delete memuat tombol berlabel `[Cancel]` dan `[Delete]`
6. Tekan `Esc`
7. Verifikasi `Esc` menutup dialog Delete
8. Ganti isi kotak search dengan `RFID Reader`, tekan Enter
9. Klik ikon aksi pada kolom Actions baris `RFID Reader` lalu klik `Delete`
10. Tekan `Tab` berulang sampai fokus berputar
11. Verifikasi fokus Tab berputar di dalam dialog blok
12. Verifikasi dialog blok memuat hanya satu tombol berlabel `[OK]`
13. Tekan `Esc`
14. Verifikasi `Esc` menutup dialog blok
15. Ganti isi kotak search dengan `Gate Antenna`, tekan Enter
16. Klik nama `Gate Antenna`
17. Tekan `Tab` berulang sampai fokus berputar
18. Verifikasi fokus Tab berputar di dalam dialog Detail
19. Verifikasi dialog Detail ditutup lewat ikon `[X]`
20. Tekan `Esc`
21. Verifikasi `Esc` menutup dialog Detail
22. Klik `(←)` pada kotak Search
23. Klik `+ Device Name`, ketik "Draft Gateway" pada field Device Name, lalu tekan `Esc`
24. Tekan `Tab` berulang sampai fokus berputar
25. Verifikasi fokus Tab berputar di dalam dialog Unsaved Changes
26. Verifikasi dialog Unsaved Changes memuat tombol berlabel `[Cancel]` dan `[Leave]`
27. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 8 dan 15 (Search untuk menemukan baris target, R-16); langkah 22 (mengosongkan Search); langkah 27 (menutup form Create yang dirty lewat dialog `Unsaved Changes` dan `[Leave]`, S-08 dan S-09).
- Pembagian TC lintas spec: TC-AC-DN-643 (dialog bulk) ada di spec 086.
- Temuan untuk QA: TC-AC-DN-621 Expected butir c menyebut penutupan dialog Detail "lewat ikon `[X]`" tanpa langkah klik di Langkah Uji; spec mengasersi ikon `[X]` sebagai kontrol penutup dan menutup dialog dengan `Esc` sesuai Langkah Uji.
