---
id: TC-FA-FAAC-E2E-017-aksesibilitas-label-dan-responsif-tablet
title: "Aksesibilitas Label Toggle, Ikon Accounts, dan Tab Detail serta Tampilan Responsif Tabel dan Form pada Lebar Tablet"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-40
  - TC-FA-FAAC-41
  - TC-FA-FAAC-42
  - TC-FA-FAAC-44
  - TC-FA-FAAC-45
sourceRules: ["§4.5#b4", "§4.1.1#r1", "D-01", "§4.5#b5", "§4.1.1#r7", "§4.5#b3", "ST-04", "§4.5#b7", "§4.1.1#r2", "§4.1.1#r3", "§4.1.1#r4", "§4.1.1#r5", "§4.1.1#r6", "§4.1.1#r8", "§4.1.1#r9"]
smoke: []
dependsOn: []
trace:
  "§4.5#b4": [2, 3, 4, 5]
  "§4.1.1#r1": [3, 5, 10, 14, 27]
  "D-01": [8, 12]
  "§4.5#b5": [16, 17, 18]
  "§4.1.1#r7": [16, 17, 18, 27]
  "§4.5#b3": [22, 23]
  "ST-04": [22, 23]
  "§4.5#b7": [27, 30]
  "§4.1.1#r2": 27
  "§4.1.1#r3": 27
  "§4.1.1#r4": 27
  "§4.1.1#r5": 27
  "§4.1.1#r6": 27
  "§4.1.1#r8": 27
  "§4.1.1#r9": 27
coverage:
  web: automated
---

# Aksesibilitas Label Toggle, Ikon Accounts, dan Tab Detail serta Tampilan Responsif Tabel dan Form pada Lebar Tablet

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite dan memulihkan lebar layar ke ukuran desktop.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): sembilan Asset Class contoh Example Data PRD §4.1.1 dengan nama literal dari Tabel Data Uji Pre-setup TC: HEAVY-EQ, VEHICLES, IT-EQ, MACHINERY, BLDG, STORAGE, OFFICE-NEW, LAND (Active) dan OFFICE-OLD (Inactive). Kondisi akun: BLDG lengkap; MACHINERY dengan akun Asset Cost dan Accumulated Depreciation kosong dan Depreciation Expense terisi; IT-EQ dengan satu akun Inactive berkode 1520 dan akun lain Active. Seed disediakan tim FE/BE (lihat `suite.md`).
- Data Pre-setup tambahan (milik TC-FA-FAAC-40): Asset Class Active `B-A11Y` tanpa Asset Name; toggle Active dioperasikan hanya pada baris ini dan selalu dibatalkan lewat `Cancel` sehingga tetap Active. Seed disediakan tim FE/BE (lihat `suite.md`).
- Spec ini tidak menyimpan perubahan: toggle `B-A11Y` hanya dibuka dialognya lalu dibatalkan, form Create dibuka tanpa mengisi field, dan tidak ada data yang dibuat atau diubah.
- Kemampuan teknis: mengubah lebar viewport browser ke ukuran tablet dan memulihkannya ke desktop; disediakan tim FE (TC-FA-FAAC-44 dan TC-FA-FAAC-45).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-FAAC-40: Label toggle kolom Active

1. Ubah ukuran halaman menjadi 100
2. Verifikasi toggle baris HEAVY-EQ berlabel aksesibilitas `Active for asset class HEAVY-EQ`
3. Verifikasi toggle baris HEAVY-EQ berstate checked
4. Verifikasi toggle baris OFFICE-OLD berlabel aksesibilitas `Active for asset class OFFICE-OLD`
5. Verifikasi toggle baris OFFICE-OLD berstate tidak checked
6. Ketik Search `B-A11Y`, tekan Enter
7. Fokuskan toggle baris B-A11Y dengan Tab, tekan Enter
8. Verifikasi dialog `Deactivate Asset Class` tampil
9. Klik `Cancel`
10. Verifikasi dialog `Deactivate Asset Class` menutup dan toggle baris B-A11Y tetap On
11. Fokuskan toggle baris B-A11Y dengan Tab, tekan Space
12. Verifikasi dialog `Deactivate Asset Class` tampil
13. Klik `Cancel`
14. Verifikasi dialog `Deactivate Asset Class` menutup dan toggle baris B-A11Y tetap On
15. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### TC-FA-FAAC-41: Label ikon kolom Accounts pada tiga kondisi

16. Verifikasi label aksesibilitas ikon Accounts baris BLDG (lengkap) berbunyi `Complete`
17. Verifikasi label aksesibilitas ikon Accounts baris MACHINERY (belum lengkap) berbunyi `Accounts incomplete: Asset Cost, Accumulated Depreciation. Journals for this asset class will be held at export.`
18. Verifikasi label aksesibilitas ikon Accounts baris IT-EQ (ada akun Inactive 1520) berbunyi `Account 1520 is inactive. Journals for this asset class will be held at export.`
19. Ubah ukuran halaman kembali menjadi 10

### TC-FA-FAAC-42: Label tab Detail yang memiliki field wajib kosong

20. Klik `[+ Asset Class]`
21. Klik `[Submit]` saat seluruh field kosong
22. Verifikasi tab General memiliki titik peringatan dan label aksesibilitas `General, has required fields`
23. Verifikasi tab Depreciation memiliki titik peringatan dan label aksesibilitas `Depreciation, has required fields`
24. Klik breadcrumb `Asset Class`

### TC-FA-FAAC-44: Tabel Asset Class pada lebar tablet

25. Ubah lebar layar ke ukuran tablet
26. Geser tabel secara horizontal
27. Verifikasi tabel menampilkan horizontal scroll sehingga kolom Active, Class Code, Class Name, Commercial, Fiscal, Capitalization Threshold, Accounts, Asset Names, dan Assets dapat dijangkau

### TC-FA-FAAC-45: Field form Detail pada lebar tablet

28. Ketik Search `HEAVY-EQ`, tekan Enter
29. Klik link Class Code `HEAVY-EQ` untuk membuka Detail
30. Verifikasi field form Detail tersusun satu kolom
31. Pulihkan lebar layar ke ukuran desktop
32. Klik breadcrumb `Asset Class`
33. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 dan 19 (ukuran halaman 100 agar baris contoh terjangkau sesuai butir Precondition TC-40 dan TC-41, lalu dipulihkan ke 10), langkah 6 (Search untuk menjangkau baris B-A11Y), langkah 9 dan 13 (membatalkan dialog Deactivate; Cancel adalah aksi TC-40 langkah 4 dan 5), langkah 15 dan 33 (mengosongkan Search, S-09), langkah 24 dan 32 (kembali ke daftar lewat breadcrumb; form Create yang tidak diisi tidak dirty), langkah 28 (Search untuk menemukan baris target karena HEAVY-EQ tidak dijamin berada di halaman 1; R-16), langkah 31 (memulihkan viewport, S-03).
- Urutan TC dalam spec: 40, 41, 42, 44, 45. Blok viewport tablet di akhir agar pemulihan viewport tidak memengaruhi blok lain (S-10).
- Temuan untuk QA:
  - TC-FA-FAAC-42 langkah 2 tidak menyebut dialog `Unsaved Changes` saat meninggalkan form; spec meninggalkan form lewat breadcrumb tanpa dialog karena field tidak diisi.
  - TC-FA-FAAC-44 dan TC-FA-FAAC-45 tidak menyebut ukuran tablet persis; ukuran ditentukan tim FE.
