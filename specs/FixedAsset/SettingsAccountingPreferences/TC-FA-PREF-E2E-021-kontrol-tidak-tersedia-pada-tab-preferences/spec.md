---
id: TC-FA-PREF-E2E-021-kontrol-tidak-tersedia-pada-tab-preferences
title: "Kontrol yang tidak disediakan tab Preferences: Create, Delete, Search, Filter, bulk action, Download, paginasi, setting keterangan jurnal"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-2
  - TC-FA-PREF-594
  - TC-FA-PREF-595
  - TC-FA-PREF-608
sourceRules: ["§4.1.1#p1", "FAPREF-LOGIC-01b", "§4.1#r1", "SET-11", "§9.5#r1", "§4.1.1#p2", "§5#p1", "§4.2a#p1"]
smoke: []
dependsOn: []
trace:
  "§4.1.1#p1": [1, 2, 4, 5, 12, 17]
  "FAPREF-LOGIC-01b": [3, 8]
  "§4.1#r1": 7
  "SET-11": 10
  "§9.5#r1": 10
  "§4.1.1#p2": 11
  "§5#p1": [13, 14, 16, 18]
  "§4.2a#p1": 15
coverage:
  web: automated
---

# Kontrol yang tidak disediakan tab Preferences: Create, Delete, Search, Filter, bulk action, Download, paginasi, setting keterangan jurnal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PA-4), email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi` (PA-1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data awal (seed di hook `before`): Preferences company sesuai PA-2 (nilai awal, tidak terkunci, semua setting wajib terisi). Blok TC-FA-PREF-594, 595, dan 608 memakai PC-1 (seluruh setting tersimpan pada nilai awal, belum ada posting penyusutan, semua periode Open, bulan berjalan Oktober 2026); seed PC-1 dijalankan lewat API oleh langkah penghubung. Nilai awal PA-2 dan PC-1 setara; spec hanya membaca tampilan dan tidak mengubah data.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-2: Tidak ada kontrol Create atau Delete Preferences

1. Verifikasi ikon View history tampil di header tab
2. Verifikasi `[Cancel]` dan `[Save changes]` tampil di footer
3. Verifikasi tidak ada tombol, menu, maupun ikon untuk membuat atau menghapus Preferences pada header, SectionCard, dan footer
4. Verifikasi satu-satunya aksi header adalah ikon View history
5. Verifikasi aksi footer hanya `[Cancel]` dan `[Save changes]`

### TC-FA-PREF-594: Tidak ada kontrol Create atau Delete Preferences (seluruh kontrol)

6. Seed ulang Preferences company ke PC-1 lewat API lalu buka ulang Fixed Asset > Settings > Accounting > Preferences
7. Verifikasi kontrol yang tersedia: ikon View history, field setting, shortcut `+ Create account` pada Default Gain on Disposal dan Default Loss on Disposal, tombol `[Cancel]`, dan tombol `[Save changes]`
8. Verifikasi tidak ada tombol atau menu untuk membuat Preferences baru maupun menghapus Preferences

### TC-FA-PREF-595: Tidak ada setting keterangan atau tanggal jurnal

9. Gulir ke SectionCard Journal Export
10. Verifikasi SectionCard Journal Export hanya memuat Journal Grouping
11. Verifikasi tidak ada setting keterangan jurnal maupun tanggal jurnal pada tab Preferences

### TC-FA-PREF-608: Tidak ada Search, Filter Panel, bulk action, Download, dan paginasi

12. Verifikasi ikon View history tampil di header tab
13. Verifikasi header tab tidak memuat kotak Search, ikon Search, ikon Filter, maupun tombol Download
14. Verifikasi satu-satunya ikon toolbar adalah View history
15. Verifikasi SectionCard General tampil pada body
16. Verifikasi body tidak memuat tabel data, Bulk Action Bar, maupun checkbox seleksi baris
17. Verifikasi footer hanya memuat `[Cancel]` dan `[Save changes]`
18. Verifikasi footer tidak memuat kontrol paginasi

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini hanya membaca tampilan; asersi absence didahului anchor positif pada surface yang sama (8b butir 2): langkah 1 dan 2 sebelum langkah 3; langkah 7 sebelum langkah 8; langkah 10 sebelum langkah 11; langkah 12 sebelum langkah 13; langkah 15 sebelum langkah 16; langkah 17 sebelum langkah 18.
- Urutan Verifikasi pada TC-FA-PREF-2 dan TC-FA-PREF-608 disusun anchor lebih dulu (S-14); isi Expected tetap sama dengan TC.
- Langkah penghubung (S-03): langkah 6 (seed ulang PC-1 dan buka ulang halaman); langkah 9 (menggulir ke SectionCard Journal Export, sesuai Langkah Uji TC-FA-PREF-595).
- Temuan untuk QA:
  - TC-FA-PREF-2, 594, 595, dan 608 tidak menyebut nama env var password; nama `FA_TC_PASSWORD` diusulkan spec dan perlu keputusan tim.
