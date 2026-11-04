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
- Akun: Total Control, Siti Nurhaliza (Tabel Data Uji Pre-setup No. 2), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman Global Settings > User > User List (sub-tab Login User) dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Data Pre-setup (hanya dibaca, tidak diubah): Ahmad Fauzi (Tabel Data Uji Pre-setup No. 13; entitas Client PT Maju Bersama dengan subscription Fixed Asset, sehingga Tab `Responsibilities` dan sub-tab `Pending Tasks` tampil).
- Data Dinamis, Population PT-22 (task pending milik Ahmad Fauzi; sub-tab `Pending Tasks` memuat `B0` + 22 baris sesudah seeding, dengan `B0` = jumlah task pending Pre-setup Ahmad Fauzi yang dibaca lewat kemampuan baca BE tepat sebelum seeding; kemampuan itu disediakan tim FE/BE). Task Borrowing dan Assignment di-seed di hook `before` lewat kemampuan seeding data FAMS (HK8) yang disediakan tim FE/BE; mekanisme dan endpoint-nya tidak ada di TC, PRD, atau LLD sehingga ditentukan tim FE/BE dan tidak dikarang di spec. Seeding juga mengatur Request Date dan Last Updated per kelompok; Group dan PIC task seed memakai Group dan user FAMS yang disediakan tim FE/BE dan bernama bersuffix `{runId}-137` (`{group-A}` = `Alfa {runId}-137`, `{group-B}` = `Beta {runId}-137`; PIC `{pic-A}` nama lengkap `Rina Pica {runId}-137`, `{pic-B}` nama lengkap `Sari Picb {runId}-137`; teks tampil sel PIC `[First Name] [Last Initial]`: `{pic-A-tampil}` = `Rina P`, `{pic-B-tampil}` = `Sari P`, dua nilai berbeda; asersi sel dan sort kolom PIC memakai nilai tampil, nama lengkap hanya untuk Search dan hover), sehingga tidak bentrok dengan task Pre-setup. Task Pre-setup Ahmad Fauzi (`B0` baris) tidak diubah dan isinya tidak diasumsikan: asersi jumlah per nilai Group atau PIC memakai nama bersuffix itu, sedangkan asersi per nilai Transaction, Status, Total Asset, Request Date, atau Last Updated menyebut baris seed (task milik spec ini). Transaction ID dihasilkan sistem (contoh format PRD: `ASG-YYYYMMDD-XXXX` untuk Assignment, `BRW-YYYYMMDD-XXXX` untuk Borrowing) sehingga tidak bersuffix `{runId}`; hook `before` mencatat task yang dibuat spec dan hook `after` hanya membersihkan task itu, tanpa berasumsi seeding berhasil penuh. Record User Ahmad Fauzi tidak diubah.

  | Kelompok | Baris | Transaction | Status | Group | PIC | Total Asset | Request Date | Last Updated |
  |---|---|---|---|---|---|---|---|---|
  | P | 8 | `Assignment` | `Waiting for Acceptance` | `{group-A}` | `{pic-A-tampil}` | `1` (5 baris), `2` (3 baris) | `{rd-1}` | `{lu-1}` |
  | Q1 | 12 | `Borrowing` | `Waiting for Confirmation` | `{group-B}` | `{pic-B-tampil}` | `3` (6 baris), `10` (6 baris) | `{rd-3}` | `{lu-2}` |
  | Q2a | 1 | `Borrowing` | `Waiting for Confirmation` | kosong (tampil `—`) | `{pic-B-tampil}` | `1` | `{rd-2}` | `{lu-1}` |
  | Q2b | 1 | `Borrowing` | `Waiting for Confirmation` | `{group-A}` | kosong (tampil `—`) | `2` | `{rd-2}` | `{lu-1}` |

  Aturan nilai: `{group-A}` lebih kecil dari `{group-B}` dan `{pic-A-tampil}` lebih kecil dari `{pic-B-tampil}` menurut urutan A-Z; `{rd-1}` < `{rd-2}` < `{rd-3}` dan `{lu-1}` < `{lu-2}`, ditulis dalam Date Format General Settings (nilai default environment, tidak diubah spec); `{kw-group}` (`lfa {runId}-137`, potongan `{group-A}`) dan `{kw-pic}` (`Pica {runId}-137`, potongan nama lengkap `{pic-A}`) hanya muncul pada kolom masing-masing, dan `Acceptance` hanya muncul pada kolom Status. Turunan (baris seed): Transaction `Assignment` 8 baris dan `Borrowing` 14 baris; Group `{group-A}` 9 baris, `{group-B}` 12 baris, dan kosong 1 baris; PIC `{pic-A-tampil}` 8 baris, `{pic-B-tampil}` 13 baris, dan kosong 1 baris (sel kosong dibutuhkan TC-GS-USER-868); Total Asset `1` 6 baris, `2` 4 baris, `3` 6 baris, `10` 6 baris; total tabel `B0` + 22 baris sehingga page size 10 menghasilkan sedikitnya 3 halaman.
