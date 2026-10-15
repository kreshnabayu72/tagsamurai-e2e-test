---
id: TC-AUTH-SES-E2E-031-buka-produk-seat-tersedia-dan-reuse-sesi-produk
title: "Buka Produk saat Seat Tersedia dan Reuse Sesi-produk"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-95
  - TC-AUTH-SES-101
  - TC-AUTH-SES-102
  - TC-AUTH-SES-103
  - TC-AUTH-SES-105
coverage:
  web: automated
---

# Buka Produk saat Seat Tersedia dan Reuse Sesi-produk

## Prerequisites

- Mode: FE+BE.
- Client Q2 (Tabel Data Uji Pre-setup #12): subscription Fixed Asset dan Supply Asset Active, kuota masing-masing 2.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan scope Client Q2 (Tabel Data Uji Pre-setup #26), kredensial `Spectra.env.GS_TC_PASSWORD`): tujuh user profil BASE milik Client Q2 dengan App Access Fixed Asset dan Supply Asset (user Activated, Active ON; MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - Seed seat: `Gunawan Prakoso` (`gunawanprakoso+{runId}-031@qwertysystem.net`) dan `Melati Anggun` (`melatianggun+{runId}-031@qwertysystem.net`), dengan sesi platform web Active
  - TC-AUTH-SES-95: `Nur Pratama` (`nurpratama+{runId}-031@qwertysystem.net`)
  - TC-AUTH-SES-101: `Lestari Saputra` (`lestarisaputra+{runId}-031@qwertysystem.net`)
  - TC-AUTH-SES-102: `Dimas Firmansyah` (`dimasfirmansyah+{runId}-031@qwertysystem.net`)
  - TC-AUTH-SES-103: `Putri Damayanti` (`putridamayanti+{runId}-031@qwertysystem.net`)
  - TC-AUTH-SES-105: `Wulan Anggraini` (`wulananggraini+{runId}-031@qwertysystem.net`)
- Kondisi seat per TC disiapkan lewat API oleh akun aktor pada awal bagian TC itu (langkah penghubung), bukan di hook `before`, karena kuota Client Q2 hanya 2 dan tiap TC membutuhkan jumlah seat terpakai yang berbeda: sebelum menyiapkan, semua sesi-produk Fixed Asset dan Supply Asset aktif Client Q2 diakhiri lewat API. Sesi platform web Active milik user TC (kecuali TC-AUTH-SES-105 yang tidak punya sesi aktif) dibuat di hook `before` lewat login API pada konteks Browser A masing-masing (Chrome on Windows, konteks browser terpisah per TC), dan Browser A berada di Portal — Product Hub.
- Konteks browser (hook `before`): Browser Admin login oleh akun aktor Total Control (Global Settings) dengan scope Client Q2 (Tabel Data Uji Pre-setup #26); Browser License login oleh akun aktor `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` (Global Role Manage Global License di Client Q2, Tabel Data Uji Pre-setup #2, kredensial `Spectra.env.FA_MGL_PASSWORD`).
- Hook `after`: akhiri semua sesi dan sesi-produk seed (Fixed Asset dan Supply Asset), tutup semua konteks browser, lalu hapus ketujuh user. Hook tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- State global yang diubah: seat Fixed Asset dan Supply Asset Client Q2. Pemulihan di hook `after`; suite berjalan serial.
- Environment variable: `GS_TC_PASSWORD`, `FA_MGL_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: banyak konteks browser bersamaan; reload (F5) dan tab baru pada Browser A; pembacaan ID sesi-produk, status sesi-produk, dan hitungan seat per produk dari BE oleh akun aktor (untuk Supply Asset termasuk); reCAPTCHA mode uji di environment (halaman Login with Password, TC-AUTH-SES-105).
- Akun yang dipakai: user uji masing-masing TC pada Browser A; akun aktor Manage Global License pada Browser License; akun aktor Total Control (Global Settings) dengan scope Client Q2 (Tabel Data Uji Pre-setup #26) pada Browser Admin.

## Test Steps

### TC-AUTH-SES-95: Buka produk saat seat tersedia membuat sesi-produk, mengambil seat, dan masuk produk

1. Siapkan lewat API: akhiri semua sesi-produk aktif Client Q2, lalu buat satu sesi-produk Fixed Asset Active milik `Gunawan Prakoso` (kuota 2, seat terpakai 1)
2. Di Browser License buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset) → halaman Concurrent User Fixed Asset tampil
3. Catat hitungan seat aktif Fixed Asset Client Q2 (1) dan penanda waktu dasar Activity Log (waktu server) sebelum membuka produk
4. Di Browser A buka Portal — Product Hub sebagai `nurpratama+{runId}-031@qwertysystem.net` → halaman Portal — Product Hub tampil
5. Di Browser A klik card Fixed Asset di Portal — Product Hub → dashboard Fixed Asset tampil
6. Verifikasi Browser A masuk ke dashboard Fixed Asset
7. Verifikasi Tidak ada popup yang tampil di Browser A
8. Verifikasi Sesi-produk Fixed Asset `Nur Pratama` berstatus Active
9. Verifikasi Jumlah seat aktif Client Q2 menjadi 2
10. Di Browser Admin buka `Activity Log > Session` milik Fixed Asset dan `Global Settings > User > Detail > User Log` milik `Nur Pratama` → halaman log tampil
11. Verifikasi Entri `Session started` untuk `Nur Pratama` tercatat di `Activity Log > Session` milik Fixed Asset (di User Log tampil `Session started (Fixed Asset)`) dengan waktu setelah penanda waktu dasar (dicari lewat email dan Note, bukan lewat posisi teratas)
12. Di Browser License muat ulang daftar `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset)
13. Verifikasi Baris `Nur Pratama` muncul pada daftar sesi aktif
14. Verifikasi Hitungan seat aktif bertambah 1 dari hitungan yang dicatat pada langkah 3

### TC-AUTH-SES-101: Reload produk yang sama saat sesi-produk Active me-reuse sesi tanpa seat baru dan tanpa log kedua

15. Siapkan lewat API: akhiri semua sesi-produk aktif Client Q2, lalu buat satu sesi-produk Fixed Asset Active milik `Lestari Saputra` (seat terpakai 1 dari kuota 2) dan catat ID sesi-produk itu
16. Di Browser A buka Portal — Product Hub sebagai `lestarisaputra+{runId}-031@qwertysystem.net` → halaman Portal — Product Hub tampil
17. Di Browser A buka dashboard Fixed Asset → dashboard Fixed Asset tampil
18. Verifikasi Pembukaan berhasil tanpa popup
19. Verifikasi Pembukaan memakai sesi-produk yang sama (ID sama dengan ID yang dicatat)
20. Tekan F5 untuk reload
21. Verifikasi Setelah reload dashboard Fixed Asset tampil
22. Verifikasi Setelah reload tidak ada popup
23. Verifikasi Setelah reload dashboard memakai sesi-produk yang sama (ID sama)
24. Buka tab baru di Browser A dan buka URL dashboard Fixed Asset yang sama
25. Verifikasi Pembukaan di tab baru berhasil tanpa popup
26. Verifikasi Pembukaan di tab baru memakai sesi-produk yang sama (ID sama)
27. Di Browser License muat ulang daftar `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset)
28. Verifikasi Jumlah seat aktif Client Q2 tetap 1

### TC-AUTH-SES-102: Pemegang seat yang reload saat jumlah seat sama dengan limit tetap masuk tanpa evaluasi limit

29. Siapkan lewat API: akhiri semua sesi-produk aktif Client Q2, lalu buat satu sesi-produk Fixed Asset Active milik `Dimas Firmansyah` dan satu milik `Gunawan Prakoso` sehingga seat terpakai 2 sama dengan kuota 2
30. Di Browser A buka Portal — Product Hub sebagai `dimasfirmansyah+{runId}-031@qwertysystem.net` → halaman Portal — Product Hub tampil
31. Di Browser A buka dashboard Fixed Asset → dashboard Fixed Asset tampil
32. Verifikasi Browser A masuk tanpa popup
33. Verifikasi Browser A memakai sesi-produk yang sama
34. Tekan F5 untuk reload
35. Verifikasi Setelah reload Browser A masuk tanpa popup
36. Verifikasi Setelah reload Browser A memakai sesi-produk yang sama
37. Di Browser License muat ulang daftar `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset)
38. Verifikasi Seat aktif tetap 2

