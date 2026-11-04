---
id: TC-FA-PREF-E2E-163-periode-dibuka-kembali-kunci-terbuka-atau-tetap-terkunci
title: "Periode yang Dibuka Kembali: Kunci Terbuka Tanpa Posting Penyusutan dan Tetap Terkunci Bila Posting Sudah Ada"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-603
  - TC-FA-PREF-604
coverage:
  web: automated
---

# Periode yang Dibuka Kembali: Kunci Terbuka Tanpa Posting Penyusutan dan Tetap Terkunci Bila Posting Sudah Ada

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup, company `PT Contoh Konstruksi`): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences). Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup PC-2 (varian kunci): periode Mar 2026 pernah Soft Closed lalu dibuka kembali menjadi Open; TC-603 tanpa posting penyusutan, TC-604 dengan posting penyusutan pertama (Asset Class IT Equipment memiliki Last Posted Period); seluruh periode lain Open. Dibentuk lewat seed API pada awal tiap TC.
- Seed dan pemulihan lewat API (Preferences ke nilai awal, Asset Class, pelepasan, akun Chart of Accounts, penguncian) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`); tiap TC dijalankan dari keadaan awal yang dinyatakan di Precondition TC-nya.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama akun dan Asset Class ditulis seperti di TC.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Hook `after` memulihkan kunci dan periode ke keadaan awal PC-1 lewat seed API (tetap jalan bila spec gagal di tengah); langkah 14 melakukan pemulihan yang sama di akhir spec.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-603: Periode yang dibuka kembali tanpa posting penyusutan membuat kedua field terbuka kembali

1. Seed periode Mar 2026 pernah Soft Closed lalu dibuka kembali tanpa posting penyusutan (PC-2) lewat API, lalu muat ulang halaman dengan F5
2. Verifikasi Select Fiscal Year Start dan Select First Accounting Period berstatus Enabled
3. Verifikasi tidak ada ikon gembok pada Select Fiscal Year Start dan Select First Accounting Period
4. Arahkan kursor ke Select Fiscal Year Start
5. Verifikasi tidak ada tooltip kunci pada Select Fiscal Year Start
6. Arahkan kursor ke Select bulan First Accounting Period
7. Verifikasi tidak ada tooltip kunci pada Select bulan First Accounting Period

### TC-FA-PREF-604: Periode yang dibuka kembali tetap mengunci kedua field bila posting penyusutan sudah ada

8. Seed posting penyusutan pertama pada varian PC-2 lewat API, lalu muat ulang halaman dengan F5
9. Verifikasi Select Fiscal Year Start dan Select First Accounting Period tampil Disabled dengan ikon gembok
10. Arahkan kursor ke Select Fiscal Year Start
11. Verifikasi tooltip Fiscal Year Start "Fiscal year start is locked because depreciation has been posted or a period has been closed. It cannot be changed from this page."
12. Arahkan kursor ke Select First Accounting Period
13. Verifikasi tooltip First Accounting Period "First accounting period is locked because depreciation has been posted or a period has been closed. It cannot be changed from this page."
14. Pulihkan kunci dan periode ke keadaan awal PC-1 lewat seed API

## Notes

- Langkah penghubung (S-03): seed varian PC-2 tiap TC; langkah 14 (pemulihan kunci dan periode ke keadaan awal PC-1 lewat seed API, tanpa Verifikasi); hover pada TC-603 (langkah 4 dan 6) melengkapi asersi absence tooltip; tiap hover diikuti satu `Verifikasi` absence tooltip pada Select yang sama (langkah 5 dan 7).
- TC-241 (seri PB-7d) ada di spec 068; TC-603 memakai seri PC-2.
- Temuan untuk QA:
  - Post Condition TC-603 dan TC-604 "-"; tidak ada yang diasersi tambahan.
  - TC-603 Expected b "tidak ada tooltip kunci" tidak memuat langkah hover; spec menambah hover sebagai langkah penghubung.
