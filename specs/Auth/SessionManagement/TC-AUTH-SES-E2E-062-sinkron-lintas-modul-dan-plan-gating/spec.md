---
id: TC-AUTH-SES-E2E-062-sinkron-lintas-modul-dan-plan-gating
title: "Sinkron Lintas Modul dan Plan Gating: Status User, Kuota Concurrent, Plan, dan Change Password"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-219
  - TC-AUTH-SES-220
  - TC-AUTH-SES-222
  - TC-AUTH-SES-299
coverage:
  web: automated
---

# Sinkron Lintas Modul dan Plan Gating: Status User, Kuota Concurrent, Plan, dan Change Password

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`; akun ini sudah login di Browser Admin pada hook), password semua user `Spectra.env.SES_PASSWORD`, email bersuffix per run. Semua user Activated, Active ON, MFA dan Agreement tidak terpicu, profil BASE:
  - TC-AUTH-SES-220: `Lestari Permata` (`lestaripermata+{runId}-062@qwertysystem.net`), milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5)
  - TC-AUTH-SES-219: milik Client Q2 (Tabel Data Uji Pre-setup #12: subscription Fixed Asset dan Supply Asset Active, kuota masing-masing 2; App Access Fixed Asset dan Supply Asset): `Hendra Santoso` (`hendrasantoso+{runId}-062@qwertysystem.net`), `Rizky Nugroho` (`rizkynugroho+{runId}-062@qwertysystem.net`), dan `Nur Maulana` (`nurmaulana+{runId}-062@qwertysystem.net`); dua user seed pemegang seat `Gunawan Prakoso` (`gunawanprakoso+{runId}-062@qwertysystem.net`) dan `Melati Anggun` (`melatianggun+{runId}-062@qwertysystem.net`) (Tabel Data Uji Pre-setup #7) dengan sesi-produk Fixed Asset Active di-seed lewat login API dan pembukaan produk API sehingga 2 seat terpakai
  - TC-AUTH-SES-222: `Putri Pratama` (`putripratama+{runId}-062@qwertysystem.net`) milik Client dengan plan Starter dan `Eko Ramadhan` (`ekoramadhan+{runId}-062@qwertysystem.net`) milik Client dengan plan Enterprise (Tabel Data Uji Pre-setup #21; batas idle 15 menit)
  - TC-AUTH-SES-299: `Siti Firmansyah` (`sitifirmansyah+{runId}-062@qwertysystem.net`) milik Client dengan plan Growth dan `Andi Damayanti` (`andidamayanti+{runId}-062@qwertysystem.net`) milik Client dengan plan Professional (Tabel Data Uji Pre-setup #21; batas idle 15 menit)
- Akun aktor Total Control untuk seeding dan pembacaan user Client Q2 (TC-AUTH-SES-219) adalah akun Total Control dengan scope Client Q2 (Tabel Data Uji Pre-setup #26); akun Total Control tanpa Client dipakai untuk user Client Alpha Logistik dan Client per plan.
- Akun aktor lain (login eksplisit di langkah, ganti konteks): Principal Admin Console `principalAdminConsole_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #4), `Spectra.env.AC_PRINCIPAL_PASSWORD`, untuk mengubah kuota di `Admin Console > License Allocation` (TC-AUTH-SES-219); Admin License `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #2), `Spectra.env.FA_MGL_PASSWORD`, untuk melihat `PLATFORM SETTINGS > License > Concurrent User` (TC-AUTH-SES-219).
- Suite berjalan serial (`parallel: false`); state global yang diubah: kuota Fixed Asset Client Q2, seat dan sesi-produk Client Q2, jam server dan jam browser/perangkat, Toggle Active `Lestari Permata`, dipulihkan di hook `after`: kuota dikembalikan ke 2 lewat `Admin Console > License Allocation`; seat dan sesi-produk Client Q2 dilepas; jam server dan jam browser/perangkat dikembalikan ke waktu nyata; Toggle Active `Lestari Permata` ON. Jam server dan jam browser/perangkat diatur bersama; tiap TC yang memajukannya memulihkan keduanya dengan langkah eksplisit.
- Hook `after`: pulihkan state global di atas; akhiri semua sesi seed; tutup semua konteks browser; hapus seluruh user. Pembersihan tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`, `AC_PRINCIPAL_PASSWORD`, `FA_MGL_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: banyak konteks browser bersamaan (Browser Admin, Browser A dan B Chrome on Windows / Firefox on Windows dengan user agent yang dapat ditetapkan, Browser Principal, Browser Lisensi, Browser Q1 sampai Q3); pengatur waktu server uji dan jam browser/perangkat yang dimajukan bersama (Tabel Data Uji Pre-setup #18); Client dengan plan Starter, Growth, Professional, dan Enterprise (satu Client per plan) serta Client Q2; reCAPTCHA mode uji di environment (halaman Login with Password).

## Test Steps

### TC-AUTH-SES-220: Status user dibaca dari Global Settings tanpa salinan di Session Management

1. Di Browser A (Chrome on Windows) login dengan `lestaripermata+{runId}-062@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil
2. Di Browser Admin buka `Global Settings > User`, cari `Lestari Permata`, dan matikan Toggle Active
3. Di Browser A amati layar → Dialog "Account Deactivated" tampil dengan Body "Your account has been deactivated. You will be logged out." dan satu tombol [OK]
4. Di Browser Admin nyalakan kembali Toggle Active `Lestari Permata`
5. Di Browser A klik [OK] pada dialog → halaman Login tampil
6. Di Browser A login ulang dengan `lestaripermata+{runId}-062@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in]
7. Verifikasi Login ulang berhasil mengikuti status Active terkini dari Global Settings: Portal — Product Hub tampil
8. Verifikasi Tidak ada status user yang bertahan basi di sesi lama: Dialog "Account Deactivated" tidak muncul lagi di Browser A

