---
id: TC-FA-TDC-E2E-096-log-job-j-02-j-03-modified-by-system-dan-job-dua-kali
title: "Log Job J-02 (L-08) dan J-03 (L-10): Modified By System di Changelog dan Activity Log, Tidak di System Log, serta J-02 Dua Kali Tidak Menulis Log Ganda"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-690
  - TC-FA-TDC-691
  - TC-FA-TDC-692
  - TC-FA-TDC-693
  - TC-FA-TDC-913
coverage:
  web: automated
---

# Log Job J-02 (L-08) dan J-03 (L-10): Modified By System di Changelog dan Activity Log, Tidak di System Log, serta J-02 Dua Kali Tidak Menulis Log Ganda

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control "Rina Puspita" (tampil sebagai "Rina P" pada Modified By). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- Time Zone entitas Asia/Jakarta (UTC+07:00). Job J-02 dijalankan oleh scheduler harian; tick scheduler J-02 dijalankan eksplisit di langkah (kemampuan penahanan dan penjalanan job disediakan tim FE/BE, `suite.md`). Posting penyusutan fiskal (job J-03; Depreciation Run belum tersedia) dipicu lewat fixture BE (disediakan tim FE/BE; mekanismenya tidak disebut TC, S-13).
- Kendali jam sistem (`suite.md`): jam server dan jam browser diatur bersama pada waktu absolut `31 Des 2026 17:00:00 UTC` (1 Jan 2027 00:00:00 WIB) pada langkah 2, 15, dan 39. Jam dipulihkan secara eksplisit pada langkah 8, 20, dan 49 (sebelum Activity Log atau System Log dibuka dan sebelum baseline System Log TC-692) dengan hook `after` sebagai cadangan (S-09). Entri log dibaca lewat Search atas Class Code (bukan posisi teratas) karena log yang dibuat saat jam digeser bercap waktu di masa depan (S-12).
- Kemampuan teknis: membaca jumlah entri System Log pada Detail User sebelum dan sesudah uji (kemampuan baca disediakan tim FE/BE; langkah 1 dan 21 membacanya lewat UI); pengaturan Search pada Popup Changelog dan Activity Log untuk menemukan entri berdasarkan Class Code.
- Nilai data mengacu ke `Fixture.fixedAssetTaxDepreciationClass` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Data Dinamis (di-seed di hook `before` lewat API, dihapus di hook `after`; Class Code bersuffix unik sehingga entri Field "Current Version" dan "Last Posted Tax Year" untuk class itu berbaseline nol di Changelog dan Activity Log, S-12):

| TC | Class (Class Code bersuffix) | Isi |
|---|---|---|
| TC-690 | `KHS-LG1-{runId}-096` (Class Name `Kelompok log uji`) | Current Effective From Jan 2026; Scheduled Effective From Jan 2027 |
| TC-691 | `KHS-LG2-{runId}-096` | Current tanpa Effective From; Scheduled Effective From Jan 2027 |
| TC-692 | `KHS-LG3-{runId}-096` | Last Posted Tax Year `2025` |
| TC-693 | `KHS-LG4-{runId}-096` | Last Posted Tax Year kosong |
| TC-913 | `KHS-J2-{runId}-096` | Active, Used By 0; Current tanpa Effective From (Useful Life 8, Straight Line dan Declining Balance); Scheduled Effective From Jan 2027 (Useful Life 10, Straight Line dan Declining Balance) |

- Baris `KHS-*` berada di halaman pertama tabel (urutan default Class Code A-Z, `KHS-*` sebelum `LAND`) sehingga dibaca tanpa Search.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-690: Log L-08, versi Scheduled menjadi Current oleh J-02

