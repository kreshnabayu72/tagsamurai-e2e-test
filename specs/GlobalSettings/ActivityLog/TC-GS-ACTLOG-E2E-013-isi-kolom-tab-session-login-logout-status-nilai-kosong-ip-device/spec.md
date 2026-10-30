---
id: TC-GS-ACTLOG-E2E-013-isi-kolom-tab-session-login-logout-status-nilai-kosong-ip-device
title: "Isi Kolom Tab Session: Login, Logout, Status, Nilai Kosong, IP, Device"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-41
  - TC-GS-ACTLOG-42
  - TC-GS-ACTLOG-43
  - TC-GS-ACTLOG-49
  - TC-GS-ACTLOG-50
  - TC-GS-ACTLOG-51
  - TC-GS-ACTLOG-52
  - TC-GS-ACTLOG-53
coverage:
  web: automated
---

# Isi Kolom Tab Session: Login, Logout, Status, Nilai Kosong, IP, Device

## Prerequisites

- Mode: FE+BE.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Akun aktor: Total Control Client A (Sari Dewi), `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > Activity Log > Session.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD_WRONG` (password salah untuk Login `Failed`), `ACTLOG_PASSWORD` (password uji yang dipasang ke user dinamis modul Activity Log). Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Dinamis (suffix per run dan nomor spec, bagian 5 konvensi), dibuat lewat API di hook `before` oleh akun aktor. Subjek diidentifikasi lewat nama bersuffix (nama tidak diasersi singkatannya di spec ini):
  - `John Doe {runId}-013`: Login `Success` (Note `Login with password`) dari IP `192.0.2.10` dengan Device `Chrome on Windows`, lalu Logout manual (Note `Logged out`).
  - `Budi Anwar {runId}-013` (Division `Finance {runId}-013`): Login `Failed` (Note `Incorrect password`) dari IP `198.51.100.24` dengan Device `Chrome on Windows`; Reset Password `Failed`, Change Password `Failed`, Logout, dan Session (`Session started`) dihasilkan oleh aksi nyata alur Auth, My Profile, dan buka card Global Settings.
  - `Siti Nurbaya {runId}-013` (tanpa Position, Division `Operations {runId}-013`): login di perangkat A (IP dan Device berbeda dari perangkat B; nilainya disediakan tim FE/BE), lalu login di perangkat B dari IP `2001:db8::1a` dengan Device `Safari on iOS` yang menggantikan sesi perangkat A (dua event: Login perangkat B dan Logout perangkat A dengan Note `Logged out (new device login)`). Baris Login perangkat A ikut tercatat; baris perangkat B dikenali lewat Device `Safari on iOS` dan IP `2001:db8::1a`.
  - `Tamu Operasional {runId}-013` (tanpa Employee ID dan tanpa Position, Division `Operations {runId}-013`): entri Reset Password `Failed` dengan Device / Browser tidak terparse (User-Agent tidak dikenali).
  - `Dina Seed {runId}-013`: entri Session dengan IP Address null (seed BE).
  - `Wayan Mobile {runId}-013`: Login dari aplikasi native dengan Device `TAG Samurai App on Android`.
  - Password semua user di atas `Spectra.env.ACTLOG_PASSWORD`.
- Kemampuan teknis (disediakan tim FE/BE): (a) alamat sumber request dan User-Agent Login dapat diatur per user (`192.0.2.10`, `198.51.100.24`, `2001:db8::1a`; `Chrome on Windows`, `Safari on iOS`, `TAG Samurai App on Android`, dan User-Agent tidak terparse); (b) seed BE entri Session dengan IP null (kondisi tidak dapat dibuat lewat UI); (c) alur Login, Logout, Reset Password, Change Password, dan buka card Global Settings dijalankan lewat API oleh user uji.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua user bersuffix `{runId}-013` dan Division `Finance {runId}-013` serta `Operations {runId}-013` bila masih ada.

## Test Steps

### TC-GS-ACTLOG-41: Baris Login Success dan Login Failed

