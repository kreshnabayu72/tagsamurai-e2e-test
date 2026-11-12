---
id: TC-FA-FAAC-E2E-053-unsaved-changes-form-create-breadcrumb-dan-menu-sidebar
title: "Unsaved Changes pada Form Create: Meninggalkan Form Lewat Breadcrumb dan Menu Sidebar"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-132
  - TC-FA-FAAC-661
coverage:
  web: automated
---

# Unsaved Changes pada Form Create: Meninggalkan Form Lewat Breadcrumb dan Menu Sidebar

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data (nama literal dari TC): Class Code `B-LEAVE` dan `B-NAVMENU` belum ada sebelum spec dan tidak pernah disimpan oleh spec ini; fixture BE menghapusnya bila ada. Hook `after` menghapus keduanya lewat fixture BE bila ada (pembersihan tidak mengandalkan setup berhasil penuh).
- Nilai data mengacu ke `Fixture.fixedAssetAssetClass.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Hook dan kemampuan suite (sesi API aktor, seed dan pemulihan lewat fixture BE, flag Guided Tooltip): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-132: Dialog Unsaved Changes saat meninggalkan form Create yang sudah diisi

1. Klik tombol `[+ Asset Class]` di toolbar tabel
2. Pada tab General isi Class Code `B-LEAVE`
3. Klik breadcrumb `Asset Class`
4. Verifikasi dialog tampil dengan teks `You have unsaved changes. Are you sure you want to leave?` dan tombol `Cancel` serta `Leave`
5. Klik `[Cancel]`
6. Verifikasi dialog menutup
7. Verifikasi form tetap terbuka dengan isian utuh (Class Code `B-LEAVE`)
8. Klik breadcrumb `Asset Class` lagi
9. Klik `[Leave]`
10. Verifikasi kembali ke tabel Asset Class
11. Ketik Search `B-LEAVE`, tekan Enter
12. Verifikasi empty state `No results found` tampil sehingga tidak ada Asset Class `B-LEAVE` yang dibuat

### TC-FA-FAAC-661: Create yang sudah diisi lalu klik menu sidebar lain: Cancel dan Leave

13. Klik tombol `[+ Asset Class]` di toolbar tabel
14. Pada tab General isi Class Code `B-NAVMENU`
15. Klik menu Dashboard di sidebar
16. Verifikasi dialog tampil dengan teks `You have unsaved changes. Are you sure you want to leave?` dan tombol `Cancel` serta `Leave`
17. Klik `[Cancel]`
18. Verifikasi dialog menutup
19. Verifikasi form Add Asset Class tetap terbuka dengan Class Code `B-NAVMENU`
20. Klik menu Dashboard di sidebar lagi
21. Klik `[Leave]`
22. Verifikasi berpindah ke halaman Dashboard
23. Buka kembali Fixed Asset > Settings > Accounting > tab Asset Class
24. Ketik Search `B-NAVMENU`, tekan Enter
25. Verifikasi empty state `No results found` tampil sehingga tidak ada Asset Class `B-NAVMENU` di tabel

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md` (TC-FA-FAAC-132, 661). TC-FA-FAAC-664 dan TC-FA-FAAC-666 (muat ulang halaman) ada di spec 063. Tidak ada TC hanya-BE di spec ini.
- Pengecualian beralasan atas S-06 dan S-12: Class Code literal dari TC dipakai apa adanya tanpa suffix `{runId}-<NNN>` karena asersi TC bergantung pada nama (keputusan yang disetujui user).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan asersi TC): langkah 11 dan 24 (Search untuk membuktikan Asset Class tidak dibuat, anchor empty state), langkah 23 (membuka kembali layar karena klik sidebar meninggalkan modul).
- Langkah 12 dan 25: empty state `No results found` hasil Search adalah anchor positif yang sah untuk asersi absence (8b.2).
- Form ditutup deterministik lewat dialog `Unsaved Changes` pada kedua TC (S-08), tidak ada form dirty tersisa di akhir spec.
- Temuan untuk QA:
  - TC-132 dan TC-661 Expected "tidak ada Asset Class dibuat" tidak menyebut cara pengamatan; spec memakai Search atas Class Code.
