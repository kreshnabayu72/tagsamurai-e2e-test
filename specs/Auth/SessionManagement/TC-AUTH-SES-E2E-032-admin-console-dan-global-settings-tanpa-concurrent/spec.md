---
id: TC-AUTH-SES-E2E-032-admin-console-dan-global-settings-tanpa-concurrent
title: "Admin Console dan Global Settings Tanpa Evaluasi Concurrent dan Tanpa Seat"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-106
  - TC-AUTH-SES-107
  - TC-AUTH-SES-108
  - TC-AUTH-SES-109
  - TC-AUTH-SES-221
coverage:
  web: automated
  mobile: automated
---

# Admin Console dan Global Settings Tanpa Evaluasi Concurrent dan Tanpa Seat

## Prerequisites

- Mode: FE+BE.
- Seeding user Principal staff (hook `before`, lewat API oleh akun aktor `principalAdminConsole_automated_{namaCompany}@qwertysystem.net`, Principal staff Admin Console, Tabel Data Uji Pre-setup #4, kredensial `Spectra.env.AC_PRINCIPAL_PASSWORD`): tiga user Principal staff (Tabel Data Uji Pre-setup #20) dengan akses Admin Console dan Global Settings (user Activated, Active ON; MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-106: `Bayu Wibowo` (`bayuwibowo+{runId}-032@qwertysystem.net`)
  - TC-AUTH-SES-107: `Intan Nugroho` (`intannugroho+{runId}-032@qwertysystem.net`)
  - TC-AUTH-SES-221: `Dimas Lestari` (`dimaslestari+{runId}-032@qwertysystem.net`), batas idle 15 menit
- Seeding user Client Q2 (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan scope Client Q2 (Tabel Data Uji Pre-setup #26), kredensial `Spectra.env.GS_TC_PASSWORD`): empat user profil BASE milik Client Q2 (Tabel Data Uji Pre-setup #12: subscription Fixed Asset dan Supply Asset Active, kuota masing-masing 2; user Activated, Active ON; MFA dan Agreement tidak terpicu) dengan App Access Fixed Asset dan Supply Asset, password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - Seed seat: `Gunawan Prakoso` (`gunawanprakoso+{runId}-032@qwertysystem.net`) dan `Melati Anggun` (`melatianggun+{runId}-032@qwertysystem.net`)
  - TC-AUTH-SES-108: `Joko Maulana` (`jokomaulana+{runId}-032@qwertysystem.net`)
  - TC-AUTH-SES-109: `Citra Wijaya` (`citrawijaya+{runId}-032@qwertysystem.net`)
- Sesi dan sesi-produk per TC dibuat lewat API oleh akun aktor pada awal bagian TC itu (langkah penghubung), bukan di hook `before`, karena perangkat Android uji A (Tabel Data Uji Pre-setup #10) dipakai bergantian oleh TC-AUTH-SES-107 dan 109, kondisi seat Fixed Asset Client Q2 hanya berlaku pada TC-AUTH-SES-108, dan TC-AUTH-SES-221 memajukan jam server: sesi platform web Active di Browser A (Chrome on Windows, konteks browser terpisah per TC) melalui login API pada konteks itu; sesi mobile Active di perangkat Android uji A (login nyata dengan email dan password user, ketuk [Not now] pada Prompt Enable Biometric; Tabel Data Uji Pre-setup #28).
- Konteks browser (hook `before`): Browser Admin login oleh akun aktor Total Control (Global Settings); Browser Principal login oleh akun aktor Principal Admin Console (`Spectra.env.AC_PRINCIPAL_PASSWORD`), dipakai membaca `Activity Log > Session` milik Admin Console.
- Hook `after`: kembalikan jam server uji dan jam browser/perangkat ke waktu nyata; akhiri semua sesi dan sesi-produk seed (web, mobile, termasuk dua seed seat); bersihkan data aplikasi mobile di perangkat Android uji A; tutup semua konteks browser; hapus ketujuh user. Hook tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Suite berjalan serial (`parallel: false`); state global yang diubah: seat Fixed Asset Client Q2 (diisi penuh oleh dua seed pada TC-AUTH-SES-108 dan dilepas setelahnya), jam server uji dan jam browser/perangkat (TC-AUTH-SES-221, diatur bersama; TC ini paling akhir karena sesi seluruh konteks lain ikut Expired), dipulihkan di hook `after`.
- Environment variable: `GS_TC_PASSWORD`, `AC_PRINCIPAL_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: konteks browser bersamaan (Browser A dengan dua tab, Browser Admin, Browser Principal); satu perangkat Android uji A dengan aplikasi mobile terpasang dan dapat diketuk oleh driver otomasi; login nyata di perangkat Android uji A (Prompt Enable Biometric: ketuk [Not now]); jam server uji dan jam browser/perangkat yang diatur bersama (dimajukan dengan presisi menit dan dipulihkan ke waktu nyata; Tabel Data Uji Pre-setup #18; kelas harness d: time-travel, TC-AUTH-SES-221); gerakan mouse pada tab Admin Console; pembacaan respons Open Product (kuota concurrent dan subscription kosong untuk Admin Console dan Global Settings), status sesi platform, dan status sesi-produk dari BE oleh akun aktor; reCAPTCHA mode uji di environment (halaman Login with Password, login ulang akun aktor pada TC-AUTH-SES-221).
- Akun yang dipakai: user uji masing-masing TC pada Browser A dan perangkat Android uji A; akun aktor Principal Admin Console pada Browser Principal; akun aktor Total Control (Global Settings) pada Browser Admin (scope Client Q2, Tabel Data Uji Pre-setup #26, untuk membaca log Client Q2 pada TC-AUTH-SES-108).

## Test Steps

### TC-AUTH-SES-106: Buka Admin Console tanpa evaluasi concurrent dan tanpa seat

1. Siapkan lewat API: sesi platform web Active milik `Bayu Wibowo` di Browser A di Portal — Product Hub; catat penanda waktu dasar Activity Log sebelum membuka Admin Console
2. Di Browser A buka Portal — Product Hub sebagai `bayuwibowo+{runId}-032@qwertysystem.net` → halaman Portal — Product Hub tampil
3. Di Browser A klik card Admin Console → Admin Console tampil
4. Verifikasi Browser A masuk Admin Console
5. Verifikasi Tidak ada popup yang tampil di Browser A
6. Verifikasi Sesi-produk Admin Console berstatus Active
7. Verifikasi Sesi-produk Admin Console tanpa Subscription (respons Open Product tanpa subscription)
8. Verifikasi Sesi-produk Admin Console tanpa seat (respons Open Product tanpa informasi kuota concurrent)
9. Di Browser Principal buka `Activity Log > Session` milik Admin Console → halaman Activity Log > Session Admin Console tampil
10. Verifikasi Entri `Session started` untuk `Bayu Wibowo` tercatat di `Activity Log > Session` milik Admin Console dengan waktu setelah penanda waktu dasar (dicari lewat email dan Note, bukan lewat posisi teratas)

### TC-AUTH-SES-107: Admin Console dibuka dari beberapa device atau tab tidak pernah memunculkan popup limit

11. Siapkan: sesi platform web Active milik `Intan Nugroho` di Browser A dan sesi mobile Active di perangkat Android uji A lewat login nyata (data aplikasi akun sebelumnya dibersihkan)
12. Di Browser A buka Portal — Product Hub sebagai `intannugroho+{runId}-032@qwertysystem.net` → halaman Portal — Product Hub tampil
13. Di Browser A klik card Admin Console → Admin Console tampil
14. Verifikasi Pembukaan pertama berhasil tanpa popup `Concurrent session limit reached`
15. Di Browser A buka tab baru, buka Portal — Product Hub, lalu klik card Admin Console → Admin Console tampil
16. Verifikasi Pembukaan kedua di tab baru berhasil tanpa popup `Concurrent session limit reached`
17. Di perangkat Android uji A buka card Admin Console → Admin Console tampil
18. Verifikasi Pembukaan ketiga di aplikasi mobile berhasil tanpa popup `Concurrent session limit reached`
19. Verifikasi Tidak ada kuota concurrent yang dibaca untuk Admin Console pada ketiga pembukaan (respons Open Product ketiganya tanpa informasi kuota concurrent)

### TC-AUTH-SES-108: Buka Global Settings tanpa evaluasi concurrent dan dicatat di GS Session

20. Siapkan lewat API: akhiri semua sesi-produk aktif Client Q2, buat satu sesi-produk Fixed Asset Active milik `Gunawan Prakoso` dan satu milik `Melati Anggun` (seat Fixed Asset terpakai 2 dari kuota 2), dan sesi platform web Active milik `Joko Maulana` di Browser A di Portal — Product Hub; catat penanda waktu dasar Activity Log sebelum membuka Global Settings
21. Di Browser A buka Portal — Product Hub sebagai `jokomaulana+{runId}-032@qwertysystem.net` → halaman Portal — Product Hub tampil
22. Di Browser A klik card Global Settings di Portal — Product Hub → Global Settings tampil
23. Verifikasi Browser A masuk Global Settings
24. Verifikasi Tidak ada popup yang tampil di Browser A walau seat Fixed Asset penuh
25. Verifikasi Sesi-produk Global Settings berstatus Active
26. Verifikasi Sesi-produk Global Settings tanpa seat (respons Open Product tanpa informasi kuota concurrent)
27. Di Browser Admin buka `Global Settings > Activity Log > Session` → halaman Activity Log > Session Global Settings tampil
28. Verifikasi Entri `Session started` untuk `Joko Maulana` tercatat di GS Session (`Global Settings > Activity Log > Session`) dengan waktu setelah penanda waktu dasar (dicari lewat email dan Note, bukan lewat posisi teratas)

### TC-AUTH-SES-109: Global Settings dibuka dari beberapa device atau tab tidak pernah memunculkan popup limit

29. Siapkan: akhiri semua sesi-produk aktif Client Q2, lalu buat sesi web Active milik `Citra Wijaya` di Browser A (Chrome on Windows) dan sesi mobile Active di perangkat Android uji A lewat login nyata (data aplikasi akun sebelumnya dibersihkan)
30. Di Browser A buka Portal — Product Hub sebagai `citrawijaya+{runId}-032@qwertysystem.net` → halaman Portal — Product Hub tampil
31. Di Browser A klik card Global Settings → Global Settings tampil
32. Verifikasi Pembukaan pertama berhasil tanpa popup `Concurrent session limit reached`
33. Di tab baru Browser A buka Portal — Product Hub, lalu klik card Global Settings → Global Settings tampil
34. Verifikasi Pembukaan kedua di tab baru berhasil tanpa popup `Concurrent session limit reached`
35. Di perangkat Android uji A buka card Global Settings → Global Settings tampil
36. Verifikasi Pembukaan ketiga di aplikasi mobile berhasil tanpa popup `Concurrent session limit reached`

### TC-AUTH-SES-221: Sesi Admin Console dan Global Settings tidak punya idle timeout independen

37. Siapkan lewat API: sesi platform web Active milik `Dimas Lestari` di Browser A, beserta sesi-produk Admin Console dan Global Settings Active (Browser A membuka tab Admin Console dan tab Global Settings); batas idle 15 menit; catat penanda waktu dasar Activity Log (waktu server) sebelum jam dimajukan
38. Majukan jam server uji dan jam browser/perangkat bersama 14 menit tanpa aktivitas di Browser A (idle 14 menit)
39. Gerakkan mouse di tab Admin Console pada Browser A
40. Majukan jam server uji dan jam browser/perangkat bersama 14 menit lagi tanpa aktivitas
41. Verifikasi Sesi-produk Admin Console tidak berakhir lebih awal dari sesi platform induknya (sesi platform dan sesi-produk Admin Console masih Active)
42. Verifikasi Sesi-produk Global Settings tidak berakhir lebih awal dari sesi platform induknya (sesi-produk Global Settings masih Active)
43. Majukan jam server uji dan jam browser/perangkat bersama 2 menit lagi
44. Verifikasi Sesi platform `Dimas Lestari` berstatus Expired
45. Verifikasi Sesi-produk Admin Console berakhir lewat cascade dari sesi platform
46. Verifikasi Sesi-produk Global Settings berakhir lewat cascade dari sesi platform
47. Pulihkan jam server uji dan jam browser/perangkat ke waktu nyata
48. Di Browser Principal login ulang sebagai `principalAdminConsole_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.AC_PRINCIPAL_PASSWORD` (sesi sebelumnya Expired akibat jam server dimajukan) → beranda akun Principal Admin Console tampil
49. Di Browser Principal buka `Activity Log > Session` milik Admin Console → halaman Activity Log > Session Admin Console tampil
50. Verifikasi Entri `Session ended` untuk `Dimas Lestari` tercatat di `Activity Log > Session` milik Admin Console dengan waktu setelah penanda waktu dasar (dicari lewat email dan Note, bukan lewat posisi teratas)
51. Di Browser Admin login ulang sebagai `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.GS_TC_PASSWORD` (sesi sebelumnya Expired akibat jam server dimajukan) → beranda akun Total Control Global Settings tampil
52. Di Browser Admin buka `Global Settings > Activity Log > Session` → halaman Activity Log > Session Global Settings tampil
53. Verifikasi Entri `Session ended` untuk `Dimas Lestari` tercatat di GS Session dengan waktu setelah penanda waktu dasar (dicari lewat email dan Note, bukan lewat posisi teratas)

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Spec ini memuat web dan mobile (TC-AUTH-SES-107 dan 109 memakai perangkat Android uji A) dan satu TC time-travel (TC-AUTH-SES-221); TC-AUTH-SES-221 memajukan jam hanya sebagai pemicu (objek ujinya cascade sesi ke sesi-produk, bukan batas TTL), sehingga tetap dalam spec ini dan ditaruh paling akhir; tiap TC berdiri sendiri.
- Ukuran: spec melewati sekitar 35 langkah karena lima TC berdiri sendiri dengan user, sesi, dan kondisi masing-masing yang disiapkan di awal bagiannya, sehingga bagian berikutnya tetap bermakna walau bagian sebelumnya gagal; blok baca log (langkah 9 sampai 10, 27 sampai 28, 49 sampai 50, dan 52 sampai 53) tidak dihitung ke batas.
- Pengecualian konvensi: TC-AUTH-SES-107 dan 109 membuka Admin Console atau Global Settings dari Browser A, tab baru, lalu perangkat Android uji A secara berurutan oleh satu user, tanpa race dan tanpa asersi lintas-konteks selain hasil buka (tanpa popup); pemakaian ini mengikuti P-2 (browser, tab, dan perangkat berbeda dipakai berurutan hanya untuk membentuk kondisi pembukaan, bukan konteks kedua yang menjadi objek asersi). TC-AUTH-SES-221 memajukan jam hanya sebagai pemicu (P-2).
- Urutan (S-10): urutan di spec ini mengikuti TC sumber (106, 107, 108, 109, 221). TC-AUTH-SES-221 tetap paling akhir karena memajukan jam server sehingga sesi lain ikut Expired; hanya kondisi sesi TC itu yang disiapkan di awal bagiannya.
- Pencatatan: TC-AUTH-SES-106 dan 108 merujuk TC-AUTH-SES-199 dan 200 untuk lokasi log (`Activity Log > Session` Admin Console dan `Global Settings > Activity Log > Session`); langkah 9, 10, 27, 28 mengikuti rujukan itu. Asersi User Log (`Session started (Admin Console)` dan `(Global Settings)`) milik TC-AUTH-SES-199 dan 200 tidak diulang di sini.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): menyiapkan sesi dan kondisi seat lewat API; membuka Portal sebagai user TC; membuka tab baru ke Portal untuk pembukaan kedua; membuka halaman log; mencatat penanda waktu dasar log; memulihkan jam server dan jam browser/perangkat ke waktu nyata sebelum akun aktor membuka log (langkah 47); login ulang akun aktor setelah jam server dimajukan (langkah 48 dan 51); gerakan mouse (langkah 39).
- Temuan untuk QA: (1) TC-AUTH-SES-106 dan 107 menyebut user "Principal staff" tanpa menyebut aktor dan cara pembuatannya; spec men-seed lewat akun aktor #4 (Principal Admin Console). (2) TC-AUTH-SES-106 dan 108 menulis "Active tanpa Subscription dan tanpa seat" tanpa menyebut permukaan baca; spec membacanya dari respons Open Product (subscription dan informasi kuota kosong untuk Admin Console dan Global Settings, sesuai `openapi.yaml` `/v2/iam/auth/product-sessions`). (3) TC-AUTH-SES-107 menulis "Tidak ada kuota concurrent yang dibaca untuk Admin Console" tanpa menyebut cara mengamati; spec mengasersi lewat respons Open Product. (4) TC-AUTH-SES-221 menulis "pada idle 14 menit" tanpa menyebut cara memajukan jam; spec memakai langkah majukan jam server uji. TC juga tidak menyebut pengamatan sesi-produk Global Settings secara terpisah; spec mengasersi keduanya. (5) TC-AUTH-SES-221 butir b menyebut `Session ended` tanpa lokasi log; spec memakai `Activity Log > Session` Admin Console (dibaca Principal Admin Console) dan GS Session (dibaca Total Control Global Settings) mengikuti TC-AUTH-SES-199 dan 200. (6) TC-AUTH-SES-107 dan 109 menulis "tab baru" tanpa menyebut cara membuka card di tab itu; spec membuka Portal di tab baru lalu klik card. (7) Konvensi belum punya pengecualian eksplisit untuk TC multi-tab atau multi-perangkat dengan satu user sebagai objek uji (TC-AUTH-SES-107 dan 109); spec memakai P-2 untuk pembukaan berurutan tanpa race dan menunggu keputusan konvensi.
