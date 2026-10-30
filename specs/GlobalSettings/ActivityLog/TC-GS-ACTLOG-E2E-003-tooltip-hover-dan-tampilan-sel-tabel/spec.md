---
id: TC-GS-ACTLOG-E2E-003-tooltip-hover-dan-tampilan-sel-tabel
title: "Tooltip Hover dan Tampilan Sel Tabel"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-12
  - TC-GS-ACTLOG-13
  - TC-GS-ACTLOG-14
  - TC-GS-ACTLOG-15
  - TC-GS-ACTLOG-16
coverage:
  web: automated
---

# Tooltip Hover dan Tampilan Sel Tabel

## Prerequisites

- Mode: FE+BE.
- Akun (login aktor di hook `before`; hook `after` mengembalikan sesi ke akun default suite):
  - Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (`Spectra.env.GS_TC_PASSWORD`), pembaca Activity Log di seluruh spec ini. Password tidak ditulis di spec atau fixture.
  - Admin `Hendra Pratama` (Client A): `Fixture.activityLog.adminHendra` (email ditetapkan tim FE) dengan `Spectra.env.GS_HENDRA_PASSWORD`. Membuat Brand lewat sesi API di hook `before` sehingga muncul baris User Action dengan Modified By `Hendra P`.
  - Admin `Wulan` (Client A, nama lengkap satu kata): `Fixture.activityLog.adminWulan` (email ditetapkan tim FE) dengan `Spectra.env.GS_WULAN_PASSWORD`. Membuat Brand lewat sesi API di hook `before` sehingga muncul baris User Action dengan Modified By `Wulan`.
  - Password user uji Session (John Doe, Siti Nurbaya, Budi): `Spectra.env.ACTLOG_PASSWORD` (memenuhi Password Policy). Password salah untuk login gagal: `Spectra.env.LP_PASSWORD_WRONG`.
- Data Pre-setup: tidak ada selain akun aktor dan akun admin di atas.
- Data Dinamis (dibuat di hook `before` lewat API oleh Total Control Client A; nama user literal karena asersi singkatan `John D`, `Siti N`, `Budi` dan tooltip nama lengkap bergantung pada nama itu; identifikasi baris memakai Employee ID bersuffix):
  - User `John Doe`, email `johndoe+{runId}-003@qwertysystem.net`, Employee ID `EMP-{runId}-003-A`.
  - User `Siti Nurbaya`, email `sitinurbaya+{runId}-003@qwertysystem.net`, Employee ID `EMP-{runId}-003-B`.
  - User `Budi` (nama lengkap satu kata `Budi`), email `budi+{runId}-003@qwertysystem.net`, Employee ID `EMP-{runId}-003-C`.
  - Baris Session (hanya yang dipakai `Verifikasi`): tiap user uji login sekali lewat sesi API sehingga terbentuk baris `Login` `Success`; John Doe ditambah satu login dengan password salah sehingga terbentuk baris `Login` `Failed`.
  - Brand `Brand Tooltip {runId}-003-H` dibuat oleh Hendra Pratama dan Brand `Brand Tooltip {runId}-003-W` dibuat oleh Wulan, keduanya lewat sesi API (aksi `Create`, Object `Brand`).
  - Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus user uji dan kedua Brand lewat API. Baris log tidak dapat dihapus (append-only).
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- Kemampuan teknis: hover elemen dan membaca tooltip; membaca gaya kursor, warna teks, dan ada/tidaknya elemen badge pada sel (TC-GS-ACTLOG-15 dan TC-GS-ACTLOG-16).
- Suite serial: `parallel: false` (lihat `suite.md`). Spec tidak mengubah format tanggal, zona waktu, atau jam.

## Test Steps

### TC-GS-ACTLOG-12: Tooltip hover pada ikon Table Tools dan header Column Visibility, kedua tab

1. Buka Global Settings > Activity Log > Session
2. Arahkan kursor ke icon Search
3. Verifikasi tab Session: tooltip icon Search `Search`
4. Arahkan kursor ke icon Filter
5. Verifikasi tab Session: tooltip icon Filter `Filter`
6. Arahkan kursor ke icon Download
7. Verifikasi tab Session: tooltip icon Download `Download`
8. Arahkan kursor ke header kolom `Column Visibility (⋯)`
9. Verifikasi tab Session: tooltip header `Column Visibility`
10. Klik tab "User Action"
11. Arahkan kursor ke icon Search
12. Verifikasi tab User Action: tooltip icon Search `Search`
13. Arahkan kursor ke icon Filter
14. Verifikasi tab User Action: tooltip icon Filter `Filter`
15. Arahkan kursor ke icon Download
16. Verifikasi tab User Action: tooltip icon Download `Download`
17. Arahkan kursor ke header kolom `Column Visibility (⋯)`
18. Verifikasi tab User Action: tooltip header `Column Visibility`

### TC-GS-ACTLOG-15: Baris tabel tidak dapat diklik, kedua tab

