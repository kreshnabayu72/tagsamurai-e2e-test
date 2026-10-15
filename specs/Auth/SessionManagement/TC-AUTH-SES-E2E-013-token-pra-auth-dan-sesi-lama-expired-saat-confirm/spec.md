---
id: TC-AUTH-SES-E2E-013-token-pra-auth-dan-sesi-lama-expired-saat-confirm
title: "Token Pra-autentikasi dan Sesi Lama Kedaluwarsa saat Confirm Duplicate Login"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-SES-34
  - TC-AUTH-SES-35
  - TC-AUTH-SES-36
  - TC-AUTH-SES-256
  - TC-AUTH-SES-282
coverage:
  web: automated
---

# Token Pra-autentikasi dan Sesi Lama Kedaluwarsa saat Confirm Duplicate Login

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): lima user profil BASE milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5 dan #11: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON; MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-34: `Dewi Nugroho` (`dewinugroho+{runId}-013@qwertysystem.net`)
  - TC-AUTH-SES-35: `Rizky Maulana` (`rizkymaulana+{runId}-013@qwertysystem.net`)
  - TC-AUTH-SES-36: `Nur Wijaya` (`nurwijaya+{runId}-013@qwertysystem.net`)
  - TC-AUTH-SES-256: `Joko Permata` (`jokopermata+{runId}-013@qwertysystem.net`)
  - TC-AUTH-SES-282: `Eko Firmansyah` (`ekofirmansyah+{runId}-013@qwertysystem.net`)
- Sesi web aktif di Browser A (Chrome on Windows, status Active) tiap user TIDAK dibuat di hook `before`, melainkan di awal tiap TC lewat login API pada konteks Browser A (kondisi yang di-seed BE). Alasannya: jam server dan jam browser/perangkat dimajukan secara kumulatif sepanjang spec, sehingga sesi yang dibuat di `before` akan melewati batas idle 15 menit sebelum TC-nya berjalan.
- Browser B (Firefox on macOS) dan Browser C (TC-AUTH-SES-282) adalah konteks baru yang belum login; tiap TC memakai konteks Browser B sendiri.
- Browser Admin: konteks terpisah yang sudah login sebagai Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #1; hook `before`, `Spectra.env.GS_TC_PASSWORD`); dipakai TC-AUTH-SES-35 untuk membaca `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log`.
- Suite berjalan serial (`parallel: false`); state global yang diubah: jam server dan jam browser/perangkat uji (diatur bersama), sweep periodik sesi (TC-AUTH-SES-36), dipulihkan di hook `after`.
- State global yang diubah dan pemulihannya di hook `after` (tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh): jam server dan jam browser/perangkat uji dikembalikan ke waktu nyata; sweep periodik sesi diaktifkan kembali (dinonaktifkan di TC-AUTH-SES-36); batas idle Client `Alpha Logistik` tidak diubah (tetap 15 menit). Setelah itu akhiri semua sesi seed dan sesi yang dibuat spec, tutup konteks Browser A, B, C, dan Admin, lalu hapus kelima user.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness d: time-travel dan TTL token pra-autentikasi 10 menit):
  - jam server uji dan jam browser/perangkat uji dapat dimajukan bersama dengan presisi detik, diatur ke waktu absolut, dibekukan pada nilai yang diminta, dan dipulihkan ke waktu nyata, termasuk waktu terbit token ditambah tepat 10 menit 00 detik dan 10 menit 01 detik (TC-AUTH-SES-282);
  - sweep periodik sesi dapat dinonaktifkan (TC-AUTH-SES-36);
  - alat uji dapat mengirim ulang request Confirm dengan token pra-autentikasi yang sama (TC-AUTH-SES-256);
  - pengamatan status HTTP respons request Confirm (422);
  - dua hingga tiga konteks browser bersamaan dengan user agent yang dapat ditetapkan (Chrome on Windows, Firefox on macOS);
  - Browser A (sesi seed lewat login API) dapat dibuka pada Portal — Product Hub dengan koneksi SSE aktif, sehingga push Dialog "Logged Out" dapat diamati saat dibiarkan tanpa interaksi hingga 10 detik (TC-AUTH-SES-35);
  - pembacaan data sesi platform per user (status Active, Force Logged Out, Expired, jumlah sesi), disediakan tim FE/BE tanpa endpoint tertentu;
  - reCAPTCHA mode uji di environment (halaman Login with Password).
