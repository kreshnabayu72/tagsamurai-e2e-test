---
id: TC-FA-SU-E2E-049-default-checkbox-switch-on-pertama-dan-indikator-loading-switch
title: "Default Checkbox Switch ON Pertama dan Indikator Loading Switch"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-166
  - TC-FA-SU-172
coverage:
  web: automated
---

# Default Checkbox Switch ON Pertama dan Indikator Loading Switch

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: lihat `suite.md` (flag Guided Tooltip `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup (Client `FaUserMain`, #20; penugasan #23): target Gita Permata dengan Global Role Manage global license dan Manage asset ID configuration OFF tanpa nilai tersimpan. Seed API memulihkan keadaan ini di hook `before` dan `after` (Catatan TC).
- Kemampuan teknis (disediakan tim FE/BE): `Spectra.intercept()` untuk menunda respons request switch 3 detik (hanya untuk mengamati loading, bukan kegagalan; bagian 3 prinsip 13b), dilepas segera setelah pengamatan (S-09); pencatat request jaringan untuk menghitung jumlah request ubah switch yang terkirim (langkah 10).
- State global dan pemulihan: penugasan Global Role Gita berubah (Manage global license dan Manage asset ID configuration ON) dan dipulihkan lewat seed API di hook `after`; entri log Assign bertambah permanen (audit trail). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-166: Default checkbox saat switch ON pertama kali

1. Ketik Search `Gita`, tekan Enter di User List, klik nama Gita Permata, lalu buka Tab Role > Sub-tab Global Role
2. Nyalakan switch pada baris Manage global license
3. Verifikasi sel Create dan Delete baris Manage global license tampil `—`
4. Verifikasi checkbox Read baris Manage global license tercentang dan Disabled
5. Verifikasi checkbox Update baris Manage global license tidak tercentang

### TC-FA-SU-172: Indikator loading mini pada switch

6. Tunda respons request switch Global Role selama 3 detik (`Spectra.intercept()`)
7. Nyalakan switch pada baris Manage asset ID configuration
8. Verifikasi switch Manage asset ID configuration menampilkan indikator loading mini
9. Klik switch Manage asset ID configuration kedua kalinya selama request berjalan
10. Verifikasi switch tidak dapat diklik ulang: hanya satu request ubah switch yang terkirim
11. Tunggu respons dilepas setelah 3 detik
12. Verifikasi switch Manage asset ID configuration berpindah ke posisi ON
13. Verifikasi indikator loading mini pada switch hilang

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Langkah penghubung tanpa awalan `Verifikasi`: langkah 1 (Search untuk menemukan baris target, R-16), langkah 6 dan 11 (menunda dan melepas respons).
- Asersi tambahan di luar Expected TC: langkah 10 menerjemahkan "tidak dapat diklik ulang" lewat jumlah request ubah switch yang terkirim (pencatat request jaringan tercantum di Kemampuan teknis, disediakan tim FE/BE).
- Temuan untuk QA:
  - Expected a TC-FA-SU-166 menyebut "role dengan dimensi C/R/U/D lengkap: R tercentang Disabled, C/U/D tidak tercentang", tetapi Langkah Uji hanya menyalakan Manage global license (dimensi terbatas) dan Pre-setup #23 tidak menyebut role berdimensi lengkap berstatus OFF tanpa nilai tersimpan. Spec hanya mengasersi butir b (langkah 3 sampai 5); butir a tidak punya data uji.
  - Post Condition TC-FA-SU-172 ("satu entri `Assign` tercatat pada tiga permukaan log") tidak punya langkah observasi di TC dan tidak diasersi (S-01).
  - Expected b TC-FA-SU-172 menyebut "switch Disabled sesaat" pada judul sementara Expected a menyebut "tidak dapat diklik ulang"; spec mengasersi tidak dapat diklik ulang.
