---
id: TC-AUTH-SES-E2E-012-dialog-lifecycle-multi-tab
title: "Dialog Lifecycle Multi-Tab: OK Hanya Berlaku untuk Tab yang Diklik dan Dua Dialog Duplicate Login Bersamaan"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-28
  - TC-AUTH-SES-79
  - TC-AUTH-SES-94
  - TC-AUTH-SES-262
  - TC-AUTH-SES-135
  - TC-AUTH-SES-321
coverage:
  web: automated
---

# Dialog Lifecycle Multi-Tab: OK Hanya Berlaku untuk Tab yang Diklik dan Dua Dialog Duplicate Login Bersamaan

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`, dengan scope Client sesuai tiap user di bawah): enam user profil BASE (Activated, Active ON; MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-28: `Nadia Hidayat` (`nadiahidayat+{runId}-012@qwertysystem.net`), Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5), disiapkan oleh akun aktor Total Control (Tabel Data Uji Pre-setup #1)
  - TC-AUTH-SES-79: `Joko Pratama` (`jokopratama+{runId}-012@qwertysystem.net`), Client Suspend (Tabel Data Uji Pre-setup #16), disiapkan oleh akun aktor Total Control (Global Settings) dengan scope Client Suspend (Tabel Data Uji Pre-setup #32)
  - TC-AUTH-SES-94: `Rizky Lestari` (`rizkylestari+{runId}-012@qwertysystem.net`), Client `Alpha Logistik`
  - TC-AUTH-SES-262: `Reza Utami` (`rezautami+{runId}-012@qwertysystem.net`), Client `Alpha Logistik`
  - TC-AUTH-SES-135: `Intan Puspita` (`intanpuspita+{runId}-012@qwertysystem.net`), Client Q2 (Tabel Data Uji Pre-setup #12: subscription Fixed Asset dan Supply Asset Active, kuota masing-masing 2) dengan App Access Fixed Asset dan Supply Asset, disiapkan oleh akun aktor Total Control (Global Settings) dengan scope Client Q2 (Tabel Data Uji Pre-setup #26)
  - TC-AUTH-SES-321: `Reza Anggraini` (`rezaanggraini+{runId}-012@qwertysystem.net`), Client `Alpha Logistik`
- Sesi aktif (status Active, Chrome on Windows) dibuat di hook `before` lewat login API sebagai kondisi yang di-seed BE:
  - TC-AUTH-SES-28, 79, 94, 262, 135: sesi web di Browser A yang dibuka pada dua tab (Tab A1 dan Tab A2), keduanya di Portal — Product Hub;
  - TC-AUTH-SES-135: ditambah sesi-produk Fixed Asset Active milik `Intan Puspita` (seat Client Q2 terpakai 1);
  - TC-AUTH-SES-321: sesi web di Browser A satu tab.
- Browser B dan Browser C (TC-AUTH-SES-28 dan 321) adalah konteks baru Firefox on macOS yang belum login.
- Browser Admin: konteks terpisah dari Browser A. Akun admin yang dipakai (login pertama di hook `before` memakai akun TC-AUTH-SES-79; pergantian akun berikutnya ditulis sebagai langkah eksplisit):
  - Principal Admin Console `principalAdminConsole_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_PRINCIPAL_PASSWORD` (Suspend Client Suspend, TC-AUTH-SES-79);
  - Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD` (hapus user TC-AUTH-SES-94; matikan Toggle Active TC-AUTH-SES-262).
