---
id: TC-AUTH-SES-E2E-073-mobile-biometric-multi-device-change-password
title: "Mobile Biometric Multi-Device: Change Password Mencabut Sesi Lain dan Kredensial Biometric"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-223
coverage:
  web: automated
  mobile: automated
---

# Mobile Biometric Multi-Device: Change Password Mencabut Sesi Lain dan Kredensial Biometric

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): satu user profil BIO (Tabel Data Uji Pre-setup #9: seperti BASE, belum pernah enroll biometric; Activated, Active ON, MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-223: `Lestari Ramadhan` (`lestariramadhan+{runId}-073@qwertysystem.net`) milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5); satu user dipakai untuk sesi web, sesi mobile, dan enroll biometric di dua perangkat (satu sesi mobile per akun)
- Kondisi "sudah enroll biometric" `Lestari Ramadhan` di perangkat Android uji B dan perangkat Android uji E (Tabel Data Uji Pre-setup #10: hardware biometric, sidik jari terdaftar di OS; cara menyiapkan: Tabel Data Uji Pre-setup #29) dibuat di dalam TC lewat alur Prompt Enable Biometric (login, [Enable], lulus verifikasi sidik jari; TC-AUTH-SES-14), karena token biometric lokal dan email cache lokal disimpan per perangkat. Sesi platform hasil login enroll di perangkat B dan E diakhiri di dalam TC lewat Manual Logout di aplikasi (menu Profile → Log Out; logout mobile tidak menghapus token biometric lokal dan tidak mencabut kredensial di server), lalu app dihapus dari recent apps sehingga pembukaan berikutnya menampilkan Screen "Sign in with biometrics" (Tabel Data Uji Pre-setup #29), supaya tidak ada sesi platform aktif di perangkat itu dan batas satu sesi mobile per akun tidak memicu Dialog Duplicate Login Attempt pada login berikutnya.
- Sesi mobile aktif di perangkat Android uji A dibuat lewat login nyata di dalam TC sesudah enroll dan pengakhiran sesi di B dan E (Tabel Data Uji Pre-setup #28: login dengan email dan password, [Not now] pada Prompt Enable Biometric).
- Password baru hasil Change Password: `Spectra.env.SES_PASSWORD_NEW`.
- Suite berjalan serial (`parallel: false`); state global yang diubah: perangkat Android uji A, B, dan E dipakai bergantian oleh spec ini (data aplikasi dan token biometric lokal di perangkat); tidak ada state global lain selain data user seed milik spec ini (password, sesi, dan kredensial biometric `Lestari Ramadhan`), dihapus di hook `after`.
- Hook `after`: hapus data aplikasi pada perangkat Android uji A, B, dan E; akhiri semua sesi seed; tutup konteks Browser A; hapus user seed. Pembersihan tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`, `SES_PASSWORD_NEW`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis disediakan tim FE/BE: satu konteks browser (Browser A, Chrome on Windows) dengan user agent yang dapat ditetapkan; driver otomasi Android untuk tiga perangkat (A, B, E); simulasi sensor sidik jari pada OS biometric prompt; pembacaan read-only tabel `biometric_credentials` (kolom `status`) per `user_id` `Lestari Ramadhan` dan `device_id` perangkat B dan E untuk butir Expected TC-AUTH-SES-223 b (langkah 32 dan 39; Tabel Data Uji Pre-setup #18); reCAPTCHA mode uji di environment untuk login web (halaman Login with Password).
- Akun yang dipakai: `Lestari Ramadhan` pada Browser A dan perangkat Android uji A, B, dan E.

## Test Steps

### TC-AUTH-SES-223: Sinkron Change Password: sesi lain dan kredensial biometric dicabut pada transaksi yang sama

1. Tutup paksa aplikasi mobile di perangkat Android uji B, hapus data aplikasi, lalu buka aplikasi mobile → halaman Login tampil
2. Ketik `lestariramadhan+{runId}-073@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.SES_PASSWORD` pada field Password
4. Klik [Login] → Prompt Enable Biometric muncul
5. Ketuk [Enable] → OS biometric prompt muncul
6. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → app masuk Portal — Product Hub
7. Di perangkat Android uji B buka menu Profile lalu pilih Log Out → form Login tampil (Manual Logout mengakhiri sesi platform hasil login enroll tanpa menghapus token biometric lokal dan tanpa mencabut kredensial biometric; Tabel Data Uji Pre-setup #29)
8. Hapus app dari recent apps
9. Tutup paksa aplikasi mobile di perangkat Android uji E, hapus data aplikasi, lalu buka aplikasi mobile → halaman Login tampil
10. Ketik `lestariramadhan+{runId}-073@qwertysystem.net` pada field Email
11. Ketik `Spectra.env.SES_PASSWORD` pada field Password
12. Klik [Login] → Prompt Enable Biometric muncul
13. Ketuk [Enable] → OS biometric prompt muncul
14. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → app masuk Portal — Product Hub
15. Di perangkat Android uji E buka menu Profile lalu pilih Log Out → form Login tampil (Manual Logout mengakhiri sesi platform hasil login enroll tanpa menghapus token biometric lokal dan tanpa mencabut kredensial biometric; Tabel Data Uji Pre-setup #29)
16. Hapus app dari recent apps
17. Di perangkat Android uji A login dengan `lestariramadhan+{runId}-073@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, ketuk [Not now] pada Prompt Enable Biometric → app masuk Portal — Product Hub (sesi mobile aktif di perangkat A)
18. Di Browser A (konteks baru, Chrome on Windows) login dengan `lestariramadhan+{runId}-073@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil
19. Di Browser A buka `Global Settings > My Profile > Change Password`
20. Isi password lama `Spectra.env.SES_PASSWORD` dan password baru `Spectra.env.SES_PASSWORD_NEW` yang valid, lalu simpan
21. Di Browser A klik menu lain
22. Verifikasi Sesi web di Browser A tetap Active (sesi pemicu)
23. Di perangkat Android uji A ketuk layar → Dialog muncul
24. Verifikasi Sesi lain (sesi mobile di perangkat A) berstatus Force Logged Out
25. Verifikasi Perangkat A menampilkan Dialog Password Changed
26. Verifikasi Judul Dialog "Password Changed"
27. Verifikasi Body Dialog "Your password has been changed. Please log in again."
28. Ketuk [OK] pada Dialog Password Changed di perangkat A
29. Di perangkat Android uji B hapus app dari recent apps lalu buka kembali aplikasi mobile → Screen biometric sign-in tampil
30. Verifikasi Screen biometric sign-in masih tampil di perangkat B (token lokal tersimpan)
31. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt di perangkat B
32. Verifikasi Kredensial biometric berstatus Revoked di perangkat B (dibaca dari tabel `biometric_credentials`, Tabel Data Uji Pre-setup #18)
33. Verifikasi Relogin ditolak (token tidak valid) di perangkat B
34. Hapus app dari recent apps lalu buka kembali aplikasi mobile di perangkat B
35. Verifikasi Halaman Login penuh tampil pada pembukaan app berikutnya di perangkat B
36. Di perangkat Android uji E hapus app dari recent apps lalu buka kembali aplikasi mobile → Screen biometric sign-in tampil
37. Verifikasi Screen biometric sign-in masih tampil di perangkat E (token lokal tersimpan)
38. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt di perangkat E
39. Verifikasi Kredensial biometric berstatus Revoked di perangkat E (dibaca dari tabel `biometric_credentials`, Tabel Data Uji Pre-setup #18)
40. Verifikasi Relogin ditolak (token tidak valid) di perangkat E
41. Hapus app dari recent apps lalu buka kembali aplikasi mobile di perangkat E
42. Verifikasi Halaman Login penuh tampil pada pembukaan app berikutnya di perangkat E
43. Di perangkat Android uji B login dengan `lestariramadhan+{runId}-073@qwertysystem.net` dan password baru `Spectra.env.SES_PASSWORD_NEW` → Prompt muncul
44. Verifikasi Prompt "Enable biometric sign-in?" muncul lagi (opt-in ulang diperlukan)

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Kelas harness: tiga perangkat Android dengan hardware biometrik (kelas d); bukan butir P-1 sampai P-4. TC-AUTH-SES-223 ada di spec ini; spec `TC-AUTH-SES-E2E-062` memuat TC sinkron lintas modul dan plan gating lainnya.
- Dependensi disalin sebagai langkah (S-04): TC-AUTH-SES-223 menyalin langkah TC-AUTH-SES-182 (langkah 17 sampai 28) dan TC-AUTH-SES-178 (langkah 29 sampai 44); enroll di perangkat B dan E (langkah 1 sampai 16) mengikuti alur TC-AUTH-SES-14 sesuai Tabel Data Uji Pre-setup #29. Asersi pada langkah 22 (sesi web di Browser A tetap Active) mengikuti Expected butir a dependensi TC-AUTH-SES-182; asersi pada langkah 24 dan 25 (sesi lain Force Logged Out; perangkat A menampilkan Dialog Password Changed) mengikuti Expected butir b dependensi TC-AUTH-SES-182; asersi pada langkah 26 dan 27 (judul dan Body Dialog Password Changed) mengikuti Expected TC-AUTH-SES-5, dependensi TC-AUTH-SES-182; asersi pada langkah 30, 37, dan 44 (Screen biometric sign-in masih tampil; Prompt muncul lagi) mengikuti Expected dependensi TC-AUTH-SES-178; semuanya tidak ada di Expected TC-AUTH-SES-223 sendiri (S-03).
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): login user uji dan enroll biometric di perangkat B dan E (langkah 1 sampai 6 dan 9 sampai 14); mengakhiri sesi platform hasil login enroll lewat Manual Logout, menu Profile → Log Out (langkah 7 dan 15; Pre-setup #29); menghapus app dari recent apps lalu membuka kembali aplikasi; menutup dialog dengan [OK]; lulus verifikasi sidik jari.
- Urutan langkah 1 sampai 17: enroll di B dan E lebih dulu, sesi hasil login enroll diakhiri lewat Manual Logout, baru sesi mobile di perangkat A dibuat, supaya batas satu sesi mobile per akun tidak memunculkan Dialog Duplicate Login Attempt dan tidak ada sesi platform aktif di B dan E (Prasyarat b TC-AUTH-SES-223).
- Jumlah langkah 44; blok enroll biometric di perangkat B dan E (hapus data aplikasi sampai hapus app dari recent apps, langkah 1 sampai 8 dan 9 sampai 16) tidak dihitung ke batas sekitar 35 langkah (konvensi bagian 3), sehingga langkah yang dihitung 28.
- Temuan untuk QA: (1) TC sumber menulis login dan enroll tanpa menyebut field dan tombol; spec menguraikannya menjadi ketik email, ketik password, klik [Login] (label tombol login mobile tidak disebut TC). (2) TC-AUTH-SES-223 Langkah Uji hanya memuat satu langkah ("ubah password lalu periksa sesi lain serta kredensial biometric"); rincian pemeriksaan per perangkat diambil dari TC-AUTH-SES-182 dan TC-AUTH-SES-178 (dependensi), dan Dialog Password Changed hanya teramati bila sesi mobile di perangkat A dibuat lewat login nyata (Pre-setup #28).
