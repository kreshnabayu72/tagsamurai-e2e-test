---
id: TC-AUTH-ACT-E2E-017-absence-pencatatan-halaman-publik
title: "Tidak Ada Pencatatan oleh Auth Account Activation dari Halaman Publik"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-90
  - TC-AUTH-ACT-91
  - TC-AUTH-ACT-92
  - TC-AUTH-ACT-93
  - TC-AUTH-ACT-94
  - TC-AUTH-ACT-95
coverage:
  web: automated
---

# Tidak Ada Pencatatan oleh Auth Account Activation dari Halaman Publik

## Prerequisites

- Akun aktor: Total Control (Global Settings), pre-setup `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.GS_TC_PASSWORD`. Login di browser admin dilakukan di hook `before`.
- Password user uji dari `Spectra.env.ACT_PASSWORD`. Tidak ada password atau token di spec atau fixture; `abc` adalah input uji validasi yang submit-nya diblokir.
- Hook `before` (seeding API) membuat user berikut dengan suffix per run `+{runId}-017` beserta link aktivasinya, semuanya Pending Activation dengan token Active kecuali disebut lain:
  - TC-AUTH-ACT-90: `Andi Santoso` (`andisantoso+{runId}-017@qwertysystem.net`)
  - TC-AUTH-ACT-91: `Dewi Kurniawan` (`dewikurniawan+{runId}-017@qwertysystem.net`); token uji `unknown-token-12345`
  - TC-AUTH-ACT-92: `Rizky Cahyani` (`rizkycahyani+{runId}-017@qwertysystem.net`)
  - TC-AUTH-ACT-93: `Nur Rahmawati` (`nurrahmawati+{runId}-017@qwertysystem.net`)
  - TC-AUTH-ACT-94: `Agus Prakoso` (`agusprakoso+{runId}-017@qwertysystem.net`)
  - TC-AUTH-ACT-95: `Wahyu Maharani` (`wahyumaharani+{runId}-017@qwertysystem.net`), sudah Activated dengan token Consumed; disiapkan sendiri oleh spec ini lewat API (tidak bergantung pada aktivasi di TC lain)
  - TC-AUTH-ACT-01 (absence): `Budi Aditya` (`budiaditya+{runId}-017@qwertysystem.net`)
  - TC-AUTH-ACT-74 (absence): `Laras Hidayat` (`larashidayat+{runId}-017@qwertysystem.net`)
- Hook `after` menghapus semua user di atas (tetap jalan walau seeding atau langkah gagal sebagian).
- Kemampuan teknis: dua konteks browser (browser admin untuk membaca surface log dan jendela privat publik untuk halaman aktivasi).

## Test Steps

### TC-AUTH-ACT-90: Membuka link aktivasi valid tidak menulis pencatatan apa pun

1. Pada browser admin, buka Activity Log (`Global Settings > Activity Log > Session`) serta Tab Changelog, Tab System Log, dan Tab User Log pada `Global Settings > User > Detail` untuk user `Andi Santoso` dan catat jumlah entri pada keempat surface yang ada (jangkar: entri pembuatan user oleh admin tetap terlihat)
2. Di jendela privat, buka link aktivasi user `Andi Santoso` → `Auth > Account Activation > Set Password` tampil
3. Kembali ke browser admin, muat ulang keempat surface tersebut dan bandingkan jumlah entri untuk user `Andi Santoso`
4. Verifikasi Activity Log (Session), Tab User Log, Tab System Log, dan Tab Changelog tidak memuat entri baru untuk user `Andi Santoso` akibat pembukaan link aktivasi valid
5. Verifikasi Entri milik modul lain yang sudah ada sebelumnya (jangkar) tetap tampil dan jumlahnya tidak berubah

### TC-AUTH-ACT-91: Membuka link aktivasi tidak valid tidak menulis pencatatan apa pun

