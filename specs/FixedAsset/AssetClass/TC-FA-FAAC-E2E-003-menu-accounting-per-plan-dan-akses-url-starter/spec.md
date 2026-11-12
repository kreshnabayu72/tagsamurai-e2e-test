---
id: TC-FA-FAAC-E2E-003-menu-accounting-per-plan-dan-akses-url-starter
title: "Menu Accounting per Plan Client dan Akses URL Tab Asset Class pada Plan Starter"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-5
  - TC-FA-FAAC-646
  - TC-FA-FAAC-6
coverage:
  web: automated
---

# Menu Accounting per Plan Client dan Akses URL Tab Asset Class pada Plan Starter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini. Pengecualian atas hook `beforeEach` suite: plan Starter menolak tab Asset Class, sehingga spec ini tidak mengandalkan layar awal tab Asset Class dan membuka layarnya sendiri lewat sidebar dan address bar. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data (state global): plan client Starter (fitur Accounting & Depreciation level None) diatur di hook `before`; hook `after` memulihkan plan client ke nilai awal.
- Tabel "Plan yang diuji" (TC-FA-FAAC-6): Growth, Professional, Enterprise.
- Kemampuan teknis: fixture BE untuk mengatur plan client dan memulihkannya, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`) karena spec ini mengubah plan client.

## Test Steps

### TC-FA-FAAC-5: Menu Accounting pada plan Starter

1. Verifikasi item menu Accounting di sidebar tetap tampil (visible)
2. Verifikasi item menu Accounting berstatus Disabled dengan chip `Upgrade`
3. Klik item menu Accounting
4. Verifikasi halaman Settings > Accounting tidak terbuka dan tab Asset Class tidak terjangkau

### TC-FA-FAAC-646: Akses langsung URL tab Asset Class pada plan Starter

5. Ketik URL tab Asset Class (Settings > Accounting > Asset Class) langsung di address bar browser, tekan Enter
6. Verifikasi toast error `You don't have permission to do this.`
7. Verifikasi konten tab Asset Class (tabel Asset Class dan toolbar) tidak ditampilkan

### TC-FA-FAAC-6: Menu Accounting pada plan Growth, Professional, dan Enterprise

8. Untuk setiap plan pada tabel "Plan yang diuji", lakukan langkah 9 sampai 14
9. Atur plan client ke plan pada tabel lewat fixture BE hingga plan tersimpan
10. Klik menu Accounting di sidebar
11. Klik tab Asset Class
12. Verifikasi menu Accounting Enabled
13. Verifikasi halaman Settings > Accounting terbuka dengan empat tab `Preferences`, `Chart of Accounts`, `Tax Depreciation Class`, `Asset Class`
14. Verifikasi tab `Asset Class` dapat dibuka dengan tabel Asset Class tampil

## Notes

- Langkah penghubung (S-03): langkah 8 (perulangan per plan; isi langkah 9 sampai 14 identik, parameter plan ada di tabel "Plan yang diuji"; 8b butir 7) dan langkah 9 (mengganti plan lewat fixture BE sebagai pemicu state; TC-FA-FAAC-5 dan TC-FA-FAAC-646 berjalan pada plan Starter yang diatur hook `before`).
- Urutan blok: plan Starter (TC-FA-FAAC-5, TC-FA-FAAC-646) lebih dulu, lalu plan yang membuka Accounting (TC-FA-FAAC-6), karena langkah mengganti plan ada di blok terakhir dan pemulihan plan awal dijamin hook `after`.
- Temuan untuk QA:
  - TC-FA-FAAC-6 langkah 1 berbunyi "Login pada client plan Growth ..." tanpa menyebut apakah tiga plan memakai tiga client berbeda atau satu client yang plannya diganti; spec memakai satu client dengan plan diganti lewat fixture BE.
  - TC-FA-FAAC-5 langkah 1 dan 2 tidak menyebut cara membuka layar (precondition hanya "Login"); spec mengamati sidebar pada halaman yang terbuka setelah login.
