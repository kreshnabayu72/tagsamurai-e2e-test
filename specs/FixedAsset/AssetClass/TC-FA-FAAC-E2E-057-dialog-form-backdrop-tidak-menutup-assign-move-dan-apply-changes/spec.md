---
id: TC-FA-FAAC-E2E-057-dialog-form-backdrop-tidak-menutup-assign-move-dan-apply-changes
title: "Klik Backdrop pada Dialog Form Assign Asset Names, Move Asset Names, dan Apply Changes Tidak Menutup Dialog"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAC-698
coverage:
  web: automated
---

# Klik Backdrop pada Dialog Form Assign Asset Names, Move Asset Names, dan Apply Changes Tidak Menutup Dialog

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca, tidak ada yang disimpan): Asset Class Active `B-TRUNC` (Class Name `Truncation Fixture`) memiliki Asset Name `Climate Probe` (0 aset aktif) sebagai satu-satunya Asset Name; Asset Name tanpa Asset Class `Meeting Table` (0 aset aktif); Asset Class Active `VEHICLES` tersedia sebagai tujuan Move; Asset Class Active `B-BKDROP` dipakai aset: 1 Asset Name dengan 5 aset aktif, Method Straight Line, Useful Life 60, belum pernah diposting, versi terakhir Effective From M-3. Seed disediakan fixture BE; tiap aksi spec dibatalkan sehingga Last Updated tidak berubah.
- Bulan berjalan M mengikuti zona waktu General Settings client (NC-11); Accounting Period bulan M-1 tidak berstatus Closed atau belum ada (seed periode akuntansi disediakan fixture BE). Spec tidak mengubah jam server atau jam browser.
- Nilai data mengacu ke `Fixture.fixedAssetAssetClass.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Kemampuan teknis: mengklik area backdrop di luar dialog.
- Hook dan kemampuan suite (sesi API aktor, seed dan pemulihan lewat fixture BE, flag Guided Tooltip): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-698: Klik backdrop pada dialog Assign Asset Names (D-13), Move Asset Names (D-14), dan Apply Changes (D-11)

1. Ketik Search `B-TRUNC`, tekan Enter
2. Klik link Class Code `B-TRUNC`, lalu klik tab `Asset Names`
3. Klik tombol `[+ Assign Asset Names]` dan centang baris `Meeting Table`
4. Klik area backdrop di luar dialog
5. Verifikasi dialog `Assign Asset Names to Truncation Fixture` tetap terbuka
6. Verifikasi baris `Meeting Table` tetap tercentang
7. Verifikasi dialog Unsaved Changes tidak muncul
8. Klik `[Cancel]` pada dialog
9. Verifikasi dialog menutup
10. Verifikasi dialog Unsaved Changes tidak muncul
11. Verifikasi tabel tab Asset Names tetap memuat `Climate Probe` saja (tidak ada Asset Name yang di-assign)
12. Klik ikon `⋯` pada baris `Climate Probe` lalu pilih `Move`
13. Pilih Destination Asset Class `VEHICLES – Vehicles`
14. Klik area backdrop di luar dialog
15. Verifikasi dialog `Move Asset Names` tetap terbuka
16. Verifikasi Destination Asset Class tetap `VEHICLES – Vehicles`
17. Verifikasi dialog Unsaved Changes tidak muncul
18. Klik `[Cancel]` pada dialog
19. Verifikasi dialog menutup
20. Verifikasi dialog Unsaved Changes tidak muncul
21. Verifikasi tabel tab Asset Names tetap memuat `Climate Probe` saja (tidak ada Asset Name yang dipindah)
22. Klik breadcrumb `Asset Class`
23. Ganti isi kotak search dengan `B-BKDROP`, tekan Enter
24. Klik link Class Code `B-BKDROP`, klik tab `Depreciation`, ubah Useful Life dari `60` menjadi `48`, lalu klik `[Save]`
25. Pada dialog Apply Changes ubah Effective From dari bulan berjalan (M) ke bulan M-1
26. Klik area backdrop di luar dialog
27. Verifikasi dialog `Apply Changes` tetap terbuka
28. Verifikasi Effective From tetap M-1
29. Verifikasi dialog Unsaved Changes tidak muncul
30. Klik `[Cancel]` pada dialog
31. Verifikasi dialog `Apply Changes` menutup
32. Verifikasi dialog Unsaved Changes tidak muncul
33. Klik breadcrumb `Asset Class`
34. Verifikasi dialog `Unsaved Changes` dengan tombol `Cancel` dan `Leave`
35. Klik `[Leave]`
36. Klik link Class Code `B-BKDROP` dan klik tab `Depreciation`
37. Verifikasi Useful Life tetap `60` (perubahan tidak tersimpan)

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-698). Tidak ada TC hanya-BE di spec ini.
- Spec ini 37 langkah, di atas 35 langkah. Alasan: satu TC (TC-FA-FAAC-698) dengan tiga dialog yang tiap-tiapnya memerlukan klik backdrop, `[Cancel]`, dan asersi ketiadaan dialog `Unsaved Changes` (Expected a sampai d, S-01); satu TC tidak boleh dipecah lintas spec (check-suite C2) dan tidak ada langkah yang dapat dihapus tanpa mengurangi Expected.
- Pengecualian beralasan atas S-06 dan S-12: Asset Class `B-TRUNC`, `B-BKDROP`, `VEHICLES` dan Asset Name `Climate Probe`, `Meeting Table` literal dari TC dipakai apa adanya tanpa suffix `{runId}-<NNN>` karena asersi TC bergantung pada nama; seluruh aksi dibatalkan sehingga data seed tidak berubah (keputusan yang disetujui user).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan asersi TC): langkah 1 dan 23 (Search untuk menemukan baris target; langkah 23 memakai "ganti isi kotak search" karena kotak Search mempertahankan nilainya sesudah breadcrumb, 8b.9), langkah 22 (kembali ke tabel; form `B-TRUNC` tidak dirty), langkah 33 dan 35 (menutup form dirty lewat dialog `Unsaved Changes`, S-08; langkah 34 adalah `Verifikasi` dialog yang diwajibkan S-08), langkah 36 (membuka ulang `B-BKDROP` untuk langkah 13 TC).
- Langkah 5, 9, 15, 19, 27, dan 31 menjadi anchor positif untuk asersi absence dialog `Unsaved Changes` sesudahnya (8b.2, 8b.11).
- Temuan untuk QA:
  - TC-698 Expected d menyebut "tabel tab Asset Names tidak berubah" tanpa baseline; spec membandingkan terhadap isi seed (`Climate Probe` saja).
