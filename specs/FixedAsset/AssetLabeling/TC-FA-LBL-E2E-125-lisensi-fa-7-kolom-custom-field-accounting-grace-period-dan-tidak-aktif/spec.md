---
id: TC-FA-LBL-E2E-125-lisensi-fa-7-kolom-custom-field-accounting-grace-period-dan-tidak-aktif
title: "Lisensi FA-7: Kolom Custom Field Accounting (Grace Period dan Tidak Aktif)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LBL-571
  - TC-FA-LBL-572
  - TC-FA-LBL-573
coverage:
  web: automated
---

# Lisensi FA-7: Kolom Custom Field Accounting (Grace Period dan Tidak Aktif)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept. Permintaan langsung ke server (TC-FA-LBL-573) memakai klien HTTP, bukan browser.
- Akun aktor: Gate-Accounting `Company Gate Grace` (lisensi `FA-7` Grace Period; Global Role Manage accounting) (Pre-setup #49 dan #42), `Fixture.assetLabeling.akun.gateAccountingGrace`, `Spectra.env.FA_GATE_ACCOUNTING_GRACE_PASSWORD`. Login di hook `before` spec ini (menggantikan akun default suite); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`).
- Akun aktor: Gate-Accounting `Company Gate Lapsed` (lisensi `FA-7` tidak aktif; Global Role Manage accounting) (Pre-setup #49 dan #42), `Fixture.assetLabeling.akun.gateAccountingLapsed`, `Spectra.env.FA_GATE_ACCOUNTING_LAPSED_PASSWORD`. Dipakai pada langkah Ganti akun dan sebagai sesi API aktor TC-FA-LBL-573.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Pre-setup `Company Gate Grace` dan `Company Gate Lapsed` (#49): salinan `Company Gate` (Pre-setup #38; data aset, Group, dan Custom Field sama dengan yang dirujuk lewat `Fixture.assetLabeling.gate`) dengan lisensi `FA-7` pada Grace Period (`Company Gate Grace`) dan lisensi `FA-7` tidak aktif di luar Grace Period (`Company Gate Lapsed`); `Gate-Accounting` (Pre-setup #42) tersedia di keduanya. Label `Gate Label` pada `Gate Item - 51` (`Cost Center` `CC-10`), `Gate Item - 52` (`Cost Center` belum diisi), `Gate Item - 53` (`Cost Center` `CC-30`), dan `Gate Plain - 54` (di luar Scope `Cost Center`).
- Data Dinamis: tidak ada.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.gateAccountingGrace`, `Fixture.assetLabeling.akun.gateAccountingLapsed` (email akun masing-masing), dan `Fixture.assetLabeling.gateGrace` (data Pre-setup #49).
- Kemampuan teknis (disediakan tim FE): hapus preferensi kolom Setup Column Drawer di browser (bagian 4). Klien HTTP dengan sesi API aktor Gate-Accounting `Company Gate Lapsed` untuk permintaan langsung ke server (login API password, token tidak dihitung sebagai sesi web; dinyatakan di `suite.md`).
- State global: konfigurasi kolom Setup Column Drawer Tagged Asset (preferensi browser) diubah dan dipulihkan oleh langkah spec; hook `after` spec ini menghapus preferensi kolom di browser sebagai cadangan, bukan `[Reset to Default]` (bagian 4). Kemampuan menghapus preferensi itu disediakan tim FE. Tidak ada state global lain yang diubah.
- Suite berjalan serial (`parallel: false`).
- Cleanup: spec tidak membuat data. Data Pre-setup hanya dibaca dan tidak diubah (Last Updated tidak berubah).
- Env var: `Spectra.env.FA_GATE_ACCOUNTING_GRACE_PASSWORD`, `Spectra.env.FA_GATE_ACCOUNTING_LAPSED_PASSWORD`, `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`. `FA_LBL_TC_PASSWORD` dipakai hanya oleh hook `after` untuk mengembalikan sesi ke akun default suite.

## Test Steps

### TC-FA-LBL-571: Kolom Custom Field Accounting tersedia pada lisensi FA-7 Grace Period dengan nilai tampil

1. Klik chip `Gate Label` di kolom Label
2. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...` dan perhatikan daftar kolom
3. Verifikasi kolom `Cost Center` tersedia di Setup Column
4. Centang `Cost Center`, lalu klik `[Save]`
5. Verifikasi `Gate Item - 51` menampilkan `CC-10`, `Gate Item - 52` `—`, `Gate Item - 53` `CC-30`, dan `Gate Plain - 54` `—`
6. Verifikasi Drawer tanpa kontrol edit (read-only)
7. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Cost Center`, lalu klik `[Save]`
8. Tutup Drawer Tagged Asset

### TC-FA-LBL-572: Kolom Custom Field Accounting tidak tersedia pada lisensi FA-7 tidak aktif

9. Ganti akun: Logout, login sebagai Gate-Accounting `Company Gate Lapsed` `Fixture.assetLabeling.akun.gateAccountingLapsed` (`Spectra.env.FA_GATE_ACCOUNTING_LAPSED_PASSWORD`), buka Fixed Asset > Settings > Asset Master > tab Labels
10. Klik chip `Gate Label` di kolom Label
11. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...` dan perhatikan daftar kolom
12. Verifikasi kolom `Asset Value (Commercial)` dan `Warranty Expiry` tersedia di Setup Column
13. Verifikasi kolom `Cost Center` tidak tersedia di Setup Column
14. Tutup Setup Column dengan `[✕]`
15. Verifikasi kolom `Cost Center` tidak tampil di tabel Drawer
16. Tutup Drawer Tagged Asset

### TC-FA-LBL-573: Permintaan langsung ke server tidak mengembalikan nilai Custom Field Accounting pada lisensi FA-7 tidak aktif

17. Kirim permintaan langsung ke server dengan sesi API Gate-Accounting `Company Gate Lapsed`: ambil daftar Tagged Assets label `Gate Label` dengan kolom `Cost Center` diminta
18. Verifikasi respons memuat baris `Gate Item - 51` sampai `Gate Plain - 54` (anchor positif)
19. Verifikasi respons tidak memuat nilai `CC-10` maupun `CC-30`

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 4c (Drawer Tagged Asset). Subjudul `###` memetakan langkah ke TC granular.
- Ganti akun: Ganti akun ke Gate-Accounting `Company Gate Lapsed` ditulis eksplisit pada langkah pembuka TC-FA-LBL-572; akun pertama (Gate-Accounting `Company Gate Grace`) login di hook `before`. TC-FA-LBL-573 memakai sesi API akun Lapsed yang sama.
- P-5 (b): TC-FA-LBL-573 (kelas a defense-in-depth, request langsung ke server) dan TC-FA-LBL-571 serta 572 (kelas h state tenant, lisensi FA-7) berada dalam satu spec dengan harness dominan yang sama (Drawer Tagged Asset, ketersediaan kolom Custom Field Accounting menurut lisensi). TC-FA-LBL-573 adalah satu-satunya objek-uji ringan kelas a; asersinya hanya isi respons (8b butir 1).
- K-1: TC-FA-LBL-573 berkelas a dengan Expected berupa isi respons API; TC tetap masuk spec FE+BE walau tumpang tindih dengan `tc-settings-asset-labeling-backend.md`, karena TC granular tetap sumber dan tiap TC tepat satu spec.
- Asersi tambahan (S-03): `Verifikasi respons memuat baris Gate Item - 51 sampai Gate Plain - 54` ditulis sebagai anchor positif untuk asersi absence respons (bagian 8b butir 2); TC tidak menyebutnya.
- Langkah penghubung (S-03): Pemulihan kolom `Cost Center` dan tutup Drawer memulihkan keadaan awal.
- Temuan untuk QA:
  - TC-FA-LBL-571 Expected b ("Drawer tanpa kontrol edit (read-only)") tidak menyebut kontrol yang dimaksud; spec menuliskan teks Expected persis tanpa menambah asersi.
  - TC-FA-LBL-573 Langkah Uji 1 menyebut "mengambil daftar Tagged Assets" tanpa endpoint atau parameter; spec tidak mengarang endpoint (S-13).
  - TC-FA-LBL-571 dan 572 tidak menyebut cara menyiapkan lisensi `FA-7` Grace Period dan tidak aktif; Pre-setup #49 menyatakan kedua company sebagai data environment, sehingga spec tidak mengatur lisensi.
