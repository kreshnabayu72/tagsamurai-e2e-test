---
id: TC-FA-TDC-E2E-181-guided-tooltip-isi-enam-langkah-kunjungan-pertama-dan-empty-state
title: "Guided Tooltip: Isi Enam Langkah, Kunjungan Pertama, dan Empty State"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-648
  - TC-FA-TDC-649
  - TC-FA-TDC-650
  - TC-FA-TDC-651
sourceRules: ["§4.7#p2", "§4.7#r1", "§4.7#r2", "§4.7#r3", "§4.7#r4", "§4.7#r6", "ST-23"]
smoke: []
dependsOn: []
trace:
  "§4.7#p2": [3, 4, 9, 21]
  "§4.7#r1": [5, 6, 7, 23]
  "§4.7#r2": [5, 6, 7, 25]
  "§4.7#r3": [5, 6, 7, 27]
  "§4.7#r4": [5, 6, 7, 29]
  "§4.7#r6": [10, 11, 12]
  "ST-23": 22
anchor: [13, 14, 17, 18, 30]
coverage:
  web: automated
---

# Guided Tooltip: Isi Enam Langkah, Kunjungan Pertama, dan Empty State

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; layar awal dibuka sendiri oleh spec ini (pengecualian `beforeEach` suite karena flag Guided Tooltip diatur spec). Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding mengikuti `suite.md`. Pengecualian flag Guided Tooltip: spec ini mengatur sendiri flag `guided_tooltip_seen_fa-tax-depreciation-class` untuk akun Total Control (langkah 1 dan 19 menghapus flag, langkah 15 menyimpannya lewat `[Done]`); hook suite `before` yang menyetel flag true untuk semua spec lain tidak berlaku, dan hook `after` memulihkan flag ke true.
- Data Pre-setup (dibaca, tidak diubah kecuali langkah 19; disediakan tim FE): `Fixture.fixedAssetTaxDepreciationClass.seedClasses` berisi tujuh class seed bawaan (NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND) belum diubah. Data Dinamis: tidak ada.
- Tabel isi langkah walkthrough TC-FA-TDC-648 (parameter langkah 4 sampai 8; Step 6 ditulis eksplisit pada langkah 9 sampai 12), literal TC:

  | Step | Target | Title | Description |
  |---|---|---|---|
  | 1 | header kolom Class Code | `Tax Depreciation Class` | `Defines how assets depreciate for tax. Asset classes pick one of these classes.` |
  | 2 | header kolom Allowed Methods | `Allowed Methods` | `The tax methods an asset class may use with this class.` |
  | 3 | header kolom Used By | `Used By` | `Shows how many asset classes use this class. Open it before changing or deactivating the class.` |
  | 4 | header kolom Effective From | `Effective From` | `Rates change per tax year. Past periods keep the rates that applied then.` |
  | 5 | icon Filter di toolbar | `Filter Tax Depreciation Classes` | `Narrow down the list. Filters combine with your search.` |

- Kemampuan teknis: menghapus dan menyetel flag Guided Tooltip akun (disediakan tim FE/BE; nama kunci flag dari TC); menghapus seluruh Tax Depreciation Class dan memulihkan tujuh class seed bawaan lewat seeding API suite (`suite.md`); navigasi baru ke layar Settings > Accounting > Tax Depreciation Class.
- State global yang diubah: flag Guided Tooltip akun Total Control (langkah 1, 15, dan 19; hook `after` memulihkan ke true) dan seluruh class dihapus pada blok TC-FA-TDC-650 (langkah 19), dipulihkan ke tujuh class seed bawaan pada langkah 32 (hook `after` sebagai cadangan).

## Test Steps

1. Hapus flag `guided_tooltip_seen_fa-tax-depreciation-class` untuk akun Total Control
2. Buka tab `Tax Depreciation Class` untuk pertama kali (navigasi baru ke Settings > Accounting > Tax Depreciation Class)

### TC-FA-TDC-649: Walkthrough muncul otomatis pada kunjungan pertama

3. Verifikasi walkthrough muncul otomatis dimulai dari Step 1 of 6

### TC-FA-TDC-648: Isi 6 langkah Guided Tooltip sesuai tabel PRD

Untuk setiap baris tabel isi langkah walkthrough pada Prerequisites (langkah 4 sampai 8), dengan `{N}`, `{target}`, `{Title}`, dan `{Description}` = nilai kolom Step, Target, Title, dan Description pada iterasi itu:

4. Verifikasi indikator `Step {N} of 6`
5. Verifikasi tooltip menyorot `{target}` (spotlight) di atas overlay gelap
6. Verifikasi Title `{Title}`
7. Verifikasi Description `{Description}`
8. Klik `[Next]`

