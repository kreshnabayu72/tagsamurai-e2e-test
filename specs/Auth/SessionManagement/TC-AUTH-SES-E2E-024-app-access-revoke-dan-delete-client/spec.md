---
id: TC-AUTH-SES-E2E-024-app-access-revoke-dan-delete-client
title: "App Access Revoke dan Delete Client: Pemutusan Sesi-Produk"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-72
  - TC-AUTH-SES-73
  - TC-AUTH-SES-74
  - TC-AUTH-SES-75
  - TC-AUTH-SES-76
  - TC-AUTH-SES-304
coverage:
  web: automated
---

# App Access Revoke dan Delete Client: Pemutusan Sesi-Produk

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD` (untuk user milik Client Q2: dengan scope Client Q2, Tabel Data Uji Pre-setup #26), dan akun Principal Admin Console `principalAdminConsole_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_PRINCIPAL_PASSWORD`, untuk Client Delete), enam user profil BASE, Activated, Active ON, MFA dan Agreement tidak terpicu, password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-72: `Lestari Maulana` (`lestarimaulana+{runId}-024@qwertysystem.net`), Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5)
  - TC-AUTH-SES-73: `Dimas Wijaya` (`dimaswijaya+{runId}-024@qwertysystem.net`), Client `Alpha Logistik`
  - TC-AUTH-SES-74: `Putri Setiawan` (`putrisetiawan+{runId}-024@qwertysystem.net`), Client `Alpha Logistik`
  - TC-AUTH-SES-304: `Rina Maulana` (`rinamaulana+{runId}-024@qwertysystem.net`), Client Q2 (Tabel Data Uji Pre-setup #12: subscription Fixed Asset dan Supply Asset Active, kuota masing-masing 2) dengan App Access Fixed Asset dan Supply Asset
  - TC-AUTH-SES-75: `Eko Santoso` (`ekosantoso+{runId}-024@qwertysystem.net`), Client Delete A (Tabel Data Uji Pre-setup #17): Default User Client Delete A dengan peran lain di entitas lain sehingga tidak ikut terhapus
  - TC-AUTH-SES-76: `Wulan Kusuma` (`wulankusuma+{runId}-024@qwertysystem.net`), Client Delete B (Tabel Data Uji Pre-setup #17): Default User Client Delete B tanpa peran lain di entitas manapun
- Dua Client Delete (A untuk TC-AUTH-SES-75 dan B untuk TC-AUTH-SES-76) di-seed terpisah karena satu Client hanya punya satu Default User dan kedua kondisi Default User berbeda; nama Client bersuffix per run `Client Delete A {runId}-024` dan `Client Delete B {runId}-024`.
- Sesi uji (hook `before`, lewat login API pada konteks Browser A masing-masing user, Chrome on Windows; tiap user punya konteks Browser A sendiri): sesi web Active untuk keenam user (Rina Maulana di Portal — Product Hub); sesi-produk Fixed Asset Active (seat terpakai) dan sesi-produk Supply Asset Active untuk Lestari Maulana (TC-AUTH-SES-72); sesi-produk Fixed Asset Active untuk Eko Santoso (TC-AUTH-SES-75).
- Kondisi awal TC-AUTH-SES-304 yang di-seed di hook `before`: sesi-produk Fixed Asset Rina Maulana dibuat lalu App Access Fixed Asset-nya dicabut oleh akun aktor sehingga sesi-produk berstatus Ended; sesi platform Active.
- Akun lain yang dipakai di langkah (login pada konteks browser baru dengan langkah ganti akun eksplisit):
  - `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #2, `Spectra.env.FA_MGL_PASSWORD`) di Browser License, TC-AUTH-SES-72
  - `principalAdminConsole_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #4, `Spectra.env.AC_PRINCIPAL_PASSWORD`) di Browser Principal, TC-AUTH-SES-75 dan 76
  - akun aktor Total Control (Global Settings) dengan scope Client Q2 (Tabel Data Uji Pre-setup #26, `Spectra.env.GS_TC_PASSWORD`) di Browser Admin, TC-AUTH-SES-304 (membaca seat dan Activity Log Session Fixed Asset milik Client Q2 serta memberikan kembali App Access); dipulihkan ke akun aktor default suite sebelum TC-AUTH-SES-75
  - Browser Admin = akun Total Control (Global Settings), sudah login dari hook `before` dan dipakai di TC selain TC-AUTH-SES-304.
- Hook `after`: kembalikan App Access Fixed Asset semua user ke kondisi awal bila masih dicabut, hapus Client Delete A dan B yang masih ada, akhiri semua sesi seed, logout Browser License dan Browser Principal, kembalikan sesi Browser Admin ke akun default suite (tanpa scope Client Q2), hapus keenam user. Hook ini tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `FA_MGL_PASSWORD`, `AC_PRINCIPAL_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: beberapa konteks browser bersamaan (Browser A per user, Tab A1 pada Browser A Dimas Wijaya, Browser Admin, Browser License, Browser Principal); pengamatan respons jaringan (403) pada Browser A; pembacaan status sesi platform dan sesi-produk (Active, Ended), hitungan seat, dan daftar sesi aktif dari BE; event push SSE ke Browser A (TC-AUTH-SES-76); reCAPTCHA mode uji di environment untuk login web (halaman Login with Password).
- Suite berjalan serial (`parallel: false`); state global yang diubah: App Access user dan keberadaan Client Delete, dipulihkan di hook `after`.

