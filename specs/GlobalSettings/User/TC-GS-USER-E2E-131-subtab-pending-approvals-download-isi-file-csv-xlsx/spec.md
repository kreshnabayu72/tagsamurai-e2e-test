---
id: TC-GS-USER-E2E-131-subtab-pending-approvals-download-isi-file-csv-xlsx
title: "Sub-tab Pending Approvals: Download CSV/XLSX (Isi Berkas, Cakupan Search, Kolom Hidden, Nilai Kosong)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-395
  - TC-GS-USER-823
  - TC-GS-USER-824
  - TC-GS-USER-825
  - TC-GS-USER-826
  - TC-GS-USER-827
coverage:
  web: automated
---

# Sub-tab Pending Approvals: Download CSV/XLSX (Isi Berkas, Cakupan Search, Kolom Hidden, Nilai Kosong)

## Prerequisites

- Mode: FE+BE. Spec hanya membaca sub-tab Pending Approvals Ahmad Fauzi (read-only, tanpa row action) dan tidak mengubah data Pre-setup User.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login dan navigasi ke Global Settings > User > User List (sub-tab Login User) dilakukan sekali di hook `before` (seedSession); hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup, hanya dibaca): Ahmad Fauzi (No. 13, data Responsibilities FAMS).
- Data Dinamis (HK8, seeding minimal S-11; seeding user dan approval FAMS lewat API di hook `before` adalah kemampuan yang disediakan tim FE/BE, endpoint tidak disebut di TC, PRD, dan LLD):
  - Requester seed (user biasa, Access `Fixed Asset`, Division `Finance`): R1 First Name `Budi`, Last Name `Santoso {runId}-131`, email `budisantoso+{runId}-131@qwertysystem.net`, tampil di tabel `Budi S`; R2 First Name `Citra`, Last Name `Anggraini {runId}-131`, email `citraanggraini+{runId}-131@qwertysystem.net`, tampil `Citra A`; R3 First Name `Dedi`, Last Name `Kurniawan {runId}-131`, email `dedikurniawan+{runId}-131@qwertysystem.net`, tampil `Dedi K`.
  - 30 request approval in-flight (status Waiting for Approval) dengan Approver Ahmad Fauzi (Pre-setup No. 13), sehingga tabel Pending Approvals Ahmad Fauzi memuat lebih dari satu halaman (page size 10). Transaction ID dibuat FAMS saat seeding dan dikembalikan ke spec; nilainya tidak ditulis di spec. Submission Date `D1` = hari uji dikurangi 14 hari dan `D2` = hari uji dikurangi 7 hari (kemampuan menetapkan Submission Date seed disediakan tim FE/BE), teks tanggal dibaca dari sel tabel dalam Date Format General Settings.
  - Transaction `Transfer`, `{transaksi-B}`, dan `{transaksi-C}`: `Transfer` dan dua nilai Transaction FAAP lain yang namanya tidak memuat `ransf`, dipilih tim FE/BE saat seeding (TC dan PRD tidak menyebut nilai selain `Transfer`). `{transaksi-D}` = satu nilai Transaction FAAP lain yang tidak di-seed (tidak punya baris).

    | Kelompok | Transaction | Requester | Submission Date | Jumlah baris |
    |---|---|---|---|---|
    | S1 | `Transfer` | R1 `Budi S` | D1 | 6 |
    | S2 | `Transfer` | R2 `Citra A` | D2 | 4 |
    | S3 | `{transaksi-B}` | R2 `Citra A` | D1 | 6 |
    | S4 | `{transaksi-B}` | R3 `Dedi K` | D2 | 6 |
    | S5 | `{transaksi-C}` | R3 `Dedi K` | D1 | 4 |
    | S6 | `{transaksi-C}` | R1 `Budi S` | D2 | 4 |

  - Hasil per dimensi: Transaction `Transfer` 10 baris, `{transaksi-B}` 12 baris, `{transaksi-C}` 8 baris; Requester R1, R2, R3 masing-masing 10 baris; Submission Date D1 16 baris, D2 14 baris. Tiap kolom yang diuji (Transaction, Requester, Submission Date) memuat tiga, tiga, dan dua nilai distinct.
  - Baris contoh = satu baris kelompok S1 (Transfer, R1 `Budi S`, D1); Transaction ID-nya `{trxId-contoh}` dikembalikan oleh seeding.
  - Keyword unik Requester (hanya cocok dengan Requester seed spec ini karena memuat suffix): `ntoso {runId}-131` (R1), `raini {runId}-131` (R2), `{runId}-131` (R1, R2, R3).
  - Baris Pre-setup Pending Approvals Ahmad Fauzi (bila ada) tidak diubah dan jumlahnya tidak diasumsikan: asersi jumlah baris memakai keyword atau filter yang hanya cocok dengan baris seed, dan asersi urutan atau isi umum tidak bergantung pada baris Pre-setup.
  - Cleanup di hook `after` (tanpa berasumsi seeding berhasil penuh): hapus 30 request approval seed dan user Requester seed lewat API.