9. Verifikasi indikator `Step 6 of 6`
10. Verifikasi tooltip menyorot icon Changelog di toolbar (spotlight) di atas overlay gelap
11. Verifikasi Title `Changelog`
12. Verifikasi Description `See the history of changes made to tax depreciation classes.`
13. Verifikasi walkthrough tidak berpindah halaman
14. Verifikasi walkthrough tidak membuka dialog
15. Klik `[Done]`

### TC-FA-TDC-651: Walkthrough tidak muncul otomatis setelah flag seen tersimpan

16. Buka tab `Tax Depreciation Class` (navigasi baru ke Settings > Accounting > Tax Depreciation Class)
17. Verifikasi tombol `[?]` tampil di sebelah kanan Breadcrumb
18. Verifikasi walkthrough tidak muncul otomatis

### TC-FA-TDC-650: Guided Tooltip Step 1-4 menyorot header kolom saat tabel dalam Empty State

19. Hapus seluruh Tax Depreciation Class (semua status) dan hapus flag `guided_tooltip_seen_fa-tax-depreciation-class` untuk akun Total Control
20. Buka tab `Tax Depreciation Class` untuk pertama kali (navigasi baru ke Settings > Accounting > Tax Depreciation Class)
21. Verifikasi walkthrough muncul otomatis dimulai dari Step 1 of 6
22. Verifikasi tabel dalam Empty State
23. Verifikasi Step 1 of 6 menyorot header kolom Class Code
24. Klik `[Next]`
25. Verifikasi Step 2 of 6 menyorot header kolom Allowed Methods
26. Klik `[Next]`
27. Verifikasi Step 3 of 6 menyorot header kolom Used By
28. Klik `[Next]`
29. Verifikasi Step 4 of 6 menyorot header kolom Effective From
30. Verifikasi header kolom tampil di atas area Empty State
31. Klik `[Skip]`
32. Pulihkan tujuh class seed bawaan (NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND)

## Notes

- Urutan TC dalam spec: TC-FA-TDC-649, TC-FA-TDC-648, TC-FA-TDC-651, lalu TC-FA-TDC-650. TC-FA-TDC-649 dan TC-FA-TDC-648 berbagi precondition (flag belum ada, tujuh class seed) dan satu kunjungan pertama; `[Done]` pada langkah 15 menyimpan flag seen sehingga TC-FA-TDC-651 (flag sudah true) langsung berlaku; TC-FA-TDC-650 membutuhkan tabel tanpa class dan flag belum ada, sehingga diletakkan di akhir (aksi yang menghapus data di akhir; langkah 32 memulihkan seed).
- Langkah berulang (8b.7): langkah 4 sampai 8 diulang lima kali (satu iterasi per baris tabel isi langkah walkthrough, Step 1 sampai 5); parameter tiap iterasi hanya Step, Target, Title, dan Description, tanpa langkah bersyarat, dan `Verifikasi` tetap satu per klausa (S-01); Step 6 tidak memakai `[Next]` sehingga ditulis eksplisit pada langkah 9 sampai 15. Dengan ekspansi spec ini 52 langkah (32 langkah nominal dan 4 x 5 langkah ulangan).
- Alasan lebih dari sekitar 35 langkah (dengan ekspansi): satu topik (Guided Tooltip), satu kelas harness; keempat TC memakai kunjungan pertama dan flag seen yang sama sehingga tidak dapat dipisah tanpa mengulang pengaturan flag, dan 20 langkah ekspansi berasal dari pengulangan isi enam langkah walkthrough (TC-FA-TDC-648).
- Langkah penghubung (S-03): langkah 1, 2, 16, 19, 20, dan 32 (mengatur flag, membuka layar awal, dan memulihkan seed), langkah 15 (`[Done]` untuk menutup walkthrough dan menyimpan flag seen), langkah 17 (anchor halaman termuat sebelum asersi absence langkah 18), langkah 21 dan 22 (anchor walkthrough muncul dan Empty State; Expected a TC-FA-TDC-650), langkah 31 (menutup walkthrough dengan `[Skip]`).
- Temuan untuk QA:
  - Email akun Total Control tidak tertulis di TC.
  - TC-FA-TDC-648 langkah 1 ("Buka tab untuk pertama kali") tidak menyebut cara menyetel flag seen belum ada; mekanismenya disediakan tim FE/BE (S-13).
  - TC-FA-TDC-648 Expected g ("spotlight di atas overlay gelap") dituliskan per Step pada langkah 5 dan 10; "tidak berpindah halaman" dan "tidak membuka dialog" dituliskan sekali pada langkah 13 dan 14.
  - TC-FA-TDC-650 tidak menyebut teks Empty State; spec hanya mengasersi tabel dalam Empty State.
  - TC-FA-TDC-651 menyebut flag true sebagai precondition tanpa menyebut cara menyetelnya; spec memakai flag yang tersimpan oleh `[Done]` pada langkah 15.