- Browser Admin login ulang sebagai akun yang sama tepat sebelum bagian admin TC-AUTH-SES-35 (baseline dan pembacaan log), karena selama jam bergeser kumulatif sesi hook `before` melewati batas idle 15 menit. Jam server dan jam browser/perangkat dipulihkan ke waktu nyata sebelum Browser Admin membuka log, baik untuk baseline maupun untuk pembacaan akhir (S-09).
- Titik waktu: umur token pra-autentikasi dihitung sejak [Log in] di Browser B berhasil memunculkan Dialog "Duplicate Login Attempt" (token berumur 0); tiap TC mengukur umur token pada TC-nya sendiri.
- Akun yang dipakai: user uji masing-masing TC (bukan akun aktor) pada Browser A, B, dan C; akun Total Control (Global Settings) pada Browser Admin.

## Test Steps

### TC-AUTH-SES-34: Confirm setelah token pra-autentikasi kedaluwarsa ditolak dan kembali ke halaman Login

1. Siapkan sesi web aktif milik `Dewi Nugroho` di Browser A (Chrome on Windows) lewat login API → status Active
2. Buka konteks Browser B baru (Firefox on macOS, belum login), lalu buka halaman `Auth > Login with Password` → halaman Login with Password tampil
3. Ketik email `dewinugroho+{runId}-013@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Dialog "Duplicate Login Attempt" muncul
4. Biarkan dialog terbuka dan majukan jam server uji 10 menit 30 detik (jam server dan jam browser/perangkat diatur bersama)
5. Klik [Confirm]
6. Verifikasi Server menolak request Confirm dengan status 422
7. Verifikasi Browser B kembali ke halaman Login
8. Verifikasi toast error: "Error, failed to log in."
9. Verifikasi Tidak ada sesi baru
10. Verifikasi Sesi di Browser A tetap Active

### TC-AUTH-SES-256: Confirm kedua dengan token pra-autentikasi yang sudah dipakai ditolak

11. Siapkan sesi web aktif milik `Joko Permata` di Browser A (Chrome on Windows) lewat login API → status Active
12. Tutup konteks Browser B TC sebelumnya (hapus sesi login browser), buka konteks Browser B baru (Firefox on macOS, belum login), lalu buka halaman `Auth > Login with Password` → halaman Login with Password tampil
13. Ketik email `jokopermata+{runId}-013@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Dialog "Duplicate Login Attempt" muncul
14. Klik [Confirm] → sesi baru di Browser B aktif
15. Kirim ulang request Confirm dengan token pra-autentikasi yang sama (alat uji)
16. Verifikasi Permintaan kedua ditolak server dengan status 422
17. Verifikasi FE kembali ke halaman Login
18. Verifikasi toast "Error, failed to log in."
19. Verifikasi Tidak ada sesi tambahan

### TC-AUTH-SES-282: Confirm tepat pada menit ke-10 masih berhasil dan pada 10 menit 01 detik ditolak

