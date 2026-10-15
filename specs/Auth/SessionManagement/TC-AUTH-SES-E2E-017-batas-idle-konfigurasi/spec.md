---
id: TC-AUTH-SES-E2E-017-batas-idle-konfigurasi
title: "Batas Idle Konfigurasi General Settings"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-59
  - TC-AUTH-SES-60
  - TC-AUTH-SES-283
  - TC-AUTH-SES-217
  - TC-AUTH-SES-218
coverage:
  web: automated
---

# Batas Idle Konfigurasi General Settings

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`, satu akun per Client uji (Tabel Data Uji Pre-setup #1): `namaCompany` Client `Alpha Logistik` untuk TC-AUTH-SES-60, 283, 217, 218 dan `namaCompany` Client `Default30` untuk TC-AUTH-SES-59. Login akun aktor Client `Alpha Logistik` di Browser Admin dilakukan di hook `before` (dipakai langkah ubah batas idle TC-AUTH-SES-217).
- Seeding (hook `before`, lewat API oleh akun aktor di atas): lima user profil BASE (user Activated, Active ON; MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-59: `Irfan Kusuma` (`irfankusuma+{runId}-017@qwertysystem.net`), milik Client `Default30` (Tabel Data Uji Pre-setup #15: batas idle tidak diubah, default 30 menit)
  - TC-AUTH-SES-60: `Tari Permata` (`taripermata+{runId}-017@qwertysystem.net`), milik Client `Alpha Logistik`
  - TC-AUTH-SES-283: `Wulan Damayanti` (`wulandamayanti+{runId}-017@qwertysystem.net`), milik Client `Alpha Logistik`
  - TC-AUTH-SES-217: `Maya Santoso` (`mayasantoso+{runId}-017@qwertysystem.net`), milik Client `Alpha Logistik`
  - TC-AUTH-SES-218: `Fajar Kusuma` (`fajarkusuma+{runId}-017@qwertysystem.net`), milik Client `Alpha Logistik`
- Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5 dan #11) berbasis batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5. Spec ini mengubah batas idle Client `Alpha Logistik` pada TC-AUTH-SES-217 (disetel 30 menit lewat seeding BE, lalu diubah ke 15 menit lewat UI) dan TC-AUTH-SES-218 (disetel opsi 8 jam lewat seeding BE oleh akun aktor sebelum login). Hook `after` mengembalikan batas idle Client `Alpha Logistik` ke 15 menit. Efek samping yang tercatat: `Last Updated` pada `Global Settings > General Settings` Client `Alpha Logistik` berubah.
- Sesi web aktif (status Active) di Browser A dibuat lewat login API oleh langkah seeding di awal TC masing-masing (TC-AUTH-SES-59, 283, 217), bukan di hook `before`: jam server uji dan jam browser/perangkat uji dimajukan kumulatif sehingga sesi yang dibuat lebih awal akan menua. TC-AUTH-SES-283 memakai Chrome on Windows. TC-AUTH-SES-60 dan 218 membuat sesi lewat langkah login di halaman Login with Password. TC-AUTH-SES-217 memakai Browser A (sesi lama) dan Browser B (login baru).
- Batas idle dibaca dari General Settings saat sesi dibuat (`AUTHSES-LOGIC-02g`): perubahan batas idle di TC-AUTH-SES-217 hanya berlaku untuk sesi yang dibuat sesudahnya.
- Hook `after`: akhiri semua sesi seed, tutup konteks Browser A dan B, kembalikan batas idle Client `Alpha Logistik` ke 15 menit, kembalikan jam server uji dan jam browser uji ke waktu nyata, hapus kelima user. Hook ini tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness d: time-travel): jam server uji dan jam browser/perangkat uji (timer idle dan Toast di client) dapat dimajukan bersama dengan presisi detik, dibekukan pada nilai yang diminta, diset ke waktu absolut (waktu aktivitas terakhir ditambah 14 menit 59 detik pada TC-AUTH-SES-283), dan dipulihkan ke waktu nyata; perekaman request jaringan di Browser A untuk heartbeat `PUT /v2/iam/auth/sessions/heartbeat` (TC-AUTH-SES-217); konteks Browser A, Browser B, dan Browser Admin bersamaan; reCAPTCHA mode uji di environment (halaman Login with Password); pembacaan status sesi Active user uji dari sisi BE untuk TC-AUTH-SES-283, disediakan tim FE/BE tanpa endpoint tertentu.
- Suite berjalan serial (`parallel: false`); state global yang diubah: jam server uji, jam browser/perangkat uji (diatur bersama), dan batas idle Client `Alpha Logistik`, dipulihkan di hook `after`.
- Karena jam bergeser pada TC-AUTH-SES-59, 60, dan 283 melewati batas idle 15 menit sesi hook `before`, Browser Admin login ulang sebagai akun aktor Client `Alpha Logistik` tepat sebelum bagian admin TC-AUTH-SES-217.
- Akun yang dipakai: user uji masing-masing TC di Browser A (dan Browser B pada TC-AUTH-SES-217); Browser Admin memakai akun aktor Client `Alpha Logistik`.

## Test Steps

### TC-AUTH-SES-59: Client tanpa konfigurasi idle memakai default 30 menit

1. Buka konteks Browser A baru lalu buat sesi web aktif `Irfan Kusuma` (Client `Default30`) lewat login API (seeding BE) → sesi berstatus Active
2. Di Browser A buka Portal — Product Hub → halaman Portal — Product Hub tampil
3. Biarkan Browser A tanpa aktivitas dan majukan jam server uji dan jam browser/perangkat uji bersama 29 menit → amati
4. Verifikasi Pada idle 29 menit Dialog Session Expired belum tampil
5. Majukan jam server uji dan jam browser/perangkat uji bersama sampai idle 31 menit → amati
6. Verifikasi Pada idle 31 menit Dialog "Session Expired" tampil

### TC-AUTH-SES-60: Batas idle yang dikonfigurasi 15 menit berlaku pada sesi baru

7. Tutup konteks Browser A TC sebelumnya (hapus sesi login browser), buka konteks Browser A baru (tanpa sesi login)
8. Di Browser A buka halaman `Auth > Login with Password` → halaman Login with Password tampil
9. Ketik email `taripermata+{runId}-017@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil
10. Biarkan Browser A tanpa aktivitas dan majukan jam server uji dan jam browser/perangkat uji bersama 14 menit
11. Verifikasi Dialog Session Expired tidak tampil pada idle 14 menit
12. Majukan jam server uji dan jam browser/perangkat uji bersama 2 menit lagi sampai idle 16 menit → amati
13. Verifikasi Dialog "Session Expired" tampil pada idle 16 menit
14. Verifikasi Nilai batas tidak di-hardcode ke 30 menit (dialog tampil pada 16 menit, bukan 30 menit)