### TC-AUTH-SES-219: Kuota concurrent dibaca dari License Allocation dan perubahan berlaku pada pembukaan berikutnya

9. Buka Browser Principal (konteks baru) dan login sebagai `principalAdminConsole_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.AC_PRINCIPAL_PASSWORD`
10. Di Browser Principal buka `Admin Console > License Allocation`
11. Ubah kuota Fixed Asset Client Q2 dari 2 ke 4 dan simpan
12. Di Browser Q1 (konteks baru) login dengan `hendrasantoso+{runId}-062@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil
13. Di Browser Q1 klik card Fixed Asset
14. Verifikasi Seat 3 berhasil dibuka tanpa popup: `Hendra Santoso` masuk Fixed Asset
15. Di Browser Q2 (konteks baru) login dengan `rizkynugroho+{runId}-062@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil
16. Di Browser Q2 klik card Fixed Asset
17. Verifikasi Seat 4 berhasil dibuka tanpa popup: `Rizky Nugroho` masuk Fixed Asset
18. Di Browser Q3 (konteks baru) login dengan `nurmaulana+{runId}-062@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil
19. Di Browser Q3 klik card Fixed Asset (seat ke-5)
20. Verifikasi Seat ke-5 memunculkan Popup "Concurrent session limit reached"
21. Buka Browser Lisensi (konteks baru) dan login sebagai `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.FA_MGL_PASSWORD`
22. Di Browser Lisensi buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset)
23. Verifikasi Menu `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset) tidak dipakai untuk mengubah kuota: tidak ada kontrol untuk mengubah nilai kuota

### TC-AUTH-SES-222: Limit login, idle timeout, dan dialog lifecycle tidak plan-gated (Starter dan Enterprise)

