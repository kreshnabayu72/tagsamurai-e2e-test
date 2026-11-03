---
id: TC-FA-CAT-E2E-004-sidebar-collapse-state-tersimpan-tablet-aksesibilitas
title: "Sidebar Collapse, State Tersimpan, Viewport Tablet, dan Aksesibilitas Pohon Kategori"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-19
  - TC-FA-CAT-18
  - TC-FA-CAT-20
  - TC-FA-CAT-21
coverage:
  web: automated
---

# Sidebar Collapse, State Tersimpan, Viewport Tablet, dan Aksesibilitas Pohon Kategori

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data: client CatMain (Pre-setup #20, plan Enterprise): 15 kategori; L1 `Accessory`, `Default Category`, `Electronics` (anak `Laptop`, `Monitor`), `Furniture`, `Peripheral` (anak `Keyboard`, `Mouse`), `Spare Part`, `Tools`, `Vehicle`. Spec hanya membaca; tidak membuat atau mengubah data.
- State awal: preferensi Open/Collapsed sidebar halaman Categories untuk akun Total Control belum pernah disetel (kunjungan pertama); direset di hook `before` dan dihapus lagi di hook `after`. Kemampuan reset preferensi disediakan tim FE (S-13).
- Kemampuan teknis: mengubah lebar viewport browser (1000px dan 1400px) serta inspeksi atribut DOM.
- Flag Guided Tooltip halaman Categories: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan client Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-categories.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-19: State Open/Collapsed sidebar disimpan per user per halaman dan kunjungan pertama Open

1. Verifikasi sidebar berstatus Open pada kunjungan pertama
2. Klik Floating Toggle di tepi kiri panel sidebar
3. Tekan F5
4. Verifikasi sidebar tetap collapsed setelah F5
5. Buka menu lain lalu kembali ke Fixed Asset > Settings > Categories
6. Verifikasi sidebar tetap collapsed setelah kembali dari menu lain
7. Klik Floating Toggle untuk membuka sidebar kembali

### TC-FA-CAT-18: Sidebar dapat di-collapse dan dibuka kembali lewat Floating Toggle dengan tooltip konsisten

8. Klik Floating Toggle di tepi kiri panel sidebar
9. Verifikasi panel sidebar tersembunyi
10. Verifikasi toggle pindah ke tepi kanan layar dengan ikon ◀
11. Verifikasi konten tabel melebar penuh
12. Hover toggle pada keadaan collapsed
13. Verifikasi tooltip toggle `Open Category Tree`
14. Klik toggle untuk membuka kembali
15. Verifikasi panel sidebar tampil kembali dengan ikon ▶
16. Hover toggle pada keadaan terbuka
17. Verifikasi tooltip toggle `Collapse Category Tree`

### TC-FA-CAT-20: Viewport tablet menyembunyikan sidebar sementara tanpa menimpa preferensi tersimpan

18. Set viewport lebar 1000px
19. Verifikasi sidebar collapse menjadi toggle icon pada lebar 1000px (rentang 768-1279px)
20. Kembalikan viewport ke lebar 1400px
21. Verifikasi sidebar kembali memakai preferensi tersimpan terakhir (Open) tanpa klik toggle

### TC-FA-CAT-21: Accessibility pohon kategori: role tree, treeitem, dan aria-expanded

22. Inspeksi atribut DOM panel sidebar
23. Verifikasi container pohon memiliki atribut role `tree`
24. Verifikasi tiap node memiliki role `treeitem`
25. Expand node `Electronics` lalu inspeksi ulang atribut DOM
26. Verifikasi node `Electronics` memiliki aria-expanded `true` saat expanded
27. Collapse node `Electronics` lalu inspeksi ulang atribut DOM
28. Verifikasi node `Electronics` memiliki aria-expanded `false` saat collapsed

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Penyimpangan urutan (S-10): TC-FA-CAT-19 diletakkan sebelum TC-FA-CAT-18 karena kunjungan pertama (preferensi belum tersimpan) hanya teramati sekali; urutan akhir TC-FA-CAT-19, 18, 20, 21.
- Langkah penghubung (S-03): langkah 7 (membuka sidebar kembali agar TC-FA-CAT-18 mulai dari keadaan Open) dan langkah 20 (mengembalikan viewport ke 1400px, juga bagian dari LK TC-FA-CAT-20).
- Temuan untuk QA:
  - TC-FA-CAT-19 mensyaratkan user yang belum pernah menutup sidebar tanpa menyebut cara menyiapkannya; spec menuliskan reset preferensi sebagai kemampuan yang disediakan tim FE.
  - TC-FA-CAT-21 tidak menyebut keadaan awal node `Electronics` (expanded atau collapsed); spec hanya mengasersi aria-expanded sesudah expand dan sesudah collapse.
  - TC-FA-CAT-20 menyebut rentang 768-1279px untuk nilai 1000px; spec memakai 1000px dan 1400px sesuai Data Uji.
- Ukuran spec 28 langkah, di bawah ambang sekitar 35.
