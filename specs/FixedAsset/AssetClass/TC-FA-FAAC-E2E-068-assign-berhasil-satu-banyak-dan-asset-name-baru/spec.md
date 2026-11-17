---
id: TC-FA-FAAC-E2E-068-assign-berhasil-satu-banyak-dan-asset-name-baru
title: "Assign Asset Name Tanpa Asset Class Berhasil: Satu, Banyak, dan Asset Name Baru Tidak Ikut Ter-assign"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-151
  - TC-FA-FAAC-152
  - TC-FA-FAAC-636
sourceRules: ["FAAC-LOGIC-13b", "FAAC-LOGIC-01e", "FAAC-LOGIC-14a", "S-13", "§[F-FAAC-08] Assign Asset Names#b2", "FI-11", "T-07", "§4.1.3#r5", "§4.1.3#r6"]
smoke: []
dependsOn: []
trace:
  "FAAC-LOGIC-13b": [10, 23, 30]
  "FAAC-LOGIC-01e": 11
  "FAAC-LOGIC-14a": 13
  "S-13": 13
  "§[F-FAAC-08] Assign Asset Names#b2": [17, 26]
  "FI-11": 18
  "T-07": [21, 29]
  "§4.1.3#r5": 22
  "§4.1.3#r6": 22
anchor: [20, 28]
coverage:
  web: automated
---

# Assign Asset Name Tanpa Asset Class Berhasil: Satu, Banyak, dan Asset Name Baru Tidak Ikut Ter-assign

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip diatur hook suite.
- Data milik spec (seed di hook `before` lewat API, dihapus di hook `after`; kode literal, lihat Notes): Asset Class Active tanpa Asset Name ter-assign, Class Code `ANCHOR-068`, Class Name `Anchor Class {runId}-068` (disebut "anchor"); Asset Name baru `Dock Forklift 2` (Category Machinery > Warehouse) dibuat oleh langkah 8 dan dihapus di hook `after`.
- Data Pre-setup bernama literal (seed idempotent, dipulihkan oleh fixture BE ke tanpa Asset Class di hook `before` dan `after`): Forklift 3T (6 aset aktif), Laptop Standard (120 aset aktif), Pallet Jack Electric (0 aset aktif), Meeting Table (0 aset aktif), Dock Forklift (Machinery > Warehouse). Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada, disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed dan pemulihan lewat fixture BE; sesi API aktor untuk membuat Asset Name baru (lihat `suite.md`); kemampuan baca BE untuk jumlah Asset Name tanpa Asset Class.
- State global: keanggotaan Asset Name tanpa Asset Class dan daftar Asset Name berubah; dipulihkan di hook `after`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAC-636: Memilih Category pada filter picker Assign tidak meng-assign Asset Name baru yang dibuat kemudian

1. Klik link Class Code `ANCHOR-068`, lalu klik tab "Asset Names"
2. Klik "+ Assign Asset Names"
3. Buka Filter, pilih Category "Warehouse"
4. Centang "Dock Forklift"
5. Klik [Assign]
6. Tunggu aksi selesai (dialog Assign menutup)
7. Baca jumlah Asset Name tanpa Asset Class sebagai baseline
8. Buat Asset Name baru "Dock Forklift 2" (Category "Machinery > Warehouse") lewat sesi API aktor hingga tersimpan
9. Muat ulang halaman Detail Asset Class anchor, lalu klik tab "Asset Names"
10. Verifikasi tab Asset Names memuat "Dock Forklift"
11. Verifikasi "Dock Forklift 2" tidak tampil di tab Asset Names (tidak ter-assign otomatis)
12. Klik breadcrumb "Asset Class"
13. Verifikasi banner Asset Name tanpa Asset Class menghitung "Dock Forklift 2" (jumlah naik 1 dari baseline langkah 7)

### TC-FA-FAAC-151: Assign satu Asset Name tanpa Asset Class ke Asset Class Active

14. Klik link Class Code `ANCHOR-068`, lalu klik tab "Asset Names"
15. Klik tombol "+ Assign Asset Names"
16. Centang baris "Forklift 3T"
17. Verifikasi ringkasan menampilkan "1 to assign"
18. Verifikasi Effective From dan pratinjau dampak Hidden
19. Klik [Assign]
20. Verifikasi dialog menutup
21. Verifikasi muncul toast sukses: "Success, asset name has been assigned."
22. Verifikasi tabel tab Asset Names menampilkan "Forklift 3T" dengan Assigned At tanggal hari ini dan Assigned By nama aktor
23. Verifikasi "Forklift 3T" langsung berlaku tanpa Effective From (tidak berstatus terjadwal)

### TC-FA-FAAC-152: Assign tiga Asset Name tanpa Asset Class sekaligus

24. Klik tombol "+ Assign Asset Names"
25. Centang baris "Laptop Standard", "Pallet Jack Electric", dan "Meeting Table"
26. Verifikasi ringkasan menampilkan "3 to assign"
27. Klik [Assign]
28. Verifikasi dialog menutup
29. Verifikasi muncul toast sukses: "Success, asset name has been assigned."
30. Verifikasi ketiga Asset Name tampil di tabel tab Asset Names

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`. Urutan TC dalam spec: 636, 151, 152 (TC-636 mengasersi tab Asset Names hanya memuat "Dock Forklift", sehingga harus dijalankan pada anchor yang masih kosong).
- Pengecualian nama literal (S-06, S-12; pengecualian beralasan yang disetujui user): Asset Name seed Pre-setup dipakai apa adanya; pemulihan oleh fixture BE di hook `after`. `Dock Forklift 2` juga tanpa suffix `{runId}`: nama persis dari TC-FA-FAAC-636 yang diasersi pada banner, dibuat spec ini dan dihapus di hook `after`.
- Class Code `ANCHOR-068` ditulis literal tanpa suffix `{runId}-<NNN>` karena Class Code dibatasi 15 karakter sehingga suffix itu tidak muat (S-12, nama literal; pola spec 047 dan 048); hook `before` menghapus sisa run sebelumnya dan hook `after` menghapus kode itu (cleanup tidak berasumsi setup berhasil penuh).
- Langkah penghubung (S-03): langkah 6 (tunggu aksi selesai, bagian 8b butir 8), 9 (memuat ulang Detail setara "kembali ke Detail" pada TC-636), 12 dan 14 (navigasi). Langkah 7 mencatat baseline jumlah untuk klausa banner.
- Langkah 8: TC-636 menyebut pembuatan Asset Name di Settings > Asset Master > Asset Name; spec membuatnya lewat sesi API aktor (R-20) karena layar itu bukan objek uji.
- Temuan untuk QA: TC-636 tidak menyebut format banner Asset Name tanpa Asset Class; spec mengasersi selisih jumlah dari baseline.
