---
id: TC-GS-USER-E2E-095-tab-changelog-detail-download-isi-file-csv-xlsx
title: "Tab Changelog Detail: Download CSV/XLSX (Isi Berkas, Cakupan Search, Kolom Hidden, dan Nilai Kosong)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-584
  - TC-GS-USER-588
  - TC-GS-USER-406
  - TC-GS-USER-585
  - TC-GS-USER-586
  - TC-GS-USER-587
coverage:
  web: automated
---

# Tab Changelog Detail: Download CSV/XLSX (Isi Berkas, Cakupan Search, Kolom Hidden, dan Nilai Kosong)

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza, tampil `Siti N`) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before` spec ini; akun ini adalah akun default suite sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > User > User List (sub-tab Login User). Password tidak ditulis di spec atau fixture.
- Akun aksi lewat API (tidak login UI): Manage user and role Full CRUD (Fajar Nugroho, tampil `Fajar N`) `manageUserFullCrud_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 4; kredensial `Spectra.env.GS_FULLCRUD_PASSWORD`). Dipakai hanya untuk membuat entri Changelog dengan Modified By kedua.
- Env var: `GS_TC_PASSWORD`, `GS_FULLCRUD_PASSWORD`.
- Data Pre-setup yang dipakai (hanya dibaca, tidak diubah; S-06): Position `Staff`, `Supervisor`, `Finance Manager`, dan `Internal Auditor` (Tabel Data Uji Pre-setup No. 22) dan Client PT Maju Bersama dengan subscription Fixed Asset + Supply Asset (No. 26). John Doe (No. 18) yang disebut TC tidak dipakai: riwayat Changelog-nya tidak dijamin memuat sedikitnya dua nilai distinct pada kolom yang diuji (S-11) dan data Pre-setup tidak diubah (S-06), sehingga spec memakai user uji milik spec.
- Data Dinamis (user uji milik spec, seeding lewat API di hook `before`; kemampuan seeding user lewat API disediakan tim FE/BE, endpoint tidak disebut di TC dan PRD):
  - User uji: Name `Log User {runId}-095`, Email `loguser+{runId}-095@qwertysystem.net`, Position `Staff`, Employee ID `{empId1}`, Access `Fixed Asset`, Active. `{empId1}`, `{empId2}`, `{empId3}` adalah tiga Employee ID numerik murni, naik berurutan (`{empId1}` < `{empId2}` < `{empId3}`), unik per run, dibuat hook dari waktu run (tanpa suffix `{runId}` karena nilainya harus numerik murni).
  - Entri Changelog base (12 entri, urutan seeding = urutan waktu, dari terlama ke terbaru; Modified By tampil `[First Name] [Last Initial]`):
    - a. `Create` | `Name` | `—` | `Log User {runId}-095` | `Siti N`
    - b. `Edit` | `Position` | `Staff` | `Supervisor` | `Siti N`
    - c. `Edit` | `Employee ID` | `{empId1}` | `{empId2}` | `Siti N`
    - d. `Deactivate` | `Status (Global)` | `Active` | `Inactive` | `Siti N`
    - e. `Activate` | `Status (Global)` | `Inactive` | `Active` | `Siti N`
    - f. `Add Access` | `App Access` | `—` | `Supply Asset` | `Siti N`
    - g. `Remove Access` | `App Access` | `Supply Asset` | `—` | `Siti N`
    - h. `Edit` | `Position` | `Supervisor` | `Finance Manager` | `Fajar N`
    - i. `Edit` | `Position` | `Finance Manager` | `Staff` | `Fajar N`
    - j. `Edit` | `Employee ID` | `{empId2}` | `{empId3}` | `Fajar N`
    - k. `Edit` | `Position` | `Staff` | `Internal Auditor` | `Fajar N`
    - l. `Edit` | `Position` | `Internal Auditor` | `Supervisor` | `Fajar N`
  - Pelaku entri: `Siti N` lewat sesi API Total Control, `Fajar N` lewat sesi API Fajar Nugroho. Dengan demikian kolom Modified By memuat dua nilai distinct (`Siti N`, `Fajar N`); kolom Action, Field, Old Value, dan New Value memuat sedikitnya dua nilai distinct (S-11).
