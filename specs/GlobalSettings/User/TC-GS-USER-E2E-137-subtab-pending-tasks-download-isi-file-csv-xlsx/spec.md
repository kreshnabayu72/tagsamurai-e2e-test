---
id: TC-GS-USER-E2E-137-subtab-pending-tasks-download-isi-file-csv-xlsx
title: "Sub-tab Pending Tasks: Download CSV/XLSX (Isi Berkas, Cakupan Search, Kolom Hidden, dan Nilai Kosong)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-398
  - TC-GS-USER-864
  - TC-GS-USER-865
  - TC-GS-USER-866
  - TC-GS-USER-867
  - TC-GS-USER-868
coverage:
  web: automated
---

# Sub-tab Pending Tasks: Download CSV/XLSX (Isi Berkas, Cakupan Search, Kolom Hidden, dan Nilai Kosong)

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data User; yang di-seed hanya task pending FAMS milik spec (Population PT-22).
- Akun: Total Control, Siti Nurhaliza (Tabel Data Uji Pre-setup No. 2), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > User > User List (sub-tab Login User) dilakukan sekali di hook `before` (seedSession); hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Data Pre-setup (hanya dibaca, tidak diubah): Ahmad Fauzi (Tabel Data Uji Pre-setup No. 13; entitas Client PT Maju Bersama dengan subscription Fixed Asset, sehingga Tab `Responsibilities` dan sub-tab `Pending Tasks` tampil).
- Data Dinamis, Population PT-22 (task pending milik Ahmad Fauzi; sub-tab `Pending Tasks` memuat tepat 22 baris saat spec mulai). Task Borrowing dan Assignment di-seed di hook `before` lewat kemampuan seeding data FAMS (HK8) yang disediakan tim FE/BE; mekanisme dan endpoint-nya tidak ada di TC, PRD, atau LLD sehingga ditentukan tim FE/BE dan tidak dikarang di spec. Seeding juga mengatur Request Date dan Last Updated per kelompok; Group dan PIC memakai Group dan user FAMS yang disediakan tim FE/BE. Bila Ahmad Fauzi sudah memiliki task pending Pre-setup, task itu dihitung ke dalam komposisi di bawah. Transaction ID dihasilkan sistem (contoh format PRD: `ASG-YYYYMMDD-XXXX` untuk Assignment, `BRW-YYYYMMDD-XXXX` untuk Borrowing) sehingga tidak bersuffix `{runId}`; hook `before` mencatat task yang dibuat spec dan hook `after` hanya membersihkan task itu, tanpa berasumsi seeding berhasil penuh. Record User Ahmad Fauzi tidak diubah.

  | Kelompok | Baris | Transaction | Status | Group | PIC | Total Asset | Request Date | Last Updated |
  |---|---|---|---|---|---|---|---|---|
  | P | 8 | `Assignment` | `Waiting for Acceptance` | `{group-A}` | `{pic-A}` | `1` (5 baris), `2` (3 baris) | `{rd-1}` | `{lu-1}` |
  | Q1 | 12 | `Borrowing` | `Waiting for Confirmation` | `{group-B}` | `{pic-B}` | `3` (6 baris), `10` (6 baris) | `{rd-3}` | `{lu-2}` |
  | Q2 | 2 | `Borrowing` | `Waiting for Confirmation` | `{group-A}` | `{pic-B}` | `1` (1 baris), `2` (1 baris) | `{rd-2}` | `{lu-1}` |

  Aturan nilai: `{group-A}` lebih kecil dari `{group-B}` dan `{pic-A}` lebih kecil dari `{pic-B}` menurut urutan A-Z; `{rd-1}` < `{rd-2}` < `{rd-3}` dan `{lu-1}` < `{lu-2}`, ditulis dalam Date Format General Settings (nilai default environment, tidak diubah spec); `{kw-group}` (kata pertama `{group-A}`) dan `{kw-pic}` (nama depan `{pic-A}`) hanya muncul pada kolom masing-masing, dan `Acceptance` hanya muncul pada kolom Status. Turunan: Transaction `Assignment` 8 baris dan `Borrowing` 14 baris; Group `{group-A}` 10 baris dan `{group-B}` 12 baris; PIC `{pic-A}` 8 baris dan `{pic-B}` 14 baris; Total Asset `1` 6 baris, `2` 4 baris, `3` 6 baris, `10` 6 baris; page size 10 menghasilkan 3 halaman (10, 10, 2 baris).
