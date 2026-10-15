---
id: TC-AUTH-SES-E2E-019-session-expired-multi-tab
title: "Session Expired Multi Tab Web"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-53
  - TC-AUTH-SES-54
  - TC-AUTH-SES-55
  - TC-AUTH-SES-49
coverage:
  web: automated
---

# Session Expired Multi Tab Web

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): empat user profil BASE milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5 dan #11: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON; MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-53: `Taufik Wibowo` (`taufikwibowo+{runId}-019@qwertysystem.net`)
  - TC-AUTH-SES-54: `Mega Nugroho` (`meganugroho+{runId}-019@qwertysystem.net`)
  - TC-AUTH-SES-55: `Reza Maulana` (`rezamaulana+{runId}-019@qwertysystem.net`)
  - TC-AUTH-SES-49: `Joko Firmansyah` (`jokofirmansyah+{runId}-019@qwertysystem.net`)
- Sesi web aktif (status Active) tiap user di Browser A dengan dua tab (Tab A dan Tab B) dibuat lewat login API oleh langkah seeding di awal TC masing-masing, bukan di hook `before`: jam server uji dan jam browser/perangkat uji dimajukan kumulatif sehingga sesi yang dibuat lebih awal akan menua dan kedaluwarsa sebelum TC-nya berjalan. Kedua tab berada di satu konteks Browser A (cookie sesi dipakai bersama).
- Hook `after`: akhiri semua sesi seed, tutup konteks Browser A, kembalikan jam server uji dan jam browser uji ke waktu nyata, hapus keempat user. Hook ini tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness c: multi-tab, dan d: time-travel): dua tab dalam satu konteks browser yang dapat dioperasikan bergantian dengan emulasi mouse per tab; jam server uji dan jam browser/perangkat uji (hitung mundur lokal tiap tab) dapat dimajukan bersama dengan presisi detik dan dipulihkan ke waktu nyata; perekaman request jaringan per tab (TC-AUTH-SES-54: request cek server milik Tab B, dibedakan dari heartbeat Tab A) dan pendeteksian pesan antar-tab di sisi client (TC-AUTH-SES-54); perekaman navigasi per tab untuk mendeteksi halaman ter-refresh (TC-AUTH-SES-55, 49); pembacaan status sesi user uji dari sisi BE (Active atau Expired) untuk TC-AUTH-SES-55; reCAPTCHA mode uji di environment (halaman Login with Password).
- Suite berjalan serial (`parallel: false`); state global yang diubah: jam server uji dan jam browser/perangkat uji (diatur bersama), dipulihkan di hook `after`.
- Titik waktu: batas idle 15 menit; tiap tab menghitung mundur sendiri dari waktu kedaluwarsa terakhir yang diketahuinya (`AUTHSES-LOGIC-02d`).
- Akun yang dipakai: user uji masing-masing TC (bukan akun aktor) di Browser A (Tab A dan Tab B).

## Test Steps

### TC-AUTH-SES-53: Tab dengan sesi masih valid tidak menampilkan Dialog Session Expired

1. Buka konteks Browser A baru lalu buat sesi web aktif `Taufik Wibowo` lewat login API (seeding BE) → sesi berstatus Active
2. Di Browser A buka dua tab (Tab A dan Tab B) pada Portal — Product Hub → kedua tab menampilkan Portal — Product Hub
3. Di Tab A gerakkan mouse (aktivitas berkala ke-1)
4. Majukan jam server uji dan jam browser/perangkat uji bersama 4 menit
5. Di Tab A gerakkan mouse (aktivitas berkala ke-2)
6. Majukan jam server uji dan jam browser/perangkat uji bersama 4 menit
7. Di Tab A gerakkan mouse (aktivitas berkala ke-3)
8. Majukan jam server uji dan jam browser/perangkat uji bersama 4 menit
9. Di Tab A gerakkan mouse (aktivitas berkala ke-4)
10. Majukan jam server uji dan jam browser/perangkat uji bersama 4 menit lagi (total 16 menit sejak aktivitas terakhir di Tab B; Tab A tetap aktif tiap beberapa menit)
11. Pindah ke Tab B dan amati
12. Verifikasi Tab B tidak menampilkan Dialog Session Expired karena sesi masih valid
13. Verifikasi Sesi dipakai bersama oleh kedua tab (Tab B memakai sesi Active yang sama dengan Tab A, tanpa login ulang)

