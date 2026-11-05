---
id: TC-FA-FAAC-E2E-082-mode-create-draft-asset-name-hapus-satu-dan-clear-field
title: "Mode Create: Hapus Satu Draft Asset Name dan Clear Field Membuang Seluruh Draft"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-257
  - TC-FA-FAAC-258
coverage:
  web: automated
---

# Mode Create: Hapus Satu Draft Asset Name dan Clear Field Membuang Seluruh Draft

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip diatur hook suite.
- Data Pre-setup bernama literal (seed idempotent, dipulihkan oleh fixture BE di hook `before` dan `after`): Asset Name tanpa Asset Class: Forklift 3T (6 aset aktif), Laptop Standard (120 aset aktif), Pallet Jack Electric (0 aset aktif); Asset Name "Delivery Van" ter-assign ke 'Vehicles'. Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada, disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed dan pemulihan lewat fixture BE; kemampuan baca BE untuk Asset Class asal Asset Name.
- State global: tidak ada yang diubah (form Create tidak pernah di-submit).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAC-257: Menghapus satu Asset Name dari daftar draft sebelum Submit

1. Klik tombol "+ Asset Class"
2. Klik tab "Asset Names"
3. Klik tombol "+ Assign Asset Names"
4. Centang "Forklift 3T" dan "Laptop Standard"
5. Klik [Assign]
6. Hapus baris draft "Laptop Standard" dari daftar
7. Verifikasi "Laptop Standard" hilang dari daftar draft
8. Verifikasi "Forklift 3T" tetap tampil di daftar draft

### TC-FA-FAAC-258: Clear Field membuang seluruh draft Asset Name

9. Klik [Clear Field] di footer
10. Klik tombol "+ Assign Asset Names"
11. Centang "Forklift 3T" dan "Laptop Standard"
12. Klik [Assign]
13. Klik [Clear Field] di footer
14. Klik tab "Asset Names"
15. Verifikasi daftar draft tab Asset Names tidak lagi memuat "Forklift 3T" dan "Laptop Standard"
16. Verifikasi "Forklift 3T" dan "Laptop Standard" tidak ter-assign ke Asset Class mana pun

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`. Urutan: 257 lalu 258.
- Pengecualian nama literal (S-06, S-12; pengecualian beralasan yang disetujui user): Asset Name seed dipakai apa adanya; spec tidak meng-submit Asset Class.
- Langkah penghubung (S-03): langkah 9 (membuang draft TC-257 agar TC-258 memulai dari draft kosong; langkah 10 sampai 12 menyalin langkah assign TC-258).
- Langkah 14 mengikuti TC-258 (klik ulang tab Asset Names).
- Temuan untuk QA: TC-257 dan TC-258 tidak menyebut apakah form Create dirty setelah Clear Field; spec mengakhiri tanpa dialog Unsaved Changes karena draft sudah dibuang.