## Test Steps

### TC-AUTH-SES-72: App Access Fixed Asset dicabut saat user punya sesi-produk Fixed Asset memutus sesi-produk dan melepas seat

1. Buka Browser License (konteks browser baru), login dengan `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` dan password `Spectra.env.FA_MGL_PASSWORD` → Portal — Product Hub tampil
2. Di Browser License buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset), pastikan baris `Lestari Maulana` untuk Fixed Asset tampil, lalu catat hitungan seat aktif
3. Di Browser Admin buka `Global Settings > User`, cari `Lestari Maulana`, buka Detail dan cabut App Access Fixed Asset
4. Verifikasi Sesi-produk Fixed Asset `Lestari Maulana` berstatus Ended
5. Verifikasi Seat sesi-produk Fixed Asset `Lestari Maulana` dilepas
6. Di Browser A (Lestari Maulana) amati halaman Portal — Product Hub
7. Verifikasi Sesi platform `Lestari Maulana` tetap Active
8. Verifikasi `Lestari Maulana` tidak melihat dialog apa pun
9. Di Browser A (Lestari Maulana) buka card Supply Asset
10. Verifikasi Sesi-produk Supply Asset tetap Active
11. Verifikasi Card Supply Asset dapat dibuka
12. Di Browser License muat ulang daftar `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset) dan periksa daftar sesi aktif serta hitungan seat
13. Verifikasi Baris `Lestari Maulana` untuk Fixed Asset hilang dari daftar sesi aktif
14. Verifikasi Hitungan seat aktif Fixed Asset berkurang 1 dari hitungan yang dicatat pada langkah 2 (cara membaca daftar mengikuti `fixed-asset/license/PRD/license.md` §3.2)

### TC-AUTH-SES-73: Request ke produk yang App Access-nya dicabut ditolak 403 dan diarahkan ke Portal tanpa dialog

15. Di Tab A1 pada Browser A (Dimas Wijaya) buka halaman Fixed Asset lewat Portal — Product Hub → halaman Fixed Asset tampil
16. Di Browser Admin buka `Global Settings > User`, cari `Dimas Wijaya`, buka Detail dan cabut App Access Fixed Asset
17. Di Tab A1 klik menu apa pun di dalam Fixed Asset sehingga request dikirim ke server
18. Verifikasi Server menolak request dengan 403
19. Verifikasi Tab A1 diarahkan ke Portal — Product Hub tampil
20. Verifikasi Tidak ada dialog yang tampil

### TC-AUTH-SES-74: Open Product dengan ID sesi-produk ter-cache setelah App Access dicabut ditolak 403

21. Di Browser A (Putri Setiawan) buka halaman Fixed Asset lewat Portal — Product Hub (FE menyimpan ID sesi-produk Fixed Asset) → halaman Fixed Asset tampil
22. Di Browser Admin buka `Global Settings > User`, cari `Putri Setiawan`, buka Detail dan cabut App Access Fixed Asset
23. Di Browser A (Putri Setiawan) buka alamat langsung halaman Fixed Asset tanpa lewat Portal
24. Verifikasi Open Product dengan ID ter-cache ditolak server 403
25. Verifikasi Browser A diarahkan ke Portal — Product Hub tampil
26. Verifikasi Tidak ada dialog yang tampil

### TC-AUTH-SES-304: App Access diberikan kembali setelah dicabut mengizinkan pembukaan produk dengan sesi dan seat baru

27. Tutup konteks Browser Admin TC sebelumnya (hapus sesi login browser), buka konteks baru, dan login dengan akun aktor Total Control (Global Settings) dengan scope Client Q2 (Tabel Data Uji Pre-setup #26) dan password `Spectra.env.GS_TC_PASSWORD` → Portal — Product Hub tampil
28. Catat hitungan seat terpakai Fixed Asset Client Q2 (dibaca dari BE) sebelum App Access diberikan kembali
29. Di Browser Admin buka Activity Log Session Fixed Asset, catat baseline: jumlah entri Note `Session started` dengan email `rinamaulana+{runId}-024@qwertysystem.net`
30. Di Browser Admin buka `Global Settings > User`, cari `Rina Maulana` dan berikan kembali App Access Fixed Asset di Detail
31. Di Browser A (Rina Maulana) klik card Fixed Asset
32. Verifikasi Browser A masuk Fixed Asset tanpa popup
33. Verifikasi Sesi-produk baru dibuat
34. Verifikasi Seat terpakai Fixed Asset Client Q2 bertambah 1 dari hitungan yang dicatat sebelum App Access diberikan kembali
35. Di Browser Admin buka Activity Log Session Fixed Asset dan cari entri berdasarkan Note `Session started` dan email `rinamaulana+{runId}-024@qwertysystem.net`
36. Verifikasi Jumlah entri `Session started` `Rina Maulana` bertambah 1 terhadap baseline (entri sesi-produk baru)
37. Tutup konteks Browser Admin dengan scope Client Q2 (hapus sesi login browser), buka konteks baru, dan login dengan akun aktor Total Control (Global Settings) default suite dan password `Spectra.env.GS_TC_PASSWORD` → Portal — Product Hub tampil

### TC-AUTH-SES-75: Delete Client dengan Default User tetap memakai alur App Access Revoke

38. Di Browser A (Eko Santoso) buka halaman Fixed Asset lewat Portal — Product Hub → halaman Fixed Asset tampil
39. Di Browser Admin catat baseline: jumlah entri Note `Session ended` dengan email `ekosantoso+{runId}-024@qwertysystem.net` di Activity Log Session Fixed Asset dan di `Global Settings > User > Detail > User Log` milik `Eko Santoso`
40. Buka Browser Principal (konteks browser baru), login dengan `principalAdminConsole_automated_{namaCompany}@qwertysystem.net` dan password `Spectra.env.AC_PRINCIPAL_PASSWORD` → halaman Admin Console tampil
41. Di Browser Principal buka `Admin Console > Client`, cari Client Delete A, buka menu elipsis, pilih Delete dan selesaikan konfirmasi sampai Client terhapus
42. Verifikasi Sesi-produk Fixed Asset `Eko Santoso` berstatus Ended
43. Verifikasi Seat sesi-produk Fixed Asset `Eko Santoso` dilepas
44. Verifikasi Sesi platform `Eko Santoso` tetap Active
45. Di Browser A (Eko Santoso) amati Portal — Product Hub dan klik menu di dalam Fixed Asset
46. Verifikasi Request berikutnya dari halaman Fixed Asset ditolak 403
47. Verifikasi Browser A diarahkan ke Portal — Product Hub
48. Verifikasi Tidak ada dialog yang tampil
49. Di Browser Admin buka Activity Log Session Fixed Asset dan `Global Settings > User > Detail > User Log` milik `Eko Santoso`, cari entri berdasarkan Note `Session ended` dan email `ekosantoso+{runId}-024@qwertysystem.net`
50. Verifikasi Jumlah entri `Session ended` di Session produk Fixed Asset bertambah 1 terhadap baseline
51. Verifikasi Jumlah entri `Session ended` di User Log `Eko Santoso` bertambah 1 terhadap baseline

### TC-AUTH-SES-76: Delete Client dengan Default User ikut terhapus memunculkan Dialog Account no longer Active

52. Di Browser Admin catat baseline: jumlah entri Note `Account deleted` dengan email `wulankusuma+{runId}-024@qwertysystem.net` di `Global Settings > Activity Log > Session`
53. Di Browser Principal buka `Admin Console > Client`, cari Client Delete B, buka menu elipsis, pilih Delete dan selesaikan konfirmasi sampai Client terhapus
54. Di Browser A (Wulan Kusuma) amati tanpa interaksi selama 10 detik (event push SSE) → Dialog Account no longer Active muncul
55. Verifikasi Dialog "Account no longer Active" tampil dengan Body "Your account has been deleted. You will be logged out."
56. Verifikasi Dialog memuat satu tombol [OK]
57. Klik [OK] pada Dialog Account no longer Active
58. Verifikasi Browser A diarahkan ke halaman Login
59. Di Browser Admin buka `Global Settings > Activity Log > Session` dan cari entri berdasarkan Note `Account deleted` dan email `wulankusuma+{runId}-024@qwertysystem.net`
60. Verifikasi Jumlah entri `Account deleted` untuk `Wulan Kusuma` bertambah 1 terhadap baseline (rincian pencatatan diuji di TC-AUTH-SES-206)

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Spec ini memuat aksi Principal Admin Console dan Total Control (Global Settings) untuk satu topik (pemutusan sesi-produk akibat App Access dan Client), dengan langkah ganti akun eksplisit (Browser License pada langkah 1, Browser Admin scope Client Q2 pada langkah 27 dan pemulihannya pada langkah 37, dan Browser Principal pada langkah 40).
- Penyimpangan urutan (S-05, S-10): urutan spec TC-AUTH-SES-72, 73, 74, 304, 75, 76 (urutan TC sumber 72, 73, 74, 75, 76, 304). TC-AUTH-SES-304 memerlukan App Access yang dicabut dan tidak merusak data, sehingga ditaruh sebelum Delete Client; aksi Delete Client (TC-AUTH-SES-75 dan 76) ditaruh paling akhir karena menghapus data (prinsip 5 konvensi bagian 3).
- TC-AUTH-SES-73 dan 74 berdependensi pada TC-AUTH-SES-72: langkah 16 dan 22 menyalin langkah pencabutan App Access dari TC-AUTH-SES-72 langkah 1 (S-04). TC-AUTH-SES-304 berdependensi pada TC-AUTH-SES-72; kondisi App Access sudah dicabut disiapkan sebagai seeding di hook `before` (S-04).
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): langkah pembukaan halaman Fixed Asset di Browser A (langkah 15, 21, 38) untuk membuat keadaan "halaman masih terbuka dari sebelum pencabutan" yang di TC sumber berupa precondition; langkah mencatat hitungan seat dan baseline entri log (2, 28, 29, 39, 52); langkah mencari entri log (35, 49, 59); langkah ganti akun (1, 27, 37, 40). Asersi "entri baru" memakai selisih jumlah entri terhadap baseline dan entri dicari berdasarkan Note dan email (S-12).
- Pencatatan hanya diasersikan sejauh disebut Expected TC sumber (TC-AUTH-SES-304, 75, 76); asersi absence log tidak ada di spec ini (S-05).
- Ukuran spec 60 langkah: Delete Client (TC-AUTH-SES-75 dan 76) ada di akhir spec karena menghabisi data (prinsip 5), dan tiap TC memakai user serta sesi seed sendiri sehingga TC sesudahnya tetap bermakna bila TC sebelumnya gagal. Blok baca-log (langkah 35, 49, 59) dan baseline-nya tidak dihitung.
- Temuan untuk QA: (1) TC-AUTH-SES-73 precondition c dan TC-AUTH-SES-74 precondition c menyebut kondisi sesudah pencabutan (halaman Fixed Asset terbuka sebelum pencabutan, ID ter-cache) tanpa langkahnya; spec mengikuti urutan sebab-akibatnya (buka halaman, cabut App Access, aksi). (2) TC-AUTH-SES-75 langkah 2 "klik menu di dalam Fixed Asset" menyiratkan Browser A sudah berada di halaman Fixed Asset, tetapi precondition tidak menyebutnya; spec menambah langkah penghubung membuka Fixed Asset. (3) TC-AUTH-SES-75 dan 76 sama-sama memakai "Client Delete" dengan kondisi Default User berbeda (Tabel Data Uji Pre-setup #17); spec men-seed dua Client Delete terpisah. (4) TC-AUTH-SES-75 tidak menyebut akun yang membaca Activity Log Session Fixed Asset; spec memakai akun Total Control (Global Settings). (5) TC-AUTH-SES-73 dan 74 mensyaratkan "alamat langsung halaman Fixed Asset" tanpa menyebut URL; spec menyebutnya generik. (6) TC-AUTH-SES-76 Expected c hanya merujuk TC-AUTH-SES-206 tanpa menyebut surface log; spec membaca `Global Settings > Activity Log > Session`.
