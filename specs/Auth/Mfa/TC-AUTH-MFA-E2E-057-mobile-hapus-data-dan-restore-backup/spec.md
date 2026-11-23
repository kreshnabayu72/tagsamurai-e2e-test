---
id: TC-AUTH-MFA-E2E-057-mobile-hapus-data-dan-restore-backup
title: "Hapus Data Aplikasi dan Restore Backup ke Perangkat Lain Membuat Device Baru"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-MFA-218
  - TC-AUTH-MFA-219
coverage:
  mobile: automated
---

# Hapus Data Aplikasi dan Restore Backup ke Perangkat Lain Membuat Device Baru

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi mobile TAG Samurai (Android) di perangkat Android uji A untuk kedua TC; perangkat Android uji B (akun Google yang sama dengan perangkat A, backup otomatis Android aktif, aplikasi TAG Samurai belum terpasang sebelum restore) untuk TC-AUTH-MFA-219.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): dua user profil MOB (Tabel Data Uji Pre-setup #11: Activated, Active ON, Authenticator sudah terdaftar), password `Spectra.env.MFA_PASSWORD`, email bersuffix per run. Untuk kedua user: sudah pernah login sukses di mobile dari perangkat Android uji A (ID device aplikasi yang terpasang di perangkat A terdaftar sebagai trusted device mobile) dan logout mobile terakhir kurang dari 30 hari:
  - TC-AUTH-MFA-219: `Gilang Permana` (`gilangpermana+{runId}-057@qwertysystem.net`)
  - TC-AUTH-MFA-218: `Taufan Hidayat` (`taufanhidayat+{runId}-057@qwertysystem.net`)
- Hook `before` juga memastikan aplikasi mobile TAG Samurai terpasang di perangkat A tanpa sesi aktif (halaman publik) dan aplikasi TAG Samurai tidak terpasang di perangkat B.
- Hook `after`: hapus kedua user, hapus aplikasi TAG Samurai hasil restore dari perangkat B, dan pastikan aplikasi mobile terpasang di perangkat A tanpa sesi aktif. Pembersihan tidak berasumsi seeding berhasil penuh. Jam server uji tidak digeser oleh spec ini.
- State global: perangkat fisik bersama (Android uji A dan B); suite berjalan serial (`parallel: false`).
- Akun yang dipakai: tanpa login (halaman publik di aplikasi mobile) untuk kedua TC.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: driver otomasi Android (aplikasi native) yang dapat menghapus data aplikasi lewat Settings Android > Apps > TAG Samurai > Storage > Clear data tanpa uninstall (TC-AUTH-MFA-218) serta menjalankan backup Android di perangkat A dan me-restore backup itu ke perangkat B sampai aplikasi TAG Samurai terpasang kembali dari backup (TC-AUTH-MFA-219); mail-catcher lingkungan uji untuk email alert "New sign-in to your TAG Samurai account" dengan baseline jumlah email per alamat.
- Seeding state BE per user (kemampuan teknis): trusted device mobile ber-ID device aplikasi yang terpasang di perangkat A dan `last_logout_at` mobile kurang dari 30 hari (Gilang Permana, Taufan Hidayat), serta Authenticator terdaftar; mekanisme seeding (endpoint atau skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.

## Test Steps

### TC-AUTH-MFA-219: Restore backup Android ke perangkat lain tidak membawa ID device sehingga perangkat baru dianggap device baru

1. Buka aplikasi mobile TAG Samurai di perangkat A → halaman Login with Password tampil
2. Ketik `gilangpermana+{runId}-057@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
4. Klik button [Log in]
5. Verifikasi Halaman MFA tidak tampil di perangkat A
6. Verifikasi Portal — Product Hub tampil di perangkat A
7. Jalankan backup Android di perangkat A, lalu restore backup tersebut ke perangkat B sampai aplikasi TAG Samurai terpasang kembali dari backup
8. Catat jumlah email dengan subject "New sign-in to your TAG Samurai account" di mail-catcher `gilangpermana+{runId}-057@qwertysystem.net` sebagai baseline
9. Buka aplikasi mobile TAG Samurai di perangkat B → halaman Login with Password tampil
10. Ketik `gilangpermana+{runId}-057@qwertysystem.net` pada field Email
11. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
12. Klik button [Log in]
13. Verifikasi Halaman `Auth > MFA > Choose Verification Method` tampil di perangkat B (ID device dikecualikan dari backup otomatis sehingga perangkat B membuat ID baru)
14. Buka mail-catcher lingkungan uji untuk `gilangpermana+{runId}-057@qwertysystem.net`
15. Verifikasi Email alert dengan subject "New sign-in to your TAG Samurai account" diterima di mail-catcher untuk `gilangpermana+{runId}-057@qwertysystem.net` (jumlah bertambah satu dari baseline)

### TC-AUTH-MFA-218: Menghapus data aplikasi mobile membuat perangkat dianggap device baru

16. Tutup paksa aplikasi mobile TAG Samurai di perangkat B; di perangkat A logout `Gilang Permana` dari aplikasi, lalu tutup paksa aplikasi di perangkat A
17. Buka aplikasi mobile TAG Samurai di perangkat A → halaman Login with Password tampil
18. Ketik `taufanhidayat+{runId}-057@qwertysystem.net` pada field Email
19. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
20. Klik button [Log in]
21. Verifikasi Halaman MFA tidak tampil
22. Verifikasi Portal — Product Hub tampil
23. Tutup aplikasi, lalu hapus data aplikasi lewat Settings Android > Apps > TAG Samurai > Storage > Clear data (aplikasi tidak di-uninstall)
24. Catat jumlah email dengan subject "New sign-in to your TAG Samurai account" di mail-catcher `taufanhidayat+{runId}-057@qwertysystem.net` sebagai baseline
25. Buka aplikasi mobile TAG Samurai di perangkat A → halaman Login with Password tampil
26. Ketik `taufanhidayat+{runId}-057@qwertysystem.net` pada field Email
27. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
28. Klik button [Log in]
29. Verifikasi Halaman `Auth > MFA > Choose Verification Method` tampil (ID device di penyimpanan aman ikut terhapus; aplikasi membuat ID baru)
30. Buka mail-catcher lingkungan uji untuk `taufanhidayat+{runId}-057@qwertysystem.net`
31. Verifikasi Email alert dengan subject "New sign-in to your TAG Samurai account" diterima di mail-catcher untuk `taufanhidayat+{runId}-057@qwertysystem.net` (jumlah bertambah satu dari baseline)

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kedua TC bertanda Automation `Manual Only` di sumber; kebutuhan manipulasi perangkat Android ditulis di Prerequisites sesuai bagian 2 konvensi.
- Kelas harness d (manipulasi perangkat Android: hapus data aplikasi, backup dan restore ke perangkat kedua): kedua TC memakai satu jenis harness. Pasang ulang aplikasi (TC-AUTH-MFA-32) ada di spec `TC-AUTH-MFA-E2E-052-platform-mobile-trust-idle-reinstall`; user dan state seeding berbeda dan tidak ada ketergantungan data antar-spec.
- Penyimpangan urutan (S-05): urutan di spec TC-AUTH-MFA-219, lalu TC-AUTH-MFA-218, bukan urutan TC sumber. Hapus data pada TC-AUTH-MFA-218 mengganti ID device aplikasi di perangkat A, sehingga trusted device perangkat A milik `Gilang Permana` yang di-seed hook `before` tidak lagi cocok bila TC-AUTH-MFA-219 berjalan sesudahnya; TC-AUTH-MFA-218 ditaruh paling akhir (S-10).
- Perangkat A lalu perangkat B pada TC-AUTH-MFA-219 dipakai berurutan hanya untuk membentuk identitas device, tanpa asersi lintas keduanya (bukan konteks kedua).
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): langkah 8 dan 24 mencatat baseline jumlah email alert (R-11); langkah 14 dan 30 membuka mail-catcher; langkah 16 menutup sesi TC-AUTH-MFA-219 (logout `Gilang Permana` di perangkat A, yang sudah sampai Portal — Product Hub, dan sesi pre-auth di perangkat B) supaya TC-AUTH-MFA-218 mulai dari halaman publik (S-09).
- Asersi pencatatan log tidak ada di spec ini; hanya halaman yang tampil dan email alert yang dicek sesuai TC.
- Temuan untuk QA:
  - Post Condition TC-AUTH-MFA-218 dan 219 ("Sesi pre-auth MFA aktif untuk `Taufan Hidayat`/`Gilang Permana` di platform mobile") tidak punya Expected padanan atau langkah observasi di TC (state BE) dan tidak diasersi; padanan yang teramati hanya halaman Choose Verification Method.
  - TC-AUTH-MFA-218 dan 219 precondition d mensyaratkan perangkat uji yang sama sudah trusted, tetapi ID device aplikasi dibuat saat pemasangan; cara men-seed trusted device untuk ID itu tidak dijelaskan (sama dengan TC-AUTH-MFA-32 di spec 052).
  - TC-AUTH-MFA-219 langkah 6 tidak menyebut mekanisme backup dan restore (mis. wizard penyiapan perangkat B sesudah reset pabrik atau alat backup Android) maupun kondisi awal perangkat B; spec mengasumsikan aplikasi TAG Samurai belum terpasang di perangkat B sebelum restore dan menuliskan backup dan restore sebagai kemampuan teknis yang disediakan tim mobile/FE.
  - TC-AUTH-MFA-219 langkah 7 ("Buka aplikasi dan login ulang") tidak menyebut layar pertama aplikasi hasil restore di perangkat B; spec mengasumsikan halaman Login with Password tampil (sesi login tidak ikut terbawa backup). TC juga tidak menyebut sesi penuh `Gilang Permana` di perangkat A sesudah langkah 5; spec menutupnya dengan logout di langkah 16.
  - TC-AUTH-MFA-218 dan 219 tidak menyebut layar Confirm to Continue padahal profil MOB sama dengan TC-AUTH-MFA-32; spec mengikuti TC.
