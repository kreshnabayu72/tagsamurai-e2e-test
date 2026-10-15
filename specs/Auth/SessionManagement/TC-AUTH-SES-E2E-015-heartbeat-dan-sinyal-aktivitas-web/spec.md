---
id: TC-AUTH-SES-E2E-015-heartbeat-dan-sinyal-aktivitas-web
title: "Heartbeat dan Sinyal Aktivitas Web"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-39
  - TC-AUTH-SES-40
  - TC-AUTH-SES-41
  - TC-AUTH-SES-42
  - TC-AUTH-SES-43
  - TC-AUTH-SES-244
coverage:
  web: automated
---

# Heartbeat dan Sinyal Aktivitas Web

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): enam user profil BASE milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5 dan #11: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON; MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-39: `Hendra Kusuma` (`hendrakusuma+{runId}-015@qwertysystem.net`)
  - TC-AUTH-SES-40: `Maya Permata` (`mayapermata+{runId}-015@qwertysystem.net`)
  - TC-AUTH-SES-41: `Fajar Lestari` (`fajarlestari+{runId}-015@qwertysystem.net`)
  - TC-AUTH-SES-42: `Lestari Pratama` (`lestaripratama+{runId}-015@qwertysystem.net`)
  - TC-AUTH-SES-43: `Dimas Ramadhan` (`dimasramadhan+{runId}-015@qwertysystem.net`)
  - TC-AUTH-SES-244: `Agus Saputra` (`agussaputra+{runId}-015@qwertysystem.net`)
- Sesi web aktif (status Active) tiap user di Browser A (TC-AUTH-SES-244 di Chrome on Windows) dibuat lewat login API oleh langkah seeding di awal TC masing-masing, bukan di hook `before`: jam server uji dan jam browser/perangkat uji dimajukan kumulatif sepanjang spec, sehingga sesi yang dibuat lebih awal akan menua sebelum TC-nya berjalan.
- Hook `after`: akhiri semua sesi seed, tutup konteks Browser A, kembalikan jam server uji dan jam browser uji ke waktu nyata, hapus keenam user. Hook ini tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness d: time-travel dan pemantauan jaringan): perekaman request dan respons jaringan di Browser A (padanan panel Network DevTools) untuk request heartbeat `PUT /v2/iam/auth/sessions/heartbeat` beserta field `expiresAt` pada respons (OpenAPI modul); emulasi sinyal aktivitas mouse (mousemove), keyboard (keydown), scroll, dan sentuhan layar (touchstart, emulasi touch); jam server uji dan jam browser/perangkat uji (timer idle dan interval heartbeat di client) dapat dimajukan bersama dengan presisi detik dan dipulihkan ke waktu nyata, sehingga spec ini tidak menunggu waktu nyata; pembacaan waktu kedaluwarsa sesi pada data sesi di backend dari BE uji (disediakan tim FE/BE, tanpa endpoint tertentu) untuk TC-AUTH-SES-43.
- Suite berjalan serial (`parallel: false`); state global yang diubah: jam server uji dan jam browser/perangkat uji (diatur bersama), dipulihkan di hook `after`.
- Titik waktu: interval heartbeat 60 detik (Data Uji TC-AUTH-SES-39); batas idle 15 menit.
- Akun yang dipakai: user uji masing-masing TC (bukan akun aktor) di Browser A.

## Test Steps

### TC-AUTH-SES-39: Sinyal aktivitas pertama setelah interval heartbeat terlewati langsung mengirim heartbeat

1. Buka konteks Browser A baru lalu buat sesi web aktif `Hendra Kusuma` lewat login API (seeding BE) → sesi berstatus Active
2. Di Browser A buka Portal — Product Hub → halaman Portal — Product Hub tampil
3. Majukan jam server uji dan jam browser/perangkat uji bersama 61 detik tanpa sinyal aktivitas supaya heartbeat terakhir sudah lebih dari 60 detik lalu
4. Mulai perekaman request jaringan heartbeat di Browser A
5. Gerakkan kursor mouse di halaman Portal — Product Hub
6. Amati request jaringan heartbeat yang terekam
7. Verifikasi Satu request heartbeat dikirim segera pada sinyal aktivitas pertama
8. Verifikasi Respons heartbeat memuat waktu kedaluwarsa sesi yang baru (`expiresAt`)

### TC-AUTH-SES-40: Tanpa sinyal aktivitas tidak ada heartbeat yang dikirim

9. Buka konteks Browser A baru lalu buat sesi web aktif `Maya Permata` lewat login API (seeding BE) → sesi berstatus Active
10. Di Browser A buka Portal — Product Hub → halaman Portal — Product Hub tampil
11. Mulai perekaman request jaringan heartbeat di Browser A
12. Di Browser A jangan gerakkan mouse, jangan tekan tombol, dan jangan scroll, sambil memajukan jam server uji dan jam browser/perangkat uji bersama 3 menit
13. Amati request jaringan heartbeat yang terekam
14. Verifikasi Tidak ada request heartbeat selama 3 menit
15. Verifikasi Tidak ada dialog dan tidak ada toast

