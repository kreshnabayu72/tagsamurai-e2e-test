---
id: TC-FA-FAAL-E2E-070-sort-tab-session-kolom-teks
title: "Sort Tab Session: Kolom Teks Employee ID, Position, Division, Note, dan Device/Browser"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-103
coverage:
  web: automated
---

# Sort Tab Session: Kolom Teks Employee ID, Position, Division, Note, dan Device/Browser

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Admin Alpha, Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Reports & Logs > Activity Log, Tab Session). Tidak ada ganti akun di tengah spec.
- Data Pre-setup #11 (Tab Session SS-01 sampai SS-11), hanya dibaca dan tidak diubah; Rows per page awal 10 sehingga SS-05 berada di halaman 2 pada urutan default (menurut TC-FA-FAAL-103). Nilai yang diurutkan (`—` berarti nilai kosong):

  | Baris | Employee ID | Position | Division | Note | Device/Browser |
  |---|---|---|---|---|---|
  | SS-01 | EMP001 | Staff | Marketing | Session started | Chrome on Windows |
  | SS-02 | EMP001 | Staff | Marketing | Session ended | Chrome on Windows |
  | SS-03 | EMP002 | Manager | Finance | Concurrent limit reached | Safari on iOS |
  | SS-04 | EMP003 | Staff | Operations | Logged out by admin | Chrome on Android |
  | SS-05 | `—` | `—` | Finance | Session started | TAG Samurai App on Android |
  | SS-06 | EMP004 | Supervisor | Operations | Session started | `—` |
  | SS-07 | EMP005 | Staff | Marketing | Session started | `—` |
  | SS-08 | EMP006 | Staff | Marketing | Session started | Firefox on Linux |
  | SS-09 | EMP007 | Manager | Finance | Session started | Edge on Windows |
  | SS-10 | EMP008 | Staff | Operations | Session started | Chrome on Windows |
  | SS-11 | EMP009 | Supervisor | Finance | Session ended | Safari on macOS |

  Identitas baris dirujuk lewat `Fixture.activity-log.<kunci>` (fixture `fixtures/activity-log.json` disediakan tim FE; nama kunci ditetapkan tim FE).
- Posisi dan urutan baris pada asersi bergantung pada Tab Session client uji yang hanya memuat baris seed #11 dalam Filter Date Jendela Seed (14/07/26 sampai 16/07/26) yang diterapkan langkah 1 sampai 3. Total entri tidak diasersi sebagai angka absolut.
- State yang diubah spec: Sort Tab Session dan halaman aktif tabel; keduanya dikembalikan oleh langkah penghubung dan di-reset pembukaan layar hook `beforeEach` suite sebelum spec berikutnya.
- Flag Guided Tooltip halaman Activity Log di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik icon Filter
2. Pilih tanggal mulai `14/07/26` dan tanggal akhir `16/07/26` pada field Date
3. Klik `[Apply]`

### Employee ID

4. Klik ikon sort header kolom Employee ID sekali (Ascending)
5. Verifikasi Klik 1: SS-02 lalu SS-01 (EMP001) di atas
6. Pindah ke halaman terakhir (halaman 2)
7. Verifikasi SS-05 (`—`) di halaman 2 baris terakhir
8. Pindah ke halaman 1
9. Klik ikon sort header kolom Employee ID kedua kali (Descending)
10. Verifikasi Klik 2: SS-05 (`—`) di baris pertama diikuti SS-11 (EMP009)
11. Klik ikon sort header kolom Employee ID ketiga kali
12. Verifikasi Klik 3 kembali default

### Position

13. Klik ikon sort header kolom Position sekali (Ascending)
14. Verifikasi Klik 1: SS-09 lalu SS-03 (Manager) di atas
15. Pindah ke halaman terakhir (halaman 2)
16. Verifikasi SS-05 (`—`) di akhir
17. Pindah ke halaman 1
18. Klik ikon sort header kolom Position kedua kali (Descending)
19. Verifikasi Klik 2: SS-05 (`—`) di baris pertama
20. Klik ikon sort header kolom Position ketiga kali
21. Verifikasi Klik 3 kembali default

### Division

22. Klik ikon sort header kolom Division sekali (Ascending)
23. Verifikasi Klik 1: SS-11, SS-09, SS-05, SS-03 (Finance) di empat baris pertama
24. Klik ikon sort header kolom Division kedua kali (Descending)
25. Verifikasi Klik 2: SS-10 (Operations) di baris pertama
26. Klik ikon sort header kolom Division ketiga kali
27. Verifikasi Klik 3 kembali default

### Note

28. Klik ikon sort header kolom Note sekali (Ascending)
29. Verifikasi Klik 1: SS-03 (Concurrent limit reached), SS-04 (Logged out by admin), SS-11, SS-02 (Session ended)
30. Klik ikon sort header kolom Note kedua kali (Descending)
31. Verifikasi Klik 2: SS-10 (Session started) di baris pertama
32. Klik ikon sort header kolom Note ketiga kali
33. Verifikasi Klik 3 kembali default

### Device/Browser

34. Klik ikon sort header kolom Device/Browser sekali (Ascending)
35. Verifikasi Klik 1: SS-04, SS-10, SS-02, SS-01, SS-09 di lima baris pertama
36. Pindah ke halaman terakhir (halaman 2)
37. Verifikasi SS-06 serta SS-07 (`—`) di akhir
38. Pindah ke halaman 1
39. Klik ikon sort header kolom Device/Browser kedua kali (Descending)
40. Verifikasi Klik 2: SS-07 lalu SS-06 (`—`) di dua baris pertama
41. Klik ikon sort header kolom Device/Browser ketiga kali
42. Verifikasi Klik 3 kembali default

## Notes

- Alasan di atas 35 langkah (42 langkah): spec memuat satu TC (TC-FA-FAAL-103) dengan lima kolom pada satu halaman, satu dataset #11, dan satu kelas fungsional (Sort); satu TC tetap satu spec dan tiap blok kolom berdiri sendiri sehingga kegagalan satu kolom tidak membuat kolom lain kehilangan makna. Langkah tiap kolom ditulis per blok karena Expected tiap kolom berbeda (ada atau tidaknya asersi akhir daftar) dan loop akan membutuhkan langkah bersyarat.
- Pembagian TC lintas spec: TC-FA-FAAL-101, 102, 104, 105 (sort Date, User, IP Address, Activity, Status) ada di spec 031.
- Langkah penghubung (S-03): langkah 1 sampai 3 (menerapkan Filter Date Jendela Seed Tab Session sesuai precondition d TC-FA-FAAL-103), langkah 6, 8, 15, 17, 36, 38 (pindah halaman agar asersi "di akhir" bermakna, S-14; TC-FA-FAAL-103 menyebut "halaman 2" pada Employee ID tetapi tidak menyebut langkah pindah halaman, dan langkah kembali ke halaman 1 menjaga Klik 2 diamati dari halaman pertama).
- Langkah 5, 7, 10, 14, 16, 19, 23, 25, 29, 31, 35, 37, dan 40 menyebut daftar baris seed sekaligus sebagai pembanding positif asersi urutan; tiap kolom diurutkan memiliki sedikitnya dua nilai berbeda (S-11).
- Temuan untuk QA:
  - TC-FA-FAAL-103 tidak menyebut Rows per page awal; spec memakai 10 berdasarkan rujukan "halaman 2" pada Employee ID (SS-05 sebagai baris terakhir).
  - Expected Division dan Note pada TC-FA-FAAL-103 tidak menyebut baris di akhir daftar; spec hanya mengasersi baris teratas sesuai TC.