### TC-AUTH-SES-103: Membuka dua produk memakai dua seat independen dan dua entri Session started

39. Siapkan lewat API: akhiri semua sesi-produk aktif Client Q2 sehingga `Putri Damayanti` tidak memiliki sesi-produk Active; catat penanda waktu dasar Activity Log Session Fixed Asset dan Supply Asset (waktu server) sebelum membuka produk
40. Di Browser A buka Portal — Product Hub sebagai `putridamayanti+{runId}-031@qwertysystem.net` → halaman Portal — Product Hub tampil
41. Di Browser A klik card Fixed Asset di Portal — Product Hub → dashboard Fixed Asset tampil
42. Buka tab baru di Browser A dan buka Portal — Product Hub (kembali ke Portal tanpa App Switcher agar sesi-produk Fixed Asset tidak berakhir) → halaman Portal — Product Hub tampil
43. Di tab baru klik card Supply Asset → dashboard Supply Asset tampil
44. Verifikasi Dua sesi-produk Active milik `Putri Damayanti`: Fixed Asset dan Supply Asset
45. Verifikasi Seat Fixed Asset terpakai 1
46. Verifikasi Seat Supply Asset terpakai 1
47. Di Browser Admin buka `Activity Log > Session` milik Fixed Asset dan milik Supply Asset → halaman log tampil
48. Verifikasi Entri `Session started` untuk `Putri Damayanti` tercatat di Session Fixed Asset dengan waktu setelah penanda waktu dasar (dicari lewat email dan Note, bukan lewat posisi teratas)
49. Verifikasi Entri `Session started` untuk `Putri Damayanti` tercatat terpisah di Session Supply Asset dengan waktu setelah penanda waktu dasar (dicari lewat email dan Note, bukan lewat posisi teratas)

