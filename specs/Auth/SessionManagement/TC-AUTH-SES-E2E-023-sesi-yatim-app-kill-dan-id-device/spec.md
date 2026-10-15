---
id: TC-AUTH-SES-E2E-023-sesi-yatim-app-kill-dan-id-device
title: "Sesi Yatim Bekas App-Kill: ID Device dan Batas Heartbeat 60 Detik"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-SES-254
  - TC-AUTH-SES-297
  - TC-AUTH-SES-298
  - TC-AUTH-SES-323
coverage:
  web: automated
  mobile: automated
---

# Sesi Yatim Bekas App-Kill: ID Device dan Batas Heartbeat 60 Detik

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi mobile TAG Samurai (Android) di perangkat Android uji A (semua TC) dan perangkat Android uji B yang belum login (TC-AUTH-SES-298), Tabel Data Uji Pre-setup #10. TC-AUTH-SES-254 juga memakai browser admin (akun Total Control (Global Settings)).
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): tiga user profil BASE milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5), user Activated, Active ON, MFA dan Agreement tidak terpicu, password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-297 dan TC-AUTH-SES-323: `Tari Wulandari` (`tariwulandari+{runId}-023@qwertysystem.net`), satu user dipakai berurutan oleh kedua TC
  - TC-AUTH-SES-298: `Budi Saputra` (`budisaputra+{runId}-023@qwertysystem.net`)
  - TC-AUTH-SES-254: `Bayu Santoso` (`bayusantoso+{runId}-023@qwertysystem.net`); sesi-produk Fixed Asset Active (seat terpakai) milik sesi mobilenya (kondisi yang di-seed BE, terkait sesi mobile yang dibuat di langkah penghubung)
