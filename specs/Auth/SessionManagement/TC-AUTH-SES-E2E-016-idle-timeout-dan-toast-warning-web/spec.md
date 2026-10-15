---
id: TC-AUTH-SES-E2E-016-idle-timeout-dan-toast-warning-web
title: "Idle Timeout dan Toast Idle Warning Web"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-44
  - TC-AUTH-SES-45
  - TC-AUTH-SES-46
  - TC-AUTH-SES-47
  - TC-AUTH-SES-48
  - TC-AUTH-SES-284
coverage:
  web: automated
---

# Idle Timeout dan Toast Idle Warning Web

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): enam user profil BASE milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5 dan #11: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON; MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-44: `Putri Wulandari` (`putriwulandari+{runId}-016@qwertysystem.net`)
  - TC-AUTH-SES-45: `Eko Hidayat` (`ekohidayat+{runId}-016@qwertysystem.net`)
  - TC-AUTH-SES-46: `Wulan Utami` (`wulanutami+{runId}-016@qwertysystem.net`)
  - TC-AUTH-SES-47: `Bayu Puspita` (`bayupuspita+{runId}-016@qwertysystem.net`)
  - TC-AUTH-SES-48: `Intan Saputra` (`intansaputra+{runId}-016@qwertysystem.net`)
  - TC-AUTH-SES-284: `Bayu Rahayu` (`bayurahayu+{runId}-016@qwertysystem.net`)
- Sesi web aktif (status Active) tiap user di Browser A dibuat lewat login API oleh langkah seeding di awal TC masing-masing, bukan di hook `before`: jam server uji dan jam browser/perangkat uji dimajukan kumulatif sepanjang spec, sehingga sesi yang dibuat lebih awal akan menua dan kedaluwarsa sebelum TC-nya berjalan. TC-AUTH-SES-284 memakai dua tab (Tab A1 dan Tab A2) di Browser A yang sama.
- Hook `after`: akhiri semua sesi seed, tutup konteks Browser A, kembalikan jam server uji dan jam browser uji ke waktu nyata, hapus keenam user. Hook ini tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness d: time-travel): jam server uji dan jam browser/perangkat uji (timer idle dan hitung mundur Toast di client) dapat dimajukan bersama dengan presisi detik, dibekukan pada nilai yang diminta, dan dipulihkan ke waktu nyata; perekaman request dan respons jaringan di Browser A untuk heartbeat `PUT /v2/iam/auth/sessions/heartbeat` beserta field `expiresAt` (TC-AUTH-SES-45, 48); pemindahan tab ke background dan aktivasi kembali tanpa sinyal aktivitas (TC-AUTH-SES-284); pembacaan status sesi user uji dari sisi BE (Active atau Expired) untuk Expected TC-AUTH-SES-47.
- Suite berjalan serial (`parallel: false`); state global yang diubah: jam server uji dan jam browser/perangkat uji (diatur bersama), dipulihkan di hook `after`.
- Titik waktu: batas idle 15 menit; Toast Idle Warning tampil saat sisa waktu 5 menit (idle 10 menit); "idle" diukur dari aktivitas terakhir.
- Akun yang dipakai: user uji masing-masing TC (bukan akun aktor) di Browser A; akun aktor hanya untuk seeding.

## Test Steps

### TC-AUTH-SES-44: Toast Idle Warning muncul saat sisa waktu kedaluwarsa 5 menit

1. Buka konteks Browser A baru lalu buat sesi web aktif `Putri Wulandari` lewat login API (seeding BE) → sesi berstatus Active
2. Di Browser A buka Portal — Product Hub → halaman Portal — Product Hub tampil
3. Biarkan Browser A tanpa aktivitas
4. Majukan jam server uji dan jam browser/perangkat uji bersama 9 menit 30 detik → amati layar
5. Verifikasi Pada idle 9 menit 30 detik Toast belum tampil
6. Majukan jam server uji dan jam browser/perangkat uji bersama sampai idle 10 menit (sisa waktu 5 menit) → amati layar
7. Verifikasi Toast "Idle Warning" tampil: Title "Session Expiring Soon"; Body "Your session will expire in 5 minutes due to inactivity. Move your mouse or press any key to stay logged in."
8. Verifikasi Toast non-blocking (halaman di belakang toast tidak terblokir)
9. Verifikasi Hanya satu toast yang tampil

