---
id: TC-AUTH-SES-E2E-058-pencatatan-produk-concurrent-dan-cascade
title: "Pencatatan Sesi Produk: Buka Produk, Concurrent Limit Reached, dan Sesi Berakhir karena Cascade"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-198
  - TC-AUTH-SES-199
  - TC-AUTH-SES-200
  - TC-AUTH-SES-201
  - TC-AUTH-SES-204
  - TC-AUTH-SES-318
  - TC-AUTH-SES-319
coverage:
  web: automated
---

# Pencatatan Sesi Produk: Buka Produk, Concurrent Limit Reached, dan Sesi Berakhir karena Cascade

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`, untuk user profil BASE (scope Client Alpha Logistik: Tabel Data Uji Pre-setup #1, scope Client Q2 untuk user milik Client Q2: Tabel Data Uji Pre-setup #26); oleh akun aktor Principal Admin Console `principalAdminConsole_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_PRINCIPAL_PASSWORD`, untuk user Principal staff), password user uji `Spectra.env.SES_PASSWORD`, email bersuffix per run. User profil BASE: Activated, Active ON, MFA dan Agreement tidak terpicu. Sesi platform web Active di Browser A dibuat lewat login API:
  - TC-AUTH-SES-198: `Yoga Wijaya` (`yogawijaya+{runId}-058@qwertysystem.net`), Client Alpha Logistik (Tabel Data Uji Pre-setup #5: kuota Fixed Asset 5) dengan App Access Fixed Asset; sesi platform di Portal — Product Hub
  - TC-AUTH-SES-200: `Taufik Santoso` (`taufiksantoso+{runId}-058@qwertysystem.net`), Client Q2 (Tabel Data Uji Pre-setup #12: kuota Fixed Asset 2) dengan App Access Fixed Asset dan Supply Asset; sesi platform di Portal — Product Hub
  - TC-AUTH-SES-204: `Galih Pratama` (`galihpratama+{runId}-058@qwertysystem.net`), Client Q2 dengan App Access Fixed Asset dan Supply Asset; sesi platform di Portal — Product Hub
  - TC-AUTH-SES-201: `Mega Kusuma` (`megakusuma+{runId}-058@qwertysystem.net`), Client Alpha Logistik dengan App Access Fixed Asset; sesi platform dan sesi-produk Fixed Asset Active (seat terpakai 1)
  - TC-AUTH-SES-319: `Taufik Damayanti` (`taufikdamayanti+{runId}-058@qwertysystem.net`), Client Alpha Logistik; sesi platform dan sesi Global Settings Active
  - TC-AUTH-SES-199: `Ayu Setiawan` (`ayusetiawan+{runId}-058@qwertysystem.net`), Principal staff (Tabel Data Uji Pre-setup #20) dengan akses Admin Console; sesi platform di Portal — Product Hub
  - TC-AUTH-SES-318: `Ayu Firmansyah` (`ayufirmansyah+{runId}-058@qwertysystem.net`), Principal staff dengan sesi Admin Console Active
- Seed seat Client Q2 (Tabel Data Uji Pre-setup #7 dan #12): dua sesi-produk Fixed Asset Active milik user seed `Gunawan Prakoso` dan `Melati Anggun` sehingga seat Fixed Asset Client Q2 penuh (2 dari 2) selama TC-AUTH-SES-200 dan 204. Seed ini dibuat idempotent di hook `before` (dilewati bila sudah ada) dan sesi-produknya diakhiri di hook `after`.
- Konteks dan akun (dibuka di hook `before`, login pertama tiap konteks ada di hook):
  - Browser Admin: akun aktor Total Control (Global Settings) di atas dengan scope Client Alpha Logistik (Tabel Data Uji Pre-setup #1) dan scope Client Q2 (Tabel Data Uji Pre-setup #26; `Taufik Santoso` dan `Galih Pratama` milik Client Q2), dipakai membaca `Global Settings > Activity Log > Session`, `Activity Log > Session` milik Fixed Asset, dan `Global Settings > User > Detail > User Log`.
  - Browser License: akun aktor `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #2 dan #33: Global Role Manage Global License, scope Client Alpha Logistik dan Client Q2), kredensial `Spectra.env.FA_MGL_PASSWORD`, dipakai di `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset).
  - Browser Principal: akun aktor Principal Admin Console di atas, dipakai membaca `Activity Log > Session` milik Admin Console.
  - Browser A (memuat sesi seed milik user TC yang sedang berjalan).
