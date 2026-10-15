---
id: TC-AUTH-SES-E2E-053-duplicate-login-dari-biometric-re-login
title: "Duplicate Login Attempt dari Biometric Re-login: Dialog, Cancel, Confirm, dan Urutan Layar"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-168
  - TC-AUTH-SES-169
  - TC-AUTH-SES-296
  - TC-AUTH-SES-328
  - TC-AUTH-SES-295
coverage:
  web: automated
  mobile: automated
---

# Duplicate Login Attempt dari Biometric Re-login: Dialog, Cancel, Confirm, dan Urutan Layar

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi mobile TAG Samurai (Android) pada perangkat Android uji B (Tabel Data Uji Pre-setup #10: hardware biometric, sidik jari terdaftar di OS) sebagai perangkat biometric re-login, dan perangkat Android uji A sebagai perangkat sesi mobile lama. Web: Browser A (Chrome on Windows) untuk TC-AUTH-SES-169 dan Browser Admin untuk TC-AUTH-SES-295.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): empat user milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-168: `Yoga Ramadhan` (`yogaramadhan+{runId}-053@qwertysystem.net`), profil BIO (Tabel Data Uji Pre-setup #9)
  - TC-AUTH-SES-169: `Ayu Wulandari` (`ayuwulandari+{runId}-053@qwertysystem.net`), profil BIO
  - TC-AUTH-SES-296: `Irfan Ramadhan` (`irfanramadhan+{runId}-053@qwertysystem.net`), profil BIOPOLMFA (Tabel Data Uji Pre-setup #24: Agreement dan MFA terpicu sekaligus; Authenticator terdaftar); kondisi Agreement dan MFA terpicu diterapkan sesudah enrollment dan seed sesi A (langkah 16)
  - TC-AUTH-SES-328 dan TC-AUTH-SES-295: `Nadia Pratama` (`nadiapratama+{runId}-053@qwertysystem.net`), profil BIO; satu user dipakai dua TC berurutan
- Sesi mobile aktif di perangkat Android uji A selalu dibuat sesudah enrollment di perangkat B selesai dan sesi platform hasil login enroll diakhiri, supaya login enroll di B tidak memunculkan Dialog Duplicate Login Attempt: untuk `Yoga Ramadhan` di-seed di hook `before` lewat login API (platform mobile, ID device perangkat A) sesudah enrollment di B; untuk `Irfan Ramadhan` di-seed lewat login API pada langkah penghubung 16 sesudah enrollment di B (langkah 15); untuk `Nadia Pratama` dibuat nyata lewat login di aplikasi pada perangkat A dengan [Not now] pada Prompt Enable Biometric (langkah penghubung 28 sebelum TC-AUTH-SES-295; cara menyiapkan: Tabel Data Uji Pre-setup #28), karena TC-AUTH-SES-295 mengasersi Dialog Logged Out di perangkat A.
- Kondisi "sudah enroll biometric di perangkat Android uji B, tanpa sesi platform aktif di perangkat itu" per user disiapkan lewat alur Prompt Enable Biometric (login, [Enable], lulus verifikasi sidik jari; TC-AUTH-SES-14; cara menyiapkan: Tabel Data Uji Pre-setup #29): user TC pertama (`Yoga Ramadhan`) di hook `before`, user TC berikutnya lewat langkah penghubung `Siapkan enrollment`, karena token biometric lokal dan email cache lokal disimpan per perangkat. Sesi platform hasil login enroll diakhiri lewat API yang disediakan tim FE/BE (tanpa menghapus token biometric lokal, bukan lewat Log Out di UI). Untuk `Irfan Ramadhan` (profil BIOPOLMFA) enrollment disiapkan sebelum kondisi Agreement dan MFA diterapkan pada user itu.
- Sesi web aktif Browser A untuk TC-AUTH-SES-169 dibuat lewat login pada langkah TC (Chrome on Windows).
- Proxy jaringan (Tabel Data Uji Pre-setup #18) menangkap request relogin di perangkat B untuk membandingkan token biometric sebelum dan sesudah [Cancel] (TC-AUTH-SES-328). Aplikasi authenticator uji (TOTP) (Tabel Data Uji Pre-setup #18) menghasilkan kode TOTP yang benar untuk Authenticator `Irfan Ramadhan` (TC-AUTH-SES-296).
- Hook `after`: hapus data aplikasi pada perangkat Android uji A dan B; akhiri semua sesi seed (mobile dan web); tutup konteks Browser A dan Browser Admin; hapus keempat user. Pembersihan tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: user uji masing-masing TC pada aplikasi mobile (dan Browser A untuk TC-AUTH-SES-169); akun aktor Total Control (Global Settings) di Browser Admin untuk TC-AUTH-SES-295, sudah login di hook `before`.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`); state global yang diubah: perangkat fisik Android uji A dan B dipakai bersama (data aplikasi, token biometric lokal, dan sesi mobile), dipulihkan di hook `after`.
- Kemampuan teknis (kelas harness d: hardware biometrik dan authenticator TOTP): driver otomasi Android (aplikasi native) untuk dua perangkat; menghapus app dari recent apps lalu membukanya kembali; menutup paksa dan menghapus data aplikasi; simulasi sensor sidik jari pada OS biometric prompt (sidik jari terdaftar lulus); proxy jaringan; aplikasi authenticator uji TOTP; login API dengan platform mobile dan ID device tertentu; API yang disediakan tim FE/BE untuk mengakhiri sesi platform hasil login enroll tanpa menghapus token biometric lokal (Tabel Data Uji Pre-setup #29); reCAPTCHA mode uji di environment untuk login web (halaman Login with Password).

## Test Steps

### TC-AUTH-SES-168: Biometric re-login saat sesi mobile aktif di device lain memunculkan Dialog Duplicate Login Attempt

1. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
2. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → Dialog muncul
3. Verifikasi Dialog "Duplicate Login Attempt" tampil di perangkat B
4. Verifikasi Biometric tidak mem-bypass Limit Login: login tidak dilanjutkan tanpa keputusan pengguna pada dialog
5. Verifikasi Sesi baru belum dibuat sebelum [Confirm]: aplikasi tetap pada dialog dan belum masuk Portal — Product Hub
6. Ketuk [Cancel] pada Dialog Duplicate Login Attempt

### TC-AUTH-SES-169: Biometric re-login mobile saat sesi web aktif diizinkan

7. Tutup paksa aplikasi mobile di perangkat Android uji B, hapus data aplikasi, lalu siapkan enrollment `ayuwulandari+{runId}-053@qwertysystem.net` sebagai user yang sudah enroll biometric di perangkat (email cache lokal = email itu; Tabel Data Uji Pre-setup #29) tanpa sesi platform aktif
8. Di Browser A (Chrome on Windows) login dengan `ayuwulandari+{runId}-053@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil
9. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
10. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
11. Verifikasi App masuk Portal — Product Hub
12. Verifikasi Tidak ada Dialog Duplicate Login Attempt
13. Pindah ke Browser A dan klik menu apa pun
14. Verifikasi Sesi web di Browser A tetap Active (halaman merespons dan tidak ada Dialog Logged Out)

### TC-AUTH-SES-296: Urutan biometric re-login: Agreement, MFA, lalu Dialog Duplicate Login Attempt

15. Tutup paksa aplikasi mobile di perangkat Android uji B, hapus data aplikasi, lalu siapkan enrollment `irfanramadhan+{runId}-053@qwertysystem.net` sebagai user yang sudah enroll biometric di perangkat (email cache lokal = email itu; Tabel Data Uji Pre-setup #29) tanpa sesi platform aktif di perangkat itu
16. Seed sesi mobile aktif `Irfan Ramadhan` di perangkat Android uji A lewat login API (platform mobile, ID device perangkat A), lalu terapkan kondisi Agreement dan MFA terpicu pada `Irfan Ramadhan` (disediakan tim FE/BE)
17. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
18. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → layar Confirm to Continue tampil
19. Verifikasi Layar Confirm to Continue tampil lebih dulu
20. Centang checkbox Agreement lalu ketuk [Continue ➔] → halaman MFA tampil
21. Verifikasi Halaman MFA tampil setelah Agreement dikonfirmasi
22. Ketik kode TOTP yang benar (dari aplikasi authenticator uji) pada halaman MFA → Dialog Duplicate Login Attempt muncul
23. Verifikasi Dialog Duplicate Login Attempt tampil setelah MFA
24. Verifikasi Urutan layar: Confirm to Continue, lalu halaman MFA, lalu Dialog Duplicate Login Attempt (langkah 19, 21, dan 23)
25. Verifikasi Sesi baru belum dibuat sebelum [Confirm]: aplikasi tetap pada dialog dan belum masuk Portal — Product Hub
26. Ketuk [Cancel] pada Dialog Duplicate Login Attempt

### TC-AUTH-SES-328: Cancel pada Dialog Duplicate Login Attempt dari biometric re-login tidak membuat sesi, tidak mencatat, dan tidak merotasi token

27. Tutup paksa aplikasi mobile di perangkat Android uji B, hapus data aplikasi, lalu siapkan enrollment `nadiapratama+{runId}-053@qwertysystem.net` sebagai user yang sudah enroll biometric di perangkat (email cache lokal = email itu; Tabel Data Uji Pre-setup #29) tanpa sesi platform aktif di perangkat itu
28. Di perangkat Android uji A login dengan `nadiapratama+{runId}-053@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, ketuk [Not now] pada Prompt Enable Biometric → app masuk Portal — Product Hub (sesi mobile aktif di perangkat A; Tabel Data Uji Pre-setup #28)
29. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
30. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → Dialog Duplicate Login Attempt muncul (proxy mencatat token biometric pada request relogin)
31. Ketuk [Cancel]
32. Verifikasi Tidak ada sesi baru di perangkat B (aplikasi tidak masuk Portal — Product Hub)
33. Verifikasi Sesi di perangkat A tetap Active (ketuk layar perangkat A, tidak ada Dialog Logged Out)
34. Hapus app dari recent apps di perangkat B lalu buka kembali aplikasi mobile → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
35. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → Dialog Duplicate Login Attempt muncul
36. Verifikasi Biometric re-login tetap berjalan dengan token biometric yang sama (token pada request relogin ini sama dengan langkah 30, tidak dirotasi oleh Cancel)
37. Verifikasi Dialog Duplicate Login Attempt muncul kembali
38. Di Browser Admin buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` milik `Nadia Pratama`, lalu catat jumlah entri `Login with biometric` dan `Logged out (new device login)` sebagai baseline

### TC-AUTH-SES-295: Confirm pada Dialog Duplicate Login Attempt dari biometric re-login mengaktifkan sesi baru dan mencatat dua event

39. Hapus app dari recent apps di perangkat B lalu buka kembali aplikasi mobile → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
40. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → Dialog Duplicate Login Attempt muncul
41. Ketuk [Confirm]
42. Verifikasi App di perangkat B masuk Portal — Product Hub
43. Verifikasi Sesi mobile baru di perangkat B berstatus Active
44. Pindah ke perangkat A (ketuk layar) → Dialog muncul
45. Verifikasi Sesi lama di perangkat A menerima Dialog Logged Out
46. Pindah ke Browser Admin dan buka `Global Settings > Activity Log > Session`
47. Verifikasi Activity Log > Session mencatat tepat satu entri `Login with biometric` (Login, Success) baru untuk `Nadia Pratama` (selisih jumlah dibanding baseline langkah 38)
48. Verifikasi Activity Log > Session mencatat tepat satu entri `Logged out (new device login)` (Logout) baru untuk sesi lama (selisih jumlah dibanding baseline langkah 38)
49. Buka `Global Settings > User > Detail > User Log` untuk `Nadia Pratama`
50. Verifikasi User Log mencatat tepat satu entri `Login with biometric` (Login, Success) baru (selisih jumlah dibanding baseline langkah 38)
51. Verifikasi User Log mencatat tepat satu entri `Logged out (new device login)` (Logout) baru untuk sesi lama (selisih jumlah dibanding baseline langkah 38)
52. Verifikasi Sesi lama di perangkat A berstatus Force Logged Out (entri `Logged out (new device login)` mencatat penghentian sesi lama)

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan (S-05, S-10): urutan di spec ini TC-AUTH-SES-168, 169, 296, 328, 295 (urutan TC sumber 295, 296, 328, 168, 169). TC-AUTH-SES-168 menjadi screening dialog di awal (dependensi TC-AUTH-SES-295 dan 328, langkah 1 sampai 2 disalin di keduanya sesuai S-04); TC-AUTH-SES-295 mengonfirmasi dialog sehingga mengakhiri sesi lama di perangkat A dan menaruh sesi baru di perangkat B; ditaruh paling akhir.
- TC-AUTH-SES-296 berdependensi pada TC-AUTH-SES-163 (Agreement lalu MFA lalu Portal); langkah 17 sampai 22 menyalin langkah 1 sampai 4 TC itu, dan hanya bagian setelah MFA yang berbeda (S-04).
- TC-AUTH-SES-328 dan TC-AUTH-SES-295 memakai satu user `Nadia Pratama` berurutan sesuai TC sumber. Kondisi akhir TC-AUTH-SES-328 sama dengan kondisi awal TC-AUTH-SES-295, sehingga user tidak di-seed ulang.
- Pembagian TC lintas spec: TC-AUTH-SES-328 Expected b (tidak ada entri `Login with biometric` maupun `Logged out (new device login)`) dan langkah 4 (membuka Activity Log dan User Log) adalah asersi absence dan ditaruh di spec absence `TC-AUTH-SES-E2E-070-absence-biometric`; spec ini tidak mengasersinya (S-05).
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): menyiapkan enrollment user TC berikutnya (langkah 7, 15, 27; Tabel Data Uji Pre-setup #29); login web dan login mobile perangkat A untuk menyiapkan sesi (langkah 8 dan 28; Tabel Data Uji Pre-setup #28); seed sesi mobile `Irfan Ramadhan` di perangkat A sesudah enrollment (langkah 16); [Cancel] pada dialog untuk menutup state TC sebelumnya (langkah 6 dan 26); menghapus app dari recent apps lalu membuka kembali aplikasi (langkah 34 dan 39); pindah antar perangkat, browser, dan menu.
- Temuan untuk QA: (1) TC-AUTH-SES-168, 169, 296, 328, 295 menyebut "sudah enroll biometric" dengan rujukan Pre-setup #29 tetapi tanpa langkah penyiapan di Langkah Uji, sementara satu perangkat hanya menyimpan satu token dan email cache lokal; langkah penghubung penyiapan enrollment ditambahkan sebagai kebutuhan teknis dan perlu konfirmasi QA (S-15). (2) TC-AUTH-SES-295 Expected b mensyaratkan Dialog Logged Out di perangkat A, sehingga sesi A untuk `Nadia Pratama` dibuat lewat login nyata di aplikasi (Pre-setup #28, termasuk [Not now] pada Prompt Enable Biometric) sesudah enrollment di B dan pengakhiran sesi enroll lewat API BE (Pre-setup #29). (3) TC-AUTH-SES-168 dan 296 tidak menyebut tindakan setelah dialog dibiarkan; spec menutupnya dengan [Cancel] sebagai langkah penghubung. (4) TC-AUTH-SES-328 Expected a dan 295 Expected b memakai istilah "Force Logged Out" tanpa cara membaca status sesi di UI; spec memakai Dialog Logged Out dan entri log sebagai bukti. (5) TC-AUTH-SES-328 dan 295 sama-sama memakai `Nadia Pratama` sebagai user; spec memakai satu user berurutan. (6) TC-AUTH-SES-169 Langkah Uji tidak menyebut login Browser A; langkah 8 menambahkannya. (7) TC-AUTH-SES-296 tidak menyebut kapan kondisi Agreement dan MFA diterapkan terhadap enrollment dan sesi A; spec menyiapkan enrollment di B, mengakhiri sesi enroll, men-seed sesi A (langkah 16), baru menerapkan kondisi itu (disediakan tim FE/BE).
- Baseline entri log (S-12, S-03): langkah 38 mencatat jumlah entri sebelum aksi [Confirm] sebagai aksi tanpa `Verifikasi`; asersi log memakai selisih terhadap baseline itu. Teks Body Dialog Logged Out tidak diasersi karena TC-AUTH-SES-295 Expected b hanya menyebut dialog tampil; teks Body diuji di spec screening pemilik TC-AUTH-SES-2.
- Kelas harness: kelas c (perangkat A sebagai objek asersi: TC-AUTH-SES-328 Expected a dan TC-AUTH-SES-295 Expected b) berada bersama kelas d (hardware biometrik dan TOTP) karena Dialog Duplicate Login Attempt dari biometric re-login hanya dapat diuji dengan dua perangkat; tidak ada butir P-1 sampai P-5 yang berlaku untuk gabungan ini, sehingga gabungan dicatat di sini.
- Ukuran spec: melewati sekitar 35 langkah walau prefix enroll (langkah 7, 15, 27) tidak dihitung. Tiap subjudul TC memakai user sendiri dengan enrollment sendiri sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal; TC-AUTH-SES-328 dan 295 berbagi satu user karena kondisi akhir 328 adalah kondisi awal 295.
