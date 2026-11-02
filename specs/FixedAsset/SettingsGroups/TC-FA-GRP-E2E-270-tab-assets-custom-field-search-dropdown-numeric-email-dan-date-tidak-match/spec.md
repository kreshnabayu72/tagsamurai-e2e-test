---
id: TC-FA-GRP-E2E-270-tab-assets-custom-field-search-dropdown-numeric-email-dan-date-tidak-match
title: "Tab Assets Custom Field Search: Dropdown/Multi-Dropdown, Numeric/Percentage, Email, serta Date dan DateTime Tidak Match"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1266
  - TC-FA-GRP-1267
  - TC-FA-GRP-1268
  - TC-FA-GRP-1269
coverage:
  web: automated
---

# Tab Assets Custom Field Search: Dropdown/Multi-Dropdown, Numeric/Percentage, Email, serta Date dan DateTime Tidak Match

## Prerequisites

- Mode: FE+BE.
- Hook suite: rujuk `suite.md` (login API aktor, sesi API, fixture BE, flag Guided Tooltip `fa-settings-groups` bernilai `seen`).
- Akun aktor pertama: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun (langkah eksplisit, untuk TC-1269): allValueAccess (Pre-setup No 17: Group Role Manage purchase pada Value Gate Node A, Global Role Manage accounting, lisensi FA-7 aktif) `allValueAccess_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_ALLVALUEACCESS_PASSWORD`.
- Data Pre-setup tambahan (hanya dibaca): Value Gate Node A (Tabel Dinamis No 10, G1-G6) dan fixture tipe Custom Field (No 18); node di-seed idempotent di hook `before` dengan nama bersuffix `{runId}-270` (mekanisme seeding disediakan tim FE/BE). Langkah dan asersi memakai nama bersuffix itu.
- Nilai uji (diacu dari fixture spec): Condition Grade (Dropdown) G1 A, G2 B, G4 C, G5 A, G6 B; Features (Multi-Dropdown Wifi/Bluetooth/NFC) G1 Wifi+Bluetooth, G2 Wifi, G4 NFC, G6 Bluetooth; Usage Hours (Numeric) G1 100, G2 250, G4 40, G6 100; Utilization (Percentage) G1 80, G2 20, G4 95, G6 50; Contact Email G1 `a@x.com`, G2 `b@x.com`; Inspection Time (DateTime) G1 01/10/2026 09:00, G2 05/10/2026 10:00, G4 10/10/2026 11:00; Purchase Date G1 10/02/2026. Teks sel Utilization G4 dibaca dari tabel sebelum di-Search.
- General Settings client: Date Format DD/MM/YYYY, Time 24-hour, Timezone Asia/Jakarta (kondisi awal client uji; spec tidak mengubahnya).
- Setup Column: hook `before` menghapus preferensi kolom Tab Assets di browser; hook `after` menghapus preferensi yang disimpan spec (kemampuan disediakan tim FE). Antar TC, konfigurasi dikembalikan dengan [Reset to Default] lalu [Save] sebagai langkah penghubung.
- State global: tidak ada yang diubah.

## Test Steps

### TC-1266: Search kolom Custom Field Dropdown dan Multi-Dropdown: label opsi, case-insensitive
1. Buka Detail Value Gate Node A (Tab Assets)
2. Buka Popup Setup Column, centang kolom Condition Grade dan Features, klik [Save]
3. Ketik Search `bluetooth`, tekan Enter
4. Verifikasi G1 dan G6 tampil (opsi Bluetooth pada Features)
5. Ganti isi kotak search dengan `wifi`, tekan Enter
6. Verifikasi G1 dan G2 tampil
7. Ganti isi kotak search dengan `xyz`, tekan Enter
8. Verifikasi empty state Illustration, title "No results found", body "Try adjusting your search or filter."
### TC-1267: Search kolom Custom Field Numeric dan Percentage: nilai yang tampil
9. Klik `(←)` pada kotak Search, buka Popup Setup Column, klik [Reset to Default], klik [Save]
10. Buka Popup Setup Column, centang kolom Usage Hours dan Utilization, klik [Save]
11. Ketik Search `250`, tekan Enter
12. Verifikasi G2 tampil (Usage Hours 250)
13. Baca teks sel Utilization G4 dari tabel
14. Ganti isi kotak search dengan teks sel Utilization G4 persis seperti tampil di sel, tekan Enter
15. Verifikasi G4 tampil
16. Verifikasi baris lain tidak tampil
### TC-1268: Search kolom Custom Field Email (Text-like): substring, case-insensitive
17. Klik `(←)` pada kotak Search, buka Popup Setup Column, klik [Reset to Default], klik [Save]
18. Buka Popup Setup Column, centang kolom Contact Email, klik [Save]
19. Ketik Search `B@X.COM`, tekan Enter
20. Verifikasi G2 tampil (nilai `b@x.com`, case-insensitive)
21. Verifikasi baris lain termasuk yang `—` tidak tampil
### TC-1269: Search kolom Custom Field Date dan DateTime tidak menghasilkan match
22. Klik `(←)` pada kotak Search, buka Popup Setup Column, klik [Reset to Default], klik [Save]
23. Ganti akun: Logout, login sebagai allValueAccess (`allValueAccess_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_GRP_ALLVALUEACCESS_PASSWORD`), buka Fixed Asset > Settings > Groups
24. Buka Detail Value Gate Node A (Tab Assets)
25. Buka Popup Setup Column, centang kolom Purchase Date dan Inspection Time, klik [Save]
26. Ketik Search `10/02/2026`, tekan Enter
27. Verifikasi empty state Illustration, title "No results found", body "Try adjusting your search or filter." (Data Type Date di luar cakupan Search)
28. Ganti isi kotak search dengan `01/10/2026`, tekan Enter
29. Verifikasi empty state Illustration, title "No results found", body "Try adjusting your search or filter." (Data Type DateTime di luar cakupan Search)
30. Klik icon Filter
31. Verifikasi Filter Panel memuat field Purchase Date dan Inspection Time

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah pembuka TC-1267, TC-1268, TC-1269 mengosongkan Search lewat `(←)` dan [Reset to Default] + [Save] (S-09); satu langkah Ganti akun sebelum TC-1269 (aktor berbeda; TC-1269 diletakkan terakhir).
- Asersi tambahan (S-03): `Verifikasi` Filter Panel memuat field Purchase Date dan Inspection Time pada akhir TC-1269 menerjemahkan Expected b "Penyaringan kedua kolom hanya lewat Filter Panel", yang tidak punya langkah observasi di TC; keberadaan kedua field itu mengikuti Langkah TC-1272.
- Temuan untuk QA:
  - TC-1267 langkah 5 tidak menyebut format tampil nilai Percentage (mis. dengan atau tanpa simbol %); spec membaca teks sel sebelum Search.
  - TC-1267 Expected a hanya menyebut G2 tampil untuk keyword `250`; apakah baris lain boleh ikut tampil (mis. Asset ID atau kolom lain yang memuat `250`) tidak dinyatakan, sehingga tidak diasersi.