- Hook `after`: akhiri semua sesi seed (platform, sesi-produk, dan seed seat), tutup konteks Browser A, Browser Admin, Browser License, dan Browser Principal, hapus ketujuh user. Pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `AC_PRINCIPAL_PASSWORD`, `FA_MGL_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`); state global yang diubah: seat Fixed Asset Client Q2 (kuota 2) diisi sesi-produk seed (`Gunawan Prakoso` dan `Melati Anggun`), dipulihkan di hook `after`.
- Kemampuan teknis: empat konteks browser bersamaan dengan Browser A; pembacaan stempel waktu entri log untuk membedakan entri baru dari entri seeding; akses akun aktor ke `Activity Log > Session` milik Fixed Asset dan Admin Console (surface produk, PRD §8 surface #2).
- Akun yang dipakai: user uji masing-masing TC di Browser A; akun aktor di Browser Admin, Browser License, dan Browser Principal.

## Test Steps

### TC-AUTH-SES-204: Pencatatan Concurrent limit reached

1. Tutup konteks Browser A sebelumnya dan buka konteks baru Browser A dengan memuat sesi web seed milik `Galih Pratama`
2. Di Browser A (sesi platform web Active `Galih Pratama` di Portal — Product Hub; seat Fixed Asset Client Q2 penuh) klik card Fixed Asset → Popup "Concurrent session limit reached" tampil
3. Di Browser Admin buka `Activity Log > Session` milik Fixed Asset dan cari entri untuk `Galih Pratama` yang dibuat sesudah langkah 2 dimulai
4. Verifikasi Entri baru tampil di `Activity Log > Session` milik Fixed Asset: Activity `Session`, Status `—`, Note `Concurrent limit reached`
5. Verifikasi Satu event menghasilkan satu entri (tidak ganda) di `Activity Log > Session` milik Fixed Asset
6. Verifikasi Entri itu memiliki kolom Date, User, IP Address, dan Device / Browser yang terisi
7. Buka `Global Settings > User > Detail > User Log` milik `Galih Pratama` dan cari entri yang dibuat sesudah langkah 2 dimulai
8. Verifikasi Entri baru tampil di `Global Settings > User > Detail > User Log`: Activity `Session`, Status `—`, Note `Concurrent limit reached (Fixed Asset)`
9. Verifikasi Satu event menghasilkan satu entri (tidak ganda) di `Global Settings > User > Detail > User Log`
10. Verifikasi Entri itu memiliki kolom Date, IP Address, dan Device / Browser yang terisi (User Log tidak memiliki kolom User)

### TC-AUTH-SES-198: Pencatatan buka produk berlisensi

11. Tutup konteks Browser A sebelumnya dan buka konteks baru Browser A dengan memuat sesi web seed milik `Yoga Wijaya`
12. Di Browser A (sesi platform web Active `Yoga Wijaya` di Portal — Product Hub) klik card Fixed Asset
13. Di Browser License buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset) dan periksa daftar sesi aktif serta hitungan seat
14. Di Browser Admin buka `Activity Log > Session` milik Fixed Asset dan cari entri untuk `Yoga Wijaya` yang dibuat sesudah langkah 12 dimulai
15. Verifikasi Entri baru tampil di `Activity Log > Session` milik Fixed Asset: Activity `Session`, Status `—`, Note `Session started`
16. Verifikasi Satu event menghasilkan satu entri (tidak ganda) di `Activity Log > Session` milik Fixed Asset
17. Verifikasi Entri itu memiliki kolom Date, User, IP Address, dan Device / Browser yang terisi
18. Buka `Global Settings > User > Detail > User Log` milik `Yoga Wijaya` dan cari entri yang dibuat sesudah langkah 12 dimulai
19. Verifikasi Entri baru tampil di `Global Settings > User > Detail > User Log`: Activity `Session`, Status `—`, Note `Session started (Fixed Asset)`
20. Verifikasi Satu event menghasilkan satu entri (tidak ganda) di `Global Settings > User > Detail > User Log`
21. Verifikasi Entri itu memiliki kolom Date, IP Address, dan Device / Browser yang terisi (User Log tidak memiliki kolom User)