24. Tutup konteks Browser A dan Browser B TC/akun sebelumnya (hapus sesi login browser), lalu di Browser A (konteks baru, Chrome on Windows) login dengan `putripratama+{runId}-062@qwertysystem.net` (plan Starter) dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil
25. Di Browser B (konteks baru, Firefox on Windows) login dengan akun yang sama dan klik [Log in] → Dialog "Duplicate Login Attempt" tampil
26. Verifikasi Dialog "Duplicate Login Attempt" tampil di Browser B untuk plan Starter dengan Body "You are already signed in on another device: Chrome on Windows. Confirm to log out that session and continue here."
27. Klik [Cancel] pada Dialog Duplicate Login Attempt
28. Biarkan Browser A tanpa aktivitas dan majukan jam server dan jam browser/perangkat bersama 16 menit (melewati batas idle 15 menit) → Dialog "Session Expired" tampil di Browser A
29. Verifikasi Dialog "Session Expired" tampil di Browser A untuk plan Starter dengan Body "Your session has expired due to inactivity." dan satu tombol [Refresh]
30. Pulihkan jam server dan jam browser/perangkat ke waktu nyata
31. Tutup konteks Browser A dan Browser B TC/akun sebelumnya (hapus sesi login browser), lalu di Browser A (konteks baru, Chrome on Windows) login dengan `ekoramadhan+{runId}-062@qwertysystem.net` (plan Enterprise) dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil
32. Di Browser B (konteks baru, Firefox on Windows) login dengan akun yang sama dan klik [Log in] → Dialog "Duplicate Login Attempt" tampil
33. Verifikasi Dialog "Duplicate Login Attempt" tampil di Browser B untuk plan Enterprise dengan Body "You are already signed in on another device: Chrome on Windows. Confirm to log out that session and continue here."
34. Klik [Cancel] pada Dialog Duplicate Login Attempt
35. Biarkan Browser A tanpa aktivitas dan majukan jam server dan jam browser/perangkat bersama 16 menit (melewati batas idle 15 menit) → Dialog "Session Expired" tampil di Browser A
36. Verifikasi Dialog "Session Expired" tampil di Browser A untuk plan Enterprise dengan Body "Your session has expired due to inactivity." dan satu tombol [Refresh]
37. Pulihkan jam server dan jam browser/perangkat ke waktu nyata
38. Verifikasi Tidak ada perbedaan perilaku berdasarkan plan: Dialog Duplicate Login Attempt dan Dialog Session Expired pada plan Starter (langkah 26 dan 29) sama dengan plan Enterprise (langkah 33 dan 36)

### TC-AUTH-SES-299: Limit login dan dialog lifecycle sama untuk plan Growth dan Professional

