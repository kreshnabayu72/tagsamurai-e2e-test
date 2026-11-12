---
id: TC-FA-FAAC-E2E-184-resilience-assign
title: "Resilience: Assign Asset Name Gagal karena Error Server, Dialog Tetap Terbuka, dan Assign Diulang setelah Kegagalan Sebagian"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-165
  - TC-FA-FAAC-166
  - TC-FA-FAAC-167
coverage:
  web: automated
---

# Resilience: Assign Asset Name Gagal karena Error Server, Dialog Tetap Terbuka, dan Assign Diulang setelah Kegagalan Sebagian

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata)
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Kemampuan teknis: `Spectra.intercept` parsial yang memaksa respons HTTP 5xx pada permintaan Assign di atas backend nyata (TC-165 dan TC-166), dilepas segera sesudah pemicu (S-09); fixture BE yang memaksa kegagalan Assign sesudah Asset Name pertama berhasil diproses dan mematikannya kembali (TC-167, "disediakan tim FE/BE", tanpa endpoint karangan). Pembacaan keanggotaan Asset Name lewat kemampuan baca BE.
- Data Dinamis milik spec: Asset Class anchor Class Code literal `B-ANC` dan Class Name `Anchor Class {runId}-184` (Active, tanpa Asset Name ter-assign; ini "Asset Class anchor" TC-165 sampai TC-167), dibuat fixture BE di hook `before` (setelah menghapus sisa run sebelumnya) dan dihapus di hook `after`.
- Data seed Pre-setup (nama literal TC, disediakan fixture BE): Asset Name tanpa Asset Class `Forklift 3T` (6 aset aktif; Machinery > Warehouse; Label Warehouse, Insured), `Forklift 5T` (2 aset aktif; Machinery > Warehouse; Label Warehouse), `Laptop Standard` (120 aset aktif; IT > Devices; IT, Portable), `Pallet Jack Electric` (0 aset aktif), `Meeting Table` (0 aset aktif); Asset Name `Office Chair` (0 aset aktif) ter-assign ke `Office Equipment (New)` (`OFFICE-NEW`), disetel fixture BE pada langkah 12 (precondition butir d TC-FA-FAAC-166). Assign TC-167 yang berhasil mengubah keanggotaan; fixture BE memulihkan seed di hook `after`.
- Nilai data mengacu ke `Fixture.fixedAssetAssetClass.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Hook dan kemampuan suite (flag Guided Tooltip, seed dan fixture BE): dinyatakan sekali di suite.md; suite serial (`parallel: false`).

## Test Steps

### TC-FA-FAAC-165: Assign gagal karena error server, dialog tetap terbuka dan pilihan dipertahankan

1. Ketik Search `B-ANC`, tekan Enter
2. Klik link Class Code `B-ANC`, lalu klik tab `Asset Names`
3. Klik tombol `+ Assign Asset Names`
4. Centang `Meeting Table` dan `Pallet Jack Electric`
5. Pasang intercept respons 5xx pada permintaan Assign, lalu klik `[Assign]`
6. Lepas intercept respons 5xx
7. Verifikasi toast error `Error, failed to assign asset name.`
8. Verifikasi dialog Assign tetap terbuka dengan kedua baris tetap tercentang
9. Verifikasi `[Assign]` kembali aktif untuk dicoba ulang
10. Klik `[×]` pada dialog Assign
11. Verifikasi tidak ada Asset Name yang tampil di tab `Asset Names`

### TC-FA-FAAC-166: Assign yang memuat Move gagal karena error server memakai toast gagal Move

12. Setel keadaan awal lewat fixture BE: `Office Chair` (0 aset aktif) ter-assign ke `Office Equipment (New)` (`OFFICE-NEW`) (precondition butir d TC-FA-FAAC-166)
13. Klik tombol `+ Assign Asset Names`
14. Hilangkan centang `Without asset class only`, lalu centang `Office Chair`
15. Pasang intercept respons 5xx pada permintaan Assign, lalu klik `[Assign]`
16. Lepas intercept respons 5xx
17. Verifikasi toast error `Error, failed to move asset name.`
18. Verifikasi dialog tetap terbuka dengan pilihan `Office Chair` dipertahankan
19. Verifikasi `Office Chair` tetap berada di `Office Equipment (New)`
20. Klik `[×]` pada dialog Assign

### TC-FA-FAAC-167: Assign diulang setelah kegagalan sebagian hanya memproses Asset Name yang belum diproses

21. Klik tombol `+ Assign Asset Names`
22. Centang `Laptop Standard`, `Pallet Jack Electric`, dan `Meeting Table`
23. Lewat fixture BE, siapkan kegagalan setelah Asset Name pertama berhasil diproses, lalu klik `[Assign]`
24. Verifikasi toast error `Error, failed to assign asset name.`
25. Verifikasi dialog tetap terbuka dengan pilihan dipertahankan
26. Klik `[×]` pada dialog Assign
27. Muat ulang daftar tab `Asset Names`
28. Verifikasi hanya 1 Asset Name yang tampil di tab `Asset Names`
29. Klik tombol `+ Assign Asset Names`
30. Centang dua Asset Name yang tersisa
31. Matikan fixture kegagalan, lalu klik `[Assign]`
32. Verifikasi toast sukses `Success, asset name has been assigned.`
33. Verifikasi ketiga Asset Name tampil tepat sekali di tab `Asset Names`
34. Verifikasi jumlah Asset Name pada Asset Class sama dengan jumlah baris yang tampil (tidak ada penghitungan ganda)

## Notes

1. Subjudul `###` memetakan langkah ke id TC granular.
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 (Search untuk menemukan baris target, R-16; link Class Code `B-ANC` dipilih dengan kecocokan teks persis karena Search juga menampilkan `B-ANCHOR`); langkah 12 (fixture BE menyetel keadaan awal dinamis TC-166, S-14, bukan bagian TC); langkah 10, 20, dan 26 (menutup dialog Assign; picker D-13 menutup tanpa konfirmasi menurut TC-154 dan TC-712); langkah 27 (muat ulang daftar, sesuai langkah TC-167). Intercept dilepas segera sesudah pemicu (langkah 6 dan 16; S-09).
3. TC-165 sampai TC-167 menyebut "Asset Class anchor (hasil TC anchor Create Asset Class valid)"; spec memakai Asset Class milik spec `B-ANC` yang dibuat fixture BE (S-06); Class Code literal karena dibatasi 15 karakter sehingga `B-ANC{runId}-184` tidak muat, `{runId}-184` dipindah ke Class Name (S-12; pola spec 066 sampai 069). Nama Asset Name seed dipakai apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada nama itu (pengecualian beralasan S-06/S-12).
4. Temuan untuk QA: TC-166 tidak menyebut kolom Effective From pada Assign yang memuat Move; spec mengikuti TC dan tidak mengisinya (`Office Chair` 0 aset aktif). TC-167 tidak menyebut kapan fixture kegagalan dimatikan relatif terhadap dialog yang tertutup; spec mematikannya tepat sebelum klik `[Assign]` kedua sesuai urutan langkah TC. Post Condition TC-167 ("Tiga Asset Name ter-assign tepat sekali; jumlah Asset Name dan Assets konsisten") diasersi melalui Expected c. Jumlah Assets pada Post Condition tidak punya langkah observasi dan tidak diasersi.