### TC-AUTH-SES-200: Pencatatan buka Global Settings di GS Session

22. Tutup konteks Browser A sebelumnya dan buka konteks baru Browser A dengan memuat sesi web seed milik `Taufik Santoso`
23. Di Browser A (sesi platform web Active `Taufik Santoso` di Portal — Product Hub; seat Fixed Asset Client Q2 penuh) klik card Global Settings di Portal
24. Di Browser Admin buka `Global Settings > Activity Log > Session` dan cari entri untuk `Taufik Santoso` yang dibuat sesudah langkah 23 dimulai
25. Verifikasi Entri baru tampil di `Global Settings > Activity Log > Session` (bukan tab terpisah): Activity `Session`, Status `—`, Note `Session started`
26. Verifikasi Satu event menghasilkan satu entri (tidak ganda) di `Global Settings > Activity Log > Session`
27. Verifikasi Entri itu memiliki kolom Date, User, IP Address, dan Device / Browser yang terisi
28. Buka `Global Settings > User > Detail > User Log` milik `Taufik Santoso` dan cari entri yang dibuat sesudah langkah 23 dimulai
29. Verifikasi Entri baru tampil di `Global Settings > User > Detail > User Log`: Activity `Session`, Status `—`, Note `Session started (Global Settings)`
30. Verifikasi Satu event menghasilkan satu entri (tidak ganda) di `Global Settings > User > Detail > User Log`
31. Verifikasi Entri itu memiliki kolom Date, IP Address, dan Device / Browser yang terisi (User Log tidak memiliki kolom User)

### TC-AUTH-SES-199: Pencatatan buka Admin Console

32. Tutup konteks Browser A sebelumnya dan buka konteks baru Browser A dengan memuat sesi web seed milik `Ayu Setiawan`
33. Di Browser A (sesi platform web Active `Ayu Setiawan` di Portal — Product Hub) klik card Admin Console
34. Di Browser Principal buka `Activity Log > Session` milik Admin Console dan cari entri untuk `Ayu Setiawan` yang dibuat sesudah langkah 33 dimulai
35. Verifikasi Entri baru tampil di `Activity Log > Session` milik Admin Console: Activity `Session`, Status `—`, Note `Session started`
36. Verifikasi Satu event menghasilkan satu entri (tidak ganda) di `Activity Log > Session` milik Admin Console
37. Verifikasi Entri itu memiliki kolom Date, User, IP Address, dan Device / Browser yang terisi
38. Di Browser Admin buka `Global Settings > User > Detail > User Log` milik `Ayu Setiawan` dan cari entri yang dibuat sesudah langkah 33 dimulai
39. Verifikasi Entri baru tampil di `Global Settings > User > Detail > User Log`: Activity `Session`, Status `—`, Note `Session started (Admin Console)`
40. Verifikasi Satu event menghasilkan satu entri (tidak ganda) di `Global Settings > User > Detail > User Log`
41. Verifikasi Entri itu memiliki kolom Date, IP Address, dan Device / Browser yang terisi (User Log tidak memiliki kolom User)

### TC-AUTH-SES-201: Pencatatan sesi-produk berakhir karena cascade

