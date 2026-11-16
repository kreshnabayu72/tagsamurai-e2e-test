---
id: TC-FA-PREF-E2E-082-defense-in-depth-setting-wajib-kosong-ditolak-dan-found-asset-credit-account-tanpa-filter-function-diterima
title: "Defense-in-Depth: Setting Wajib Kosong Ditolak Server Lewat Request Langsung dan Found Asset Credit Account Active Tanpa Filter Function Diterima"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-531
  - TC-FA-PREF-532
  - TC-FA-PREF-533
  - TC-FA-PREF-534
  - TC-FA-PREF-535
  - TC-FA-PREF-541
sourceRules: ["V-01", "E-FAPREF-02", "RG-02", "E-FAPREF-40", "V-04", "FAPREF-LOGIC-08e"]
smoke: []
dependsOn: []
trace:
  "V-01": [3, 8, 13, 18, 23]
  "E-FAPREF-02": [5, 10, 15, 20, 25]
  "RG-02": [6, 11, 16, 21, 26]
  "E-FAPREF-40": 28
  "V-04": 28
  "FAPREF-LOGIC-08e": 30
coverage:
  web: automated
---

# Defense-in-Depth: Setting Wajib Kosong Ditolak Server Lewat Request Langsung dan Found Asset Credit Account Active Tanpa Filter Function Diterima

## Prerequisites

- Mode: FE+BE.
- Akun aktor UI dan sesi API: Total Control "Rina Anggraini" `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Request langsung dan pembacaan ulang memakai sesi API aktor yang sama (butir "Sesi API aktor" di `suite.md`).
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: PC-1 (seluruh setting tersimpan pada nilai awal; Found Asset Credit Account tersimpan kosong) dan PC-5 (akun `4-9100 – Laba Pelepasan Aset` berstatus Active dengan function Gain on Disposal).
- Kemampuan teknis: kirim request langsung ke endpoint Save Preferences dengan klien HTTP dan baca jumlah baris Changelog, System Log, dan Activity Log FAMS (N dibaca sebelum aksi, bagian 8b butir 10). Disediakan tim FE/BE tanpa endpoint karangan (S-13).
- Seed dan pemulihan Preferences lewat API: lihat butir "Seed dan pemulihan lewat API" di `suite.md`. TC-541 menyimpan Found Asset Credit Account `4-9100 – Laba Pelepasan Aset`; pemulihan ke nilai awal (kosong) dilakukan di hook `after` spec ini.
- Flag Guided Tooltip halaman Preferences: lihat butir "Flag Guided Tooltip" di `suite.md`.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Catat jumlah baris Changelog, System Log, dan Activity Log FAMS

### TC-FA-PREF-531: Request langsung dengan Fiscal Year Start kosong ditolak server

2. Kirim request langsung Save Preferences menggunakan sesi Total Control Rina Anggraini dengan Fiscal Year Start kosong
3. Verifikasi server menolak permintaan dengan pesan "Fiscal year start must not be empty"
4. Baca ulang nilai Preferences tersimpan dan hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
5. Verifikasi nilai Preferences tersimpan tidak berubah: Fiscal Year Start tidak kosong
6. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal

### TC-FA-PREF-532: Request langsung dengan Default Capitalization Threshold kosong ditolak server

7. Kirim request langsung Save Preferences menggunakan sesi Total Control Rina Anggraini dengan Default Capitalization Threshold kosong
8. Verifikasi server menolak permintaan dengan pesan "Default capitalization threshold must not be empty"
9. Baca ulang nilai Preferences tersimpan dan hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
10. Verifikasi nilai Preferences tersimpan tidak berubah: Default Capitalization Threshold tidak kosong
11. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal

### TC-FA-PREF-533: Request langsung dengan In-service Date Source kosong ditolak server

12. Kirim request langsung Save Preferences menggunakan sesi Total Control Rina Anggraini dengan In-service Date Source kosong
13. Verifikasi server menolak permintaan dengan pesan "In-service date source must not be empty"
14. Baca ulang nilai Preferences tersimpan dan hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
15. Verifikasi nilai Preferences tersimpan tidak berubah: In-service Date Source tidak kosong
16. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal

### TC-FA-PREF-534: Request langsung dengan Depreciation in Disposal Month kosong ditolak server

17. Kirim request langsung Save Preferences menggunakan sesi Total Control Rina Anggraini dengan Depreciation in Disposal Month kosong
18. Verifikasi server menolak permintaan dengan pesan "Depreciation in disposal month must not be empty"
19. Baca ulang nilai Preferences tersimpan dan hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
20. Verifikasi nilai Preferences tersimpan tidak berubah: Depreciation in Disposal Month tidak kosong
21. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal

### TC-FA-PREF-535: Request langsung dengan First Accounting Period kosong ditolak server

22. Kirim request langsung Save Preferences menggunakan sesi Total Control Rina Anggraini dengan First Accounting Period kosong
23. Verifikasi server menolak permintaan dengan pesan "First accounting period must not be empty"
24. Baca ulang nilai Preferences tersimpan dan hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
25. Verifikasi nilai Preferences tersimpan tidak berubah: First Accounting Period tidak kosong
26. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal

### TC-FA-PREF-541: Request langsung Found Asset Credit Account dengan akun Active tanpa filter function diterima server

27. Kirim request langsung Save Preferences menggunakan sesi Total Control Rina Anggraini, mengisi Found Asset Credit Account dengan akun 4-9100 – Laba Pelepasan Aset
28. Verifikasi permintaan berhasil
29. Baca ulang nilai Preferences tersimpan
30. Verifikasi Found Asset Credit Account tersimpan 4-9100 – Laba Pelepasan Aset

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Pengecualian K-1: spec defense-in-depth (kelas a) dengan Expected respons API. Request langsung tidak melewati browser; asersi penolakan dan penerimaan ada pada langkah Verifikasi respons.
- Baseline log (langkah 1) dicatat sekali; penolakan tidak mengubah jumlah baris log sehingga hitung ulang tiap TC dibandingkan dengan jumlah awal yang sama (S-12). TC-541 ditaruh paling akhir karena menyimpan perubahan; Precondition TC-541 tidak mencatat baseline log dan Expected tidak meminta asersi log.
- Post Condition TC-531 sampai 535 ("... tersimpan tidak berubah dan tidak kosong") dicakup Expected butir b dan diasersi pada langkah nilai tersimpan dan jumlah baris log. Nilai tersimpan tidak kosong diasersi tanpa nilai literal karena TC tidak menyebutnya.
- Temuan untuk QA:
  - TC-FA-PREF-531 sampai 535 tidak menyebut nilai tersimpan yang diharapkan (hanya "tidak berubah dan tidak kosong"); spec mengasersi sesuai itu.
  - TC-FA-PREF-541 menyebut Found Asset Credit Account tanpa filter function, sementara TC-FA-PREF-539 menolak Default Capitalization Offset ber-function Gain on Disposal; perbedaan filter antar-setting perlu dikonfirmasi terhadap PRD (FAPREF-LOGIC-08e).
  - TC-FA-PREF-541 tidak meminta pencatatan log atau asersi log setelah penyimpanan berhasil.
