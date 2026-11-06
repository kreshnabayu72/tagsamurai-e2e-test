---
id: TC-FA-FAAC-E2E-070-assign-sebagai-move-dan-pratinjau-dampak
title: "Assign Asset Name yang Sudah di Asset Class Lain Diperlakukan sebagai Move dengan Effective From dan Pratinjau Dampak"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-156
  - TC-FA-FAAC-157
  - TC-FA-FAAC-158
coverage:
  web: automated
---

# Assign Asset Name yang Sudah di Asset Class Lain Diperlakukan sebagai Move dengan Effective From dan Pratinjau Dampak

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip diatur hook suite.
- Data milik spec (seed di hook `before` lewat API setelah menghapus sisa run sebelumnya, dihapus di hook `after`): Asset Class Active tanpa Asset Name ter-assign, Class Code `ANCHOR-070`, Class Name `Anchor Class {runId}-070` (disebut "anchor").
- Data Pre-setup bernama literal (seed idempotent, dipulihkan ke Asset Class semula oleh fixture BE di hook `before` dan `after`): Keadaan awal dinamis (TC-156): Asset Name "Office Chair" (0 aset aktif) ter-assign ke 'Office Equipment (New)' (OFFICE-NEW) lewat fixture BE sebelum blok TC-156; isi OFFICE-NEW selain Office Chair tidak dinyatakan TC-156 dan tidak diasersi; "Delivery Van" (9 aset aktif) dan "Pickup Truck" (3 aset aktif) di 'Vehicles' (VEHICLES); "Forklift 5T" (2 aset aktif) tanpa Asset Class. Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada, disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed dan pemulihan lewat fixture BE; seed periode akuntansi, Last Posted Period, dan Last Exported Period lewat fixture; jam: bulan berjalan (M) dihitung pada zona waktu General Settings client (NC-11).
- State global: keanggotaan Asset Name di Asset Class berubah; dipulihkan di hook `after`.
- Populasi tabel nyata: tabel Asset Class memuat lebih dari 25 baris (seed spec lain ikut tampil), sehingga Class Code target dijangkau lewat Search kode (R-16), bukan lewat posisi baris di halaman 1.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAC-156: Assign Asset Name yang sudah di Asset Class lain tanpa aset aktif diperlakukan sebagai Move

1. Atur keadaan awal lewat fixture BE: Asset Name "Office Chair" (0 aset aktif) ter-assign ke 'Office Equipment (New)' (OFFICE-NEW)
2. Ketik Search `ANCHOR-070`, tekan Enter
3. Klik link Class Code `ANCHOR-070`, lalu klik tab "Asset Names"
4. Klik tombol "+ Assign Asset Names"
5. Hilangkan centang "Without asset class only"
6. Centang baris "Office Chair"
7. Verifikasi ringkasan menampilkan "0 to assign · 1 to move from other asset classes" tanpa bagian "(... with active assets)"
8. Verifikasi Effective From dan pratinjau dampak Hidden
9. Klik [Assign]
10. Verifikasi dialog menutup
11. Verifikasi muncul toast sukses: "Success, asset name has been moved." (bukan toast Assign)
12. Verifikasi "Office Chair" tampil di tab Asset Names Asset Class anchor
13. Klik breadcrumb "Asset Class", lalu ganti isi kotak search dengan `OFFICE-NEW`, tekan Enter
14. Klik link Class Code "OFFICE-NEW", lalu klik tab "Asset Names"
15. Verifikasi tab Asset Names OFFICE-NEW termuat (tabel atau empty state tampil)
16. Verifikasi "Office Chair" tidak lagi tampil di tab Asset Names OFFICE-NEW

### TC-FA-FAAC-157: Assign Asset Name di Asset Class lain dengan aset aktif menampilkan Effective From dan pratinjau dampak

17. Klik breadcrumb "Asset Class", lalu ganti isi kotak search dengan `ANCHOR-070`, tekan Enter
18. Klik link Class Code "ANCHOR-070", lalu klik tab "Asset Names"
19. Klik tombol "+ Assign Asset Names"
20. Hilangkan centang "Without asset class only"
21. Centang baris "Delivery Van"
22. Verifikasi ringkasan menampilkan "0 to assign · 1 to move from other asset classes (1 with active assets)"
23. Verifikasi Effective From tampil dengan nilai awal bulan berjalan
24. Verifikasi pratinjau dampak berlabel "Assets affected" bernilai 9 (jumlah aset aktif Delivery Van)
25. Klik [Assign]
26. Verifikasi dialog menutup
27. Verifikasi muncul toast sukses: "Success, asset name has been moved."
28. Verifikasi "Delivery Van" tampil di tab Asset Names Asset Class anchor
29. Verifikasi "Delivery Van" langsung berlaku saat Confirm (tidak berstatus terjadwal)

### TC-FA-FAAC-158: Assign campuran satu Asset Name tanpa Asset Class dan satu Move dengan aset aktif

30. Klik tombol "+ Assign Asset Names"
31. Hilangkan centang "Without asset class only"
32. Centang baris "Forklift 5T" dan "Pickup Truck"
33. Verifikasi ringkasan menampilkan "1 to assign · 1 to move from other asset classes (1 with active assets)"
34. Verifikasi Effective From tampil dengan nilai awal bulan berjalan
35. Verifikasi pratinjau dampak berlabel "Assets affected" bernilai 3 (3 aset aktif Pickup Truck; 2 aset aktif Forklift 5T tidak dihitung karena berupa Assign)
36. Klik [Assign]
37. Verifikasi dialog menutup
38. Verifikasi muncul toast sukses: "Success, asset name has been moved." (pilihan yang memuat minimal satu Move memakai toast Move)
39. Verifikasi "Forklift 5T" dan "Pickup Truck" tampil di tab Asset Names Asset Class anchor

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`. Urutan: 156, 157, 158 (tiap blok memakai anchor yang sama; Asset Name yang sudah ter-assign tidak dipilih ulang).
- Class Code `ANCHOR-070` ditulis literal tanpa `{runId}` karena Class Code dibatasi 15 karakter (TC-98) sehingga suffix itu tidak muat; `{runId}-070` dipindah ke Class Name agar unik per run (S-12; pola spec 066 sampai 069 dan 047/048); cleanup di hook `before` dan `after`.
- Pengecualian nama literal (S-06, S-12; pengecualian beralasan yang disetujui user): Asset Name dan Asset Class seed (OFFICE-NEW, VEHICLES) dipakai apa adanya dan dipulihkan oleh fixture BE.
- Langkah penghubung (S-03): langkah 1 (penyetel Keadaan awal TC-156 lewat fixture BE), 2, 3, 13, 14, 17, dan 18 (Search kode untuk menemukan baris target, R-16, dan navigasi ke Detail Asset Class).
- Langkah 15 menjadi anchor positif (tab Asset Names OFFICE-NEW termuat) bagi asersi absence langkah 16 (bagian 8b butir 2).
- Temuan untuk QA: nilai awal Effective From "bulan berjalan" tidak disebut format tampilnya; spec mengasersi bulan berjalan pada zona waktu General Settings client.
- Spec di atas 35 langkah (39 langkah): tiga TC satu topik (Assign yang diperlakukan sebagai Move) memakai anchor dan seed yang sama; Expected bermajemuk dipecah satu `Verifikasi` per klausa (S-01) dan enam langkah di antaranya adalah Search kode dan navigasi ke Detail Asset Class (R-16); memecah lagi menggandakan seed anchor tanpa pemisah nyata.
