---
id: TC-FA-PREF-E2E-157-shimmer-pratinjau-d01-save-tetap-enabled
title: "Shimmer pratinjau dampak dialog D-01: tombol Save tetap Enabled saat hitungan dimuat"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-204
  - TC-FA-PREF-597
coverage:
  web: automated
---

# Shimmer pratinjau dampak dialog D-01: tombol Save tetap Enabled saat hitungan dimuat

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PA-4), email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi` (PA-1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data awal blok TC-FA-PREF-204 (seed di hook `before`): Preferences company dalam nilai awal (PB-1: Default Capitalization Threshold 5.000.000); akun Chart of Accounts tersedia (PB-2); Asset Class IT Equipment, Vehicles, Furniture tersedia (PB-3).
- Data awal blok TC-FA-PREF-597 (seed lewat API oleh langkah penghubung): Preferences dalam nilai awal (PC-1: Default Capitalization Threshold 5.000.000); Asset Class Vehicles dan Furniture tidak mengisi threshold sendiri (PC-6). Seri fixture PB dan PC berbeda pada Asset Class sehingga seed diulang di antara kedua blok.
- Menahan respons: `Spectra.intercept()` di atas backend nyata menahan respons permintaan hitungan dampak (PV-01) hanya untuk mengamati state Loading, lalu melepasnya dalam spec; endpoint ditentukan tim FE dari kebutuhan permintaan halaman. Intercept dilepas di hook `after` bila spec berhenti di tengah.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-204: Area pratinjau D-01 menampilkan Shimmer dan Save tetap dapat diklik

1. Tunda respons permintaan hitungan dampak selama beberapa detik (intercept jaringan)
2. Ketik 10000000 pada CurrencyInput Default Capitalization Threshold
3. Klik `[Save changes]`
4. Verifikasi area pratinjau dampak pada dialog D-01 menampilkan Shimmer (loading component)
5. Verifikasi tombol `[Save]` pada dialog D-01 berstatus Enabled selama Shimmer tampil
6. Klik `[Save]` pada dialog D-01 selagi hitungan belum selesai
7. Verifikasi dialog D-01 tertutup
8. Verifikasi toast "Success, accounting preferences have been saved." tampil
9. Verifikasi toast tampil di kanan bawah layar
10. Lepas tahanan respons permintaan hitungan dampak

### TC-FA-PREF-597: Save pada dialog Save Changes tetap Enabled saat hitungan dimuat

11. Seed ulang Preferences company ke PC-1 dan Asset Class PC-6 lewat API lalu buka ulang Fixed Asset > Settings > Accounting > Preferences
12. Ubah Default Capitalization Threshold menjadi "10000000"
13. Tunda respons hitungan dampak pada alat intercept jaringan
14. Klik `[Save changes]`
15. Verifikasi area pratinjau dampak pada dialog Save Changes menampilkan Shimmer
16. Verifikasi tombol `[Save]` Enabled
17. Klik `[Save]`
18. Verifikasi toast "Success, accounting preferences have been saved." tampil
19. Lepas tahanan respons hitungan dampak

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Menahan respons di sini hanya untuk mengamati state Loading dan bukan fault injection (bagian 3, prinsip 13b).
- Langkah penghubung (S-03): langkah 10 dan 19 (melepas tahanan respons); langkah 11 (seed ulang PC-1 dan PC-6 serta buka ulang halaman, memulihkan Default Capitalization Threshold ke 5.000.000 dari hasil Save blok sebelumnya, S-09).
- Pembagian TC lintas spec: TC-FA-PREF-73 dan TC-FA-PREF-295 (Shimmer form dan modal Changelog) ada di spec 014.
- Temuan untuk QA:
  - TC-FA-PREF-204 Post Condition ("Preferences company menyimpan Default Capitalization Threshold = 10.000.000") dan TC-FA-PREF-597 Post Condition ("Default Capitalization Threshold tersimpan 10.000.000") tidak punya langkah observasi di TC sehingga tidak diasersi (S-01).
  - TC-FA-PREF-204 memakai nilai "10000000" pada langkah dan "10.000.000" pada Data Uji; spec mengetik "10000000" mengikuti Langkah Uji.
  - TC-FA-PREF-204 dan TC-FA-PREF-597 tidak menyebut nama env var password; nama `FA_TC_PASSWORD` diusulkan spec dan perlu keputusan tim.
