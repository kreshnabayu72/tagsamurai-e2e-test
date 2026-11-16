---
id: TC-FA-FAAC-E2E-071-assign-campuran-effective-from-dan-pratinjau
title: "Effective From dan Pratinjau Dampak Hanya Muncul bila Pilihan Memuat Move dengan Aset Aktif"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-159
  - TC-FA-FAAC-688
sourceRules: ["FI-11", "FI-12", "§[F-FAAC-08] Assign Asset Names#b2", "FAAC-LOGIC-07k", "F-FAAC-08.k2", "§4.2f#b2"]
smoke: []
dependsOn: []
trace:
  "FI-11": [5, 9]
  "FI-12": 7
  "§[F-FAAC-08] Assign Asset Names#b2": 14
  "FAAC-LOGIC-07k": 15
  "F-FAAC-08.k2": 16
  "§4.2f#b2": [19, 20, 21]
anchor: [18]
coverage:
  web: automated
---

# Effective From dan Pratinjau Dampak Hanya Muncul bila Pilihan Memuat Move dengan Aset Aktif

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip diatur hook suite.
- Data milik spec (seed di hook `before` lewat API setelah menghapus sisa run sebelumnya, dihapus di hook `after`): Asset Class Active tanpa Asset Name ter-assign, Class Code `ANCHOR-071`, Class Name `Anchor Class {runId}-071` (disebut "anchor").
- Data Pre-setup bernama literal (seed idempotent, dipulihkan oleh fixture BE di hook `before` dan `after`): tanpa Asset Class: Forklift 3T (6 aset aktif), Forklift 5T (2 aset aktif); "Delivery Van" (9 aset aktif) dan "Pickup Truck" (3 aset aktif) di 'Vehicles' (VEHICLES); "Wheel Loader" (4 aset aktif) di 'Heavy Equipment' (HEAVY-EQ). Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada, disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed dan pemulihan lewat fixture BE; seed periode akuntansi, Last Posted Period, dan Last Exported Period lewat fixture; jam: bulan berjalan (M) dihitung pada zona waktu General Settings client (NC-11); kemampuan baca BE untuk Asset Class asal sebuah Asset Name.
- State global: tidak ada yang diubah (kedua blok dibatalkan sebelum Assign).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik link Class Code `ANCHOR-071`, lalu klik tab "Asset Names"

### TC-FA-FAAC-159: Effective From dan pratinjau muncul hanya bila pilihan memuat Move dengan aset aktif

2. Klik tombol "+ Assign Asset Names"
3. Hilangkan centang "Without asset class only"
4. Centang "Forklift 3T" (Assign murni)
5. Verifikasi Effective From dan pratinjau dampak Hidden
6. Centang "Delivery Van" (Move dengan aset aktif)
7. Verifikasi Effective From dan pratinjau dampak tampil di bawah tabel
8. Hilangkan centang "Delivery Van"
9. Verifikasi Effective From dan pratinjau dampak Hidden kembali
10. Klik [Cancel]

### TC-FA-FAAC-688: Assign campuran dua Asset Name tanpa Asset Class dan dua Move dari Asset Class berbeda menghitung pratinjau dampak hanya dari Move

11. Klik tombol "+ Assign Asset Names"
12. Hilangkan centang "Without asset class only"
13. Centang baris "Forklift 3T", "Forklift 5T", "Pickup Truck", dan "Wheel Loader"
14. Verifikasi ringkasan menampilkan "2 to assign · 2 to move from other asset classes (2 with active assets)"
15. Verifikasi Effective From tampil dengan nilai awal bulan berjalan
16. Verifikasi pratinjau dampak berlabel "Assets affected" bernilai 7 (3 + 4 aset aktif kedua Move; 6 + 2 aset aktif kedua Asset Name Assign tidak dihitung)
17. Klik [Cancel]
18. Verifikasi dialog menutup
19. Verifikasi tidak ada toast
20. Verifikasi tab "Asset Names" Asset Class anchor tetap kosong
21. Verifikasi keempat Asset Name tidak berpindah: "Pickup Truck" tetap di VEHICLES dan "Wheel Loader" tetap di HEAVY-EQ, "Forklift 3T" dan "Forklift 5T" tetap tanpa Asset Class

## Notes

- Class Code `ANCHOR-071` ditulis literal tanpa `{runId}` karena Class Code dibatasi 15 karakter (TC-98) sehingga suffix itu tidak muat; `{runId}-071` dipindah ke Class Name agar unik per run (S-12; pola spec 066 sampai 069 dan 047/048); cleanup di hook `before` dan `after`.
- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`. Urutan: 159 lalu 688.
- Pengecualian nama literal (S-06, S-12; pengecualian beralasan yang disetujui user): Asset Name dan Asset Class seed dipakai apa adanya; spec tidak mengubahnya (kedua blok berakhir di [Cancel]).
- Langkah penghubung (S-03): langkah 1 (membuka Detail anchor), langkah 10 (menutup dialog TC-159 sebelum TC-688 membuka dialog baru).
- Langkah 7 menjadi anchor positif (Effective From dan pratinjau terbukti dapat tampil) bagi asersi Hidden langkah 9.
- Temuan untuk QA: tidak ada selisih lain.
