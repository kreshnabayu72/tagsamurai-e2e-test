---
id: TC-GS-USER-E2E-101-tab-system-log-detail-download-isi-file-csv-xlsx
title: "Tab System Log Detail: Download CSV/XLSX (Nama Berkas, Seluruh Baris, Cakupan Search, Kolom Hidden, dan Nilai Kosong)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-408
  - TC-GS-USER-624
  - TC-GS-USER-625
  - TC-GS-USER-626
  - TC-GS-USER-627
  - TC-GS-USER-628
coverage:
  web: automated
---

# Tab System Log Detail: Download CSV/XLSX (Nama Berkas, Seluruh Baris, Cakupan Search, Kolom Hidden, dan Nilai Kosong)

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor UI: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > User > User List (sub-tab Login User). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`, `USER_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 23 dan 26): hanya dibaca (Division dan Access dipakai sebagai nilai field user seed). Spec tidak mengubah atau menghapus data Pre-setup.
- Data Dinamis, di-seed lewat API di hook `before` (kemampuan seeding user lewat API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD). System Log memuat aksi yang dilakukan user sebagai aktor (PRD user.md §8.3). Tiap user diberi Division `Finance` dan Access `Fixed Asset`:
  - Pemilik log `Aktor Log {runId}-101`, email `aktorlog+{runId}-101@qwertysystem.net`, tier Total Control, status Activated, password `Spectra.env.USER_PASSWORD`. Aktivasi akun seed dan sesi API Aktor Log disediakan tim FE/BE (TC, PRD, dan LLD tidak menyebut mekanismenya). Seluruh aksi seed di bawah dijalankan lewat sesi API Aktor Log.
  - Target aksi `Target Alfa {runId}-101` (email `targetalfa+{runId}-101@qwertysystem.net`, Position `Staff`) dan `Target Beta {runId}-101` (email `targetbeta+{runId}-101@qwertysystem.net`).
  - Aksi seed oleh Aktor Log, berurutan (hanya data yang dipakai `Verifikasi`, S-11): (1) Create `Target Alfa` (Field `Name`, Old Value `—`); (2) Create `Target Beta`; (3) Edit Position `Target Alfa` dari `Staff` menjadi `Supervisor`; (4) empat kali Edit Position `Target Alfa` bergantian `Supervisor` ke `Staff` dan `Staff` ke `Supervisor`; (5) Deactivate `Target Alfa` (Field `Status (Global)`, `Active` menjadi `Inactive`); (6) Activate `Target Alfa`; (7) Delete `Target Beta` (Field `Name`, New Value `—`); (8) Assign Total Control ke `Target Alfa` (Object `Total Control`, Field `Access Level`, New Value `Total Control`).
  - Hasil: 11 entri (lebih dari 10 baris per halaman, sehingga berkas yang memuat seluruh baris dapat dibedakan dari satu halaman tabel). Search `alfa` mencocokkan 9 entri (semua kecuali Create dan Delete `Target Beta`). Entri Create memiliki Old Value kosong dan entri Delete memiliki New Value kosong (nilai kosong di berkas, TC-GS-USER-628).