1. Buka Global Settings > Activity Log > Session
2. Ketik Search `John Doe {runId}-013`, tekan Enter
3. Verifikasi baris Login milik `John Doe {runId}-013`: Activity `Login`, Status `Success`, Note `Login with password`, IP Address `192.0.2.10`, Device / Browser `Chrome on Windows`
4. Ganti isi kotak search dengan `Budi Anwar {runId}-013`, tekan Enter
5. Verifikasi baris Login milik `Budi Anwar {runId}-013`: Activity `Login`, Status `Failed`, Note `Incorrect password`, IP Address `198.51.100.24`, Device / Browser `Chrome on Windows`

### TC-GS-ACTLOG-42: Baris Logout manual dan Logout paksa akibat login di perangkat baru

6. Ganti isi kotak search dengan `John Doe {runId}-013`, tekan Enter
7. Verifikasi baris Logout milik `John Doe {runId}-013`: Activity `Logout`, Status `—`, Note `Logged out`
8. Ganti isi kotak search dengan `Siti Nurbaya {runId}-013`, tekan Enter
9. Verifikasi baris Login milik `Siti Nurbaya {runId}-013` dengan Device `Safari on iOS` (login perangkat B): Activity `Login`, Status `Success`
10. Verifikasi baris Logout milik `Siti Nurbaya {runId}-013`: Activity `Logout`, Status `—`, Note `Logged out (new device login)`

### TC-GS-ACTLOG-43: Kolom Status per Activity

11. Ganti isi kotak search dengan `Budi Anwar {runId}-013`, tekan Enter
12. Verifikasi baris `Login` milik `Budi Anwar {runId}-013`: Status `Failed`
13. Verifikasi baris `Reset Password`: Status `Failed`
14. Verifikasi baris `Change Password`: Status `Failed`
15. Verifikasi baris `Logout`: Status `—`
16. Verifikasi baris `Session`: Status `—`

### TC-GS-ACTLOG-49: Kolom Division dan Note selalu terisi pada setiap Activity

17. Verifikasi baris `Login` milik `Budi Anwar {runId}-013`: sel Division berisi nama Division dan sel Note berisi teks Note, bukan `—`
18. Verifikasi baris `Logout` milik `Budi Anwar {runId}-013`: sel Division berisi nama Division dan sel Note berisi teks Note, bukan `—`
19. Verifikasi baris `Reset Password` milik `Budi Anwar {runId}-013`: sel Division berisi nama Division dan sel Note berisi teks Note, bukan `—`
20. Verifikasi baris `Change Password` milik `Budi Anwar {runId}-013`: sel Division berisi nama Division dan sel Note berisi teks Note, bukan `—`
21. Verifikasi baris `Session` milik `Budi Anwar {runId}-013`: sel Division berisi nama Division dan sel Note berisi teks Note, bukan `—`

### TC-GS-ACTLOG-50: Nilai kosong tampil `—` pada Employee ID, Position, dan Device / Browser

22. Ganti isi kotak search dengan `Tamu Operasional {runId}-013`, tekan Enter
23. Verifikasi sel Employee ID pada baris `Tamu Operasional {runId}-013` tampil `—` (bukan sel kosong dan bukan teks `null`)
24. Verifikasi sel Position pada baris `Tamu Operasional {runId}-013` tampil `—` (bukan sel kosong dan bukan teks `null`)
25. Verifikasi sel Device / Browser pada baris Reset Password milik `Tamu Operasional {runId}-013` tampil `—`

### TC-GS-ACTLOG-51: Nilai kosong tampil `—` pada IP Address

26. Ganti isi kotak search dengan `Dina Seed {runId}-013`, tekan Enter
27. Verifikasi sel IP Address pada baris `Dina Seed {runId}-013` tampil `—`

### TC-GS-ACTLOG-52: IP Address IPv4 dan IPv6 tampil penuh

28. Ganti isi kotak search dengan `John Doe {runId}-013`, tekan Enter
29. Verifikasi sel IP Address baris Login `John Doe {runId}-013` tampil `192.0.2.10` utuh
30. Ganti isi kotak search dengan `Siti Nurbaya {runId}-013`, tekan Enter
31. Verifikasi sel IP Address baris Login `Siti Nurbaya {runId}-013` dengan Device `Safari on iOS` tampil `2001:db8::1a` utuh

### TC-GS-ACTLOG-53: Format Device / Browser

