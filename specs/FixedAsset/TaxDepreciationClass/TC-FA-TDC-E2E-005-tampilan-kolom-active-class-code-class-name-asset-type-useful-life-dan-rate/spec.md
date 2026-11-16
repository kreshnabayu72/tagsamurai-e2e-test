---
id: TC-FA-TDC-E2E-005-tampilan-kolom-active-class-code-class-name-asset-type-useful-life-dan-rate
title: "Tampilan Kolom Active, Class Code, Class Name, Asset Type, Useful Life, dan Rate"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-16
  - TC-FA-TDC-17
  - TC-FA-TDC-18
  - TC-FA-TDC-19
  - TC-FA-TDC-20
sourceRules: ["§4.1.1#r1", "§4.1.1#r16", "§4.1.1#r24", "§4.5#b4", "ST-27", "§4.1.2#r3", "§4.1.1#r4", "§4.1.1#r20", "§4.1.1#r22", "§4.1.1#r5", "§4.1.1#r17", "§4.1.1#r6", "§4.1.1#r7", "§4.1.1#r18", "§4.1.1#r2"]
smoke: []
dependsOn: []
trace:
  "§4.1.1#r1": [1, 2]
  "§4.1.1#r16": [1, 12, 14, 18]
  "§4.1.1#r24": 2
  "§4.5#b4": [3, 4, 5, 6]
  "ST-27": [4, 6]
  "§4.1.2#r3": 7
  "§4.1.1#r4": [12, 13]
  "§4.1.1#r20": [12, 16, 21]
  "§4.1.1#r22": [12, 17, 22]
  "§4.1.1#r5": [14, 15, 16, 17]
  "§4.1.1#r17": [15, 19]
  "§4.1.1#r6": [18, 19, 20, 21, 22]
  "§4.1.1#r7": [18, 19, 20, 21, 22]
  "§4.1.1#r18": 20
  "§4.1.1#r2": [23, 28]
anchor: [8, 9, 11, 25, 26]
coverage:
  web: automated
---

# Tampilan Kolom Active, Class Code, Class Name, Asset Type, Useful Life, dan Rate

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.exampleData`, disediakan tim FE): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data. Nilai yang diasersi: NB-1 Active On, Useful Life 4, Straight Line Rate 25%, Declining Balance Rate 50%; NB-2 Useful Life 8, 12.5%, 25%; NB-SL 6.25% dan `—`; BLD-P Useful Life 20, 5%, `—`; LAND `—`, `—`, `—`; NB-OLD Active Off; Asset Type NB-1 `Non-building`, BLD-P `Building`, LAND `Land`.
- Data Dinamis (milik spec, dibuat di hook `before` lewat seeding API, dihapus di `after`): satu class dengan Class Name sepanjang 120 karakter, Class Code `KHS-N120-{runId}-005`, kunci `className120`. Bersama sembilan class di atas tabel berisi 10 baris pada satu halaman (page size default 10), sehingga baris dicari tanpa Search.
- Kemampuan teknis: seeding class lewat API (`suite.md`); membaca label aksesibilitas (aria-label) dan state checked toggle; mengarahkan kursor (hover); membuka Drawer Edit tanpa mengubah.
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-TDC-16: Tampilan kolom Active: toggle On dan Off

1. Verifikasi kolom Active baris NB-1 menampilkan toggle On (Active)
2. Verifikasi kolom Active baris NB-OLD menampilkan toggle Off (Inactive)
3. Verifikasi label aksesibilitas toggle NB-1 `Active for tax depreciation class NB-1`
4. Verifikasi toggle NB-1 dengan state checked
5. Verifikasi label aksesibilitas toggle NB-OLD `Active for tax depreciation class NB-OLD`
6. Verifikasi toggle NB-OLD dengan state tidak checked

### TC-FA-TDC-18: Kolom Class Name dan Asset Type menampilkan teks utuh tanpa pemotongan

7. Verifikasi Class Name baris `KHS-N120-{runId}-005` tampil utuh 120 karakter
8. Verifikasi Class Name tidak dipotong dengan `..`
9. Verifikasi kolom Class Name melebar mengikuti isi
10. Arahkan kursor ke sel Class Name baris `KHS-N120-{runId}-005`
11. Verifikasi tidak ada tooltip pada sel Class Name itu
12. Verifikasi Asset Type NB-1 `Non-building`, BLD-P `Building`, dan LAND `Land`
13. Verifikasi tidak ada sel kosong pada kolom Asset Type

### TC-FA-TDC-19: Kolom Useful Life (years): bilangan bulat dan strip untuk Land

14. Verifikasi Useful Life NB-1 `4`
15. Verifikasi Useful Life NB-2 `8`
16. Verifikasi Useful Life BLD-P `20`
17. Verifikasi Useful Life LAND `—`

### TC-FA-TDC-20: Kolom Straight Line Rate dan Declining Balance Rate: format persen dan strip

18. Verifikasi NB-1: Straight Line Rate `25%`, Declining Balance Rate `50%`
19. Verifikasi NB-2: Straight Line Rate `12.5%`, Declining Balance Rate `25%`
20. Verifikasi NB-SL: Straight Line Rate `6.25%`, Declining Balance Rate `—`
21. Verifikasi BLD-P: Straight Line Rate `5%`, Declining Balance Rate `—`
22. Verifikasi LAND: Straight Line Rate `—`, Declining Balance Rate `—`

### TC-FA-TDC-17: Kolom Class Code: tampilan link, hover, dan buka Drawer

23. Verifikasi Class Code NB-1 tampil sebagai text link dengan warna teks default netral
24. Arahkan kursor ke Class Code NB-1
25. Verifikasi warna Class Code NB-1 berubah menjadi warna primary produk Fixed Asset (biru)
26. Verifikasi Class Code NB-1 tampil tanpa underline saat hover
27. Klik Class Code NB-1
28. Verifikasi Drawer mode Edit untuk NB-1 terbuka
29. Tutup Drawer lewat `[×]`

## Notes

- Urutan TC dalam spec: TC-FA-TDC-16, 18, 19, 20, 17. TC-FA-TDC-17 membuka Drawer dan diletakkan terakhir supaya semua TC tampilan murni berjalan sebelum form dibuka dan ditutup (prinsip 6 bagian 3).
- Langkah penghubung (S-03): langkah 10 (hover sel Class Name sebagai pemicu untuk menilai "tanpa tooltip"; TC hanya meminta mengamati, sehingga asersi absence langkah 11 memerlukan pemicu) dan langkah 29 (menutup Drawer yang tidak diubah; tidak ada dialog `Unsaved Changes`).
- Asersi absence langkah 11 didahului anchor positif pada langkah 7 sampai 9 (sel Class Name termuat) dan hover pada langkah 10 (8b.2). Asersi langkah 13 didahului langkah 12.
- Temuan untuk QA:
  - TC-FA-TDC-18 tidak menyebut Class Code dan Asset Type baris dengan Class Name 120 karakter; spec membuat class milik spec `KHS-N120-{runId}-005` (Class Code dan Asset Type ditetapkan tim FE saat seeding).
  - TC-FA-TDC-18 langkah 1 tidak menyebut hover, tetapi Expected "tanpa tooltip" butuh pemicu; spec menambah hover sebagai langkah penghubung (S-03).
  - TC-FA-TDC-17 Expected b menggabungkan perubahan warna dan "tanpa underline"; spec memecahnya menjadi dua `Verifikasi`.
  - Email akun Total Control tidak tertulis di TC.