- Baseline audit trail (S-12, bagian 8b butir 10): aktor `Aktor Log {runId}-101` dibuat baru oleh hook `before` dengan nama dan email bersuffix `-101`, sehingga sebelum seeding Tab System Log belum memuat entri apa pun; baseline = 0 dicatat eksplisit di hook `before` tepat sebelum seeding. Jumlah baris total yang diasersi adalah selisih terhadap baseline itu (baseline 0 + 11 entri seed), bukan total absolut tabel. Bila baseline perlu dibaca, kemampuan baca total entri disediakan tim FE/BE (TC, PRD, dan LLD tidak menyebut caranya).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Target Alfa` (cabut tier Total Control lebih dulu bila diperlukan), `Target Beta` bila masih ada, dan `Aktor Log`; hapus sisa user bersuffix `-101` dari run lama; hapus berkas unduhan. Entri log tidak bisa dihapus.
- Kemampuan teknis (kelas binary buffer, prinsip 13f konvensi): menangkap berkas unduhan browser ke direktori bersih per unduhan supaya nama berkas yang sama tidak tertimpa atau diberi akhiran `(1)`; membaca isi berkas CSV dan XLSX (nama kolom, jumlah baris data, nilai sel). Nama berkas mengikuti `System-Log-[User-Name]` dengan spasi diganti `-` (PRD user.md §4.1; TC-GS-USER-408 `System-Log-John-Doe`).
- State global yang diubah dan dipulihkan: visibilitas kolom `Field` pada tabel System Log (di-hide pada langkah 32 lalu dicentang kembali pada langkah 40); hook `before` mengosongkan preferensi Setup Column tab ini (tempat penyimpanan preferensi tidak disebut TC User; disediakan tim FE) dan hook `after` memulihkannya sebagai cadangan. Suite berjalan serial (`parallel: false`).
- Precondition TC-GS-USER-408, 624 sampai 628: login sebagai Total Control dan berada di Global Settings > User > User List (sub-tab Login User).

## Test Steps

### Pembukaan tab

1. Klik icon Search di User List, ketik `Aktor Log {runId}-101`, tekan Enter
2. Klik Name `Aktor Log {runId}-101`
3. Klik Tab `System Log`

### TC-GS-USER-624: Download CSV seluruh data tanpa toast sukses

4. Klik icon Download
5. Verifikasi overlay memuat opsi `Download as CSV` dan `Download as XLSX`
6. Klik `Download as CSV`
7. Verifikasi tidak ada toast sukses
8. Verifikasi file `System-Log-Aktor-Log-{runId}-101.csv` terunduh
9. Buka isi file `System-Log-Aktor-Log-{runId}-101.csv`
10. Verifikasi file memuat semua baris: selisih 11 baris data terhadap baseline 0 entri (11 entri seed, lebih dari 10 baris, tidak dibatasi halaman)

### TC-GS-USER-408: Download Tab System Log memakai nama file per user

11. Klik icon Download
12. Klik `Download as XLSX`
13. Verifikasi tidak ada toast
14. Verifikasi file `System-Log-Aktor-Log-{runId}-101.xlsx` terunduh

### TC-GS-USER-625: Download XLSX

15. Ubah page size ke 100
16. Verifikasi tabel menampilkan selisih 11 baris terhadap baseline 0 entri
17. Klik icon Download
18. Klik `Download as XLSX`
19. Verifikasi file `System-Log-Aktor-Log-{runId}-101.xlsx` terunduh
20. Buka isi file `System-Log-Aktor-Log-{runId}-101.xlsx`
21. Verifikasi file memuat selisih 11 baris data terhadap baseline 0 entri, sama dengan jumlah baris tabel
22. Verifikasi nilai kolom `Action`, `Object`, `Name`, `Field`, `Old Value`, dan `New Value` tiap baris pada file sama dengan baris tabel
23. Ubah page size ke 10

### TC-GS-USER-626: Download mengikuti Search aktif

24. Klik icon Search, ketik `alfa`, tekan Enter
25. Klik icon Download
26. Klik `Download as CSV`
27. Buka isi file hasil unduhan
28. Verifikasi file memuat 9 baris data (hasil search)
29. Verifikasi seluruh baris data pada file bernilai Name `Target Alfa {runId}-101`
30. Klik icon `×`
31. Tekan Enter pada input kosong

### TC-GS-USER-627: Download mengecualikan kolom hidden lalu menyertakan lagi setelah unhide

32. Klik header Column Visibility (⋯), hilangkan centang kolom `Field`
33. Verifikasi kolom `Field` tidak tampil di tabel
34. Klik icon Download
35. Klik `Download as CSV`
36. Verifikasi tidak ada toast peringatan
37. Buka isi file hasil unduhan
38. Verifikasi file memuat kolom `Date`, `Action`, `Object`, `Name`, `Old Value`, dan `New Value`
39. Verifikasi file tidak memuat kolom `Field`
40. Klik header Column Visibility (⋯), centang kembali kolom `Field`
41. Verifikasi kolom `Field` tampil kembali di tabel
42. Klik icon Download
43. Klik `Download as CSV`
44. Buka isi file hasil unduhan
45. Verifikasi file memuat kolom `Field`

### TC-GS-USER-628: Nilai kosong ditulis `—` di file export

46. Klik icon Download
47. Klik `Download as CSV`
48. Buka isi file hasil unduhan
49. Verifikasi sel Old Value pada baris Action `Create` ditulis `—`
50. Verifikasi sel New Value pada baris Action `Delete` ditulis `—`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Spec melewati sekitar 35 langkah (50 langkah) karena enam blok TC berada di satu kelas harness (kelas f, isi berkas unduhan) pada satu dataset. Tiap blok mengunduh berkasnya sendiri dan tidak bergantung pada hasil blok lain kecuali pembacaan berkas yang tertulis di langkahnya, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pemilik log: TC sumber memakai `John Doe` (TC-GS-USER-408) dan `Siti Nurhaliza` (TC-GS-USER-624 sampai 628) sebagai pemilik System Log; isi log kedua user itu bergantung pada aksi spec lain. Spec memakai user milik spec (`Aktor Log`) dengan aksi seed yang diketahui (S-06, S-11), sehingga nama berkas memuat nama user milik spec dengan aturan penamaan yang sama.
- Urutan TC dalam spec: TC-GS-USER-624, 408, 625, 626, 627, 628. Alasan: TC-GS-USER-624 memuat `Verifikasi` isi overlay Download (bagian screening) dan unduhan tanpa saringan sehingga ditaruh pertama; TC-GS-USER-626 dan 627 memasang Search dan menyembunyikan kolom, sehingga dijalankan sesudah unduhan tanpa saringan; TC-GS-USER-628 di akhir pada konfigurasi tabel yang sudah dipulihkan.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): langkah 1 sampai 3 (membuka User Detail; Name dicari di User List), langkah 30 sampai 31 (mengosongkan Search sebelum TC-GS-USER-627), langkah 15 dan 23 (page size 100 agar seluruh 11 baris tampil pada tabel untuk TC-GS-USER-625, lalu pemulihan page size 10). Langkah 9, 20, 27, 37, 44, 48 (membuka isi berkas) adalah langkah TC "Buka file" atau pembacaan berkas yang diperlukan `Verifikasi` berikutnya. Langkah 33 (kolom `Field` tidak tampil) dan 41 (kolom `Field` tampil kembali) adalah observasi keadaan sebelum unduhan (S-14).
- Langkah 38 (file memuat kolom lain) adalah anchor positif untuk `Verifikasi` ketiadaan kolom `Field` pada langkah 39 (bagian 8b butir 2). `Verifikasi` tidak ada toast (langkah 7, 13, 36) diletakkan segera sesudah klik pilihan format dan sebelum `Verifikasi` berkas (bagian 8b butir 11); klik pilihan format menjadi anchor positifnya.
- Isi berkas export dipisah dari kegagalan export (kelas binary buffer, prinsip 13f); kegagalan unduhan seluruh permukaan tabel ada di spec 069.
- Asersi pada berkas memakai pola baris dan kolom (bukan urutan), sehingga entri log dari run atau spec lain tidak memengaruhi hasil.
- Pembagian TC lintas spec: Search, Filter, Sort, Pagination Tab System Log di spec 096 sampai 099; Setup Column di spec 100.
- Total entri Tab System Log tidak diasersi sebagai angka absolut (S-12, bagian 8b butir 10): asersi jumlah baris total memakai selisih 11 terhadap baseline 0 yang ditulis eksplisit di Prerequisites (user seed bersuffix `-101` dibuat baru, jadi baseline nol). Hitungan hasil Search atau Filter bersuffix dan isi per halaman tidak berubah.
- Temuan untuk QA: (1) TC-GS-USER-408 dan 625 mengasersi hal yang sama (unduhan XLSX bernama `System-Log-[User-Name]`); spec menjalankan keduanya pada user yang sama. (2) TC-GS-USER-626 judul "Search/Filter aktif" tetapi langkah dan Expected hanya memuat Search; Filter tidak diuji di spec ini. (3) TC-GS-USER-628 tidak menyebut sel yang diamati; spec memakai Old Value baris Create dan New Value baris Delete. (4) TC-GS-USER-627 "Hide 1 kolom" tidak menyebut kolom; spec memakai `Field`. (5) TC-GS-USER-626 "keyword" tidak disebut; spec memakai `alfa`. (6) TC-GS-USER-624 "semua baris" tidak menyebut cara mengetahui total entri; spec membandingkan dengan 11 entri seed (lebih dari 10 baris halaman). (7) TC-GS-USER-625 "sama dengan baris tabel" tidak menyebut halaman tabel yang dibandingkan; spec menaikkan page size ke 100 sehingga seluruh 11 baris tampil di tabel.