42. Tutup konteks Browser A sebelumnya dan buka konteks baru Browser A dengan memuat sesi web seed milik `Mega Kusuma`
43. Di Browser A (sesi platform web dan sesi-produk Fixed Asset Active `Mega Kusuma`) klik menu Profile lalu pilih Log Out → Browser A diarahkan ke halaman Login with Password
44. Di Browser License buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset) dan periksa daftar sesi aktif serta hitungan seat
45. Di Browser Admin buka `Activity Log > Session` milik Fixed Asset dan cari entri untuk `Mega Kusuma` yang dibuat sesudah langkah 43 dimulai
46. Verifikasi Entri baru tampil di `Activity Log > Session` milik Fixed Asset: Activity `Session`, Status `—`, Note `Session ended`
47. Verifikasi Satu event menghasilkan satu entri (tidak ganda) di `Activity Log > Session` milik Fixed Asset
48. Verifikasi Entri itu memiliki kolom Date, User, IP Address, dan Device / Browser yang terisi
49. Buka `Global Settings > User > Detail > User Log` milik `Mega Kusuma` dan cari entri yang dibuat sesudah langkah 43 dimulai
50. Verifikasi Entri baru tampil di `Global Settings > User > Detail > User Log`: Activity `Session`, Status `—`, Note `Session ended (Fixed Asset)`
51. Verifikasi Satu event menghasilkan satu entri (tidak ganda) di `Global Settings > User > Detail > User Log`
52. Verifikasi Entri itu memiliki kolom Date, IP Address, dan Device / Browser yang terisi (User Log tidak memiliki kolom User)

### TC-AUTH-SES-319: Pencatatan sesi Global Settings berakhir karena cascade

53. Tutup konteks Browser A sebelumnya dan buka konteks baru Browser A dengan memuat sesi web seed milik `Taufik Damayanti`
54. Di Browser A (sesi Global Settings Active `Taufik Damayanti`) klik menu Profile lalu pilih Log Out → Browser A diarahkan ke halaman Login with Password
55. Di Browser Admin buka `Global Settings > Activity Log > Session` dan cari entri untuk `Taufik Damayanti` yang dibuat sesudah langkah 54 dimulai
56. Verifikasi Entri `Session ended` (Activity `Session`, Status `—`) tampil di `Global Settings > Activity Log > Session`
57. Buka `Global Settings > User > Detail > User Log` milik `Taufik Damayanti` dan cari entri yang dibuat sesudah langkah 54 dimulai
58. Verifikasi Entri `Session ended` (Activity `Session`, Status `—`) tampil di User Log sebagai `Session ended (Global Settings)`

### TC-AUTH-SES-318: Pencatatan sesi Admin Console berakhir karena cascade