### TC-AUTH-SES-45: Aktivitas saat Toast Idle Warning tampil menghilangkan toast dan memperpanjang sesi

10. Buka konteks Browser A baru lalu buat sesi web aktif `Eko Hidayat` lewat login API (seeding BE) → sesi berstatus Active
11. Di Browser A buka Portal — Product Hub → halaman Portal — Product Hub tampil
12. Mulai perekaman request jaringan heartbeat di Browser A
13. Majukan jam server uji dan jam browser/perangkat uji bersama sampai idle 10 menit tanpa aktivitas → Toast "Idle Warning" tampil
14. Gerakkan mouse di Browser A → heartbeat terkirim
15. Verifikasi Toast hilang setelah mouse digerakkan
16. Verifikasi Waktu kedaluwarsa pada respons heartbeat (`expiresAt`) maju ke aktivitas terakhir + 15 menit
17. Majukan jam server uji dan jam browser/perangkat uji bersama 6 menit tanpa aktivitas
18. Verifikasi Setelah 6 menit berikutnya tidak ada Dialog Session Expired

### TC-AUTH-SES-46: Idle sampai batas memunculkan Dialog Session Expired dan halaman beku

19. Buka konteks Browser A baru lalu buat sesi web aktif `Wulan Utami` lewat login API (seeding BE) → sesi berstatus Active
20. Di Browser A buka Portal — Product Hub → halaman Portal — Product Hub tampil
21. Biarkan Browser A tanpa aktivitas dan majukan jam server uji dan jam browser/perangkat uji bersama 10 menit → amati Toast
22. Verifikasi Pada idle 10 menit Toast Idle Warning sudah tampil lebih dulu
23. Majukan jam server uji dan jam browser/perangkat uji bersama 6 menit lagi (idle 16 menit) → Dialog Session Expired tampil
24. Verifikasi Dialog "Session Expired" tampil dengan Body "Your session has expired due to inactivity."
25. Verifikasi Dialog hanya memuat satu tombol [Refresh]
26. Klik salah satu tombol atau menu di halaman Portal — Product Hub di belakang dialog
27. Verifikasi Halaman di belakang dialog beku: klik tidak berpengaruh

### TC-AUTH-SES-47: Idle tepat sama dengan batas dianggap kedaluwarsa

28. Buka konteks Browser A baru lalu buat sesi web aktif `Bayu Puspita` lewat login API (seeding BE) → sesi berstatus Active
29. Di Browser A buka Portal — Product Hub → halaman Portal — Product Hub tampil
30. Biarkan Browser A tanpa aktivitas
31. Majukan jam server uji dan jam browser/perangkat uji bersama tepat 15 menit 00 detik sejak aktivitas terakhir dan tunggu cek server
32. Verifikasi Dialog "Session Expired" tampil (idle = batas dianggap kedaluwarsa)
33. Verifikasi Sesi berstatus Expired

### TC-AUTH-SES-48: Aktivitas sesaat sebelum batas mengirim heartbeat segera dan mencegah Session Expired

34. Buka konteks Browser A baru lalu buat sesi web aktif `Intan Saputra` lewat login API (seeding BE) → sesi berstatus Active
35. Di Browser A buka Portal — Product Hub → halaman Portal — Product Hub tampil
36. Mulai perekaman request jaringan heartbeat di Browser A
37. Majukan jam server uji dan jam browser/perangkat uji bersama 14 menit 50 detik tanpa aktivitas (interval heartbeat sudah terlewati)
38. Gerakkan mouse di Browser A
39. Verifikasi Heartbeat dikirim segera pada sinyal aktivitas pertama
40. Verifikasi Waktu kedaluwarsa diperbarui (`expiresAt` pada respons heartbeat maju dari aktivitas terakhir)
41. Majukan jam server uji dan jam browser/perangkat uji bersama 1 menit lagi
42. Verifikasi Dialog Session Expired tidak tampil

### TC-AUTH-SES-284: Tab yang kembali aktif setelah ambang toast terlewat langsung menampilkan toast, atau dialog bila sesi sudah expired

