---
id: TC-FA-FAAC-E2E-058-dialog-form-ikon-x-dan-esc-memunculkan-unsaved-changes
title: "Ikon ✕ dan Esc pada Dialog Form Apply Changes dan Move Asset Names Memunculkan Dialog Unsaved Changes"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-708
  - TC-FA-FAAC-709
sourceRules: ["§4.2f#b2", "§4.1.2#p11", "§4.1.2#p1"]
smoke: []
dependsOn: []
trace:
  "§4.2f#b2": [5, 10, 18, 25, 30]
  "§4.1.2#p11": [5, 7, 10, 12, 18, 25, 27, 30, 32]
  "§4.1.2#p1": 13
anchor: [8, 14, 16, 28, 33, 34]
coverage:
  web: automated
---

# Ikon ✕ dan Esc pada Dialog Form Apply Changes dan Move Asset Names Memunculkan Dialog Unsaved Changes

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca, tidak ada yang disimpan): Asset Class Active `B-BKDROP` dipakai aset: 1 Asset Name dengan 5 aset aktif, Method Straight Line, Useful Life 60, belum pernah diposting, versi terakhir Effective From M-3; Asset Class Active `B-TRUNC` (Class Name `Truncation Fixture`) memiliki Asset Name `Climate Probe` (0 aset aktif); Asset Class Active `VEHICLES` tersedia sebagai tujuan Move. Seed disediakan fixture BE; tiap aksi spec dibuang sehingga Last Updated tidak berubah.
- Bulan berjalan M mengikuti zona waktu General Settings client (NC-11); Accounting Period bulan M-1 tidak berstatus Closed atau belum ada (seed periode akuntansi disediakan fixture BE). Spec tidak mengubah jam server atau jam browser.
- Nilai data mengacu ke `Fixture.fixedAssetAssetClass.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Kemampuan teknis: menekan tombol Esc dan mengklik ikon `✕` pada header dialog.
- Hook dan kemampuan suite (sesi API aktor, seed dan pemulihan lewat fixture BE, flag Guided Tooltip): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-708: Ikon ✕ dan Esc pada dialog Apply Changes (D-11) yang Effective From-nya sudah diubah

1. Ketik Search `B-BKDROP`, tekan Enter
2. Klik link Class Code `B-BKDROP`, klik tab `Depreciation`, ubah Useful Life dari `60` menjadi `48`, lalu klik `[Save]`
3. Pada dialog Apply Changes ubah Effective From dari bulan berjalan (M) ke bulan M-1
4. Klik ikon `✕` di header dialog Apply Changes
5. Verifikasi dialog `Unsaved Changes` tampil di atas dialog `Apply Changes` dengan teks `You have unsaved changes. Are you sure you want to leave?` dan tombol `Cancel` serta `Leave`
6. Klik `[Cancel]` pada dialog `Unsaved Changes`
7. Verifikasi dialog `Unsaved Changes` menutup
8. Verifikasi dialog `Apply Changes` tetap terbuka dengan Effective From M-1
9. Tekan tombol Esc
10. Verifikasi dialog `Unsaved Changes` tampil lagi dengan teks `You have unsaved changes. Are you sure you want to leave?` dan tombol `Cancel` serta `Leave`
11. Klik `[Leave]` pada dialog `Unsaved Changes`
12. Verifikasi dialog `Unsaved Changes` dan dialog `Apply Changes` menutup
13. Verifikasi halaman Detail `B-BKDROP` tampil
14. Verifikasi tidak ada toast
15. Klik tab `Depreciation`
16. Verifikasi Useful Life tetap `48` (hanya isian dialog `Apply Changes` yang dibuang; form Detail tetap memuat perubahan yang belum disimpan)
17. Klik breadcrumb `Asset Class`
18. Verifikasi dialog `Unsaved Changes` dengan tombol `Cancel` dan `Leave`
19. Klik `[Leave]`

### TC-FA-FAAC-709: Ikon ✕ dan Esc pada dialog Move Asset Names (D-14) yang Destination-nya sudah dipilih

20. Ganti isi kotak search dengan `B-TRUNC`, tekan Enter
21. Klik link Class Code `B-TRUNC`, lalu klik tab `Asset Names`
22. Klik ikon `⋯` pada baris `Climate Probe` lalu pilih `Move`
23. Pilih Destination Asset Class `VEHICLES – Vehicles`
24. Klik ikon `✕` di header dialog Move Asset Names
25. Verifikasi dialog `Unsaved Changes` tampil di atas dialog `Move Asset Names` dengan teks `You have unsaved changes. Are you sure you want to leave?` dan tombol `Cancel` serta `Leave`
26. Klik `[Cancel]` pada dialog `Unsaved Changes`
27. Verifikasi dialog `Unsaved Changes` menutup
28. Verifikasi dialog `Move Asset Names` tetap terbuka dengan Destination Asset Class `VEHICLES – Vehicles`
29. Tekan tombol Esc
30. Verifikasi dialog `Unsaved Changes` tampil lagi dengan teks `You have unsaved changes. Are you sure you want to leave?` dan tombol `Cancel` serta `Leave`
31. Klik `[Leave]` pada dialog `Unsaved Changes`
32. Verifikasi dialog `Unsaved Changes` dan dialog `Move Asset Names` menutup
33. Verifikasi `Climate Probe` tetap berada di tabel tab Asset Names `B-TRUNC` (tidak dipindah)
34. Verifikasi tidak ada toast

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-708, 709). Tidak ada TC hanya-BE di spec ini. Pembagian TC lintas spec: TC-FA-FAAC-698 (klik backdrop pada dialog yang sama) ada di spec 057.
- Pengecualian beralasan atas S-06 dan S-12: Asset Class `B-BKDROP`, `B-TRUNC`, `VEHICLES` dan Asset Name `Climate Probe` literal dari TC dipakai apa adanya tanpa suffix `{runId}-<NNN>` karena asersi TC bergantung pada nama; seluruh aksi dibuang sehingga data seed tidak berubah (keputusan yang disetujui user).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan asersi TC): langkah 1 dan 20 (Search untuk menemukan baris target; langkah 20 memakai "ganti isi kotak search" karena kotak Search mempertahankan nilainya sesudah `[Leave]`, 8b.9), langkah 15 (membuka tab Depreciation yang diminta langkah 7 TC-708), langkah 17 sampai 19 (menutup form Detail `B-BKDROP` yang masih dirty lewat dialog `Unsaved Changes`, S-08, S-09; langkah 18 adalah `Verifikasi` dialog yang diwajibkan S-08).
- Langkah 14 dan 34 (tidak ada toast) diletakkan segera setelah anchor yang membuktikan dialog sudah menutup (langkah 12 dan 13, langkah 32 dan 33).
- Temuan untuk QA:
  - TC-708 Expected d menyebut "tidak ada toast" tanpa menyebut jenis toast; spec mengasersi ketiadaan toast apa pun.