- Browser License: konteks terpisah dari Browser A dan Browser Admin, dibuka pada TC-AUTH-SES-135 dengan akun Admin License `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_MGL_PASSWORD`, Global Role Manage Global License dengan scope Client Q2 (Tabel Data Uji Pre-setup #2 dan #33; force-logout TC-AUTH-SES-135).
- Suite berjalan serial (`parallel: false`); state global yang diubah: status Client Suspend (TC-AUTH-SES-79) dan seat Fixed Asset Client Q2 (TC-AUTH-SES-135), dipulihkan di hook `after`.
- State global yang diubah: status Client Suspend (Tabel Data Uji Pre-setup #16) menjadi Suspended pada TC-AUTH-SES-79 (efek: Last Updated Client Suspend berubah), dan seat Fixed Asset Client Q2 terpakai oleh sesi-produk TC-AUTH-SES-135. Pemulihan di hook `after`: Unsuspend Client Suspend lewat akun Principal bila masih Suspended, akhiri sesi-produk seed, logout Browser Admin dan Browser License.
- Hook `after`: selain pemulihan di atas, akhiri semua sesi seed dan sesi yang dibuat spec, tutup konteks Browser A, B, C, Admin, dan License, hapus keenam user (termasuk user yang sudah dihapus atau dinonaktifkan oleh spec). Hook ini tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`, `AC_PRINCIPAL_PASSWORD`, `FA_MGL_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness c: multi-tab dan multi-konteks):
  - satu konteks browser dengan dua tab bersamaan (Tab A1 dan Tab A2) yang berbagi satu sesi dan sama-sama menerima push SSE;
  - konteks Browser B, C, Admin, dan License bersamaan dengan Browser A;
  - pembacaan data sesi platform per user (status Active, Force Logged Out), disediakan tim FE/BE tanpa endpoint tertentu;
  - reCAPTCHA mode uji di environment (halaman Login with Password).
- Akun yang dipakai: user uji pada Browser A, B, dan C; akun admin pada Browser Admin dan Browser License sesuai daftar di atas.

## Test Steps

### TC-AUTH-SES-28: Dialog Logged Out tampil di semua tab dan OK hanya berlaku untuk tab yang diklik

1. Buka konteks Browser B baru (Firefox on macOS, belum login), lalu buka halaman `Auth > Login with Password` → halaman Login with Password tampil
2. Ketik email `nadiahidayat+{runId}-012@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Dialog "Duplicate Login Attempt" muncul
3. Klik [Confirm]
4. Pindah ke Browser A dan amati Tab A1 dan Tab A2
5. Verifikasi Dialog "Logged Out" tampil di Tab A1
6. Verifikasi Dialog "Logged Out" tampil di Tab A2
7. Di Tab A1 klik [OK]
8. Verifikasi Tab A1 diarahkan ke halaman Login
9. Amati Tab A2
10. Verifikasi Tab A2 masih menampilkan Dialog "Logged Out" sampai [OK] diklik di tab itu

### TC-AUTH-SES-79: Dialog Access Restricted tampil di semua tab dan OK hanya berlaku untuk tab itu

11. Di Browser Admin (login sebagai `principalAdminConsole_automated_{namaCompany}@qwertysystem.net` dari hook `before`) buka `Admin Console > Client`, buka menu elipsis Client Suspend dan pilih Suspend
12. Pindah ke Browser A dan amati Tab A1 dan Tab A2
13. Verifikasi Dialog "Access Restricted" tampil di Tab A1
14. Verifikasi Dialog "Access Restricted" tampil di Tab A2
15. Di Tab A1 klik [OK]
16. Verifikasi Setelah [OK] di Tab A1, hanya Tab A1 yang ter-refresh
17. Amati Tab A2
18. Verifikasi Tab A2 masih menampilkan Dialog "Access Restricted" sampai [OK] diklik di tab itu
19. Di Browser Admin buka `Admin Console > Client`, buka menu elipsis Client Suspend dan pilih Unsuspend (pemulihan status Client Suspend)

### TC-AUTH-SES-94: Dialog akun dihapus tampil di semua tab dan OK hanya berlaku untuk tab itu

20. Di Browser Admin keluar dari akun `principalAdminConsole_automated_{namaCompany}@qwertysystem.net`, lalu login sebagai `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan password `Spectra.env.GS_TC_PASSWORD`
21. Di Browser Admin buka `Global Settings > User`, cari `Rizky Lestari`, lalu hapus user
22. Pindah ke Browser A dan amati Tab A1 dan Tab A2
23. Verifikasi Dialog "Account no longer Active" tampil di Tab A1
24. Verifikasi Dialog "Account no longer Active" tampil di Tab A2
25. Di Tab A1 klik [OK]
26. Verifikasi Tab A1 diarahkan ke halaman Login setelah [OK]
27. Amati Tab A2
28. Verifikasi Tab A2 tetap menampilkan Dialog "Account no longer Active" sampai [OK] diklik di tab itu

### TC-AUTH-SES-262: Dialog Account Deactivated tampil di semua tab dan OK hanya berlaku untuk tab itu

29. Di Browser Admin buka `Global Settings > User`, cari `Reza Utami`, lalu matikan Toggle Active
30. Pindah ke Browser A dan amati Tab A1 dan Tab A2
31. Verifikasi Dialog "Account Deactivated" tampil di Tab A1
32. Verifikasi Dialog "Account Deactivated" tampil di Tab A2
33. Di Tab A1 klik [OK]
34. Verifikasi Tab A1 diarahkan ke halaman Login setelah [OK]
35. Amati Tab A2
36. Verifikasi Tab A2 tetap menampilkan Dialog "Account Deactivated" sampai [OK] diklik di tab itu

### TC-AUTH-SES-135: Dialog Log Out tampil di semua tab dan OK hanya berlaku untuk tab itu

37. Buka konteks Browser License baru (belum login), lalu login sebagai `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` dengan password `Spectra.env.FA_MGL_PASSWORD`
38. Di Browser License buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset), pilih `Intan Puspita`, lalu klik [Force Logout] dan [Confirm Logout]
39. Pindah ke Browser A dan amati Tab A1 dan Tab A2
40. Verifikasi Dialog "Log Out" tampil di Tab A1
41. Verifikasi Dialog "Log Out" tampil di Tab A2
42. Di Tab A1 klik [OK]
43. Amati Tab A2
44. Verifikasi Tab A2 masih menampilkan Dialog "Log Out" setelah [OK] di Tab A1

### TC-AUTH-SES-321: Dua dialog Duplicate Login terbuka bersamaan: Confirm kedua meng-invalidate sesi aktif saat itu

