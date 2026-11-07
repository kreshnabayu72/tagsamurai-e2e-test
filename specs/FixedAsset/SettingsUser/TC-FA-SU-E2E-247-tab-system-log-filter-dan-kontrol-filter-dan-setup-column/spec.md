---
id: TC-FA-SU-E2E-247-tab-system-log-filter-dan-kontrol-filter-dan-setup-column
title: "Tab System Log: Filter dan Kontrol Filter dan Setup Column"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-751
  - TC-FA-SU-752
  - TC-FA-SU-753
coverage:
  web: automated
---

# Tab System Log: Filter dan Kontrol Filter dan Setup Column

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan System Log (#28). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Tab System Log Budi Santoso (Pre-setup #28, 7 baris; urutan default Date descending; kolom Name berisi target perubahan). Alias baris yang dipakai langkah (Action | Name | Field):
  - S-1: `Resend Activation Email` | `Hana Kusuma` | `Activation Email`
  - S-2: `Auto-Revert` | `Oscar Pranata` | `Group Manager — IT Infrastructure`
  - S-3: `Edit` | `Oscar Pranata` | `Manage group — IT Infrastructure — Update`
  - S-4: `Assign` | `Lina Marlina` | `Access Level`
  - S-5: `Assign` | `Eka Wulandari` | `Manage group — Finance & Accounting`
  - S-6: `Assign` | `Eka Wulandari` | `Manage accounting`
  - S-7: `Activate` | `Eka Wulandari` | `Status`
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed System Log #28 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface System Log dan tidak menambah entri pada Budi Santoso.

## Test Steps

### TC-FA-SU-751: Chip dan checkbox dropdown Filter

1. Ketik Search `Budi Santoso`, tekan Enter
2. Buka Detail pengguna Budi Santoso lalu klik tab System Log
3. Klik icon Filter
4. Buka dropdown Action
5. Centang dua opsi (`Activate` dan `Assign`), klik `[Apply]`
6. Verifikasi dua chip tampil di dalam field
7. Verifikasi hasil adalah gabungan (OR) kedua opsi
8. Klik ✕ pada satu chip tanpa membuka dropdown
9. Verifikasi chip itu hilang
10. Verifikasi checkbox opsi terkait ter-uncheck
11. Verifikasi chip lain tetap
12. Buka dropdown Action
13. Hilangkan centang opsi yang tersisa
14. Verifikasi chip yang bersangkutan hilang
15. Centang dua opsi (`Activate` dan `Assign`) lalu hilangkan centang satu opsi
16. Verifikasi chip opsi yang di-uncheck hilang
17. Verifikasi chip lain tetap
18. Ketik `ass` pada kotak cari dropdown
19. Verifikasi opsi dipersempit (substring, tidak case-sensitive)
20. Ganti isi kotak cari dropdown dengan `zzzz`
21. Verifikasi `No results found` tampil di dropdown
22. Kosongkan kotak cari dropdown, tutup dropdown, lalu klik `[Clear Field]` dan `[Apply]`

### TC-FA-SU-752: Screening Overlay Column Visibility

23. Klik header kolom Actions (⋯)
24. Verifikasi overlay tampil dengan tooltip `Column Visibility` pada header
25. Verifikasi daftar kolom berurutan Date, Action, Object, Name, Field, Old Value, New Value dengan checkbox Hideable terpilih dan enabled serta drag handle
26. Verifikasi item `Setup Column...` di bagian bawah overlay

### TC-FA-SU-753: Screening Popup Setup Column dan Preview Table

27. Klik item `Setup Column...` pada overlay Column Visibility yang masih terbuka
28. Verifikasi Title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, dan icon close ✕ tampil
29. Verifikasi body: daftar kolom Date, Action, Object, Name, Field, Old Value, New Value dengan checkbox, drag handle, icon Pin, dan Live Preview tabel
30. Verifikasi footer: `[Reset to Default]` dan `[Save]` rata kanan tanpa `[Cancel]`
31. Klik ✕ untuk menutup popup Setup Column

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (Ketik Search `Budi Santoso` di User List untuk menemukan baris target sebelum membuka Detail, R-16, butir 8b.13); User List memuat 25 pengguna pada 3 halaman sehingga posisi baris tidak diandalkan.
- Temuan untuk QA (S-15): (1) TC mengasersi urutan dan isi baris seed tanpa Filter pembatas pada audit trail permanen; spec mengikuti TC dan mengandalkan seed #28 yang disediakan ulang di hook `before` dan `after` (S-14). Aksi spec lain terhadap Budi Santoso menambah entri System Log, sehingga penyediaan ulang seed menjadi syarat asersi urutan dan jumlah baris. (2) TC-FA-SU-751 langkah 6 menyebut kata kunci tanpa hasil di kotak cari dropdown tanpa nilai konkret; spec memakai `zzzz` dan `ass` sebagai pilihan sendiri. Opsi yang dicentang (`Activate` dan `Assign`) juga pilihan spec karena TC tidak menyebutnya.
