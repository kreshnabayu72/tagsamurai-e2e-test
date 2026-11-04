---
id: TC-FA-TDC-E2E-040-drawer-create-screening-opsi-asset-type-satu-form-tanpa-tab-dan-aksesibilitas
title: "Drawer Create - Screening, Opsi Asset Type, Satu Form Tanpa Tab, dan Aksesibilitas"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-103
  - TC-FA-TDC-104
  - TC-FA-TDC-915
  - TC-FA-TDC-176
coverage:
  web: automated
---

# Drawer Create - Screening, Opsi Asset Type, Satu Form Tanpa Tab, dan Aksesibilitas

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.exampleDataClasses`, disediakan tim FE): tabel berisi 9 class sesuai Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data. Master Data Count Limit belum tercapai. Data Dinamis: tidak ada; spec tidak menyimpan data.
- State global yang diubah: tidak ada (tidak ada Submit; Drawer ditutup di akhir spec).

## Test Steps

### TC-FA-TDC-103: Screening Drawer Add Tax Depreciation Class (mode Create) 3 zona

1. Klik `+ Class` di toolbar
2. Verifikasi Header Drawer: judul "Add Tax Depreciation Class"
3. Verifikasi Header Drawer: ikon ✕ di sudut kanan atas
4. Verifikasi Header Drawer tidak memuat badge Status, baris teks "Class Name: ...", dan Alert versi Scheduled
5. Verifikasi Body urutan pertama: Regulation Reference * - Text input, placeholder "Enter regulation reference", helper "e.g. UU HPP 7/2021; PMK 72/2023"
6. Verifikasi Body urutan kedua: Class Code * - Text input, placeholder "Enter class code", helper "Letters, numbers, hyphens, underscores, and dots only (e.g. NB-1)"
7. Verifikasi Body urutan ketiga: Class Name * - Text input, placeholder "Enter class name"
8. Verifikasi Body urutan keempat: Asset Type * - Select single, placeholder "Select asset type"
9. Verifikasi Body urutan kelima: Useful Life (years) * - Number input, placeholder "Enter useful life"
10. Verifikasi Body urutan keenam: Allowed Methods * - Multi-select, placeholder "Select allowed methods"
11. Verifikasi Straight Line Rate (%) dan Declining Balance Rate (%) tidak tampil (tanpa nilai dan tanpa placeholder) selama belum ada metode di Allowed Methods yang dipilih
12. Verifikasi field Effective From, Last Posted Tax Year, dan tautan View versions tidak ada
13. Verifikasi Footer: checkbox "Stay on this form after submitting" tepat di atas tombol, rata kanan, tidak dicentang
14. Verifikasi Footer: tombol `[Clear Field]` (text, primary) dan `[Submit]` (filled, success) rata kanan
15. Verifikasi Footer tidak memuat tombol `[Cancel]` dan `[Close]`

### TC-FA-TDC-104: Opsi Select Asset Type pada Drawer Create

16. Verifikasi placeholder "Select asset type" tampil pada Select Asset Type sebelum ada pilihan
17. Klik Select Asset Type
18. Verifikasi daftar opsi tepat tiga, berurutan: "Non-building", "Building", "Land"
19. Verifikasi daftar opsi tidak memuat opsi "None"
20. Tutup dropdown Asset Type tanpa memilih opsi

### TC-FA-TDC-915: Drawer Create dan Drawer Edit memuat satu form tanpa tab (bagian Drawer Create)

21. Verifikasi Drawer Create: seluruh field berada dalam satu form; tidak ada tab atau tab bar

### TC-FA-TDC-176: Accessibility Drawer Create - navigasi keyboard, fokus ter-trap, dan Esc

22. Tekan Tab berulang kali melewati seluruh elemen interaktif Drawer
23. Verifikasi fokus berpindah berurutan antar field, checkbox, `[Clear Field]`, `[Submit]`, ikon ✕ dan kembali ke elemen pertama Drawer tanpa keluar dari Drawer (fokus ter-trap)
24. Pada checkbox "Stay on this form after submitting" tekan Space
25. Verifikasi Space mencentang checkbox "Stay on this form after submitting"
26. Tekan `Esc`
27. Verifikasi Drawer Create tertutup (Esc menutup Drawer; juga memenuhi TC-FA-TDC-915 Expected b)
28. Verifikasi dialog Unsaved Changes tidak muncul (form bersih)

### TC-FA-TDC-915: Drawer Edit memuat satu form tanpa tab (bagian Drawer Edit)

29. Klik link Class Code `NB-4`
30. Verifikasi Drawer Edit: seluruh field berada dalam satu form; tidak ada tab atau tab bar
31. Tutup Drawer Edit dengan klik ikon ✕

## Notes

- Langkah penghubung (S-03): langkah 20 (menutup dropdown Asset Type) dan langkah 31 (menutup Drawer Edit yang bersih).
- Pembagian TC lintas spec: seluruh TC sumber ada di spec ini; tidak ada TC yang dibagi.
- Urutan TC-FA-TDC-915 mengikuti satu pembukaan Drawer Create (prinsip 6): Expected a TC-FA-TDC-915 diasersi di langkah 21 pada Drawer yang sama dengan TC-FA-TDC-103, 104, dan 176; langkah Esc TC-FA-TDC-915 (langkah 2) dan Esc TC-FA-TDC-176 (langkah 4) adalah satu aksi pada langkah 26. Drawer Edit hanya dibuka satu kali (langkah 29).
- Langkah 29 tidak didahului Search karena tabel Example Data berisi 9 baris dan memuat satu halaman (page size bawaan 10); baris `NB-4` tampil tanpa Search (8b.13, R-23).
- Temuan untuk QA:
  - TC-FA-TDC-103 Expected b.vii memuat klausa kedua ("setelah metode dipilih, rate tetap tidak tampil sampai Useful Life terisi") yang tidak punya langkah di TC-FA-TDC-103 (TC hanya membuka Drawer dan mengamati). Spec hanya memverifikasi keadaan awal tanpa metode (langkah 11); perilaku setelah metode dipilih diuji TC-FA-TDC-166.
  - TC-FA-TDC-103 Expected b.v: helper Useful Life tidak disebut; spec tidak menambah asersi helper.
  - TC-FA-TDC-176 Expected c dan TC-FA-TDC-915 Expected b ("form bersih tanpa dialog") dipenuhi satu Esc; checkbox dicentang pada langkah 24 bukan field data, sehingga Drawer dianggap bersih. Perlu konfirmasi QA bahwa centang checkbox tidak membuat Drawer dirty.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