- Data uji per TC: format `CSV` (TC-GS-USER-398, 864, 866, 867, 868) dan `XLSX` (TC-GS-USER-865); nama file `Pending-Tasks-Ahmad-Fauzi` (`Pending-Tasks-[User-Name]`, PRD `user.md` §4.1.3); TC-GS-USER-866 keyword `Assignment`; TC-GS-USER-867 kolom `PIC` di-hide lalu di-unhide.
- Kemampuan teknis (kelas binary buffer, prinsip 13f konvensi): menangkap berkas unduhan browser (event download) ke direktori bersih per unduhan supaya nama berkas yang sama (`Pending-Tasks-Ahmad-Fauzi.csv`) tidak tertimpa atau diberi akhiran `(1)`; membaca isi berkas CSV dan XLSX (nama kolom, jumlah baris, nilai sel); mendeteksi ada tidaknya toast saat unduhan. Berkas unduhan dihapus di hook `after`; seeding task pending FAMS dan pembersihannya (di atas).
- Preferensi kolom tabel Pending Tasks (visibilitas, urutan, pin) tersimpan per user di browser (cache `localStorage`, PRD `prd-conventions.md` §9.3); hook `after` menghapus preferensi itu sebagai cadangan. Nama key dan cara menghapusnya tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
- State yang diubah dan dipulihkan: kolom `PIC` dicentang kembali di langkah 35; kotak Search ditutup di langkah 25; hook `after` sebagai cadangan.
- Hook `beforeEach`: kembali ke layar Global Settings > User > User List (sub-tab Login User).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-USER-398: Nama file Download sub-tab Pending Tasks per user

1. Klik Name `Ahmad Fauzi` di User List
2. Klik Tab `Responsibilities`
3. Klik sub-tab `Pending Tasks`
4. Klik icon Download
5. Klik `Download as CSV`
6. Verifikasi file `Pending-Tasks-Ahmad-Fauzi.csv` terunduh
7. Verifikasi tidak ada toast sukses

### TC-GS-USER-864: Download CSV seluruh data tanpa toast sukses

8. Klik icon Download
9. Verifikasi overlay menampilkan opsi `Download as CSV` dan `Download as XLSX`
10. Klik `Download as CSV`
11. Verifikasi file `Pending-Tasks-Ahmad-Fauzi.csv` terunduh
12. Buka isi file `Pending-Tasks-Ahmad-Fauzi.csv` yang diunduh
13. Verifikasi file memuat seluruh 22 baris data (tidak dibatasi 10 baris halaman 1)
14. Verifikasi tidak ada toast sukses

### TC-GS-USER-865: Download XLSX

15. Klik icon Download
16. Klik `Download as XLSX`
17. Verifikasi file `Pending-Tasks-Ahmad-Fauzi.xlsx` terunduh

### TC-GS-USER-866: Download mengikuti Search aktif

18. Klik icon Search, ketik `Assignment`, tekan Enter
19. Verifikasi tabel menampilkan 8 baris Transaction `Assignment` (hasil search aktif)
20. Klik icon Download
21. Klik `Download as CSV`
22. Buka isi file hasil unduhan
23. Verifikasi file memuat 8 baris hasil search (Transaction `Assignment`)
24. Verifikasi file tidak memuat baris Transaction `Borrowing`
25. Klik icon panah `(←)` untuk menutup Search dan mereset tabel

### TC-GS-USER-867: Download mengecualikan kolom hidden lalu menyertakan lagi setelah unhide

26. Klik header kolom Column Visibility (⋯)
27. Hilangkan centang kolom `PIC` pada Overlay Column Visibility
28. Verifikasi kolom `PIC` tidak tampil di tabel
29. Klik icon Download
30. Klik `Download as CSV`
31. Buka isi file hasil unduhan pertama
32. Verifikasi file pertama tidak memuat kolom `PIC`
33. Verifikasi tidak ada toast peringatan
34. Klik header kolom Column Visibility (⋯)
35. Centang kembali kolom `PIC` pada Overlay Column Visibility
36. Klik icon Download
37. Klik `Download as CSV`
38. Buka isi file hasil unduhan kedua
39. Verifikasi file kedua memuat kolom `PIC`

