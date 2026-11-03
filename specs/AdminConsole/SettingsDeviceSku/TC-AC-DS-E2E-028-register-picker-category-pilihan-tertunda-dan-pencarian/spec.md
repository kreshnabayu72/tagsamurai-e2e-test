---
id: TC-AC-DS-E2E-028-register-picker-category-pilihan-tertunda-dan-pencarian
title: "Register SKU: Pilihan Node Category, Pilihan Tertunda sampai Select, Pencarian Picker, dan Section Kondisional"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-90
  - TC-AC-DS-91
  - TC-AC-DS-92
  - TC-AC-DS-93
coverage:
  web: automated
---

# Register SKU: Pilihan Node Category, Pilihan Tertunda sampai Select, Pencarian Picker, dan Section Kondisional

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima `totalControlSku_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Jane Setiawan`), password `Spectra.env.AC_DS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (dibaca saja, tidak diubah): pohon Category #25, Device Name #26, Brand #27, file foto #37, SKU inti #29 dan seed #30. Dirujuk lewat fixture `fixtures/settings-device-sku.json` (disediakan tim FE, belum ada). Spec ini tidak menyimpan SKU: popup Register SKU ditutup lewat `[✕]` dan `[Leave]`.
- Kemampuan teknis: membaca DOM popup (atribut `aria-hidden` dan keberadaan elemen) untuk TC-93, disediakan tim FE.
- Env var `AC_DS_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; pendaftarannya disediakan tim FE.
- Suite berjalan serial (`parallel: false`); hook suite sesuai `suite.md`. Tidak ada seeding dan tidak ada state global yang diubah.

## Test Steps

### TC-AC-DS-90: Node yang punya anak dapat dipilih

1. Klik tombol `[+ SKU]` pada toolbar
2. Klik field Category
3. Expand node `Hardware`
4. Klik node `Handheld Reader`
5. Verifikasi node `Handheld Reader` ter-highlight dengan latar dan teks bold/primary
6. Klik `[Select]`
7. Verifikasi field Category menampilkan `Handheld Reader`
8. Verifikasi section Range Type muncul karena ancestry Handheld Reader

### TC-AC-DS-91: Pilihan tertunda sampai [Select]

9. Klik `[Clear Field]`
10. Klik field Category
11. Expand node `TAG` dan `NFC`, lalu klik node `Asset TAG` tanpa menekan `[Select]`
12. Klik `[Cancel]` pada picker
13. Verifikasi field Category menampilkan placeholder "Select category"
14. Verifikasi tidak ada section kondisional
15. Klik field Category
16. Verifikasi node `Asset TAG` tidak ter-highlight karena pilihan tidak tersimpan

### TC-AC-DS-92: Pencarian pada picker Category

17. Ketik `Tunnel` pada kotak pencarian picker
18. Verifikasi hanya node `Tunnel Reader` beserta parent `Smart Fixed Reader` dan `Hardware` yang tampil
19. Verifikasi node yang tidak cocok (`UHF Handheld`, `Asset TAG`, dan lainnya) disembunyikan
20. Klik `[Cancel]` pada picker

### TC-AC-DS-93: Section kondisional

21. Verifikasi section Range Type, Port, dan This is User TAG tidak dirender
22. Verifikasi elemen kondisional yang tidak relevan memakai aria-hidden="true"
23. Klik field Category
24. Expand node `Hardware`
25. Klik node `BLE Gateway`
26. Klik `[Select]`
27. Verifikasi tidak ada section tambahan karena BLE Gateway tidak punya field kondisional
28. Klik ikon close `[✕]`
29. Verifikasi dialog `Unsaved Changes` tampil
30. Klik `[Leave]`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC dalam spec: TC-90, TC-91, TC-92, TC-93. Keempatnya memakai satu pembukaan popup Register SKU; popup ditutup satu kali di langkah 28 sampai 30 (S-08).
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1 sampai 4, 6, 10, 11, 15, 17, 23 sampai 26 (membuka popup, picker, dan memilih node; hasilnya diasersi pada langkah berikutnya), langkah 9 (`[Clear Field]` mengosongkan Category sebelum TC-91 mengandalkan field kosong, S-09), langkah 12 dan 20 (menutup picker lewat `[Cancel]`).
- Asersi absence langkah 14 didahului langkah 13 (field Category tampil); langkah 19 didahului langkah 18; langkah 21 didahului langkah 20 (picker tertutup dan popup tampil dengan field Category).
- Temuan untuk QA:
  - S-12: asersi memakai nama literal Pre-setup #25 karena TC menetapkannya; Lampiran A tidak memuat pengecualian nama literal untuk modul ini (menunggu keputusan).
  - Fixture rancangan: ketersediaan Pre-setup #25/#26/#27/#37 di environment belum diverifikasi.
  - TC-93 Expected a menyebut section "tidak dirender" sekaligus "memakai aria-hidden="true""; kedua klausa saling bersinggungan (elemen yang tidak dirender tidak punya atribut). Spec mengasersi keduanya sesuai TC dan menandai ambiguitas ini; interpretasi disediakan tim FE.
  - TC-91 langkah 4 mengisi pilihan tanpa `[Select]` dan Expected b ("pilihan tidak tersimpan") tidak merinci cara mengamati; langkah 15 dan 16 membuka kembali picker dan memeriksa highlight.
  - TC-92 tidak menyebut Enter pada pencarian picker; spec mengikuti TC.
  - Env var `AC_DS_*` (akun #1 sampai #23) belum terdaftar; email akun berbeda dari akun Admin Console yang sudah ada.
