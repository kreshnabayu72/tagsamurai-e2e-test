---
id: TC-FA-PREF-E2E-020-spinner-saving-save-pada-dialog-d01
title: "Spinner Saving pada [Save] di dialog Save Changes D-01"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-90
  - TC-FA-PREF-284
sourceRules: ["ST-02", "T-01", "D-01", "F-FAPREF-01.k21b"]
smoke: []
dependsOn: []
trace:
  "ST-02": [5, 6, 14, 15]
  "T-01": [8, 17, 20]
  "D-01": [16, 19]
  "F-FAPREF-01.k21b": 19
anchor: [21]
coverage:
  web: automated
---

# Spinner Saving pada [Save] di dialog Save Changes D-01

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PA-4), email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi` (PA-1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data awal blok TC-FA-PREF-90 (seed di hook `before`): Preferences company sesuai PA-2 (Default Capitalization Threshold 5.000.000; nilai awal, tidak terkunci, semua setting wajib terisi); Asset Class sesuai PA-16 (dipakai sebagai precondition, tidak diasersi).
- Data blok TC-FA-PREF-284 (seed lewat API oleh langkah penghubung): Preferences company dalam nilai awal PB-1; akun Chart of Accounts tersedia (PB-2); Asset Class IT Equipment, Vehicles, Furniture tersedia (PB-3). Seed ulang mengembalikan Default Capitalization Threshold ke 5.000.000 setelah Save blok sebelumnya. Hook `after` memulihkan Preferences ke PA-2.
- Menahan respons: `Spectra.intercept()` di atas backend nyata menahan respons Save Preferences hanya untuk mengamati state Saving, lalu melepasnya dalam spec; endpoint ditentukan tim FE dari kebutuhan permintaan halaman. Intercept dilepas di hook `after` bila spec berhenti di tengah.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-90: Tombol Save pada dialog menampilkan spinner dan non-interaktif

1. Ubah Default Capitalization Threshold menjadi "6.000.000"
2. Klik `[Save changes]` sehingga dialog "Save Changes" tampil
3. Tahan (delay) response simpan
4. Klik `[Save]` pada dialog
5. Verifikasi `[Save]` pada dialog menampilkan spinner selama response belum kembali
6. Verifikasi `[Save]` pada dialog non-interaktif selama response belum kembali
7. Lepaskan response simpan
8. Verifikasi toast sukses "Success, accounting preferences have been saved." tampil

### TC-FA-PREF-284: Save pada D-01 diproses, dialog tertutup setelah respons

9. Seed ulang Preferences company ke PB-1 lewat API lalu buka ulang Fixed Asset > Settings > Accounting > Preferences
10. Tunda respons permintaan Save Preferences selama beberapa detik (intercept jaringan)
11. Ketik 10000000 pada CurrencyInput Default Capitalization Threshold
12. Klik `[Save changes]`
13. Klik `[Save]` pada dialog D-01
14. Verifikasi tombol `[Save]` pada D-01 menampilkan spinner selama respons belum diterima
15. Verifikasi tombol `[Save]` pada D-01 tidak dapat diklik
16. Verifikasi dialog D-01 tetap terbuka
17. Verifikasi tidak ada toast sukses selama respons belum diterima
18. Lepas tahanan respons Save Preferences dan tunggu respons diterima
19. Verifikasi dialog D-01 tertutup
20. Verifikasi Toast "Success, accounting preferences have been saved." tampil
21. Verifikasi Toast tampil di kanan bawah layar

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Menahan respons di sini hanya untuk mengamati state Saving dan bukan fault injection (bagian 3, prinsip 13b).
- Langkah penghubung (S-03): langkah 7 dan 18 (melepas tahanan respons); langkah 9 (seed ulang PB-1 dan buka ulang halaman, memulihkan Default Capitalization Threshold ke 5.000.000).
- Asersi absence toast (langkah 17) diletakkan segera setelah pemicu dengan spinner sebagai anchor positif (8b butir 11).
- TC-FA-PREF-285 dan TC-FA-PREF-286 (klik ganda cepat) ada di spec 158; TC-FA-PREF-89 dan TC-FA-PREF-283 (Save tanpa D-01) ada di spec 019.
- Temuan untuk QA:
  - TC-FA-PREF-90 Post Condition a ("Default Capitalization Threshold tersimpan "6.000.000"") dan TC-FA-PREF-284 Post Condition ("menyimpan Default Capitalization Threshold = 10.000.000") tidak punya langkah observasi di TC sehingga tidak diasersi (S-01).
  - TC-FA-PREF-90 dan TC-FA-PREF-284 tidak menyebut nama env var password; nama `FA_TC_PASSWORD` diusulkan spec dan perlu keputusan tim.
