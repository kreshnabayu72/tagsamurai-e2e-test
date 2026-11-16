---
id: TC-FA-PREF-E2E-081-defense-in-depth-default-capitalization-threshold-negatif-17-digit-3-desimal-lewat-request-langsung
title: "Defense-in-Depth: Default Capitalization Threshold Negatif, 17 Digit, dan 3 Desimal Ditolak Server Lewat Request Langsung"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-233
  - TC-FA-PREF-234
  - TC-FA-PREF-235
  - TC-FA-PREF-526
  - TC-FA-PREF-527
  - TC-FA-PREF-528
sourceRules: ["V-02", "E-FAPREF-03", "RG-02", "V-03"]
smoke: []
dependsOn: []
trace:
  "V-02": [3, 19]
  "E-FAPREF-03": [5, 10, 15, 21, 26, 31]
  "RG-02": [6, 11, 16, 22, 27, 32]
  "V-03": [8, 13, 24, 29]
coverage:
  web: automated
---

# Defense-in-Depth: Default Capitalization Threshold Negatif, 17 Digit, dan 3 Desimal Ditolak Server Lewat Request Langsung

## Prerequisites

- Mode: FE+BE.
- Akun aktor UI dan sesi API: Total Control "Rina Anggraini" `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Request langsung dan pembacaan ulang memakai sesi API aktor yang sama (butir "Sesi API aktor" di `suite.md`).
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: TC-233 sampai 235 memakai PB-1 (Default Capitalization Threshold tersimpan 5.000.000) dan PB-2; TC-526 sampai 528 memakai PC-1 dan PC-6 (Default Capitalization Threshold tersimpan 5.000.000). Nilai awal PB-1 dan PC-1 setara.
- Kemampuan teknis: kirim request langsung ke endpoint Save Preferences dengan klien HTTP dan baca jumlah baris Changelog, System Log, dan Activity Log FAMS (N dibaca sebelum aksi, bagian 8b butir 10). Disediakan tim FE/BE tanpa endpoint karangan (S-13).
- Seed dan pemulihan Preferences lewat API: lihat butir "Seed dan pemulihan lewat API" di `suite.md`. Spec ini tidak menyimpan perubahan; seed ulang hanya untuk berpindah seri fixture dari PB-1 ke PC-1.
- Flag Guided Tooltip halaman Preferences: lihat butir "Flag Guided Tooltip" di `suite.md`.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Catat jumlah baris Changelog, System Log, dan Activity Log FAMS

### TC-FA-PREF-233: Permintaan langsung dengan Default Capitalization Threshold negatif ditolak server

2. Kirim permintaan Save Preferences langsung (fixture BE) dengan Default Capitalization Threshold = -1
3. Verifikasi server menolak permintaan dengan pesan "Capitalization threshold must be 0 or more"
4. Baca ulang Preferences dan hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
5. Verifikasi Default Capitalization Threshold tetap Rp 5.000.000,00 pada tab Preferences
6. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal (tidak ada entri log baru)

### TC-FA-PREF-234: Permintaan langsung dengan Default Capitalization Threshold 17 digit bulat ditolak server

7. Kirim permintaan Save Preferences langsung (fixture BE) dengan Default Capitalization Threshold = 10000000000000000 (17 digit bulat)
8. Verifikasi server menolak permintaan dengan pesan "Capitalization threshold is too large"
9. Baca ulang Preferences dan hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
10. Verifikasi Default Capitalization Threshold tetap Rp 5.000.000,00 pada tab Preferences
11. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal (tidak ada entri log baru)

### TC-FA-PREF-235: Permintaan langsung dengan Default Capitalization Threshold 3 desimal ditolak server

12. Kirim permintaan Save Preferences langsung (fixture BE) dengan Default Capitalization Threshold = 100.123
13. Verifikasi server menolak permintaan dengan pesan "Capitalization threshold is too large"
14. Baca ulang Preferences dan hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
15. Verifikasi Default Capitalization Threshold tetap Rp 5.000.000,00 pada tab Preferences
16. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal (tidak ada entri log baru)
17. Seed ulang Preferences ke PC-1 lewat API dan catat jumlah baris Changelog, System Log, dan Activity Log FAMS

### TC-FA-PREF-526: Request langsung Default Capitalization Threshold -1 ditolak server

18. Kirim request langsung Save Preferences menggunakan sesi Total Control Rina Anggraini, mengisi Default Capitalization Threshold -1
19. Verifikasi server menolak permintaan dengan pesan "Capitalization threshold must be 0 or more"
20. Baca ulang nilai Preferences tersimpan dan hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
21. Verifikasi nilai Preferences tersimpan tidak berubah (Default Capitalization Threshold tetap 5.000.000)
22. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal

### TC-FA-PREF-527: Request langsung Default Capitalization Threshold 12345678901234567 ditolak server

23. Kirim request langsung Save Preferences menggunakan sesi Total Control Rina Anggraini, mengisi Default Capitalization Threshold 12345678901234567
24. Verifikasi server menolak permintaan dengan pesan "Capitalization threshold is too large"
25. Baca ulang nilai Preferences tersimpan dan hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
26. Verifikasi nilai Preferences tersimpan tidak berubah (Default Capitalization Threshold tetap 5.000.000)
27. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal

### TC-FA-PREF-528: Request langsung Default Capitalization Threshold (payload API 100.001) ditolak server

28. Kirim request langsung Save Preferences menggunakan sesi Total Control Rina Anggraini, mengisi Default Capitalization Threshold 100.001
29. Verifikasi server menolak permintaan karena lebih dari 2 desimal (V-03)
30. Baca ulang nilai Preferences tersimpan dan hitung ulang jumlah baris Changelog, System Log, dan Activity Log FAMS
31. Verifikasi nilai Preferences tersimpan tidak berubah (Default Capitalization Threshold tetap 5.000.000)
32. Verifikasi jumlah baris ketiga surface sama dengan jumlah awal

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Pengecualian K-1: spec defense-in-depth (kelas a) dengan Expected respons API. Request langsung tidak melewati browser; asersi penolakan ada pada langkah Verifikasi respons.
- Baseline log (langkah 1 dan 17) dicatat sesudah tiap seed dan dipakai sebagai pembanding hitung ulang TC sesudahnya, karena penolakan tidak mengubah jumlah baris log (S-12).
- Langkah penghubung (S-03): langkah 17 (seed ulang saat seri fixture berganti dari PB-1 ke PC-1).
- Post Condition ("Preferences company belum berubah dan tidak ada entri log baru") dicakup Expected butir b dan diasersi pada langkah nilai tersimpan dan jumlah baris log.
- Temuan untuk QA:
  - TC-FA-PREF-235 (payload 100.123, 3 desimal) menyebut pesan "Capitalization threshold is too large" untuk pelanggaran V-03, sedangkan TC-FA-PREF-528 (payload 100.001) hanya menyebut "lebih dari 2 desimal (V-03)" tanpa teks pesan; keduanya menguji kelas yang sama. Pesan "too large" untuk 3 desimal perlu dikonfirmasi terhadap PRD.
  - TC-FA-PREF-526 sampai 528 menyebut "sesi Total Control Rina Anggraini" tanpa menyatakan UI atau API; spec memakai sesi API.