### TC-AUTH-SES-105: Login platform tidak mengevaluasi concurrent walau seat produk penuh

50. Siapkan lewat API: akhiri semua sesi-produk aktif Client Q2, lalu buat satu sesi-produk Fixed Asset Active milik `Gunawan Prakoso` dan satu milik `Melati Anggun` sehingga seat terpakai 2 dari kuota 2; `Wulan Anggraini` tidak memiliki sesi aktif
51. Tutup konteks Browser A TC sebelumnya (hapus sesi login browser), buka konteks Browser A baru yang belum login, lalu buka halaman `Auth > Login with Password` → halaman Login with Password tampil
52. Ketik email `wulananggraini+{runId}-031@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil
53. Verifikasi Login berhasil dan Portal — Product Hub tampil
54. Verifikasi Tidak ada popup concurrent saat login
55. Di Browser A klik card Fixed Asset di Portal — Product Hub → Popup muncul
56. Verifikasi Popup "Concurrent session limit reached" muncul saat card Fixed Asset diklik, tidak saat login
57. Klik [OK] pada popup

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan mengikuti TC sumber (95, 101, 102, 103, 105). Tidak ada aksi yang menghabisi data; tiap TC memakai user sendiri dan kondisi seat disiapkan ulang di awal bagiannya sehingga tidak saling bergantung (S-06).
- Ukuran: spec melewati sekitar 35 langkah karena lima TC berdiri sendiri dengan user, sesi platform, dan kondisi seat masing-masing yang disiapkan ulang di awal bagiannya, sehingga bagian berikutnya tetap bermakna walau bagian sebelumnya gagal; blok baca log (langkah 10 sampai 11 dan 47 sampai 49) dan prefix login faktor-1 (langkah 51 sampai 52) tidak dihitung ke batas.
- Pencatatan: asersi `Session started` (langkah 10 sampai 11 dan 47 sampai 49), dicari berdasarkan email dan Note dengan waktu setelah penanda waktu dasar (S-12), mengikuti rujukan TC-AUTH-SES-95 dan 103 ke TC-AUTH-SES-198 untuk lokasi log. Asersi "tidak ada entri `Session started` kedua / tidak ada log baru" pada Expected TC-AUTH-SES-101 (butir c) dan TC-AUTH-SES-102 (butir b) tidak ditulis di spec ini; dirujuk ke spec absence `TC-AUTH-SES-E2E-067-absence-sesi-produk-dan-concurrent` (S-05).
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): menyiapkan kondisi seat lewat API; mencatat hitungan seat; mencatat penanda waktu dasar log; membuka Portal sebagai user TC; muat ulang daftar Concurrent User; menutup konteks Browser A TC sebelumnya dan membuka konteks baru yang belum login (S-09, TC-AUTH-SES-105); membuka halaman log; menutup popup (langkah 57). Langkah 55 dan 56 adalah aksi dan asersi tambahan agar butir b TC-AUTH-SES-105 ("popup hanya muncul saat card Fixed Asset diklik") terbukti; langkah TC sumber hanya login.
- Temuan untuk QA: (1) TC-AUTH-SES-103 menulis "lalu kembali ke Portal" tanpa cara; App Switcher mengakhiri sesi-produk (TC-AUTH-SES-132) sehingga Expected "dua sesi-produk Active" tidak terpenuhi bila dipakai; spec membuka Portal di tab baru. (2) TC-AUTH-SES-103 menyebut seat dan Session Supply Asset tanpa menyebut halaman License > Concurrent User atau Activity Log > Session milik Supply Asset; spec membaca seat Supply Asset dari BE dan memakai log Session masing-masing produk. (3) TC-AUTH-SES-101 menulis "ID sama" tanpa menyebut tempat ID dibaca; spec membacanya dari BE (productSessionId pada respons Open Product). (4) TC-AUTH-SES-105 mengetik email dan password lalu login tanpa menyebut label tombol dan widget reCAPTCHA; spec memakai label `[Log in]` mengikuti PRD Login with Password dan mengandalkan reCAPTCHA mode uji. (5) Akun #2 `manageGlobalLicenseFixedAsset` pada Tabel Data Uji Pre-setup tidak menyebut Client cakupannya; spec mengasumsikan scope Client Q2. (6) Akun #1 Total Control (Global Settings) dipakai membaca `Activity Log > Session` milik Fixed Asset dan Supply Asset; TC-AUTH-SES-198 menyebut kemampuan ini hanya untuk Fixed Asset dan GS.
