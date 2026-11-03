---
id: TC-FA-FAAL-E2E-005-sel-tab-session
title: "Sel Tab Session: User, Device/Browser, Employee ID, Position, IP, Division, Note, Activity, Status"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-12
  - TC-FA-FAAL-13
  - TC-FA-FAAL-14
  - TC-FA-FAAL-15
  - TC-FA-FAAL-16
  - TC-FA-FAAL-17
  - TC-FA-FAAL-18
  - TC-FA-FAAL-19
coverage:
  web: automated
---

# Sel Tab Session: User, Device/Browser, Employee ID, Position, IP, Division, Note, Activity, Status

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Reports & Logs > Activity Log > Session.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Data: Data Log Tab Session SS-01 sampai SS-11 (Pre-setup #11), 11 baris, dipulihkan ke keadaan Pre-setup oleh fixture backend sebelum spec. Urutan default Date terbaru di atas dengan 10 baris per halaman: halaman 1 berisi SS-11 sampai SS-02, halaman 2 berisi SS-01. Nilai baris yang diasersi:
  | Baris | User | Employee ID | Position | Division | Note | IP Address | Device/Browser |
  |---|---|---|---|---|---|---|---|
  | SS-01 | John Doe | EMP001 | Staff | Marketing | Session started | 192.168.1.10 | Chrome on Windows |
  | SS-03 | Siti Nurbaya | EMP002 | Manager | Finance | Concurrent limit reached | 10.0.0.5 | Safari on iOS |
  | SS-04 | Mike Tan | EMP003 | Staff | Operations | Logged out by admin | 172.16.0.8 | Chrome on Android |
  | SS-05 | Jane Smith | tanpa | tanpa | Finance | Session started | kosong | TAG Samurai App on Android |
  | SS-06 | Budi Santoso | EMP004 | Supervisor | Operations | Session started | 9.0.0.1 | Browser terparse, OS tidak |
  | SS-07 | Dewi Lestari | EMP005 | Staff | Marketing | Session started | 10.0.0.2 | Browser dan OS tidak terparse |
  | SS-08 | Hendra Pratama #1 | EMP006 | Staff | Marketing | Session started | 192.168.1.20 | Firefox on Linux |
  | SS-09 | Hendra Pratama #2 | EMP007 | Manager | Finance | Session started | 192.168.1.21 | Edge on Windows |
  Kolom Activity `Session` dan Status `—` pada semua baris. Empat nilai kanonikal Note: `Session started`, `Session ended`, `Concurrent limit reached`, `Logged out by admin`.
- Flag Guided Tooltip: mengikuti butir "Flag Guided Tooltip" di `suite.md` (flag akun Total Control bernilai true lewat hook suite).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).

## Test Steps

### TC-FA-FAAL-12: Kolom User Tab Session tampil sebagai nama singkat dengan hover nama lengkap

1. Verifikasi kolom User baris SS-03 tampil `Siti N` sebagai plain text
2. Verifikasi kolom User baris SS-08 tampil `Hendra P` sebagai plain text
3. Arahkan kursor ke sel User baris SS-03
4. Verifikasi tooltip `Siti Nurbaya` tampil
5. Arahkan kursor ke sel User baris SS-08
6. Verifikasi tooltip `Hendra Pratama` tampil

### TC-FA-FAAL-13: Kolom Device/Browser Tab Session tampil sebagai Browser on OS bila keduanya terparse

7. Verifikasi kolom Device/Browser baris SS-03 tampil `Safari on iOS`
8. Verifikasi kolom Device/Browser baris SS-04 tampil `Chrome on Android`
9. Verifikasi kolom Device/Browser baris SS-08 tampil `Firefox on Linux`
10. Verifikasi kolom Device/Browser baris SS-09 tampil `Edge on Windows`
11. Klik `[Next →]`
12. Verifikasi kolom Device/Browser baris SS-01 tampil `Chrome on Windows`
13. Klik `[← Prev]`

### TC-FA-FAAL-14: Kolom Device/Browser untuk sesi aplikasi native Android

14. Verifikasi kolom Device/Browser baris SS-05 tampil `TAG Samurai App on Android`

### TC-FA-FAAL-15: Device/Browser tampil strip bila salah satu atau kedua bagian tidak terparse

15. Verifikasi kolom Device/Browser baris SS-06 tampil `—` pada seluruh sel (tidak tampil `Chrome on`)
16. Verifikasi kolom Device/Browser baris SS-07 tampil `—` pada seluruh sel

### TC-FA-FAAL-16: Employee ID dan Position kosong tampil strip

17. Verifikasi baris SS-05 tampil `—` pada Employee ID dan `—` pada Position
18. Klik `[Next →]`
19. Verifikasi baris SS-01 tampil `EMP001` pada Employee ID dan `Staff` pada Position
20. Klik `[← Prev]`

### TC-FA-FAAL-17: IP Address kosong tampil strip

21. Verifikasi kolom IP Address baris SS-05 tampil `—`
22. Klik `[Next →]`
23. Verifikasi kolom IP Address baris SS-01 tampil `192.168.1.10`
24. Klik `[← Prev]`

### TC-FA-FAAL-18: Division dan Note Tab Session tidak pernah kosong

25. Verifikasi tabel menampilkan sedikitnya satu baris pada halaman 1
26. Verifikasi kolom Division setiap baris pada halaman 1 terisi `Marketing`, `Finance`, atau `Operations` dan tidak ada sel Division bernilai `—`
27. Verifikasi kolom Note setiap baris pada halaman 1 terisi salah satu dari `Session started`, `Session ended`, `Concurrent limit reached`, atau `Logged out by admin` dan tidak ada sel Note bernilai `—`
28. Klik `[Next →]`
29. Verifikasi baris SS-01 tampil Division `Marketing` dan Note `Session started`, keduanya bukan `—`
30. Klik `[← Prev]`

### TC-FA-FAAL-19: Activity selalu Session dan Status selalu strip

31. Verifikasi kolom Activity baris SS-04, SS-03, dan SS-02 tampil `Session`
32. Verifikasi kolom Status baris SS-04, SS-03, dan SS-02 tampil `—`
33. Klik `[Next →]`
34. Verifikasi baris SS-01 tampil Activity `Session` dan Status `—`

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 13, 20, 24, dan 30 (`[← Prev]` mengembalikan halaman 1 sebelum TC berikutnya, S-09); langkah 25 (anchor baris pembanding untuk asersi universal pada langkah 26 dan 27, bagian 8b butir 2). Klik `[Next →]` ke halaman 2 (langkah 11, 18, 22, 28, 33) berasal dari langkah TC-FA-FAAL-13, 16, 17, 18, dan 19.
- Urutan `Verifikasi` TC-FA-FAAL-13 mengikuti langkah TC (baris halaman 1, lalu SS-01 di halaman 2); urutan huruf Expected TC (a. SS-01 lebih dulu) tidak dipertahankan, isinya tetap lengkap.
- Hover pada langkah 3 dan 5 diasersi segera sebelum elemen berikutnya disentuh (bagian 8b butir 5).
- Spec ini 34 langkah.
- Temuan untuk QA:
  - TC-FA-FAAL-18 butir b menyebut "empat nilai kanonikal" Note tanpa mendaftarnya; spec memakai empat nilai Note yang muncul di data Pre-setup #11.
  - TC-FA-FAAL-15 menyebut baris SS-06 "Browser terparse, OS tidak" tetapi tidak menyebut nilai Browser yang terparse; spec mengikuti Expected TC (`—` pada seluruh sel).
