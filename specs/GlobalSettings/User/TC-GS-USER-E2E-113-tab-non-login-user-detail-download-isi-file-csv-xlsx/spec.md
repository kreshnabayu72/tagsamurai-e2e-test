---
id: TC-GS-USER-E2E-113-tab-non-login-user-detail-download-isi-file-csv-xlsx
title: "Tab Non-Login User Detail: Download CSV/XLSX (isi berkas, cakupan Search/Filter, kolom hidden, nilai kosong)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-404
  - TC-GS-USER-709
  - TC-GS-USER-710
  - TC-GS-USER-711
  - TC-GS-USER-712
  - TC-GS-USER-713
coverage:
  web: automated
---

# Tab Non-Login User Detail: Download CSV/XLSX (isi berkas, cakupan Search/Filter, kolom hidden, nilai kosong)

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data Pre-setup; satu-satunya state yang diubah adalah visibilitas kolom `Division` (dipulihkan) dan Search (ditutup).
- Akun: Total Control, `Siti Nurhaliza`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > User > User List (sub-tab Login User) dilakukan sekali di hook `before` (seedSession). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Data Pre-setup (hanya dibaca): Master Data Position (`Finance Manager`, `Staff`, `Supervisor`, `Internal Auditor`) dan Division (`Finance`, `General Affairs`, `Legal`) Pre-setup No. 22 dan 23 sebagai nilai seed.
- Data Dinamis, holder: Login User milik spec `Ahmad Fauzi {runId}-113` (email `ahmadfauzi+{runId}-113@qwertysystem.net`, status Activated, Access Global Settings) sebagai Represented By seluruh Non-Login User di bawah. Holder milik spec dipakai, bukan `Ahmad Fauzi` Pre-setup (Tabel Data Uji Pre-setup No. 13) beserta `Agus Prasetyo` dan `Lina Marlina` Pre-setup (No. 21), karena S-06 melarang mengubah data Pre-setup bersama dan S-11 menuntut data dengan lebih dari satu halaman serta sedikitnya dua nilai distinct pada kolom yang diuji.
- Data Dinamis, 12 Non-Login User milik spec (Represented By = `Ahmad Fauzi {runId}-113`), di-seed di hook `before`. Tabel memuat 12 baris: halaman 1 berisi 10 baris dan total 2 halaman (berkas harus memuat 12 baris, bukan 10). Nilai Name, Email, dan Employee ID bersuffix `{runId}-113`. `{U1}` dan `{U2}` pada kolom Temporary Until adalah tanggal hari uji + 30 hari dan hari uji + 60 hari, ditampilkan dalam Date Format General Settings.

  | Name | Email | Employee ID | Position | Division | Active | Temporary User | Temporary Until |
  |---|---|---|---|---|---|---|---|
  | `Agus Prasetyo {runId}-113` | `nlu01+{runId}-113@qwertysystem.net` | `EMP-AGS-{runId}-113` | Finance Manager | Finance | Active | No | kosong |
  | `Bagas Santoso {runId}-113` | `nlu02+{runId}-113@qwertysystem.net` | `EMP-BGS-{runId}-113` | Staff | General Affairs | Active | No | kosong |
  | `Citra Dewanti {runId}-113` | `nlu03+{runId}-113@qwertysystem.net` | `EMP-CTR-{runId}-113` | Supervisor | Finance | Active | Yes | `{U1}` (hari uji + 30 hari) |
  | `Dimas Pranoto {runId}-113` | `nlu04+{runId}-113@qwertysystem.net` | `EMP-DMS-{runId}-113` | Staff | General Affairs | Active | No | kosong |
  | `Eka Wulandari {runId}-113` | `nlu05+{runId}-113@qwertysystem.net` | `EMP-EKA-{runId}-113` | Finance Manager | Legal | Active | No | kosong |
  | `Fitri Handayani {runId}-113` | `nlu06+{runId}-113@qwertysystem.net` | `EMP-FTR-{runId}-113` | Internal Auditor | Finance | Active | Yes | `{U2}` (hari uji + 60 hari) |
  | `Galih Permadi {runId}-113` | `nlu07+{runId}-113@qwertysystem.net` | `EMP-GLH-{runId}-113` | Staff | Legal | Active | No | kosong |
  | `Hana Kusuma {runId}-113` | `nlu08+{runId}-113@qwertysystem.net` | `EMP-HNA-{runId}-113` | Supervisor | General Affairs | Active | No | kosong |
  | `Lina Marlina {runId}-113` | `nlu09+{runId}-113@qwertysystem.net` | kosong | kosong | Legal | Inactive | No | kosong |
  | `Nadia Rahma {runId}-113` | `nlu10+{runId}-113@qwertysystem.net` | `EMP-NDR-{runId}-113` | Staff | Finance | Active | No | kosong |
  | `Rizky Fadillah {runId}-113` | `nlu11+{runId}-113@qwertysystem.net` | `EMP-RZK-{runId}-113` | Finance Manager | General Affairs | Inactive | No | kosong |
  | `Wahyu Hidayat {runId}-113` | `nlu12+{runId}-113@qwertysystem.net` | `EMP-WHY-{runId}-113` | Supervisor | Legal | Active | No | kosong |

  `Lina Marlina` tidak memiliki Employee ID dan Position sehingga sel itu kosong di tabel dan berkas (TC-GS-USER-713). Position `Staff` dimiliki 4 baris (`Bagas Santoso`, `Dimas Pranoto`, `Galih Permadi`, `Nadia Rahma`), dan keyword `Staff` hanya mencocokkan kolom Position pada data di atas (TC-GS-USER-711).