39. Tutup konteks Browser A dan Browser B TC/akun sebelumnya (hapus sesi login browser), lalu di Browser A (konteks baru, Chrome on Windows) login dengan `sitifirmansyah+{runId}-062@qwertysystem.net` (plan Growth) dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil
40. Di Browser B (konteks baru, Firefox on Windows) login dengan akun yang sama dan klik [Log in] → Dialog "Duplicate Login Attempt" tampil
41. Verifikasi Dialog "Duplicate Login Attempt" tampil di Browser B untuk plan Growth dengan Body "You are already signed in on another device: Chrome on Windows. Confirm to log out that session and continue here."
42. Klik [Cancel] pada Dialog Duplicate Login Attempt
43. Biarkan Browser A tanpa aktivitas dan majukan jam server dan jam browser/perangkat bersama 16 menit (melewati batas idle 15 menit) → Dialog "Session Expired" tampil di Browser A
44. Verifikasi Dialog "Session Expired" tampil di Browser A untuk plan Growth dengan Body "Your session has expired due to inactivity." dan satu tombol [Refresh]
45. Pulihkan jam server dan jam browser/perangkat ke waktu nyata
46. Tutup konteks Browser A dan Browser B TC/akun sebelumnya (hapus sesi login browser), lalu di Browser A (konteks baru, Chrome on Windows) login dengan `andidamayanti+{runId}-062@qwertysystem.net` (plan Professional) dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil
47. Di Browser B (konteks baru, Firefox on Windows) login dengan akun yang sama dan klik [Log in] → Dialog "Duplicate Login Attempt" tampil
48. Verifikasi Dialog "Duplicate Login Attempt" tampil di Browser B untuk plan Professional dengan Body "You are already signed in on another device: Chrome on Windows. Confirm to log out that session and continue here."
49. Klik [Cancel] pada Dialog Duplicate Login Attempt
50. Biarkan Browser A tanpa aktivitas dan majukan jam server dan jam browser/perangkat bersama 16 menit (melewati batas idle 15 menit) → Dialog "Session Expired" tampil di Browser A
51. Verifikasi Dialog "Session Expired" tampil di Browser A untuk plan Professional dengan Body "Your session has expired due to inactivity." dan satu tombol [Refresh]
52. Pulihkan jam server dan jam browser/perangkat ke waktu nyata
53. Verifikasi Pada kedua plan Dialog Duplicate Login Attempt dan Dialog Session Expired tampil sama seperti plan lain (langkah 41, 44, 48, dan 51 sama dengan langkah 26, 29, 33, dan 36)

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Spec memuat 53 langkah karena empat TC lintas modul dan plan masing-masing butuh konteks akun sendiri; bagian setelah sebuah TC tetap bermakna walau TC sebelumnya gagal karena tiap TC memakai user dan sesinya sendiri.
- Penyimpangan urutan (S-05, S-10): urutan di spec ini TC-AUTH-SES-220, 219, 222, 299 (urutan TC sumber 219, 220, 222, 299). TC-AUTH-SES-220 ditaruh paling awal karena akun aktor pertama di hook adalah Total Control (Global Settings); TC-AUTH-SES-219 mengubah kuota Client Q2 dan butuh ganti akun ke Principal; TC-AUTH-SES-299 menyusul TC-AUTH-SES-222 sesuai kolom Dependensi (pola langkah identik, plan berbeda).
- Dependensi disalin sebagai langkah (S-04): TC-AUTH-SES-220 menyalin langkah TC-AUTH-SES-90 (langkah 2 sampai 3); TC-AUTH-SES-219 memakai seeding seat dari TC-AUTH-SES-124 dan TC-AUTH-SES-127 lewat API di hook; TC-AUTH-SES-299 menyalin langkah TC-AUTH-SES-222 (plan berbeda). Asersi pada langkah 3 mengikuti Expected dependensi yang disalin dan tidak ada di Expected TC-AUTH-SES-220 sendiri (S-03).
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): login user uji (langkah pembuka tiap bagian plan juga menutup konteks Browser A dan Browser B sebelumnya dan menghapus sesi login browser, S-09); ganti akun ke Principal dan Admin License; memajukan dan memulihkan waktu server; menutup dialog dengan [Cancel] atau [OK].
- Asersi Body dan tombol dialog pada langkah 26, 29, 33, 36, 41, 44, 48, dan 51 mengambil teks dari PRD §4 dan Expected TC-AUTH-SES-1 dan TC-AUTH-SES-46 yang disalin sebagai dependensi; Expected TC-AUTH-SES-222 dan 299 hanya menyebut dialog tampil sama (S-03).
- TC-AUTH-SES-223 (sinkron Change Password pada tiga perangkat Android) ada di spec `TC-AUTH-SES-E2E-073`.
- Temuan untuk QA: (1) TC-AUTH-SES-219 menyebut "user Client Q2" tanpa nama; spec memakai `Hendra Santoso`, `Rizky Nugroho`, dan `Nur Maulana` dari TC dependensi TC-AUTH-SES-127 dan 124, serta dua seat awal dari user seed `Gunawan Prakoso` dan `Melati Anggun`. (2) TC-AUTH-SES-219 Expected c ("menu Concurrent User tidak dipakai untuk mengubah kuota") tidak menyebut cara memeriksanya, dan akun Admin License (Tabel Data Uji Pre-setup #2) tidak dinyatakan milik Client Q2; spec memeriksa tidak adanya kontrol ubah kuota di halaman itu dengan akun tersebut. (3) TC-AUTH-SES-220 Expected b ("tidak ada status user yang bertahan basi di sesi lama") ambigu; spec mengasersinya sebagai Dialog Account Deactivated tidak muncul lagi setelah login ulang. (4) TC-AUTH-SES-222 dan 299 menyebut batas idle 15 menit pada Client per plan tanpa menyatakan nilai itu di Tabel Data Uji Pre-setup #21; spec mengandalkan batas idle 15 menit di-seed BE. (5) TC-AUTH-SES-219 mengubah kuota dan seat Client Q2 yang dipakai bersama TC-AUTH-SES-240 (spec `TC-AUTH-SES-E2E-065`) dan TC lain di suite; suite berjalan serial dan kuota dipulihkan ke 2 di hook `after`.
