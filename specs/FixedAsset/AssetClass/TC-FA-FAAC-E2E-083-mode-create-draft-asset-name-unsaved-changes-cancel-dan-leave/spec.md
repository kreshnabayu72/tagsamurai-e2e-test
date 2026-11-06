---
id: TC-FA-FAAC-E2E-083-mode-create-draft-asset-name-unsaved-changes-cancel-dan-leave
title: "Mode Create: Draft Asset Name sebagai Perubahan Belum Disimpan pada Dialog Unsaved Changes"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-260
  - TC-FA-FAAC-261
coverage:
  web: automated
---

# Mode Create: Draft Asset Name sebagai Perubahan Belum Disimpan pada Dialog Unsaved Changes

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip diatur hook suite.
- Data Pre-setup bernama literal (seed idempotent, dipulihkan oleh fixture BE di hook `before` dan `after`): Asset Name tanpa Asset Class: Forklift 3T (6 aset aktif), Laptop Standard (120 aset aktif), Pallet Jack Electric (0 aset aktif); Asset Name "Delivery Van" ter-assign ke 'Vehicles'. Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada, disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed dan pemulihan lewat fixture BE; kemampuan baca BE untuk jumlah Asset Class dan jumlah Asset Name tanpa Asset Class.
- State global: tidak ada yang diubah (draft dibuang lewat [Leave]).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Baca jumlah Asset Class dan jumlah Asset Name tanpa Asset Class sebagai baseline

### TC-FA-FAAC-260: Draft Asset Name dihitung sebagai perubahan belum disimpan: Cancel pada dialog Unsaved Changes

2. Klik tombol "+ Asset Class"
3. Klik tab "Asset Names"
4. Klik tombol "+ Assign Asset Names"
5. Centang "Forklift 3T" dan "Laptop Standard"
6. Klik [Assign]
7. Klik breadcrumb "Asset Class"
8. Verifikasi dialog tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave]
9. Klik [Cancel] pada dialog
10. Verifikasi dialog menutup
11. Verifikasi halaman Add Asset Class tetap terbuka
12. Verifikasi daftar draft tetap memuat "Forklift 3T" dan "Laptop Standard"

### TC-FA-FAAC-261: Leave pada dialog Unsaved Changes membuang draft tanpa meng-assign Asset Name

13. Klik breadcrumb "Asset Class"
14. Verifikasi dialog Unsaved Changes tampil
15. Klik [Leave] pada dialog
16. Verifikasi halaman kembali ke tabel Asset Class tanpa Asset Class baru (jumlah Asset Class sama dengan baseline langkah 1)
17. Verifikasi "Forklift 3T" dan "Laptop Standard" tetap tanpa Asset Class (jumlah Asset Name tanpa Asset Class pada banner sama dengan baseline langkah 1)

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`. Urutan: 260 lalu 261; TC-261 melanjutkan form TC-260 yang masih berisi draft (langkah membuat draft TC-261 sama dengan langkah 2 sampai 6 dan tidak diulang).
- Pengecualian nama literal (S-06, S-12; pengecualian beralasan yang disetujui user): Asset Name seed dipakai apa adanya; spec tidak men-submit Asset Class.
- Langkah penghubung (S-03): langkah 1 (baseline S-12).
- Langkah 14 menjalankan S-08 (verifikasi dialog Unsaved Changes sebelum [Leave]) untuk TC-261.
- Temuan untuk QA: TC-261 tidak menyebut cara membaca banner; spec memakai jumlah dari kemampuan baca BE.