### TC-AUTH-SES-41: Banyak sinyal aktivitas dalam satu interval hanya mengirim satu heartbeat

16. Buka konteks Browser A baru lalu buat sesi web aktif `Fajar Lestari` lewat login API (seeding BE) → sesi berstatus Active
17. Di Browser A buka Portal — Product Hub → halaman Portal — Product Hub tampil
18. Mulai perekaman request jaringan heartbeat di Browser A
19. Di Browser A gerakkan mouse, tekan tombol keyboard, dan scroll terus-menerus, sambil memajukan jam server uji dan jam browser/perangkat uji bersama 50 detik
20. Amati request jaringan di Browser A
21. Verifikasi Tidak lebih dari satu request heartbeat per interval 60 detik, walau sinyal aktivitas banyak
22. Verifikasi Sinyal mentah (mousemove, keydown, scroll) tidak dikirim satu per satu ke server

### TC-AUTH-SES-244: Heartbeat tetap dipakai sebagai sumber kebenaran: waktu kedaluwarsa dihitung ulang tiap heartbeat

23. Buka konteks Browser A baru (Chrome on Windows) lalu buat sesi web aktif `Agus Saputra` lewat login API (seeding BE) → sesi berstatus Active
24. Di Browser A buka Portal — Product Hub → halaman Portal — Product Hub tampil
25. Mulai perekaman request jaringan heartbeat di Browser A
26. Gerakkan mouse di Browser A → heartbeat pertama terkirim
27. Verifikasi Respons heartbeat pertama memuat waktu kedaluwarsa = aktivitas terakhir + 15 menit
28. Majukan jam server uji dan jam browser/perangkat uji bersama 60 detik, lalu gerakkan mouse di Browser A → heartbeat kedua terkirim
29. Verifikasi Respons heartbeat kedua memuat waktu kedaluwarsa = aktivitas terakhir + 15 menit
30. Majukan jam server uji dan jam browser/perangkat uji bersama 60 detik, lalu gerakkan mouse di Browser A → heartbeat ketiga terkirim
31. Verifikasi Respons heartbeat ketiga memuat waktu kedaluwarsa = aktivitas terakhir + 15 menit
32. Verifikasi FE memakai waktu kedaluwarsa dari respons heartbeat, bukan batas dalam menit

### TC-AUTH-SES-42: Setiap jenis sinyal aktivitas mereset timer idle

33. Buka konteks Browser A baru lalu buat sesi web aktif `Lestari Pratama` lewat login API (seeding BE) → sesi berstatus Active
34. Di Browser A buka Portal — Product Hub → halaman Portal — Product Hub tampil
35. Mulai perekaman request jaringan heartbeat di Browser A
36. Majukan jam server uji dan jam browser/perangkat uji bersama 12 menit tanpa aktivitas
37. Gerakkan mouse di Browser A → heartbeat terkirim
38. Catat waktu kedaluwarsa (`expiresAt`) pada respons heartbeat
39. Verifikasi Timer idle di client direset
40. Verifikasi Waktu kedaluwarsa pada respons heartbeat = waktu aktivitas terakhir (mouse) + 15 menit
41. Verifikasi Tidak ada Toast Idle Warning dan tidak ada Dialog Session Expired setelah aktivitas mouse
42. Majukan jam server uji dan jam browser/perangkat uji bersama 12 menit tanpa aktivitas
43. Tekan tombol keyboard di Browser A → heartbeat terkirim
44. Catat waktu kedaluwarsa (`expiresAt`) pada respons heartbeat
45. Verifikasi Timer idle di client direset
46. Verifikasi Waktu kedaluwarsa pada respons heartbeat = waktu aktivitas terakhir (keyboard) + 15 menit
47. Verifikasi Tidak ada Toast Idle Warning dan tidak ada Dialog Session Expired setelah aktivitas keyboard
48. Majukan jam server uji dan jam browser/perangkat uji bersama 12 menit tanpa aktivitas
49. Scroll halaman di Browser A → heartbeat terkirim
50. Catat waktu kedaluwarsa (`expiresAt`) pada respons heartbeat
51. Verifikasi Timer idle di client direset
52. Verifikasi Waktu kedaluwarsa pada respons heartbeat = waktu aktivitas terakhir (scroll) + 15 menit
53. Verifikasi Tidak ada Toast Idle Warning dan tidak ada Dialog Session Expired setelah aktivitas scroll
54. Majukan jam server uji dan jam browser/perangkat uji bersama 12 menit tanpa aktivitas
55. Sentuh layar di Browser A (emulasi touch) → heartbeat terkirim
56. Catat waktu kedaluwarsa (`expiresAt`) pada respons heartbeat
57. Verifikasi Timer idle di client direset
58. Verifikasi Waktu kedaluwarsa pada respons heartbeat = waktu aktivitas terakhir (touch) + 15 menit
59. Verifikasi Tidak ada Toast Idle Warning dan tidak ada Dialog Session Expired setelah aktivitas touch