45. Tutup konteks Browser B TC sebelumnya (hapus sesi login browser), buka konteks Browser B baru (Firefox on macOS, belum login), lalu buka halaman `Auth > Login with Password` → halaman Login with Password tampil
46. Di Browser B ketik email `rezaanggraini+{runId}-012@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Dialog "Duplicate Login Attempt" muncul
47. Buka konteks Browser C baru (belum login), lalu buka halaman `Auth > Login with Password` → halaman Login with Password tampil
48. Di Browser C ketik email `rezaanggraini+{runId}-012@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Dialog "Duplicate Login Attempt" muncul
49. Di Browser B klik [Confirm] (sesi Browser A di-invalidate)
50. Verifikasi Browser B masuk Portal — Product Hub
51. Verifikasi Sesi Browser A berstatus Force Logged Out
52. Di Browser C klik [Confirm]
53. Verifikasi Browser C masuk Portal — Product Hub
54. Verifikasi Browser C memakai sesi baru
55. Verifikasi Sesi Browser B yang ada saat [Confirm] di Browser C diproses di-invalidate
56. Pindah ke Browser A
57. Verifikasi Browser A tidak menerima dialog kedua

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pembagian TC lintas spec: screening isi Dialog Logged Out ada di `TC-AUTH-SES-E2E-001-screening-dialog-duplicate-login-dan-logged-out` (TC-AUTH-SES-2), sedangkan isi dialog Account Deactivated (TC-AUTH-SES-7) dan Access Restricted (TC-AUTH-SES-77) diuji di spec lain pada rencana. Spec ini hanya menguji perilaku multi-tab.
- Urutan mengikuti TC sumber (28, 79, 94, 262, 135, 321); tidak ada penyimpangan (S-05, S-10). Aksi yang menghapus atau menonaktifkan user (TC-AUTH-SES-94 dan 262) hanya memengaruhi user milik TC itu sendiri, sehingga tidak perlu ditaruh paling akhir.
- TC-AUTH-SES-79 berdependensi pada TC-AUTH-SES-77 (Suspend Client Suspend); langkah 11 menyalin langkah itu (S-04). TC-AUTH-SES-262 berdependensi pada TC-AUTH-SES-7 (matikan Toggle Active hingga dialog tampil); langkah 29 menyalin langkah itu. Asersi sesi, seat, dan pencatatan dari TC-AUTH-SES-77 diuji di spec lain.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03, S-07, S-09): membuka konteks Browser B, C, dan License baru (serta menutup konteks Browser B TC sebelumnya pada langkah 45); berpindah antar Browser A, Admin, dan License; Unsuspend Client Suspend (langkah 19) sebagai pemulihan state sebelum TC berikutnya, dengan hook `after` sebagai cadangan; pergantian akun di Browser Admin (langkah 20) dan login akun Admin License di Browser License (langkah 37).
- Pencatatan: TC sumber batch ini tidak memuat asersi "tidak ada pencatatan"; asersi absence dikerjakan di spec absence (060).
- Temuan untuk QA: (1) TC-AUTH-SES-94 dan 262 menulis "hapus user" dan "matikan Toggle Active" tanpa menyebut layar atau dialog konfirmasi; spec memakai `Global Settings > User` mengikuti TC-AUTH-SES-7 dan tidak menambah langkah konfirmasi. (2) TC-AUTH-SES-79 tidak menyebut dialog konfirmasi Suspend maupun akun yang membuat user di Client Suspend; spec memakai akun aktor Total Control dengan scope Client Suspend (Pre-setup #32) untuk seeding user di Client Suspend dan Principal untuk Suspend. (3) TC-AUTH-SES-321 Expected c ("Browser A tidak menerima dialog kedua") tidak menjelaskan dialog pertama; spec menafsirkannya sebagai tidak ada dialog tambahan di Browser A setelah [Confirm] di Browser C, di luar Dialog "Logged Out" dari [Confirm] di Browser B. (4) TC-AUTH-SES-321 Expected b menyebut sesi Browser B "di-invalidate" tanpa status; spec mengasersi kata itu apa adanya. (5) TC-AUTH-SES-28 dan 321 menulis login dengan "password yang benar" tanpa menyebut reCAPTCHA atau nilai password; spec mengikuti TC dan memakai `Spectra.env.SES_PASSWORD`. (6) TC-AUTH-SES-135 tidak menyebut dialog konfirmasi "Force Logout User"; langkah [Force Logout] dan [Confirm Logout] mengikuti TC-AUTH-SES-133 dan 139. (7) TC-AUTH-SES-321 Expected a/b menyebut status sesi (Force Logged Out, di-invalidate) tanpa menyebut cara membacanya; spec memakai kemampuan pembacaan data sesi platform yang disediakan tim FE/BE (Prerequisites).
- Ukuran: spec memuat 57 langkah (melebihi sekitar 35) karena enam TC satu kelas harness (multi-tab dan multi-konteks) berada dalam satu spec; tiap TC memakai user dan sesi sendiri, sehingga bagian berikutnya tetap bermakna meski TC lain di spec ini tidak dijalankan.