1. Buka Detail User Rina Puspita > Tab System Log dan catat jumlah entri (baseline)
2. Atur jam server dan jam browser ke 31 Des 2026 17:00:00 UTC (1 Jan 2027 00:00 WIB) lalu jalankan tick scheduler J-02
3. Buka Settings > Accounting > Tax Depreciation Class
4. Klik ikon Changelog di toolbar
5. Ketik Search `KHS-LG1-{runId}-096`, tekan Enter
6. Verifikasi Changelog, Dicatat: satu baris: Action "Edit" | Class Code "KHS-LG1-{runId}-096" | Field "Current Version" | Old Value "Jan 2026" | New Value "Jan 2027" | Modified By "System"
7. Tutup Popup Changelog
8. Pulihkan jam server dan jam browser ke waktu nyata
9. Buka Reports & Logs > Activity Log, tab `User Action`
10. Ketik Search `KHS-LG1-{runId}-096`, tekan Enter
11. Verifikasi Activity Log FAMS, Dicatat: satu baris: Action "Edit" | Object "Tax Depreciation Class" | Name "KHS-LG1-{runId}-096" | Field "Current Version" | Old Value "Jan 2026" | New Value "Jan 2027" | Modified By "System"
12. Buka Detail User Rina Puspita > Tab System Log
13. Verifikasi System Log Rina Puspita, Tidak dicatat: jumlah entri sama dengan baseline langkah 1

### TC-FA-TDC-691: Log L-08, Old Value bernilai "—" bila versi Current sebelumnya adalah versi pertama

14. Buka Settings > Accounting > Tax Depreciation Class
15. Atur jam server dan jam browser ke 31 Des 2026 17:00:00 UTC lalu jalankan tick scheduler J-02
16. Klik ikon Changelog di toolbar
17. Ketik Search `KHS-LG2-{runId}-096`, tekan Enter
18. Verifikasi Changelog, Dicatat: baris Action "Edit" | Class Code "KHS-LG2-{runId}-096" | Field "Current Version" | Old Value "—" | New Value "Jan 2027" | Modified By "System"
19. Tutup Popup Changelog
20. Pulihkan jam server dan jam browser ke waktu nyata

### TC-FA-TDC-692: Log L-10, posting penyusutan fiskal mencatat Last Posted Tax Year

21. Buka Detail User Rina Puspita > Tab System Log dan catat jumlah entri (baseline)
22. Buka Settings > Accounting > Tax Depreciation Class
23. Picu posting penyusutan fiskal tahun pajak 2026 untuk `KHS-LG3-{runId}-096` lewat fixture BE (J-03)
24. Klik ikon Changelog di toolbar
25. Ketik Search `KHS-LG3-{runId}-096`, tekan Enter
26. Verifikasi Changelog, Dicatat: satu baris: Action "Edit" | Class Code "KHS-LG3-{runId}-096" | Field "Last Posted Tax Year" | Old Value "2025" | New Value "2026" | Modified By "System"
27. Tutup Popup Changelog
28. Buka Reports & Logs > Activity Log, tab `User Action`
29. Ketik Search `KHS-LG3-{runId}-096`, tekan Enter
30. Verifikasi Activity Log FAMS, Dicatat: satu baris dengan Object "Tax Depreciation Class", Name "KHS-LG3-{runId}-096", Field "Last Posted Tax Year", Old Value "2025", New Value "2026", Modified By "System"
31. Buka Detail User Rina Puspita > Tab System Log
32. Verifikasi System Log Rina Puspita, Tidak dicatat: jumlah entri sama dengan baseline langkah 21

### TC-FA-TDC-693: Log L-10, Old Value bernilai "—" pada posting pertama

33. Buka Settings > Accounting > Tax Depreciation Class
34. Picu posting penyusutan fiskal tahun pajak 2026 untuk `KHS-LG4-{runId}-096` lewat fixture BE (J-03)
35. Klik ikon Changelog di toolbar
36. Ketik Search `KHS-LG4-{runId}-096`, tekan Enter
37. Verifikasi Changelog, Dicatat: baris Field "Last Posted Tax Year" | Old Value "—" | New Value "2026" | Modified By "System"
38. Tutup Popup Changelog

### TC-FA-TDC-913: J-02 dijalankan dua kali pada hari Effective From tidak menerapkan ulang versi dan tidak menulis log ganda