19. Klik tab "Session"
20. Klik sel kolom Activity pada satu baris
21. Klik sel kolom User pada baris yang sama
22. Verifikasi tab Session: tidak ada navigasi, popup, atau halaman Detail yang terbuka
23. Arahkan kursor ke sel kolom User pada baris yang sama
24. Verifikasi tab Session: kursor bukan pointer link
25. Verifikasi tab Session: teks sel tidak berubah warna saat hover
26. Klik tab "User Action"
27. Klik sel kolom Object pada satu baris
28. Klik sel kolom Name pada baris yang sama
29. Verifikasi tab User Action: tidak ada navigasi, popup, atau halaman Detail yang terbuka
30. Arahkan kursor ke sel kolom Name pada baris yang sama
31. Verifikasi tab User Action: kursor bukan pointer link
32. Verifikasi tab User Action: teks sel tidak berubah warna saat hover

### TC-GS-ACTLOG-16: Kolom Activity, Status, Action, Object tampil sebagai plain text tanpa badge berwarna

33. Klik tab "Session"
34. Amati kolom Activity dan kolom Status
35. Verifikasi tab Session: nilai kolom Activity dan kolom Status tampil sebagai teks biasa, tanpa kotak badge
36. Verifikasi tab Session: nilai kolom Activity dan kolom Status tanpa warna severity
37. Klik tab "User Action"
38. Amati kolom Action dan kolom Object
39. Verifikasi tab User Action: nilai kolom Action dan kolom Object tampil sebagai teks biasa, tanpa kotak badge
40. Verifikasi tab User Action: nilai kolom Action dan kolom Object tanpa warna severity

### TC-GS-ACTLOG-13: Tooltip nama lengkap pada kolom User Tab Session

41. Klik tab "Session"
42. Ketik Search `EMP-{runId}-003`, tekan Enter
43. Amati sel kolom User pada baris `Login` `Success` milik `John Doe`, `Siti Nurbaya`, dan `Budi`
44. Verifikasi nilai sel kolom User: `John D`, `Siti N`, `Budi`
45. Verifikasi sel kolom User tampil sebagai plain text, bukan badge
46. Arahkan kursor ke sel `John D`
47. Verifikasi tooltip `John Doe`
48. Arahkan kursor ke sel `Siti N`
49. Verifikasi tooltip `Siti Nurbaya`
50. Arahkan kursor ke sel `Budi`
51. Verifikasi tooltip `Budi`
52. Klik `(←)` pada kotak Search

### TC-GS-ACTLOG-14: Tooltip nama lengkap pada kolom Modified By Tab User Action

53. Klik tab "User Action"
54. Ketik Search `Brand Tooltip {runId}-003`, tekan Enter
55. Amati sel kolom Modified By pada baris `Create` dengan Name `Brand Tooltip {runId}-003-H` (Hendra Pratama) dan baris `Create` dengan Name `Brand Tooltip {runId}-003-W` (Wulan)
56. Verifikasi nilai sel kolom Modified By: `Hendra P`, `Wulan`
57. Verifikasi sel kolom Modified By tampil sebagai plain text, bukan badge
58. Arahkan kursor ke sel `Hendra P`
59. Verifikasi tooltip `Hendra Pratama`
60. Arahkan kursor ke sel `Wulan`
61. Verifikasi tooltip `Wulan`
62. Klik `(←)` pada kotak Search

## Notes

- Sumber: `global-settings/activity-log/TestCases/tc-activity-log.md` (TC-GS-ACTLOG-12, 13, 14, 15, 16). Tidak ada TC hanya-BE.
- Urutan TC di spec: TC-12, TC-15, TC-16, TC-13, TC-14 (bukan urutan nomor) supaya TC yang mengamati tabel tanpa Search (15 dan 16) berjalan sebelum TC yang memakai Search (13 dan 14); asersi tiap TC tidak berubah.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 19, 33, 41 (kembali ke tab Session), 23 dan 30 (hover sel untuk mengamati kursor dan warna, butir Expected TC-15), 42 dan 54 (Search dengan Employee ID atau Name bersuffix untuk menemukan baris milik run ini; langkah TC hanya menyebut "amati sel pada baris"; kotak Search pada tiap tab belum terbuka sebelum langkah itu), 52 dan 62 (menutup kotak Search dan mereset tabel sebelum TC berikutnya, S-09).
- Spec di atas smell 35 langkah (62 langkah). Alasan: seluruh TC satu kelas (observasi tampilan read-only atas dataset yang sama), tidak ada mutasi data pada langkah uji, dan tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-14 menulis admin `Admin Satu` (nama lengkap `Hendra Pratama`) tetapi tidak menjelaskan hubungan alias `Admin Satu` dengan kolom Modified By; spec memakai nama lengkap `Hendra Pratama` dan tidak mengasersi alias.
  - Env `ACTLOG_PASSWORD`, `GS_HENDRA_PASSWORD`, dan `GS_WULAN_PASSWORD` belum terdaftar di `.env.example`; email admin ditetapkan tim FE (fixture baru).
  - Precondition TC-16 menyebut variasi Activity (`Reset Password`, `Change Password`, `Session`) dan Action (`Edit`, `Delete`), sedangkan Expected tidak mengasersi per varian; spec hanya menyiapkan baris yang diasersi (Activity `Login`, Status `Success` dan `Failed`, Action `Create`, Object `Brand` dan `User`).
  - TC-15 tidak menyebut cara mengamati "kursor bukan pointer link" dan "tidak berubah warna"; spec mengasumsikan kemampuan membaca gaya CSS elemen.
