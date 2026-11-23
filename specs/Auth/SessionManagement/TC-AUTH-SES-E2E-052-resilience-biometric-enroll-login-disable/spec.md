---
id: TC-AUTH-SES-E2E-052-resilience-biometric-enroll-login-disable
title: "Resilience Biometric: Kegagalan Server saat Enroll, Re-login, dan Disable"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-SES-150
  - TC-AUTH-SES-174
  - TC-AUTH-SES-248
coverage:
  mobile: automated
---

# Resilience Biometric: Kegagalan Server saat Enroll, Re-login, dan Disable

## Prerequisites

- Mode: FE+BE. Kegagalan 5xx dipaksakan di sisi server lewat failure injection (Tabel Data Uji Pre-setup #18) pada request enroll, relogin, dan disable; aplikasi mobile tidak dapat memakai `Spectra.intercept()`, sehingga spec tetap berjalan terhadap backend nyata (konvensi bagian 6).
- Platform: aplikasi mobile TAG Samurai (Android) terpasang di perangkat Android uji B (Tabel Data Uji Pre-setup #10: hardware biometric, sidik jari terdaftar di OS). Semua TC memakai perangkat yang sama.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): tiga user profil BIO milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5 dan #9: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON; MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-150: `Andi Hidayat` (`andihidayat+{runId}-052@qwertysystem.net`), belum pernah enroll biometric
  - TC-AUTH-SES-174: `Galih Firmansyah` (`galihfirmansyah+{runId}-052@qwertysystem.net`)
  - TC-AUTH-SES-248: `Fajar Anggraini` (`fajaranggraini+{runId}-052@qwertysystem.net`)
- Kondisi "sudah enroll biometric di perangkat Android uji B" untuk TC-AUTH-SES-174 dan TC-AUTH-SES-248 disiapkan lewat alur Prompt Enable Biometric (login, [Enable], lulus verifikasi sidik jari; TC-AUTH-SES-14; cara menyiapkan: Tabel Data Uji Pre-setup #29) pada langkah penghubung `Siapkan enrollment`, karena token biometric lokal dan email cache lokal disimpan per perangkat. Untuk TC-AUTH-SES-174 sesi platform hasil login enroll diakhiri lewat API yang disediakan tim FE/BE (tanpa menghapus token biometric lokal, bukan lewat Log Out di UI); untuk TC-AUTH-SES-248 sesi mobile tetap aktif sesudah enrollment (aplikasi di Portal — Product Hub), lalu pada langkah 29 menjadi sisa app-kill yang dikenali server lewat ID device yang sama dan tidak ada heartbeat lebih dari 60 detik (jam dimajukan 90 detik di langkah 30; NC-02, TC-AUTH-SES-70), sehingga Dialog Duplicate Login Attempt tidak tampil pada re-login biometric.
- Hook `before` juga menghapus data aplikasi pada perangkat Android uji B supaya TC-AUTH-SES-150 dimulai tanpa enrollment dan tanpa sesi.
- State global yang diubah: failure injection 5xx pada request enroll, relogin, dan disable, serta jam server dan jam browser/perangkat (dimajukan bersama pada langkah 30 TC-AUTH-SES-248 dan dipulihkan ke waktu nyata pada langkah 34). Tiap TC menonaktifkan failure injection sebelum langkah berikutnya; hook `after` menonaktifkan semua failure injection dan memulihkan jam sebagai cadangan.
- Hook `after`: nonaktifkan failure injection; pulihkan jam server dan jam browser/perangkat ke waktu nyata; hapus data aplikasi pada perangkat Android uji B; akhiri semua sesi seed; hapus ketiga user. Pembersihan tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: user uji masing-masing TC pada aplikasi mobile; akun aktor hanya di hook.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness b dan d): driver otomasi Android (aplikasi native); menghapus app dari recent apps lalu membukanya kembali; menutup paksa dan menghapus data aplikasi; simulasi sensor sidik jari pada OS biometric prompt (sidik jari terdaftar lulus); failure injection 5xx per endpoint yang dapat diaktifkan dan dinonaktifkan dari alat uji; jam server dan jam browser/perangkat dapat dimajukan bersama dan dipulihkan ke waktu nyata (Tabel Data Uji Pre-setup #18; langkah 30 dan 34); API yang disediakan tim FE/BE untuk mengakhiri sesi platform hasil login enroll tanpa menghapus token biometric lokal (Tabel Data Uji Pre-setup #29).
- Suite berjalan serial (`parallel: false`); state global yang diubah: failure injection 5xx pada request enroll, relogin, dan disable, serta jam server dan jam browser/perangkat, dipulihkan di hook `after`.

## Test Steps

### TC-AUTH-SES-150: Kegagalan server saat enroll menampilkan toast error dan enrollment tidak tersimpan

1. Buka aplikasi mobile di perangkat Android uji B → halaman Login tampil
2. Ketik `andihidayat+{runId}-052@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.SES_PASSWORD` pada field Password
4. Klik [Login] → Prompt Enable Biometric muncul
5. Aktifkan failure injection 5xx pada request enroll
6. Ketuk [Enable]
7. Lulus verifikasi biometric pada OS biometric prompt
8. Verifikasi Toast error "Error, failed to enable biometric."
9. Nonaktifkan failure injection 5xx pada request enroll
10. Hapus app dari recent apps lalu buka kembali aplikasi mobile
11. Verifikasi Enrollment tidak tersimpan: re-entry berikutnya menampilkan form Login, bukan Screen biometric sign-in

### TC-AUTH-SES-174: Kegagalan server saat biometric re-login menampilkan toast error dan token lokal tidak dihapus

12. Tutup paksa aplikasi mobile di perangkat Android uji B, hapus data aplikasi, lalu siapkan enrollment `galihfirmansyah+{runId}-052@qwertysystem.net` sebagai user yang sudah enroll biometric di perangkat (email cache lokal = email itu) tanpa sesi platform aktif
13. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
14. Aktifkan failure injection 5xx pada request relogin
15. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
16. Verifikasi Toast error "Error, failed to log in." pada percobaan pertama
17. Nonaktifkan failure injection 5xx pada request relogin
18. Hapus app dari recent apps lalu buka kembali aplikasi mobile
19. Verifikasi Token lokal tidak dihapus: Screen biometric sign-in tampil
20. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
21. Verifikasi Percobaan berikutnya berhasil: app masuk Portal — Product Hub

### TC-AUTH-SES-248: Kegagalan server saat disable biometric menampilkan toast error dan toggle kembali aktif

22. Tutup paksa aplikasi mobile di perangkat Android uji B, hapus data aplikasi, lalu siapkan enrollment `fajaranggraini+{runId}-052@qwertysystem.net` sebagai user yang sudah enroll biometric di perangkat (email cache lokal = email itu) dengan sesi mobile aktif
23. Aktifkan failure injection 5xx pada request disable
24. Buka Settings > Security di aplikasi mobile perangkat Android uji B
25. Matikan toggle "Biometric sign-in"
26. Verifikasi Toast error "Error, failed to disable biometric."
27. Verifikasi Toggle kembali ke posisi aktif
28. Nonaktifkan failure injection 5xx pada request disable
29. Hapus app dari recent apps
30. Majukan jam server dan jam browser/perangkat bersama 90 detik (lebih dari 60 detik sejak heartbeat terakhir sesi mobile `fajaranggraini+{runId}-052@qwertysystem.net`, supaya sesi lama dikenali sebagai sisa app-kill)
31. Buka kembali aplikasi mobile → Screen biometric sign-in tampil
32. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
33. Verifikasi Kredensial biometric tetap Active: re-login biometric berhasil dan app masuk Portal — Product Hub
34. Pulihkan jam server dan jam browser/perangkat ke waktu nyata

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan mengikuti TC sumber ke-150, 174, 248 setelah dikelompokkan per aksi (enroll, re-login, disable); tidak ada penyimpangan (S-05, S-10).
- Kelas harness gabungan b dan d (prinsip 13, tanpa id P-1 sampai P-5): spec ini memuat kelas b (failure injection 5xx) dan kelas d (hardware biometrik). Alasan: ketiga TC memakai perangkat Android uji B dan alur biometrik yang sama (enroll, re-login, disable), dan failure injection hanya memaksa kegagalan di dalam alur biometrik itu; memisahkannya per kelas menggandakan enrollment, hook perangkat, dan pembersihan token biometric lokal. Penggabungan ini perlu konfirmasi QA (S-15).
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): menghapus app dari recent apps lalu membuka kembali aplikasi untuk menghasilkan keadaan yang diasersi; menyiapkan enrollment user TC berikutnya (langkah 12 dan 22; Tabel Data Uji Pre-setup #29); menonaktifkan failure injection; memajukan jam 90 detik sesudah app dihapus dari recent apps (langkah 30) dan memulihkannya sesudah asersi re-login (langkah 34), supaya sesi mobile sisa app-kill tidak memunculkan Dialog Duplicate Login Attempt (NC-02, TC-AUTH-SES-70).
- Temuan untuk QA: (1) TC-AUTH-SES-174 dan 248 menyebut "sudah enroll biometric" tanpa langkah penyiapan, sementara satu perangkat hanya menyimpan satu token dan email cache lokal; langkah penghubung penyiapan enrollment ditambahkan sebagai kebutuhan teknis dan perlu konfirmasi QA (S-15). (2) TC-AUTH-SES-174 Langkah Uji tidak menyebut kapan failure injection diaktifkan, hanya precondition c; spec mengaktifkannya sebelum langkah lulus verifikasi sidik jari (langkah 14). (3) TC-AUTH-SES-174 Expected b ("percobaan berikutnya berhasil") dan TC-AUTH-SES-248 Expected b ("kredensial biometric tetap Active") tidak menyebut tujuan setelah berhasil; spec memakai Portal — Product Hub seperti TC biometric lain. (4) TC-AUTH-SES-150 tidak menyebut kondisi aplikasi setelah toast error; spec hanya mengasersi toast lalu menutup aplikasi untuk menilai re-entry berikutnya. (5) TC-AUTH-SES-248 mensyaratkan sesi mobile aktif dan Expected b "kredensial biometric tetap Active" tidak punya langkah observasi di TC; spec mengamatinya lewat re-login biometric setelah app dihapus dari recent apps, tetapi sesi mobile lama yang masih tercatat aktif memunculkan Dialog Duplicate Login Attempt bila heartbeat terakhir kurang dari 60 detik (NC-02). Spec memajukan jam server dan jam browser/perangkat bersama 90 detik (langkah 30) dan memulihkannya (langkah 34) supaya sesi lama dikenali sebagai sisa app-kill; TC tidak menyebut langkah ini dan perlu konfirmasi QA (S-15).
