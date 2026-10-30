---
id: TC-GS-USER-E2E-119-subtab-borrowed-assets-download-isi-file-csv-xlsx
title: "Sub-tab Borrowed Assets: Download CSV/XLSX (isi berkas, cakupan Search/Filter, kolom hidden, nilai kosong)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-389
  - TC-GS-USER-748
  - TC-GS-USER-749
  - TC-GS-USER-750
  - TC-GS-USER-751
  - TC-GS-USER-752
coverage:
  web: automated
---

# Sub-tab Borrowed Assets: Download CSV/XLSX (isi berkas, cakupan Search/Filter, kolom hidden, nilai kosong)

## Prerequisites

- Mode: FE+BE. Spec hanya membaca data user; tidak ada data user yang diubah.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun: Total Control, Siti Nurhaliza, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > User > User List dilakukan sekali di hook `before` (seedSession). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`.
- Data Pre-setup (hanya dibaca): `Joko Susilo` (No. 19; Access Fixed Asset + Supply Asset) sebagai pemilik tabel Borrowed Assets; `Andi Wijaya`, `Doni Pratama` (No. 10 dan 11) sebagai PIC seed. Client FAMS aktif. `Joko Susilo` (Tabel Pre-setup No. 19) sudah punya borrowed asset Pre-setup (`B0` baris, nilainya tidak disebut TC). Baris itu tidak diubah dan ikut tampil di tabel. Asersi memakai nilai bersuffix `{runId}-119` (Name, Brand, Model / Type) sehingga tidak bentrok dengan `B0`; jumlah baris tabel = `B0` + baris seed.
- Data Dinamis (seeding FAMS atas `Joko Susilo`, 26 baris aset pinjaman; seluruhnya tanpa foto sehingga kolom Photo menampilkan `—`):
  - Grup L (8 baris): Name `Laptop 1 {runId}-119` sampai `Laptop 8 {runId}-119`; Brand `Lenovo {runId}-119`; Model / Type `ThinkPad {runId}-119`; PIC `Andi Wijaya` (tampil `Andi W`); Due Return Date = hari uji + 10 hari (`{tglL}`).
  - Grup P (10 baris): Name `Proyektor 1 {runId}-119` sampai `Proyektor 10 {runId}-119`; Brand `Epson {runId}-119`; Model / Type `EB-X06 {runId}-119`; PIC `Doni Pratama` (tampil `Doni P`); Due Return Date = hari uji + 20 hari (`{tglP}`).
  - Grup K (8 baris): Name `Kamera 1 {runId}-119` sampai `Kamera 8 {runId}-119`; Brand `Canon {runId}-119`; Model / Type `EOS-R10 {runId}-119`; PIC `Andi Wijaya` (tampil `Andi W`); Due Return Date = hari uji + 30 hari (`{tglK}`).
  - Seluruh nilai Name, Brand, dan Model / Type unik per spec dan per run; setiap kolom yang diuji punya sedikitnya dua nilai distinct (Brand dan Model / Type tiga nilai, PIC dua nilai, Due Return Date tiga nilai) (S-11). `{tglL}`, `{tglP}`, `{tglK}` adalah tanggal Due Return Date grup tersebut dalam Date Format General Settings client, dihitung di hook `before` dari hasil seeding. PIC memakai user Pre-setup `Andi Wijaya` dan `Doni Pratama` yang hanya dibaca.
- Jumlah baris data yang diharapkan pada berkas tanpa Search dan Filter = jumlah baris tabel = `B0` + 26 (lebih dari 10 baris satu halaman).
- Data uji per TC: format `CSV` (TC-GS-USER-389, 748, 750, 751, 752) dan `XLSX` (TC-GS-USER-749); TC-GS-USER-750 keyword `Proyektor`; TC-GS-USER-751 kolom `Brand` di-hide lalu di-unhide.
- Kemampuan teknis (kelas binary buffer, prinsip 13f konvensi): menangkap berkas unduhan browser (event download) ke direktori bersih per unduhan supaya nama berkas yang sama (`Borrowed-Assets-Joko-Susilo.csv`) tidak tertimpa atau diberi akhiran `(1)`; membaca isi berkas CSV dan XLSX (nama kolom, jumlah baris, nilai sel). Berkas unduhan dihapus di hook `after`.
- Kemampuan teknis (HK8, disediakan tim FE/BE; endpoint tidak disebut di TC, PRD, atau LLD): seeding FAMS yang membuat aset beserta transaksi peminjaman atas `Joko Susilo` dengan Name, Brand, Model / Type, PIC, dan Due Return Date yang ditentukan; membaca Transaction ID dan Asset ID hasil seeding; membaca jumlah borrowed asset Pre-setup `Joko Susilo` sebelum seeding (disebut `B0` di bawah); menghapus atau mengembalikan aset dan transaksi seed di hook `after`.
- State yang diubah dan dipulihkan: Search dikosongkan dan ditutup, kolom `Brand` ditampilkan kembali (langkah centang kembali) di akhir spec; preferensi kolom tabel Borrowed Assets dikembalikan ke default di hook `after` sebagai cadangan. Aset dan transaksi seed dibersihkan di hook `after` tanpa mengandalkan seeding berhasil penuh.
- Hook `beforeEach`: kembali ke layar Global Settings > User > User List.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-USER-389: Download memakai nama file per user

1. Klik icon Search di User List, ketik `Joko Susilo`, tekan Enter
2. Klik Name `Joko Susilo` di User List
3. Klik Tab `Responsibilities`
4. Klik sub-tab `Borrowed Assets`
5. Klik icon Download
6. Klik `Download as CSV`
7. Verifikasi file `Borrowed-Assets-Joko-Susilo.csv` terunduh
8. Verifikasi tidak ada toast sukses

### TC-GS-USER-748: Download CSV seluruh data tanpa toast sukses

9. Klik icon Download
10. Verifikasi overlay opsi menampilkan `Download as CSV`
11. Verifikasi overlay opsi menampilkan `Download as XLSX`
12. Klik `Download as CSV`
13. Verifikasi file `Borrowed-Assets-Joko-Susilo.csv` terunduh
14. Verifikasi tidak ada toast sukses
15. Buka isi file `Borrowed-Assets-Joko-Susilo.csv` hasil unduhan langkah 12
16. Verifikasi file memuat 26 baris data aset seed (`Laptop 1 {runId}-119` sampai `Laptop 8`, `Proyektor 1` sampai `Proyektor 10`, dan `Kamera 1` sampai `Kamera 8`)
17. Verifikasi jumlah baris data file sama dengan jumlah baris tabel, yaitu `B0` + 26, lebih banyak dari 10 baris satu halaman (tidak dibatasi halaman)

### TC-GS-USER-752: Nilai kosong ditulis `-` di file export

18. Verifikasi seluruh sel pada file hasil unduhan langkah 12 terisi: tidak ada sel blank, `null`, atau `—`

### TC-GS-USER-749: Download XLSX

19. Klik icon Download
20. Klik `Download as XLSX`
21. Verifikasi file `Borrowed-Assets-Joko-Susilo.xlsx` terunduh

### TC-GS-USER-750: Download mengikuti Search/Filter aktif

22. Klik icon Search, ketik `Proyektor`, tekan Enter
23. Verifikasi tabel menampilkan baris `Proyektor 1 {runId}-119`
24. Klik icon Download
25. Klik `Download as CSV`
26. Buka isi file `Borrowed-Assets-Joko-Susilo.csv` hasil unduhan ini
27. Verifikasi file memuat 10 baris hasil search (`Proyektor 1 {runId}-119` sampai `Proyektor 10`)
28. Verifikasi file tidak memuat baris `Laptop 1 {runId}-119` dan `Kamera 1 {runId}-119`
29. Klik icon panah `(←)` untuk menutup Search dan mereset tabel

### TC-GS-USER-751: Download mengecualikan kolom hidden lalu menyertakan lagi setelah unhide

30. Klik header kolom Column Visibility (⋯)
31. Hilangkan centang kolom `Brand` pada Overlay Column Visibility
32. Klik icon Download
33. Klik `Download as CSV`
34. Buka isi file `Borrowed-Assets-Joko-Susilo.csv` hasil unduhan ini
35. Verifikasi file memuat kolom `Name`
36. Verifikasi file tanpa kolom `Brand`
37. Verifikasi tidak ada toast peringatan
38. Klik header kolom Column Visibility (⋯)
39. Centang kembali kolom `Brand` pada Overlay Column Visibility
40. Klik icon Download
41. Klik `Download as CSV`
42. Buka isi file `Borrowed-Assets-Joko-Susilo.csv` hasil unduhan ini
43. Verifikasi file memuat kolom `Brand`

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE. Kelas harness binary buffer (prinsip 13f): isi berkas CSV dan XLSX dipisah dari kegagalan ekspor. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Data target: TC sumber memakai `Ahmad Fauzi` dan nama berkas `Borrowed-Assets-Ahmad-Fauzi`; spec memakai `Joko Susilo` (Tabel Pre-setup No. 19) dengan populasi aset pinjaman milik spec, sehingga nama berkas `Borrowed-Assets-Joko-Susilo` (format `Borrowed-Assets-[User-Name]`, PRD user.md §4.1.3).
- Urutan TC dalam spec: 389, 748, 752, 749, 750, 751. TC-GS-USER-752 membaca berkas hasil unduhan TC-GS-USER-748 (langkah 12) tanpa unduh ulang karena state tabel keduanya identik (tanpa Search dan Filter, semua kolom); TC-GS-USER-750 (Search aktif) dan 751 (kolom hidden) mengubah state tabel sehingga diletakkan sesudah TC yang membutuhkan tabel tanpa Search dan kolom penuh. Urutan di `tc-user.md` adalah 389, 748, 749, 750, 751, 752.
- TC-GS-USER-389 dan 748 memuat Expected nama berkas dan tanpa toast sukses yang sama; keduanya diasersi pada unduhannya masing-masing (unduhan pada langkah 6 untuk TC-GS-USER-389 dan langkah 12 untuk TC-GS-USER-748).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (mencari user target di User List); langkah 15, 26, 34, 42 (membaca isi berkas unduhan); langkah 29 (menutup Search). Langkah membaca isi berkas termasuk blok baca berpola.
- Spec melewati sekitar 35 langkah (43 langkah) karena enam TC Download berbagi satu layar, satu dataset seed, dan satu kelas harness (binary buffer); tiap blok mengunduh berkas sendiri kecuali TC-GS-USER-752 yang membaca berkas TC-GS-USER-748. Pembukaan layar (empat langkah pertama) dan langkah membaca isi berkas tidak dihitung ke batas.
- Pembagian TC lintas spec: TC-GS-USER-387, 388, 716 sampai 721 ada di spec 114; TC-GS-USER-722 sampai 730 ada di spec 115; TC-GS-USER-731 sampai 735 ada di spec 116; TC-GS-USER-736, 737, 738, 753, 754 ada di spec 117; TC-GS-USER-739 sampai 747 ada di spec 118. Kegagalan ekspor sub-tab (bila ada TC-nya) bukan bagian spec ini.
- Temuan untuk QA:
  - TC-GS-USER-752: "Sel kosong ditulis `-`" tidak punya objek uji: semua kolom data Borrowed Assets tidak pernah kosong (PRD user.md §4.1.3, Nilai Kosong) dan foto tidak diikutsertakan dalam export (prd-conventions §9.9), sehingga tidak ada sel kosong yang dapat memicu `-`. Spec mengasersi seluruh sel terisi (tanpa blank, `null`, `—`); aturan `-` tidak teramati.
  - TC-GS-USER-748 Expected b: "semua baris" dipenuhi dengan jumlah baris tabel (`B0` + 26); TC tidak menyebut jumlah, dan UI tidak menampilkan total baris sehingga angka itu berasal dari seeding dan pembacaan `B0` (kemampuan disediakan tim FE/BE).
  - TC-GS-USER-749: Expected hanya menyebut nama berkas `.xlsx`; isi berkas XLSX tidak diasersi.
  - TC-GS-USER-750: keyword tidak disebut; spec memakai `Proyektor`. Nama kolom header berkas (mis. `Brand`) tidak disebut TC; spec mengasersi nama kolom sesuai header tabel.
  - TC-GS-USER-751: "Hide 1 kolom" tidak menyebut kolom; spec memakai `Brand`.
  - Mekanisme menandai Guided Tooltip sebagai sudah dilihat, menangkap berkas unduhan, dan seeding FAMS tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
