---
id: TC-FA-CAID-E2E-001-screening-tab-dan-navigasi
title: "Screening Tab Custom Asset ID: Tampilan Awal, Breadcrumb, dan Refresh"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-1
  - TC-FA-CAID-2
  - TC-FA-CAID-3
  - TC-FA-CAID-4
  - TC-FA-CAID-5
coverage:
  web: automated
---

# Screening Tab Custom Asset ID: Tampilan Awal, Breadcrumb, dan Refresh

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka hook `beforeEach` suite.
- Akun aktor: Total Control Company Alpha (Pre-setup No 1, akun default suite) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Hook suite (`suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-asset-id` disetel seen; konfigurasi Company Alpha dipulihkan ke baseline B1 dan aset A1 sampai A5 ke Pre-setup No 11 di `beforeEach` lewat sesi API aktor (kemampuan disediakan tim FE).
- Data Pre-setup No 10 (baseline B1: Master Switch ON, Separator `/ (Slash)`, segmen tercentang Group Code, Category Code, Asset Name Code, Purchase Date, Asset Increment, tanpa Initial Company) dibaca dari `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE). Aset Pre-setup No 11 (A1 sampai A5) dipakai sebagai precondition TC-FA-CAID-1, tidak diasersi.
- Spec hanya membaca: tidak membuat data, tidak menekan `[Save]`, tidak mengubah state global. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-1: Screening halaman tab Custom Asset ID (3 zona)

1. Verifikasi Breadcrumb tampil `Settings > Asset Master > Custom Asset ID`
2. Verifikasi tombol `[?]` tampil di kanan Breadcrumb
3. Verifikasi Tabs Bar memuat `Asset Name`, `Custom Asset ID` (aktif), dan `Labels` berurutan
4. Verifikasi kartu menampilkan Title `Custom Asset ID Configuration`
5. Verifikasi kartu menampilkan Description `Define a standardized sequential format for auto-generating unique asset codes.`
6. Verifikasi tombol `[Changelog]` tampil di header kartu
7. Verifikasi switch `Enable Custom Asset ID` pada posisi ON
8. Verifikasi ikon info (i) tampil di samping switch
9. Verifikasi tidak ada helper text di bawah switch
10. Verifikasi field `Separator *` bernilai `/ (Slash)` dan placeholder `Select separator` tidak tampil karena sudah terpilih
11. Verifikasi kartu Live Preview berjudul `Live Generated Preview`
12. Verifikasi Code Box Live Preview menampilkan `JKT/LAP/T490/0926/1`
13. Verifikasi Live Preview menampilkan lima sub-label di bawah Code Box
14. Verifikasi label `Segments Order *` tampil
15. Verifikasi Subtitle `Check and drag to arrange your Asset ID format.` tampil
16. Verifikasi tautan `[View Code List]` tampil
17. Verifikasi delapan baris segmen berurutan: `Initial Company`, `Group Code`, `Category Code`, `Asset Name Code`, `Division Code`, `Account Code`, `Purchase Date (MMYY)`, `Asset Increment`
18. Verifikasi checkbox: `Initial Company`, `Division Code`, dan `Account Code` tidak tercentang; `Group Code`, `Category Code`, `Asset Name Code`, `Purchase Date (MMYY)`, dan `Asset Increment` tercentang; checkbox `Asset Increment` terkunci
19. Verifikasi Example tiap baris: `Group Code` JKT, `Category Code` LAP, `Asset Name Code` T490, `Division Code` 0000, `Account Code` 0000, `Purchase Date (MMYY)` 0926, `Asset Increment` 1
20. Verifikasi tombol `[Save]` tampil dengan status disabled karena form belum ada interaksi
21. Verifikasi tidak ada alert di atas `[Save]`
22. Verifikasi tidak ada elemen Page Title terpisah di bawah Breadcrumb

### TC-FA-CAID-2: Breadcrumb tab Custom Asset ID: teks path dan state tiap segmen

23. Verifikasi Breadcrumb tampil persis `Settings > Asset Master > Custom Asset ID` (3 segmen)
24. Klik segmen pertama `Settings`
25. Verifikasi segmen pertama `Settings` berupa label statis: halaman tidak berpindah dan tab `Custom Asset ID` tetap aktif
26. Klik segmen terakhir `Custom Asset ID`
27. Verifikasi segmen terakhir `Custom Asset ID` berupa label statis: halaman tidak berpindah dan tab `Custom Asset ID` tetap aktif
28. Verifikasi segmen tengah `Asset Master` tampil sebagai segmen yang dapat diklik

### TC-FA-CAID-3: Klik segmen tengah Breadcrumb `Asset Master` membuka tab default Asset Name

29. Klik segmen `Asset Master` pada Breadcrumb
30. Verifikasi halaman Asset Master terbuka dengan tab `Asset Name` aktif
31. Verifikasi Breadcrumb tampil `Settings > Asset Master > Asset Name`
32. Klik tab `Custom Asset ID` pada Tabs Bar

### TC-FA-CAID-4: Halaman tab Custom Asset ID tidak menampilkan Page Title di bawah Breadcrumb

33. Verifikasi tidak ada elemen Page Title bertuliskan `Custom Asset ID` atau `Asset Master` di bawah Breadcrumb
34. Verifikasi konten langsung dimulai dengan Tabs Bar `Asset Name | Custom Asset ID (aktif) | Labels`, lalu kartu `Custom Asset ID Configuration`

### TC-FA-CAID-5: Refresh F5 pada tab Custom Asset ID memuat tab yang sama

35. Tekan F5 pada halaman tab Custom Asset ID
36. Verifikasi tab `Custom Asset ID` tetap aktif setelah reload
37. Verifikasi Breadcrumb tampil `Settings > Asset Master > Custom Asset ID`

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular. Langkah TC-FA-CAID-1 (buka Fixed Asset > Settings > Asset Master dan klik tab `Custom Asset ID`) dan langkah pembuka TC-FA-CAID-2, 4, 5 dipenuhi hook `beforeEach` suite; spec langsung mengasersi.
- Spec ini 37 langkah tanpa langkah berulang, melewati sekitar 35 langkah. Alasan: satu kelas (screening satu layar, hanya membaca, tanpa seeding spec dan tanpa mengubah state), kelima TC memakai akun dan halaman yang sama, dan Expected TC-FA-CAID-1 berderet 22 klausa independen yang masing-masing mendapat satu `Verifikasi` (S-01).
- Pecahan Expected TC-FA-CAID-1: a i menjadi langkah 1 dan 2; a ii menjadi langkah 3; a iii menjadi langkah 4 sampai 9; b i menjadi langkah 10; b ii menjadi langkah 11 sampai 13; b iii menjadi langkah 14 sampai 16; b iv menjadi langkah 17 sampai 19; c menjadi langkah 20 dan 21; d menjadi langkah 22. Nilai dan placeholder satu field Separator adalah satu klausa (langkah 10).
- Langkah penghubung (tanpa `Verifikasi`): langkah 24 dan 26 (klik segmen sebagai pemicu), langkah 29 (pemicu), langkah 32 (kembali ke tab `Custom Asset ID` agar TC-FA-CAID-4 dan 5 mengamati tab itu), langkah 35 (F5 sebagai pemicu).
- Asersi absence (langkah 9, 21, 22, 33) didahului asersi positif atas elemen lain pada halaman yang sama (langkah 1 sampai 8 dan 10 sampai 20 untuk langkah 9, 21, dan 22; tab `Custom Asset ID` yang terbuka pada langkah 32 untuk langkah 33), sehingga halaman terbukti sudah termuat.
- Temuan untuk QA:
  - TC-FA-CAID-1 b ii menyebut "lima sub-label" tanpa teks dan format sub-label; PRD tidak mendefinisikannya (G-11 di catatan TC). Spec hanya mengasersi jumlah (langkah 13).
  - Post Condition TC-FA-CAID-1 sampai 5 kosong; tidak ada yang diasersi.
