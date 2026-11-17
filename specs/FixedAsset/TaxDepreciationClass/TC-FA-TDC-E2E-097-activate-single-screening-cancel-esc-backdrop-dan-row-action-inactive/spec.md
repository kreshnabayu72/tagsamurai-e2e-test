---
id: TC-FA-TDC-E2E-097-activate-single-screening-cancel-esc-backdrop-dan-row-action-inactive
title: "Activate Single: Screening Dialog, Cancel, Esc, Backdrop, dan Row Action Class Inactive"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-361
  - TC-FA-TDC-363
  - TC-FA-TDC-364
  - TC-FA-TDC-365
  - TC-FA-TDC-372
sourceRules: ["FATDC-LOGIC-08h", "D-03", "L-04", "§4.5#b1", "§4.1.1#p3", "FATDC-LOGIC-08g"]
smoke: []
dependsOn: []
trace:
  "FATDC-LOGIC-08h": [3, 7, 16, 22, 25]
  "D-03": 4
  "L-04": [11, 18, 26]
  "§4.5#b1": [15, 25]
  "§4.1.1#p3": 28
  "FATDC-LOGIC-08g": 29
anchor: [6, 8, 10, 17, 21, 23]
coverage:
  web: automated
---

# Activate Single: Screening Dialog, Cancel, Esc, Backdrop, dan Row Action Class Inactive

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (`Fixture.fixedAssetTaxDepreciationClass.exampleData`, disediakan tim FE): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data. Kebutuhan spec ini: NB-OLD berstatus Inactive (toggle Off) dengan Used By 0 dan Last Posted Tax Year kosong, nama "Kelompok khusus lama". Sembilan baris berada dalam satu halaman Pagination (10 baris per halaman), sehingga baris target tidak dicari lewat Search. Semua blok hanya membuka lalu membatalkan dialog; tidak ada data class yang berubah. Class Code dibatasi 15 karakter menurut TC sehingga kode class memakai literal Example Data tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA); hook `before` menyeed ulang kondisi awal lewat API dan hook `after` memulihkannya. Data Dinamis: tidak ada.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seed dan pemulihan class lewat API; kemampuan baca jumlah entri Changelog class NB-OLD untuk field Status (baseline dicatat sebelum aksi dan dibandingkan sesudahnya, 8b.10, S-12); menekan `Esc` dan mengklik backdrop dialog.
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-TDC-361: Screening dialog Activate single dari klik toggle Active Off

1. Catat baseline jumlah entri Changelog class NB-OLD untuk field Status
2. Klik toggle `Active` pada baris NB-OLD
3. Verifikasi toggle `Active` baris NB-OLD tetap Off selama dialog terbuka
4. Verifikasi dialog dengan judul `Activate Tax Depreciation Class` (tanpa tanda tanya), body bullet `• NB-OLD – Kelompok khusus lama` pada baris pertama diikuti kalimat `Are you sure you want to activate it?`, dan footer dua tombol berurutan `[Cancel]` lalu `[Activate]`

### TC-FA-TDC-363: Cancel pada dialog Activate tidak mengubah status

5. Klik `[Cancel]` pada dialog Activate
6. Verifikasi dialog menutup
7. Verifikasi toggle `Active` baris NB-OLD tetap Off
8. Verifikasi tidak ada toast yang tampil
9. Klik ikon Changelog di toolbar
10. Verifikasi modal Changelog menampilkan sedikitnya satu entri
11. Verifikasi jumlah entri Changelog NB-OLD untuk field Status sama dengan baseline langkah 1 (tidak ada entri baru)
12. Tutup modal Changelog

### TC-FA-TDC-364: Tombol Esc menutup dialog Activate setara Cancel

13. Klik toggle `Active` pada baris NB-OLD
14. Tekan tombol `Esc`
15. Verifikasi dialog menutup
16. Verifikasi toggle `Active` baris NB-OLD tetap Off
17. Verifikasi tidak ada toast
18. Verifikasi jumlah entri Changelog NB-OLD untuk field Status sama dengan baseline langkah 1 (tidak ada entri log baru)

### TC-FA-TDC-365: Klik backdrop tidak menutup dialog Activate (D-03)

19. Klik toggle `Active` baris NB-OLD
20. Klik area gelap di luar dialog (backdrop)
21. Verifikasi dialog Activate tetap terbuka
22. Verifikasi toggle `Active` baris NB-OLD tetap Off
23. Verifikasi tidak ada toast
24. Tekan `Esc`
25. Verifikasi dialog menutup tanpa perubahan data (toggle `Active` baris NB-OLD tetap Off)
26. Verifikasi jumlah entri Changelog NB-OLD untuk field Status sama dengan baseline langkah 1 (tidak ada entri log baru)

### TC-FA-TDC-372: Class Inactive tetap memiliki row action Edit dan Delete

27. Klik tombol `⋯` pada baris NB-OLD
28. Verifikasi menu row action memuat `Edit` dan `Delete`
29. Verifikasi menu row action tidak memuat `Activate` maupun `Deactivate`
30. Tekan `Esc` untuk menutup menu

## Notes

- Langkah penghubung (S-03): langkah 12 (menutup modal Changelog) dan langkah 30 (menutup menu row action); langkah 1 (baseline Changelog) dipakai sebagai pembanding langkah 11, 18, dan 26 karena tidak ada aksi yang mengubah log di antara blok (S-12).
- Urutan TC: 361, 363, 364, 365, 372. Dialog Activate dari langkah 2 dipakai sebagai pembuka TC-FA-TDC-363 (langkah 1 TC: klik toggle yang sama; keadaan identik), jadi langkah 5 langsung `[Cancel]`. TC-FA-TDC-372 diletakkan paling akhir karena membaca menu row action baris yang sama tanpa mengubah data.
- Absence "tidak ada toast" pada langkah 8, 17, dan 23 diletakkan segera setelah pemicu; Verifikasi dialog menutup dan keadaan toggle sebelumnya menjadi anchor tabel termuat (8b.2, 8b.11). Absence entri log pada langkah 11 memakai langkah 10 sebagai anchor; langkah 18 dan 26 memakai langkah yang sama sebagai pembanding jumlah (S-12).
- Aktivasi sukses (konfirmasi `[Activate]`, loading, dan toast) ada di spec 241 (TC-FA-TDC-362); Used By dan Post Condition lintas modul ada di spec lain.
- Temuan untuk QA:
  - Email akun Total Control tidak tertulis di TC; nama env password adalah usulan.
  - TC tidak memiliki tabel Data Uji Pre-setup dan Dinamis terpisah; data ditulis di kolom Precondition tiap TC dan disalin ke Prerequisites.
  - Class Code dibatasi 15 karakter, sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal Example Data dan menyeed ulang lewat hook. Perlu konfirmasi QA.
  - TC-FA-TDC-363 Expected c ("tidak memuat entri baru untuk NB-OLD") dan TC-FA-TDC-364, TC-FA-TDC-365 ("tidak ada entri log baru") tidak menyebut pembanding; spec memakai baseline jumlah entri (langkah 1).
  - TC-FA-TDC-365 langkah 1 memuat klaim "→ dialog Activate terbuka" pada langkah aksi; spec menuliskannya sebagai Verifikasi sendiri (R-02).