- Data uji: format `CSV` (TC-GS-USER-395, 823, 825, 826, 827) dan `XLSX` (TC-GS-USER-824); Search `ntoso {runId}-131` (TC-GS-USER-825, 10 baris R1 `Budi S`); kolom `Requester` di-hide lalu di-unhide (TC-GS-USER-826); `{total-baris}` = jumlah seluruh baris tabel (30 seed ditambah baris Pre-setup), dibaca dari tabel pada page size 100.
- Kemampuan teknis (kelas binary buffer, prinsip 13f konvensi): menangkap berkas unduhan browser (event download) ke direktori bersih per unduhan supaya nama berkas yang sama (`Pending-Approvals-Ahmad-Fauzi.csv`) tidak tertimpa atau diberi akhiran `(1)`; membaca isi berkas CSV dan XLSX (nama kolom, jumlah baris, nilai sel). Berkas unduhan dihapus di hook `after`.
- State yang diubah dan dipulihkan: Search ditutup dan dikosongkan (langkah 26), visibilitas kolom `Requester` dikembalikan (langkah 38), page size dikembalikan ke 10 (langkah 6); hook `after` sebagai cadangan.
- Hook `beforeEach`: kembali ke layar Global Settings > User > User List (sub-tab Login User).
- Suite berjalan serial (`parallel: false`): tabel Pending Approvals Ahmad Fauzi hanya boleh memuat baris Pre-setup dan seed spec ini saat spec berjalan.

## Test Steps

### TC-GS-USER-395: Download memakai nama file per user

1. Klik Name `Ahmad Fauzi` di User List
2. Klik Tab `Responsibilities`
3. Klik sub-tab `Pending Approvals`
4. Ubah page size ke 100
5. Baca jumlah baris tabel sebagai `{total-baris}`
6. Kembalikan page size ke 10
7. Klik icon Download
8. Klik `Download as CSV`
9. Verifikasi file `Pending-Approvals-Ahmad-Fauzi.csv` terunduh
10. Verifikasi tidak ada toast sukses

### TC-GS-USER-823: Download CSV seluruh data tanpa toast sukses

11. Klik icon Download
12. Verifikasi overlay opsi `Download as CSV` dan `Download as XLSX` tampil
13. Klik `Download as CSV`
14. Verifikasi file `Pending-Approvals-Ahmad-Fauzi.csv` terunduh
15. Buka isi file `Pending-Approvals-Ahmad-Fauzi.csv` yang diunduh
16. Verifikasi file memuat seluruh `{total-baris}` baris data (tidak dibatasi 10 baris halaman yang tampil)
17. Verifikasi tidak ada toast sukses

### TC-GS-USER-824: Download XLSX

18. Klik icon Download
19. Klik `Download as XLSX`
20. Verifikasi file `Pending-Approvals-Ahmad-Fauzi.xlsx` terunduh

### TC-GS-USER-825: Download mengikuti Search aktif

21. Klik icon Search, ketik `ntoso {runId}-131`, tekan Enter
22. Klik icon Download
23. Klik `Download as CSV`
24. Buka isi file `Pending-Approvals-Ahmad-Fauzi.csv` yang diunduh
25. Verifikasi file hanya memuat 10 baris hasil search (seluruh baris dengan Requester R1 `Budi S`)
26. Klik icon panah `(←)` untuk menutup Search dan mereset tabel

### TC-GS-USER-826: Download mengecualikan kolom hidden lalu menyertakan lagi setelah unhide

