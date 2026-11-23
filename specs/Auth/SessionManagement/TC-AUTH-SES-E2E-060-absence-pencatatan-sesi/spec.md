---
id: TC-AUTH-SES-E2E-060-absence-pencatatan-sesi
title: "Absence Pencatatan Sesi: Kondisi yang Tidak Menulis Session Log Entry"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-SES-190
  - TC-AUTH-SES-195
  - TC-AUTH-SES-196
  - TC-AUTH-SES-202
  - TC-AUTH-SES-203
  - TC-AUTH-SES-211
coverage:
  web: automated
  mobile: automated
---

# Absence Pencatatan Sesi: Kondisi yang Tidak Menulis Session Log Entry

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`; scope Client Alpha Logistik: Tabel Data Uji Pre-setup #1, scope Client Expired/uji untuk `Reza Permata`: Tabel Data Uji Pre-setup #31, scope Client Suspend untuk `Intan Wibowo`: Tabel Data Uji Pre-setup #32): tujuh user (enam user target dan satu user aktor tanpa capability), password `Spectra.env.SES_PASSWORD`, email bersuffix per run. User Activated, Active ON, MFA dan Agreement tidak terpicu kecuali dinyatakan lain:
  - TC-AUTH-SES-190: `Dimas Saputra` (`dimassaputra+{runId}-060@qwertysystem.net`), profil BASE Client Alpha Logistik (Tabel Data Uji Pre-setup #5); sesi web Active di Browser A (Chrome on Windows); Browser B (Firefox on macOS) belum login
  - TC-AUTH-SES-202: `Reza Permata` (`rezapermata+{runId}-060@qwertysystem.net`), profil BASE milik Client dengan subscription Fixed Asset berstatus Archive (Tabel Data Uji Pre-setup #14) dan App Access Fixed Asset; sesi platform web Active di Browser A pada Portal — Product Hub; tidak ada sesi-produk Active
  - TC-AUTH-SES-203: `Sari Lestari` (`sarilestari+{runId}-060@qwertysystem.net`), profil BASE Client Alpha Logistik dengan App Access Fixed Asset dan sesi-produk Fixed Asset Active; user aktor tanpa capability: `Sari Nugroho` (`sarinugroho+{runId}-060@qwertysystem.net`), profil BASE di Client yang sama tanpa Global Role Manage Global License
  - TC-AUTH-SES-211: `Dewi Anggraini` (`dewianggraini+{runId}-060@qwertysystem.net`), profil BIO (Tabel Data Uji Pre-setup #9) yang sudah enroll biometric di perangkat Android uji B (Tabel Data Uji Pre-setup #10) dengan kredensial biometric yang sudah di-revoke di server; tidak ada sesi platform aktif di perangkat itu
  - TC-AUTH-SES-195: `Intan Wibowo` (`intanwibowo+{runId}-060@qwertysystem.net`), profil BASE milik Client Suspend (Tabel Data Uji Pre-setup #16: subscription Fixed Asset Active); sesi platform web dan sesi-produk Fixed Asset Active di Browser A
  - TC-AUTH-SES-196: `Joko Nugroho` (`jokonugroho+{runId}-060@qwertysystem.net`), profil BASE Client Alpha Logistik (batas idle 15 menit); sesi web Active di Browser A dengan Tab A dan Tab B sama-sama di Portal — Product Hub
- Konteks dan akun (dibuka di hook `before`, login pertama tiap konteks ada di hook):
  - Browser Admin: akun aktor Total Control (Global Settings) di atas dengan scope Client Alpha Logistik (Tabel Data Uji Pre-setup #1), scope Client Expired/uji (Tabel Data Uji Pre-setup #31; TC-AUTH-SES-202) dan scope Client Suspend (Tabel Data Uji Pre-setup #32; TC-AUTH-SES-195), dipakai membaca `Global Settings > Activity Log > Session`, `Activity Log > Session` milik Fixed Asset, dan `Global Settings > User > Detail > User Log`.
  - Browser Principal: akun aktor `principalAdminConsole_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_PRINCIPAL_PASSWORD`, dipakai Suspend dan Unsuspend Client Suspend di `Admin Console > Client` (TC-AUTH-SES-195).
  - Browser A (memuat sesi seed milik user TC yang sedang berjalan), Browser B, Browser C (konteks bersih untuk login `Sari Nugroho`), dan perangkat Android uji B.
- Suite berjalan serial (`parallel: false`); state global yang diubah: perangkat fisik Android uji B dipakai bersama (data aplikasi dan token biometric lokal), status Client Suspend (Suspended pada TC-AUTH-SES-195, di-Unsuspend di akhir TC itu) serta jam server dan jam browser/perangkat yang diatur bersama (digeser pada TC-AUTH-SES-196, dikembalikan ke waktu normal di langkah TC sebelum hasil log dihitung), dipulihkan di hook `after` yang mengembalikan status Client Suspend ke Active dan jam ke waktu normal walau spec gagal di tengah. Karena jam bergeser melewati batas idle 15 menit, akun aktor di Browser Admin login ulang di langkah penghubung pada TC-AUTH-SES-196.
- Hook `after`: akhiri semua sesi seed (web, mobile, sesi-produk), cabut kredensial biometric seed, tutup konteks Browser A, B, C, Browser Principal, dan Browser Admin, hapus ketujuh user. Pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `AC_PRINCIPAL_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: konteks browser bersamaan dengan user agent yang dapat ditetapkan (Chrome on Windows, Firefox on macOS) serta Tab A dan Tab B dalam satu Browser A; pengatur waktu (Tabel Data Uji Pre-setup #18) yang memajukan dan memulihkan jam server dan jam browser/perangkat bersama; driver otomasi Android (aplikasi native) pada perangkat B dengan simulasi verifikasi sidik jari sukses; pengiriman request langsung ke `POST /v2/iam/auth/product-sessions/{id}/force-logout` (TC-AUTH-SES-203, `{id}` = ID sesi-produk Fixed Asset milik `Sari Lestari`; sumber: `auth/session-management/API/openapi.yaml`); pembacaan stempel waktu entri log untuk membedakan entri baru dari entri seeding; reCAPTCHA mode uji di environment untuk login web (halaman Login with Password).
- Akun yang dipakai: user uji masing-masing TC di Browser A, B, C, dan perangkat B; akun aktor di Browser Admin dan Browser Principal.

## Test Steps

### TC-AUTH-SES-190: Duplicate Login Cancel tidak dicatat

1. Tutup konteks Browser A sebelumnya dan buka konteks baru Browser A dengan memuat sesi web seed milik `Dimas Saputra`
2. Di Browser B (Firefox on macOS) buka `Auth > Login with Password` → halaman Login with Password tampil
3. Ketik email `dimassaputra+{runId}-060@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Dialog Duplicate Login Attempt muncul
4. Klik [Cancel] pada Dialog Duplicate Login Attempt
5. Pindah ke Browser A dan klik area mana pun
6. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Dimas Saputra` yang dibuat sesudah langkah 3 dimulai
7. Verifikasi Tidak ada entri baru untuk `Dimas Saputra` di `Global Settings > Activity Log > Session` untuk kondisi Cancel pada Dialog Duplicate Login Attempt
8. Buka `Global Settings > User > Detail > User Log` milik `Dimas Saputra` dan cari entri yang dibuat sesudah langkah 3 dimulai
9. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi Cancel pada Dialog Duplicate Login Attempt

### TC-AUTH-SES-202: Pembukaan produk diblok karena subscription tidak aktif tidak dicatat

10. Tutup konteks Browser A sebelumnya dan buka konteks baru Browser A dengan memuat sesi web seed milik `Reza Permata`
11. Di Browser A (sesi platform web Active `Reza Permata` di Portal — Product Hub) klik card Fixed Asset → Popup Subscription Not Active tampil
12. Di Browser Admin buka `Activity Log > Session` milik Fixed Asset dan cari entri untuk `Reza Permata` yang dibuat sesudah langkah 11 dimulai
13. Verifikasi Tidak ada entri baru untuk `Reza Permata` di `Activity Log > Session` milik Fixed Asset untuk kondisi pembukaan produk diblok karena subscription tidak aktif
14. Buka `Global Settings > User > Detail > User Log` milik `Reza Permata` dan cari entri yang dibuat sesudah langkah 11 dimulai
15. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi pembukaan produk diblok karena subscription tidak aktif

### TC-AUTH-SES-203: Force-logout ditolak 403 tidak dicatat

16. Di Browser C login sebagai `sarinugroho+{runId}-060@qwertysystem.net` dengan password `Spectra.env.SES_PASSWORD` → Portal — Product Hub tampil
17. Kirim request force-logout langsung ke `POST /v2/iam/auth/product-sessions/{id}/force-logout` untuk sesi-produk Fixed Asset milik `Sari Lestari` → server menolak dengan 403
18. Di Browser Admin buka `Activity Log > Session` milik Fixed Asset dan cari entri untuk `Sari Lestari` yang dibuat sesudah langkah 17 dimulai
19. Verifikasi Tidak ada entri baru untuk `Sari Lestari` di `Activity Log > Session` milik Fixed Asset untuk kondisi request force-logout ditolak 403
20. Buka `Global Settings > Activity Log > Session` dan cari entri untuk `Sari Lestari` yang dibuat sesudah langkah 17 dimulai
21. Verifikasi Tidak ada entri baru untuk `Sari Lestari` di `Global Settings > Activity Log > Session` untuk kondisi request force-logout ditolak 403
22. Buka `Global Settings > User > Detail > User Log` milik `Sari Lestari` dan cari entri yang dibuat sesudah langkah 17 dimulai
23. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi request force-logout ditolak 403

### TC-AUTH-SES-211: Biometric Re-login gagal karena token invalid tidak dicatat

24. Tutup paksa aplikasi mobile di perangkat Android uji B, hapus data aplikasi, lalu siapkan enrollment `dewianggraini+{runId}-060@qwertysystem.net` sebagai user yang sudah enroll biometric di perangkat (token biometric lokal dan email cache lokal = email itu; Tabel Data Uji Pre-setup #29) tanpa sesi platform aktif, lalu kredensial biometric itu di-revoke di server (kemampuan disediakan tim FE/BE)
25. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
26. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → server menolak (401 token tidak valid), token lokal dihapus, dan halaman Login penuh tampil
27. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Dewi Anggraini` yang dibuat sesudah langkah 25 dimulai
28. Verifikasi Tidak ada entri baru untuk `Dewi Anggraini` di `Global Settings > Activity Log > Session` untuk kondisi Re-login biometric ditolak
29. Buka `Global Settings > User > Detail > User Log` milik `Dewi Anggraini` dan cari entri yang dibuat sesudah langkah 25 dimulai
30. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi Re-login biometric ditolak

### TC-AUTH-SES-195: Client Suspended tidak menulis Session Log Entry

31. Tutup konteks Browser A sebelumnya dan buka konteks baru Browser A dengan memuat sesi web seed milik `Intan Wibowo`
32. Di Browser Principal buka `Admin Console > Client`, buka menu elipsis Client Suspend, dan pilih Suspend
33. Di Browser A (sesi platform web dan sesi-produk Fixed Asset Active `Intan Wibowo`) amati layar
34. Di Browser Admin buka `Global Settings > Activity Log > Session` dan cari entri untuk `Intan Wibowo` yang dibuat sesudah langkah 32 dimulai
35. Verifikasi Tidak ada entri baru untuk `Intan Wibowo` di `Global Settings > Activity Log > Session` untuk kondisi Client Suspended
36. Buka `Activity Log > Session` milik Fixed Asset dan cari entri untuk `Intan Wibowo` yang dibuat sesudah langkah 32 dimulai
37. Verifikasi Tidak ada entri baru untuk `Intan Wibowo` di `Activity Log > Session` milik Fixed Asset untuk kondisi Client Suspended
38. Buka `Global Settings > User > Detail > User Log` milik `Intan Wibowo` dan cari entri yang dibuat sesudah langkah 32 dimulai
39. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi Client Suspended
40. Di Browser Principal buka `Admin Console > Client`, buka menu elipsis Client Suspend, dan pilih Unsuspend

### TC-AUTH-SES-196: Refresh pada Session Expired saat sesi valid tidak dicatat

41. Tutup konteks Browser A sebelumnya dan buka konteks baru Browser A dengan memuat sesi web seed milik `Joko Nugroho`
42. Di Browser A (sesi web Active `Joko Nugroho`; Tab A dan Tab B di Portal — Product Hub; batas idle 15 menit) biarkan tanpa aktivitas dan majukan jam server dan jam browser/perangkat bersama 10 menit → amati Toast
43. Majukan jam server dan jam browser/perangkat bersama 6 menit lagi (idle 16 menit) → Tab A dan Tab B menampilkan Dialog Session Expired
44. Di Tab A klik [Refresh] → halaman Login with Password tampil
45. Di Tab A login ulang dengan `jokonugroho+{runId}-060@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD` → Portal — Product Hub tampil
46. Kembalikan jam server dan jam browser/perangkat uji ke waktu normal
47. Di Browser Admin login ulang dengan akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` dan password `Spectra.env.GS_TC_PASSWORD`, lalu klik [Log in] (sesi aktor kedaluwarsa selama jam digeser)
48. Di Browser Admin buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` milik `Joko Nugroho`, lalu catat jumlah entri sebagai baseline
49. Di Tab B klik [Refresh]
50. Di Browser Admin buka `Global Settings > Activity Log > Session` dan cari entri untuk `Joko Nugroho` (`jokonugroho+{runId}-060@qwertysystem.net`), lalu hitung jumlah entri
51. Verifikasi Tidak ada entri baru untuk `Joko Nugroho` di `Global Settings > Activity Log > Session` untuk kondisi Refresh pada Session Expired saat sesi valid (jumlah entri sama dengan baseline)
52. Buka `Global Settings > User > Detail > User Log` milik `Joko Nugroho` dan hitung jumlah entri
53. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi Refresh pada Session Expired saat sesi valid (jumlah entri sama dengan baseline)

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Kelas harness: asersi absence (kelas g, "tidak ada entri") dengan beberapa jenis harness (multi-konteks, mobile biometric, time-travel) sesuai `P-5` (a): pemicu kelas lain hanya membentuk kondisi yang diasersi tidak tercatat; asersi pencatatan lain ada di spec `TC-AUTH-SES-E2E-056` sampai `059`. TC-AUTH-SES-267 (presence entri `Consent not given`) ada di spec `TC-AUTH-SES-E2E-059-pencatatan-biometric`.
- Penyimpangan urutan (S-05, S-10): urutan di spec ini 190, 202, 203, 211, 195, 196 (urutan TC sumber 190, 195, 196, 202, 203, 211). TC-AUTH-SES-196 menggeser jam server sehingga ditaruh paling akhir; TC-AUTH-SES-195 (Suspend Client lalu Unsuspend) sebelum itu. Tiap TC memakai user sendiri, jadi urutan tidak membuat TC saling bergantung.
- Langkah dependensi disalin (S-04): TC-AUTH-SES-190 dari TC-AUTH-SES-29 (langkah 2–5); TC-AUTH-SES-195 dari TC-AUTH-SES-77 (langkah 32–33); TC-AUTH-SES-196 dari TC-AUTH-SES-49, 55, dan 46 (langkah 42–48: idle 16 menit sampai Dialog Session Expired di dua tab, Tab A [Refresh] dan login ulang, Tab B [Refresh]); TC-AUTH-SES-202 dari TC-AUTH-SES-113 (langkah 11); TC-AUTH-SES-203 dari TC-AUTH-SES-233 (langkah 16–17); TC-AUTH-SES-211 dari TC-AUTH-SES-160 (langkah 25–26). Asersi hasil dependensi (dialog, popup, 403, halaman Login) diuji di spec pemilik TC dependensi.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): perpindahan antar konteks browser dan perangkat; memuat aplikasi ke keadaan awal TC (langkah 24); Unsuspend Client Suspend (langkah 40) dan mengembalikan jam server (langkah 46) sebagai pemulihan state (S-09; hook `after` sebagai cadangan). Entri "baru" dibedakan dari entri seeding lewat stempel waktu: hanya entri yang dibuat sesudah langkah pemicu TC itu yang dihitung (langkah pemicu masing-masing TC); TC-AUTH-SES-196 memakai baseline jumlah entri yang dicatat sebelum aksi.
- Temuan untuk QA:
  - TC-AUTH-SES-202 menulis user milik Client Alpha, sedangkan dependensi TC-AUTH-SES-113 mensyaratkan Client dengan subscription Fixed Asset Archive (Tabel Data Uji Pre-setup #14); spec memakai Client tersebut dan membaca log-nya dengan akun Total Control scope Client Expired/uji (Pre-setup #31).
  - TC-AUTH-SES-203 menyebut user target `Sari Lestari`, sedangkan dependensi TC-AUTH-SES-233 memakai target `Reza Wibowo` dan aktor `Sari Nugroho`; spec memakai `Sari Lestari` sebagai target dan men-seed `Sari Nugroho` sebagai aktor tanpa capability. ID sesi-produk target untuk request langsung tidak disebut TC; spec mengambilnya dari seeding.
  - TC-AUTH-SES-196 Expected tidak menyebut batas waktu entri, padahal langkah dependensi (idle sampai Session Expired dan login ulang, langkah 42–45) dapat menulis entri sendiri; spec mencatat jumlah entri sebagai baseline sesudah jam dipulihkan dan sebelum klik [Refresh] di Tab B, lalu mengasersi jumlah yang sama sesudah [Refresh].
  - TC-AUTH-SES-211 Expected butir "Tidak ada entri baru" tidak menyebut apakah login biometric yang ditolak memunculkan halaman Login; spec hanya mengasersi absence log (halaman Login diuji di spec pemilik TC-AUTH-SES-160).
- Baseline entri log (S-12, S-03): TC-AUTH-SES-196 mencatat jumlah entri `Joko Nugroho` di Activity Log > Session dan User Log sebagai aksi tanpa `Verifikasi` sesudah jam dipulihkan dan sebelum klik [Refresh] di Tab B, karena alur dependensi (idle sampai login ulang) menulis entri sendiri; jam dipulihkan sebelum Browser Admin membuka log (S-09). TC-AUTH-SES-211: langkah 24 mengakhiri sesi platform hasil login enroll lewat Manual Logout di aplikasi (menu Profile → Log Out, lalu app dihapus dari recent apps; Tabel Data Uji Pre-setup #29); jendela absence dimulai sesudah langkah 25 dimulai, sehingga entri login enroll dan entri `Logged out` dari Log Out itu tidak termasuk asersi "tidak ada entri baru". Langkah penghubung ganti akun di Browser A dan di perangkat Android uji B (menyiapkan enrollment, memuat sesi seed) tanpa awalan `Verifikasi` (S-07).
- Temuan untuk QA (lanjutan): TC-AUTH-SES-211 memakai token biometric lokal per user pada satu perangkat; spec memakai cara penyiapan Tabel Data Uji Pre-setup #29. Kemampuan mencabut kredensial biometric `Dewi Anggraini` di server (TC-AUTH-SES-211) disediakan tim FE/BE; cara mencabutnya tidak ditulis di TC.