### TC-AUTH-SES-283: Idle 14 menit 59 detik pada batas 15 menit belum kedaluwarsa

15. Buka konteks Browser A baru (Chrome on Windows) lalu buat sesi web aktif `Wulan Damayanti` lewat login API (seeding BE) → sesi berstatus Active
16. Di Browser A buka Portal — Product Hub dan catat waktu server saat halaman tampil sebagai waktu aktivitas terakhir → halaman Portal — Product Hub tampil
17. Atur jam server uji dan jam browser/perangkat uji bersama secara absolut ke waktu aktivitas terakhir (dicatat di langkah 16) ditambah tepat 14 menit 59 detik, lalu bekukan keduanya di nilai itu, tanpa aktivitas di Browser A
18. Amati Browser A
19. Verifikasi Dialog Session Expired belum tampil
20. Verifikasi Sesi masih Active
21. Verifikasi Toast Idle Warning sudah tampil (sisa waktu kurang dari 5 menit)
22. Pulihkan jam server uji dan jam browser/perangkat uji ke waktu nyata (keduanya bersama)

### TC-AUTH-SES-217: Perubahan batas idle di General Settings dan pengaruhnya pada sesi berjalan

23. Setel batas idle Client `Alpha Logistik` menjadi 30 menit lewat seeding BE oleh akun aktor Client `Alpha Logistik`
24. Buka konteks Browser A baru lalu buat sesi web aktif `Maya Santoso` lewat login API (seeding BE) → sesi berstatus Active dengan batas idle 30 menit
25. Di Browser A buka Portal — Product Hub → halaman Portal — Product Hub tampil
26. Di Browser Admin login ulang sebagai `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Client `Alpha Logistik`) dengan password `Spectra.env.GS_TC_PASSWORD`
27. Di Browser Admin (akun aktor Client `Alpha Logistik`) ubah Session Idle Timeout Client `Alpha Logistik` menjadi 15 menit di `Global Settings > General Settings` dan simpan
28. Pindah ke Browser A dan mulai perekaman request jaringan heartbeat
29. Gerakkan mouse di Browser A secara berkala sampai heartbeat berikutnya terkirim
30. Biarkan Browser A tanpa aktivitas dan majukan jam server uji dan jam browser/perangkat uji bersama 16 menit → amati Browser A
31. Verifikasi Sesi berjalan tetap memakai batas lama 30 menit: tidak ada Dialog Session Expired pada idle 16 menit
32. Majukan jam server uji dan jam browser/perangkat uji bersama sampai idle 31 menit → amati Browser A
33. Verifikasi Dialog Session Expired tampil pada idle 31 menit (perubahan batas tidak retroaktif)
34. Buka konteks Browser B baru lalu buka halaman `Auth > Login with Password` → halaman Login with Password tampil
35. Ketik email `mayasantoso+{runId}-017@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil di Browser B (sesi baru dibuat sesudah perubahan)
36. Majukan jam server uji dan jam browser/perangkat uji bersama 16 menit tanpa aktivitas → amati Browser B
37. Verifikasi Sesi baru yang dibuat sesudah perubahan memakai 15 menit: Dialog Session Expired tampil pada idle 16 menit di Browser B
38. Biarkan Browser B tanpa aktivitas dan majukan jam server uji dan jam browser/perangkat uji bersama 16 menit lagi