39. Atur jam server dan jam browser ke 31 Des 2026 17:00:00 UTC (1 Jan 2027 00:00 WIB) lalu jalankan tick scheduler J-02
40. Verifikasi tidak ada toast pada tick pertama
41. Jalankan tick scheduler J-02 sekali lagi tanpa mengubah jam server
42. Verifikasi tidak ada toast pada tick kedua
43. Muat ulang halaman; baca baris `KHS-J2-{runId}-096`
44. Verifikasi baris `KHS-J2-{runId}-096`: Effective From "Jan 2027", Useful Life "10"
45. Klik ikon Changelog di toolbar
46. Ketik Search `KHS-J2-{runId}-096`, tekan Enter
47. Verifikasi Changelog memuat tepat satu baris: Action "Edit" | Class Code "KHS-J2-{runId}-096" | Field "Current Version" | Old Value "—" | New Value "Jan 2027" | Modified By "System"; tidak ada baris ganda
48. Tutup Popup Changelog
49. Pulihkan jam server dan jam browser ke waktu nyata

## Notes

- Alasan spec di atas sekitar 35 langkah: kelima TC satu kelas harness (d: job J-02 dan J-03 sebagai objek uji) dan berdiri sendiri (kegagalan satu TC tidak membuat TC lain kehilangan makna); sekitar separuh langkah adalah blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom log) yang tidak dihitung menurut prinsip 13 bagian 3.
- Jam diatur absolut pada tiap pemicu J-02 (langkah 2, 15, 39); jam yang sama dipakai berulang karena tiap TC memakai class berbeda yang berstatus Scheduled. Jam dipulihkan sebelum Activity Log dan System Log dibuka (langkah 8, 20, 49): baseline System Log (langkah 1 dan 21) dicatat pada jam nyata dan dibandingkan terhadap hasil baca pada jam nyata (langkah 13 dan 32), sehingga cap waktu masa depan dari entri yang dibuat saat jam digeser tidak memengaruhi pembacaan jumlah entri (S-09, S-12). Langkah 8, 20, dan 49 adalah langkah penghubung pemulihan state (S-03).
- Entri Changelog dan Activity Log dicari lewat Search atas Class Code bersuffix unik (baseline nol untuk Field "Current Version" dan "Last Posted Tax Year", S-12); dicatat sebagai langkah penghubung (R-16): langkah 5, 10, 17, 25, 29, 36, 46. Jam server yang digeser membuat entri baru bercap waktu di masa depan; karena itu entri dibaca lewat Search atas Class Code, bukan posisi teratas.
- Langkah penghubung (S-03): langkah 3, 14, 22, 33 (kembali ke Settings > Accounting > Tax Depreciation Class sesudah berpindah modul, S-14), langkah 7, 19, 27, 38, 48 (menutup Popup Changelog), dan langkah 43 (muat ulang dan baca baris).
- Langkah 40 dan 42 (absence toast, 8b.11) berpegang pada tampilan halaman yang termuat (tabel class tampil) sebagai anchor; langkah 44 menegaskan hasil tick di tabel.
- Asersi "tepat satu baris" (langkah 6, 11, 26, 30, 47) adalah asersi jumlah dengan baseline nol, bukan absence (kelas g); asersi "tidak dicatat" pada System Log (langkah 13 dan 32) memakai selisih jumlah entri terhadap baseline (S-12), bukan absence, karena Expected TC menyatakannya sebagai jumlah sama dengan sebelum uji. Anchor positifnya adalah entri Changelog dan Activity Log yang baru diasersi pada pemicu yang sama (langkah 6 dan 11, 26 dan 30).
- Post Condition TC-913 ("versi Jan 2027 tetap Current; tidak ada versi lain berubah") tidak punya langkah observasi di TC; "versi Jan 2027 Current" diamati sebagian lewat langkah 44.
- Temuan untuk QA:
  - TC-690 sampai 693 memakai satu Class Code `KHS-LG` untuk lima keadaan berbeda; spec memakai `KHS-LG1` sampai `KHS-LG4` bersuffix `-{runId}-096` karena tiap TC mengonsumsi keadaan class (S-12).
  - TC-690/692 tidak menyebut cara menemukan baris di Popup Changelog dan Activity Log, serta filter produk FAMS; spec memakai Search atas Class Code.
  - TC-690 dan 692 menyebut System Log Rina Puspita tanpa email; user pada surface admin dan log seharusnya diidentifikasi lewat email bersuffix (R-06); email akun Total Control tidak tertulis di TC.
  - TC-913 memakai `KHS-J2` tanpa suffix (S-12).
