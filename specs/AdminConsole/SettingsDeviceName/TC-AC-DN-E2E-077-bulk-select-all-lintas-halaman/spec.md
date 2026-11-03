---
id: TC-AC-DN-E2E-077-bulk-select-all-lintas-halaman
title: "Bulk Delete: Select All dan Unselect All Lintas Halaman"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-209
  - TC-AC-DN-211
  - TC-AC-DN-210
  - TC-AC-DN-212
coverage:
  web: automated
---

# Bulk Delete: Select All dan Unselect All Lintas Halaman

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`; email dirujuk lewat `Fixture.settings-device-name`, belum ada, disediakan tim FE), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (`suite.md`): hook `beforeEach` suite membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip disetel `seen` oleh hook `before` suite dan dipulihkan di `after`.
- Data Pre-setup (baca-saja, nilai dirujuk lewat `Fixture.settings-device-name`): #16 `Cable Tester`; #17 seed `Seed Device 001` sampai `Seed Device 120` (total baris Device Name 130, sehingga tombol `Select All (130 records)`). Spec hanya memilih baris dan tidak mengubah data.
- Env var yang dipakai: `AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`).

## Test Steps

### TC-AC-DN-209: Select All memilih seluruh baris lintas halaman

1. Centang baris `Cable Tester`
2. Klik tombol `Select All (130 records)`
3. Klik tombol pagination ke halaman 2
4. Verifikasi teks counter `130 Device Names selected`
5. Verifikasi seluruh baris pada halaman 2 tercentang
6. Verifikasi tombol berubah menjadi `Unselect All`

### TC-AC-DN-211: Klik Unselect All membatalkan seleksi lintas halaman dan menutup bar

7. Klik `Unselect All`
8. Verifikasi Bulk Action Bar hilang
9. Verifikasi tidak ada baris tercentang pada halaman 2
10. Klik tombol pagination ke halaman 1
11. Verifikasi tidak ada baris tercentang pada halaman 1

### TC-AC-DN-210: Tombol Select All berubah menjadi Unselect All setelah semua baris hasil Search dicentang manual

12. Ketik Search `Seed Device 00`, tekan Enter
13. Centang kesembilan baris `Seed Device 001` sampai `Seed Device 009` satu per satu
14. Verifikasi teks counter `9 Device Names selected`
15. Verifikasi tombol pada bar berlabel `Unselect All`
16. Klik `Unselect All`

### TC-AC-DN-212: Melepas satu baris dari kondisi terpilih penuh mengembalikan tombol menjadi Select All

17. Klik `(←)` pada kotak Search
18. Centang baris `Cable Tester`
19. Klik `Select All (130 records)`
20. Hilangkan centang baris `Cable Tester`
21. Verifikasi teks counter `129 Device Names selected`
22. Verifikasi Bulk Action Bar tetap tampil
23. Verifikasi tombol pada bar kembali berlabel `Select All` dan bukan `Unselect All`
24. Klik ikon `(X)` pada Bulk Action Bar

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Kelas e menurut dataset: List memuat 130 baris (120 seed) dan `Select All` lintas halaman memakai seluruhnya; tidak ada TC dari kelas lain di spec ini.
- Urutan TC berbeda dari urutan nomor TC (TC-AC-DN-210 sebelum TC-AC-DN-211): spec ini menjalankan TC-AC-DN-209, 211, 210, 212 supaya TC-AC-DN-211 melanjutkan kondisi terpilih penuh dari TC-AC-DN-209 (halaman yang sama dipakai berulang) dan seleksi dibersihkan sebelum TC berikutnya (S-09).
- Langkah penghubung (S-03, S-09): langkah 10 (menuju halaman 1 agar keadaan halaman 1 bisa dicek, S-14); langkah 16 dan 24 (membersihkan seleksi); langkah 17 (mengosongkan Search).
- Temuan untuk QA: tidak ada.