59. Tutup konteks Browser A sebelumnya dan buka konteks baru Browser A dengan memuat sesi web seed milik `Ayu Firmansyah`
60. Di Browser A (sesi Admin Console Active `Ayu Firmansyah`) klik menu Profile lalu pilih Log Out → Browser A diarahkan ke halaman Login with Password
61. Di Browser Principal buka `Activity Log > Session` milik Admin Console dan cari entri untuk `Ayu Firmansyah` yang dibuat sesudah langkah 60 dimulai
62. Verifikasi Entri `Session ended` (Activity `Session`, Status `—`) tampil di `Activity Log > Session` milik Admin Console
63. Di Browser Admin buka `Global Settings > User > Detail > User Log` milik `Ayu Firmansyah` dan cari entri yang dibuat sesudah langkah 60 dimulai
64. Verifikasi Entri `Session ended` (Activity `Session`, Status `—`) tampil di User Log sebagai `Session ended (Admin Console)`

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Kelas harness: pencatatan (Status/Note spesifik) dibaca lewat akun aktor; asersi absence ada di spec `TC-AUTH-SES-E2E-060-absence-pencatatan-sesi`. Klausa absence pada TC-AUTH-SES-204 Expected butir a ("tidak pernah muncul di GS Session") tidak diasersi di spec ini (S-05); dirujuk ke spec absence `TC-AUTH-SES-E2E-067-absence-sesi-produk-dan-concurrent`.
- Penyimpangan urutan (S-05, S-10): urutan di spec ini 204, 198, 200, 199, 201, 319, 318 (urutan TC sumber 198, 199, 200, 201, 204, 318, 319). TC-AUTH-SES-204 (penolakan) lebih dulu; TC yang mengakhiri sesi (201, 319, 318) ditaruh paling akhir. Tiap TC memakai user sendiri, jadi urutan tidak membuat TC saling bergantung. TC-AUTH-SES-204 harus berjalan saat seat Fixed Asset Client Q2 penuh dan tidak ada TC lain di spec ini yang mengambil seat Client Q2; seat penuh dibangun sekali di hook `before` dan ditahan sepanjang spec. TC-AUTH-SES-204 (blokir karena kuota penuh) berada bersama TC pencatatan alur normal karena pencatatannya dibaca di surface yang sama; tidak ada butir P-1 sampai P-5 yang berlaku untuk gabungan ini, sehingga gabungan dicatat di sini.
- Langkah dependensi disalin (S-04): TC-AUTH-SES-198 dari TC-AUTH-SES-95 (langkah 12–13); TC-AUTH-SES-199 dari TC-AUTH-SES-106 (langkah 33); TC-AUTH-SES-200 dari TC-AUTH-SES-108 (langkah 23); TC-AUTH-SES-201 dari TC-AUTH-SES-141 (langkah 43–44); TC-AUTH-SES-204 dari TC-AUTH-SES-96 (langkah 2). Asersi hasil dependensi (popup, dashboard, seat) diuji di spec pemilik TC dependensi.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): perpindahan antar konteks browser; pembacaan Concurrent User (langkah 13 dan 44) sebagai salinan langkah dependensi. Entri "baru" dibedakan dari entri seeding lewat stempel waktu: hanya entri yang dibuat sesudah langkah pembuka TC itu yang dihitung.
- Temuan untuk QA:
  - TC-AUTH-SES-198, 200, 201, 204 menulis user milik Client Alpha, sedangkan dependensinya (TC-AUTH-SES-95, 96, 108, 141) memakai user Client Q2 dengan kuota 2. TC-AUTH-SES-200 dan 204 memerlukan seat Fixed Asset penuh (kuota Client Alpha adalah 5); spec memakai Client Q2 untuk 200 dan 204 dan Client Alpha untuk 198 dan 201.
  - TC-AUTH-SES-204 Expected butir a ("tidak pernah muncul di GS Session") adalah asersi absence di TC pencatatan yang sama dengan asersi presence; asersi absence-nya ada di spec `TC-AUTH-SES-E2E-067-absence-sesi-produk-dan-concurrent`.
  - TC-AUTH-SES-199 dan 318 membaca `Activity Log > Session` milik Admin Console; TC-AUTH-SES-199 menyebut Principal admin dapat membacanya sedangkan TC-AUTH-SES-318 menulis akun Total Control Global Settings. Spec memakai akun Principal Admin Console (Browser Principal) untuk surface Admin Console di kedua TC dan akun Total Control Global Settings untuk User Log.
  - TC-AUTH-SES-318 [DEFERRED] untuk surface `Activity Log > Session` milik Admin Console (forward-dependency PRD §12 #3).
  - TC-AUTH-SES-319 dan 318 Expected tidak menyebut butir "satu entri tidak ganda" dan kolom terisi; spec hanya mengasersi butir yang ada di Expected.
  - Kolom "User" pada Expected butir b TC batch ini tidak ada di surface User Log (PRD §8 surface #3); spec mengasersi kolom User hanya di surface yang memilikinya. PRD §9.8 LOG-06, 10, 11, 12, 13, 16 menulis Status `Success`/`Failed`, sedangkan TC dan PRD §8 menulis `—` untuk Activity `Session`; spec mengikuti TC.
  - TC-AUTH-SES-319 precondition b menyebut "Sesi Global Settings Active" tanpa menjelaskan cara menyiapkannya; spec men-seed sesi Global Settings lewat login API dan pembukaan card Global Settings.
- Langkah penghubung ganti akun (S-03, S-07): tiap TC membuka konteks baru Browser A dengan memuat sesi web seed milik user TC itu, tanpa awalan `Verifikasi`.
