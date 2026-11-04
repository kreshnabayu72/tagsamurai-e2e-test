---
id: TC-GS-USER-E2E-125-subtab-assigned-assets-download-isi-file-csv-xlsx
title: "Sub-tab Assigned Assets: Download CSV/XLSX (Nama Berkas, Isi, Cakupan Search, Kolom Hidden, dan Nilai Kosong)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-392
  - TC-GS-USER-785
  - TC-GS-USER-786
  - TC-GS-USER-787
  - TC-GS-USER-788
  - TC-GS-USER-789
coverage:
  web: automated
---

# Sub-tab Assigned Assets: Download CSV/XLSX (Nama Berkas, Isi, Cakupan Search, Kolom Hidden, dan Nilai Kosong)

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data Pre-setup user; hanya dataset Assigned Assets milik spec yang ditambahkan lalu dibersihkan.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login dan navigasi ke Global Settings > User > User List (sub-tab Login User) dilakukan sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`.
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-22, hanya dibaca): Ahmad Fauzi (No. 13; Assigned Assets berisi K1).
- Data Dinamis, dataset Assigned Assets milik Ahmad Fauzi (27 baris; dengan page size 10 menjadi tiga halaman: 10, 10, 7 baris). K1 adalah data Pre-setup (hanya dibaca, tidak dihapus); K2 sampai K27 di-seed milik spec lewat kemampuan seeding data Responsibilities/FAMS (HK8) di hook `before` (disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD). Saat spec mulai, Assigned Assets Ahmad Fauzi hanya berisi K1 sampai K27. Transaction ID `ASG-{runId}-125-kk` dan Asset ID `AST-{runId}-125-kk` dengan kk = nomor K dua digit:
  - K1 (Pre-setup, literal dari TC-GS-USER-390): Transaction ID `ASG-20260505-0001`, Name `Company Vehicle B1234XY`, Asset ID `AST-0001`, Brand `Toyota`, Model / Type `Hilux`, PIC `Citra Wulandari`.
  - K2 sampai K4: Name `Company Vehicle V1 {runId}-125` sampai `Company Vehicle V3 {runId}-125`, Brand `Toyota`, Model / Type `Hilux`, PIC `Rudi Hartanto {runId}-125`.
  - K5 sampai K7: Name `Company Vehicle V4 {runId}-125` sampai `Company Vehicle V6 {runId}-125`, Brand `Honda`, Model / Type `Civic`, PIC `Sinta Dewi {runId}-125`.
  - K8 sampai K12: Name `Laptop L1 {runId}-125` sampai `Laptop L5 {runId}-125`, Brand `Dell`, Model / Type `Latitude 5440`, PIC `Bambang Susanto {runId}-125`.
  - K13 sampai K17: Name `Laptop L6 {runId}-125` sampai `Laptop L10 {runId}-125`, Brand `Lenovo`, Model / Type `ThinkPad T14`, PIC `Rudi Hartanto {runId}-125`.
  - K18 sampai K22: Name `Printer P1 {runId}-125` sampai `Printer P5 {runId}-125`, Brand `Canon`, Model / Type `PIXMA G3010`, PIC `Sinta Dewi {runId}-125`.
  - K23 sampai K27: Name `Printer P6 {runId}-125` sampai `Printer P10 {runId}-125`, Brand `Epson`, Model / Type kosong (tidak diisi), PIC `Bambang Susanto {runId}-125`.
  - Ringkasan: Name 27 nilai distinct; Brand 6 nilai (Toyota 4 baris, Honda 3, Dell 5, Lenovo 5, Canon 5, Epson 5); PIC 4 nilai (Citra Wulandari 1 baris, Rudi Hartanto 8, Sinta Dewi 8, Bambang Susanto 10); baris ber-Name memuat `Vehicle`: 7 (K1 sampai K7). Nilai distinct pada kolom yang di-sort, di-search, dan di-filter dipenuhi (S-11).
  - Nama literal tanpa suffix hanya K1 (Pre-setup); seluruh nilai Name, Transaction ID, Asset ID, dan PIC milik spec bersuffix `{runId}-125`. Nama Brand dan Model / Type adalah nilai master tanpa suffix.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus aset seed K2 sampai K27 lewat kemampuan seeding yang sama; data Pre-setup (K1 dan record user) tidak diubah. Seeding aset tidak mengubah record user Ahmad Fauzi.
- Nilai kosong untuk TC-GS-USER-789: Model / Type K27 (`Printer P10 {runId}-125`) sengaja tidak diisi; kolom lain K27 terisi.
- Data uji per TC: TC-GS-USER-785, 392, 786, 789 tanpa Search dan Filter (27 baris); TC-GS-USER-787 keyword `{runId}-125` (mencocokkan K2 sampai K27, 26 baris, melebihi satu halaman tabel); TC-GS-USER-788 kolom `PIC` di-hide lalu di-unhide.
- Kemampuan teknis (kelas binary buffer, prinsip 13f konvensi): menangkap berkas unduhan browser (event download) ke direktori bersih per unduhan supaya nama berkas yang sama tidak tertimpa atau diberi akhiran `(1)`; membaca isi berkas CSV (header, jumlah baris data, nilai sel) dan nama berkas XLSX; seeding Assigned Assets (HK8) (disediakan tim FE/BE). Berkas unduhan dihapus di hook `after`.
- State yang diubah dan dipulihkan: Search (ditutup lewat `(←)` pada langkah 27) dan visibilitas kolom `PIC` (dipulihkan pada langkah 39); hook `after` mengembalikan visibilitas kolom sub-tab Assigned Assets ke default sebagai cadangan. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik icon Search, ketik `Ahmad Fauzi`, tekan Enter
2. Klik Name `Ahmad Fauzi` di User List
3. Klik Tab `Responsibilities`
4. Klik sub-tab `Assigned Assets`

### TC-GS-USER-785: Download CSV seluruh data tanpa toast sukses

5. Klik icon Download
6. Verifikasi overlay opsi `Download as CSV` dan `Download as XLSX`
7. Klik `Download as CSV`
8. Verifikasi tidak ada toast sukses
9. Verifikasi file `Assigned-Assets-Ahmad-Fauzi.csv` terunduh
10. Buka isi berkas `Assigned-Assets-Ahmad-Fauzi.csv` yang diunduh
11. Verifikasi berkas memuat semua 27 baris data (tidak dibatasi 10 baris halaman 1)

### TC-GS-USER-789: Nilai kosong ditulis `-` di file export

12. Verifikasi sel Model / Type baris `Printer P10 {runId}-125` pada berkas tertulis `-`

### TC-GS-USER-392: Download sub-tab Assigned Assets memakai nama file per user

13. Klik icon Download
14. Klik `Download as CSV`
15. Verifikasi tidak ada toast sukses
16. Verifikasi file `Assigned-Assets-Ahmad-Fauzi.csv` terunduh

### TC-GS-USER-786: Download XLSX

17. Klik icon Download
18. Klik `Download as XLSX`
19. Verifikasi file `Assigned-Assets-Ahmad-Fauzi.xlsx` terunduh

### TC-GS-USER-787: Download mengikuti Search aktif

20. Klik icon Search, ketik `{runId}-125`, tekan Enter
21. Verifikasi tabel menampilkan hasil search 26 baris dalam 3 halaman (pembanding sebelum Download)
22. Klik icon Download
23. Klik `Download as CSV`
24. Buka isi berkas `Assigned-Assets-Ahmad-Fauzi.csv` yang diunduh
25. Verifikasi berkas memuat 26 baris data hasil search (tidak dibatasi 10 baris halaman 1)
26. Verifikasi berkas tidak memuat baris Transaction ID `ASG-20260505-0001` (Name `Company Vehicle B1234XY`)

### TC-GS-USER-788: Download mengecualikan kolom hidden lalu menyertakan lagi setelah unhide

27. Klik icon panah `(←)` di kiri toolbar
28. Klik header kolom Actions (⋯)
29. Hilangkan centang kolom `PIC` pada Overlay Column Visibility
30. Tutup Overlay Column Visibility dengan menekan Esc
31. Verifikasi kolom `PIC` tidak tampil di tabel
32. Klik icon Download
33. Klik `Download as CSV`
34. Verifikasi tidak ada toast peringatan
35. Buka isi berkas `Assigned-Assets-Ahmad-Fauzi.csv` yang diunduh
36. Verifikasi header berkas memuat kolom `Transaction ID`, `Name`, `Asset ID`, `Brand`, dan `Model / Type`
37. Verifikasi header berkas tidak memuat kolom `PIC`
38. Klik header kolom Actions (⋯)
39. Centang kembali kolom `PIC` pada Overlay Column Visibility
40. Tutup Overlay Column Visibility dengan menekan Esc
41. Klik icon Download
42. Klik `Download as CSV`
43. Buka isi berkas `Assigned-Assets-Ahmad-Fauzi.csv` yang diunduh
44. Verifikasi header berkas memuat kolom `PIC`

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE. Kelas harness binary buffer (prinsip 13f): isi berkas CSV dan XLSX dipisah dari kegagalan ekspor. Dataset 27 baris (lebih dari satu halaman) dipenuhi spec lewat seeding di hook `before`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 785, 789, 392, 786, 787, 788. TC-GS-USER-789 membaca berkas hasil unduhan TC-GS-USER-785 (langkah 10, tanpa unduh ulang) karena state tabel keduanya identik (tanpa Search dan Filter, semua kolom, 27 baris); TC-GS-USER-785 didahulukan sebelum TC-GS-USER-392 karena memuat verifikasi overlay Download. TC-GS-USER-787 dan 788 yang mengubah state tabel (Search, kolom hidden) berada di akhir. Urutan di `tc-user.md`: 392, 785, 786, 787, 788, 789.
- TC-GS-USER-392 dan 785 melakukan unduhan sendiri karena Expected keduanya menyangkut perilaku layar saat klik (nama berkas dan tidak ada toast sukses).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 sampai 4 (pembukaan layar bersama untuk Ahmad Fauzi), langkah membuka isi berkas unduhan, langkah 27 (menutup Search dan mereset tabel), serta menutup overlay Column Visibility dengan Esc. Langkah 39 memulihkan visibilitas kolom `PIC`. Langkah membuka isi berkas termasuk blok baca berpola.
- Spec melewati sekitar 35 langkah (44 langkah) karena enam TC Download memakai satu layar, satu dataset 27 baris, dan satu kelas harness (binary buffer). Blok 785, 392, 786, 787, dan 788 mengunduh berkas sendiri dan berdiri sendiri; blok 789 membaca berkas hasil blok 785. Langkah membaca isi berkas termasuk blok baca berpola.
- Anchor positif (bagian 8b butir 2): verifikasi hasil search 26 baris dan berkas memuat 26 baris mendahului asersi ketiadaan baris `ASG-20260505-0001` pada berkas; verifikasi header berkas memuat lima kolom lain mendahului asersi ketiadaan kolom `PIC`.
- Pembagian TC lintas spec: TC-GS-USER-390, 391, 755 sampai 760 ada di spec 120; TC-GS-USER-761 sampai 768 ada di spec 121; TC-GS-USER-769 sampai 773 ada di spec 122; TC-GS-USER-774, 775, 790, 791 ada di spec 123; TC-GS-USER-776 sampai 784 ada di spec 124.
- Temuan untuk QA:
  - TC-GS-USER-785, 788, 789: TC tidak menyebut nama header kolom di berkas CSV dan nama kolom Photo di berkas; spec mengasumsikan header sama dengan nama kolom tabel dan tidak mengasersi kolom Photo di berkas.
  - TC-GS-USER-789: TC tidak menyebut kolom mana yang dapat kosong; spec menetapkan Model / Type K27 kosong dan mengasersi `-` pada sel itu (dataset ini disediakan tim FE/BE).
  - TC-GS-USER-786: Expected hanya nama berkas `.xlsx`; isi XLSX tidak diasersi karena TC tidak memberi Expected isi.
  - TC-GS-USER-787 dan 788: Data Uji kosong; keyword (`{runId}-125`) dan kolom yang di-hide (`PIC`) ditetapkan spec.
  - Mekanisme menandai Guided Tooltip sebagai sudah dilihat, menyiapkan data FAMS, serta menangkap dan membaca berkas unduhan tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
