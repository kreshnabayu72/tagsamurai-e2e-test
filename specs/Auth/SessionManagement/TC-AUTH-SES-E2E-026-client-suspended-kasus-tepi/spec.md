---
id: TC-AUTH-SES-E2E-026-client-suspended-kasus-tepi
title: "Client Suspended: Push Terlewat, Tampil Ulang, Write Guard, dan Bulk Suspend"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-SES-80
  - TC-AUTH-SES-81
  - TC-AUTH-SES-82
  - TC-AUTH-SES-83
  - TC-AUTH-SES-84
  - TC-AUTH-SES-86
  - TC-AUTH-SES-87
  - TC-AUTH-SES-269
coverage:
  web: automated
---

# Client Suspended: Push Terlewat, Tampil Ulang, Write Guard, dan Bulk Suspend

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) dengan scope Client Suspend (Tabel Data Uji Pre-setup #32) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): sembilan user profil BASE, Activated, Active ON, MFA dan Agreement tidak terpicu, password `Spectra.env.SES_PASSWORD`, email bersuffix per run. Status Client Suspend dan Client Suspend 2 (Tabel Data Uji Pre-setup #16) Active di awal spec. User milik Client Suspend kecuali dinyatakan lain:
  - TC-AUTH-SES-80: `Citra Ramadhan` (`citraramadhan+{runId}-026@qwertysystem.net`)
  - TC-AUTH-SES-81: `Yoga Wulandari` (`yogawulandari+{runId}-026@qwertysystem.net`)
  - TC-AUTH-SES-82: `Ayu Hidayat` (`ayuhidayat+{runId}-026@qwertysystem.net`)
  - TC-AUTH-SES-83: `Taufik Utami` (`taufikutami+{runId}-026@qwertysystem.net`)
  - TC-AUTH-SES-84: `Mega Puspita` (`megapuspita+{runId}-026@qwertysystem.net`)
  - TC-AUTH-SES-86: `Sari Firmansyah` (`sarifirmansyah+{runId}-026@qwertysystem.net`)
  - TC-AUTH-SES-269: `Siti Wijaya` (`sitiwijaya+{runId}-026@qwertysystem.net`)
  - TC-AUTH-SES-87: `Galih Damayanti` (`galihdamayanti+{runId}-026@qwertysystem.net`), milik Client Suspend
  - TC-AUTH-SES-87: `Nadia Rahayu` (`nadiarahayu+{runId}-026@qwertysystem.net`), milik Client Suspend 2
- Sesi uji (hook `before`, lewat login API; tiap user punya konteks Browser A sendiri): sesi web Active untuk Citra Ramadhan, Yoga Wulandari, Ayu Hidayat, Taufik Utami, Mega Puspita, Sari Firmansyah, dan Siti Wijaya; sesi-produk Fixed Asset Active untuk Mega Puspita, Sari Firmansyah, dan Siti Wijaya. Sesi Galih Damayanti dan Nadia Rahayu dibuat lewat langkah login di awal TC-AUTH-SES-87, karena Client Suspend sudah melalui siklus Suspend sebelum TC itu.
- Akun aktor Principal Admin Console `principalAdminConsole_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #4, `Spectra.env.AC_PRINCIPAL_PASSWORD`) login di Browser Principal pada hook `before`; dipakai untuk Suspend, Unsuspend, dan Bulk Suspend Client. Browser Principal dan Browser A masing-masing user adalah konteks browser terpisah.
- Hook `after`: pulihkan jam server uji dan jam browser/perangkat ke waktu nyata, Unsuspend Client Suspend dan Client Suspend 2 bila masih Suspended (pemulihan state tenant), pulihkan koneksi SSE semua konteks browser, akhiri semua sesi seed, logout Browser Principal dan kembalikan sesi ke akun default suite, hapus kesembilan user. Hook ini tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Efek pada data Pre-setup bersama (S-06): Suspend, Unsuspend, dan Bulk Suspend Client Suspend dan Client Suspend 2 (Tabel Data Uji Pre-setup #16, dipakai bersama spec lain) mengubah status dan Last Updated kedua Client itu; status keduanya dikembalikan ke Active di hook `after`, Last Updated tidak dipulihkan.
- Environment variable: `GS_TC_PASSWORD`, `AC_PRINCIPAL_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness h: state tenant, dengan kendali SSE dan heartbeat):
  - pemutus dan pemulih koneksi SSE per konteks browser (Tabel Data Uji Pre-setup #18);
  - heartbeat web dikirim saat ada aktivitas mouse dengan interval 60 detik; pengamatan isi respons heartbeat (status Suspended) pada Browser A Yoga Wulandari;
  - pengamatan respons 403 pada aksi tulis Fixed Asset (Mega Puspita);
  - pembacaan status sesi platform, sesi-produk, dan seat dari BE;
  - fitur Bulk Suspend di `Admin Console > Client`;
  - penanganan dialog `beforeunload` browser pada Browser A Siti Wijaya;
  - reCAPTCHA mode uji di environment untuk login web (halaman Login with Password).
- Suite berjalan serial (`parallel: false`); state global yang diubah: status Client Suspend (Active, Suspended, Active, Suspended, Active, Suspended berurutan sepanjang spec), Client Suspend 2 (Active menjadi Suspended pada TC-AUTH-SES-87), serta jam server uji dan jam browser/perangkat (diatur bersama), dipulihkan di hook `after`.
- Menunggu waktu nyata tidak dipakai; interval heartbeat 60 detik dipenuhi dengan menggeser jam server dan jam browser/perangkat bersama sambil menggerakkan mouse.
- Fixture yang belum ada, disediakan tim FE/BE: pembacaan status sesi platform, sesi-produk, dan seat dari BE.

## Test Steps

### Persiapan keadaan awal (Client Suspend masih Active)

1. Di Browser A (Citra Ramadhan) putuskan koneksi SSE (offline)
2. Di Browser A (Mega Puspita) putuskan koneksi SSE dan jangan gerakkan mouse sampai langkah 10
3. Di Browser A (Sari Firmansyah) buka Fixed Asset, buka form Create dan isi sebagian field
4. Di Browser A (Siti Wijaya) buka Fixed Asset, buka form Create dan isi sebagian field

### TC-AUTH-SES-80: Push terlewat: respons heartbeat membawa status Suspended dan dialog tampil pada heartbeat berikutnya

5. Di Browser Principal buka `Admin Console > Client`, buka menu elipsis Client Suspend dan pilih Suspend
6. Di Browser A (Citra Ramadhan) pulihkan koneksi, gerakkan mouse, dan majukan jam server uji dan jam browser/perangkat bersama 60 detik sampai heartbeat berikutnya dikirim → Dialog Access Restricted muncul
7. Verifikasi Dialog "Access Restricted" tampil di Browser A dengan copy yang sama seperti push realtime ("Your organization's access has been suspended. You can still view data, but write actions are disabled until access is restored.")
8. Verifikasi Sesi `Citra Ramadhan` tidak berubah
9. Verifikasi Seat `Citra Ramadhan` tidak berubah

### TC-AUTH-SES-84: Write yang ditolak server pada Client Suspended menampilkan toast baku tanpa Dialog Access Restricted

10. Di Browser A (Mega Puspita) di dalam Fixed Asset buka form Create, isi field wajib dengan data valid, lalu klik [Submit] (aksi tulis)
11. Verifikasi Server menolak write dengan 403
12. Verifikasi Toast error "Changes can't be saved while this workspace is suspended or expired." tampil
13. Verifikasi Dialog "Access Restricted" tidak tampil dan tidak ada redirect

### TC-AUTH-SES-86: Form yang belum di-submit hilang setelah OK pada Dialog Access Restricted

14. Di Browser A (Sari Firmansyah) amati layar → Dialog Access Restricted tampil pada form Create yang terisi sebagian
15. Verifikasi Dialog tetap muncul walau form sedang diisi
16. Klik [OK] pada Dialog Access Restricted
17. Verifikasi Setelah refresh data form yang belum di-submit hilang

### TC-AUTH-SES-269: Refresh dari OK pada Dialog Access Restricted tidak memicu konfirmasi beforeunload

18. Di Browser A (Siti Wijaya) amati layar → Dialog Access Restricted tampil pada form Create yang terisi sebagian
19. Klik [OK] pada dialog
20. Verifikasi Halaman ter-refresh tanpa konfirmasi bawaan browser (`beforeunload`)
21. Verifikasi Data form yang belum di-submit hilang

### TC-AUTH-SES-81: Dialog Access Restricted tampil sekali per transisi ke Suspended per tab

22. Di Browser A (Yoga Wulandari) amati layar → Dialog Access Restricted tampil
23. Di Browser A (Yoga Wulandari) klik [OK] pada Dialog Access Restricted
24. Di Browser A (Yoga Wulandari) gerakkan mouse dan majukan jam server uji dan jam browser/perangkat bersama 120 detik (dua interval heartbeat)
25. Verifikasi Heartbeat tetap membawa status Suspended
26. Verifikasi Dialog Access Restricted tidak tampil lagi

### TC-AUTH-SES-83: Refresh manual halaman saat Client masih Suspended menampilkan dialog lagi

27. Di Browser A (Taufik Utami) amati layar → Dialog Access Restricted tampil
28. Di Browser A (Taufik Utami) klik [OK] pada Dialog Access Restricted
29. Di Browser A (Taufik Utami) tekan F5 untuk me-refresh halaman → Dialog Access Restricted muncul
30. Verifikasi Dialog "Access Restricted" tampil lagi setelah refresh manual karena status masih Suspended
31. Di Browser A (Taufik Utami) gerakkan mouse dan majukan jam server uji dan jam browser/perangkat bersama 60 detik sampai heartbeat berikutnya
32. Klik [OK] pada Dialog Access Restricted ini
33. Verifikasi Halaman ter-refresh
34. Verifikasi Klik [OK] pada dialog ini tidak dihitung sebagai pemicu tampil ulang (dialog tidak tampil lagi)

### TC-AUTH-SES-82: Dialog Access Restricted tampil lagi setelah status kembali Active lalu Suspended lagi

35. Di Browser A (Ayu Hidayat) amati layar → Dialog Access Restricted tampil
36. Di Browser A (Ayu Hidayat) klik [OK] pada Dialog Access Restricted
37. Di Browser Principal buka `Admin Console > Client`, buka menu elipsis Client Suspend dan pilih Unsuspend
38. Di Browser A (Ayu Hidayat) gerakkan mouse dan majukan jam server uji dan jam browser/perangkat bersama 60 detik sampai heartbeat berikutnya
39. Verifikasi Setelah Unsuspend tidak ada dialog
40. Verifikasi Setelah Unsuspend tidak ada push
41. Di Browser Principal buka `Admin Console > Client`, buka menu elipsis Client Suspend dan pilih Suspend lagi
42. Di Browser A (Ayu Hidayat) amati layar → Dialog Access Restricted muncul
43. Verifikasi Setelah Suspend kedua Dialog "Access Restricted" tampil lagi di Browser A

### TC-AUTH-SES-87: Bulk Suspend beberapa Client memunculkan dialog pada semua user terdampak tanpa memutus sesi

44. Di Browser Principal buka `Admin Console > Client`, buka menu elipsis Client Suspend dan pilih Unsuspend (mengembalikan Client Suspend ke Active sebelum Bulk Suspend)
45. Buka Browser A (Galih Damayanti) sebagai konteks baru, login dengan `galihdamayanti+{runId}-026@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu buka card Fixed Asset (sesi web dan sesi-produk Active) → halaman Fixed Asset tampil
46. Buka Browser A (Nadia Rahayu) sebagai konteks baru, login dengan `nadiarahayu+{runId}-026@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu buka card Fixed Asset (sesi web dan sesi-produk Active) → halaman Fixed Asset tampil
47. Di Browser Principal buka `Admin Console > Client`, centang Client Suspend dan Client Suspend 2, lalu jalankan Bulk Suspend
48. Amati Browser A (Galih Damayanti) dan Browser A (Nadia Rahayu) → Dialog Access Restricted muncul di kedua browser
49. Verifikasi Dialog "Access Restricted" tampil di kedua browser
50. Verifikasi Semua sesi platform `Galih Damayanti` dan `Nadia Rahayu` tetap Active
51. Verifikasi Semua sesi-produk `Galih Damayanti` dan `Nadia Rahayu` tetap Active
52. Verifikasi Tidak ada seat yang dilepas

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness h (state tenant: Client Suspended), dengan kendali SSE dan heartbeat.
- Spec melewati sekitar 50 langkah karena delapan TC berbagi satu rantai state tenant (Client Suspend berpindah Active, Suspended, Active, Suspended, Active, Suspended); memecahnya berarti mengulang Suspend/Unsuspend dan seeding sesi per spec. Tiap TC memakai user dan konteks Browser A sendiri sehingga bagian sesudahnya tetap bermakna walau satu TC gagal.
- Penyimpangan urutan (S-05, S-10): urutan spec TC-AUTH-SES-80, 84, 86, 269, 81, 83, 82, 87 (urutan TC sumber 80, 81, 82, 83, 84, 86, 87, 269). Satu kali Suspend (langkah 5) memunculkan dialog pada semua user Client Suspend. TC yang bergantung pada keadaan "push belum diterima" (TC-AUTH-SES-80, 84) dan dialog yang masih tampil dengan form terisi (TC-AUTH-SES-86, 269) ditaruh di depan; TC yang siklusnya Unsuspend lalu Suspend lagi (TC-AUTH-SES-82) ditaruh sesudah TC yang memakai keadaan Suspended pertama; TC-AUTH-SES-87 yang memakai Bulk Suspend ditaruh paling akhir.
- TC-AUTH-SES-81, 82, 83 berdependensi pada TC-AUTH-SES-78; langkah klik [OK] pada Dialog Access Restricted disalin sebagai langkah 23, 28, dan 36 (S-04). TC-AUTH-SES-269 berdependensi pada TC-AUTH-SES-86; langkah klik [OK] dan pengamatan form disalin sebagai langkah 18-19 (S-04).
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): langkah 1-4 (menyiapkan keadaan awal), langkah mengamati dialog yang menjadi precondition (14, 18, 22, 27, 35), langkah menggerakkan mouse dan menunggu heartbeat, langkah 44 (mengembalikan Client Suspend ke Active), dan langkah 45-46 (membuat sesi Client yang baru Active).
- Unsuspend pada langkah 37 dan 44 tidak diasersikan sebagai pencatatan; asersi absence log dan pencatatan tidak ada di spec ini (S-05).
- Temuan untuk QA: (1) TC-AUTH-SES-84 menyebut "buka form Create dan Submit" tanpa field valid; spec menambah pengisian field wajib dengan data valid sebagai langkah penghubung supaya request tulis sampai ke guard server dan tidak diblokir validasi. (2) TC-AUTH-SES-84, 86, 269 tidak menyebut form Create Fixed Asset yang dipakai; spec menyebutnya generik. (3) TC-AUTH-SES-83 Expected b dan Langkah 2 "Tunggu heartbeat berikutnya" tidak menyebut urutan antara refresh dan klik [OK]; spec memakai urutan F5, dialog tampil, tunggu heartbeat, lalu klik [OK], dan memverifikasi dialog tidak tampil lagi sesudahnya. (4) TC-AUTH-SES-80 meminta "pulihkan koneksi dan gerakkan mouse sampai heartbeat berikutnya"; heartbeat web diandaikan dikirim hanya saat ada aktivitas mouse. (5) TC-AUTH-SES-87 tidak menyebut cara membuat sesi-produk kedua user; spec membuka card Fixed Asset di Browser A masing-masing. (7) TC-AUTH-SES-80 b dan TC-AUTH-SES-87 b tidak menyebut permukaan pembacaan status sesi, sesi-produk, dan seat; spec memakai kemampuan BE yang disediakan tim FE/BE. (8) Pre-setup #32 hanya menyebut scope Client Suspend; seeding user Client Suspend 2 (TC-AUTH-SES-87) memakai akun aktor yang sama dan scope Client Suspend 2 tidak dinyatakan TC. (6) TC-AUTH-SES-80, 81, 82, 83 memakai satu Client Suspend bersama sehingga antar-TC saling memengaruhi lewat status Client; spec menjaga keterkaitan lewat urutan di atas.