- Sesi mobile yang dibutuhkan TC dibuat lewat langkah login pada awal TC di `## Test Steps`, bukan di hook `before`: sesi yang di-seed di awal akan melewati batas idle 15 menit setelah pergeseran jam kumulatif TC-AUTH-SES-298 dan 254, dan hanya satu app yang aktif per perangkat.
- Hook `after`: lepaskan pembekuan jam server uji, kembalikan jam server uji dan jam browser/perangkat ke waktu nyata, hapus pengaturan heartbeat uji, akhiri semua sesi mobile dan sesi-produk yang dibuat spec, hentikan dan bersihkan aplikasi mobile pada perangkat A dan B, hapus ketiga user. Hook ini tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: user uji masing-masing TC pada aplikasi mobile; akun aktor Total Control (Global Settings) sudah login di browser admin dari hook `before` dan dipakai pada TC-AUTH-SES-254 (login ulang di langkah 27).
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness d: time-travel dan heartbeat):
  - driver otomasi Android (hapus app dari recent apps, buka kembali app, ketuk tombol dialog);
  - pengatur waktu server uji (Tabel Data Uji Pre-setup #18) yang dapat memajukan dan memulihkan jam server per menit; jam server dan jam browser/perangkat diatur bersama;
  - pembekuan jam server uji (Tabel Data Uji Pre-setup #18) untuk batas eksak 60 detik pada TC-AUTH-SES-323: jam dibekukan sebelum login ulang, dilepas setelah asersi dialog, dan dipulihkan di hook `after`;
  - pengaturan waktu heartbeat terakhir sesi mobile yang diterima server tepat 60 detik lalu dengan app di foreground (TC-AUTH-SES-323);
  - pembacaan status sesi mobile, sesi-produk (Active, Ended, Expired), dan seat dari BE;
  - login aplikasi mobile dengan ID device yang sama pada sesi yang masih aktif (TC-AUTH-SES-297 dan 323);
  - reCAPTCHA mode uji di environment untuk login ulang akun aktor di Browser Admin (TC-AUTH-SES-254, langkah 27).
- Suite berjalan serial (`parallel: false`); state global yang diubah: jam server uji (digeser dan dibekukan), jam browser/perangkat (diatur bersama jam server), dan waktu heartbeat sesi uji, dipulihkan di hook `after`.

## Test Steps

### TC-AUTH-SES-297: ID device sama dengan heartbeat masih baru tetap memunculkan Dialog Duplicate Login Attempt

1. Buka aplikasi mobile di perangkat Android uji A, login sebagai `tariwulandari+{runId}-023@qwertysystem.net` dengan password `Spectra.env.SES_PASSWORD` dan masuk Portal — Product Hub; biarkan app di foreground (heartbeat terakhir kurang dari 60 detik lalu) → halaman Portal — Product Hub tampil
2. Di perangkat Android uji A (ID device yang sama) coba login lagi dengan `tariwulandari+{runId}-023@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD` → Dialog Duplicate Login Attempt muncul
3. Verifikasi Dialog "Duplicate Login Attempt" tampil (sesi lama tidak dianggap sisa app-kill)
4. Verifikasi Sesi baru belum dibuat sebelum [Confirm]
5. Ketuk [Cancel] pada Dialog Duplicate Login Attempt

### TC-AUTH-SES-323: Heartbeat terakhir tepat 60 detik tetap memunculkan Dialog Duplicate Login Attempt

6. Atur heartbeat terakhir yang diterima server dari sesi mobile `Tari Wulandari` di perangkat Android uji A menjadi tepat 60 detik lalu (app di foreground)
7. Bekukan jam server uji tepat pada saat heartbeat terakhir berumur 60 detik
8. Di perangkat Android uji A (ID device yang sama) coba login lagi dengan `tariwulandari+{runId}-023@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD` → Dialog Duplicate Login Attempt muncul
9. Verifikasi Dialog "Duplicate Login Attempt" tampil (sesi lama tidak dianggap sisa app-kill karena batas eksklusif: hanya lebih dari 60 detik yang dianggap sisa app-kill)
10. Verifikasi Sesi baru belum dibuat sebelum [Confirm]
11. Lepaskan pembekuan jam server uji
12. Ketuk [Cancel] pada Dialog Duplicate Login Attempt

### TC-AUTH-SES-298: Sesi yatim bekas app-kill dari perangkat lain tetap dihitung aktif dan memunculkan Dialog Duplicate Login Attempt

13. Bersihkan state app mobile dari TC sebelumnya di perangkat Android uji A (logout atau bersihkan data app, tutup dialog yang masih tampil)
14. Buka aplikasi mobile di perangkat Android uji A, login sebagai `budisaputra+{runId}-023@qwertysystem.net` dengan password `Spectra.env.SES_PASSWORD` dan masuk Portal — Product Hub → halaman Portal — Product Hub tampil
15. Hapus app dari recent apps di perangkat Android uji A
16. Majukan jam server uji dan jam browser/perangkat bersama 2 menit (heartbeat terakhir lebih dari 60 detik, sesi belum Expired)
17. Di perangkat Android uji B (ID device berbeda, belum login) login dengan `budisaputra+{runId}-023@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD` → Dialog Duplicate Login Attempt muncul
18. Verifikasi Dialog "Duplicate Login Attempt" tampil karena sesi yatim milik perangkat lain tetap dihitung aktif
19. Ketuk [Cancel] pada Dialog Duplicate Login Attempt
20. Pulihkan jam server uji dan jam browser/perangkat ke waktu nyata

### TC-AUTH-SES-254: Server menandai sesi yatim bekas app-kill sebagai Expired lewat idle timeout tanpa login baru

21. Bersihkan state app mobile dari TC sebelumnya di perangkat Android uji A (logout atau bersihkan data app, tutup dialog yang masih tampil)
22. Buka aplikasi mobile di perangkat Android uji A, login sebagai `bayusantoso+{runId}-023@qwertysystem.net` dengan password `Spectra.env.SES_PASSWORD` dan masuk Portal — Product Hub (sesi-produk Fixed Asset Active, seat terpakai) → halaman Portal — Product Hub tampil
23. Hapus app dari recent apps sehingga app dihentikan
24. Catat baseline: penanda waktu sesudah aplikasi dihentikan, serta jumlah entri `Session expired` dan `Session ended` milik `bayusantoso+{runId}-023@qwertysystem.net` di `Global Settings > Activity Log > Session`, User Log `Bayu Santoso`, dan `Activity Log > Session` milik Fixed Asset (Browser Admin, akun Total Control (Global Settings))
25. Majukan jam server uji dan jam browser/perangkat bersama 16 menit tanpa membuka aplikasi
26. Pulihkan jam server uji dan jam browser/perangkat ke waktu nyata
27. Login ulang akun Total Control (Global Settings) di Browser Admin dengan password `Spectra.env.GS_TC_PASSWORD` (sesi aktor melewati batas idle 15 menit karena pergeseran jam 16 menit) → halaman Portal — Product Hub tampil
28. Di Browser Admin buka `Global Settings > Activity Log > Session`, cari entri berdasarkan Note `Session expired` dan email `bayusantoso+{runId}-023@qwertysystem.net`
29. Di Browser Admin buka `Global Settings > User`, cari `Bayu Santoso`, buka Detail dan tab User Log, cari entri berdasarkan Note `Session expired` dan email `bayusantoso+{runId}-023@qwertysystem.net`
30. Di Browser Admin buka `Activity Log > Session` milik Fixed Asset, cari entri berdasarkan Note `Session ended` dan email `bayusantoso+{runId}-023@qwertysystem.net`
31. Verifikasi Sesi mobile berstatus Expired
32. Verifikasi Sesi-produk Fixed Asset berstatus Ended
33. Verifikasi Seat sesi-produk Fixed Asset dilepas
34. Verifikasi Di `Global Settings > Activity Log > Session` jumlah entri `Session expired` Bayu bertambah 1 terhadap baseline
35. Verifikasi Di User Log `Bayu Santoso` jumlah entri `Session expired` bertambah 1 terhadap baseline
36. Verifikasi Di `Activity Log > Session` Fixed Asset jumlah entri `Session ended` untuk sesi-produk anak bertambah 1 terhadap baseline
37. Verifikasi Stempel waktu entri `Session expired` jatuh setelah titik 16 menit tanpa aktivitas dihitung dari penanda waktu baseline (jam sudah dipulihkan), bukan pada saat aplikasi dibunuh

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness d (time-travel dan heartbeat 60 detik).
- Penyimpangan urutan (S-05, S-10): urutan spec TC-AUTH-SES-297, 323, 298, 254 (urutan TC sumber 254, 297, 298, 323). TC-AUTH-SES-254 memajukan jam server 16 menit dan sesinya baru dibuat di dalam TC itu; ditaruh paling akhir supaya pergeseran jam tidak mengganggu TC heartbeat 60 detik yang lain. TC-AUTH-SES-297 dan 323 memakai satu user (`Tari Wulandari`) sehingga berurutan; [Cancel] di akhir tiap TC mempertahankan sesi lama dan membersihkan dialog sebelum TC berikutnya.
- TC-AUTH-SES-254 berdependensi pada TC-AUTH-SES-67 (login lalu hapus app dari recent apps); langkah 22-23 menyalin langkah dependensi itu (S-04).
- TC-AUTH-SES-298 precondition b ("dihapus dari background 2 menit lalu") ditulis sebagai "Majukan jam server uji 2 menit" supaya satu mekanisme waktu dipakai di seluruh spec. Jam dipulihkan di akhir TC itu (langkah 20), sebelum baseline log TC-AUTH-SES-254 dibaca (S-09).
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): langkah login pada awal tiap TC (membuat sesi aktif yang di TC sumber berupa precondition), langkah 6 (mengatur heartbeat), langkah 7 dan 11 (membekukan dan melepas jam server untuk batas eksak TC-AUTH-SES-323), [Cancel] pada dialog (langkah 5, 12, 19), pemulihan jam (langkah 20 dan 26), dan langkah pencatatan baseline, login ulang akun aktor, dan langkah mencari entri log pada TC-AUTH-SES-254. Login ulang akun aktor dilakukan karena pergeseran jam 16 menit pada TC-AUTH-SES-254 melewati batas idle 15 menit sesi aktor; pembersihan state app mobile antar-TC (logout atau bersihkan data app, tutup dialog) dilakukan sebelum login Budi Saputra dan Bayu Santoso. Jam dipulihkan sebelum aktor membuka log (S-09); entri dicari berdasarkan Note dan email, dan asersi memakai selisih jumlah entri terhadap baseline (S-12).
- Ukuran spec 37 langkah: blok baca-log pada TC-AUTH-SES-254 (langkah 28 sampai 30 dan 34 sampai 36) tidak dihitung; tiap TC memakai user dan sesinya sendiri sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal.
- Pencatatan `Session expired` dan `Session ended` pada TC-AUTH-SES-254 diasersikan sebagai pencatatan (bukan absence); asersi absence log tetap di spec absence (S-05).
- Temuan untuk QA: (1) TC-AUTH-SES-297 dan 323 meminta login lagi dari ID device yang sama saat sesi lama masih aktif di foreground, tanpa menyebut cara layar Login dapat ditampilkan; spec mengikuti TC apa adanya dan kebutuhannya dicatat di Prerequisites. (2) TC-AUTH-SES-323 mensyaratkan heartbeat terakhir "tepat 60 detik lalu" dengan app di foreground tanpa menyebut cara menahan heartbeat berikutnya; spec menambah langkah pengaturan heartbeat sebagai langkah penghubung dan membekukan jam server sesuai langkah 1 TC. (3) TC-AUTH-SES-297 dan 323 memakai user yang sama (`Tari Wulandari`); spec memakai satu user berurutan. (4) TC-AUTH-SES-254 tidak menyebut cara membuat sesi-produk Fixed Asset anak yang Active dari sesi mobile; spec mengandalkan kondisi yang di-seed BE tanpa endpoint. (5) TC-AUTH-SES-254 langkah 2 menyebut "Activity Log > Session milik Fixed Asset" tanpa menyebut akun yang membacanya; spec memakai akun Total Control (Global Settings). (6) TC-AUTH-SES-297, 298, 323, 254 menulis "login ... dan password yang benar" tanpa nilai; spec memakai `Spectra.env.SES_PASSWORD`.