- Kemampuan teknis (disediakan tim FE/BE; endpoint ditentukan tim FE di tahap script): seeding Login User holder dan Non-Login User dengan Represented By = holder lewat API di hook `before`; cleanup di hook `after` menghapus Non-Login User lalu holder lewat API tanpa berasumsi seeding berhasil penuh. Seeding menambah 13 user pada hitungan Master Data Count Limit gabungan Login + Non-Login User; nilai limit environment cukup besar untuk itu.
- Nama berkas: `Non-Login-User-[User-Name]` (PRD user.md §4.1.4, §7) dengan `[User-Name]` = nama holder `Ahmad Fauzi {runId}-113` dan spasi diganti hyphen, sehingga berkas bernama `Non-Login-User-Ahmad-Fauzi-{runId}-113.csv` dan `Non-Login-User-Ahmad-Fauzi-{runId}-113.xlsx`.
- Data uji: format `CSV` (TC-GS-USER-404, 709, 711, 712, 713) dan `XLSX` (TC-GS-USER-710); keyword `Staff` (TC-GS-USER-711); kolom `Division` di-hide lalu di-unhide (TC-GS-USER-712).
- Date Format General Settings default environment (`DD/MM/YY`); spec tidak mengubahnya.
- Kemampuan teknis (kelas binary buffer, prinsip 13f konvensi): menangkap berkas unduhan browser (event download) ke direktori bersih per unduhan supaya nama berkas yang sama tidak tertimpa atau diberi akhiran `(1)`; membaca isi berkas CSV dan XLSX (nama kolom, jumlah baris, nilai sel). Berkas unduhan dihapus di hook `after`. Menekan Esc untuk menutup Overlay Column Visibility.
- Preferensi kolom tersimpan di browser (PRD prd-conventions.md §9.3); hook `after` mengembalikan preferensi kolom Tab Non-Login User ke default.
- State yang diubah dan dipulihkan: visibilitas kolom `Division` (dicentang kembali di langkah 33 sampai 35), Search (ditutup dengan icon ← di langkah terakhir); hook `after` sebagai cadangan.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`). Spec tidak mengubah data Pre-setup bersama (S-06).

## Test Steps

1. Klik icon Search, ketik `Ahmad Fauzi {runId}-113`, tekan Enter
2. Klik Name `Ahmad Fauzi {runId}-113` di User List
3. Klik Tab `Non-Login User`

### TC-GS-USER-404: Download memakai nama file per user

4. Klik icon Download
5. Klik `Download as CSV`
6. Verifikasi file `Non-Login-User-Ahmad-Fauzi-{runId}-113.csv` terunduh
7. Verifikasi tidak ada toast sukses

### TC-GS-USER-709: Download CSV seluruh data tanpa toast sukses

8. Klik icon Download
9. Verifikasi overlay menampilkan opsi `Download as CSV`
10. Verifikasi overlay menampilkan opsi `Download as XLSX`
11. Klik `Download as CSV`
12. Verifikasi file `Non-Login-User-Ahmad-Fauzi-{runId}-113.csv` terunduh
13. Buka isi file `Non-Login-User-Ahmad-Fauzi-{runId}-113.csv` yang diunduh
14. Verifikasi file memuat seluruh 12 baris data, termasuk baris halaman 2 (`Rizky Fadillah {runId}-113`, `Wahyu Hidayat {runId}-113`) dan bukan hanya 10 baris halaman 1
15. Verifikasi tidak ada toast sukses

### TC-GS-USER-710: Download XLSX

16. Klik icon Download
17. Klik `Download as XLSX`
18. Verifikasi file `Non-Login-User-Ahmad-Fauzi-{runId}-113.xlsx` terunduh

### TC-GS-USER-713: Nilai kosong ditulis `-` di file export

19. Klik icon Download
20. Klik `Download as CSV`
21. Buka isi file `Non-Login-User-Ahmad-Fauzi-{runId}-113.csv` yang diunduh
22. Verifikasi sel kosong ditulis `-`: Employee ID dan Position pada baris `Lina Marlina {runId}-113` bernilai `-`

### TC-GS-USER-712: Download mengecualikan kolom hidden lalu menyertakan lagi setelah unhide

23. Klik header kolom Column Visibility (⋯)
24. Hilangkan centang kolom `Division`
25. Tutup Overlay Column Visibility dengan menekan Esc
26. Verifikasi kolom `Division` tidak tampil di tabel
27. Klik icon Download
28. Klik `Download as CSV`
29. Buka isi file `Non-Login-User-Ahmad-Fauzi-{runId}-113.csv` yang diunduh
30. Verifikasi file pertama memuat kolom `Name`, `Email`, `Employee ID`, `Position`, `Active`, dan `Last Update`
31. Verifikasi file pertama tanpa kolom `Division`
32. Verifikasi tidak ada toast peringatan
33. Klik header kolom Column Visibility (⋯)
34. Centang kolom `Division`
35. Tutup Overlay Column Visibility dengan menekan Esc
36. Klik icon Download
37. Klik `Download as CSV`
38. Buka isi file `Non-Login-User-Ahmad-Fauzi-{runId}-113.csv` yang diunduh
39. Verifikasi file kedua memuat kolom `Division`

### TC-GS-USER-711: Download mengikuti Search aktif

40. Klik icon Search, ketik `Staff`, tekan Enter
41. Verifikasi tabel hanya menampilkan 4 baris dengan Position `Staff`: `Bagas Santoso {runId}-113`, `Dimas Pranoto {runId}-113`, `Galih Permadi {runId}-113`, `Nadia Rahma {runId}-113`
42. Klik icon Download
43. Klik `Download as CSV`
44. Buka isi file `Non-Login-User-Ahmad-Fauzi-{runId}-113.csv` yang diunduh
45. Verifikasi file hanya berisi 4 baris hasil search: `Bagas Santoso {runId}-113`, `Dimas Pranoto {runId}-113`, `Galih Permadi {runId}-113`, `Nadia Rahma {runId}-113`
46. Klik icon ←

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE. Kelas harness binary buffer (prinsip 13f): isi berkas CSV dan XLSX dipisah dari kegagalan ekspor. Holder dan 12 Non-Login User dipenuhi spec ini lewat seeding di hook `before`; spec tidak menumpang spec lain.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 404, 709, 710 (unduhan tanpa Search dan tanpa kolom hidden), 713 (isi berkas, nilai kosong), 712 (kolom hidden), lalu 711 (Search aktif) di akhir, karena TC-GS-USER-711 memerlukan Search yang harus ditutup sesudahnya, sedangkan TC lain memerlukan tabel tanpa Search. Urutan di `tc-user.md`: 404, 709, 710, 711, 712, 713.
- Langkah penghubung (aksi tanpa `Verifikasi`): pembukaan Tab (langkah 1 sampai 3); langkah membuka isi berkas unduhan; langkah 23 sampai 25 dan 33 sampai 35 (menyembunyikan dan menampilkan kolom `Division` lewat Overlay Column Visibility, penutupan dengan Esc); `Klik icon ←` di akhir spec (menutup Search dan mereset tabel).
- Asersi tambahan (S-03): TC-GS-USER-712 memverifikasi enam kolom lain tetap ada pada berkas pertama (pembanding bagi asersi ketiadaan kolom `Division`, bagian 8b butir 2); TC-GS-USER-711 memverifikasi tabel menampilkan hasil search sebelum Download. TC-GS-USER-709 Expected b juga dipenuhi `Verifikasi` yang memuat baris halaman 2.
- TC-GS-USER-404 dan TC-GS-USER-709 sama-sama mengunduh CSV tanpa Search; unduhan dilakukan dua kali karena Expected TC-GS-USER-404 menyangkut nama berkas dan TC-GS-USER-709 menyangkut overlay opsi serta isi berkas. Nama berkas, toast, dan isi diasersi pada unduhan masing-masing.
- Pembagian TC lintas spec: TC-GS-USER-400 sampai 403 (screening Tab, navigasi) dan 671 sampai 677 (Search) ada di spec 108; TC-GS-USER-678 sampai 686 (Filter Panel) ada di spec 109; TC-GS-USER-687 sampai 691 (kombinasi Search dan Filter) ada di spec 110; TC-GS-USER-692 sampai 696, 714, dan 715 (Sort, Pagination) ada di spec 111; TC-GS-USER-697 sampai 708 (Setup Column) ada di spec 112. Kegagalan Download Tab Non-Login User (`"Error, failed to download Non-Login-User-[User-Name]."`, PRD user.md §7 T-20) tidak termasuk TC sumber spec ini.
- Spec melewati sekitar 35 langkah (46 langkah) karena enam TC Download berbagi satu layar (Tab Non-Login User), satu dataset (12 Non-Login User milik spec), dan satu kelas harness (binary buffer). Tiap blok mengunduh berkasnya sendiri dan berdiri sendiri (kegagalan satu blok tidak menghapus makna blok lain); memisahkannya mengulang login, seeding 13 user, dan pembukaan Tab. Langkah membuka isi berkas termasuk blok baca berpola.
- Temuan untuk QA:
  - TC-GS-USER-404, 709, 710: Expected menyebut berkas `Non-Login-User-Ahmad-Fauzi.csv` tanpa suffix; holder milik spec bernama `Ahmad Fauzi {runId}-113` (S-06, S-11), sehingga spec mengasersi `Non-Login-User-Ahmad-Fauzi-{runId}-113.csv` dan `.xlsx`. Aturan konversi nama user ke nama berkas (spasi menjadi hyphen) berasal dari contoh TC dan PRD user.md §4.1.4 (`Non-Login-User-[User-Name]`).
  - TC-GS-USER-404 sampai 713 menyebut Name tanpa suffix; spec memakai holder dan Non-Login User milik spec bersuffix.
  - TC-GS-USER-709, 711, 712, 713: TC tidak menyebut cara menangkap berkas unduhan dan membaca isinya; kemampuan tersebut disediakan tim FE (Prerequisites). TC-GS-USER-710 tidak menyebut isi berkas XLSX; spec hanya mengasersi nama berkas.
  - TC-GS-USER-711: TC tidak menyebut keyword; spec memakai `Staff`. Expected "File hanya berisi baris hasil search" tidak menyebut kolom berkas; spec mengasersi nama baris.
  - TC-GS-USER-712: TC tidak menyebut kolom yang di-hide; spec memakai `Division`. Expected tidak menyebut pembanding kolom lain pada berkas; spec menambahkan asersi enam kolom lain (S-03).
  - TC-GS-USER-713: TC tidak menyebut baris yang berisi sel kosong; spec memakai baris `Lina Marlina` (Employee ID dan Position kosong). Rujukan PRD prd-conventions.md §9.9: sel kosong ditulis `-` (hyphen tunggal).
  - TC-GS-USER-713: TC tidak menyebut format file untuk nilai kosong pada XLSX; spec hanya mengasersi CSV sesuai langkah TC.
  - Cara menutup Overlay Column Visibility tidak didefinisikan di TC maupun PRD; spec memakai Esc.
  - Mekanisme seeding Login User dan Non-Login User (Represented By, Employee ID, Position, Division, Temporary Until) dan penghapusan sisa tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