### TC-GS-USER-868: Nilai kosong ditulis `-` di file export

40. Klik icon Download
41. Klik `Download as CSV`
42. Buka isi file hasil unduhan
43. Verifikasi tidak ada sel kosong di file: sel tanpa nilai ditulis `-`

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE. Kelas harness binary buffer (prinsip 13f): isi berkas CSV dan XLSX; kegagalan ekspor sub-tab Pending Tasks tidak punya TC sumber.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (398, 864, 865, 866, 867, 868) dipertahankan.
- Langkah 1 sampai 3 memenuhi langkah awal "Klik Name `Ahmad Fauzi`, Tab `Responsibilities`, sub-tab `Pending Tasks`" dari seluruh TC sumber; layar itu dibuka sekali dan dipakai bersama. Langkah "Klik Download → `Download as CSV`" TC-GS-USER-398 dan "Klik icon Download, Klik `Download as CSV`" TC-GS-USER-864 menghasilkan dua unduhan terpisah karena Expected keduanya mengamati unduhan masing-masing.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 12, 22, 31, 38, dan 42 (membuka isi berkas unduhan), langkah 27 dan 35 (hide dan unhide `PIC` untuk TC-GS-USER-867), serta langkah 25 (menutup Search sebelum TC-GS-USER-867). Search bar TC-GS-USER-866 ditutup agar TC-GS-USER-867 dan 868 mengunduh seluruh data.
- Asersi tambahan (S-03, dengan alasan): langkah 28 memastikan kolom `PIC` benar-benar hidden sebelum unduhan (S-14); `Verifikasi` 8 baris hasil search sebelum unduhan pada TC-GS-USER-866 menjadi anchor positif sebelum `Verifikasi` file tidak memuat baris Transaction `Borrowing` (bagian 8b butir 2, S-11 dua nilai distinct pada kolom Transaction); jumlah 22 baris pada TC-GS-USER-864 adalah konkretisasi "semua baris (tidak dibatasi halaman)" dari Population PT-22.
- Pembagian TC lintas spec: TC-GS-USER-396, 397, dan 830 sampai 836 ada di spec 132; TC-GS-USER-837 sampai 846 ada di spec 133; TC-GS-USER-847 sampai 851 ada di spec 134; TC-GS-USER-852 sampai 854, 869, dan 870 ada di spec 135; TC-GS-USER-855 sampai 863 ada di spec 136. TC Download sub-tab Pending Approvals ada di spec 131.
- Spec melewati sekitar 35 langkah (43 langkah) karena enam TC Download berbagi satu layar, satu dataset (PT-22), dan satu kelas harness (binary buffer). Tiap blok TC mengunduh berkasnya sendiri dan berdiri sendiri; langkah "Klik icon Download, Klik `Download as CSV`, buka isi berkas" merupakan blok baca berpola yang berulang.
- Temuan untuk QA:
  - TC-GS-USER-398 dan 864: kedua TC memverifikasi unduhan CSV seluruh data tanpa toast sukses dengan nama file yang sama; TC-GS-USER-398 tidak menyebut isi berkas.
  - TC-GS-USER-865: Expected hanya nama file `.xlsx`; TC tidak menyebut isi berkas XLSX, sehingga spec tidak mengasersi isi.
  - TC-GS-USER-866 dan 867: keyword (`Assignment`) dan kolom yang di-hide (`PIC`) tidak konkret di TC; spec memakai nilai dari Population PT-22. TC tidak menyebut cara menangkap berkas unduhan dan membaca isinya; kemampuan itu disediakan tim FE (Prerequisites).
  - TC-GS-USER-868: PRD `user.md` §4.1.3 menetapkan seluruh kolom Pending Tasks `Tidak pernah kosong`, sehingga tidak ada sel kosong yang dapat dibentuk; Expected "Sel kosong ditulis `-`" tidak dapat dibuktikan dengan data nyata. Spec hanya mengasersi tidak ada sel kosong di berkas (langkah 43). TC juga tidak menyebut kolom yang kosong.
  - Seeding task pending FAMS tidak punya mekanisme di TC, PRD, atau LLD; disediakan tim FE/BE. Nama key preferensi kolom di browser dan cara menghapusnya tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
