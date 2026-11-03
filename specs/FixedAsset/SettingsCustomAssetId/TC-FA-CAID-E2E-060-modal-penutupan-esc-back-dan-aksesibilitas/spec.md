---
id: TC-FA-CAID-E2E-060-modal-penutupan-esc-back-dan-aksesibilitas
title: "Modal Code List dan Changelog: Penutupan, Esc Berlapis, Back Browser, dan Aksesibilitas Fokus"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-160
  - TC-FA-CAID-161
  - TC-FA-CAID-231
  - TC-FA-CAID-232
  - TC-FA-CAID-343
coverage:
  web: automated
---

# Modal Code List dan Changelog: Penutupan, Esc Berlapis, Back Browser, dan Aksesibilitas Fokus

## Prerequisites

- Mode: FE+BE (isi Code List dibaca dari backend nyata).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun aktor: Total Control Company Alpha (Pre-setup No 1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Hook suite (`suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-asset-id` disetel `seen`; konfigurasi Company Alpha baseline B1 (Pre-setup No 10) dipulihkan lewat seed API sesi aktor (dipakai sebagai precondition TC, tidak diasersi); layar awal Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka di `beforeEach`. Suite berjalan serial (`parallel: false`).
- Nilai data dirujuk lewat `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Master data Code List Company Alpha (Pre-setup No 28): Groups `Head Office` (HO), `Head Office > Floor 1` (F1), `Head Office > Floor 2` (F2), `Jakarta Office` (JKT), `Surabaya Branch` (SBY, Excess), `Warehouse` (WH); Categories `IT Equipment` (ITE), `IT Equipment > Laptop` (LAP), `Old Equipment` (OLD, Locked), `Printer` (PRN); Asset Names `Dell, Latitude 14"` (DL14), `LaserJet Pro` (LJP), `ThinkPad T490` (T490); Divisions `Finance` (FIN), `Human Resources` (HR), `Operations` (OPS); Accounts Active `Computer Equipment` (1210) dan `Office Furniture` (1220). Di-seed di hook `before` lewat sesi API aktor (kemampuan disediakan tim FE). Dataset itu dipakai sebagai precondition TC-FA-CAID-160 dan 161 untuk Modal View Code List, tidak diasersi.
- Data Pre-setup No 15 (`Company Changelog`): entri seed L1 sampai L7 log Custom Asset ID, di-seed lewat API di hook `before` pada Company aktor (kemampuan disediakan tim FE/BE); entri log audit lain tidak dihapus dan tidak diasersi. Data Pre-setup No 27: General Settings baseline (Date Format `dd/MM/yy`, Time Format 24 jam). Keduanya dipakai sebagai precondition TC-FA-CAID-231 dan 232 untuk Modal Changelog, tidak diasersi (spec tidak mengasersi isi entri).
- Kemampuan teknis: navigasi riwayat browser (tombol Back) dan penekanan tombol Tab berulang untuk mengamati fokus keyboard.
- Data Dinamis: tidak ada. State global: tidak ada yang diubah.

## Test Steps

### TC-FA-CAID-160: Menutup Modal Code List

1. Klik tautan `[View Code List]`
2. Klik area backdrop di luar modal
3. Verifikasi klik backdrop tidak menutup modal
4. Klik ikon close `[✕]`
5. Verifikasi `[✕]` menutup modal
6. Klik tautan `[View Code List]`
7. Tekan `Esc`
8. Verifikasi `Esc` menutup modal

### TC-FA-CAID-161: Esc menutup overlay paling atas lebih dulu

9. Klik tautan `[View Code List]`
10. Klik header kolom Actions (⋯) sampai overlay Column Visibility terbuka
11. Tekan `Esc`
12. Verifikasi Esc pertama menutup overlay Column Visibility
13. Verifikasi Modal Code List tetap terbuka
14. Tekan `Esc` lagi
15. Verifikasi Esc kedua menutup Modal Code List

### TC-FA-CAID-231: Menutup Modal Changelog

16. Klik tombol `[Changelog]` pada header kartu untuk membuka Modal Changelog
17. Klik area backdrop di luar modal
18. Verifikasi klik backdrop tidak menutup Modal Changelog
19. Klik ikon close `[✕]`
20. Verifikasi `[✕]` menutup Modal Changelog
21. Klik tombol `[Changelog]` pada header kartu untuk membuka Modal Changelog
22. Tekan `Esc`
23. Verifikasi `Esc` menutup Modal Changelog

### TC-FA-CAID-232: Aksesibilitas modal

24. Klik tombol `[Changelog]` pada header kartu untuk membuka Modal Changelog
25. Tekan Tab berulang sampai melewati elemen terakhir di modal
26. Verifikasi fokus keyboard berputar di dalam modal dan tidak keluar ke halaman di belakangnya
27. Tekan `Esc`
28. Verifikasi `Esc` menutup Modal Changelog

### TC-FA-CAID-343: Tombol Back browser saat Modal Code List terbuka

29. Klik tab `Asset Name`, lalu klik tab `Custom Asset ID` pada Fixed Asset > Settings > Asset Master
30. Klik tautan `[View Code List]`
31. Klik tombol Back browser
32. Verifikasi pengguna kembali ke tab `Asset Name`
33. Verifikasi Modal Code List tertutup
34. Verifikasi modal tidak masuk riwayat browser

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. 34 langkah.
- Urutan TC di dalam spec: TC-FA-CAID-160, 161, 231, 232, lalu 343. TC-FA-CAID-343 meninggalkan tab Custom Asset ID lewat Back sehingga ditaruh paling akhir.
- Langkah penghubung (tanpa `Verifikasi`): langkah 29 (membentuk riwayat navigasi tab `Asset Name` lalu tab `Custom Asset ID` yang menjadi precondition TC-FA-CAID-343; hook `beforeEach` suite membuka tab Custom Asset ID langsung tanpa riwayat itu).
- Pembukaan modal diulang sesudah `[✕]` atau `Esc` karena TC-FA-CAID-160 dan 231 menguji penutupan dengan dua cara dan membuka kembali modal di antaranya; langkah itu adalah langkah TC.
- Pembagian TC lintas spec: Modal Changelog (format, Search, Filter, Sort, Setup Column, Pagination) dikover spec 066 sampai 080; TC-FA-CAID-160, 161, 231, 232, dan 343 hanya ada di spec ini.
- Temuan untuk QA:
  - Kolom akun TC-FA-CAID-231 dan 232 menyebut dataset `Company Changelog` (Pre-setup No 15) bersama akun #1 (Company Alpha) tanpa menyebut Company-nya; spec menyiapkan dataset pada Company aktor.
  - TC-FA-CAID-343 mencantumkan sumber `toast-copy.md` yang tidak relevan dengan isi Expected (navigasi Back); spec mengikuti Expected.
  - TC-FA-CAID-232 menyebut "melewati elemen terakhir di modal" tanpa jumlah penekanan Tab; spec menekan Tab berulang sampai fokus kembali ke elemen pertama.