20. Siapkan sesi web aktif milik `Eko Firmansyah` di Browser A (Chrome on Windows) lewat login API → status Active
21. Tutup konteks Browser B TC sebelumnya (hapus sesi login browser), buka konteks Browser B baru (Firefox on macOS, belum login), lalu buka halaman `Auth > Login with Password` → halaman Login with Password tampil
22. Ketik email `ekofirmansyah+{runId}-013@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] dan catat waktu server saat Dialog muncul sebagai waktu terbit token → Dialog "Duplicate Login Attempt" muncul
23. Atur jam server uji dan jam browser/perangkat uji bersama secara absolut ke waktu terbit token (dicatat di langkah 22) ditambah tepat 10 menit 00 detik, lalu bekukan keduanya di nilai itu sampai respons Confirm diterima
24. Klik [Confirm]
25. Verifikasi Pada umur token 10:00 [Confirm] berhasil
26. Verifikasi Browser B masuk Portal — Product Hub
27. Buka konteks Browser C baru (belum login), lalu buka halaman `Auth > Login with Password` → halaman Login with Password tampil
28. Ketik email `ekofirmansyah+{runId}-013@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] dan catat waktu server saat Dialog muncul sebagai waktu terbit token → Dialog "Duplicate Login Attempt" muncul (sesi aktif adalah sesi Browser B)
29. Atur jam server uji dan jam browser/perangkat uji bersama secara absolut ke waktu terbit token (dicatat di langkah 28) ditambah tepat 10 menit 01 detik, lalu bekukan keduanya di nilai itu sampai respons Confirm diterima
30. Klik [Confirm]
31. Verifikasi Pada umur token 10:01 request ditolak server dengan status 422
32. Verifikasi FE kembali ke halaman Login
33. Verifikasi Tidak ada sesi baru dari Browser C
34. Pulihkan jam server uji dan jam browser/perangkat uji ke waktu nyata (keduanya bersama; pergeseran kumulatif TC-AUTH-SES-34 dan 282 diakhiri sebelum akun aktor membuka log)

### TC-AUTH-SES-35: Confirm saat sesi lama sudah kedaluwarsa tetap berhasil tanpa Dialog Logged Out

35. Siapkan sesi web aktif milik `Rizky Maulana` di Browser A (Chrome on Windows) lewat login API → status Active
36. Di Browser A buka Portal — Product Hub dengan sesi seed itu supaya koneksi SSE aktif → halaman Portal — Product Hub tampil
37. Di Browser Admin login ulang sebagai `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan password `Spectra.env.GS_TC_PASSWORD`
38. Di Browser Admin buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` untuk `Rizky Maulana`, lalu catat baseline: jumlah entri `Session expired` untuk email `rizkymaulana+{runId}-013@qwertysystem.net` di kedua log
39. Majukan jam server uji 6 menit (jam server dan jam browser/perangkat diatur bersama) tanpa aktivitas di Browser A (Browser A idle 6 menit)
40. Tutup konteks Browser B TC sebelumnya (hapus sesi login browser), buka konteks Browser B baru (Firefox on macOS, belum login), lalu buka halaman `Auth > Login with Password` → halaman Login with Password tampil
41. Ketik email `rizkymaulana+{runId}-013@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Dialog "Duplicate Login Attempt" muncul (token pra-autentikasi berumur 0)
42. Majukan jam server uji 9 menit (jam server dan jam browser/perangkat diatur bersama) tanpa aktivitas di Browser A (Browser A idle tepat 15 menit; token pra-autentikasi berumur 9 menit)
43. Klik [Confirm] di Browser B
44. Verifikasi Browser B masuk Portal — Product Hub
45. Verifikasi Sesi baru di Browser B berstatus Active
46. Pindah ke Browser A dan amati tanpa interaksi selama 10 detik
47. Verifikasi Browser A tidak menerima Dialog "Logged Out"
48. Pulihkan jam server uji dan jam browser/perangkat uji ke waktu nyata (keduanya bersama)
49. Di Browser Admin login ulang sebagai `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan password `Spectra.env.GS_TC_PASSWORD`
50. Di Browser Admin buka `Global Settings > Activity Log > Session`
51. Verifikasi Entri `Session expired` untuk email `rizkymaulana+{runId}-013@qwertysystem.net` (dicari per Note dan email) bertambah tepat satu dibanding baseline di `Global Settings > Activity Log > Session`
52. Buka `Global Settings > User > Detail > User Log` untuk `Rizky Maulana`
53. Verifikasi Entri `Session expired` (dicari per Note dan email) bertambah tepat satu dibanding baseline di User Log `Rizky Maulana`

