---
id: TC-FA-SU-E2E-150-sub-tab-assigned-assets-screening-dan-search
title: "Sub-tab Assigned Assets: Screening dan Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-442
  - TC-FA-SU-443
  - TC-FA-SU-444
  - TC-FA-SU-445
coverage:
  web: automated
---

# Sub-tab Assigned Assets: Screening dan Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook suite dinyatakan di `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup (hanya dibaca, tidak diubah): Client `FaUserMain` (#20) dan Responsibilities (#24): Detail Budi Santoso dengan Sub-tab Assigned Assets 5 baris (satu halaman). Nilai dibaca dari `Fixture.faSettingsUser.preSetup` (fixture belum ada, disediakan tim FE). Pre-setup #24 hanya menyebut "5 baris"; nilai kolom di bawah diturunkan dari Expected TC (Asset ID dan Transaction ID hanya tertulis sebagian):

| Name | Asset ID | Transaction ID | Brand | Model / Type | PIC |
|---|---|---|---|---|---|
| `AC Split Ruang Kerja` | tidak tertulis | tidak tertulis | `Daikin` | `1PK` | `Ahmad D` |
| `Lemari Arsip` | tidak tertulis | tidak tertulis | `Lion` | `2 Pintu` | `Citra L` |
| `Meja Kerja Kepala Divisi` | tidak tertulis | `ASG-20260505` | `Modera` | `Executive` | `Ahmad D` |
| `Printer Multifungsi` | tidak tertulis | tidak tertulis | `Canon` | `PIXMA G3010` | `Citra L` |
| `Server Rack Mini` | `AST-02113` | tidak tertulis | `HP` | `ProLiant DL20` | `Eka W` (Eka Wulandari) |
- Data Dinamis: tidak ada.
- State global: tidak ada yang diubah; spec hanya membaca Pre-setup. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-442: Screening Sub-tab Assigned Assets: Table Tools, kolom, dan default sort

1. Klik nama `Budi Santoso` di User List
2. Klik tab Responsibilities, lalu klik Sub-tab Assigned Assets
3. Verifikasi Table Tools `Search`, `Filter`, dan `Download` tampil
4. Verifikasi Table Tools rata kanan
5. Hover icon Search
6. Verifikasi tooltip `Search` tampil
7. Hover icon Filter
8. Verifikasi tooltip `Filter` tampil
9. Hover icon Download
10. Verifikasi tooltip `Download` tampil
11. Klik icon Search
12. Verifikasi placeholder Search `Search name, asset ID, or transaction ID...`
13. Klik `(←)` pada kotak Search
14. Verifikasi header kolom `Photo (unsortable)`, `Name (sortable)`, `Asset ID (sortable)`, `Transaction ID (sortable)`, `Brand (sortable)`, `Model / Type (sortable)`, `PIC (sortable)`, dan `Column Visibility (⋯)`
15. Klik header kolom Column Visibility (⋯)
16. Verifikasi overlay Column Visibility terbuka
17. Tekan Esc untuk menutup overlay Column Visibility
18. Verifikasi body tiap baris pada kolom Column Visibility (⋯) kosong tanpa row action
19. Verifikasi default sort Name ascending: `AC Split Ruang Kerja`, `Lemari Arsip`, `Meja Kerja Kepala Divisi`, `Printer Multifungsi`, `Server Rack Mini`
20. Verifikasi footer pagination menampilkan 10 data per halaman
21. Klik dropdown page size
22. Verifikasi pilihan page size `10`, `25`, `50`, dan `100`
23. Tekan Esc untuk menutup pilihan page size

### TC-FA-SU-443: Search kelas teks: kolom Name, Asset ID, Transaction ID

24. Ketik Search `Printer`, tekan Enter
25. Verifikasi keyword `Printer` menyisakan `Printer Multifungsi` (1 baris)
26. Kosongkan isi kotak search, tekan Enter
27. Ketik Search `AST-02113`, tekan Enter
28. Verifikasi keyword `AST-02113` menyisakan `Server Rack Mini` (1 baris)
29. Kosongkan isi kotak search, tekan Enter
30. Ketik Search `ASG-20260505`, tekan Enter
31. Verifikasi keyword `ASG-20260505` menyisakan `Meja Kerja Kepala Divisi` (1 baris)
32. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-444: Search kelas badge: kolom Brand, Model / Type

33. Ketik Search `Canon`, tekan Enter
34. Verifikasi keyword `Canon` menyisakan `Printer Multifungsi` (1 baris)
35. Kosongkan isi kotak search, tekan Enter
36. Ketik Search `Executive`, tekan Enter
37. Verifikasi keyword `Executive` menyisakan `Meja Kerja Kepala Divisi` (1 baris)
38. Kosongkan isi kotak search, tekan Enter

### TC-FA-SU-445: Search kelas user: kolom PIC

39. Ketik Search `Wulandari`, tekan Enter
40. Verifikasi keyword `Wulandari` menyisakan `Server Rack Mini` (1 baris)
41. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pembukaan Detail dan sub-tab (langkah 1 dan 2), klik header kolom Column Visibility (⋯) dan Esc penutup overlay (langkah 15 dan 17; langkah 16 mengasersi klausa Expected b "header ⋯ membuka overlay Column Visibility"), serta langkah yang mengosongkan Search, Filter, atau popup di antara blok TC supaya blok berikutnya tidak mengandalkan state blok sebelumnya (S-09).
- Baris Search dipakai berurutan pada satu pembukaan Detail: kotak Search dikosongkan (langkah pembersih) di antara kata kunci, dan ditutup dengan `(←)` di akhir spec.
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (41 langkah, 41 langkah nominal). Seluruhnya satu kelas (fungsional/screening sub-tab Assigned Assets, satu akun, data Pre-setup sama, tanpa mengubah data Pre-setup), dan tiap blok TC berdiri sendiri: kegagalan satu blok tidak menghilangkan makna blok lain. Satu pembukaan Detail dipakai bersama seluruh blok.
- Pembagian TC lintas spec: TC-FA-SU-446 dan 447 ada di spec 151; TC-FA-SU-468 ada di spec 158.
- Temuan untuk QA (S-15):
  - Pre-setup #24 hanya menyebut "5 baris" Assigned Assets; nilai Asset ID dan Transaction ID sebagian besar tidak tertulis, spec memakai nilai yang tercantum pada Expected TC dan menurunkan sisanya dari urutan sort.
  - TC-FA-SU-442 Expected a menyebut tooltip hover Table Tools, sedangkan TC-FA-SU-468 (UI Only) menguji tooltip yang sama; spec mengasersi tooltip di kedua spec sesuai Expected masing-masing.
