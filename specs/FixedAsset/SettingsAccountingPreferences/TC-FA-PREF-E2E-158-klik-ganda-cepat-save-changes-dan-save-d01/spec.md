---
id: TC-FA-PREF-E2E-158-klik-ganda-cepat-save-changes-dan-save-d01
title: "Klik ganda cepat pada [Save changes] dan [Save] di D-01 hanya mengirim satu permintaan Save"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-285
  - TC-FA-PREF-286
sourceRules: ["R-01c", "T-01", "L-02e", "§4.1.4#p1"]
smoke: []
dependsOn: []
trace:
  "R-01c": [7, 8, 22, 23]
  "T-01": [8, 23]
  "L-02e": [11, 26]
  "§4.1.4#p1": [12, 27]
anchor: [9, 24]
coverage:
  web: automated
---

# Klik ganda cepat pada [Save changes] dan [Save] di D-01 hanya mengirim satu permintaan Save

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PA-4), email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi` (PA-1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data awal blok TC-FA-PREF-285 (seed di hook `before`): Preferences company dalam nilai awal PB-1 (In-service Date Source Activation date); akun Chart of Accounts tersedia (PB-2). Changelog Preferences berisi entri Create (PB-1); jumlah baris dibaca sebagai baseline sebelum aksi dan tidak diasumsikan dari seed (S-12).
- Data blok TC-FA-PREF-286 (seed lewat API oleh langkah penghubung): Preferences company dalam nilai awal PB-1 (Default Capitalization Threshold 5.000.000); Asset Class IT Equipment, Vehicles, Furniture tersedia (PB-3). Hook `after` memulihkan Preferences ke PA-2 (nilai awal setara).
- Klik ganda: dua klik beruntun dengan jeda kurang dari 200 milidetik; `Spectra.intercept()` di atas backend nyata menahan respons Save Preferences dan menghitung permintaan Save yang terkirim; endpoint ditentukan tim FE dari kebutuhan permintaan halaman. Intercept dilepas di hook `after` bila spec berhenti di tengah. Menahan respons hanya untuk mengamati jumlah permintaan dan bukan fault injection.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-285: Klik ganda cepat pada [Save changes]

1. Klik ikon View history lalu catat jumlah baris pada modal Changelog (baseline N)
2. Tutup modal Changelog
3. Tunda respons permintaan Save Preferences selama beberapa detik (intercept jaringan) dan hitung permintaan yang terkirim
4. Ubah Select In-service Date Source dari "Activation date" menjadi "Manual by Accounting"
5. Klik `[Save changes]` dua kali dengan jeda kurang dari 200 milidetik
6. Lepas tahanan respons dan tunggu respons diterima
7. Verifikasi hanya satu permintaan Save terkirim
8. Verifikasi toast "Success, accounting preferences have been saved." tampil satu kali
9. Verifikasi toast tampil di kanan bawah layar
10. Klik ikon View history
11. Verifikasi jumlah baris pada modal Changelog bertambah satu dari baseline N
12. Verifikasi baris Edit In-service Date Source tampil sebagai baris teratas
13. Tutup modal Changelog

### TC-FA-PREF-286: Klik ganda cepat pada [Save] di D-01

14. Seed ulang Preferences company ke PB-1 lewat API lalu buka ulang Fixed Asset > Settings > Accounting > Preferences
15. Klik ikon View history lalu catat jumlah baris pada modal Changelog (baseline M)
16. Tutup modal Changelog
17. Tunda respons permintaan Save Preferences selama beberapa detik (intercept jaringan) dan hitung permintaan yang terkirim
18. Ketik 10000000 pada CurrencyInput Default Capitalization Threshold
19. Klik `[Save changes]`
20. Klik `[Save]` pada dialog D-01 dua kali dengan jeda kurang dari 200 milidetik
21. Lepas tahanan respons dan tunggu respons diterima
22. Verifikasi hanya satu permintaan Save terkirim
23. Verifikasi toast "Success, accounting preferences have been saved." tampil satu kali
24. Verifikasi toast tampil di kanan bawah layar
25. Klik ikon View history
26. Verifikasi jumlah baris pada modal Changelog bertambah satu dari baseline M
27. Verifikasi baris Edit Default Capitalization Threshold tampil sebagai baris teratas
28. Tutup modal Changelog

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 2, 13, 16, dan 28 (menutup modal Changelog); langkah 6 dan 21 (melepas tahanan respons); langkah 14 (seed ulang PB-1 dan buka ulang halaman).
- Expected TC menulis "Modal Changelog berisi 2 baris (1 baris Create dan 1 baris Edit ...)" sebagai angka absolut; karena Changelog adalah audit trail permanen, spec mengasersi selisih satu baris terhadap baseline dan baris Edit teratas pada urutan default Date terbaru (S-12, S-14).
- TC-FA-PREF-89, 283 (Save tanpa D-01) ada di spec 019; TC-FA-PREF-90, 284 (Save pada D-01) ada di spec 020.
- Temuan untuk QA:
  - TC-FA-PREF-285 dan TC-FA-PREF-286 Expected butir c menulis jumlah baris Changelog absolut ("2 baris"); spec memakai selisih terhadap baseline (S-12) dan perlu konfirmasi bahwa seed PB-1 selalu menyisakan tepat satu entri Create.
  - TC-FA-PREF-285 Expected butir b menulis "tampil di kanan bawah layar tampil satu kali" (kalimat rancu); spec memecahnya menjadi dua `Verifikasi`.
  - TC-FA-PREF-285 dan TC-FA-PREF-286 Post Condition ("tepat satu entri log Edit") sepadan dengan Expected butir c dan tidak diasersi terpisah.
  - TC-FA-PREF-285 dan TC-FA-PREF-286 tidak menyebut nama env var password; nama `FA_TC_PASSWORD` diusulkan spec dan perlu keputusan tim.
