---
id: TC-AC-LCS-E2E-092-independensi-antar-tab-save-in-flight-dan-save-berhasil
title: "Independensi Antar Tab: Save In-Flight dan Save Berhasil Tidak Memengaruhi Tab Lain"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-350
  - TC-AC-LCS-351
coverage:
  web: automated
---

# Independensi Antar Tab: Save In-Flight dan Save Berhasil Tidak Memengaruhi Tab Lain

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif).
- Konfigurasi ketujuh tab pada nilai default (Pre-setup 7) dipulihkan lewat Fixture BE di hook `beforeEach` dan `after` suite (kemampuan disediakan tim FE/BE).
- Kemampuan teknis: `Spectra.intercept` menahan respons permintaan Save tab Trial Settings selama 10 detik (TC-AC-LCS-350); intercept dilepas di langkah 10 dan dipulihkan di hook `beforeEach` dan `after` suite. Fixture BE memulihkan ketujuh tab ke default di langkah 16 (kemampuan disediakan tim FE/BE).
- Data uji: Max Trial Duration `45`, Free Plan Duration `400` (diubah spec dan dipulihkan ke default).
- Data uji mengacu ke fixture `Fixture.plansLicensingLifecycleSettings` (nilai default tiap tab); fixture belum ada dan disediakan tim FE/BE.
- Konfigurasi Lifecycle Settings bersifat platform-wide; suite berjalan serial (`parallel: false`).
- Env var: `AC_TC_PASSWORD` (password Total Control Admin Console, satu nama satu arti).

## Test Steps

### TC-AC-LCS-350: Save Trial Settings in-flight tidak memblokir pengeditan dan Save tab Free Plan Settings

1. Atur intercept: tahan respons permintaan Save tab Trial Settings selama 10 detik
2. Ubah Max Trial Duration dari `30` menjadi `45`
3. Klik `[Save]`
4. Saat permintaan berjalan, klik tab Free Plan Settings
5. Ubah Free Plan Duration dari `365` menjadi `400`
6. Verifikasi field Free Plan Duration enabled
7. Verifikasi `[Save]` tab Free Plan Settings enabled
8. Klik `[Save]` tab Free Plan Settings
9. Verifikasi toast sukses "Success, free plan settings have been saved."
10. Lepas tahanan respons Save tab Trial Settings dan tunggu kedua respons diterima
11. Verifikasi toast sukses "Success, trial settings have been saved." menggantikan toast sebelumnya (satu slot toast aktif)
12. Klik tab Trial Settings
13. Verifikasi Max Trial Duration `45`
14. Klik tab Free Plan Settings
15. Verifikasi Free Plan Duration `400`

### TC-AC-LCS-351: Save berhasil pada satu tab tidak membuang perubahan belum disimpan pada tab lain

16. Pulihkan ketujuh tab ke nilai default lewat Fixture BE
17. Muat ulang halaman dengan F5
18. Klik tab Trial Settings
19. Ubah Max Trial Duration dari `30` menjadi `45` (belum disimpan)
20. Klik tab Free Plan Settings
21. Ubah Free Plan Duration dari `365` menjadi `400`
22. Klik `[Save]`
23. Verifikasi toast sukses "Success, free plan settings have been saved."
24. Klik tab Trial Settings
25. Verifikasi Max Trial Duration tetap `45`
26. Verifikasi `[Save]` tab Trial Settings tetap enabled
27. Kembalikan Max Trial Duration ke nilai tersimpan `30`

## Notes

- Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: langkah 10 (lepas intercept), 16 sampai 18 (pemulihan state antar TC, S-09), 27 (form Trial tidak dibiarkan dirty di akhir spec, S-09).
- TC-AC-LCS-352 ada di spec 191 (`TC-AC-LCS-E2E-191-independensi-antar-tab-reset-tidak-menyentuh-tab-lain`).
- Temuan untuk QA:
  - Post Condition TC-AC-LCS-350 (nilai tersimpan `45` dan `400`) diamati lewat nilai pada tab sesudah kedua respons; TC tidak memberi langkah observasi muat ulang.
  - Post Condition TC-AC-LCS-351 (Free Plan Duration tersimpan `400`, Max Trial Duration tersimpan tetap `30`) tidak punya langkah observasi di TC dan tidak diasersi.
