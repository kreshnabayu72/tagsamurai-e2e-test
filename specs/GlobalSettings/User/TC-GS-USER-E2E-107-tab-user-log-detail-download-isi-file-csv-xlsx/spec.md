---
id: TC-GS-USER-E2E-107-tab-user-log-detail-download-isi-file-csv-xlsx
title: "Tab User Log Detail: Download CSV/XLSX (Nama Berkas, Isi, Cakupan Search, Kolom Hidden, dan Nilai Kosong)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-410
  - TC-GS-USER-664
  - TC-GS-USER-665
  - TC-GS-USER-666
  - TC-GS-USER-667
  - TC-GS-USER-668
coverage:
  web: automated
---

# Tab User Log Detail: Download CSV/XLSX (Nama Berkas, Isi, Cakupan Search, Kolom Hidden, dan Nilai Kosong)

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > User > User List (sub-tab Login User). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`, `USER_PASSWORD`, `USER_PASSWORD_NEW` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-22 dan No. 23, 26): hanya dibaca (Division dan Access dipakai sebagai nilai field user seed). TC memakai `John Doe` (Pre-setup No. 18) sebagai pemilik log, sedangkan isi User Log-nya bergantung pada riwayat login lingkungan dan tidak boleh diubah; spec memakai user seed milik spec (S-06, S-11). Spec tidak mengubah atau menghapus data Pre-setup.
- Data Dinamis, di-seed lewat API di hook `before`. User diberi Division `Finance` dan Access `Fixed Asset` (Pre-setup No. 23 dan 26):
  - U-1: Name `John Doe {runId}-107`, email `johndoe+{runId}-107@qwertysystem.net`, status Activated, password `Spectra.env.USER_PASSWORD`. Pemilik User Log yang diunduh (pengganti `John Doe` di TC). Nama berkas unduhan mengikuti PRD user.md §4.1 (`User-Log-[User-Name]`) dengan spasi pada Name ditulis `-`: `User-Log-John-Doe-{runId}-107`.
  - Riwayat event U-1 (13 event, dipicu berurutan di hook `before`; Expected TC-GS-USER-664 mensyaratkan berkas memuat semua baris tanpa dibatasi halaman sehingga jumlah baris melebihi 10; sedikitnya dua nilai distinct pada kolom, S-11):
    - Event 1 (terlama): Activity `Login`, Status `Failed`, Note `Invalid password`, IP Address `192.168.5.7`, Device / Browser `Firefox on macOS` (password salah sembarang yang disediakan tim FE/BE).
    - Event 2: Activity `Login`, Status `Success`, Note `—`, IP Address `192.168.5.7`, Device / Browser `Firefox on macOS`.
    - Event 3: Activity `Change Password`, Status `Success`, Note `Password changed`, IP Address `192.168.5.7`, Device / Browser `Firefox on macOS` (password diganti dari `Spectra.env.USER_PASSWORD` menjadi `Spectra.env.USER_PASSWORD_NEW`; login berikutnya memakai password baru).
    - Event 4: Activity `Logout`, Status `—`, Note `—`, IP Address `192.168.5.7`, Device / Browser `Firefox on macOS`.
    - Event 5 sampai 12: 4 pasang Login (Status `Success`, Note `—`) lalu Logout (Status `—`, Note `—`), seluruhnya IP Address `10.0.0.11`, Device / Browser `Chrome on Windows`.
    - Event 13 (terbaru): Activity `Login`, Status `Success`, Note `—`, IP Address `172.16.9.3`, Device / Browser `—` (User-Agent tidak dikenal, tidak terparse).
  - Hasil pada tabel (13 baris): Activity memuat `Login` (7 baris), `Logout` (5), dan `Change Password` (1); IP Address memuat `10.0.0.11` (8), `192.168.5.7` (4), dan `172.16.9.3` (1); Device / Browser memuat `Chrome on Windows` (8), `Firefox on macOS` (4), dan `—` (1). Halaman 1 menampilkan 10 baris.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API U-1, serta sisa user bersuffix `-107` dari run lama. Entri User Log tidak bisa dihapus. Berkas unduhan dihapus di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE; TC, PRD, dan LLD tidak menyebut mekanisme maupun endpoint): (a) seeding user berstatus Activated lewat API dengan password `Spectra.env.USER_PASSWORD`; (b) memicu event Login (Success dan Failed), Logout, dan Change Password (Success) untuk user uji dengan IP Address dan User-Agent tertentu, berurutan dengan jeda sedikitnya satu detik antar-event supaya cap waktu tiap event berbeda. Event dipicu berurutan sesuai daftar dan bercap waktu hari uji.
- Kemampuan teknis (kelas binary buffer, prinsip 13f konvensi): menangkap berkas unduhan browser (event download) ke direktori bersih per unduhan supaya nama berkas yang sama (mis. `User-Log-John-Doe-{runId}-107.csv`) tidak tertimpa atau diberi akhiran `(1)`; membaca isi berkas CSV (nama kolom, jumlah baris, nilai sel). Penyetelan visibilitas kolom lewat Overlay Column Visibility dan pengetikan di kotak Search.
- State yang diubah dan dipulihkan: visibilitas kolom `Note` dicentang kembali di langkah 31; Search ditutup di langkah 43; hook `after` sebagai cadangan. Suite berjalan serial (`parallel: false`).
- Precondition TC-GS-USER-410, 664 sampai 668: login sebagai Total Control dan berada di Global Settings > User > User List (sub-tab Login User).

## Test Steps

### TC-GS-USER-410: Download Tab User Log memakai nama file per user (XLSX)

1. Klik icon Search di User List, ketik `John Doe {runId}-107`, tekan Enter
2. Klik Name `John Doe {runId}-107`
3. Klik Tab `User Log`
4. Klik icon Download
5. Klik `Download as XLSX`
6. Verifikasi file `User-Log-John-Doe-{runId}-107.xlsx` terunduh
7. Verifikasi tidak ada toast

### TC-GS-USER-664: Download CSV seluruh data tanpa toast sukses

8. Klik icon Download
9. Verifikasi overlay menampilkan opsi `Download as CSV` dan `Download as XLSX`
10. Klik `Download as CSV`
11. Verifikasi file `User-Log-John-Doe-{runId}-107.csv` terunduh
12. Buka isi file `User-Log-John-Doe-{runId}-107.csv` yang diunduh
13. Verifikasi file memuat seluruh 13 baris data (tidak dibatasi 10 baris per halaman)
14. Verifikasi tidak ada toast sukses

### TC-GS-USER-668: Nilai kosong ditulis `-` di file export

15. Buka isi file `User-Log-John-Doe-{runId}-107.csv` hasil unduhan pada langkah 10
16. Verifikasi sel kosong di tabel ditulis `-` di file: Status dan Note baris Logout, Note baris Login Success, serta Device / Browser baris IP Address `172.16.9.3`
17. Verifikasi tidak ada sel kosong tanpa `-` pada seluruh baris data

### TC-GS-USER-665: Download XLSX

18. Klik icon Download
19. Klik `Download as XLSX`
20. Verifikasi file `User-Log-John-Doe-{runId}-107.xlsx` terunduh

### TC-GS-USER-667: Download mengecualikan kolom hidden, menyertakan lagi setelah unhide

21. Klik header Column Visibility (⋯)
22. Hilangkan centang kolom `Note`
23. Verifikasi kolom `Note` tidak tampil di tabel
24. Klik icon Download
25. Klik `Download as CSV`
26. Buka isi file `User-Log-John-Doe-{runId}-107.csv` yang diunduh
27. Verifikasi file memuat kolom `Date`, `Activity`, `Status`, `IP Address`, dan `Device / Browser`
28. Verifikasi kolom `Note` tidak ikut diekspor
29. Verifikasi tidak ada toast peringatan
30. Klik header Column Visibility (⋯)
31. Centang kembali kolom `Note`
32. Klik icon Download
33. Klik `Download as CSV`
34. Buka isi file `User-Log-John-Doe-{runId}-107.csv` yang diunduh
35. Verifikasi file memuat kolom `Date`, `Activity`, `Status`, `Note`, `IP Address`, dan `Device / Browser`

### TC-GS-USER-666: Download mengikuti Search aktif

36. Klik icon Search, ketik `Firefox`, tekan Enter
37. Verifikasi tabel menampilkan 4 baris dengan Device / Browser `Firefox on macOS` (hasil Search)
38. Klik icon Download
39. Klik `Download as CSV`
40. Buka isi file `User-Log-John-Doe-{runId}-107.csv` yang diunduh
41. Verifikasi file memuat 4 baris data hasil Search, seluruhnya dengan Device / Browser `Firefox on macOS`
42. Verifikasi file tidak memuat baris dengan IP Address `10.0.0.11` maupun `172.16.9.3`
43. Klik icon `←`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`. Kelas harness binary buffer (prinsip 13f): isi berkas CSV dan XLSX dipisah dari kegagalan ekspor.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pemilik log: TC sumber memakai `John Doe` (Pre-setup No. 18) dan nama berkas `User-Log-John-Doe`. Isi User Log-nya bergantung pada riwayat login lingkungan, sehingga spec memakai user milik spec dengan riwayat event yang diketahui (S-06, S-11) dan nama bersuffix per run (S-12); nama berkas mengikuti Name user seed.
- Urutan TC dalam spec: TC-GS-USER-410, 664, 668, 665, 667, 666. Urutan `sourceTc`: 410, 664, 665, 666, 667, 668. TC-GS-USER-668 membaca berkas CSV hasil unduhan TC-GS-USER-664 (langkah 10) tanpa unduh ulang karena state tabel keduanya identik (tanpa Search dan Filter, semua kolom), sehingga ditaruh tepat sesudahnya. TC-GS-USER-666 (Search aktif) di akhir karena Search harus ditutup sesudahnya, sedangkan TC-GS-USER-665 dan 667 memerlukan tabel tanpa Search.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): langkah 1 (mencari user di User List agar Name dapat diklik); langkah "Buka isi file ... yang diunduh" (12, 15, dan sesudah tiap unduhan CSV; membaca isi berkas); langkah 21 sampai 31 (hide dan unhide kolom `Note` bagian TC-GS-USER-667); langkah 43 (menutup Search).
- Asersi tambahan (dicatat sesuai S-03): TC-GS-USER-664 `Verifikasi` overlay opsi `Download as CSV` dan `Download as XLSX` mengikuti Expected a; jumlah baris 13 pada berkas adalah konkretisasi "semua baris (tidak dibatasi halaman)" untuk data seed yang diketahui. TC-GS-USER-666: `Verifikasi` 4 baris hasil Search pada tabel adalah anchor positif sebelum asersi baris lain tidak ikut diekspor (8b butir 2). TC-GS-USER-665 dan 410 hanya mengasersi nama berkas XLSX; isi XLSX tidak diasersi karena Expected TC tidak menyebutnya.
- Spec melewati sekitar 35 langkah (43 langkah) karena enam TC Download memakai tab, dataset (U-1), dan satu kelas harness (binary buffer) yang sama; langkah membaca isi berkas termasuk blok baca berpola dan unduhan CSV yang berulang merupakan prefix berulang. Tiap blok berdiri sendiri kecuali TC-GS-USER-668 yang membaca berkas hasil TC-GS-USER-664.
- Pembagian TC lintas spec: Screening dan Search TC-GS-USER-409, 411, 412, 631 sampai 637 diverifikasi di spec 102; Filter Panel TC-GS-USER-638 sampai 646 di spec 103; kombinasi Search dan Filter TC-GS-USER-647 sampai 651 di spec 104; Sort, Pagination, dan kombinasi TC-GS-USER-652 sampai 654, 669, 670 di spec 105; Setup Column TC-GS-USER-655 sampai 663 di spec 106.
- Temuan untuk QA: (1) TC-GS-USER-410 dan 664 sampai 668 memakai `John Doe` Pre-setup dan nama berkas `User-Log-John-Doe.xlsx`/`.csv`; spec memakai user seed bersuffix sehingga nama berkas `User-Log-John-Doe-{runId}-107`, dengan asumsi spasi pada Name ditulis `-` (PRD hanya menyebut `User-Log-[User-Name]`). (2) Mekanisme memicu event Login, Logout, dan Change Password dengan IP Address dan User-Agent tertentu tidak disebut di TC, PRD, dan LLD; disediakan tim FE/BE. (3) TC-GS-USER-410 dan 665 memakai `Download → XLSX`/`Download as XLSX`, sedangkan Division memakai `Download XLSX`; spec memakai `Download as CSV`/`Download as XLSX` mengikuti TC-GS-USER-664. (4) TC-GS-USER-664, 666, 667, dan 668 tidak menyebut cara menangkap berkas unduhan dan membaca isinya; kemampuan tersebut disediakan tim FE (Prerequisites). (5) TC-GS-USER-668 tidak menyebut kolom mana yang berisi sel kosong; spec mengasersi Status/Note baris Logout, Note baris Login Success, dan Device / Browser tidak terparse (padanan `—` di tabel). (6) TC-GS-USER-667 tidak menyebut kolom yang di-hide; spec memakai `Note`. (7) TC-GS-USER-666 tidak menyebut keyword; spec memakai `Firefox`. (8) TC-GS-USER-410 dan 665 hanya mengharapkan nama berkas XLSX; isi XLSX tidak diasersi. (9) Mekanisme menandai Guided Tooltip sebagai sudah dilihat tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
