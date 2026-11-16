---
id: TC-FA-FACO-E2E-076-tabel-last-used-dep-export-journal
title: "Search, Sort, dan Filter atas kolom Last Used in Journal"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1.1#r6", "§4.1.1#b1", "EB-FLT-5@tabel-account-list", EB-SRT-2]
smoke: [EB-SRT-2]
dependsOn: ["Export Journal: export jurnal yang mengisi Last Used in Journal"]
trace:
  "§4.1.1#r6": [4, 8, 12, 17]
  "§4.1.1#b1": [18, 19, 20, 21, 25, 26, 27]
  "EB-FLT-5@tabel-account-list": [22, 30]
  EB-SRT-2: [9, 11]
anchor: [2]
coverage:
  web: automated
---

# Search, Sort, dan Filter atas kolom Last Used in Journal

## Prerequisites
- Aktor: Admin dengan role Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - M0 adalah bulan saat spec dijalankan. Periode pada Last Used in Journal tampil dengan format `MMM YYYY`, dan semua periode di bawah ini sudah lewat.
  - DU-076-1: Account Code `LUS1-{runId}`, Account Name `Building Cost {runId}`, Account Function `Asset Cost`, Status `Active`, Used By `0`, Last Used in Journal `M0 − 7 bulan`, ada di entitas aktor.
  - DU-076-2: Account Code `LUS2-{runId}`, Account Name `Vehicle Cost {runId}`, Account Function `Asset Cost`, Status `Active`, Used By `0`, Last Used in Journal `M0 − 4 bulan`, ada di entitas aktor.
  - DU-076-3: Account Code `LUS3-{runId}`, Account Name `Machinery Cost {runId}`, Account Function `Asset Cost`, Status `Active`, Used By `0`, Last Used in Journal `M0 − 5 bulan`, ada di entitas aktor.
  - DU-076-4: Account Code `LUS4-{runId}`, Account Name `Furniture Cost {runId}`, Account Function `Asset Cost`, Status `Active`, Used By `0`, Last Used in Journal `M0 − 6 bulan`, ada di entitas aktor.
  - DU-076-5: Account Code `LUS5-{runId}`, Account Name `Equipment Cost {runId}`, Account Function `Asset Cost`, Status `Active`, Used By `0`, Last Used in Journal `M0 − 3 bulan`, ada di entitas aktor.
  - DU-076-6: Account Code `LUS6-{runId}`, Account Name `Software Cost {runId}`, Account Function `Asset Cost`, Status `Active`, Used By `0`, Last Used in Journal `—` (belum pernah diekspor), ada di entitas aktor.
  - Keenam akun DU-076-1 sampai DU-076-6 adalah seluruh akun milik spec ini.

## Test Steps

### Search tidak mencocokkan kolom Last Used in Journal
1. Ketik Search `{runId}`, tekan Enter
2. Verifikasi baris `LUS1-{runId}`, `LUS2-{runId}`, `LUS3-{runId}`, `LUS4-{runId}`, `LUS5-{runId}`, dan `LUS6-{runId}` tampil
3. Ganti isi kotak search dengan teks periode baris `LUS3-{runId}` yang tampil dengan format `MMM YYYY` (periode `M0 − 5 bulan`), tekan Enter
4. Verifikasi baris `LUS3-{runId}` tidak tampil
5. Klik `(←)` pada kotak Search

### Sort Last Used in Journal menaik lalu menurun
6. Ketik Search `{runId}`, tekan Enter
7. Klik header kolom `Last Used in Journal`
8. Verifikasi urutan baris dari atas ke bawah `LUS1-{runId}`, `LUS4-{runId}`, `LUS3-{runId}`, `LUS2-{runId}`, `LUS5-{runId}` menurut periode dari terlama ke terbaru
9. Verifikasi baris `LUS6-{runId}` yang bernilai `—` berada di akhir daftar saat urutan menaik
10. Klik header kolom `Last Used in Journal`
11. Verifikasi baris `LUS6-{runId}` yang bernilai `—` berada di awal daftar saat urutan menurun
12. Verifikasi urutan baris sesudah `LUS6-{runId}` adalah `LUS5-{runId}`, `LUS2-{runId}`, `LUS3-{runId}`, `LUS4-{runId}`, `LUS1-{runId}` menurut periode dari terbaru ke terlama
13. Klik header kolom `Last Used in Journal`

### Filter rentang bulan bersifat inklusif di kedua batas
14. Klik ikon `Filter` di toolbar
15. Pilih rentang filter `Last Used in Journal` dari periode `M0 − 6 bulan` sampai periode `M0 − 4 bulan`
16. Klik `[Apply]`
17. Verifikasi baris `LUS3-{runId}` tampil
18. Verifikasi baris `LUS4-{runId}` tampil, yaitu periodenya tepat di bulan awal rentang
19. Verifikasi baris `LUS2-{runId}` tampil, yaitu periodenya tepat di bulan akhir rentang
20. Verifikasi baris `LUS1-{runId}` tidak tampil, yaitu periodenya satu bulan sebelum bulan awal rentang
21. Verifikasi baris `LUS5-{runId}` tidak tampil, yaitu periodenya satu bulan sesudah bulan akhir rentang
22. Verifikasi baris `LUS6-{runId}` tidak tampil, yaitu nilai kosong tersaring keluar oleh rentang

### Filter rentang satu bulan hanya memuat bulan itu
23. Pilih rentang filter `Last Used in Journal` dari periode `M0 − 5 bulan` sampai periode `M0 − 5 bulan`
24. Klik `[Apply]`
25. Verifikasi baris `LUS3-{runId}` tampil
26. Verifikasi baris `LUS4-{runId}` tidak tampil
27. Verifikasi baris `LUS2-{runId}` tidak tampil

### Melepas filter menampilkan kembali baris yang nilainya kosong
28. Klik `[Clear Field]`
29. Klik `[Apply]`
30. Verifikasi baris `LUS6-{runId}` tampil kembali
