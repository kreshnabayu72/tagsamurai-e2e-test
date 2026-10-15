---
id: TC-AUTH-SES-E2E-002-screening-dialog-lifecycle-akun-dan-akses
title: "Screening Dialog Password Changed, Account Deactivated, Account no longer Active, Log Out, dan Access Restricted"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-5
  - TC-AUTH-SES-6
  - TC-AUTH-SES-7
  - TC-AUTH-SES-8
  - TC-AUTH-SES-9
coverage:
  web: automated
  mobile: automated
---

# Screening Dialog Password Changed, Account Deactivated, Account no longer Active, Log Out, dan Access Restricted

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): lima user profil BASE (TC-AUTH-SES-5, 6, 7, dan 8 milik Client `Alpha Logistik`; TC-AUTH-SES-9 milik Client Suspend, Tabel Data Uji Pre-setup #16; user Client Suspend di-seed oleh akun aktor Total Control (Global Settings) dengan scope Client Suspend, Tabel Data Uji Pre-setup #32) (Tabel Data Uji Pre-setup #5: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON; MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-5: `Rizky Pratama` (`rizkypratama+{runId}-002@qwertysystem.net`)
  - TC-AUTH-SES-6: `Nur Ramadhan` (`nurramadhan+{runId}-002@qwertysystem.net`)
  - TC-AUTH-SES-7: `Agus Wulandari` (`aguswulandari+{runId}-002@qwertysystem.net`)
  - TC-AUTH-SES-8: `Rina Hidayat` (`rinahidayat+{runId}-002@qwertysystem.net`)
  - TC-AUTH-SES-9: `Hendra Utami` (`hendrautami+{runId}-002@qwertysystem.net`), milik Client Suspend
- Sesi aktif yang dibuat di hook `before` lewat login API pada konteks masing-masing:
  - TC-AUTH-SES-5: sesi web di Browser A (Chrome on Windows) dan sesi mobile di perangkat Android uji A (Tabel Data Uji Pre-setup #10) yang dibuat lewat login nyata di perangkat dengan email dan password user lalu mengetuk [Not now] pada Prompt Enable Biometric (Tabel Data Uji Pre-setup #28), keduanya status Active.
  - TC-AUTH-SES-6, 7, 9: sesi web di Browser A (Chrome on Windows), status Active.
  - TC-AUTH-SES-8: sesi platform di Browser A beserta sesi-produk Fixed Asset aktif (seat terpakai).
- Browser A adalah konteks terpisah per user uji; TC berikutnya membuka konteks Browser A baru di langkah pembukanya.
- Browser Admin: konteks terpisah dari Browser A, login oleh akun aktor Total Control (Global Settings) di hook `before` (dipakai TC-AUTH-SES-6 dan 7). Browser License: konteks terpisah, login di hook `before` oleh akun aktor `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` (Global Role Manage Global License, Tabel Data Uji Pre-setup #2, kredensial `Spectra.env.FA_MGL_PASSWORD`), dipakai TC-AUTH-SES-8. TC-AUTH-SES-9 memakai akun aktor `principalAdminConsole_automated_{namaCompany}@qwertysystem.net` (Principal staff Admin Console, Tabel Data Uji Pre-setup #4, kredensial `Spectra.env.AC_PRINCIPAL_PASSWORD`) di Browser Admin lewat langkah eksplisit: konteks Browser Admin akun Total Control ditutup dan konteks baru dibuka.
- Hook `after`: pulihkan status Client Suspend ke Active (Unsuspend oleh akun aktor Principal Admin Console) bila TC-AUTH-SES-9 sempat men-Suspend-nya; kembalikan sesi Browser Admin ke akun default (Total Control Global Settings); akhiri semua sesi seed (web dan mobile), tutup Browser A, Browser License, dan Browser Admin; hapus kelima user (user TC-AUTH-SES-6 sudah terhapus oleh spec, pembersihan melewatinya). Hook tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Suite berjalan serial (`parallel: false`); state global yang diubah: status Client Suspend (Suspended pada TC-AUTH-SES-9; efek ke seluruh user Client itu, sehingga TC ini paling akhir), status Toggle Active dan keberadaan user milik spec ini, serta password user TC-AUTH-SES-5, dipulihkan di hook `after`.
- Environment variable: `GS_TC_PASSWORD`, `FA_MGL_PASSWORD`, `AC_PRINCIPAL_PASSWORD`, `SES_PASSWORD`, `SES_PASSWORD_NEW`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: tiga konteks browser bersamaan untuk Browser A, Browser License, dan Browser Admin; satu perangkat Android uji A dengan aplikasi mobile terpasang dan dapat diketuk oleh driver otomasi (TC-AUTH-SES-5); push dialog lifecycle lewat SSE ke Browser A dan aplikasi mobile; reCAPTCHA mode uji di environment (login web akun Principal Admin Console pada Browser Admin).
- Akun yang dipakai: user uji masing-masing TC (bukan akun aktor) pada Browser A dan perangkat Android; akun aktor pada Browser Admin dan Browser License.

## Test Steps

### TC-AUTH-SES-5: Screening Dialog Password Changed di device lain

1. Di Browser A buka `Global Settings > My Profile > Change Password` sebagai `rizkypratama+{runId}-002@qwertysystem.net` → modal Change Password tampil
2. Ketik password lama yang benar `Spectra.env.SES_PASSWORD` pada field Current Password
3. Ketik password baru yang valid sesuai kebijakan password `Spectra.env.SES_PASSWORD_NEW` pada field New Password
4. Ketik `Spectra.env.SES_PASSWORD_NEW` pada field Confirm New Password
5. Klik [Save] → password berhasil diubah
6. Di perangkat Android uji A ketuk layar → Dialog muncul
7. Susuri dialog dari atas ke bawah
8. Verifikasi **Header**: Title "Password Changed"
9. Verifikasi **Header**: Dialog modal
10. Verifikasi **Header**: Severity danger
11. Verifikasi **Body**: Body "Your password has been changed. Please log in again."
12. Verifikasi **Footer**: [OK] (variant text, severity contrast) sebagai satu-satunya tombol

### TC-AUTH-SES-7: Screening Dialog Account Deactivated

13. Tutup konteks Browser A TC sebelumnya, buka konteks Browser A baru (sesi seed milik `aguswulandari+{runId}-002@qwertysystem.net`), lalu buka Portal — Product Hub sebagai `aguswulandari+{runId}-002@qwertysystem.net` → halaman Portal — Product Hub tampil
14. Di Browser Admin buka `Global Settings > User` dan cari `Agus Wulandari` (`aguswulandari+{runId}-002@qwertysystem.net`)
15. Matikan Toggle Active untuk `aguswulandari+{runId}-002@qwertysystem.net` → Toggle Active OFF
16. Pindah ke Browser A → Dialog muncul
17. Susuri dialog dari atas ke bawah
18. Verifikasi **Header**: Title "Account Deactivated"
19. Verifikasi **Header**: Dialog modal
20. Verifikasi **Header**: Severity danger
21. Verifikasi **Header**: Tanpa tombol silang (X)
22. Verifikasi **Body**: Body "Your account has been deactivated. You will be logged out."
23. Verifikasi **Footer**: [OK] (variant text, severity contrast) sebagai satu-satunya tombol

### TC-AUTH-SES-6: Screening Dialog Account no longer Active

24. Tutup konteks Browser A TC sebelumnya, buka konteks Browser A baru (sesi seed milik `nurramadhan+{runId}-002@qwertysystem.net`), lalu buka Portal — Product Hub sebagai `nurramadhan+{runId}-002@qwertysystem.net` → halaman Portal — Product Hub tampil
25. Di Browser Admin buka `Global Settings > User` dan cari `Nur Ramadhan` (`nurramadhan+{runId}-002@qwertysystem.net`)
26. Hapus user tersebut sampai konfirmasi selesai → user terhapus
27. Pindah ke Browser A → Dialog muncul
28. Susuri dialog dari atas ke bawah
29. Verifikasi **Header**: Title "Account no longer Active"
30. Verifikasi **Header**: Dialog modal
31. Verifikasi **Header**: Severity danger
32. Verifikasi **Header**: Tanpa tombol silang (X)
33. Verifikasi **Body**: Body "Your account has been deleted. You will be logged out."
34. Verifikasi **Footer**: [OK] (variant text, severity contrast) sebagai satu-satunya tombol

### TC-AUTH-SES-8: Screening Dialog Log Out pada user yang di-force-logout admin

35. Tutup konteks Browser A TC sebelumnya dan buka konteks Browser A baru dengan sesi-produk Fixed Asset seed milik `rinahidayat+{runId}-002@qwertysystem.net` (seat terpakai) → halaman Fixed Asset tampil
36. Di Browser License buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset) → halaman Concurrent User Fixed Asset tampil
37. Pilih `Rina Hidayat` (`rinahidayat+{runId}-002@qwertysystem.net`), lalu klik [Force Logout] → dialog konfirmasi "Force Logout User" tampil
38. Klik [Confirm Logout] pada dialog konfirmasi "Force Logout User" → force logout selesai
39. Pindah ke Browser A → Dialog muncul
40. Susuri dialog dari atas ke bawah
41. Verifikasi **Header**: Title "Log Out"
42. Verifikasi **Header**: Dialog modal
43. Verifikasi **Header**: Severity danger
44. Verifikasi **Header**: Tanpa tombol silang (X)
45. Verifikasi **Body**: Body "You have been logged out by an administrator."
46. Verifikasi **Footer**: [OK] (variant text, severity contrast) sebagai satu-satunya tombol

### TC-AUTH-SES-9: Screening Dialog Access Restricted pada user Client yang di-Suspend

47. Tutup konteks Browser A TC sebelumnya, buka konteks Browser A baru (sesi seed milik `hendrautami+{runId}-002@qwertysystem.net`), lalu buka Portal — Product Hub sebagai `hendrautami+{runId}-002@qwertysystem.net` → halaman Portal — Product Hub tampil
48. Tutup konteks Browser Admin akun Total Control, buka konteks Browser Admin baru, lalu login sebagai `principalAdminConsole_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.AC_PRINCIPAL_PASSWORD` → halaman beranda akun Principal Admin Console tampil
49. Di Browser Admin buka `Admin Console > Client` → halaman daftar Client tampil
50. Buka menu elipsis Client Suspend (Tabel Data Uji Pre-setup #16) dan pilih Suspend, lalu konfirmasi sampai Client berstatus Suspended
51. Pindah ke Browser A → Dialog muncul
52. Susuri dialog dari atas ke bawah
53. Verifikasi **Header**: Title "Access Restricted"
54. Verifikasi **Header**: Dialog modal
55. Verifikasi **Header**: Severity warning
56. Verifikasi **Header**: Tanpa tombol silang (X)
57. Verifikasi **Body**: Body "Your organization's access has been suspended. You can still view data, but write actions are disabled until access is restored."
58. Verifikasi **Footer**: [OK] (variant text, severity contrast) sebagai satu-satunya tombol

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan (S-05, S-10): urutan di spec ini TC-AUTH-SES-5, 7, 6, 8, 9 (urutan TC sumber 5, 6, 7, 8, 9). TC-AUTH-SES-7 (Deactivate) mendahului TC-AUTH-SES-6 (Delete) karena aksi yang menghapus data ditaruh setelah aksi yang tidak menghapus (S-10); keduanya memakai akun Total Control Global Settings yang sudah login di Browser Admin dari hook. TC-AUTH-SES-8 memakai Browser License yang terpisah sehingga tidak membutuhkan ganti akun. TC-AUTH-SES-9 paling akhir karena membutuhkan ganti akun Browser Admin ke Principal dan mengubah status Client Suspend. Spec ini memuat 58 langkah, di atas batas sekitar 35: satu kelas harness (screening dialog lifecycle multi-konteks) yang bila dipecah mengulang penyiapan sesi Browser A, Browser Admin, Browser License, dan perangkat Android, sehingga dipertahankan satu spec. Tiap TC memakai user sendiri sehingga urutan tidak membuat TC saling bergantung.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): perpindahan Browser A, Browser Admin, dan perangkat Android; penutupan konteks Browser A TC sebelumnya dan pembukaan konteks Browser A baru di langkah pembuka TC (langkah 13, 24, 35, dan 47); penutupan konteks Browser Admin dan pembukaan konteks baru dengan akun Principal (langkah 48); penyusuran dialog tanpa klik.
- Asersi pencatatan sesi (Activity Log > Session dan User Log) untuk kejadian Password Changed, Deactivate, Delete, Force Logout, dan Suspend tidak diasersikan di spec ini; pencatatan diuji di spec pencatatan dan absence modul ini (S-05).
- Temuan untuk QA: (1) TC-AUTH-SES-6 dan 9 tidak menyebut label aksi Delete dan dialog konfirmasi Delete atau Suspend; spec memakai deskripsi aksi dari TC ("hapus user sampai konfirmasi selesai", "Suspend") tanpa mengarang label. (2) TC-AUTH-SES-9 dan TC-AUTH-SES-292 menyebut Browser Admin untuk aksi akun Principal, sedangkan Tabel Data Uji Pre-setup #1 mendefinisikan Browser Admin sebagai konteks akun Total Control; spec membuka konteks Browser Admin baru dengan akun Principal. (3) Login user uji pada hook dan langkah tidak menyebut reCAPTCHA; mengikuti TC.