6. Pada browser admin, buka Activity Log (`Global Settings > Activity Log > Session`) serta Tab Changelog, Tab System Log, dan Tab User Log pada `Global Settings > User > Detail` untuk user `Dewi Kurniawan` dan catat jumlah entri pada keempat surface yang ada (jangkar: entri pembuatan user oleh admin tetap terlihat)
7. Di jendela privat, buka link aktivasi dengan token `unknown-token-12345` → `Auth > Account Activation > Invalid Link` tampil
8. Kembali ke browser admin, muat ulang keempat surface tersebut dan bandingkan jumlah entri untuk user `Dewi Kurniawan`
9. Verifikasi Activity Log (Session), Tab User Log, Tab System Log, dan Tab Changelog tidak memuat entri baru untuk user `Dewi Kurniawan` akibat pembukaan link tidak valid dan tampilnya halaman 404
10. Verifikasi Entri milik modul lain yang sudah ada sebelumnya (jangkar) tetap tampil dan jumlahnya tidak berubah

### TC-AUTH-ACT-92: Set Password berhasil tidak menulis pencatatan apa pun

11. Pada browser admin, buka Activity Log (`Global Settings > Activity Log > Session`) serta Tab Changelog, Tab System Log, dan Tab User Log pada `Global Settings > User > Detail` untuk user `Rizky Cahyani` dan catat jumlah entri pada keempat surface yang ada (jangkar: entri pembuatan user oleh admin tetap terlihat)
12. Di jendela privat, buka link aktivasi user `Rizky Cahyani`
13. Ketik `Spectra.env.ACT_PASSWORD` di field Password dan Confirm Password
14. Klik button "Set Password"
15. Kembali ke browser admin, muat ulang keempat surface tersebut dan bandingkan jumlah entri untuk user `Rizky Cahyani`
16. Verifikasi Activity Log (Session), Tab User Log, Tab System Log, dan Tab Changelog tidak memuat entri baru untuk user `Rizky Cahyani` akibat aktivasi berhasil (token consumed dan transisi status)
17. Verifikasi Entri milik modul lain yang sudah ada sebelumnya (jangkar) tetap tampil dan jumlahnya tidak berubah
18. Verifikasi Token aktivasi user `Rizky Cahyani` Consumed dan status user Activated

### TC-AUTH-ACT-93: Set Password gagal validasi tidak menulis pencatatan apa pun

19. Pada browser admin, buka Activity Log (`Global Settings > Activity Log > Session`) serta Tab Changelog, Tab System Log, dan Tab User Log pada `Global Settings > User > Detail` untuk user `Nur Rahmawati` dan catat jumlah entri pada keempat surface yang ada (jangkar: entri pembuatan user oleh admin tetap terlihat)
20. Di jendela privat, buka link aktivasi user `Nur Rahmawati`
21. Klik button "Set Password" dengan kedua field kosong, lalu ketik `abc` di Password dan `abc` di Confirm Password dan klik button "Set Password"
22. Kembali ke browser admin, muat ulang keempat surface tersebut dan bandingkan jumlah entri untuk user `Nur Rahmawati`
23. Verifikasi Activity Log (Session), Tab User Log, Tab System Log, dan Tab Changelog tidak memuat entri baru untuk user `Nur Rahmawati` akibat percobaan Set Password yang gagal validasi
24. Verifikasi Entri milik modul lain yang sudah ada sebelumnya (jangkar) tetap tampil dan jumlahnya tidak berubah

### TC-AUTH-ACT-94: Klik Go to Login tidak menulis pencatatan apa pun

25. Pada browser admin, buka Activity Log (`Global Settings > Activity Log > Session`) serta Tab Changelog, Tab System Log, dan Tab User Log pada `Global Settings > User > Detail` untuk user `Agus Prakoso` dan catat jumlah entri pada keempat surface yang ada (jangkar: entri pembuatan user oleh admin tetap terlihat)
26. Di jendela privat, buka link aktivasi user `Agus Prakoso`
27. Ketik `Spectra.env.ACT_PASSWORD` di field Password dan Confirm Password
28. Klik button "Set Password"
29. Klik CTA "Go to Login"
30. Kembali ke browser admin, muat ulang keempat surface tersebut dan bandingkan jumlah entri untuk user `Agus Prakoso`
31. Verifikasi Activity Log (Session), Tab User Log, Tab System Log, dan Tab Changelog tidak memuat entri baru untuk user `Agus Prakoso` akibat klik Go to Login
32. Verifikasi Entri milik modul lain yang sudah ada sebelumnya (jangkar) tetap tampil dan jumlahnya tidak berubah
33. Verifikasi Token aktivasi user `Agus Prakoso` Consumed dan status user Activated