### TC-AUTH-SES-218: Nilai batas idle mengikuti opsi di General Settings tanpa validasi ulang di modul ini

39. Setel batas idle Client `Alpha Logistik` ke opsi 8 jam lewat seeding BE oleh akun aktor Client `Alpha Logistik`
40. Tutup konteks Browser A TC sebelumnya (hapus sesi login browser), buka konteks Browser A baru lalu buka halaman `Auth > Login with Password` → halaman Login with Password tampil
41. Ketik email `fajarkusuma+{runId}-017@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil
42. Biarkan Browser A tanpa aktivitas dan majukan jam server uji dan jam browser/perangkat uji bersama 7 jam 55 menit
43. Verifikasi Toast Idle Warning tampil pada sisa 5 menit (idle 7 jam 55 menit)
44. Majukan jam server uji dan jam browser/perangkat uji bersama sampai 8 jam 01 menit
45. Verifikasi Dialog "Session Expired" tampil pada idle 8 jam 01 menit

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness d (time-travel).
- Urutan mengikuti TC sumber dengan variasi dari ringan ke yang mengubah state global: TC-AUTH-SES-59 (Client lain), 60 dan 283 (Alpha 15 menit), lalu 217 dan 218 yang mengubah batas idle Client `Alpha Logistik`. TC-AUTH-SES-218 paling akhir karena mengubah batas ke 8 jam; pemulihan ke 15 menit di hook `after` (S-05, S-06, S-10).
- Dependensi (S-04): TC-AUTH-SES-283 berdependensi pada TC-AUTH-SES-47 sebagai pasangan batas (idle tepat 15 menit 00 detik kedaluwarsa); keduanya berdiri sendiri dan tidak memakai hasil satu sama lain. TC-AUTH-SES-47 ada di spec `TC-AUTH-SES-E2E-016-idle-timeout-dan-toast-warning-web`.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): menutup konteks Browser A TC sebelumnya (hapus sesi login browser, langkah 7 dan 40) dan membuka konteks browser baru serta membuat sesi seed; membuka Portal — Product Hub; memulai perekaman request jaringan heartbeat; pindah antar Browser A, Browser B, dan Browser Admin; mencatat waktu aktivitas terakhir (langkah 16) dan memulihkan jam setelah batas eksak TC-AUTH-SES-283 (langkah 22); login ulang Browser Admin (langkah 26); setelan batas idle lewat seeding BE pada TC-AUTH-SES-217 dan 218.
- TC-AUTH-SES-217 langkah 5 (spec: langkah 38) tidak punya Expected sendiri; spec menuliskannya sebagai aksi tanpa `Verifikasi`.
- Temuan untuk QA: (1) Tabel Data Uji Pre-setup #1 hanya menyebut satu akun aktor `{namaCompany}`, sedangkan TC-AUTH-SES-59 memakai Client `Default30`; spec memakai akun aktor `namaCompany` Client `Default30` untuk seeding user itu. (2) TC-AUTH-SES-217 langkah 4 sudah memuat "majukan waktu server 16 menit tanpa aktivitas" dan langkah 5 mengulanginya ("Biarkan tanpa aktivitas dan majukan waktu server 16 menit") tanpa Expected tambahan; spec memasukkan keduanya apa adanya. (3) TC-AUTH-SES-217 tidak menyebut toast atau indikator sukses saat menyimpan Session Idle Timeout di General Settings, jadi tidak ada `Verifikasi` untuk penyimpanan. (4) TC-AUTH-SES-217 Precondition b menyebut batas idle 30 menit untuk Client `Alpha Logistik`, sedangkan Tabel Data Uji Pre-setup #5 dan #11 menetapkan 15 menit; spec menyetel 30 menit lewat seeding BE di awal TC-AUTH-SES-217. (5) TC-AUTH-SES-217 "gerakkan mouse sampai heartbeat berikutnya terkirim" tidak menyebut berapa lama; spec menggerakkan mouse berkala sampai satu request heartbeat terekam. (6) TC-AUTH-SES-60 dan 218 menyebut login tanpa menyebut widget reCAPTCHA pada halaman Login with Password; spec mengikuti TC dan mengandalkan reCAPTCHA mode uji. (7) TC-AUTH-SES-283 butuh pembacaan status sesi "Active" dari sisi BE yang tidak punya endpoint di OpenAPI modul; kebutuhan ditulis di Prerequisites. (8) TC-AUTH-SES-60 Expected a menyebut "tidak tampil pada idle 14 menit" tetapi Langkah Uji hanya "majukan 16 menit"; spec menambah langkah majukan 14 menit lebih dulu. (9) TC-AUTH-SES-217, 218, dan semua TC jam server menyebut "majukan waktu server" saja; kebutuhan jam browser uji ikut dimajukan ditulis di Prerequisites. (10) TC-AUTH-SES-283 memakai batas presisi detik (14 menit 59 detik, margin 1 detik); detik nyata antara memajukan jam dan pengamatan menambah idle melewati 15 menit sehingga dialog Session Expired bisa muncul bukan karena perilaku yang diuji. Spec mengatur jam server dan jam browser/perangkat bersama secara absolut ke waktu aktivitas terakhir ditambah 14 menit 59 detik dan membekukannya (bagian 6), lalu memulihkannya di langkah 22; jam server uji perlu dapat diset absolut atau dibekukan.
- Ukuran: spec memuat 45 langkah (melebihi sekitar 35) karena lima TC satu kelas harness (time-travel) berada dalam satu spec; tiap TC memakai user dan sesi sendiri, sehingga bagian berikutnya tetap bermakna meski TC lain di spec ini tidak dijalankan.
