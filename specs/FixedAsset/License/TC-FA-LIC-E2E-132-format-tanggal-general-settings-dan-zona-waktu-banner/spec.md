---
id: TC-FA-LIC-E2E-132-format-tanggal-general-settings-dan-zona-waktu-banner
title: "Format Tanggal General Settings pada Tabel, Modal Changelog, dan Zona Waktu Banner"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-420
  - TC-FA-LIC-421
  - TC-FA-LIC-422
coverage:
  web: automated
---

# Format Tanggal General Settings pada Tabel, Modal Changelog, dan Zona Waktu Banner

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, kata sandi `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1). Password tidak ditulis di spec atau fixture; nama env `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup #15 (`Fixture.fixedAssetLicense.banner`): term live Active milik PT Sejahtera, Plan Owner `PT Maju Bersama` (Distributor), End Date 31/12/26, konfigurasi Client Lifecycle 30/7/1 (nilai bawaan), Grace End 30/01/27. Tanggal "hari ini" dan status term diatur lewat fixture BE (disediakan tim FE/BE, endpoint tidak dikarang); jam server tidak digeser. Fixture `fixedAssetLicense` adalah fixture baru yang isinya ditetapkan tim FE.
- Data Pre-setup #13 (`Fixture.fixedAssetLicense.riwayat`), #26 (`Fixture.fixedAssetLicense.sesiTabel`: Login Time `29 Sep 26, 09:20 AM` untuk contoh), dan #27 (`Fixture.fixedAssetLicense.changelogAlokasi`) dibaca tanpa diubah; disediakan tim FE/BE.
- General Settings (Date Format, Time Format, zona waktu) diatur lewat fixture BE: Date Format `dd MMM yy`, Time Format 12 jam, zona Asia/Jakarta untuk TC-FA-LIC-420 dan 421; zona Asia/Jakarta lalu UTC untuk TC-FA-LIC-422. Dipulihkan ke `dd/MM/yy`, `HH:mm`, `Asia/Jakarta` di hook `after`.
- TC-FA-LIC-422: waktu server fixture 30/12/26 20:00 UTC (jam server digeser); sesi UI dan sesi API aktor tetap valid selama jam digeser, jam dipulihkan di hook `after` (dinyatakan sekali di `suite.md`).
- State global: tanggal fixture hari ini, status term, Plan Owner, dan konfigurasi Client Lifecycle dipulihkan ke Pre-setup #15 di hook `after` (tetap jalan walau spec gagal di tengah).
- Hook dan kemampuan suite (fixture BE penyetel state, sesi API aktor, flag Guided Tooltip): dinyatakan sekali di `suite.md`.
- Suite serial (`parallel: false`, lihat `suite.md`): spec mengubah state global bersama (tanggal fixture, status term).

## Test Steps

### TC-FA-LIC-420: Format tanggal General Settings pada tabel riwayat dan sesi (Surface 1) termasuk input date filter

1. Atur General Settings: Date Format `dd MMM yy`, Time Format 12 jam, zona Asia/Jakarta lewat fixture BE
2. Buka License > All License
3. Klik Sub-Tab `Subscription History`
4. Verifikasi kolom Start Date dan End Date memakai Date Format dan Time Format General Settings
5. Klik Sub-Tab `Allocation History`
6. Verifikasi kolom Date, End Date, dan Last Updated memakai Date Format dan Time Format General Settings
7. Klik Tab `Concurrent User`
8. Verifikasi kolom Login Time memakai Date Format dan Time Format General Settings (`29 Sep 26, 09:20 AM`)
9. Verifikasi kolom Last Activity memakai Date Format dan Time Format General Settings
10. Buka Filter Panel
11. Pilih rentang tanggal pada Filter Panel
12. Verifikasi teks tanggal terpilih pada input date filter memakai Date Format yang sama
13. Tutup Filter Panel

### TC-FA-LIC-421: Format tanggal General Settings pada Modal Changelog (Surface 2)

14. Atur General Settings: Date Format `dd MMM yy` lewat fixture BE
15. Buka License > Allocation Quota
16. Klik ikon Changelog pada toolbar Section 2
17. Verifikasi kolom Date Changelog memakai Date Format dan Time Format General Settings
18. Tutup modal Changelog: Allocation Quota dengan `×`

### TC-FA-LIC-422: Perubahan General Settings tercermin di License tanpa hardcode (zona waktu mengubah N banner)

19. Atur waktu server fixture ke `30/12/26 20:00` UTC dan zona General Settings ke Asia/Jakarta (di sana 31/12/26 03:00) lewat fixture BE
20. Buka License > All License
21. Verifikasi Tabs Bar tampil
22. Verifikasi banner tidak dirender (N dihitung terhadap tanggal kalender 31/12/26 sehingga N = 0)
23. Ubah zona General Settings ke UTC (30/12/26 20:00) lewat fixture BE
24. Muat ulang halaman License
25. Verifikasi banner Final `Subscription expires tomorrow` tampil (N = 1)

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): pengaturan General Settings dan waktu server lewat fixture BE, "Tutup Filter Panel", dan "Tutup modal Changelog: Allocation Quota".
- Asersi "banner tidak dirender" didahului `Verifikasi Tabs Bar tampil` sebagai anchor positif.
- Temuan untuk QA:
  - TC-FA-LIC-420 langkah 2 ("Buka Filter Panel dan pilih rentang tanggal") tidak menyebut tabel dan field tanggal yang dipakai; spec memakai Filter Panel tabel Concurrent User yang sedang terbuka dan field tanggal yang tersedia di sana.
  - TC-FA-LIC-420 Expected hanya memberi contoh format untuk Login Time (`29 Sep 26, 09:20 AM`); contoh format kolom lain tidak tertulis.
  - TC-FA-LIC-422 tidak menyebut tanggal fixture hari ini; N dihitung dari waktu server yang diatur pada precondition.