- Kemampuan teknis yang disediakan tim FE/BE (TC, PRD, dan LLD tidak memberi cara): memberi cap waktu pada entri seed sehingga setiap entri berjarak sedikitnya 1 menit dari entri sebelumnya mengikuti urutan huruf di atas, dan entri a (`Create`) bercap tanggal hari uji dikurangi 2 hari (H-2) sedangkan entri lain bercap hari uji. Cap waktu ini membuat urutan Date deterministik (entri terbaru di atas) dan memberi dua nilai distinct pada kolom Date.
- Kemampuan teknis (kelas binary buffer, prinsip 13f): menangkap berkas unduhan browser ke direktori bersih terpisah per unduhan; membaca isi berkas CSV dan XLSX (nama berkas, header kolom, jumlah dan isi baris data); membaca total entri Changelog user uji sebagai pembanding jumlah baris.
- Konfigurasi kolom Tab Changelog akun Total Control dalam keadaan default (6 kolom tampil, tanpa pin) saat spec dimulai; hook `before` mengosongkan konfigurasi kolom Tab Changelog bila perlu (mekanisme disediakan tim FE).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus user uji `Log User {runId}-095` lewat API; hapus berkas unduhan. Entri Changelog tidak bisa dihapus.
- Precondition TC-GS-USER-406, 584, 585, 586, 587, 588: login sebagai Total Control dan berada di Global Settings > User > User List (sub-tab Login User); data Pre-setup (Tabel Data Uji Pre-setup No. 10 sampai 22) tersedia; user uji punya riwayat Changelog.
- Suite serial (`parallel: false`) karena spec membaca dan mengubah konfigurasi kolom Tab Changelog di browser yang sama dengan spec lain.
- State global yang diubah dan dipulihkan: tidak ada yang bertahan; visibilitas kolom yang diubah di dalam spec dikembalikan lewat langkah, dan hook `after` memulihkan konfigurasi kolom Tab Changelog ke nilai awal sebagai cadangan.

## Test Steps

### TC-GS-USER-584: Download CSV seluruh data tanpa toast sukses

1. Klik icon Search di User List, ketik `Log User {runId}-095`, tekan Enter
2. Klik Name `Log User {runId}-095` di User List
3. Klik Tab `Changelog`
4. Klik icon Download
5. Verifikasi overlay memuat opsi `Download as CSV`
6. Verifikasi overlay memuat opsi `Download as XLSX`
7. Klik `Download as CSV`
8. Verifikasi file `Changelog-Log-User-{runId}-095.csv` terunduh
9. Verifikasi file memuat semua baris (12 baris data, sama dengan total entri Changelog user uji dan lebih dari 10 baris halaman)
10. Verifikasi tidak ada toast sukses

### TC-GS-USER-588: Nilai kosong ditulis `-` di file export

11. Klik icon Download, lalu klik `Download as CSV`
12. Buka file CSV yang terunduh
13. Verifikasi sel kosong ditulis `-` (baris `Create`: Old Value `-`; baris `Remove Access`: New Value `-`)

### TC-GS-USER-406: Download Tab Changelog memakai nama file per user

14. Klik icon Download, lalu klik `Download as XLSX`
15. Verifikasi file `Changelog-Log-User-{runId}-095.xlsx` terunduh
16. Verifikasi tidak ada toast

### TC-GS-USER-585: Download XLSX

17. Klik icon Download
18. Klik `Download as XLSX`
19. Verifikasi file `Changelog-Log-User-{runId}-095.xlsx` terunduh

### TC-GS-USER-586: Download mengikuti Search aktif

20. Klik icon Search, ketik `edit`, tekan Enter
21. Klik icon Download, lalu klik `Download as CSV`
22. Verifikasi file hanya berisi baris hasil search (7 baris data, semuanya Action `Edit`, lebih sedikit dari 12 baris pada unduhan tanpa Search)
23. Klik icon ×, lalu tekan Enter pada input kosong

### TC-GS-USER-587: Download mengecualikan kolom hidden lalu menyertakan lagi setelah unhide

