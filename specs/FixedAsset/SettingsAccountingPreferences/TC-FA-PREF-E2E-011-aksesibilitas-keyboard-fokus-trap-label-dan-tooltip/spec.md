---
id: TC-FA-PREF-E2E-011-aksesibilitas-keyboard-fokus-trap-label-dan-tooltip
title: "Aksesibilitas: navigasi keyboard, fokus ter-trap dialog D-01 dan modal Changelog, label titik peringatan, tooltip keyboard"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-60
  - TC-FA-PREF-61
  - TC-FA-PREF-62
  - TC-FA-PREF-63
  - TC-FA-PREF-64
  - TC-FA-PREF-65
coverage:
  web: automated
---

# Aksesibilitas: navigasi keyboard, fokus ter-trap dialog D-01 dan modal Changelog, label titik peringatan, tooltip keyboard

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PA-4), email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi` (PA-1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Nama diusulkan karena TC tidak menyebutnya (lihat Temuan untuk QA). Password tidak ditulis di spec atau fixture.
- Data awal (seed di hook `before`): Preferences company sesuai PA-2 (nilai awal, tidak terkunci, semua setting wajib terisi); Asset Class sesuai PA-16 (IT Equipment, Vehicles, Furniture memakai threshold default; dipakai sebagai precondition TC-FA-PREF-61, tidak diasersi); Changelog Preferences terisi data contoh PA-17 (9 entri; dipakai sebagai precondition TC-FA-PREF-62, tidak diasersi).
- Blok TC-FA-PREF-63 dan TC-FA-PREF-64 memakai Preferences sesuai PA-5 (SET-01, SET-02, SET-03, SET-04, dan SET-12 kosong; setting lain bernilai awal); seed PA-5 dijalankan lewat API oleh langkah penghubung sebelum blok itu, dan PA-2 dipulihkan oleh hook `after`.
- Pemakai keyboard dan accessibility tree: kemampuan membaca label aksesibilitas elemen disediakan tim FE.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-60: Navigasi keyboard pada form

1. Tekan Tab berulang dari awal form dan catat urutan fokus
2. Verifikasi fokus berpindah antar elemen interaktif (ikon View history, Select, CurrencyInput, MultiSelect, `[Cancel]`, `[Save changes]` bila Enabled)
3. Verifikasi indikator fokus terlihat pada setiap elemen yang menerima fokus
4. Fokus ke Select Fiscal Year Start lalu tekan Enter
5. Verifikasi Enter membuka daftar opsi Select Fiscal Year Start
6. Tekan Esc
7. Fokus ke Select In-service Date Source lalu tekan Space
8. Verifikasi Space membuka daftar opsi Select In-service Date Source
9. Tekan Esc

### TC-FA-PREF-61: Dialog D-01, fokus ter-trap dan Esc menutup dialog

10. Ubah Default Capitalization Threshold menjadi "6.000.000"
11. Klik `[Save changes]` sehingga dialog "Save Changes" tampil
12. Tekan Tab berulang sebanyak jumlah elemen interaktif dialog ditambah satu
13. Verifikasi selama dialog terbuka fokus berputar hanya di antara elemen dialog (`[Cancel]` dan `[Save]`) dan tidak keluar ke form di belakang
14. Tekan Esc
15. Verifikasi dialog "Save Changes" tertutup tanpa menyimpan
16. Verifikasi form tetap memuat "Rp 6.000.000,00" yang belum disimpan
17. Kembalikan Default Capitalization Threshold ke "5.000.000"

### TC-FA-PREF-62: Modal Changelog, fokus ter-trap dan Esc menutup modal

18. Klik ikon View history sehingga modal Changelog terbuka
19. Tekan Tab berulang sebanyak jumlah elemen interaktif modal ditambah satu
20. Verifikasi selama modal terbuka fokus berputar hanya di dalam modal Changelog
21. Tekan Esc
22. Verifikasi modal Changelog tertutup
23. Verifikasi Tab Preferences tampil sebagai tab aktif

### TC-FA-PREF-65: Tooltip ikon ⓘ lewat keyboard focus

24. Tekan Tab hingga fokus berada pada ikon ⓘ Fiscal Year Start
25. Verifikasi tooltip "The month your company's financial year starts every year. Can be changed until depreciation is posted or a period has been closed." tampil saat ikon ⓘ menerima fokus keyboard

### TC-FA-PREF-63 dan TC-FA-PREF-64: Label aksesibilitas titik peringatan

26. Seed ulang Preferences company ke PA-5 lewat API lalu buka ulang Fixed Asset > Settings > Accounting > Preferences
27. Verifikasi judul SectionCard General memiliki titik peringatan dengan label aksesibilitas "General, has required fields" (diperiksa melalui accessibility tree)
28. Verifikasi judul SectionCard Capitalization memiliki titik peringatan dengan label aksesibilitas "Capitalization, has required fields" (diperiksa melalui accessibility tree)

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan blok: TC-FA-PREF-65 ditaruh sebelum TC-FA-PREF-63 dan TC-FA-PREF-64 supaya empat TC berdata PA-2 berurutan sebelum satu kali seed ulang PA-5 (S-10).
- Langkah penghubung (S-03): "Kembalikan Default Capitalization Threshold ke "5.000.000"" setelah TC-FA-PREF-61 (pemulihan form dirty, S-09); langkah 26 (seed ulang PA-5 dan buka ulang halaman); pemulihan PA-2 oleh hook `after`.
- Temuan untuk QA:
  - TC-FA-PREF-61 Post Condition a dan b ("tidak ada perubahan data Preferences tersimpan", "tidak ada entri log baru") tidak punya langkah observasi di TC sehingga tidak diasersi (S-01).
  - TC-FA-PREF-60 Expected a menyebut `[Save changes]` "bila Enabled" padahal form pristine (kedua tombol Disabled dan tidak menerima fokus); spec mengikuti teks TC.
  - TC-FA-PREF-60 sampai 65 tidak menyebut nama env var password; nama `FA_TC_PASSWORD` diusulkan spec dan perlu keputusan tim.