32. Ganti isi kotak search dengan `John Doe {runId}-013`, tekan Enter
33. Verifikasi sel Device / Browser baris Login `John Doe {runId}-013` tampil `Chrome on Windows`
34. Ganti isi kotak search dengan `Siti Nurbaya {runId}-013`, tekan Enter
35. Verifikasi sel Device / Browser baris Login `Siti Nurbaya {runId}-013` dengan IP Address `2001:db8::1a` tampil `Safari on iOS`
36. Ganti isi kotak search dengan `Wayan Mobile {runId}-013`, tekan Enter
37. Verifikasi sel Device / Browser baris `Wayan Mobile {runId}-013` tampil `TAG Samurai App on Android`

## Notes

- Sumber TC: `global-settings/activity-log/TestCases/tc-activity-log.md` (TC-GS-ACTLOG-41, 42, 43, 49, 50, 51, 52, 53). Semua TC ini hanya mengamati baris hasil seeding di hook `before` (tidak ada aksi yang menambah baris), sehingga tidak memakai baseline "baris baru" (S-12).
- Langkah penghubung (tanpa awalan `Verifikasi`): mengetik atau mengganti Search nama subjek bersuffix pada langkah 2, 4, 6, 8, 11, 22, 26, 28, 30, 32, 34, 36 agar baris subjek ditemukan di antara baris run lain; tidak ada langkah pemulihan state yang diperlukan antar TC karena Search berikutnya menggantikan isi kotak Search sebelumnya.
- TC-GS-ACTLOG-49 (langkah 17 sampai 21) memakai hasil Search `Budi Anwar {runId}-013` dari langkah 11 tanpa Search ulang; kelima Activity milik subjek yang sama. Sel Division dan Note satu baris dinilai dalam satu `Verifikasi` per baris (kolom dari satu entri log, S-01); pernyataan "bukan `—`" (Expected TC-GS-ACTLOG-49) ada di tiap langkah itu.
- TC-GS-ACTLOG-42: spec tidak mengasersi jumlah baris atau urutan tampil dua baris `Siti Nurbaya {runId}-013`; kedua baris dikenali lewat Device `Safari on iOS` (Login perangkat B) dan Note `Logged out (new device login)` (Logout perangkat A). Baris Login perangkat A ikut tercatat.
- TC-GS-ACTLOG-52 dan TC-GS-ACTLOG-53: baris Login `Siti Nurbaya {runId}-013` perangkat B dikenali lewat Device `Safari on iOS` (langkah 31) dan lewat IP `2001:db8::1a` (langkah 35), supaya terpisah dari baris Login perangkat A.
- Spec ini 37 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik (isi kolom tab Session dari data hasil seeding) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Nama pada TC (`John Doe`, `Budi Anwar`, `Siti Nurbaya`) diganti nama bersuffix karena nama tidak menjadi bagian asersi di TC-GS-ACTLOG-41, 42, 43, 49, 50, 51, 52, 53.
- Temuan untuk QA:
  - TC-GS-ACTLOG-43 dan TC-GS-ACTLOG-49 tidak menyebut user pemilik entri tiap Activity; spec memakai satu user (`Budi Anwar {runId}-013`) untuk kelima Activity.
  - TC-GS-ACTLOG-42 Expected b ("pada waktu login perangkat B") tidak menyebut cara mengidentifikasi dua baris; TC-GS-ACTLOG-42, 52, dan 53 tidak menyebut atribut Login perangkat A `Siti Nurbaya`. Spec mengenali baris lewat Device, IP, dan Note perangkat B; nilai atribut perangkat A disediakan tim FE/BE dan QA konfirmasi apakah Login perangkat A tercatat sebagai baris.
  - TC-GS-ACTLOG-50 menyebut Device "tidak terparse" tanpa menyebut User-Agent; mekanismenya disediakan tim FE/BE.
  - TC-GS-ACTLOG-51 berstatus Manual Only karena entri IP null di-seed BE; mekanisme seed tidak ditentukan di TC, sehingga ditulis sebagai kemampuan yang disediakan tim FE/BE.
  - TC-GS-ACTLOG-53 tidak menyebut user tiap Device; spec memakai John, Siti, dan `Wayan Mobile {runId}-013`.
