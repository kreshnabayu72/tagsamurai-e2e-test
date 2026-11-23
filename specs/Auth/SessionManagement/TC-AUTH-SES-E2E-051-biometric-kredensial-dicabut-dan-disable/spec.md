---
id: TC-AUTH-SES-E2E-051-biometric-kredensial-dicabut-dan-disable
title: "Kredensial Biometric Dicabut oleh Disable, Reset Password, Change Email, dan Change Password"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-177
  - TC-AUTH-SES-178
  - TC-AUTH-SES-179
  - TC-AUTH-SES-180
coverage:
  web: automated
  mobile: automated
---

# Kredensial Biometric Dicabut oleh Disable, Reset Password, Change Email, dan Change Password

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi mobile TAG Samurai (Android) pada perangkat Android uji B (Tabel Data Uji Pre-setup #10: hardware biometric, sidik jari terdaftar di OS) dan, khusus TC-AUTH-SES-178, perangkat Android uji E (biometric). Web: Browser A (Chrome on Windows) dan Browser Admin.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): empat user profil BIO milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5 dan #9: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON; MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-177: `Tari Anggraini` (`tarianggraini+{runId}-051@qwertysystem.net`)
  - TC-AUTH-SES-179: `Siti Setiawan` (`sitisetiawan+{runId}-051@qwertysystem.net`)
  - TC-AUTH-SES-180: `Andi Santoso` (`andisantoso+{runId}-051@qwertysystem.net`); email baru hasil Change Email: `andisantosobaru+{runId}-051@qwertysystem.net`
  - TC-AUTH-SES-178: `Budi Wijaya` (`budiwijaya+{runId}-051@qwertysystem.net`)
- Password baru hasil Change Password dan Reset Password: `Spectra.env.SES_PASSWORD_NEW` (TC-AUTH-SES-178 dan TC-AUTH-SES-179).
- Kondisi "sudah enroll biometric di perangkat Android uji B" per user disiapkan lewat alur Prompt Enable Biometric (login, [Enable], lulus verifikasi sidik jari; TC-AUTH-SES-14; cara menyiapkan: Tabel Data Uji Pre-setup #29): user TC-AUTH-SES-177 di hook `before` dengan sesi mobile aktif (aplikasi tetap di Portal — Product Hub), user TC berikutnya lewat langkah penghubung `Siapkan enrollment` tanpa sesi platform aktif, karena token biometric lokal dan email cache lokal disimpan per perangkat. Bila TC meminta tanpa sesi platform aktif, sesi platform hasil login enroll diakhiri lewat Manual Logout di aplikasi (menu Profile → Log Out; logout mobile tidak menghapus token biometric lokal dan tidak mencabut kredensial di server), lalu app dihapus dari recent apps (Tabel Data Uji Pre-setup #29); langkah `Siapkan enrollment` (langkah 10, 21, 31, 32) mencakup Log Out dan penghapusan app dari recent apps itu. Pada TC-AUTH-SES-177 respons request enroll ditangkap proxy jaringan agar token biometric (T1) tersimpan di alat uji.
- Mail-catcher lingkungan uji (Tabel Data Uji Pre-setup #19) dapat membaca email reset password `sitisetiawan+{runId}-051@qwertysystem.net` dan email konfirmasi email baru `andisantosobaru+{runId}-051@qwertysystem.net`.
- Hook `after`: hapus data aplikasi pada perangkat Android uji B dan E; akhiri semua sesi seed; tutup konteks Browser A dan Browser Admin; hapus keempat user (termasuk yang emailnya sudah diubah). Pembersihan tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: user uji masing-masing TC (Browser A dan aplikasi mobile); akun aktor Total Control (Global Settings) di Browser Admin untuk TC-AUTH-SES-180, sudah login di hook `before`.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`, `SES_PASSWORD_NEW`. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`); state global yang diubah: perangkat fisik Android uji B dan E dipakai bersama (data aplikasi dan token biometric lokal), dipulihkan di hook `after`.
- Kemampuan teknis (kelas harness d: hardware biometrik dan mail-catcher): driver otomasi Android (aplikasi native) untuk dua perangkat; menghapus app dari recent apps lalu membukanya kembali; menutup paksa dan menghapus data aplikasi; simulasi sensor sidik jari pada OS biometric prompt (sidik jari terdaftar lulus); proxy jaringan untuk menangkap respons enroll; alat uji untuk mengirim request relogin langsung (`/v2/iam/auth/biometric/relogin`) dengan token T1; pembacaan email di mail-catcher; reCAPTCHA mode uji di environment untuk halaman web ber-reCAPTCHA (halaman Login with Password dan halaman Reset Password).

## Test Steps

### TC-AUTH-SES-177: Disable biometric lewat toggle Settings > Security

1. Buka Settings > Security di aplikasi mobile perangkat Android uji B
2. Matikan toggle "Biometric sign-in"
3. Verifikasi Toggle berlabel "Biometric sign-in" dinonaktifkan langsung
4. Verifikasi Tanpa dialog konfirmasi saat toggle dinonaktifkan
5. Verifikasi Toast sukses "Success, biometric disabled."
6. Hapus app dari recent apps lalu buka kembali aplikasi mobile
7. Verifikasi Token lokal dihapus: halaman Login (form) tampil, bukan Screen biometric sign-in
8. Kirim lewat alat uji request relogin langsung ke `/v2/iam/auth/biometric/relogin` dengan ID device perangkat Android uji B dan token T1
9. Verifikasi Status kredensial biometric Revoked: request relogin ditolak (token tidak valid)

### TC-AUTH-SES-179: Reset Password sukses mencabut kredensial biometric

10. Tutup paksa aplikasi mobile di perangkat Android uji B, hapus data aplikasi, lalu siapkan enrollment `sitisetiawan+{runId}-051@qwertysystem.net` sebagai user yang sudah enroll biometric di perangkat (email cache lokal = email itu) tanpa sesi platform aktif
11. Di Browser A (konteks baru, belum login) buka `Auth > Login with Password` dan jalankan Forgot Password untuk `sitisetiawan+{runId}-051@qwertysystem.net`
12. Buka email reset password di mail-catcher dan buka tautan Reset Password-nya di Browser A
13. Isi password baru `Spectra.env.SES_PASSWORD_NEW` yang valid dan selesaikan Reset Password
14. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
15. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
16. Verifikasi Relogin ditolak (token tidak valid) setelah biometric sukses
17. Verifikasi Halaman Login penuh tampil
18. Hapus app dari recent apps lalu buka kembali aplikasi mobile
19. Verifikasi Token lokal dihapus: halaman Login (form) tampil, bukan Screen biometric sign-in
20. Verifikasi Tidak ada sesi baru untuk `Siti Setiawan` (aplikasi tidak masuk Portal — Product Hub)

### TC-AUTH-SES-180: Change Email sukses mencabut kredensial biometric

21. Tutup paksa aplikasi mobile di perangkat Android uji B, hapus data aplikasi, lalu siapkan enrollment `andisantoso+{runId}-051@qwertysystem.net` sebagai user yang sudah enroll biometric di perangkat (email cache lokal = email itu) tanpa sesi platform aktif
22. Di Browser Admin buka `Global Settings > User`, cari `Andi Santoso`, dan buka form Edit
23. Ubah email menjadi `andisantosobaru+{runId}-051@qwertysystem.net`, lalu klik [Save]
24. Buka email konfirmasi di mail-catcher dan selesaikan konfirmasi email baru
25. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
26. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
27. Verifikasi Relogin ditolak (token tidak valid) karena semua kredensial biometric di-revoke
28. Verifikasi Halaman Login penuh tampil
29. Hapus app dari recent apps lalu buka kembali aplikasi mobile
30. Verifikasi Token lokal dihapus: halaman Login (form) tampil, bukan Screen biometric sign-in

### TC-AUTH-SES-178: Change atau Reset Password sukses mencabut kredensial biometric di semua device

31. Tutup paksa aplikasi mobile di perangkat Android uji B, hapus data aplikasi, lalu siapkan enrollment `budiwijaya+{runId}-051@qwertysystem.net` sebagai user yang sudah enroll biometric di perangkat (email cache lokal = email itu) tanpa sesi platform aktif
32. Tutup paksa aplikasi mobile di perangkat Android uji E, hapus data aplikasi, lalu siapkan enrollment `budiwijaya+{runId}-051@qwertysystem.net` sebagai user yang sudah enroll biometric di perangkat tersebut tanpa sesi platform aktif
33. Tutup konteks Browser A TC sebelumnya (hapus sesi login browser), buka konteks baru Browser A (Chrome on Windows)
34. Di Browser A login dengan `budiwijaya+{runId}-051@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil
35. Di Browser A buka `Global Settings > My Profile > Change Password`
36. Isi Current Password `Spectra.env.SES_PASSWORD`, New Password `Spectra.env.SES_PASSWORD_NEW`, dan Confirm New Password `Spectra.env.SES_PASSWORD_NEW`, lalu klik [Save]
37. Di perangkat Android uji B hapus app dari recent apps lalu buka kembali aplikasi mobile → Screen biometric sign-in tampil
38. Verifikasi Screen biometric sign-in masih tampil di perangkat B (token lokal tersimpan)
39. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt di perangkat B
40. Verifikasi Relogin ditolak (token tidak valid) di perangkat B
41. Verifikasi Halaman Login penuh tampil di perangkat B
42. Hapus app dari recent apps lalu buka kembali aplikasi mobile di perangkat B
43. Verifikasi Token lokal dihapus di perangkat B: halaman Login (form) tampil, bukan Screen biometric sign-in
44. Di perangkat Android uji E hapus app dari recent apps lalu buka kembali aplikasi mobile → Screen biometric sign-in tampil
45. Verifikasi Screen biometric sign-in masih tampil di perangkat E (token lokal tersimpan)
46. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt di perangkat E
47. Verifikasi Relogin ditolak (token tidak valid) di perangkat E
48. Verifikasi Halaman Login penuh tampil di perangkat E
49. Hapus app dari recent apps lalu buka kembali aplikasi mobile di perangkat E
50. Verifikasi Token lokal dihapus di perangkat E: halaman Login (form) tampil, bukan Screen biometric sign-in
51. Di perangkat Android uji B login dengan `budiwijaya+{runId}-051@qwertysystem.net` dan password baru `Spectra.env.SES_PASSWORD_NEW` → Prompt muncul
52. Verifikasi Opt-in ulang diperlukan setelah login berikutnya: biometric belum aktif sehingga login memakai password dan menawarkan Prompt
53. Verifikasi Prompt "Enable biometric sign-in?" muncul lagi

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan (S-05, S-10): urutan di spec ini TC-AUTH-SES-177, 179, 180, 178 (urutan TC sumber 177, 178, 179, 180). TC-AUTH-SES-178 memakai dua perangkat dan mengubah password sesi web; ditaruh paling akhir, sedangkan TC-AUTH-SES-177 memakai sesi mobile aktif hasil enrollment di hook sehingga ditaruh paling awal.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): menghapus app dari recent apps lalu membuka kembali aplikasi untuk menghasilkan keadaan yang diasersi; menyiapkan enrollment user TC berikutnya (langkah 10, 21, 31, 32; Tabel Data Uji Pre-setup #29); menutup konteks Browser A TC sebelumnya (langkah 33, S-09); membuka mail-catcher; membuka form Edit; menyusuri layar.
- Pencatatan: TC-AUTH-SES-177 Expected c ("tidak dicatat ke surface manapun") adalah asersi absence dan ditaruh di spec absence `TC-AUTH-SES-E2E-070-absence-biometric`; spec ini tidak mengasersinya (S-05).
- Temuan untuk QA: (1) TC-AUTH-SES-177, 178, 179, 180 menyebut "sudah enroll biometric" tanpa langkah penyiapan, sementara satu perangkat hanya menyimpan satu token dan email cache lokal; langkah penghubung penyiapan enrollment ditambahkan sebagai kebutuhan teknis dan perlu konfirmasi QA (S-15). (2) TC-AUTH-SES-180 menyebut "selesaikan konfirmasi email baru" tetapi precondition tidak mencantumkan mail-catcher; spec memakai mail-catcher (Tabel Data Uji Pre-setup #19) dan email baru `andisantosobaru+{runId}-051@qwertysystem.net`. (3) TC-AUTH-SES-178 menyatakan "Browser A (Chrome on Windows) sesi web aktif" sebagai precondition tanpa menyebut login; langkah 34 menambahkannya. Judul TC-AUTH-SES-178 menyebut "Change atau Reset Password", sedangkan Langkah Uji hanya Change Password; Reset Password diuji di TC-AUTH-SES-179. (4) TC-AUTH-SES-178 Expected b ("opt-in ulang diperlukan setelah login berikutnya") dan c (Prompt muncul lagi) tumpang tindih; spec memisahkan dua `Verifikasi` (langkah 52 dan 53). (5) TC-AUTH-SES-180 dan 179 tidak menyebut perilaku tombol atau toast pada form Edit dan Reset Password; spec hanya memakai [Save] sesuai konvensi dan tidak mengasersi toast. (6) TC-AUTH-SES-179 memakai Browser A (belum login) sedangkan judul menyebut hanya "Reset Password"; spec mengikuti Langkah Uji. (7) TC-AUTH-SES-177 Expected b (status kredensial biometric menjadi Revoked) tidak tampil di UI dan TC tidak memberi cara memeriksanya; spec membuktikannya lewat request relogin langsung dengan token T1 yang ditangkap proxy saat enroll (langkah 8 sampai 9) dan memakainya hanya sebagai cara membaca status Expected itu, bukan asersi baru (S-11, S-15).
- Temuan untuk QA (lanjutan): TC-AUTH-SES-178 Langkah Uji hanya menyebut "ubah password" tanpa nilai field; spec mengisi Current Password, New Password, Confirm New Password (nilai baru dan konfirmasi sama), lalu klik [Save], sama dengan TC-AUTH-SES-182 (S-15).
- Ukuran spec: melewati sekitar 35 langkah walau prefix enroll (langkah 10, 21, 31, 32) tidak dihitung, karena empat TC kredensial dicabut berbagi perangkat dan pola yang sama. Tiap subjudul TC memakai user sendiri dengan enrollment sendiri sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal (konvensi bagian 3, batas ukuran).