### TC-AUTH-SES-43: Panggilan API apa pun dianggap aktivitas dan memperpanjang waktu kedaluwarsa

60. Buka konteks Browser A baru lalu buat sesi web aktif `Dimas Ramadhan` lewat login API (seeding BE) → sesi berstatus Active
61. Di Browser A buka Portal — Product Hub → halaman Portal — Product Hub tampil
62. Majukan jam server uji dan jam browser/perangkat uji bersama 12 menit tanpa sinyal UI
63. Di Browser A buka `Global Settings > User` sehingga daftar dimuat dari server (aksi yang memanggil API)
64. Verifikasi Waktu kedaluwarsa sesi pada data sesi di backend dihitung ulang dari panggilan API tersebut (aktivitas terakhir + 15 menit)
65. Majukan jam server uji dan jam browser/perangkat uji bersama 4 menit lagi tanpa aktivitas
66. Verifikasi Dialog Session Expired belum tampil (total 16 menit sejak sesi dibuat, tetapi hanya 4 menit sejak aktivitas API terakhir)

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness d (time-travel dan pemantauan jaringan).
- Penyimpangan urutan (S-05, S-10): urutan di spec ini TC-AUTH-SES-39, 40, 41, 244, 42, 43 (urutan TC sumber 39, 40, 41, 42, 43, 244). TC-AUTH-SES-244 hanya memajukan jam 60 detik per langkah, sehingga ditaruh sebelum dua TC yang memajukan jam belasan menit. Tiap TC memakai user dan sesi sendiri yang dibuat di awal TC-nya, jadi urutan tidak membuat TC saling bergantung.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): membuka konteks Browser A baru dan membuat sesi seed; membuka Portal — Product Hub; memulai perekaman request jaringan; memajukan jam server dan jam browser/perangkat bersama (61 detik pada TC-AUTH-SES-39, 3 menit pada TC-AUTH-SES-40, 50 detik pada TC-AUTH-SES-41, 60 detik antar heartbeat pada TC-AUTH-SES-244); mencatat `expiresAt`.
- Pada TC-AUTH-SES-42 setelah 12 menit tanpa aktivitas Toast Idle Warning sudah tampil (sisa kurang dari 5 menit) sebelum sinyal aktivitas diberikan; TC sumber tidak mengasersikannya, jadi spec ini hanya mengasersikan keadaan sesudah aktivitas. Asersi Toast Idle Warning ada di spec `TC-AUTH-SES-E2E-016-idle-timeout-dan-toast-warning-web`.
- Temuan untuk QA: (1) TC-AUTH-SES-39 menulis kondisi "heartbeat terakhir sudah lebih dari 60 detik lalu" sebagai precondition tanpa cara membuatnya; spec memajukan jam server dan jam browser/perangkat bersama 61 detik tanpa sinyal aktivitas setelah sesi dibuat. (2) TC-AUTH-SES-40 dan 41 menulis "heartbeat terakhir baru saja dikirim" tanpa cara membuatnya; spec memulai langkah segera setelah sesi seed dibuat dan halaman Portal terbuka. (3) TC-AUTH-SES-42, 43 hanya menyebut "majukan waktu server", sedangkan timer idle dan Toast dihitung di client (`AUTHSES-LOGIC-02d`); spec menambahkan kebutuhan jam browser uji ikut dimajukan di Prerequisites. (4) TC-AUTH-SES-244 menyebut "waktu kedaluwarsa" tanpa sumber pembacaan; spec membacanya dari field `expiresAt` respons heartbeat (OpenAPI `HeartbeatResponseData`). TC-AUTH-SES-43 Expected a menyebut "data sesi di backend" tanpa cara membacanya; panggilan `Global Settings > User` bukan heartbeat, sehingga spec memakai kemampuan pembacaan data sesi BE uji yang disediakan tim FE/BE (Prerequisites) tanpa mengarang endpoint. (5) TC-AUTH-SES-43 memakai `Global Settings > User` sebagai contoh aksi API untuk user profil BASE tanpa menyebut izin akses halaman itu; spec mengikuti TC. (6) TC-AUTH-SES-244 "FE memakai nilai itu, bukan batas dalam menit" tidak menyebut cara mengamatinya; spec menuliskannya sebagai satu `Verifikasi` dan cara amatnya diputuskan di tahap script. (7) Halaman Login with Password tidak dipakai di spec ini karena sesi seed dibuat lewat login API; bila TC dijalankan lewat UI, widget reCAPTCHA tidak disebut TC.
- Ukuran: spec memuat 66 langkah (melebihi sekitar 35) karena enam TC satu kelas harness (time-travel dan pemantauan jaringan) berada dalam satu spec; tiap TC memakai user dan sesi sendiri yang dibuat di awal TC-nya, sehingga bagian berikutnya tetap bermakna meski TC lain di spec ini tidak dijalankan.
