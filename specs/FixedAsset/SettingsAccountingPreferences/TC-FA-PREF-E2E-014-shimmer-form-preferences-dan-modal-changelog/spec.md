---
id: TC-FA-PREF-E2E-014-shimmer-form-preferences-dan-modal-changelog
title: "Shimmer: form Preferences dan modal Changelog saat data dimuat"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-73
  - TC-FA-PREF-295
sourceRules: ["ST-21", "ST-03", "§4.1#r2"]
smoke: []
dependsOn: []
trace:
  "ST-21": [3, 11, 13]
  "ST-03": [4, 6, 7]
  "§4.1#r2": 14
coverage:
  web: automated
---

# Shimmer: form Preferences dan modal Changelog saat data dimuat

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PA-4), email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi` (PA-1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data awal (seed di hook `before`): Preferences company sesuai PA-2 (nilai awal, tidak terkunci, semua setting wajib terisi). Blok TC-FA-PREF-295 memakai Preferences PB-1 dan Changelog Preferences 9 entri contoh (PB-C1; dipakai sebagai precondition, tidak diasersi satu per satu); format tanggal General Settings `dd/MM/yy` 24 jam (PB-1). Seed PB-1 dan PB-C1 dijalankan lewat API oleh langkah penghubung sebelum blok itu; nilai awal PA-2 dan PB-1 setara.
- Menahan respons: `Spectra.intercept()` di atas backend nyata menahan respons pemuatan data Preferences (TC-FA-PREF-73) dan respons data Changelog (TC-FA-PREF-295) hanya untuk mengamati state Loading, lalu melepasnya dalam spec; endpoint ditentukan tim FE dari kebutuhan permintaan halaman. Intercept dilepas di hook `after` bila spec berhenti di tengah.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-73: Form menampilkan Shimmer saat data Preferences dimuat

1. Tahan (delay) response pemuatan data Preferences
2. Buka Tab Preferences
3. Verifikasi form menampilkan Loading component (Shimmer)
4. Verifikasi SectionCard dan nilai setting belum tampil
5. Lepas tahanan response pemuatan data Preferences
6. Verifikasi Shimmer hilang
7. Verifikasi form tampil dengan nilai tersimpan

### TC-FA-PREF-295: Modal Changelog menampilkan Shimmer saat data dimuat

8. Seed ulang Preferences company ke PB-1 dengan Changelog PB-C1 lewat API lalu buka ulang Fixed Asset > Settings > Accounting > Preferences
9. Tunda respons data Changelog selama beberapa detik (intercept jaringan)
10. Klik ikon View history di header tab Preferences
11. Verifikasi area tabel modal menampilkan Shimmer (loading component) selama data belum diterima
12. Lepas tahanan respons data Changelog
13. Verifikasi Shimmer hilang
14. Verifikasi sedikitnya satu baris Changelog tampil
15. Tutup modal Changelog

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Menahan respons di sini hanya untuk mengamati state Loading dan bukan fault injection (bagian 3, prinsip 13b).
- Langkah penghubung (S-03): langkah 8 (seed ulang PB-1 dan PB-C1 serta buka ulang halaman); langkah 5 dan 12 (melepas tahanan respons); langkah 15 (menutup modal Changelog).
- Verifikasi pada langkah 14 membaca "baris Changelog tampil" sebagai sedikitnya satu baris, karena TC tidak menyebut jumlah dan total entri audit trail tidak diasersi sebagai angka absolut (S-12).
- TC-FA-PREF-204 dan TC-FA-PREF-597 (Shimmer pratinjau dampak D-01) ada di spec 157.
- Temuan untuk QA:
  - TC-FA-PREF-73 dan TC-FA-PREF-295 tidak menyebut nama env var password; nama `FA_TC_PASSWORD` diusulkan spec dan perlu keputusan tim.
