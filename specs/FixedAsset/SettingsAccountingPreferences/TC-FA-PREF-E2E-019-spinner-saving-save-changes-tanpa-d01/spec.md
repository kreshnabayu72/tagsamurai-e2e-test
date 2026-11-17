---
id: TC-FA-PREF-E2E-019-spinner-saving-save-changes-tanpa-d01
title: "Spinner Saving pada [Save changes] saat Save tanpa dialog D-01 diproses"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-89
  - TC-FA-PREF-283
sourceRules: ["ST-02", "T-01", "F-FAPREF-01.k22b"]
smoke: []
dependsOn: []
trace:
  "ST-02": [4, 5, 12, 13]
  "T-01": [7, 19]
  "F-FAPREF-01.k22b": 16
anchor: [14, 15, 17, 20]
coverage:
  web: automated
---

# Spinner Saving pada [Save changes] saat Save tanpa dialog D-01 diproses

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PA-4), email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi` (PA-1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data awal blok TC-FA-PREF-89 (seed di hook `before`): Preferences company sesuai PA-2 (In-service Date Source Activation date; nilai awal, tidak terkunci, semua setting wajib terisi).
- Data blok TC-FA-PREF-283 (seed lewat API oleh langkah penghubung): Preferences company dalam nilai awal PB-1; akun Chart of Accounts tersedia (PB-2). Nilai awal PA-2 dan PB-1 setara; seed ulang mengembalikan In-service Date Source ke Activation date setelah Save blok sebelumnya. Hook `after` memulihkan Preferences ke PA-2.
- Menahan respons: `Spectra.intercept()` di atas backend nyata menahan respons Save Preferences hanya untuk mengamati state Saving, lalu melepasnya dalam spec; endpoint ditentukan tim FE dari kebutuhan permintaan halaman. Intercept dilepas di hook `after` bila spec berhenti di tengah.
- Kemampuan baca BE (disediakan tim FE/BE): nilai tersimpan Preferences company, dipakai TC-FA-PREF-283 untuk Expected butir b.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-89: Spinner dan non-interaktif saat Save tanpa dialog sedang diproses

1. Ubah In-service Date Source menjadi "Manual by Accounting"
2. Tahan (delay) response simpan
3. Klik `[Save changes]`
4. Verifikasi `[Save changes]` menampilkan spinner selama response belum kembali
5. Verifikasi `[Save changes]` non-interaktif selama response belum kembali
6. Lepaskan response simpan
7. Verifikasi toast sukses "Success, accounting preferences have been saved." tampil

### TC-FA-PREF-283: State Saving dan hasil baru tampil setelah respons

8. Seed ulang Preferences company ke PB-1 lewat API lalu buka ulang Fixed Asset > Settings > Accounting > Preferences
9. Tunda respons permintaan Save Preferences selama beberapa detik (intercept jaringan)
10. Ubah Select In-service Date Source dari "Activation date" menjadi "Manual by Accounting"
11. Klik `[Save changes]`
12. Verifikasi `[Save changes]` menampilkan spinner
13. Verifikasi `[Save changes]` tidak dapat diklik
14. Verifikasi `[Cancel]` tidak dapat diklik
15. Verifikasi kontrol input tidak dapat diubah
16. Verifikasi tidak ada toast sukses selama respons belum diterima
17. Verifikasi Preferences company belum menyimpan "Manual by Accounting" sebagai nilai In-service Date Source
18. Lepas tahanan respons Save Preferences dan tunggu respons diterima
19. Verifikasi toast "Success, accounting preferences have been saved." tampil
20. Verifikasi toast tampil di kanan bawah layar

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Menahan respons di sini hanya untuk mengamati state Saving dan bukan fault injection (bagian 3, prinsip 13b).
- Langkah penghubung (S-03): langkah 6 dan 18 (melepas tahanan respons); langkah 8 (seed ulang PB-1 dan buka ulang halaman).
- Asersi absence toast (langkah 16) diletakkan segera setelah pemicu dengan spinner sebagai anchor positif (8b butir 11).
- TC-FA-PREF-285 dan TC-FA-PREF-286 (klik ganda cepat) ada di spec 158; TC-FA-PREF-90 dan TC-FA-PREF-284 (Save pada dialog D-01) ada di spec 020.
- Temuan untuk QA:
  - TC-FA-PREF-89 Post Condition a ("In-service Date Source tersimpan "Manual by Accounting"") tidak punya langkah observasi di TC sehingga tidak diasersi (S-01); TC-FA-PREF-283 Post Condition sepadan dengan Expected c dan tidak diasersi terpisah.
  - TC-FA-PREF-89 tidak menyebut cara membaca "nilai tersimpan" dan TC-FA-PREF-283 Expected b meminta nilai tersimpan belum berubah; spec memakai kemampuan baca BE yang disediakan tim FE/BE.
  - TC-FA-PREF-89 dan TC-FA-PREF-283 tidak menyebut nama env var password; nama `FA_TC_PASSWORD` diusulkan spec dan perlu keputusan tim.