- Data uji per TC: format `CSV` (TC-GS-USER-398, 864, 866, 867, 868) dan `XLSX` (TC-GS-USER-865); nama file `Pending-Tasks-Ahmad-Fauzi` (`Pending-Tasks-[User-Name]`, PRD `user.md` §4.1.3); TC-GS-USER-866 keyword `{kw-group}` (9 baris Group `{group-A}`); TC-GS-USER-867 kolom `PIC` di-hide lalu di-unhide; TC-GS-USER-868 sel Group baris Q2a dan sel PIC baris Q2b yang kosong.
- Kemampuan teknis (kelas binary buffer, prinsip 13f konvensi): menangkap berkas unduhan browser (event download) ke direktori bersih per unduhan supaya nama berkas yang sama (`Pending-Tasks-Ahmad-Fauzi.csv`) tidak tertimpa atau diberi akhiran `(1)`; membaca isi berkas CSV dan XLSX (nama kolom, jumlah baris, nilai sel); mendeteksi ada tidaknya toast saat unduhan. Berkas unduhan dihapus di hook `after`; seeding task pending FAMS dan pembersihannya (di atas).
- Preferensi kolom tabel Pending Tasks (visibilitas, urutan, pin) tersimpan per user di browser (cache `localStorage`, PRD `prd-conventions.md` §9.3); hook `after` menghapus preferensi itu sebagai cadangan. Nama key dan cara menghapusnya tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
- State yang diubah dan dipulihkan: kolom `PIC` dicentang kembali di langkah 37; kotak Search ditutup di langkah 26; hook `after` sebagai cadangan.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-USER-398: Nama file Download sub-tab Pending Tasks per user

1. Klik icon Search di User List, ketik `Ahmad Fauzi`, tekan Enter
2. Klik Name `Ahmad Fauzi` di User List
3. Klik Tab `Responsibilities`
4. Klik sub-tab `Pending Tasks`
5. Klik icon Download
6. Klik `Download as CSV`
7. Verifikasi tidak ada toast sukses
8. Verifikasi file `Pending-Tasks-Ahmad-Fauzi.csv` terunduh

### TC-GS-USER-864: Download CSV seluruh data tanpa toast sukses

9. Klik icon Download
10. Verifikasi overlay menampilkan opsi `Download as CSV` dan `Download as XLSX`
11. Klik `Download as CSV`
12. Verifikasi tidak ada toast sukses
13. Verifikasi file `Pending-Tasks-Ahmad-Fauzi.csv` terunduh
14. Buka isi file `Pending-Tasks-Ahmad-Fauzi.csv` yang diunduh
15. Verifikasi file memuat seluruh `B0` + 22 baris data (tidak dibatasi 10 baris halaman 1)

### TC-GS-USER-865: Download XLSX

16. Klik icon Download
17. Klik `Download as XLSX`
18. Verifikasi file `Pending-Tasks-Ahmad-Fauzi.xlsx` terunduh

### TC-GS-USER-866: Download mengikuti Search aktif

19. Klik icon Search, ketik `{kw-group}`, tekan Enter
20. Verifikasi tabel menampilkan 9 baris Group `{group-A}` (hasil search aktif)
21. Klik icon Download
22. Klik `Download as CSV`
23. Buka isi file hasil unduhan
24. Verifikasi file memuat 9 baris hasil search (Group `{group-A}`)
25. Verifikasi file tidak memuat baris Group `{group-B}`
26. Klik icon panah `(←)` untuk menutup Search dan mereset tabel

### TC-GS-USER-867: Download mengecualikan kolom hidden lalu menyertakan lagi setelah unhide

27. Klik header kolom Column Visibility (⋯)
28. Hilangkan centang kolom `PIC` pada Overlay Column Visibility
29. Verifikasi kolom `PIC` tidak tampil di tabel
30. Klik icon Download
31. Klik `Download as CSV`
32. Verifikasi tidak ada toast peringatan
33. Buka isi file hasil unduhan pertama
34. Verifikasi file pertama memuat kolom `Group`
35. Verifikasi file pertama tidak memuat kolom `PIC`
36. Klik header kolom Column Visibility (⋯)
37. Centang kembali kolom `PIC` pada Overlay Column Visibility
38. Klik icon Download
39. Klik `Download as CSV`
40. Buka isi file hasil unduhan kedua
41. Verifikasi file kedua memuat kolom `PIC`

### TC-GS-USER-868: Nilai kosong ditulis `-` di file export