### TC-AUTH-ACT-95: Membuka link yang sudah dipakai dan tampilnya halaman Invalid Link tidak menulis pencatatan apa pun

34. Pada browser admin, buka Activity Log (`Global Settings > Activity Log > Session`) serta Tab Changelog, Tab System Log, dan Tab User Log pada `Global Settings > User > Detail` untuk user `Wahyu Maharani` dan catat jumlah entri pada keempat surface yang ada (jangkar: entri pembuatan user oleh admin tetap terlihat)
35. Di jendela privat, buka link aktivasi user `Wahyu Maharani` yang sudah dipakai → `Auth > Account Activation > Invalid Link` varian Used tampil
36. Kembali ke browser admin, muat ulang keempat surface tersebut dan bandingkan jumlah entri untuk user `Wahyu Maharani`
37. Verifikasi Activity Log (Session), Tab User Log, Tab System Log, dan Tab Changelog tidak memuat entri baru untuk user `Wahyu Maharani` akibat tampilnya halaman 404 varian Used
38. Verifikasi Entri milik modul lain yang sudah ada sebelumnya (jangkar) tetap tampil dan jumlahnya tidak berubah

### TC-AUTH-ACT-01 (absence): Screening halaman Set Password tidak menulis pencatatan dari Auth

39. Pada browser admin, buka Activity Log (`Global Settings > Activity Log > Session`) serta Tab Changelog, Tab System Log, dan Tab User Log pada `Global Settings > User > Detail` untuk user `Budi Aditya` dan catat jumlah entri pada keempat surface yang ada (jangkar: entri pembuatan user oleh admin tetap terlihat)
40. Di jendela privat, buka link aktivasi user `Budi Aditya` → `Auth > Account Activation > Set Password` tampil, susuri halaman tanpa mengisi atau mengklik apa pun
41. Kembali ke browser admin, muat ulang keempat surface tersebut dan bandingkan jumlah entri untuk user `Budi Aditya`
42. Verifikasi Tidak ada entri pencatatan dari Auth untuk user `Budi Aditya`

### TC-AUTH-ACT-74 (absence): Aktivasi lalu Go to Login tidak menulis pencatatan dari Auth

43. Pada browser admin, buka Activity Log (`Global Settings > Activity Log > Session`) serta Tab Changelog, Tab System Log, dan Tab User Log pada `Global Settings > User > Detail` untuk user `Laras Hidayat` dan catat jumlah entri pada keempat surface yang ada (jangkar: entri pembuatan user oleh admin tetap terlihat)
44. Di jendela privat, buka link aktivasi user `Laras Hidayat`, ketik `Spectra.env.ACT_PASSWORD` di field Password dan Confirm Password, klik button "Set Password", lalu klik CTA "Go to Login"
45. Kembali ke browser admin, muat ulang keempat surface tersebut dan bandingkan jumlah entri untuk user `Laras Hidayat`
46. Verifikasi Status user `Laras Hidayat` Activated dan token Consumed; tidak ada pencatatan dari Auth

## Notes

- Mode: FE+BE. Sumber: `auth/account-activation/TestCases/tc-account-activation.md`.
- Kelas harness g (asersi absence), pemicu dari halaman publik aktivasi. Absence untuk pemicu admin (pembuatan user, Resend, penolakan login) ada di E2E-029; dipisah supaya pemicu publik dan pemicu admin tidak bergantian dalam satu spec.
- TC terbelah lintas spec (prinsip 10): asersi absence TC-AUTH-ACT-01 (Post Condition b) dan TC-AUTH-ACT-74 (Post Condition) diuji di spec ini; bagian fungsionalnya ada di E2E-001 (TC-01) dan E2E-032 (TC-74). `sourceTc` tidak mencantumkan keduanya supaya tiap TC tetap terpetakan ke satu spec utama di `docs/coverage`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec ini 46 langkah, di atas smell sekitar 35 langkah (prinsip 13). Dipertahankan karena tiap blok TC berdiri sendiri (soft assertion, user terpisah per blok), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan seluruh spec satu kelas harness (g).