27. Klik header kolom Actions (⋯)
28. Hilangkan centang kolom `Requester` pada Overlay Column Visibility
29. Tutup Overlay Column Visibility
30. Klik icon Download
31. Klik `Download as CSV`
32. Buka isi file `Pending-Approvals-Ahmad-Fauzi.csv` yang diunduh
33. Verifikasi file memuat kolom `Transaction ID`, `Transaction`, dan `Submission Date`
34. Verifikasi file tidak memuat kolom `Requester`
35. Verifikasi tidak ada toast peringatan
36. Klik header kolom Actions (⋯)
37. Centang kembali kolom `Requester` pada Overlay Column Visibility
38. Tutup Overlay Column Visibility
39. Klik icon Download
40. Klik `Download as CSV`
41. Buka isi file `Pending-Approvals-Ahmad-Fauzi.csv` yang diunduh
42. Verifikasi file memuat kolom `Transaction ID`, `Transaction`, `Requester`, dan `Submission Date`

### TC-GS-USER-827: Nilai kosong ditulis `-` di file export

43. Buka isi file `Pending-Approvals-Ahmad-Fauzi.csv` hasil unduhan langkah 15 (tabel tanpa Search dan Filter, semua kolom visible)
44. Verifikasi tidak ada sel kosong pada berkas: setiap sel terisi nilai atau `-`

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE. Kelas harness binary buffer (prinsip 13f): isi berkas CSV dan XLSX dipisah dari kegagalan ekspor. Dependensi data Pending Approvals Ahmad Fauzi dipenuhi spec ini lewat seeding di hook `before`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber (395, 823, 824, 825, 826, 827) dipertahankan. TC-GS-USER-827 membaca berkas `Pending-Approvals-Ahmad-Fauzi.csv` hasil unduhan TC-GS-USER-823 (langkah 15) tanpa unduh ulang: state tabel keduanya identik (tanpa Search dan Filter, semua kolom), sehingga langkah "Download CSV" TC-GS-USER-827 terpenuhi unduhan itu.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 4 sampai 6 (mengubah page size ke 100, membaca jumlah baris `{total-baris}`, mengembalikan ke 10 supaya unduhan diuji pada page size 10), 15, 24, 32, 41, dan 43 (membuka isi berkas unduhan), 26 (menutup Search dan mereset tabel), serta 29 dan 38 (menutup Overlay Column Visibility).
- TC-GS-USER-395 dan TC-GS-USER-823 sama-sama mengasersi nama berkas dan tidak adanya toast sukses; masing-masing mengunduh sendiri karena TC-GS-USER-823 juga mengasersi overlay opsi dan isi berkas.
- Pembagian TC lintas spec: TC-GS-USER-393, 394, 792 sampai 797 ada di spec 126; TC-GS-USER-798 sampai 806 ada di spec 127; TC-GS-USER-807 sampai 811 ada di spec 128; TC-GS-USER-812, 813, 828, 829 ada di spec 129; TC-GS-USER-814 sampai 822 (Setup Column) ada di spec 130.
- Spec melewati sekitar 35 langkah (44 langkah) karena enam TC Download berada di satu kelas harness (binary buffer), satu sub-tab, dan dataset seed yang sama; blok 395, 823, 824, 825, dan 826 mengunduh berkas sendiri, blok 827 membaca berkas blok 823, dan langkah membuka isi berkas termasuk blok baca berpola.
- Temuan untuk QA:
  - TC-GS-USER-827: PRD §4.1.3 menetapkan semua kolom Pending Approvals "Tidak pernah kosong", sehingga seeding tidak dapat menghasilkan sel kosong yang ditulis `-`. Spec hanya mengasersi tidak ada sel kosong; Expected "sel kosong ditulis `-`" tidak teramati sebagai nilai `-`.
  - TC-GS-USER-825: judul menyebut "Search/Filter aktif" tetapi langkah dan Expected hanya Search; Filter tidak diuji di spec ini.
  - TC-GS-USER-825 dan 826: TC tidak menyebut format nilai Requester di berkas (nama lengkap atau `[First Name] [Last Initial]`) dan nama header kolom berkas; spec mengasersi baris milik Requester R1 dan keberadaan kolom `Requester` sesuai judul kolom tabel.
  - TC-GS-USER-823: TC tidak menyebut jumlah total baris; spec membacanya dari tabel (`{total-baris}`).
  - TC-GS-USER-395, 823 sampai 827: TC tidak menyebut cara menangkap berkas unduhan dan membaca isinya; kemampuan tersebut disediakan tim FE (Prerequisites).
  - Mekanisme seeding user Requester dan request approval FAMS (jenis Transaction, Requester, Submission Date, Approver) tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE tanpa endpoint karangan. TC tidak menyebut nilai Transaction selain `Transfer`; dua nilai FAAP lain dipilih tim FE/BE.
  - Mekanisme menyetel flag Guided Tooltip `gs-user` tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (hook suite).
