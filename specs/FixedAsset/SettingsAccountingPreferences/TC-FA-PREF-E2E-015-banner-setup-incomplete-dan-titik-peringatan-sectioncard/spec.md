---
id: TC-FA-PREF-E2E-015-banner-setup-incomplete-dan-titik-peringatan-sectioncard
title: "Banner Setup Incomplete dan titik peringatan SectionCard: isi, tidak dapat ditutup, tidak tampil bila lengkap"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-76
  - TC-FA-PREF-77
  - TC-FA-PREF-78
  - TC-FA-PREF-79
  - TC-FA-PREF-81
  - TC-FA-PREF-82
sourceRules: ["ST-07", "§4.3#b2", "ST-04", "§4.1.1#p1", "FAPREF-LOGIC-11c", "§9.5#r1"]
smoke: []
dependsOn: []
trace:
  "ST-07": [1, 2, 4, 6, 10]
  "§4.3#b2": 3
  "ST-04": [7, 8, 15]
  "§4.1.1#p1": 12
  "FAPREF-LOGIC-11c": 13
  "§9.5#r1": 14
coverage:
  web: automated
---

# Banner Setup Incomplete dan titik peringatan SectionCard: isi, tidak dapat ditutup, tidak tampil bila lengkap

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PA-4), email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi` (PA-1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data awal (seed di hook `before`): Preferences company sesuai PA-5 (Fiscal Year Start, First Accounting Period, Default Capitalization Threshold, In-service Date Source, dan Depreciation in Disposal Month kosong; setting lain bernilai awal; Journal Grouping Group). Dipakai TC-FA-PREF-76, TC-FA-PREF-78, dan TC-FA-PREF-81.
- Seed berikutnya dijalankan lewat API oleh langkah penghubung: PA-6 (hanya Default Capitalization Threshold kosong; setting lain bernilai awal PA-2) untuk TC-FA-PREF-77; PA-2 (nilai awal, semua setting wajib terisi) untuk TC-FA-PREF-79 dan TC-FA-PREF-82. Hook `after` memulihkan Preferences ke PA-2.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-76: Banner memuat seluruh setting wajib kosong menurut urutan SectionCard

1. Verifikasi Alert severity danger tampil di bawah header tab
2. Verifikasi teks Alert persis "Accounting setup is incomplete: Fiscal Year Start, First Accounting Period, Default Capitalization Threshold, In-service Date Source, Depreciation in Disposal Month. Depreciation and journal export are blocked until completed."
3. Verifikasi kelima setting yang kosong tercantum tanpa dipotong

### TC-FA-PREF-78: Banner tidak dapat ditutup

4. Verifikasi banner tidak memiliki tombol tutup (X)
5. Klik area banner
6. Verifikasi banner tetap tampil setelah diklik

### TC-FA-PREF-81: Titik peringatan pada judul SectionCard dengan setting wajib kosong

7. Verifikasi judul SectionCard General, Capitalization, dan Depreciation menampilkan Badge Standalone Dot severity danger
8. Verifikasi judul SectionCard Disposal, Chart of Accounts, dan Journal Export tidak menampilkan titik peringatan

### TC-FA-PREF-77: Banner hanya memuat satu setting wajib kosong

9. Seed ulang Preferences company ke PA-6 lewat API lalu buka ulang Fixed Asset > Settings > Accounting > Preferences
10. Verifikasi banner tampil dengan teks persis "Accounting setup is incomplete: Default Capitalization Threshold. Depreciation and journal export are blocked until completed."

### TC-FA-PREF-79: Banner tidak tampil bila seluruh setting wajib terisi

11. Seed ulang Preferences company ke PA-2 lewat API lalu buka ulang Fixed Asset > Settings > Accounting > Preferences
12. Verifikasi ikon View history tampil di header tab
13. Verifikasi banner Setup Incomplete tidak tampil (tidak dirender)

### TC-FA-PREF-82: Titik peringatan tidak tampil bila setting wajib terisi

14. Verifikasi judul keenam SectionCard tampil
15. Verifikasi tidak ada titik peringatan pada judul enam SectionCard

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan blok: TC-FA-PREF-78 dan TC-FA-PREF-81 (seed PA-5) mengikuti TC-FA-PREF-76, lalu TC-FA-PREF-77 (PA-6), lalu TC-FA-PREF-79 dan TC-FA-PREF-82 (PA-2), supaya setiap seed dijalankan sekali (S-10).
- Langkah penghubung (S-03): langkah 9 dan 11 (seed ulang Preferences dan buka ulang halaman). Langkah 12 (anchor positif ikon View history untuk absence banner, 8b butir 2) dan langkah 14 (anchor positif judul SectionCard sebelum absence titik peringatan) adalah asersi tambahan di luar Expected TC, dicatat di sini beserta alasannya.
- Expected TC-FA-PREF-76 butir b ("seluruh lima setting tercantum tanpa dipotong") ditulis sebagai `Verifikasi` tersendiri meski teks Alert pada langkah 2 sudah memuatnya (S-01).
- Temuan untuk QA:
  - TC-FA-PREF-76, 77, 78, 79, 81, dan 82 tidak menyebut nama env var password; nama `FA_TC_PASSWORD` diusulkan spec dan perlu keputusan tim.
