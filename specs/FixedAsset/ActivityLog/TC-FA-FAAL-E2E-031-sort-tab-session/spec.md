---
id: TC-FA-FAAL-E2E-031-sort-tab-session
title: "Sort Tab Session: Date, User, IP Address, Activity, dan Status"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-101
  - TC-FA-FAAL-102
  - TC-FA-FAAL-104
  - TC-FA-FAAL-105
coverage:
  web: automated
---

# Sort Tab Session: Date, User, IP Address, Activity, dan Status

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Admin Alpha, Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Reports & Logs > Activity Log, Tab Session). Tidak ada ganti akun di tengah spec.
- Data Pre-setup #11 (Tab Session SS-01 sampai SS-11), hanya dibaca dan tidak diubah; waktu Asia/Jakarta, Rows per page awal 10 (SS-05 berada di halaman 2 menurut TC-FA-FAAL-103). Nilai yang diurutkan:

  | Baris | Date | User | IP Address |
  |---|---|---|---|
  | SS-01 | 14/07/26 08:05 | John Doe | `192.168.1.10` |
  | SS-02 | 14/07/26 09:30 | John Doe | `192.168.1.10` |
  | SS-03 | 14/07/26 10:00 | Siti Nurbaya | `10.0.0.5` |
  | SS-04 | 14/07/26 14:00 | Mike Tan | `172.16.0.8` |
  | SS-05 | 15/07/26 08:00 | Jane Smith | `—` |
  | SS-06 | 15/07/26 09:00 | Budi Santoso | `9.0.0.1` |
  | SS-07 | 15/07/26 10:00 | Dewi Lestari | `10.0.0.2` |
  | SS-08 | 15/07/26 11:00 | Hendra Pratama (#1) | `192.168.1.20` |
  | SS-09 | 15/07/26 12:00 | Hendra Pratama (#2) | `192.168.1.21` |
  | SS-10 | 16/07/26 08:00 | John Dalton | `192.168.2.10` |
  | SS-11 | 16/07/26 09:00 | John Davis | `192.168.2.11` |

  Kolom Activity bernilai `Session` dan kolom Status bernilai `—` pada semua baris. Identitas baris dirujuk lewat `Fixture.activity-log.<kunci>` (fixture `fixtures/activity-log.json` disediakan tim FE; nama kunci ditetapkan tim FE).
- Kolom untuk langkah berulang (langkah 25 sampai 33):

  | Kolom |
  |---|
  | `Activity` |
  | `Status` |

- Jendela Seed Tab Session: Filter Date `14/07/26` sampai `16/07/26` (memuat SS-01 sampai SS-11), diterapkan di langkah 1 (precondition TC-FA-FAAL-101, 102, 104, 105) sehingga baris yang diasersi hanya baris seed #11 (SS-11 di baris pertama default, SS-05 di akhir); total entri tidak diasersi.
- State yang diubah spec: Filter Date, Sort Tab Session, dan halaman aktif tabel; Sort dan halaman dikembalikan oleh langkah penghubung, Filter Date di-reset pembukaan layar hook `beforeEach` suite sebelum spec berikutnya.
- Flag Guided Tooltip halaman Activity Log di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps
1. Klik icon Filter, pilih tanggal mulai `14/07/26` dan tanggal akhir `16/07/26` pada field Date, klik `[Apply]`

### TC-FA-FAAL-101: Sort kolom Date Tab Session, siklus tiga tahap

2. Klik ikon sort header kolom Date sekali (Ascending)
3. Verifikasi Klik 1 (Oldest First): SS-01 di baris pertama
4. Klik ikon sort header kolom Date kedua kali (Descending)
5. Verifikasi Klik 2 (Newest First): SS-11 di baris pertama
6. Klik ikon sort header kolom Date ketiga kali
7. Verifikasi indikator sort hilang
8. Verifikasi urutan kembali default Date Newest First (SS-11, SS-10)

### TC-FA-FAAL-102: Sort kolom User Tab Session berdasarkan nama lengkap

9. Klik ikon sort header kolom User sekali (Ascending)
10. Verifikasi Klik 1 (A-Z menurut nama lengkap): lima baris pertama SS-06 (Budi), SS-07 (Dewi), SS-09 lalu SS-08 (Hendra Pratama), SS-05 (Jane)
11. Klik ikon sort header kolom User kedua kali (Descending)
12. Verifikasi Klik 2 (Z-A): lima baris pertama SS-03 (Siti), SS-04 (Mike), SS-02 lalu SS-01 (John Doe), SS-11 (John Davis)
13. Klik ikon sort header kolom User ketiga kali
14. Verifikasi Klik 3: kembali urutan default Date Newest First

### TC-FA-FAAL-104: Sort kolom IP Address Tab Session sebagai teks

15. Klik ikon sort header kolom IP Address sekali (Ascending)
16. Verifikasi Klik 1 (teks A-Z): SS-07 (`10.0.0.2`), SS-03 (`10.0.0.5`), SS-04 (`172.16.0.8`) di atas
17. Verifikasi `9.0.0.1` (SS-06) tampil setelah `192.168.2.11` (SS-11)
18. Pindah ke halaman terakhir (halaman 2)
19. Verifikasi SS-05 (`—`) di akhir
20. Pindah ke halaman 1
21. Klik ikon sort header kolom IP Address kedua kali (Descending)
22. Verifikasi Klik 2: SS-05 (`—`) di baris pertama dan SS-06 (`9.0.0.1`) di baris kedua
23. Klik ikon sort header kolom IP Address ketiga kali
24. Verifikasi Klik 3: kembali default

### TC-FA-FAAL-105: Sort kolom Activity dan Status Tab Session

Untuk setiap baris tabel Prerequisites "Kolom untuk langkah berulang" (langkah 25 sampai 33):

25. Verifikasi ikon sort ada pada header kolom
26. Klik ikon sort header kolom sekali
27. Verifikasi Klik 1 menampilkan indikator panah
28. Verifikasi urutan baris tidak berubah dari default (SS-11 di baris pertama)
29. Klik ikon sort header kolom kedua kali
30. Verifikasi Klik 2 menampilkan indikator panah
31. Verifikasi urutan baris tidak berubah dari default (SS-11 di baris pertama)
32. Klik ikon sort header kolom ketiga kali
33. Verifikasi indikator sort hilang

## Notes

- Alasan di atas 35 langkah dengan ekspansi (33 langkah nominal; langkah 25 sampai 33 diulang untuk dua kolom sehingga 42 langkah): keempat TC satu halaman, satu dataset #11, satu kelas fungsional (Sort), dan tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah berulang mengikuti idiom "Untuk setiap baris tabel" (butir 8b.7); `Verifikasi` tetap satu per klausa.
- Pembagian TC lintas spec: TC-FA-FAAL-103 (sort kolom teks Employee ID, Position, Division, Note, dan Device/Browser) ada di spec 070.
- Langkah penghubung (S-03): langkah 18 dan 20 (pindah halaman agar asersi "di akhir" bermakna, S-14). TC-FA-FAAL-104 tidak menyebut pindah halaman; langkah 20 mengembalikan tabel ke halaman 1 sebelum Klik 2.
- Langkah 1 (S-03): menerapkan Filter Date Jendela Seed Tab Session sesuai precondition d TC-FA-FAAL-101, 102, 104, dan 105.
- Langkah 3, 5, 8, 10, 12, 16, 17, 19, 22, dan 24 menyebut daftar baris seed sekaligus sebagai pembanding positif asersi urutan; setiap asersi sort memakai kolom dengan sedikitnya dua nilai berbeda (S-11), kecuali Activity dan Status yang memang bernilai seragam sehingga yang diasersi adalah indikator dan urutan yang tidak berubah (TC-FA-FAAL-105).
- Temuan untuk QA:
  - TC-FA-FAAL-101, 102, 104, 105 memberi precondition Filter Date Jendela Seed Tab Session (14/07/26 sampai 16/07/26) agar asersi posisi baris tidak bergantung pada baris log lain; spec menerapkannya di langkah 1 dan mengikuti TC.
  - TC-FA-FAAL-102 Klik 1 menulis SS-09 lalu SS-08 (nama sama, Date terbaru di atas) dan Klik 2 menulis SS-02 lalu SS-01, tetapi tidak menyebut aturan tie-break pada Expected; spec menulis urutan seperti TC.
  - TC-FA-FAAL-105 tidak menyebut apa yang diamati pada "ikon sort ada" selain keberadaannya; spec menulisnya sebagai `Verifikasi` keberadaan ikon pada header (langkah 25).
