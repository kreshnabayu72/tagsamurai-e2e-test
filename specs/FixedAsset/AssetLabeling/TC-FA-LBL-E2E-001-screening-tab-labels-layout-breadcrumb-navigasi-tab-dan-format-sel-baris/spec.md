---
id: TC-FA-LBL-E2E-001-screening-tab-labels-layout-breadcrumb-navigasi-tab-dan-format-sel-baris
title: "Screening Tab Labels: Layout, Breadcrumb, Tab Aktif, dan Format Sel Baris (bagian 1/2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-1
  - TC-FA-LBL-2
  - TC-FA-LBL-3
  - TC-FA-LBL-4
  - TC-FA-LBL-5
  - TC-FA-LBL-6
  - TC-FA-LBL-7
coverage:
  web: automated
---

# Screening Tab Labels: Layout, Breadcrumb, Tab Aktif, dan Format Sel Baris (bagian 1/2)

## Prerequisites

- Mode: FE+BE.
- Hook suite: `before`, `beforeEach`, dan `after` berlaku sesuai `suite.md` (termasuk flag Guided Tooltip `seen`); spec ini tidak menulis ulang isinya.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson), `Fixture.assetLabeling.akun.totalControl`, `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels).
- Environment variable: `FA_LBL_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Fixture: `Fixture.assetLabeling.*` (`fixtures/asset-labeling.json`) memuat identitas akun dan nama data tanpa rahasia; fixture ini belum ada dan disediakan tim FE.
- Data Pre-setup (dibaca saja, tidak diubah spec): #12 (katalog Company Alpha 9 label: `High Priority` `#EF4444`, `Finance Department` `#3B82F6`, `Audit Ready` `#10B981`, `Executive Asset` `#8B5CF6`, `Maintenance Due` `#F59E0B`, `Seasonal Event` `#EC4899`, `Night Shift` `#1E3A8A`, `Warehouse Priority` `#0EA5E9`, `Field Kit` `#84CC16`; Total Asset `High Priority` 3, `Seasonal Event` 0; Modified By `Sarah J` dan `Michael W`; Last Updated `15 Sep 2026 14:25` dan `05 Sep 2026 10:00`) dan #13 (aset berlabel yang menghasilkan Total Asset). Nilai Pre-setup dipakai literal karena Population Company Alpha bernama literal (lihat `suite.md`).
- Daftar label Company Alpha pada awal spec tepat 9 label Pre-setup #12; label milik spec lain sudah dibersihkan oleh hook `after` spec itu.
- Format Last Updated mengikuti General Settings Company Alpha (nilai awal, tidak diubah spec).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-FA-LBL-1: Screening halaman tab Labels saat pertama dibuka (3 zona)

1. Verifikasi Breadcrumb tampil `Settings > Asset Master > Labels`
2. Verifikasi Tab tampil `Asset Name | Custom Asset ID | Labels (aktif)`
3. Verifikasi Table Tools tampil `Search | Filter | Download | Changelog | [+ Label]`
4. Verifikasi kolom tabel `Checkbox | Label (sortable) | Color Hex (sortable) | Total Asset (sortable) | Modified By (sortable) | Last Updated (sortable) | Column Visibility (⋯)`
5. Klik header kolom Column Visibility (⋯)
6. Verifikasi overlay Column Visibility terbuka dengan CTA `[Setup Column]` di dalamnya
7. Tutup overlay Column Visibility
8. Verifikasi 9 baris label Pre-setup #12 tampil dengan urutan default Label A-Z: `Audit Ready`, `Executive Asset`, `Field Kit`, `Finance Department`, `High Priority`, `Maintenance Due`, `Night Shift`, `Seasonal Event`, `Warehouse Priority`
9. Verifikasi setiap baris pada kolom Column Visibility (⋯) berisi tombol row action menu
10. Verifikasi pagination default 10 data per halaman
11. Verifikasi Bulk Action Bar tidak tampil karena belum ada baris tercentang

### TC-FA-LBL-2: Breadcrumb tab Labels: teks path dan state tiap segmen

12. Verifikasi Breadcrumb tampil persis `Settings > Asset Master > Labels` (3 segmen)
13. Hover lalu klik segmen pertama `Settings`
14. Verifikasi segmen `Settings` berupa label statis yang tidak dapat diklik
15. Verifikasi klik segmen `Settings` tidak memindahkan halaman
16. Hover lalu klik segmen terakhir `Labels`
17. Verifikasi segmen `Labels` berupa label statis yang tidak dapat diklik
18. Verifikasi klik segmen `Labels` tidak memindahkan halaman
19. Verifikasi segmen tengah `Asset Master` dapat diklik

### TC-FA-LBL-4: Halaman tab Labels tidak menampilkan Page Title terpisah di bawah Breadcrumb