### TC-AUTH-SES-36: Sesi lama yang melewati batas idle tapi belum ditandai sweep tidak dihitung sebagai sesi aktif

54. Siapkan sesi web aktif milik `Nur Wijaya` di Browser A (Chrome on Windows) lewat login API → status Active
55. Nonaktifkan sweep periodik sesi
56. Majukan jam server uji 16 menit (jam server dan jam browser/perangkat diatur bersama) tanpa aktivitas di Browser A (sweep belum menandai sesi)
57. Tutup konteks Browser B TC sebelumnya (hapus sesi login browser), buka konteks Browser B baru (Firefox on macOS, belum login), lalu buka halaman `Auth > Login with Password` → halaman Login with Password tampil
58. Ketik email `nurwijaya+{runId}-013@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil
59. Verifikasi Browser B langsung masuk Portal — Product Hub
60. Verifikasi Dialog "Duplicate Login Attempt" tidak tampil
61. Verifikasi Sesi baru di Browser B berstatus Active
62. Verifikasi Sesi lama di Browser A berstatus Expired
63. Aktifkan kembali sweep periodik sesi (pemulihan state global)

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness d (time-travel dan TTL token pra-autentikasi).
- Penyimpangan urutan (S-05, S-10): urutan di spec ini TC-AUTH-SES-34, 256, 282, 35, lalu 36 (urutan TC sumber 34, 35, 36, 256, 282). Penolakan token (34, 256, 282) diletakkan sebelum Confirm yang berhasil tanpa penolakan (35, 36). Jam server dan jam browser/perangkat dimajukan bersama secara kumulatif dan tidak dipulihkan antar-TC 34, 256, dan 282; jam dipulihkan di akhir TC-AUTH-SES-282 (langkah 34), sebelum Browser Admin membuka log untuk baseline TC-AUTH-SES-35, dan sekali lagi sebelum pembacaan log akhir TC-AUTH-SES-35 (langkah 48); sesi Browser A tiap TC dibuat di awal TC itu sehingga pergeseran kumulatif tidak mengubah hasil.
- Penyimpangan dari pola seeding sesi di hook `before` (S-06, S-11): sesi Browser A dibuat per TC di langkah awal (langkah 1, 11, 20, 35, 54) karena jam server dimajukan kumulatif; alasannya tercatat di Prerequisites. Langkah itu adalah seeding BE, bukan asersi.
- TC-AUTH-SES-256 berdependensi pada TC-AUTH-SES-26 (login di Browser B hingga Confirm) dan TC-AUTH-SES-282 pada TC-AUTH-SES-34 (login di Browser B hingga Confirm setelah jam digeser); langkah dependensi itu disalin pada langkah 12-14 dan 21-24 (S-04). Asersi hasil Confirm TC-AUTH-SES-26 diuji di `TC-AUTH-SES-E2E-011-confirm-cancel-duplicate-login-web`.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): membuka konteks Browser B dan C baru; berpindah antar Browser A, B, dan Admin; mencatat waktu terbit token (langkah 22 dan 28) dan mengatur jam secara absolut lalu membekukannya untuk batas eksak TC-AUTH-SES-282 (langkah 23 dan 29); menonaktifkan dan mengaktifkan kembali sweep periodik (langkah 55 dan 63, dengan hook `after` sebagai cadangan); login ulang Browser Admin (langkah 37 dan 49), memulihkan jam (langkah 34 dan 48), dan mencatat baseline log (langkah 38). Membuka Portal — Product Hub di Browser A (langkah 36) memastikan koneksi SSE aktif, karena asersi "Browser A tidak menerima Dialog Logged Out" (langkah 47) hanya bermakna bila Browser A hasil seeding API sedang membuka halaman app. Konteks Browser B TC sebelumnya ditutup pada langkah pembuka (langkah 12, 21, 40, dan 57).
- Pencatatan: asersi "tidak ada entri log baru" pada TC-AUTH-SES-34 (Expected d) dan TC-AUTH-SES-256 (Expected b), serta bagian "tidak ada `Logged out (new device login)`" pada TC-AUTH-SES-35 (Expected d), tidak diasersikan di spec ini; dirujuk ke spec absence `TC-AUTH-SES-E2E-066-absence-duplicate-login-dan-session-expired` sesuai S-05. Bagian "dicatat `Session expired`" pada TC-AUTH-SES-35 diasersikan di langkah 51 dan 53 dengan selisih terhadap baseline (S-12).
- Temuan untuk QA: (1) TC-AUTH-SES-282 langkah 3 ("Ulangi dari awal di sesi baru") tidak menyebut browser yang dipakai pada pengulangan; spec memakai Browser C (precondition d), dengan sesi aktif yang dilawan adalah sesi Browser B hasil pengulangan pertama. (2) TC-AUTH-SES-282 memakai batas presisi detik; waktu nyata antara memajukan jam dan klik [Confirm] bisa menggeser umur token, jadi jam server uji perlu dapat diatur absolut dan dibekukan pada nilai yang diminta; spec mengatur jam ke waktu terbit token ditambah 10 menit 00 detik (dan 10 menit 01 detik) lalu membekukannya (bagian 6). (3) TC-AUTH-SES-256 Expected a menyebut "FE kembali ke halaman Login" setelah request dikirim ulang oleh alat uji; TC tidak menjelaskan bagaimana FE mengetahui penolakan itu, dan spec mengikuti TC. (4) TC-AUTH-SES-34 dan 282 mengasersi status 422 yang hanya terlihat lewat pengamatan jaringan; kebutuhannya dicatat di Prerequisites. (5) TC-AUTH-SES-35 precondition b ("sudah idle 6 menit") tidak menyebut cara mencapainya; spec memajukan jam server 6 menit (langkah 39). (8) TC-AUTH-SES-35 mengasersi push di Browser A (Dialog "Logged Out" tidak diterima), tetapi precondition-nya hanya "sesi web aktif di Browser A" dan tidak menyatakan Browser A menampilkan Portal — Product Hub; spec menambah langkah penghubung membuka Portal — Product Hub di Browser A (langkah 36) dan kemampuan SSE di Prerequisites. (6) TC sumber menulis login dengan "password yang benar" tanpa menyebut reCAPTCHA atau nilai password; spec mengikuti TC, memakai `Spectra.env.SES_PASSWORD`, dan mengandalkan reCAPTCHA mode uji. (7) TC-AUTH-SES-34 c, 35 b, 36 b/c, 256 b, dan 282 menyebut status atau jumlah sesi (Active, Expired, "tidak ada sesi tambahan") tanpa menyebut cara membacanya; spec memakai kemampuan pembacaan data sesi platform yang disediakan tim FE/BE (Prerequisites).
- P-5(b): TC-AUTH-SES-256 (langkah 11-19) adalah satu TC objek-uji ringan kelas a (kirim ulang request Confirm dengan token terpakai lewat alat uji) tanpa harness eksternal sendiri, berada di spec harness dominan d (TTL token pra-autentikasi) yang permukaannya sama (Confirm duplicate login).
- Ukuran: spec memuat 63 langkah (melebihi sekitar 35) karena lima TC satu kelas harness (time-travel dan TTL token) berada dalam satu spec; tiap TC memakai user dan sesi sendiri, sehingga bagian berikutnya tetap bermakna meski TC lain di spec ini tidak dijalankan.