43. Buka konteks Browser A baru lalu buat sesi web aktif `Bayu Rahayu` lewat login API (seeding BE) → sesi berstatus Active
44. Di Browser A buka dua tab (Tab A1 dan Tab A2) pada Portal — Product Hub → kedua tab menampilkan Portal — Product Hub
45. Pindahkan Tab A1 ke background (aktifkan Tab A2)
46. Majukan jam server uji dan jam browser/perangkat uji bersama sampai sisa waktu 4 menit (idle 11 menit)
47. Aktifkan kembali Tab A1
48. Verifikasi Toast "Idle Warning" langsung tampil di Tab A1 karena sesi masih valid
49. Pindahkan Tab A1 ke background lagi (aktifkan Tab A2)
50. Majukan jam server uji dan jam browser/perangkat uji bersama sampai idle 16 menit
51. Aktifkan kembali Tab A1
52. Verifikasi Dialog "Session Expired" langsung tampil di Tab A1 karena sesi sudah lewat batas

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness d (time-travel).
- Urutan mengikuti TC sumber. Tiap TC memakai user dan sesi sendiri yang dibuat di awal TC-nya; jam server uji dan jam browser/perangkat uji dimajukan kumulatif dan tidak dipulihkan antar-TC, tetapi tidak memengaruhi TC berikutnya karena sesinya dibuat sesudah jam digeser (pemulihan di hook `after`).
- Dependensi (S-04): TC-AUTH-SES-45 dan 46 berdependensi pada TC-AUTH-SES-44 (Toast tampil pada idle 10 menit); langkah penyiapan itu disalin sebagai langkah 13 (TC-AUTH-SES-45) dan langkah 21 (TC-AUTH-SES-46), asersi Toast lengkap hanya di TC-AUTH-SES-44. TC-AUTH-SES-47 dan 283 berhubungan sebagai pasangan batas; TC-AUTH-SES-283 (idle 14 menit 59 detik) ada di spec `TC-AUTH-SES-E2E-017-batas-idle-konfigurasi`.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): membuka konteks Browser A baru dan membuat sesi seed; membuka Portal — Product Hub; memulai perekaman request jaringan; memindahkan tab ke background dan mengaktifkannya kembali.
- TC-AUTH-SES-46 Expected butir c (Toast sudah tampil pada idle 10 menit) diletakkan sebagai `Verifikasi` langsung setelah langkah 21 karena terjadi lebih dulu daripada Dialog (S-01, S-14).
- Pencatatan sesi expired (log) tidak diasersikan di spec ini; absence dan pencatatan ada di spec lain modul ini (S-05).
- Temuan untuk QA: (1) TC-AUTH-SES-44 sampai 48 dan 284 hanya menyebut "majukan waktu server", sedangkan Toast dan Dialog dipicu hitung mundur di client (`AUTHSES-LOGIC-02d`); spec menambahkan kebutuhan jam browser uji ikut dimajukan di Prerequisites. (2) TC-AUTH-SES-47 dan 48 memakai batas presisi detik (15 menit 00 detik, 14 menit 50 detik); waktu nyata antara memajukan jam dan pengamatan dapat menggeser hasil, sehingga jam server uji perlu dapat dibekukan pada nilai yang diminta. (3) Expected "sesi berstatus Expired" (TC-AUTH-SES-47) tidak menyebut cara membaca status sesi dan OpenAPI modul tidak punya endpoint baca status; spec menuliskan kebutuhan pembacaan status dari sisi BE di Prerequisites. (4) TC-AUTH-SES-46 langkah 3 "klik tombol atau menu di halaman di belakang dialog" tidak menyebut elemennya; spec memakai satu tombol atau menu di Portal — Product Hub. (5) TC-AUTH-SES-284 "sisa 4 menit" ditafsirkan sebagai idle 11 menit pada batas 15 menit, dan "pindahkan ke background" ditafsirkan sebagai mengaktifkan tab lain; TC tidak menyebut cara memindahkan tab tanpa sinyal aktivitas.
- Ukuran: spec memuat 52 langkah (melebihi sekitar 35) karena enam TC satu kelas harness (time-travel) berada dalam satu spec; tiap TC memakai user dan sesi sendiri yang dibuat di awal TC-nya, sehingga bagian berikutnya tetap bermakna meski TC lain di spec ini tidak dijalankan.
