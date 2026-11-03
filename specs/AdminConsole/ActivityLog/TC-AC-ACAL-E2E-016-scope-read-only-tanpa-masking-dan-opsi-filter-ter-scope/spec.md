---
id: TC-AC-ACAL-E2E-016-scope-read-only-tanpa-masking-dan-opsi-filter-ter-scope
title: "Scope Read Only, Tanpa Masking, dan Opsi Filter Ter-scope"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-40
  - TC-AC-ACAL-41
  - TC-AC-ACAL-43
coverage:
  web: automated
---

# Scope Read Only, Tanpa Masking, dan Opsi Filter Ter-scope

## Prerequisites

- Mode: FE+BE.
- Suite serial (`parallel: false`); hook suite (flag Guided Tooltip, kemampuan sesi API aktor) dinyatakan di suite.md.
- Guided Tooltip: hook before/after spec ini menyetel dan memulihkan flag seen halaman Activity Log untuk akun Read Only Distributor Alfa, Read Only Partner Beta, dan Total Control Partner Beta (kemampuan disediakan tim FE/BE; hook suite hanya mencakup Total Control Principal, lihat suite.md).
- Akun aktor (password tidak ditulis di spec atau fixture; di antara nama env AC_* hanya `AC_TC_PASSWORD` yang sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`, nama lain adalah usulan tim FE (lihat Temuan untuk QA)):

| Akun | Email (Pre-setup TC) | Env var password |
|---|---|---|
| Read Only (Distributor Alfa) | `readOnlyAdminConsoleDistributorAlfa_automated_{namaCompany}@qwertysystem.net` (No 7) | `Spectra.env.AC_ALFA_RO_PASSWORD` |
| Read Only (Partner Beta) | `readOnlyAdminConsolePartnerBeta_automated_{namaCompany}@qwertysystem.net` (No 7) | `Spectra.env.AC_BETA_RO_PASSWORD` |
| Total Control (Partner Beta) | `totalControlAdminConsolePartnerBeta_automated_{namaCompany}@qwertysystem.net` (No 7) | `Spectra.env.AC_BETA_TC_PASSWORD` |
| Total Control (Distributor Alfa), hanya sesi API pembanding TC-AC-ACAL-40 | `totalControlAdminConsoleDistributorAlfa_automated_{namaCompany}@qwertysystem.net` (No 7) | `Spectra.env.AC_ALFA_TC_PASSWORD` |

- Login akun pertama (Read Only Distributor Alfa) di hook `before` spec ini; halaman Admin Console > Activity Log (tab Session) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal).
- Data Pre-setup (tetap di environment): hierarki entitas No 8 dan data log No 9 dan No 10 untuk scope Distributor Alfa.
- Data Dinamis (suffix per run dan nomor spec, bagian 5 konvensi), dibuat lewat sesi API di hook `before`; password staf dan admin `Spectra.env.AC_DYN_PASSWORD`:
  - Staf `Staf Beta {runId}-016` (Partner Beta), `Staf Alfa {runId}-016` (Distributor Alfa), `Staf Gamma {runId}-016` (Distributor Gamma), dan `Staf Principal {runId}-016` (Principal), masing-masing membuka lalu menutup Admin Console sehingga punya baris Session. Staf Beta diberi Employee ID `Fixture.activityLog.employeeIdStafBeta` (bersuffix `{runId}-016`) dan baris Session-nya memuat IP Address dan Device / Browser dengan nilai seed `Fixture.activityLog.ipAddressStafBeta` dan `Fixture.activityLog.deviceBrowserStafBeta` (nilai ditetapkan tim FE/BE).
  - Client `Klien Uji {runId}-016` milik Partner Beta; admin `Admin Beta {runId}-016` (Partner Beta) mengubah PIC Name client itu dari `PIC Lama {runId}-016` menjadi `PIC Baru {runId}-016`, menghasilkan entri User Action dengan Old Value dan New Value tersebut.
  - Client `Klien Gamma {runId}-016` milik Distributor Gamma, dengan satu entri User Action oleh admin `Admin Gamma {runId}-016` (Distributor Gamma); entri ini ada di luar scope Partner Beta.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API kedua client dan semua staf dan admin dinamis di atas bila masih ada. Entri log tidak dapat dihapus; nama bersuffix run.
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor Total Control Distributor Alfa untuk membaca jumlah total entri Session dan User Action pada saat yang sama dengan pembacaan UI Read Only (sesi API tidak membuka sesi web dan tidak menambah entri Session, sehingga jumlah kedua pengamat dibandingkan pada data yang sama); seeding sesi dan entri User Action; membuka lalu menutup Admin Console dan mengubah PIC Name oleh staf dan admin dinamis lewat sesi API.
- Fixture: `Fixture.activityLog.*` (employeeIdStafBeta, ipAddressStafBeta, deviceBrowserStafBeta) memakai fixture activityLog baru, nilai ditetapkan tim FE.
- Tidak ada state global yang diubah.

## Test Steps

### TC-AC-ACAL-40: Read Only memiliki scope identik Total Control pada entitas yang sama

1. Catat jumlah total entri tab Session dari footer `Showing X–Y of Z entries` (nilai Z) sebagai jumlah Session Read Only Alfa
2. Klik tab "User Action"
3. Catat jumlah total entri tab User Action dari footer `Showing X–Y of Z entries` (nilai Z) sebagai jumlah User Action Read Only Alfa
4. Baca lewat sesi API aktor Total Control (Distributor Alfa) jumlah total entri Session dan jumlah total entri User Action pada data yang sama
5. Verifikasi jumlah total entri Session Read Only Alfa sama dengan jumlah total entri Session Total Control Distributor Alfa
6. Verifikasi jumlah total entri User Action Read Only Alfa sama dengan jumlah total entri User Action Total Control Distributor Alfa

### TC-AC-ACAL-41: Tidak ada masking kolom untuk aktor ber-akses

7. Ganti akun: logout, lalu login sebagai Read Only (Partner Beta) dengan `Spectra.env.AC_BETA_RO_PASSWORD`
8. Klik menu Activity Log di sidebar Admin Console
9. Ketik Search `Staf Beta {runId}-016`, tekan Enter
10. Verifikasi baris `Staf Beta {runId}-016` menampilkan IP Address, Employee ID, dan Device / Browser penuh sama dengan nilai seed, tanpa bagian yang di-mask
11. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel
12. Klik tab "User Action"
13. Ketik Search `Klien Uji {runId}-016`, tekan Enter
14. Verifikasi baris Edit `PIC Name` menampilkan Old Value `PIC Lama {runId}-016` dan New Value `PIC Baru {runId}-016` penuh, tanpa bagian yang di-mask
15. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

### TC-AC-ACAL-43: Opsi dropdown filter ikut ter-scope entitas aktor

16. Ganti akun: logout, lalu login sebagai Total Control (Partner Beta) dengan `Spectra.env.AC_BETA_TC_PASSWORD`
17. Klik menu Activity Log di sidebar Admin Console
18. Klik icon Filter, lalu buka dropdown User
19. Verifikasi daftar opsi User memuat staf Partner Beta `Staf Beta {runId}-016`
20. Verifikasi daftar opsi User tidak memuat `Staf Alfa {runId}-016`, `Staf Gamma {runId}-016`, dan `Staf Principal {runId}-016`
21. Tutup dropdown User dan Filter Panel
22. Klik tab "User Action"
23. Klik icon Filter, lalu buka dropdown Modified By
24. Verifikasi daftar opsi Modified By memuat admin Partner Beta `Admin Beta {runId}-016`
25. Verifikasi daftar opsi Modified By tidak memuat `Admin Gamma {runId}-016`
26. Tutup dropdown Modified By, lalu buka dropdown Object
27. Verifikasi daftar opsi Object memuat `Client`
28. Verifikasi daftar opsi Object tidak memuat `Distributor` dan `Brand`
29. Tutup dropdown Object dan Filter Panel

## Notes

- Sumber TC: `admin-console/activity-log/TestCases/tc-activity-log.md` (TC-AC-ACAL-40, 41, 43).
- Perbandingan jumlah TC-AC-ACAL-40 memakai pembacaan jumlah total pada saat yang sama lewat sesi API Total Control Alfa, bukan sesi UI kedua: login UI Total Control Alfa menambah baris Session dan membuat jumlah kedua pengamat tidak sebanding. Jumlah dibandingkan relatif satu sama lain (selisih nol), bukan angka absolut (S-12).
- Langkah penghubung (tanpa awalan `Verifikasi`): ganti akun (langkah 7 dan 16), membuka menu dan tab (langkah 2, 8, 12, 17, 22), mengetik dan menutup Search (langkah 9, 11, 13, 15), serta membuka dan menutup dropdown dan Filter Panel (langkah 18, 21, 23, 26, 29). Langkah 1, 3, dan 4 mencatat atau membaca jumlah sebagai baseline pembanding.
- Asersi tambahan di luar Expected TC (S-03): langkah 19, 24, dan 27 membuktikan opsi pembanding pada dropdown yang sama sudah tampil sebelum asersi absence opsi (bagian 8b butir 2).
- Batas asersi "hanya" (TC-AC-ACAL-43 Expected "hanya dari baris log dalam scope Partner Beta"): diperiksa dengan sampel, yaitu opsi bernama (`Staf Alfa {runId}-016`, `Staf Gamma {runId}-016`, `Staf Principal {runId}-016`, `Admin Gamma {runId}-016`, `Distributor`, `Brand`) yang tidak boleh ada; bukan seluruh isi daftar opsi, sehingga opsi lain di luar sampel tidak diasersi.
- Pembagian TC lintas spec: tidak ada TC yang terbelah.
- Temuan untuk QA:
  - TC-AC-ACAL-40 langkah 3 "Bandingkan dengan Total Control (Distributor Alfa)" tidak menyebut cara membaca jumlah pembanding; spec memakai pembacaan lewat sesi API aktor (kemampuan disediakan tim FE/BE).
  - TC-AC-ACAL-41 dan 43 tidak menyebut nilai IP Address, Employee ID, Device / Browser, Old Value, dan New Value yang di-seed, serta nama pelaku; spec memakai nilai bersuffix dari seed (Pre-setup No 9, 10 tanpa nilai kolom). Opsi dropdown User dan Modified By dalam nama lengkap atau singkatan tidak dinyatakan TC; spec mengikuti nama lengkap, QA konfirmasi.
  - TC-AC-ACAL-43 Expected b "hanya dari baris log dalam scope Partner Beta" tidak menyebut daftar Object yang diharapkan; spec memverifikasi `Client` ada serta `Distributor` dan `Brand` tidak ada.
  - Email Pre-setup memakai placeholder `{namaCompany}`; password: `AC_ALFA_RO_PASSWORD`, `AC_BETA_RO_PASSWORD`, `AC_BETA_TC_PASSWORD`, `AC_ALFA_TC_PASSWORD`, `AC_DYN_PASSWORD` adalah nama usulan tim FE dan belum terdaftar di `.env.example` maupun `spectra.config.ts`.
