---
id: TC-FA-LBL-E2E-030-labels-list-chip-label-tampil-penuh-dan-kontras-teks
title: "Labels List: chip Label tampil penuh tanpa truncation dan kontras teks otomatis"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:component-states/label-chip-badge
  - FALB:aksesibilitas/teks-chip-label-memakai-kontras-otomatis
  - FALB:aksesibilitas/warna-label-bukan-satu-satunya-pembawa-i
coverage:
  web: automated
---

# Labels List: chip Label tampil penuh tanpa truncation dan kontras teks otomatis

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `DU-01` (env `FA_TC_EMAIL`, `FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite.
- Data uji: `DU-57` (tiga label `Chip-{runId}-030-nn`). Warna tiga label dipilih dari palet preset PRD §4.3: label bernama 120 karakter berwarna `#3B82F6`, label berwarna terang `#EAB308` (Yellow), dan label berwarna gelap `#64748B` (Slate).
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor dan fixture BE untuk seeding label.
- State global: tidak ada yang diubah. Hook `after` menghapus ketiga label seed `DU-57` lewat sesi API.

## Test Steps

1. Ketik Search `DU-57` (nama dasar `Chip-{runId}-030`), tekan Enter

### FALB:component-states/label-chip-badge: Chip tampil penuh, pill, dan tanpa tooltip

2. Verifikasi Labels List menampilkan tiga baris label `DU-57` (nama 120 karakter, warna terang, dan warna gelap)
3. Verifikasi chip label bernama 120 karakter menampilkan seluruh 120 karakter tanpa pemotongan dan tanpa ellipsis, dan membungkus ke baris berikutnya bila melebihi lebar kolom
4. Verifikasi chip ketiga label berlatar warna hex label masing-masing dan bersudut melengkung penuh (pill)
5. Arahkan kursor ke chip label bernama 120 karakter
6. Verifikasi tidak ada tooltip yang tampil pada chip label bernama 120 karakter
7. Klik `[⋯]` pada baris label bernama 120 karakter, pilih `Edit`
8. Verifikasi Live Preview pada Modal `Edit Label` menampilkan chip berisi seluruh 120 karakter nama tanpa pemotongan dan tanpa ellipsis
9. Arahkan kursor ke chip Live Preview
10. Verifikasi tidak ada tooltip yang tampil pada chip Live Preview
11. Klik `[✕]` pada header Modal Edit Label

### FALB:aksesibilitas/teks-chip-label-memakai-kontras-otomatis: Kontras teks chip otomatis

12. Verifikasi chip label berwarna terang `#EAB308` menampilkan teks hitam `#000000`
13. Verifikasi chip label berwarna gelap `#64748B` menampilkan teks putih `#FFFFFF`

### FALB:aksesibilitas/warna-label-bukan-satu-satunya-pembawa-i: Kode hex tampil di kolom Color Hex

14. Verifikasi kolom Color Hex menampilkan kode hex `#3B82F6`, `#EAB308`, dan `#64748B` pada baris masing-masing ketiga label `DU-57`

## Notes

- Langkah penghubung (S-03): langkah 1 (Search yang mempersempit tabel ke label `DU-57`, R-16) dan langkah 11 (menutup Modal Edit yang tidak diubah).
- Anchor positif (bagian 8b butir 2): langkah 2 sampai 4 membuktikan chip sudah tampil penuh sebelum langkah 6 mengasersi ketiadaan tooltip; langkah 8 menjadi anchor langkah 10.
- Rasio kontras langkah 12 dan 13 dihitung dengan rumus rasio kontras WCAG 2.1 berbasis luminansi relatif (PRD §4.3): latar `#EAB308` memberi rasio sekitar 10,96 terhadap hitam dan sekitar 1,92 terhadap putih, sehingga teks hitam; latar `#64748B` memberi rasio sekitar 4,76 terhadap putih dan sekitar 4,41 terhadap hitam, sehingga teks putih.
- Pembagian klausa lintas spec: klausa kedua `FALB:component-states/label-chip-badge` (chip Label pada kolom Label Tabel 2 `FLD-24` mengikuti truncation badge kontekstual `prd-conventions.md` §9.14) tidak diasersi di spec ini karena permukaannya Drawer Tagged Asset, bukan Labels List dan Live Preview; klausa itu diasersi di spec 043 (pembagian klausa lintas spec).
