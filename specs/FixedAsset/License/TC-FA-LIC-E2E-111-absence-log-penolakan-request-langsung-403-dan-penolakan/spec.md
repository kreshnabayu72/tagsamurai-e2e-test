---
id: TC-FA-LIC-E2E-111-absence-log-penolakan-request-langsung-403-dan-penolakan
title: "Absence Log: Request Langsung yang Ditolak Server Tidak Menulis Entri Log"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LIC-440
  - TC-FA-LIC-441
  - TC-FA-LIC-445
  - TC-FA-LIC-453
  - TC-FA-LIC-549
  - TC-FA-LIC-614
coverage:
  web: automated
---

# Absence Log: Request Langsung yang Ditolak Server Tidak Menulis Entri Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor hook `before`: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), client PT Sejahtera plan Paid, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Spec ini tidak membuka UI untuk membaca log; pemicu dan pembacaan memakai klien HTTP dan kemampuan baca jumlah entri.
- Akun pemicu (token lewat login API, tanpa UI): Read Only #2 `readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net` (`Spectra.env.FA_RO_PASSWORD`), Manage asset license #4 `manageAssetLicenseHQ_automated_{namaCompany}@qwertysystem.net` (`Spectra.env.FA_MAL_HQ_PASSWORD`), Group Manager #6 `groupManagerHQ_automated_{namaCompany}@qwertysystem.net` (`Spectra.env.FA_GM_HQ_PASSWORD`), role tanpa capability #8 `noCapability_automated_{namaCompany}@qwertysystem.net` (`Spectra.env.FA_NOCAP_PASSWORD`), Total Control #1 (`Spectra.env.FA_TC_PASSWORD`), dan Total Control client toggle OFF #35 `totalControlToggleOff_automated_{namaCompany}@qwertysystem.net` (`Spectra.env.FA_TOGGLEOFF_TC_PASSWORD`). Pada TC-FA-LIC-549 token yang dipakai adalah token Total Control #1 sesudah plan client diturunkan ke Starter lewat fixture BE. Nama env di atas didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (sesi API aktor, fixture BE pemulih Pre-setup): dinyatakan sekali di `suite.md`; spec ini merujuknya.
- Data Pre-setup (hanya dibaca; request ditolak sehingga tidak ada perubahan; fixture BE pemulih memulihkannya di hook `before` dan `after`): hierarki dan kuota #12 (Divisi Logistik beralokasi 500), sesi aktif #14 (sesi Budi Santoso aktif; sesi aktor #1 di dua perangkat), client toggle OFF #35 (Divisi Logistik beralokasi 500 dipertahankan), dan client PT Sejahtera yang diturunkan ke plan Starter lewat fixture BE pada TC-FA-LIC-549 (`Divisi Logistik` beralokasi 500) lalu dikembalikan ke Paid. Last Updated alokasi tidak berubah.
- Kemampuan teknis:
  - Klien HTTP untuk request langsung ke endpoint Force Logout dan Edit Allocation (endpoint sesuai openapi dan LLD modul, disediakan tim FE).
  - Membaca state sesi dan jumlah entri log lewat fixture BE: Changelog Allocation Quota, Changelog Concurrent User, System Log tiap akun pemicu, dan Activity Log Fixed Asset. Baseline dicatat per TC sebelum request dan asersi memakai selisih terhadap baseline (S-12).
  - Fixture downgrade plan Starter dan toggle OFF (disediakan tim FE/BE).
- Pemicu (request langsung kelas a) hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji (P-5 butir a); tiap TC punya akun dan baseline sendiri.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-LIC-440: Request langsung Force Logout tanpa hak ditolak 403

1. Catat jumlah entri Changelog Concurrent User, Activity Log, dan System Log akun #2, #4, #6, dan #8 (baseline TC-FA-LIC-440)
2. Kirim request Force Logout langsung untuk sesi Budi Santoso memakai token akun #2, #4, #6, dan #8
3. Verifikasi respons `403 Forbidden` untuk keempat token
4. Verifikasi jumlah entri Changelog Concurrent User tidak bertambah dari baseline
5. Verifikasi jumlah entri Activity Log tidak bertambah dari baseline
6. Verifikasi jumlah entri System Log akun #2, #4, #6, dan #8 tidak bertambah dari baseline

### TC-FA-LIC-441: Request langsung Edit atau Remove Allocation tanpa hak ditolak 403

7. Catat jumlah entri Changelog Allocation Quota, Activity Log, dan System Log akun #2 dan #8 (baseline TC-FA-LIC-441)
8. Kirim request Edit Allocation `Divisi Logistik` = `600` dan request dengan nilai kosong (Remove) memakai token akun #2 dan #8
9. Verifikasi respons `403 Forbidden` untuk kedua token pada kedua request
10. Verifikasi jumlah entri Changelog Allocation Quota tidak bertambah dari baseline
11. Verifikasi jumlah entri Activity Log tidak bertambah dari baseline
12. Verifikasi jumlah entri System Log akun #2 dan #8 tidak bertambah dari baseline

