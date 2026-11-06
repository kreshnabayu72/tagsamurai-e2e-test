---
id: TC-FA-FAAC-E2E-054-unsaved-changes-form-edit-breadcrumb-dan-nilai-kembali
title: "Unsaved Changes pada Form Edit: Breadcrumb dengan Cancel dan Leave, serta Nilai yang Dikembalikan Identik"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-659
  - TC-FA-FAAC-660
  - TC-FA-FAAC-663
coverage:
  web: automated
---

# Unsaved Changes pada Form Edit: Breadcrumb dengan Cancel dan Leave, serta Nilai yang Dikembalikan Identik

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Pre-setup (diubah hanya di form, tidak pernah disimpan): Asset Class `B-ANCHOR` (Active) tersimpan dengan Class Name `Anchor Heavy Equipment`, disediakan fixture BE sebelum spec; Last Updated `B-ANCHOR` tidak berubah.
- Kemampuan teknis: membaca jumlah entri Changelog `B-ANCHOR`, System Log aktor, dan Activity Log FAMS lewat fixture BE sebelum dan sesudah aksi (audit trail permanen, jumlah absolut tidak diasersi; disediakan tim FE/BE).
- Nilai data mengacu ke `Fixture.fixedAssetAssetClass.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Hook dan kemampuan suite (sesi API aktor, seed dan pemulihan lewat fixture BE, flag Guided Tooltip): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Ketik Search `B-ANCHOR`, tekan Enter

### TC-FA-FAAC-659: Breadcrumb pada Edit yang sudah diubah: Cancel mempertahankan form

2. Catat jumlah entri Changelog `B-ANCHOR` (N1), System Log aktor (Ns1), dan Activity Log FAMS (Na1) lewat fixture BE
3. Klik link Class Code `B-ANCHOR` di tabel
4. Ubah Class Name menjadi `Anchor Edited` tanpa klik `[Save]`
5. Klik breadcrumb `Asset Class`
6. Verifikasi dialog tampil dengan teks `You have unsaved changes. Are you sure you want to leave?` dan tombol `Cancel` serta `Leave`
7. Klik `[Cancel]`
8. Verifikasi dialog menutup
9. Verifikasi Detail Edit `B-ANCHOR` tetap terbuka dengan Class Name `Anchor Edited`
10. Verifikasi tidak ada toast
11. Verifikasi jumlah entri Changelog `B-ANCHOR` tetap N1 (selisih 0)
12. Verifikasi jumlah entri System Log aktor tetap Ns1 (selisih 0)
13. Verifikasi jumlah entri Activity Log FAMS tetap Na1 (selisih 0)

### TC-FA-FAAC-660: Breadcrumb pada Edit yang sudah diubah: Leave membuang perubahan

14. Catat jumlah entri Changelog `B-ANCHOR` (N2), System Log aktor (Ns2), dan Activity Log FAMS (Na2) lewat fixture BE
15. Klik breadcrumb `Asset Class` (form masih berisi Class Name `Anchor Edited` yang belum disimpan)
16. Verifikasi dialog tampil dengan teks `You have unsaved changes. Are you sure you want to leave?` dan tombol `Cancel` serta `Leave`
17. Klik `[Leave]`
18. Verifikasi kembali ke tabel Asset Class
19. Verifikasi baris `B-ANCHOR` tetap bernama `Anchor Heavy Equipment`
20. Verifikasi tidak ada toast
21. Verifikasi jumlah entri Changelog `B-ANCHOR` tetap N2 (tidak ada entri Edit baru)
22. Verifikasi jumlah entri System Log aktor tetap Ns2 (tidak ada entri baru)
23. Verifikasi jumlah entri Activity Log FAMS tetap Na2 (tidak ada entri baru)

### TC-FA-FAAC-663: Edit diubah lalu dikembalikan identik ke nilai awal

24. Catat jumlah entri Changelog `B-ANCHOR` (N3), System Log aktor (Ns3), dan Activity Log FAMS (Na3) lewat fixture BE
25. Klik link Class Code `B-ANCHOR` di tabel
26. Ubah Class Name menjadi `Anchor Edited`
27. Kembalikan Class Name menjadi `Anchor Heavy Equipment` (identik dengan nilai awal)
28. Klik breadcrumb `Asset Class`
29. Verifikasi langsung kembali ke tabel Asset Class
30. Verifikasi dialog Unsaved Changes tidak tampil
31. Verifikasi tidak ada toast
32. Verifikasi jumlah entri Changelog `B-ANCHOR` tetap N3 (tidak ada entri baru)
33. Verifikasi jumlah entri System Log aktor tetap Ns3 (tidak ada entri baru)
34. Verifikasi jumlah entri Activity Log FAMS tetap Na3 (tidak ada entri baru)

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-659, 660, 663). Tidak ada TC hanya-BE di spec ini.
- Pengecualian beralasan atas S-06 dan S-12: Asset Class `B-ANCHOR` dan Class Name literal dari TC dipakai apa adanya tanpa suffix `{runId}-<NNN>` karena asersi TC bergantung pada nama; `B-ANCHOR` hanya dibuka di form dan tidak pernah disimpan, sehingga Last Updated tidak berubah (keputusan yang disetujui user).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan asersi TC): langkah 1 (Search untuk menemukan baris target), langkah 2, 14, dan 24 (mencatat baseline Changelog, System Log aktor, dan Activity Log FAMS sebelum aksi pemicu tiap TC, S-12).
- Urutan langkah TC-660: langkah 1 dan 2 TC-660 (membuka `B-ANCHOR` dan mengubah Class Name) sudah terpenuhi oleh keadaan akhir TC-659 (form Edit masih berisi `Anchor Edited` yang belum disimpan), sehingga TC-660 dimulai dari langkah 3 TC-660 (klik breadcrumb). Form ditutup deterministik lewat dialog `Unsaved Changes` (S-08).
- "Tidak ada entri baru" di tiga surface log pada langkah 11 sampai 13, 21 sampai 23, dan 32 sampai 34 adalah asersi jumlah terhadap baseline (selisih 0), bukan asersi absence kelas g (prinsip 13g, S-12); kotak Search tetap berisi `B-ANCHOR` sesudah breadcrumb sehingga baris target tetap terlihat (8b.9). Langkah 10, 20, dan 31 (tidak ada toast) diletakkan segera setelah anchor yang membuktikan aksi sudah diproses (dialog menutup, kembali ke tabel).
- Temuan untuk QA:
  - TC-659, 660, dan 663 menyebut "entri baru" di Changelog Asset Class, System Log, maupun Activity Log tanpa menyebut jenis entri; spec membandingkan jumlah total entri Changelog `B-ANCHOR`, System Log aktor, dan Activity Log FAMS terhadap baseline masing-masing.
