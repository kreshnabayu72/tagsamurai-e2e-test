---
id: TC-AUTH-SES-E2E-028-delete-dan-deactivate-akun-web
title: "Deactivate dan Delete Akun User yang Sedang Login di Web"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-90
  - TC-AUTH-SES-92
  - TC-AUTH-SES-88
  - TC-AUTH-SES-89
  - TC-AUTH-SES-91
coverage:
  web: automated
---

# Deactivate dan Delete Akun User yang Sedang Login di Web

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): lima user profil BASE milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON; MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-90: `Budi Setiawan` (`budisetiawan+{runId}-028@qwertysystem.net`)
  - TC-AUTH-SES-92: `Andi Kusuma` (`andikusuma+{runId}-028@qwertysystem.net`)
  - TC-AUTH-SES-88: `Irfan Anggraini` (`irfananggraini+{runId}-028@qwertysystem.net`)
  - TC-AUTH-SES-89: `Tari Wibowo` (`tariwibowo+{runId}-028@qwertysystem.net`)
  - TC-AUTH-SES-91: `Siti Santoso` (`sitisantoso+{runId}-028@qwertysystem.net`)
- Sesi web Active di Browser A (Chrome on Windows) untuk tiap user, dibuat di hook `before` lewat login API pada konteks Browser A masing-masing (Browser A adalah konteks browser terpisah per TC).
- Browser Admin: konteks terpisah dari Browser A, login oleh akun aktor Total Control (Global Settings) di hook `before`; dipakai untuk Toggle Active dan Delete user di `Global Settings > User`.
- Hook `after`: pulihkan koneksi SSE Browser A bila masih terputus; akhiri semua sesi seed, tutup Browser A dan Browser Admin; hapus user yang masih ada (user TC-AUTH-SES-90 dan 92 hanya dinonaktifkan; user TC-AUTH-SES-88, 89, dan 91 sudah terhapus oleh spec, pembersihan melewatinya). Hook tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- State global yang diubah: Toggle Active dan keberadaan user milik spec ini, koneksi SSE Browser A (TC-AUTH-SES-92 dan 91). Pemulihan di hook `after`.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: dua konteks browser bersamaan (Browser A dan Browser Admin); push dialog lifecycle akun lewat SSE ke Browser A; pemutus SSE (Tabel Data Uji Pre-setup #18) yang memutus lalu memulihkan koneksi SSE Browser A; pengamatan respons HTTP request dari Browser A (status 401 beserta alasannya); pembacaan status sesi platform (Active, Force Logged Out) dari BE oleh akun aktor; reCAPTCHA mode uji di environment untuk login web di halaman Login with Password (TC-AUTH-SES-89).
- Akun yang dipakai: user uji masing-masing TC (bukan akun aktor) pada Browser A; akun aktor Total Control (Global Settings) pada Browser Admin.

## Test Steps

### TC-AUTH-SES-90: Admin menonaktifkan akun user yang sedang login memunculkan Dialog Account Deactivated dan auto-logout

1. Di Browser A buka Portal — Product Hub sebagai `budisetiawan+{runId}-028@qwertysystem.net` → halaman Portal — Product Hub tampil
2. Di Browser Admin buka `Global Settings > User` dan cari `Budi Setiawan` (`budisetiawan+{runId}-028@qwertysystem.net`)
3. Matikan Toggle Active untuk `budisetiawan+{runId}-028@qwertysystem.net` → Toggle Active OFF
4. Pindah ke Browser A dan amati layar → Dialog muncul
5. Susuri dialog dari atas ke bawah
6. Verifikasi Dialog "Account Deactivated" tampil dengan Body "Your account has been deactivated. You will be logged out."
7. Verifikasi Dialog hanya memuat satu tombol [OK]
8. Klik [OK] pada dialog di Browser A
9. Verifikasi Browser A diarahkan ke halaman Login
10. Verifikasi Sesi platform `Budi Setiawan` berstatus Force Logged Out

### TC-AUTH-SES-92: Akun dinonaktifkan saat user offline: Dialog Account Deactivated muncul pada request berikutnya

11. Di Browser A buka Portal — Product Hub sebagai `andikusuma+{runId}-028@qwertysystem.net` → halaman Portal — Product Hub tampil
12. Putuskan koneksi SSE Browser A dengan pemutus SSE → koneksi SSE Browser A terputus
13. Di Browser Admin buka `Global Settings > User` dan cari `Andi Kusuma` (`andikusuma+{runId}-028@qwertysystem.net`)
14. Matikan Toggle Active untuk `andikusuma+{runId}-028@qwertysystem.net` → Toggle Active OFF
15. Di Browser A pulihkan koneksi SSE
16. Di Browser A klik menu apa pun sehingga request dikirim
17. Verifikasi Server menjawab 401 dengan alasan akun dinonaktifkan
18. Verifikasi Dialog "Account Deactivated" tampil di Browser A
19. Verifikasi User `Andi Kusuma` ter-logout dari Browser A

### TC-AUTH-SES-88: Admin menghapus akun user yang sedang login memunculkan Dialog Account no longer Active dan auto-logout

20. Di Browser A buka Portal — Product Hub sebagai `irfananggraini+{runId}-028@qwertysystem.net` → halaman Portal — Product Hub tampil
21. Di Browser Admin buka `Global Settings > User` dan cari `Irfan Anggraini` (`irfananggraini+{runId}-028@qwertysystem.net`)
22. Hapus user tersebut sampai konfirmasi selesai → user terhapus
23. Pindah ke Browser A dan amati layar → Dialog muncul
24. Susuri dialog dari atas ke bawah
25. Verifikasi Dialog "Account no longer Active" tampil dengan Body "Your account has been deleted. You will be logged out."
26. Verifikasi Dialog hanya memuat satu tombol [OK]
27. Verifikasi Sesi platform `Irfan Anggraini` berstatus Force Logged Out

### TC-AUTH-SES-89: OK pada Dialog Account no longer Active mengarah ke Login dan akun tidak dapat login lagi

28. Di Browser A buka Portal — Product Hub sebagai `tariwibowo+{runId}-028@qwertysystem.net` → halaman Portal — Product Hub tampil
29. Di Browser Admin buka `Global Settings > User` dan cari `Tari Wibowo` (`tariwibowo+{runId}-028@qwertysystem.net`)
30. Hapus user tersebut sampai konfirmasi selesai → user terhapus
31. Pindah ke Browser A → Dialog "Account no longer Active" muncul
32. Klik [OK] pada dialog di Browser A
33. Verifikasi Browser A diarahkan ke halaman Login
34. Di halaman Login ketik email `tariwibowo+{runId}-028@qwertysystem.net` dan password lama `Spectra.env.SES_PASSWORD`, lalu klik [Log in]
35. Verifikasi Login ditolak karena akun sudah dihapus
36. Verifikasi Sesi tidak dibuat untuk `Tari Wibowo`

### TC-AUTH-SES-91: Akun dihapus saat user offline: request berikutnya 401 dengan alasan dan Dialog Account no longer Active

37. Di Browser A buka Portal — Product Hub sebagai `sitisantoso+{runId}-028@qwertysystem.net` → halaman Portal — Product Hub tampil
38. Putuskan koneksi SSE Browser A dengan pemutus SSE → koneksi SSE Browser A terputus
39. Di Browser Admin buka `Global Settings > User` dan cari `Siti Santoso` (`sitisantoso+{runId}-028@qwertysystem.net`)
40. Hapus user tersebut sampai konfirmasi selesai → user terhapus
41. Di Browser A pulihkan koneksi SSE
42. Di Browser A klik menu apa pun sehingga request dikirim
43. Verifikasi Server menjawab 401 dengan alasan akun dihapus
44. Verifikasi Dialog "Account no longer Active" tampil di Browser A
45. Verifikasi User `Siti Santoso` ter-logout dari Browser A

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan (S-05, S-10): urutan di spec ini TC-AUTH-SES-90, 92, 88, 89, 91 (urutan TC sumber 88, 89, 90, 91, 92). Deactivate (90, 92) dijalankan lebih dulu, aksi Delete (88, 89, 91) di akhir karena menghabisi data user. Tiap TC memakai user sendiri sehingga urutan tidak membuat TC saling bergantung.
- Dependensi disalin sebagai langkah (S-04): TC-AUTH-SES-90 berdependensi pada TC-AUTH-SES-7 (langkah 1 sampai 5 menyalin buka Portal, Deactivate oleh admin, dialog muncul, dan menyusuri dialog); TC-AUTH-SES-88 pada TC-AUTH-SES-6 (langkah 20 sampai 24 dengan pola yang sama untuk Delete); TC-AUTH-SES-89 pada TC-AUTH-SES-88 (langkah 28 sampai 31). Asersi screening dialog (Header dan Footer) milik TC-AUTH-SES-6 dan 7 diuji di spec screening modul ini.
- Ukuran spec 45 langkah: tiap TC memakai user dan konteks Browser A sendiri (sesi disiapkan lewat API), sehingga TC sesudahnya tetap bermakna bila TC sebelumnya gagal; Deactivate (TC-AUTH-SES-90, 92) di depan dan Delete (TC-AUTH-SES-88, 89, 91) di akhir karena menghabisi data (prinsip 5).
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): perpindahan antar Browser A dan Browser Admin; menyusuri dialog tanpa klik; memutus dan memulihkan koneksi SSE.
- Asersi pencatatan sesi (Activity Log > Session dan User Log) untuk `Account deactivated` dan `Account deleted` tidak diasersikan di spec ini; pencatatan diuji di spec pencatatan dan absence modul ini (S-05).
- Temuan untuk QA: (1) TC-AUTH-SES-88, 89, 90, 91, 92 tidak menyebut label dialog konfirmasi Delete atau tombol aksi Delete di `Global Settings > User`; spec memakai deskripsi aksi dari TC ("hapus user sampai konfirmasi selesai") tanpa mengarang label. (2) TC-AUTH-SES-91 dan 92 menulis "ter-logout" tanpa menyebut bentuknya (status sesi atau halaman Login) dan tidak menyebut Body dialog; spec hanya mengasersi judul dialog dan user ter-logout. (3) TC-AUTH-SES-89 menulis "password lama" tanpa nilai dan tidak menyebut bentuk penolakan login (pesan error atau caption); spec memakai `Spectra.env.SES_PASSWORD` dan mengasersi penolakan tanpa teks. (4) TC-AUTH-SES-89 mengetik email dan password lalu klik [Log in] tanpa menyebut widget reCAPTCHA; spec mengikuti TC tanpa langkah reCAPTCHA, dan kemampuan reCAPTCHA mode uji dicatat di Prerequisites. (5) TC-AUTH-SES-88, 90, 91, 92 menyebut status sesi (Force Logged Out) tanpa menyebut permukaan tempat status dibaca; spec membacanya dari BE oleh akun aktor.
