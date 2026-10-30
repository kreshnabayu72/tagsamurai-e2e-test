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
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Target Alfa` (cabut tier Total Control lebih dulu bila diperlukan), `Target Beta` bila masih ada, dan `Aktor Log`; hapus sisa user bersuffix `-101` dari run lama; hapus berkas unduhan. Entri log tidak bisa dihapus.
- Kemampuan teknis (kelas binary buffer, prinsip 13f konvensi): menangkap berkas unduhan browser ke direktori bersih per unduhan supaya nama berkas yang sama tidak tertimpa atau diberi akhiran `(1)`; membaca isi berkas CSV dan XLSX (nama kolom, jumlah baris data, nilai sel). Nama berkas mengikuti `System-Log-[User-Name]` dengan spasi diganti `-` (PRD user.md §4.1; TC-GS-USER-408 `System-Log-John-Doe`).
- State global yang diubah dan dipulihkan: visibilitas kolom `Field` pada tabel System Log (di-hide pada langkah 26 lalu dicentang kembali pada langkah 34); hook `before` mengosongkan preferensi Setup Column tab ini (tempat penyimpanan preferensi tidak disebut TC User; disediakan tim FE) dan hook `after` memulihkannya sebagai cadangan. Suite berjalan serial (`parallel: false`).
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
7. Verifikasi file `System-Log-Aktor-Log-{runId}-101.csv` terunduh
8. Buka isi file `System-Log-Aktor-Log-{runId}-101.csv`
9. Verifikasi file memuat semua 11 baris data (lebih dari 10 baris, tidak dibatasi halaman)
10. Verifikasi tidak ada toast sukses

### TC-GS-USER-408: Download Tab System Log memakai nama file per user

11. Klik icon Download
12. Klik `Download as XLSX`
13. Verifikasi file `System-Log-Aktor-Log-{runId}-101.xlsx` terunduh
14. Verifikasi tidak ada toast

### TC-GS-USER-625: Download XLSX

15. Klik icon Download
16. Klik `Download as XLSX`
17. Verifikasi file `System-Log-Aktor-Log-{runId}-101.xlsx` terunduh

### TC-GS-USER-626: Download mengikuti Search aktif

18. Klik icon Search, ketik `alfa`, tekan Enter
19. Klik icon Download
20. Klik `Download as CSV`
21. Buka isi file hasil unduhan
22. Verifikasi file memuat 9 baris data (hasil search)
23. Verifikasi seluruh baris data pada file bernilai Name `Target Alfa {runId}-101`
24. Klik icon `×`
25. Tekan Enter pada input kosong

### TC-GS-USER-627: Download mengecualikan kolom hidden lalu menyertakan lagi setelah unhide

26. Klik header Column Visibility (⋯), hilangkan centang kolom `Field`
27. Verifikasi kolom `Field` tidak tampil di tabel
28. Klik icon Download
29. Klik `Download as CSV`
30. Buka isi file hasil unduhan
31. Verifikasi file memuat kolom `Date`, `Action`, `Object`, `Name`, `Old Value`, dan `New Value`
32. Verifikasi file tidak memuat kolom `Field`
33. Verifikasi tidak ada toast peringatan
34. Klik header Column Visibility (⋯), centang kembali kolom `Field`
35. Verifikasi kolom `Field` tampil kembali di tabel
36. Klik icon Download
37. Klik `Download as CSV`
38. Buka isi file hasil unduhan
39. Verifikasi file memuat kolom `Field`

### TC-GS-USER-628: Nilai kosong ditulis `-` di file export

40. Klik icon Download
41. Klik `Download as CSV`
42. Buka isi file hasil unduhan
43. Verifikasi sel Old Value pada baris Action `Create` ditulis `-`
44. Verifikasi sel New Value pada baris Action `Delete` ditulis `-`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Spec melewati sekitar 35 langkah (44 langkah) karena enam blok TC berada di satu kelas harness (kelas f, isi berkas unduhan) pada satu dataset. Tiap blok mengunduh berkasnya sendiri dan tidak bergantung pada hasil blok lain kecuali pembacaan berkas yang tertulis di langkahnya, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pemilik log: TC sumber memakai `John Doe` (TC-GS-USER-408) dan `Siti Nurhaliza` (TC-GS-USER-624 sampai 628) sebagai pemilik System Log; isi log kedua user itu bergantung pada aksi spec lain. Spec memakai user milik spec (`Aktor Log`) dengan aksi seed yang diketahui (S-06, S-11), sehingga nama berkas memuat nama user milik spec dengan aturan penamaan yang sama.
- Urutan TC dalam spec: TC-GS-USER-624, 408, 625, 626, 627, 628. Alasan: TC-GS-USER-624 memuat `Verifikasi` isi overlay Download (bagian screening) dan unduhan tanpa saringan sehingga ditaruh pertama; TC-GS-USER-626 dan 627 memasang Search dan menyembunyikan kolom, sehingga dijalankan sesudah unduhan tanpa saringan; TC-GS-USER-628 di akhir pada konfigurasi tabel yang sudah dipulihkan.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): langkah 1 sampai 3 (membuka User Detail; Name dicari di User List), langkah 24 sampai 25 (mengosongkan Search sebelum TC-GS-USER-627). Langkah 8, 21, 30, 38, 42 (membuka isi berkas) adalah langkah TC "Buka file" atau pembacaan berkas yang diperlukan `Verifikasi` berikutnya. Langkah 27 (kolom `Field` tidak tampil) dan 35 (kolom `Field` tampil kembali) adalah observasi keadaan sebelum unduhan (S-14).
- Langkah 31 (file memuat kolom lain) adalah anchor positif untuk `Verifikasi` ketiadaan kolom `Field` pada langkah 32 (bagian 8b butir 2).
- Isi berkas export dipisah dari kegagalan export (kelas binary buffer, prinsip 13f); kegagalan unduhan seluruh permukaan tabel ada di spec 069.
- Asersi pada berkas memakai pola baris dan kolom (bukan urutan), sehingga entri log dari run atau spec lain tidak memengaruhi hasil.
- Pembagian TC lintas spec: Search, Filter, Sort, Pagination Tab System Log di spec 096 sampai 099; Setup Column di spec 100.
- Temuan untuk QA: (1) TC-GS-USER-408 dan 625 mengasersi hal yang sama (unduhan XLSX bernama `System-Log-[User-Name]`); spec menjalankan keduanya pada user yang sama. (2) TC-GS-USER-626 judul "Search/Filter aktif" tetapi langkah dan Expected hanya memuat Search; Filter tidak diuji di spec ini. (3) TC-GS-USER-628 menulis nilai kosong `-` sedangkan tabel UI menampilkan nilai kosong `—` (PRD user.md §4.1.6); spec mengasersi `-` di berkas sesuai TC. (4) TC-GS-USER-628 tidak menyebut sel yang diamati; spec memakai Old Value baris Create dan New Value baris Delete. (5) TC-GS-USER-627 "Hide 1 kolom" tidak menyebut kolom; spec memakai `Field`. (6) TC-GS-USER-626 "keyword" tidak disebut; spec memakai `alfa`. (7) TC-GS-USER-624 "semua baris" tidak menyebut cara mengetahui total entri; spec membandingkan dengan 11 entri seed (lebih dari 10 baris halaman).