24. Klik header kolom Column Visibility (⋯), hilangkan centang `Old Value`, lalu tutup overlay
25. Verifikasi kolom `Old Value` tidak tampil
26. Klik icon Download, lalu klik `Download as CSV`
27. Verifikasi file pertama tidak memuat kolom `Old Value`
28. Verifikasi file pertama tidak disertai toast peringatan
29. Klik header kolom Column Visibility (⋯), centang kembali `Old Value`, lalu tutup overlay
30. Verifikasi kolom `Old Value` tampil kembali
31. Klik icon Download, lalu klik `Download as CSV`
32. Verifikasi file kedua memuat kolom `Old Value`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-GS-USER-584, 588, 406, 585, 586, 587. Alasan: TC-GS-USER-584 dan 588 mengunduh CSV penuh tanpa saringan dan TC-GS-USER-406 dan 585 mengunduh XLSX penuh, sehingga keempatnya dijalankan sebelum TC-GS-USER-586 (Search aktif) dan 587 (kolom hidden) yang mengubah cakupan unduhan; TC-GS-USER-587 terakhir karena mengubah visibilitas kolom. Detail user dan Tab `Changelog` dibuka sekali di langkah 1 sampai 3.
- Langkah 1 sampai 3 (mencari user uji lewat Search User List, lalu klik Name dan Tab `Changelog`) adalah langkah penghubung tanpa `Verifikasi`; TC menulis "Klik Name `John Doe`" tanpa cara menemukan baris, dan user uji milik spec menggantikan John Doe (lihat Prerequisites).
- Nama berkas mengikuti nama user dengan spasi diganti hyphen (`Changelog-[User-Name]`, PRD user.md §4.1; contoh TC `Changelog-John-Doe`), sehingga user uji `Log User {runId}-095` menghasilkan `Changelog-Log-User-{runId}-095`.
- Isi berkas export dipisah dari spec kegagalan export (kelas binary buffer, prinsip 13f). Tiap unduhan ditangkap ke direktori terpisah (Prerequisites) karena nama berkas CSV kedua sama dengan unduhan sebelumnya.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): membersihkan Search (Klik icon ×, lalu Enter pada input kosong) setelah TC-GS-USER-586; menyembunyikan lalu menampilkan kembali `Old Value` lewat overlay Column Visibility tanpa Save pada TC-GS-USER-587; langkah "Buka file CSV yang terunduh" di TC-GS-USER-588 adalah langkah TC.
- TC-GS-USER-406 dan 585 menguji unduhan XLSX yang sama (nama berkas tanpa toast); keduanya mengunduh sendiri sehingga masing-masing punya `Verifikasi` Expected-nya. Pada TC-GS-USER-406 `Verifikasi` tidak ada toast adalah Expected TC; pada TC-GS-USER-585 Expected hanya berkas terunduh.
- Asersi tambahan di luar Expected TC (S-03): `Verifikasi` jumlah baris data 7 pada TC-GS-USER-586 (semua baris Action `Edit`) dan 12 pada TC-GS-USER-584 (total entri) membuktikan cakupan Search dan "semua baris"; `Verifikasi` kolom `Old Value` tidak tampil di tabel pada TC-GS-USER-587 adalah anchor sebelum unduhan.
- Pembagian TC Tab Changelog di User Detail: Download di spec 095. TC-GS-USER-406 diverifikasi di spec 095; TC-GS-USER-405 (screening toolbar `Download`) di spec 090.
- Spec berjalan sekitar 35 langkah (32 langkah), semua blok satu kelas harness (isi berkas export Tab Changelog), satu akun, satu dataset.
- Temuan untuk QA: (1) Cap waktu entri Changelog (entri `Create` H-2, jarak sedikitnya 1 menit antar entri) tidak punya cara di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE (S-13). (2) Label Field Changelog untuk perubahan Employee ID tidak disebut eksplisit (PRD user.md §8.3 hanya menulis `[Field]`); spec memakai `Employee ID`. (3) TC-GS-USER-584 Expected b "semua baris" tidak menyebut cara mengetahui total entri; spec membandingkan jumlah baris data berkas dengan total entri user uji (12) yang dibaca tim FE/BE. (4) TC-GS-USER-588 Expected "sel kosong ditulis `-`" memakai hyphen, sedangkan tabel menampilkan `—` (em dash); spec mengasersi `-` di berkas (prd-conventions.md §9.9). (5) TC-GS-USER-406 dan 585 menguji unduhan XLSX yang sama; keduanya tetap ditulis sesuai TC. (6) TC-GS-USER-587 Expected "tanpa toast peringatan" tidak menyebut kolom yang disembunyikan; spec memakai `Old Value`. (7) TC-GS-USER-586 tidak menyebut keyword; spec memakai `edit`.

