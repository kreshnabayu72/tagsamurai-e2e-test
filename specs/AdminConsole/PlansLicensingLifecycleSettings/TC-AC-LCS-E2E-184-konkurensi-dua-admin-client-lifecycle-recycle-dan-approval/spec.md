---
id: TC-AC-LCS-E2E-184-konkurensi-dua-admin-client-lifecycle-recycle-dan-approval
title: "Konkurensi Dua Admin: Save Bersamaan Tab Client Lifecycle, Recycle Bin, dan Approval Settings"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LCS-654
  - TC-AC-LCS-655
  - TC-AC-LCS-656
coverage:
  web: automated
---

# Konkurensi Dua Admin: Save Bersamaan Tab Client Lifecycle, Recycle Bin, dan Approval Settings

## Prerequisites

- Mode: FE+BE. Kelas harness c (multi-konteks: dua admin pada dua sesi browser terpisah).
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Sesi A = Total Control (nama tampil `Andi Wijaya`; Modified By `Andi W`). Sesi B = Manage plans & licensing (Read dan Update) `managePlansLicensingAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Rina Kusuma`; Modified By `Rina K`), password dari `Spectra.env.AC_MPL_PASSWORD` (nama env baru yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example`, di luar folder suite); konteks browser kedua login di hook `before` spec ini, membuka tab yang sama dengan sesi A, dan ditutup di hook `after` dengan sesi login dihapus.
- Data Pre-setup yang dipakai: ketujuh tab pada nilai default (Pre-setup 7). Baseline jumlah entri Changelog tab Client Lifecycle, Recycle Bin, dan Approval Settings dicatat di hook `before` spec ini lewat kemampuan baca yang disediakan tim FE/BE (Changelog bersifat permanen, S-12); asersi Changelog memakai selisih terhadap baseline.
- Kemampuan teknis (disediakan tim FE/BE; tidak ada endpoint yang dikarang): konteks browser kedua yang login dengan akun Manage plans & licensing; Fixture BE untuk memulihkan ketujuh tab ke nilai default dan membaca jumlah entri Changelog.
- State global: konfigurasi tab Lifecycle Settings diubah lewat Fixture BE atau permintaan langsung; dipulihkan di hook `beforeEach` dan `after` suite lewat Fixture BE; suite berjalan serial.
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab Lifecycle Settings ke nilai default, jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings; flag Guided Tooltip halaman ini diset true oleh hook `before` suite; hook `after` suite memulihkan state global. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).

## Test Steps

### TC-AC-LCS-654: Dua admin Save tab Client Lifecycle bersamaan, penulisan terakhir menang tanpa dialog konflik

1. Sesi A dan sesi B: klik tab Client Lifecycle
2. Sesi A: ubah Notify Plan Owner Before Event menjadi `46` (belum Save)
3. Sesi B: ubah Notify Plan Owner Before Event menjadi `47` lalu klik `[Save]` dan tunggu toast sukses
4. Verifikasi toast sukses "Success, client lifecycle settings have been saved." pada sesi B
5. Sesi A: klik `[Save]`
6. Verifikasi toast sukses "Success, client lifecycle settings have been saved." pada sesi A
7. Verifikasi tidak ada dialog konflik pada sesi A
8. Sesi B: muat ulang tab Client Lifecycle dan amati nilai
9. Verifikasi Notify Plan Owner Before Event bernilai `46` pada sesi B (penulisan terakhir menang)
10. Sesi B: klik icon Changelog
11. Verifikasi Changelog tab Client Lifecycle memuat dua entri terpisah, satu per Save (selisih jumlah entri terhadap baseline 2)
12. Sesi B: tutup modal Changelog lewat `✕`

### TC-AC-LCS-655: Dua admin Save tab Recycle Bin bersamaan, penulisan terakhir menang tanpa dialog konflik

13. Sesi A dan sesi B: klik tab Recycle Bin
14. Sesi A: ubah Permanently Delete Recycle Bin menjadi `31` (belum Save)
15. Sesi B: ubah Permanently Delete Recycle Bin menjadi `32` lalu klik `[Save]` dan tunggu toast sukses
16. Verifikasi toast sukses "Success, recycle bin settings have been saved." pada sesi B
17. Sesi A: klik `[Save]`
18. Verifikasi toast sukses "Success, recycle bin settings have been saved." pada sesi A
19. Verifikasi tidak ada dialog konflik pada sesi A
20. Sesi B: muat ulang tab Recycle Bin dan amati nilai
21. Verifikasi Permanently Delete Recycle Bin bernilai `31` pada sesi B (penulisan terakhir menang)
22. Sesi B: klik icon Changelog
23. Verifikasi Changelog tab Recycle Bin memuat dua entri terpisah, satu per Save (selisih jumlah entri terhadap baseline 2)
24. Sesi B: tutup modal Changelog lewat `✕`

### TC-AC-LCS-656: Dua admin Save tab Approval Settings bersamaan, penulisan terakhir menang tanpa dialog konflik

25. Sesi A dan sesi B: klik tab Approval Settings
26. Sesi A: ubah Approval Timeout menjadi `4` (belum Save)
27. Sesi B: ubah Approval Timeout menjadi `5` lalu klik `[Save]` dan tunggu toast sukses
28. Verifikasi toast sukses "Success, approval settings have been saved." pada sesi B
29. Sesi A: klik `[Save]`
30. Verifikasi toast sukses "Success, approval settings have been saved." pada sesi A
31. Verifikasi tidak ada dialog konflik pada sesi A
32. Sesi B: muat ulang tab Approval Settings dan amati nilai
33. Verifikasi Approval Timeout bernilai `4` pada sesi B (penulisan terakhir menang)
34. Sesi B: klik icon Changelog
35. Verifikasi Changelog tab Approval Settings memuat dua entri terpisah, satu per Save (selisih jumlah entri terhadap baseline 2)

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Kelas harness c.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC mengikuti urutan nomor kolom `sourceTc`. Konteks browser kedua (sesi B) adalah objek asersi sehingga spec ini kelas c tanpa butir `P-2`.
- Dua TC dalam satu spec memakai tab berbeda; tiap TC memulai dari nilai default tab tersebut sehingga hasil TC sebelumnya tidak dipakai (S-06, S-09).
- Temuan untuk QA:
  - TC 651 sampai 657 dan 675 bertanda `Manual Only` (dua sesi pengguna paralel); spec tetap menulisnya sebagai kelas c dengan kebutuhan dua sesi di Prerequisites (bagian 2 konvensi).
  - TC 651 sampai 657 Expected d "Changelog memuat dua entri terpisah" tanpa baseline; spec mengasersi selisih dua terhadap baseline jumlah entri (S-12).
  - TC 651 sampai 657 tidak menyebut apakah kedua sesi membuka tab target sejak awal; spec menulis langkah klik tab pada kedua sesi di awal tiap TC sesuai precondition "Dua sesi browser terpisah membuka tab yang sama".
  - Post Condition seluruh TC tanpa langkah observasi tidak diasersi.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`; pemulihan state, pembukaan tab, pengaturan data lewat Fixture BE, dan ganti akun): langkah 1, 12-13, 24-25.
