---
id: TC-FA-PREF-E2E-032-validasi-v-01-first-accounting-period-bulan-kosong-dan-titik-peringatan
title: "Validasi V-01: First Accounting Period Bulan Kosong, Caption Hilang Saat Field Terisi, dan Titik Peringatan Section"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-130
  - TC-FA-PREF-131
  - TC-FA-PREF-132
sourceRules: ["§3.1#b3", "V-01", "ST-04"]
smoke: []
dependsOn: []
trace:
  "§3.1#b3": 4
  "V-01": [5, 11, 13, 14, 19, 22]
  "ST-04": [6, 11, 15, 19, 23, 24]
coverage:
  web: automated
---

# Validasi V-01: First Accounting Period Bulan Kosong, Caption Hilang Saat Field Terisi, dan Titik Peringatan Section

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture. Nama diusulkan mengikuti `<APP>_<ROLE>_PASSWORD` (perlu dikonfirmasi tim FE).
- Data: company `PT Contoh Konstruksi` (plan Growth). Preferences nilai awal PA-2 untuk TC-FA-PREF-130 (First Accounting Period Mar 2026, tidak terkunci). Preferences PA-5 (Fiscal Year Start, First Accounting Period, Default Capitalization Threshold, In-service Date Source, dan Depreciation in Disposal Month kosong; setting lain bernilai awal) untuk TC-FA-PREF-131 dan 132, dibentuk lewat seed pada langkah 8 karena Save UI menolak nilai kosong.
- Jam sistem: tanggal sistem uji 28 Oktober 2026 pukul 10:00 pada Time Zone entitas Asia/Jakarta (PA-1), bulan berjalan = Oktober 2026. Jam server dan jam browser diatur bersama di hook `before` dan dipulihkan di hook `after` (bagian 6, butir "Kendali jam sistem" di `suite.md`). Suite serial.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed Preferences PA-5 dan pemulihan lewat sesi API aktor (butir "Seed dan pemulihan lewat API" dan "Sesi API aktor" di `suite.md`).
- State yang diubah spec: Preferences company (hanya seed PA-5) dan jam sistem. Tidak ada Save yang berhasil. Hook `after` memulihkan Preferences ke PA-2 dan jam sistem.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-130: Save dengan bulan First Accounting Period yang dikosongkan FI-06 menampilkan caption V-01

1. Pilih tahun "2025" lalu bulan "December" pada First Accounting Period
2. Ganti Select tahun menjadi "2026" sehingga bulan dikosongkan
3. Klik `[Save changes]`
4. Verifikasi tidak ada dialog "Save Changes" dan tidak ada toast
5. Verifikasi caption di bawah First Accounting Period: "First accounting period must not be empty"
6. Verifikasi judul SectionCard General memiliki titik peringatan
7. Pilih bulan "March" pada Select bulan First Accounting Period

### TC-FA-PREF-131: Caption V-01 field yang diisi hilang segera tetapi titik peringatan section bertahan

8. Bentuk Preferences PA-5 lewat seed hingga tersimpan, lalu muat ulang halaman Preferences
9. Tambahkan opsi "Category" pada Journal Grouping
10. Klik `[Save changes]`
11. Verifikasi caption "In-service date source must not be empty" dan "Default capitalization threshold must not be empty" tampil beserta titik peringatan pada judul SectionCard Capitalization
12. Pilih "Activation date" pada Select In-service Date Source
13. Verifikasi caption "In-service date source must not be empty" hilang segera
14. Verifikasi caption "Default capitalization threshold must not be empty" tetap tampil
15. Verifikasi titik peringatan pada judul SectionCard Capitalization tetap tampil karena Default Capitalization Threshold masih kosong
16. Klik `[Cancel]`

### TC-FA-PREF-132: Titik peringatan section hilang segera setelah seluruh setting wajib di section itu terisi

17. Tambahkan opsi "Category" pada Journal Grouping
18. Klik `[Save changes]`
19. Verifikasi kedua caption pada SectionCard Capitalization tampil beserta titik peringatan pada judul SectionCard General, Capitalization, dan Depreciation
20. Pilih "Activation date" pada Select In-service Date Source
21. Ketik "5000000" pada CurrencyInput Default Capitalization Threshold
22. Verifikasi kedua caption pada SectionCard Capitalization hilang segera
23. Verifikasi titik peringatan pada judul SectionCard Capitalization hilang segera
24. Verifikasi titik peringatan pada judul SectionCard General dan Depreciation tetap tampil
25. Klik `[Cancel]`

## Notes

- Urutan: TC-FA-PREF-130 (PA-2) lebih dulu, lalu TC-FA-PREF-131 dan 132 (PA-5) karena membutuhkan seed company dengan setting wajib kosong.
- Langkah penghubung (S-03): langkah 7 (mengembalikan bulan ke nilai tersimpan agar form tidak dirty; S-09), 8 (seed PA-5), 16 dan 25 (`[Cancel]` mengembalikan form ke nilai tersimpan PA-5; S-09 dan R-12 agar caption TC-FA-PREF-131 tidak terbawa ke TC-FA-PREF-132).
- Langkah 11 dan 19 adalah anchor positif asersi hilang (8b.2): caption dan titik peringatan terbukti tampil sebelum diisi. Langkah itu menyalin langkah 2 TC ("sehingga caption V-01 dan titik peringatan tampil") dan tidak ada di Expected TC (dicatat sesuai S-03).
- Jam sistem dibekukan 28 Oktober 2026 (PA-1) karena Precondition d TC-FA-PREF-130 menyebut bulan berjalan.
- Temuan untuk QA:
  - Post Condition TC-FA-PREF-130 ("Tidak ada perubahan data Preferences tersimpan"; "Tidak ada entri log baru") tidak punya langkah observasi sehingga tidak diasersi (S-01).
  - Step 2 TC-FA-PREF-131 dan 132 ("klik `[Save changes]` sehingga caption V-01 dan titik peringatan tampil") menggabungkan aksi dan keadaan hasil; spec memisahkan aksi (langkah 9, 10, 17, 18) dan keadaan (langkah 11, 19).