### TC-FA-LIC-445: Force Logout atas sesi sendiri via API ditolak server tanpa dialog khusus dan tanpa log

13. Catat jumlah entri System Log Rudi Hartono dan Activity Log (baseline TC-FA-LIC-445)
14. Kirim request Force Logout langsung untuk sesi milik aktor #1 sendiri memakai token akun #1
15. Verifikasi respons akses ditolak (`403 Forbidden`)
16. Verifikasi jumlah entri System Log Rudi Hartono tidak bertambah dari baseline
17. Verifikasi jumlah entri Activity Log tidak bertambah dari baseline

### TC-FA-LIC-453: Payload Allocated Quota non-bilangan-bulat via API ditolak server

18. Catat jumlah entri Changelog Allocation Quota, Activity Log, dan System Log Rudi Hartono (baseline TC-FA-LIC-453)
19. Kirim request Edit Allocation dengan nilai `12.5`, `-5`, `abc`, dan `1e3` melalui klien HTTP memakai token akun #1
20. Verifikasi keempat request ditolak server dengan respons error 4xx
21. Verifikasi jumlah entri Changelog Allocation Quota tidak bertambah dari baseline
22. Verifikasi jumlah entri Activity Log tidak bertambah dari baseline
23. Verifikasi jumlah entri System Log Rudi Hartono tidak bertambah dari baseline

### TC-FA-LIC-549: Request langsung Edit dan Remove Allocation saat plan Starter ditolak 403

24. Turunkan plan client ke Starter lewat fixture downgrade (`Divisi Logistik` beralokasi 500)
25. Catat jumlah entri Changelog Allocation Quota (baseline TC-FA-LIC-549)
26. Kirim request Edit Allocation `Divisi Logistik` = `600` memakai token akun #1
27. Kirim request Edit `Divisi Logistik` dengan nilai kosong (Remove Allocation) memakai token yang sama
28. Verifikasi kedua request mendapat respons `403 Forbidden`
29. Verifikasi jumlah entri Changelog Allocation Quota tidak bertambah dari baseline
30. Pulihkan plan client ke Paid lewat fixture BE

### TC-FA-LIC-614: Request langsung Edit dan Remove Allocation saat Paid dengan toggle OFF ditolak 403

31. Catat jumlah entri Changelog Allocation Quota, System Log akun #35, dan Activity Log (baseline TC-FA-LIC-614)
32. Kirim request Edit Allocation `Divisi Logistik` = `600` memakai token akun #35
33. Kirim request Edit `Divisi Logistik` dengan nilai kosong (Remove Allocation) memakai token akun #35
34. Verifikasi kedua request mendapat respons `403 Forbidden` seperti request tanpa capability
35. Verifikasi jumlah entri Changelog Allocation Quota tidak bertambah dari baseline
36. Verifikasi jumlah entri System Log akun #35 tidak bertambah dari baseline
37. Verifikasi jumlah entri Activity Log tidak bertambah dari baseline

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Pembagian TC lintas spec: asersi status respons `403` dan state data (sesi tetap aktif, Allocated Quota tetap 500) pada TC-FA-LIC-440, TC-FA-LIC-441, TC-FA-LIC-445, TC-FA-LIC-453, TC-FA-LIC-549, dan TC-FA-LIC-614 ada di spec kelas a masing-masing (K-1); spec ini mengasersi pemicu `403` hanya sebagai anchor absence dan memuat klausa absence log (S-05, bagian 8b butir 1). Spec asal mencatat rujukan ke spec ini di `## Notes`.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1, 7, 13, 18, 25, dan 31 mencatat baseline; langkah 24 dan 30 menyetel dan memulihkan plan (S-09). Asersi respons dan jumlah entri tidak melewati browser, sehingga tidak ada asersi tampilan (bagian 8b butir 1).
- Anchor absence: respons penolakan (langkah 3, 9, 15, 20, 28, 34) membuktikan request diproses server sebelum asersi jumlah entri, dan baseline per surface menjadi pembanding agregat (bagian 8b butir 2).
- Spec di atas 35 langkah (37 langkah): alasan dipertahankan, seluruh blok adalah absence log atas request langsung yang ditolak, dengan akun dan baseline masing-masing, dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-LIC-549 butir c ("Tidak ada entri log baru") tidak menyebut surface; spec memeriksa Changelog Allocation Quota sesuai langkah 3 TC.
  - TC-FA-LIC-135, 136, dan 175 memuat klausa absence log pada alur fungsional (bukan request langsung) dan tidak ada di spec ini.
