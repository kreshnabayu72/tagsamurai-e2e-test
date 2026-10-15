---
id: TC-AUTH-SES-E2E-064-defense-in-depth-server-side
title: "Defense-in-depth Server-side: Create Session, Force-logout, dan Manipulasi Sesi"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-SES-231
  - TC-AUTH-SES-232
  - TC-AUTH-SES-233
  - TC-AUTH-SES-234
  - TC-AUTH-SES-235
  - TC-AUTH-SES-320
  - TC-AUTH-SES-250
coverage:
  web: automated
---

# Defense-in-depth Server-side: Create Session, Force-logout, dan Manipulasi Sesi

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`), password semua user `Spectra.env.SES_PASSWORD`, email bersuffix per run. Semua user milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; Activated dan Active ON kecuali disebut lain; MFA dan Agreement tidak terpicu) profil BASE kecuali disebut lain:
  - TC-AUTH-SES-235: `Nadia Wijaya` (`nadiawijaya+{runId}-064@qwertysystem.net`)
  - TC-AUTH-SES-320: `Mega Rahayu` (`megarahayu+{runId}-064@qwertysystem.net`), profil PENDING (belum aktivasi; Tabel Data Uji Pre-setup #25)
  - TC-AUTH-SES-250: `Dimas Nugroho` (`dimasnugroho+{runId}-064@qwertysystem.net`), profil INACTIVE (Toggle Active OFF)
  - TC-AUTH-SES-233: `Reza Wibowo` (`rezawibowo+{runId}-064@qwertysystem.net`) dengan sesi-produk Fixed Asset Active di-seed lewat login API dan pembukaan produk API; `Sari Nugroho` (`sarinugroho+{runId}-064@qwertysystem.net`) tanpa Global Role Manage Global License
  - TC-AUTH-SES-234: `Galih Maulana` (`galihmaulana+{runId}-064@qwertysystem.net`) dengan sesi-produk Fixed Asset Active di-seed lewat API; admin target adalah Admin License di Client Q2 (Tabel Data Uji Pre-setup #2 dan #12)
  - TC-AUTH-SES-232: `Mega Anggraini` (`megaanggraini+{runId}-064@qwertysystem.net`) dengan sesi web berstatus Force Logged Out: login API pertama menyimpan token sesi lama di alat uji, lalu login API kedua dan konfirmasi duplicate login mengakhiri sesi pertama
  - TC-AUTH-SES-231: `Taufik Rahayu` (`taufikrahayu+{runId}-064@qwertysystem.net`)
- Akun aktor lain (login eksplisit di langkah): Admin License `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_MGL_PASSWORD`, untuk TC-AUTH-SES-234 (dipakai sebagai admin Client Q2).
- Token autentikasi untuk request langsung (user PENDING, INACTIVE, dan `Nadia Wijaya` pada TC yang mengirim Create Session) diterbitkan oleh alat uji di hook `before`.
- Suite berjalan serial (`parallel: false`); state global yang diubah: jam server dan jam browser/perangkat (dimajukan bersama pada TC-AUTH-SES-231), dipulihkan di hook `after`.
- Hook `after`: pulihkan jam server dan jam browser/perangkat ke waktu nyata; akhiri semua sesi dan sesi-produk seed; tutup semua konteks browser; hapus seluruh user. Pembersihan tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: pada TC-AUTH-SES-233 dan 234 aktor request adalah `Sari Nugroho` dan Admin License; selainnya user uji masing-masing pada Browser C atau Browser A.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`, `FA_MGL_PASSWORD`. Password dan token tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness a): client HTTP yang mengirim request langsung ke API dengan token tertentu, dikirim dari dalam konteks halaman browser (Browser C) supaya reaksi UI (redirect ke halaman Login, kemunculan dialog) dapat diamati dan respons HTTP dapat dibaca; menghapus elemen dialog dan overlay lewat DevTools pada Browser A; pengatur waktu server uji dan jam browser/perangkat yang dimajukan bersama (Tabel Data Uji Pre-setup #18); banyak konteks browser bersamaan; reCAPTCHA mode uji di environment (halaman Login with Password).

## Test Steps

### TC-AUTH-SES-235: Platform tidak valid pada pembuatan sesi ditolak server

1. Buka Browser C (konteks baru) di halaman `Auth > Login with Password`
2. Kirim dari Browser C request Create Session dengan token autentikasi `Nadia Wijaya` dan platform `Desktop`
3. Verifikasi Request ditolak (400) karena platform tidak valid
4. Verifikasi Sesi tidak dibuat: respons tidak memuat sessionId dan tidak ada cookie `sid`
5. Verifikasi Tidak ada dialog yang tampil di Browser C

### TC-AUTH-SES-320: Create Session untuk user yang belum aktivasi ditolak dan diarahkan ke Login

6. Buka Browser C (konteks baru) di halaman `Auth > Login with Password`
7. Kirim dari Browser C request Create Session dengan token autentikasi `Mega Rahayu` (belum aktivasi)
8. Verifikasi Server menolak request
9. Verifikasi User diarahkan ke halaman Login
10. Verifikasi Tidak ada dialog yang tampil di Browser C
11. Verifikasi Tidak ada sesi yang dibuat: respons tidak memuat sessionId dan tidak ada cookie `sid`

### TC-AUTH-SES-250: Create Session untuk user tidak aktif atau belum aktivasi ditolak dan diarahkan ke Login

12. Buka Browser C (konteks baru) di halaman `Auth > Login with Password`
13. Kirim dari Browser C request Create Session dengan token autentikasi `Dimas Nugroho` (Toggle Active OFF)
14. Verifikasi Server menolak request
15. Verifikasi User diarahkan ke halaman Login
16. Verifikasi Tidak ada dialog yang tampil di Browser C
17. Verifikasi Tidak ada sesi yang dibuat: respons tidak memuat sessionId dan tidak ada cookie `sid`

### TC-AUTH-SES-233: Request force-logout tanpa capability Manage Global License ditolak 403

18. Tutup konteks Browser C sebelumnya (hapus sesi login browser), lalu di Browser C (konteks baru, Chrome on Windows) login dengan `sarinugroho+{runId}-064@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil
19. Kirim dari Browser C request `POST /v2/iam/auth/product-sessions/{id}/force-logout` langsung untuk sesi-produk Fixed Asset milik `Reza Wibowo`
20. Verifikasi Server menolak dengan 403
21. Verifikasi Tidak ada dialog khusus yang tampil di Browser C
22. Kirim lewat client HTTP heartbeat (`PUT /v2/iam/auth/sessions/heartbeat`) dengan token sesi `Reza Wibowo`
23. Verifikasi Sesi `Reza Wibowo` tetap Active: heartbeat diterima

### TC-AUTH-SES-234: Request force-logout terhadap user di luar scope entitas admin ditolak 403

24. Buka Browser Lisensi (konteks baru) dan login sebagai `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.FA_MGL_PASSWORD` (admin Client Q2)
25. Kirim dari Browser Lisensi request `POST /v2/iam/auth/product-sessions/{id}/force-logout` langsung untuk sesi-produk Fixed Asset milik `Galih Maulana` (Client `Alpha Logistik`)
26. Verifikasi Server menolak dengan 403
27. Verifikasi Tidak ada dialog khusus yang tampil di Browser Lisensi
28. Kirim lewat client HTTP heartbeat (`PUT /v2/iam/auth/sessions/heartbeat`) dengan token sesi `Galih Maulana`
29. Verifikasi Sesi `Galih Maulana` tetap Active: heartbeat diterima

### TC-AUTH-SES-232: Client tidak dapat menghidupkan kembali sesi Expired atau Force Logged Out lewat manipulasi request

30. Kirim lewat client HTTP request terautentikasi ke API dengan token sesi lama `Mega Anggraini` (berstatus Force Logged Out), yaitu `POST /v2/iam/auth/product-sessions`
31. Verifikasi Request ditolak 401 dengan alasan sesi berakhir
32. Kirim lewat client HTTP heartbeat (`PUT /v2/iam/auth/sessions/heartbeat`) dengan token yang sama
33. Verifikasi Heartbeat ditolak 401 dengan alasan sesi berakhir
34. Verifikasi Status sesi tetap Force Logged Out: respons 401 tetap memuat alasan sesi berakhir yang sama dan sesi tidak kembali Active

### TC-AUTH-SES-231: Dialog dipaksa tertutup lewat manipulasi DOM tetap ditolak server pada request berikutnya

35. Di Browser A (konteks baru, Chrome on Windows) login dengan `taufikrahayu+{runId}-064@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil
36. Biarkan Browser A tanpa aktivitas dan majukan jam server dan jam browser/perangkat bersama 10 menit → Toast Idle Warning tampil
37. Majukan jam server dan jam browser/perangkat bersama 6 menit lagi (idle 16 menit) → Dialog "Session Expired" tampil dan sesi berstatus Expired
38. Hapus elemen dialog dan overlay lewat DevTools di Browser A
39. Klik menu apa pun di Browser A sehingga request dikirim
40. Verifikasi Server menolak request karena sesi invalid (401)
41. Verifikasi Dialog "Session Expired" muncul kembali
42. Verifikasi Tidak ada data yang dapat dimuat di halaman
43. Pulihkan jam server dan jam browser/perangkat ke waktu nyata

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan (S-05, S-10): urutan di spec ini TC-AUTH-SES-235, 320, 250, 233, 234, 232, 231 (urutan TC sumber 231 sampai 235, 320, 250). Penolakan validasi dan 403 lebih dulu; TC-AUTH-SES-231 memajukan waktu server (menghabiskan sesi dan mengubah state global) sehingga ditaruh paling akhir.
- Spec ini memuat 43 langkah karena tujuh TC granular masing-masing butuh konteks, token, atau user sendiri; tiap TC berdiri sendiri sehingga tidak dipecah.
- TC-AUTH-SES-231 berdependensi pada TC-AUTH-SES-46; langkah 36 dan 37 menyalin langkah idle TC itu (S-04). Asersi Toast Idle Warning milik TC-AUTH-SES-46 tidak diulang.
- Pencatatan: TC-AUTH-SES-233 Expected b ("tidak ada entri log", merujuk TC-AUTH-SES-203), TC-AUTH-SES-234 Expected a ("tanpa dicatat"), serta TC-AUTH-SES-320 dan 250 Expected b ("tidak ada entri log") adalah asersi absence dan ditaruh di spec absence `TC-AUTH-SES-E2E-069-absence-penolakan-force-logout-dan-aksi-admin`; spec ini tidak mengasersinya (S-05).
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): membuka Browser C dan Browser Lisensi (langkah pembuka login Browser C juga menutup konteks Browser C sebelumnya, S-09); login user uji dan Admin License; mengirim request langsung dan heartbeat; memajukan dan memulihkan jam server dan jam browser/perangkat.
- Temuan untuk QA: (1) TC-AUTH-SES-235, 320, dan 250 menyebut "endpoint Create Session" yang tidak ada sebagai endpoint publik di `auth/session-management/API/openapi.yaml`; spec tidak menulis path untuk Create Session dan mengandalkan alat uji. (2) TC-AUTH-SES-320 dan 250 mensyaratkan "token autentikasi" milik user yang belum aktivasi dan tidak aktif tanpa menyebut cara memperolehnya; spec mengasumsikan token diterbitkan alat uji di hook. (3) TC-AUTH-SES-235, 320, 250, 233, dan 234 menyebut "tidak ada dialog" atau "diarahkan ke Login" tanpa konteks UI pengirim request; spec mengirim request dari dalam halaman browser (Browser C atau Browser Lisensi) agar reaksi UI dapat diamati. (4) TC-AUTH-SES-234 memakai Admin License Client Q2 (Tabel Data Uji Pre-setup #2 dan #12), sedangkan akun #2 tidak dinyatakan milik Client Q2; perlu akun Admin License di Client Q2. (5) TC-AUTH-SES-232 "Status sesi tetap Force Logged Out" tidak menyebut cara membaca status di UI; spec membuktikannya lewat alasan penolakan 401 yang tetap sama. (7) TC-AUTH-SES-232 menyebut "request terautentikasi" ke API tanpa menyebut endpoint; spec memilih satu endpoint, `POST /v2/iam/auth/product-sessions`, yang ada di `auth/session-management/API/openapi.yaml`. (6) TC-AUTH-SES-233 dan 234 "sesi tetap Active" tidak menyebut cara membaca status; spec memakai heartbeat dengan token sesi target.
