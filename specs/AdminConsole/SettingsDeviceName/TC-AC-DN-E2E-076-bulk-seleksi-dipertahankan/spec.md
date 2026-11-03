---
id: TC-AC-DN-E2E-076-bulk-seleksi-dipertahankan
title: "Bulk Delete: Checkbox Header dan Seleksi Dipertahankan saat Halaman, Search, Filter, dan Sort Berubah"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-206
  - TC-AC-DN-207
  - TC-AC-DN-213
  - TC-AC-DN-214
  - TC-AC-DN-215
  - TC-AC-DN-216
coverage:
  web: automated
---

# Bulk Delete: Checkbox Header dan Seleksi Dipertahankan saat Halaman, Search, Filter, dan Sort Berubah

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`; email dirujuk lewat `Fixture.settings-device-name`, belum ada, disediakan tim FE), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (`suite.md`): hook `beforeEach` suite membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip disetel `seen` oleh hook `before` suite dan dipulihkan di `after`.
- Data Pre-setup (baca-saja, nilai dirujuk lewat `Fixture.settings-device-name`): #16 `Cable Tester`, `Door Antenna`, `Field Radio` (Measurement `Box`); #17 seed `Seed Device 001` sampai `Seed Device 120` (total baris 130, sehingga List punya halaman 2 dan seterusnya dengan 10 baris per halaman). Spec hanya memilih baris dan tidak mengubah data.
- Env var yang dipakai: `AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`).

## Test Steps

### TC-AC-DN-206: Checkbox header memilih seluruh baris pada halaman aktif

1. Klik checkbox pada header kolom Checkbox
2. Verifikasi checkbox header berstatus tercentang
3. Verifikasi sepuluh baris halaman 1 tercentang (`Barcode Station` sampai `Seed Device 002`)
4. Verifikasi teks counter `10 Device Names selected`
5. Klik tombol pagination ke halaman 2
6. Verifikasi baris halaman 2 tidak tercentang
7. Klik tombol pagination kembali ke halaman 1

### TC-AC-DN-207: Melepas checkbox header membatalkan seleksi halaman aktif dan menutup bar

8. Klik checkbox header lagi untuk melepas centang
9. Verifikasi seluruh baris halaman aktif tidak tercentang
10. Verifikasi checkbox header tidak tercentang
11. Verifikasi Bulk Action Bar hilang

### TC-AC-DN-213: Seleksi dipertahankan saat berpindah halaman

12. Centang baris `Cable Tester` pada halaman 1
13. Klik tombol pagination ke halaman 2
14. Verifikasi baris halaman 2 tidak tercentang
15. Klik tombol pagination kembali ke halaman 1
16. Verifikasi baris `Cable Tester` pada halaman 1 tetap tercentang
17. Verifikasi counter tetap `1 Device Name selected`

### TC-AC-DN-214: Seleksi dipertahankan saat Search diubah dan dikosongkan

18. Ketik Search `Door`, tekan Enter
19. Verifikasi counter tetap `1 Device Name selected` walau baris `Cable Tester` tidak tampil pada hasil Search
20. Klik `(←)` pada kotak Search
21. Verifikasi baris `Cable Tester` tetap tercentang

### TC-AC-DN-215: Seleksi dipertahankan saat Filter Measurement diterapkan

22. Klik ikon Filter, pilih Measurement `Box` pada field `Measurement`, klik `[Apply]`
23. Verifikasi counter tetap `1 Device Name selected`
24. Verifikasi Bulk Action Bar tetap tampil
25. Bersihkan Filter Measurement `Box`

### TC-AC-DN-216: Seleksi dipertahankan saat urutan Sort diubah

26. Klik ikon sort pada header kolom `Device Name` sekali lagi hingga urutan menurun (Z-A)
27. Verifikasi counter tetap `1 Device Name selected`
28. Klik tombol pagination ke halaman terakhir
29. Verifikasi baris `Cable Tester` tetap tercentang pada posisi barunya
30. Kembalikan urutan Sort `Device Name` ke urutan awal, lalu klik ikon `(X)` pada Bulk Action Bar

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, S-09): langkah 7 (kembali ke halaman 1 agar header dan baris yang dicek ada di halaman 1); langkah 20 (mengosongkan Search); langkah 25 (membersihkan Filter, label tombol pembersih tidak disebut TC); langkah 28 (menuju halaman tempat `Cable Tester` berada pada urutan Z-A, S-14); langkah 30 (membersihkan Sort dan seleksi).
- Halaman yang sama dipakai berulang tanpa submit: TC-AC-DN-207 melanjutkan sepuluh baris tercentang dari TC-AC-DN-206; TC-AC-DN-214, TC-AC-DN-215, dan TC-AC-DN-216 melanjutkan seleksi `Cable Tester` yang dibuat pada TC-AC-DN-213 (langkah awal identik).
- Temuan untuk QA:
  - TC-AC-DN-216 Expected "pada posisi barunya" tidak menyebut halaman; spec menuju halaman terakhir (urutan Z-A menempatkan `Cable Tester` di dekat akhir).
  - TC-AC-DN-215 tidak menyebut cara membersihkan Filter sesudah uji; dicatat sebagai langkah penghubung tanpa nama tombol.
