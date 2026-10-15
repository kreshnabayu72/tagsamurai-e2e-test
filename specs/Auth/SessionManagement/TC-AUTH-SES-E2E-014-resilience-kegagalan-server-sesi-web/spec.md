---
id: TC-AUTH-SES-E2E-014-resilience-kegagalan-server-sesi-web
title: "Resilience Kegagalan Server pada Sesi Web: Confirm, Refresh, Heartbeat, Buka Produk, Force-Logout, dan Logout"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-SES-33
  - TC-AUTH-SES-51
  - TC-AUTH-SES-52
  - TC-AUTH-SES-61
  - TC-AUTH-SES-110
  - TC-AUTH-SES-139
  - TC-AUTH-SES-143
coverage:
  web: automated
---

# Resilience Kegagalan Server pada Sesi Web: Confirm, Refresh, Heartbeat, Buka Produk, Force-Logout, dan Logout

## Prerequisites

- Mode: FE+BE. Kegagalan dipaksa lewat `Spectra.intercept()` parsial di atas backend nyata (konvensi bagian 6): hanya respons request yang disebut di bawah yang diganti menjadi HTTP 500; semua request lain tetap ke backend nyata, dan asersi state sesi, seat, dan Client dibaca dari backend nyata.
  - Confirm (TC-AUTH-SES-33): `POST /v2/iam/auth/sessions/confirm-duplicate`.
  - Cek sesi saat [Refresh] pada Dialog "Session Expired" (TC-AUTH-SES-51 dan 52): cek sesi gateway `GET /auth/validate` (LLD `auth/session-management/API/low-level-design.md` bagian 3, bukan route publik di `openapi.yaml`). Bila request ini tidak terjangkau intercept browser, kegagalan 5xx diinjeksi di sisi gateway atau server dengan mekanisme yang sama.
  - Heartbeat (TC-AUTH-SES-61): `PUT /v2/iam/auth/sessions/heartbeat`.
  - Open Product (TC-AUTH-SES-110): `POST /v2/iam/auth/product-sessions`.
  - Force-logout (TC-AUTH-SES-139): `POST /v2/iam/auth/product-sessions/{id}/force-logout`.
  - Logout (TC-AUTH-SES-143): `POST /v2/iam/auth/logout`.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): tujuh user profil BASE (Activated, Active ON; MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-33: `Andi Wibowo` (`andiwibowo+{runId}-014@qwertysystem.net`), Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5 dan #11: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5)
  - TC-AUTH-SES-51: `Yoga Rahayu` (`yogarahayu+{runId}-014@qwertysystem.net`), Client `Alpha Logistik`
  - TC-AUTH-SES-52: `Ayu Anggraini` (`ayuanggraini+{runId}-014@qwertysystem.net`), Client `Alpha Logistik`
  - TC-AUTH-SES-61: `Budi Wulandari` (`budiwulandari+{runId}-014@qwertysystem.net`), Client `Alpha Logistik`
  - TC-AUTH-SES-110: `Yoga Setiawan` (`yogasetiawan+{runId}-014@qwertysystem.net`), Client Q2 (Tabel Data Uji Pre-setup #12: subscription Fixed Asset dan Supply Asset Active, kuota masing-masing 2) dengan App Access Fixed Asset dan Supply Asset, disiapkan oleh akun aktor Total Control (Global Settings) dengan scope Client Q2 (Tabel Data Uji Pre-setup #26); tidak ada sesi-produk Active
  - TC-AUTH-SES-139: `Ayu Rahayu` (`ayurahayu+{runId}-014@qwertysystem.net`), Client Q2 dengan App Access Fixed Asset dan Supply Asset, disiapkan oleh akun aktor Total Control (Global Settings) dengan scope Client Q2 (Tabel Data Uji Pre-setup #26)
  - TC-AUTH-SES-143: `Sari Maulana` (`sarimaulana+{runId}-014@qwertysystem.net`), Client `Alpha Logistik`
- Sesi web aktif di Browser A (Chrome on Windows, status Active) tiap user, serta sesi-produk Fixed Asset Active milik `Ayu Rahayu` (TC-AUTH-SES-139, seat Client Q2 terpakai 1), TIDAK dibuat di hook `before`, melainkan di awal tiap TC lewat login API dan Open Product API (kondisi yang di-seed BE). Alasannya: TC-AUTH-SES-51 dan 52 memajukan jam server secara kumulatif, dan sesi yang dibuat di `before` akan melewati batas idle 15 menit sebelum TC-nya berjalan.
- Browser B (Firefox on macOS) untuk TC-AUTH-SES-33 adalah konteks baru yang belum login.
- Browser License: konteks terpisah yang sudah login sebagai Admin License `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` (hook `before`, `Spectra.env.FA_MGL_PASSWORD`, Global Role Manage Global License dengan scope Client Q2; Tabel Data Uji Pre-setup #2 dan #33); dipakai TC-AUTH-SES-139. Karena jam bergeser kumulatif (TC-AUTH-SES-51 dan 52) melewati batas idle 15 menit, Browser License login ulang sebagai akun yang sama tepat sebelum bagian admin TC-AUTH-SES-139.
- Suite berjalan serial (`parallel: false`); state global yang diubah: failure injection per endpoint, jam server dan jam browser/perangkat uji (diatur bersama), dipulihkan di hook `after`.
- State global yang diubah dan pemulihannya di hook `after` (tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh): matikan semua intercept dan failure injection; jam server uji dan jam browser/perangkat uji dikembalikan ke waktu nyata; akhiri sesi-produk dan semua sesi seed; tutup konteks Browser A, B, dan License; hapus ketujuh user.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`, `FA_MGL_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness b: fault injection parsial):
  - `Spectra.intercept()` atau failure injection setara yang dapat dinyalakan dan dimatikan per endpoint di tengah spec;
  - jam server uji dan jam browser/perangkat uji dapat dimajukan bersama dengan presisi menit dan dipulihkan ke waktu nyata (TC-AUTH-SES-51, 52, dan 61), karena Toast dan Dialog Session Expired dipicu hitung mundur di client;
  - pergerakan mouse terus-menerus di Browser A selama 3 interval heartbeat (interval default 60 detik, dipenuhi dengan memajukan jam server dan jam browser/perangkat bersama 3 menit, tanpa menunggu waktu nyata) untuk TC-AUTH-SES-61;
  - pembacaan data sesi platform dan sesi-produk per user serta hitungan seat Client Q2 (status Active, jumlah sesi-produk, seat terpakai) untuk asersi status, disediakan tim FE/BE tanpa endpoint tertentu;
  - pembacaan waktu kedaluwarsa dari respons heartbeat (TC-AUTH-SES-61);
  - reCAPTCHA mode uji di environment (halaman Login with Password).
- Akun yang dipakai: user uji masing-masing TC (bukan akun aktor) pada Browser A dan B; Admin License pada Browser License untuk TC-AUTH-SES-139.

## Test Steps

### TC-AUTH-SES-33: Kegagalan server saat Confirm menampilkan toast error dan sesi lama tetap aktif

1. Siapkan sesi web aktif milik `Andi Wibowo` di Browser A (Chrome on Windows) lewat login API → status Active
2. Buka konteks Browser B baru (Firefox on macOS, belum login), lalu buka halaman `Auth > Login with Password` → halaman Login with Password tampil
3. Ketik email `andiwibowo+{runId}-014@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Dialog "Duplicate Login Attempt" muncul
4. Aktifkan failure injection 5xx (respons 500) pada request Confirm
5. Klik [Confirm]
6. Verifikasi toast error: "Error, failed to log in."
7. Verifikasi Dialog "Duplicate Login Attempt" tetap tampil
8. Verifikasi [Confirm] kembali enabled
9. Verifikasi Tidak ada sesi baru
10. Pindah ke Browser A (tanpa mengklik apa pun)
11. Verifikasi Sesi di Browser A tetap Active
12. Nonaktifkan failure injection pada request Confirm

### TC-AUTH-SES-51: Cek sesi gagal saat klik Refresh menampilkan toast error dan dialog tetap tampil

13. Siapkan sesi web aktif milik `Yoga Rahayu` di Browser A (Chrome on Windows) lewat login API dan buka Browser A di Portal — Product Hub (batas idle 15 menit)
14. Di Browser A biarkan tanpa aktivitas dan majukan jam server uji 10 menit (jam server dan jam browser/perangkat diatur bersama) → amati Toast
15. Majukan jam server uji 6 menit lagi (jam server dan jam browser/perangkat diatur bersama; idle 16 menit) → Dialog "Session Expired" tampil di Browser A
16. Aktifkan failure injection 5xx (respons 500) pada request cek sesi
17. Di Browser A klik [Refresh]
18. Verifikasi toast error: "Error, failed to refresh."
19. Verifikasi Dialog "Session Expired" tetap tampil
20. Verifikasi [Refresh] aktif lagi
21. Verifikasi Browser A tidak diarahkan ke Login
22. Nonaktifkan failure injection pada request cek sesi

### TC-AUTH-SES-52: Klik Refresh ulang setelah kegagalan berhasil bila server pulih

23. Siapkan sesi web aktif milik `Ayu Anggraini` di Browser A (Chrome on Windows) lewat login API dan buka Browser A di Portal — Product Hub (batas idle 15 menit)
24. Di Browser A biarkan tanpa aktivitas dan majukan jam server uji 10 menit (jam server dan jam browser/perangkat diatur bersama) → amati Toast
25. Majukan jam server uji 6 menit lagi (jam server dan jam browser/perangkat diatur bersama; idle 16 menit) → Dialog "Session Expired" tampil di Browser A
26. Aktifkan failure injection 5xx (respons 500) pada request cek sesi
27. Di Browser A klik [Refresh] → toast error "Error, failed to refresh." tampil dan Dialog "Session Expired" tetap tampil
28. Nonaktifkan failure injection pada request cek sesi
29. Di Browser A klik [Refresh] lagi
30. Verifikasi Cek sesi berhasil (respons bukan 5xx)
31. Verifikasi Browser A diarahkan ke halaman Login with Password (sesi masih expired)
32. Verifikasi Tidak ada toast error baru

### TC-AUTH-SES-61: Heartbeat yang gagal sesaat tidak membuat sesi kedaluwarsa lebih awal

33. Siapkan sesi web aktif milik `Budi Wulandari` di Browser A (Chrome on Windows) lewat login API dan buka Browser A di Portal — Product Hub (batas idle 15 menit)
34. Aktifkan failure injection yang menggagalkan request heartbeat (respons 500)
35. Gerakkan mouse terus-menerus di Browser A selama 3 interval heartbeat, sambil memajukan jam server uji dan jam browser/perangkat uji bersama 3 menit
36. Verifikasi Selama heartbeat gagal tidak ada Dialog "Session Expired"
37. Nonaktifkan failure injection pada request heartbeat
38. Gerakkan mouse lagi di Browser A
39. Verifikasi Heartbeat berikutnya berhasil
40. Verifikasi Waktu kedaluwarsa disinkronkan ke nilai server yang benar (sesuai respons heartbeat)

### TC-AUTH-SES-110: Kegagalan server saat buka produk menampilkan toast error dan seat tidak diambil

41. Siapkan sesi platform web aktif milik `Yoga Setiawan` di Browser A (Chrome on Windows) lewat login API dan buka Browser A di Portal — Product Hub
42. Aktifkan failure injection 5xx (respons 500) pada request Open Product
43. Di Browser A klik card Fixed Asset
44. Verifikasi toast error: "Error, failed to open product."
45. Verifikasi Seat tidak diambil
46. Verifikasi Sesi-produk tidak dibuat
47. Nonaktifkan failure injection pada request Open Product

### TC-AUTH-SES-139: Kegagalan server saat force-logout menampilkan toast error

48. Siapkan sesi-produk Fixed Asset Active milik `Ayu Rahayu` (sesi platform web aktif di Browser A, lalu Open Product Fixed Asset) lewat API → seat Client Q2 terpakai 1
49. Di Browser License login ulang sebagai `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` dengan password `Spectra.env.FA_MGL_PASSWORD`
50. Di Browser License buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset) → daftar sesi aktif tampil
51. Aktifkan failure injection 5xx (respons 500) pada request force-logout
52. Di Browser License pilih baris `Ayu Rahayu`, lalu klik [Force Logout] dan [Confirm Logout]
53. Verifikasi toast error: "Error, failed to log out user."
54. Verifikasi Sesi `Ayu Rahayu` tetap Active
55. Verifikasi Retry dapat dilakukan: baris `Ayu Rahayu` masih tampil dan [Force Logout] enabled
56. Nonaktifkan failure injection pada request force-logout

### TC-AUTH-SES-143: Kegagalan server saat Manual Logout menampilkan toast error dan tetap di halaman

57. Siapkan sesi web aktif milik `Sari Maulana` di Browser A (Chrome on Windows) lewat login API dan buka Browser A di Portal — Product Hub
58. Aktifkan failure injection 5xx (respons 500) pada request logout
59. Di Browser A klik menu Profile lalu pilih Log Out
60. Verifikasi toast error: "Error, failed to log out."
61. Verifikasi Browser A tetap di halaman terakhir
62. Verifikasi Sesi tetap Active
63. Buka kembali menu Profile
64. Verifikasi Menu Profile tetap menampilkan Log Out sehingga logout dapat diulang
65. Nonaktifkan failure injection pada request logout

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness b (fault injection parsial atas backend nyata; Mode tetap FE+BE).
- Urutan mengikuti TC sumber (33, 51, 52, 61, 110, 139, 143); tidak ada penyimpangan (S-05, S-10). Tiap TC memakai user dan sesi sendiri, jadi TC tidak saling bergantung.
- Penyimpangan dari pola seeding sesi di hook `before` (S-06, S-11): sesi Browser A dan sesi-produk dibuat per TC di langkah awal (langkah 1, 13, 23, 33, 41, 48, 57) karena jam server dimajukan kumulatif pada TC-AUTH-SES-51 dan 52; alasannya tercatat di Prerequisites. Langkah itu adalah seeding BE, bukan asersi.
- TC-AUTH-SES-51 dan 52 berdependensi pada TC-AUTH-SES-46 (idle hingga Dialog "Session Expired"), dan TC-AUTH-SES-52 pada TC-AUTH-SES-51 (klik [Refresh] gagal). Langkah dependensi itu disalin pada langkah 14-15, 24-25, dan 26-27 (S-04); asersi hasil TC-AUTH-SES-46 (Toast Idle Warning, halaman beku) diuji di spec lain. Pada langkah 27 toast dan dialog hanya prasyarat TC-AUTH-SES-52, bukan asersi baru.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03, S-09): login ulang Browser License sebelum bagian admin TC-AUTH-SES-139 (langkah 49); menyiapkan sesi seed per TC; membuka konteks Browser B baru; berpindah antar Browser A dan B; menonaktifkan failure injection di akhir tiap TC sebagai pemulihan state, dengan hook `after` sebagai cadangan.
- Temuan untuk QA: (1) TC-AUTH-SES-33, 51, 61, 110, 139, dan 143 berlabel `Manual Only` karena failure injection; spec tetap memuatnya dan pemicunya ditulis sebagai langkah eksplisit dengan kemampuan teknis di Prerequisites. (2) TC-AUTH-SES-51 menyebut "request cek sesi" tanpa endpoint; LLD bagian 3 menyebutnya cek sesi gateway `GET /auth/validate` yang bukan route publik di `openapi.yaml`, sehingga kemampuan menginjeksi 5xx di titik itu perlu dikonfirmasi tim FE/BE. (3) TC-AUTH-SES-52 Expected a ("Cek sesi berhasil: sesi masih expired") memakai kata "berhasil" untuk hasil yang berujung ke halaman Login; spec mengasersi respons bukan 5xx dan pengalihan ke Login with Password. (4) TC-AUTH-SES-52 precondition b mengandaikan klik [Refresh] gagal sudah terjadi; spec menyalin langkah itu dari TC-AUTH-SES-51 (langkah 26-27). (5) TC-AUTH-SES-61 tidak menyebut jenis kegagalan heartbeat dan lama 3 interval; spec memakai respons 500 dan interval default 60 detik dari PRD. (6) TC-AUTH-SES-110 dan 139 tidak menyebut cara membaca "seat tidak diambil" dan "sesi tetap Active"; spec membacanya dari data BE uji (Prerequisites). (7) TC-AUTH-SES-139 Expected b ("retry dapat dilakukan") tidak punya langkah retry; spec mengasersi baris dan tombol masih tersedia tanpa mengulang aksi. (8) TC-AUTH-SES-33 dan TC login lain menulis login dengan "password yang benar" tanpa menyebut reCAPTCHA atau nilai password; spec mengikuti TC, memakai `Spectra.env.SES_PASSWORD`, dan mengandalkan reCAPTCHA mode uji. (9) TC-AUTH-SES-33 Expected b menulis "[Confirm] kembali enabled" tanpa menyebut state Loading di antaranya; spec mengasersi hasil akhir saja.
- Ukuran: spec memuat 65 langkah (melebihi sekitar 35) karena tujuh TC satu kelas harness (fault injection parsial) berada dalam satu spec; tiap TC memakai user dan sesi sendiri, sehingga bagian berikutnya tetap bermakna meski TC lain di spec ini tidak dijalankan.