### TC-AUTH-SES-54: Hitungan mundur tab habis tetapi sesi sudah diperpanjang tab lain memperbarui waktu kedaluwarsa tanpa dialog

14. Buka konteks Browser A baru lalu buat sesi web aktif `Mega Nugroho` lewat login API (seeding BE) → sesi berstatus Active
15. Di Browser A buka dua tab (Tab A dan Tab B) pada Portal — Product Hub → kedua tab menampilkan Portal — Product Hub
16. Mulai perekaman request jaringan per tab (Tab A dan Tab B) dan pemantauan pesan antar-tab di sisi client
17. Majukan jam server uji dan jam browser/perangkat uji bersama 10 menit
18. Di Tab A gerakkan mouse pada menit ke-10 sehingga sesi diperpanjang
19. Biarkan Tab B tanpa aktivitas dan majukan jam server uji dan jam browser/perangkat uji bersama 5 menit lagi sampai hitungan mundur lokalnya habis (15 menit sejak aktivitas terakhir di Tab B)
20. Amati Tab B dan perekaman request jaringan
21. Verifikasi Tab B mengecek server satu kali saat hitungannya habis
22. Verifikasi Server menyatakan sesi masih valid
23. Verifikasi Waktu kedaluwarsa Tab B diperbarui
24. Verifikasi Tidak ada dialog yang tampil di Tab B
25. Verifikasi Tab B tidak memakai mekanisme sinkronisasi antar-tab di sisi client (pembaruan waktu kedaluwarsa Tab B berasal dari respons cek server, bukan dari pesan antar-tab)

### TC-AUTH-SES-55: Dua tab kena Session Expired lalu satu tab login ulang dan tab lain Refresh tanpa me-logout sesi baru