42. Klik icon Download
43. Klik `Download as CSV`
44. Buka isi file hasil unduhan
45. Verifikasi sel Group pada baris bernilai Request Date `{rd-2}` dan Total Asset `1` (baris Q2a) ditulis `-`
46. Verifikasi sel PIC pada baris bernilai Request Date `{rd-2}` dan Total Asset `2` (baris Q2b) ditulis `-`

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE. Kelas harness binary buffer (prinsip 13f): isi berkas CSV dan XLSX; kegagalan ekspor sub-tab Pending Tasks tidak punya TC sumber.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (398, 864, 865, 866, 867, 868) dipertahankan.
- Langkah 1 sampai 4 memenuhi langkah awal "Klik Name `Ahmad Fauzi`, Tab `Responsibilities`, sub-tab `Pending Tasks`" dari seluruh TC sumber; layar itu dibuka sekali dan dipakai bersama. Langkah "Klik Download → `Download as CSV`" TC-GS-USER-398 dan "Klik icon Download, Klik `Download as CSV`" TC-GS-USER-864 menghasilkan dua unduhan terpisah karena Expected keduanya mengamati unduhan masing-masing.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (mencari user target di User List agar Name dapat diklik, bagian 8b butir 12), langkah 14, 23, 33, 40, 44 (membuka isi berkas unduhan), langkah 28 dan 37 (hide dan unhide `PIC` untuk TC-GS-USER-867), serta langkah 26 (menutup Search sebelum TC-GS-USER-867). Search bar TC-GS-USER-866 ditutup agar TC-GS-USER-867 dan 868 mengunduh seluruh data. `Verifikasi` tidak ada toast diletakkan segera sesudah klik pilihan format dan sebelum `Verifikasi` berkas (bagian 8b butir 11).
- Asersi tambahan (S-03, dengan alasan): langkah 29 memastikan kolom `PIC` benar-benar hidden sebelum unduhan (S-14); `Verifikasi` 9 baris hasil search sebelum unduhan pada TC-GS-USER-866 menjadi anchor positif sebelum `Verifikasi` file tidak memuat baris Group `{group-B}` (bagian 8b butir 2, S-11 dua nilai distinct pada kolom Group); `Verifikasi` file pertama memuat kolom `Group` menjadi anchor positif sebelum `Verifikasi` ketiadaan kolom `PIC`; jumlah `B0` + 22 baris pada TC-GS-USER-864 adalah konkretisasi "semua baris (tidak dibatasi halaman)" dari Population PT-22 (baris Pre-setup `B0` ikut terunduh).
- Pembagian TC lintas spec: TC-GS-USER-396, 397, dan 830 sampai 836 ada di spec 132; TC-GS-USER-837 sampai 846 ada di spec 133; TC-GS-USER-847 sampai 851 ada di spec 134; TC-GS-USER-852 sampai 854, 869, dan 870 ada di spec 135; TC-GS-USER-855 sampai 863 ada di spec 136. TC Download sub-tab Pending Approvals ada di spec 131.
- Spec melewati sekitar 35 langkah (46 langkah) karena enam TC Download berbagi satu layar, satu dataset (PT-22), dan satu kelas harness (binary buffer). Tiap blok TC mengunduh berkasnya sendiri dan berdiri sendiri; langkah "Klik icon Download, Klik `Download as CSV`, buka isi berkas" merupakan blok baca berpola yang berulang.
- Temuan untuk QA:
  - Sel PIC di tabel menampilkan `[First Name] [Last Initial]` (nilai tampil `{pic-A-tampil}`/`{pic-B-tampil}`). Format PIC di berkas unduhan tidak disebut TC; langkah 45 dan 46 mengenali baris Q2a/Q2b lewat Request Date `{rd-2}` dan Total Asset (`1`/`2`), bukan lewat PIC.
  - TC-GS-USER-398 dan 864: kedua TC memverifikasi unduhan CSV seluruh data tanpa toast sukses dengan nama file yang sama; TC-GS-USER-398 tidak menyebut isi berkas.
  - TC-GS-USER-865: Expected hanya nama file `.xlsx`; TC tidak menyebut isi berkas XLSX, sehingga spec tidak mengasersi isi.
  - TC-GS-USER-866 dan 867: keyword (`{kw-group}`) dan kolom yang di-hide (`PIC`) tidak konkret di TC; spec memakai nilai dari Population PT-22. TC tidak menyebut cara menangkap berkas unduhan dan membaca isinya; kemampuan itu disediakan tim FE (Prerequisites).
  - TC-GS-USER-868: "Sel kosong" tidak menyebut kolom; spec memakai sel Group dan PIC yang kosong (PRD `user.md` §4.1.3 menampilkan `—` pada tabel untuk Group dan PIC kosong) pada baris seed Q2a dan Q2b.
  - Seeding task pending FAMS tidak punya mekanisme di TC, PRD, atau LLD; disediakan tim FE/BE. Nama key preferensi kolom di browser dan cara menghapusnya tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
