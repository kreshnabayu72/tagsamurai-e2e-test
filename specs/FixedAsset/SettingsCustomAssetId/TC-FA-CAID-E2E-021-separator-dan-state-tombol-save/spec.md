---
id: TC-FA-CAID-E2E-021-separator-dan-state-tombol-save
title: "Dropdown Separator dan State Tombol Save Pristine"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-68
  - TC-FA-CAID-69
  - TC-FA-CAID-70
  - TC-FA-CAID-71
coverage:
  web: automated
---

# Dropdown Separator dan State Tombol Save Pristine

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control Company Alpha (Pre-setup No 1, `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`); halaman Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip disetel seen untuk akun UI suite; konfigurasi Company Alpha dipulihkan ke baseline B1 di `beforeEach` dan `after` lewat sesi API aktor (klien HTTP dan token sesi API disediakan tim FE; token tidak dihitung sebagai sesi web).
- Data Pre-setup No 10: baseline B1 (Master Switch ON, Separator `/ (Slash)`, segmen tercentang Group Code, Category Code, Asset Name Code, Purchase Date, Asset Increment, tanpa Initial Company). TC-FA-CAID-70 memakai baseline B1 dengan Master Switch OFF, di-seed lewat sesi API aktor pada langkah 24. Nilai dibaca dari `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE): konfirmasi otomatis dialog `beforeunload` bawaan browser oleh harness untuk muat ulang pada form yang belum disimpan (langkah 19 dan 24).
- State: spec ini tidak menekan `[Save]`; satu-satunya perubahan tersimpan adalah Master Switch OFF dari seed langkah 24, dipulihkan hook `after` suite.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-68: Dropdown Separator: nilai terpilih dan enam opsi berurutan

1. Buka dropdown `Separator *`
2. Verifikasi nilai terpilih saat dibuka adalah `/ (Slash)`
3. Verifikasi label field `Separator *`
4. Verifikasi daftar opsi berurutan: `/ (Slash)`, `- (Dash)`, `. (Dot)`, `_ (Underscore)`, `Space`, `None`
5. Verifikasi placeholder `Select separator` tidak tampil karena opsi default terpilih

### TC-FA-CAID-69: Pilihan Separator memperbarui Live Preview

6. Pilih `/ (Slash)` pada dropdown `Separator *` yang masih terbuka
7. Verifikasi Live Preview menampilkan `JKT/LAP/T490/0926/1`
8. Buka dropdown `Separator *` dan pilih `- (Dash)`
9. Verifikasi Live Preview menampilkan `JKT-LAP-T490-0926-1`
10. Buka dropdown `Separator *` dan pilih `. (Dot)`
11. Verifikasi Live Preview menampilkan `JKT.LAP.T490.0926.1`
12. Buka dropdown `Separator *` dan pilih `_ (Underscore)`
13. Verifikasi Live Preview menampilkan `JKT_LAP_T490_0926_1`
14. Buka dropdown `Separator *` dan pilih `Space`
15. Verifikasi Live Preview menampilkan `JKT LAP T490 0926 1`
16. Verifikasi Live Preview tanpa spasi tambahan di kiri-kanan pemisah
17. Buka dropdown `Separator *` dan pilih `None`
18. Verifikasi Live Preview menampilkan `JKTLAPT49009261` bersambung tanpa pemisah
19. Pilih kembali Separator `/ (Slash)`, lalu muat ulang halaman

### TC-FA-CAID-71: Tombol Save disabled saat pristine dan aktif setelah perubahan

20. Verifikasi tombol `[Save]` berstatus disabled
21. Centang `Division Code`
22. Verifikasi tombol `[Save]` berstatus aktif
23. Hilangkan centang `Division Code`

### TC-FA-CAID-70: Dropdown Separator disabled saat Master Switch OFF

24. Setel Master Switch OFF pada konfigurasi Company Alpha lewat sesi API aktor hingga tersimpan, lalu muat ulang halaman
25. Klik dropdown `Separator *`
26. Verifikasi Live Preview redup menampilkan `1`
27. Verifikasi dropdown tidak terbuka karena disabled

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Perubahan urutan TC: TC-FA-CAID-71 dijalankan sebelum TC-FA-CAID-70 karena TC-FA-CAID-70 membutuhkan Master Switch OFF tersimpan, sedangkan TC-FA-CAID-71 membutuhkan form pristine pada Master Switch ON (S-05/S-10). Di dalam TC-FA-CAID-70, `Verifikasi` Live Preview redup (langkah 26) ditulis sebelum dropdown tidak terbuka (langkah 27) agar Live Preview menjadi anchor positif untuk asersi absence.
- Langkah penghubung (tanpa `Verifikasi`): langkah 19 (mengembalikan Separator ke nilai tersimpan dan memuat ulang agar form pristine untuk TC-FA-CAID-71; Save tetap aktif setelah nilai dikembalikan, jadi muat ulang diperlukan), langkah 23 (memulihkan centang Division Code), dan langkah 24 (seed Master Switch OFF).
- Langkah 6 memilih opsi pada dropdown yang dibuka langkah 1 (opsi `/ (Slash)` sudah terpilih sebelum dipilih).
- Pola berulang pada TC-FA-CAID-69: langkah 8 sampai 18 (satu pasangan buka-pilih dan `Verifikasi` per opsi).
- Temuan untuk QA:
  - TC-FA-CAID-70 menulis baseline sebagai "baseline B1 status OFF"; Tabel Pre-setup No 10 tidak mendefinisikan B1 dengan Master Switch OFF. Spec memakai B1 dengan Master Switch OFF.
  - TC-FA-CAID-69 e ("tanpa spasi tambahan di kiri-kanan pemisah") ditulis sebagai `Verifikasi` terpisah (langkah 16) dari nilai Live Preview.