26. Buka konteks Browser A baru lalu buat sesi web aktif `Reza Maulana` lewat login API (seeding BE) → sesi berstatus Active
27. Di Browser A buka dua tab (Tab A dan Tab B) pada Portal — Product Hub → kedua tab menampilkan Portal — Product Hub
28. Biarkan Browser A tanpa aktivitas dan majukan jam server uji dan jam browser/perangkat uji bersama 10 menit → Toast Idle Warning tampil
29. Majukan jam server uji dan jam browser/perangkat uji bersama 6 menit lagi (idle 16 menit) → Tab A dan Tab B sama-sama menampilkan Dialog Session Expired
30. Di Tab A klik [Refresh] → halaman Login with Password tampil
31. Di Tab A login ulang dengan email `rezamaulana+{runId}-019@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil
32. Verifikasi Tab A masuk Portal — Product Hub
33. Verifikasi Sesi baru di Tab A berstatus Active
34. Di Tab B klik [Refresh]
35. Verifikasi Tab B tetap di halaman
36. Verifikasi Tab B ter-refresh
37. Verifikasi Tab B tanpa login ulang
38. Verifikasi Sesi baru dari Tab A tidak di-logout oleh klik [Refresh] di Tab B
39. Verifikasi Tab B tidak menampilkan dialog lain

### TC-AUTH-SES-49: Refresh pada Dialog Session Expired saat sesi sudah valid tetap di halaman

40. Buka konteks Browser A baru lalu buat sesi web aktif `Joko Firmansyah` lewat login API (seeding BE) → sesi berstatus Active
41. Di Browser A buka dua tab (Tab A dan Tab B) pada Portal — Product Hub → kedua tab menampilkan Portal — Product Hub
42. Biarkan Browser A tanpa aktivitas dan majukan jam server uji dan jam browser/perangkat uji bersama 10 menit → Toast Idle Warning tampil
43. Majukan jam server uji dan jam browser/perangkat uji bersama 6 menit lagi (idle 16 menit) → Tab A dan Tab B sama-sama menampilkan Dialog Session Expired
44. Di Tab A klik [Refresh] → halaman Login with Password tampil
45. Di Tab A ketik email `jokofirmansyah+{runId}-019@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil dengan sesi baru Active
46. Pindah ke Tab B → Tab B masih menampilkan Dialog Session Expired
47. Di Tab B klik [Refresh]
48. Verifikasi Tab B tetap di halaman yang sama
49. Verifikasi Halaman Tab B ter-refresh dengan sesi yang ada
50. Verifikasi Tab B tidak diarahkan ke halaman Login
51. Verifikasi Sesi baru dari Tab A tidak di-logout

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness c (multi-tab) dan d (time-travel). Spec ini 51 langkah karena seluruh TC-nya satu kelas harness (c, dua tab dalam satu konteks browser) dan tiap TC mandiri dengan user dan sesi sendiri; memecahnya hanya menambah overhead seeding dan pengaturan jam yang sama.
- Urutan mengikuti TC sumber; tiap TC memakai user dan sesi sendiri yang dibuat di awal TC-nya, sehingga tidak saling bergantung. TC-AUTH-SES-55 dan 49 ditaruh di akhir karena membuat sesi baru dan mengakhiri sesi lama; TC-AUTH-SES-49 memakai user `Joko Firmansyah` sendiri sehingga tidak bergantung pada state TC-AUTH-SES-55.
- Dependensi (S-04): TC-AUTH-SES-55 berdependensi pada TC-AUTH-SES-46 (idle sampai Dialog Session Expired); langkah penyiapan 1 dan 2 TC-AUTH-SES-46 disalin sebagai langkah 28-29 untuk dua tab. TC-AUTH-SES-49 berdependensi pada TC-AUTH-SES-55; langkah penyiapan (kedua tab kena Session Expired, Tab A [Refresh] dan login ulang) disalin sebagai langkah 42-45 dengan user sendiri. Asersi TC-AUTH-SES-46 (Toast, isi dialog, halaman beku) diuji di spec `TC-AUTH-SES-E2E-016-idle-timeout-dan-toast-warning-web`.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): membuka konteks Browser A baru dan membuat sesi seed; membuka dua tab di Portal — Product Hub; memulai perekaman request jaringan; berpindah antar Tab A dan Tab B.
- Pembagian TC lintas spec: Expected butir c TC-AUTH-SES-49 ("tidak ada entri log baru di `Global Settings > Activity Log > Session` dan User Log `Joko Firmansyah`") adalah asersi absence dan tidak ditulis di spec ini (S-05); asersinya ada di spec absence `TC-AUTH-SES-E2E-066-absence-duplicate-login-dan-session-expired`. TC-AUTH-SES-50 (Refresh saat sesi masih expired) ada di spec `TC-AUTH-SES-E2E-018-refresh-pada-dialog-session-expired`.
- Temuan untuk QA: (1) TC-AUTH-SES-53 menulis "aktivitas secara berkala" dan "tiap beberapa menit" tanpa interval; spec memakai aktivitas mouse di Tab A tiap 4 menit (sisa waktu Tab A tidak pernah mendekati batas). (2) TC-AUTH-SES-54 Expected c "tidak memakai mekanisme sinkronisasi antar-tab di sisi client" tidak menyebut cara mengamatinya; spec memakai pemantauan pesan antar-tab dan perekaman request jaringan per tab sebagai kebutuhan teknis di Prerequisites. (3) TC-AUTH-SES-54 menyebut "cek server" tanpa endpoint; OpenAPI modul hanya memuat heartbeat `PUT /v2/iam/auth/sessions/heartbeat`, sehingga spec menulis "request cek server" tanpa menyebut endpoint. (4) TC-AUTH-SES-55 Expected c dan butir sesi Active butuh pembacaan status sesi dari sisi BE yang tidak punya endpoint di OpenAPI modul; kebutuhan ditulis di Prerequisites. (5) TC-AUTH-SES-53, 54, 55 hanya menyebut "majukan waktu server", sedangkan hitung mundur dijalankan di client tiap tab; spec menambahkan kebutuhan jam browser uji ikut dimajukan di Prerequisites. (6) TC-AUTH-SES-55 dan 49 langkah 2 "login ulang dengan password yang benar" tidak menyebut reCAPTCHA; spec mengikuti TC dan mengandalkan reCAPTCHA mode uji.
