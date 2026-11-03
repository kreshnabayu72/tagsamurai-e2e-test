---
id: TC-AC-LCS-E2E-195-konkurensi-dua-admin-system-limits-dan-save-identik
title: "Konkurensi Dua Admin: Save Bersamaan Tab System Limits dan Save Identik Akibat Save Admin Lain"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LCS-657
  - TC-AC-LCS-675
coverage:
  web: automated
---

# Konkurensi Dua Admin: Save Bersamaan Tab System Limits dan Save Identik Akibat Save Admin Lain

## Prerequisites

- Mode: FE+BE. Kelas harness c (multi-konteks: dua admin pada dua sesi browser terpisah).
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Sesi A = Total Control (nama tampil `Andi Wijaya`; Modified By `Andi W`). Sesi B = Manage plans & licensing (Read dan Update) `managePlansLicensingAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Rina Kusuma`; Modified By `Rina K`), password dari `Spectra.env.AC_MPL_PASSWORD` (nama env baru yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example`, di luar folder suite); konteks browser kedua login di hook `before` spec ini, membuka tab yang sama dengan sesi A, dan ditutup di hook `after` dengan sesi login dihapus.
- Data Pre-setup yang dipakai: ketujuh tab pada nilai default (Pre-setup 7). Baseline jumlah entri Changelog tab System Limits dan Trial Settings dicatat di hook `before` spec ini lewat kemampuan baca yang disediakan tim FE/BE (Changelog bersifat permanen, S-12); asersi Changelog memakai selisih terhadap baseline.
- Kemampuan teknis (disediakan tim FE/BE; tidak ada endpoint yang dikarang): konteks browser kedua yang login dengan akun Manage plans & licensing; Fixture BE untuk memulihkan ketujuh tab ke nilai default dan membaca jumlah entri Changelog.
- State global: konfigurasi tab Lifecycle Settings diubah lewat Fixture BE atau permintaan langsung; dipulihkan di hook `beforeEach` dan `after` suite lewat Fixture BE; suite berjalan serial.
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab Lifecycle Settings ke nilai default, jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings; flag Guided Tooltip halaman ini diset true oleh hook `before` suite; hook `after` suite memulihkan state global. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).

## Test Steps

### TC-AC-LCS-657: Dua admin Save tab System Limits bersamaan, penulisan terakhir menang tanpa dialog konflik

1. Sesi A dan sesi B: klik tab System Limits
2. Sesi A: ubah Bulk Transaction Row Limit menjadi `1001` (belum Save)
3. Sesi B: ubah Bulk Transaction Row Limit menjadi `1002` lalu klik `[Save]` dan tunggu toast sukses
4. Verifikasi toast sukses "Success, system limits settings have been saved." pada sesi B
5. Sesi A: klik `[Save]`
6. Verifikasi toast sukses "Success, system limits settings have been saved." pada sesi A
7. Verifikasi tidak ada dialog konflik pada sesi A
8. Sesi B: muat ulang tab System Limits dan amati nilai
9. Verifikasi Bulk Transaction Row Limit bernilai `1001` pada sesi B (penulisan terakhir menang)
10. Sesi B: klik icon Changelog
11. Verifikasi Changelog tab System Limits memuat dua entri terpisah, satu per Save (selisih jumlah entri terhadap baseline 2)
12. Sesi B: tutup modal Changelog lewat `✕`

### TC-AC-LCS-675: Save tab Trial Settings yang menjadi identik dengan nilai tersimpan akibat Save admin lain menampilkan toast netral

13. Sesi A dan sesi B: klik tab Trial Settings
14. Sesi B: ubah Max Trial Duration dari `30` menjadi `31`, klik `[Save]`, tunggu toast sukses
15. Sesi A (belum dimuat ulang): ubah Max Trial Duration dari `30` menjadi `31`
16. Sesi A: klik `[Save]`
17. Verifikasi toast netral "No changes to save." tampil pada sesi A
18. Verifikasi tidak ada toast sukses "Success, trial settings have been saved." pada sesi A
19. Verifikasi tab Trial Settings pada sesi A memuat ulang dengan Max Trial Duration `31`
20. Sesi A: klik icon Changelog tab Trial Settings
21. Verifikasi Changelog memuat tepat satu entri baru dari sesi B dengan Modified By `Rina K` (selisih jumlah entri terhadap baseline 1)
22. Verifikasi tidak ada entri baru dari sesi A dengan Modified By `Andi W`

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Kelas harness c.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC mengikuti urutan nomor kolom `sourceTc`. Konteks browser kedua (sesi B) adalah objek asersi sehingga spec ini kelas c tanpa butir `P-2`.
- Dua TC dalam satu spec memakai tab berbeda; tiap TC memulai dari nilai default tab tersebut sehingga hasil TC sebelumnya tidak dipakai (S-06, S-09).
- TC 675: toast netral "No changes to save." ditulis sebagai `Verifikasi` yang menjadi anchor positif sebelum `Verifikasi` absence toast sukses (bagian 8b butir 11); asersi "tidak ada entri dari sesi A" didahului `Verifikasi` entri sesi B tampil di Changelog yang sama (anchor, bagian 8b butir 2).
- Temuan untuk QA:
  - TC 651 sampai 657 dan 675 bertanda `Manual Only` (dua sesi pengguna paralel); spec tetap menulisnya sebagai kelas c dengan kebutuhan dua sesi di Prerequisites (bagian 2 konvensi).
  - TC 651 sampai 657 Expected d "Changelog memuat dua entri terpisah" tanpa baseline; spec mengasersi selisih dua terhadap baseline jumlah entri (S-12).
  - TC 651 sampai 657 tidak menyebut apakah kedua sesi membuka tab target sejak awal; spec menulis langkah klik tab pada kedua sesi di awal tiap TC sesuai precondition "Dua sesi browser terpisah membuka tab yang sama".
  - Post Condition seluruh TC tanpa langkah observasi tidak diasersi.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`; pemulihan state, pembukaan tab, pengaturan data lewat Fixture BE, dan ganti akun): langkah 1, 12-13.