20. Verifikasi tidak ada elemen Page Title bertuliskan `Labels` atau `Asset Master` di bawah Breadcrumb
21. Verifikasi konten langsung dimulai di SectionCard dengan Tab `Asset Name | Custom Asset ID | Labels (aktif)`

### TC-FA-LBL-7: Format sel baris Labels List: chip, kode hex, Total Asset, Modified By, Last Updated

22. Verifikasi kolom Label menampilkan chip badge berlatar `#EF4444` untuk `High Priority` dan `#EC4899` untuk `Seasonal Event`
23. Verifikasi chip `High Priority` dan `Seasonal Event` berbentuk pill dengan teks `High Priority` dan `Seasonal Event`
24. Verifikasi kolom Color Hex menampilkan teks `#EF4444` dan `#EC4899`
25. Verifikasi kolom Total Asset menampilkan angka bulat `3` dan `0`; angka `0` ditulis `0`, bukan `—`
26. Verifikasi angka kolom Total Asset rata kanan
27. Verifikasi angka kolom Total Asset tampil sebagai link
28. Verifikasi kolom Modified By menampilkan `Sarah J` dan `Michael W`
29. Verifikasi kolom Last Updated menampilkan `15 Sep 2026 14:25` dan `05 Sep 2026 10:00` dalam format General Settings
30. Verifikasi tidak ada sel kosong di kelima kolom (Label, Color Hex, Total Asset, Modified By, Last Updated)

### TC-FA-LBL-6: Refresh F5 pada URL tab Labels memuat tab Labels, bukan tab pertama

31. Tekan F5 pada halaman tab Labels
32. Verifikasi tab `Labels` tetap aktif setelah reload
33. Verifikasi Breadcrumb tampil `Settings > Asset Master > Labels`

### TC-FA-LBL-3: Klik segmen tengah Breadcrumb `Asset Master` membuka tab Asset Name

34. Klik segmen `Asset Master` pada Breadcrumb
35. Verifikasi halaman Asset Master terbuka dengan tab `Asset Name` aktif
36. Verifikasi Breadcrumb tampil `Settings > Asset Master > Asset Name`

### TC-FA-LBL-5: Tab aktif saat pertama masuk Settings > Asset Master adalah Asset Name

37. Klik beranda Fixed Asset
38. Buka Fixed Asset > Settings > Asset Master tanpa memilih tab
39. Verifikasi Tab `Asset Name` aktif
40. Verifikasi Tab `Labels` berada di posisi ketiga setelah `Asset Name` dan `Custom Asset ID` dan tidak aktif
41. Verifikasi Breadcrumb tampil `Settings > Asset Master > Asset Name`

## Notes

- Langkah penghubung (S-03): langkah 7 (menutup overlay Column Visibility sebelum asersi berikutnya) dan langkah 37 (kembali ke beranda Fixed Asset supaya TC-FA-LBL-5 dimulai dari keadaan "belum membuka Asset Master").
- Layar awal: langkah 1 sampai 2 TC-FA-LBL-1 (buka Fixed Asset > Settings > Asset Master, klik Tab `Labels`) dipenuhi hook `beforeEach` suite yang membuka tab Labels; asersi dimulai dari keadaan itu (bagian 4).
- Urutan TC: TC-FA-LBL-4 dan TC-FA-LBL-7 yang hanya mengamati ditaruh sebelum TC-FA-LBL-6, TC-FA-LBL-3, dan TC-FA-LBL-5 yang memuat ulang atau berpindah halaman (S-10).
- Sel baris Column Visibility (⋯): isi menu row action diasersi pada TC-FA-LBL-16 (spec 002); langkah 9 hanya memeriksa keberadaan tombol per baris (Expected TC-FA-LBL-1 butir b.i).
- Alasan di atas sekitar 35 langkah (41 langkah): seluruh blok adalah screening halaman Labels yang sama dengan akun dan dataset yang sama (Pre-setup #12), kelas harness tunggal, tiap blok berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-LBL-1 butir b.ii dan TC-FA-LBL-9 menyebut tepat 9 baris Pre-setup #12; Pre-setup #22 (label 120 karakter) dan label milik TC lain berada di katalog yang sama tetapi tidak dinyatakan apakah ada pada saat TC-FA-LBL-1 dijalankan. Spec mengandalkan cleanup tiap spec sehingga katalog awal tepat 9 label.
  - TC-FA-LBL-2 meminta "hover" pada segmen Breadcrumb tanpa Expected state hover; hover ditulis sebagai bagian aksi dan tidak diasersi.
  - TC-FA-LBL-5 Precondition "halaman setelah login (belum membuka Asset Master)" tidak menyebut halaman asalnya; spec memakai beranda Fixed Asset (langkah 37).
