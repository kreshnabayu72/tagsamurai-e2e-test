---
id: TC-AC-DN-E2E-075-bulk-action-bar-dan-seleksi-dasar
title: "Bulk Action Bar: Screening, Overlay Aksi, Counter, Tutup, dan Indeterminate"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-202
  - TC-AC-DN-203
  - TC-AC-DN-204
  - TC-AC-DN-205
  - TC-AC-DN-208
coverage:
  web: automated
---

# Bulk Action Bar: Screening, Overlay Aksi, Counter, Tutup, dan Indeterminate

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`; email dirujuk lewat `Fixture.settings-device-name`, belum ada, disediakan tim FE), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (`suite.md`): hook `beforeEach` suite membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip disetel `seen` oleh hook `before` suite dan dipulihkan di `after`.
- Data Pre-setup (baca-saja, nilai dirujuk lewat `Fixture.settings-device-name`): #16 `Cable Tester`, `Door Antenna`; #17 seed `Seed Device 001` sampai `Seed Device 120` sehingga total baris Device Name 130 (label `Select All (130 records)`). Spec hanya memilih baris dan tidak mengubah data.
- Env var yang dipakai: `AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`).

## Test Steps

### TC-AC-DN-202: Screening Bulk Action Bar setelah satu baris dicentang

1. Centang checkbox baris `Cable Tester`
2. Verifikasi kolom Checkbox berada paling kiri tabel dengan checkbox pada header kolom
3. Verifikasi Bulk Action Bar tampil di atas tabel, rata kiri, sejajar dengan toolbar
4. Verifikasi urutan elemen: tombol `Bulk Action`, teks `1 Device Name selected`, tombol `Select All (130 records)`, ikon `(X)` paling kanan

### TC-AC-DN-203: Overlay tombol Bulk Action hanya memuat aksi Delete

5. Klik tombol `Bulk Action`
6. Verifikasi overlay memuat satu aksi `Delete` dengan ikon DeleteBin6Line dan severity danger
7. Verifikasi tidak ada aksi bulk lain
8. Tekan Esc untuk menutup overlay

### TC-AC-DN-204: Counter Bulk Action Bar berubah realtime saat baris dicentang dan dilepas

9. Hilangkan centang baris `Cable Tester`
10. Centang baris `Cable Tester`
11. Verifikasi counter `1 Device Name selected`
12. Centang baris `Door Antenna`
13. Verifikasi counter `2 Device Names selected`
14. Hilangkan centang baris `Cable Tester`
15. Verifikasi counter `1 Device Name selected`
16. Hilangkan centang baris `Door Antenna`

### TC-AC-DN-205: Ikon X pada Bulk Action Bar membatalkan seluruh seleksi dan menutup bar

17. Centang baris `Cable Tester` dan `Door Antenna`
18. Klik ikon `(X)` pada Bulk Action Bar
19. Verifikasi Bulk Action Bar hilang
20. Verifikasi checkbox baris `Cable Tester` dan `Door Antenna` tidak tercentang
21. Verifikasi checkbox header tidak tercentang

### TC-AC-DN-208: Checkbox header menampilkan status indeterminate saat sebagian baris tercentang

22. Centang baris `Cable Tester` saja
23. Verifikasi checkbox header menampilkan ikon strip minus `[-]` (indeterminate)
24. Verifikasi teks counter `1 Device Name selected`
25. Hilangkan centang baris `Cable Tester`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, S-09): langkah 8 (menutup overlay); langkah 9 (membersihkan seleksi dari TC-AC-DN-203 sebelum TC-AC-DN-204 mengandalkan seleksi kosong); langkah 16 dan 25 (membersihkan seleksi).
- Halaman yang sama dipakai berulang tanpa submit: TC-AC-DN-203 melanjutkan seleksi `Cable Tester` dari TC-AC-DN-202.
- Dataset 130 baris dipakai hanya untuk label tombol `Select All (130 records)`; spec tidak memuat TC volume sehingga tetap satu kelas fungsional.
- Temuan untuk QA: tidak ada.
