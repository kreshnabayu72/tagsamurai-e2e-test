---
id: TC-FA-CAID-E2E-064-code-list-search-kelas-nama-hierarki-dan-kelas-nama-datar
title: "Modal View Code List: Search Kelas Nama Hierarki dan Kelas Nama Datar"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-122
  - TC-FA-CAID-123
coverage:
  web: automated
---

# Modal View Code List: Search Kelas Nama Hierarki dan Kelas Nama Datar

## Prerequisites

- Mode: FE+BE (isi Code List dibaca dari backend nyata).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun aktor: Total Control Company Alpha (Pre-setup No 1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Hook suite (`suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-asset-id` disetel `seen`; konfigurasi Company Alpha baseline B1 (Pre-setup No 10) dan aset A1 sampai A5 (Pre-setup No 11) dipulihkan lewat seed API sesi aktor; layar awal Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka di `beforeEach`. Suite berjalan serial (`parallel: false`).
- Nilai data dirujuk lewat `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Master data Code List Company Alpha (Pre-setup No 28): Groups `Head Office` (HO), `Head Office > Floor 1` (F1), `Head Office > Floor 2` (F2), `Jakarta Office` (JKT), `Surabaya Branch` (SBY, Excess), `Warehouse` (WH); Categories `IT Equipment` (ITE), `IT Equipment > Laptop` (LAP), `Old Equipment` (OLD, Locked), `Printer` (PRN); Asset Names `Dell, Latitude 14"` (DL14), `LaserJet Pro` (LJP), `ThinkPad T490` (T490); Divisions `Finance` (FIN), `Human Resources` (HR), `Operations` (OPS); Accounts Active `Computer Equipment` (1210) dan `Office Furniture` (1220). Di-seed di hook `before` lewat sesi API aktor (kemampuan disediakan tim FE). Spec hanya membaca.
- Data Dinamis: tidak ada. State global: tidak ada yang diubah.

## Test Steps

### TC-FA-CAID-122: Search tab Groups dan Categories

1. Klik tautan `[View Code List]`
2. Ketik Search `floor`, tekan Enter
3. Verifikasi `Group Name`: `floor` menemukan `Head Office > Floor 1` dan `Head Office > Floor 2`
4. Ganti isi kotak search dengan `jkt`, tekan Enter
5. Verifikasi `Code` tab Groups: `jkt` menemukan `Jakarta Office / JKT`
6. Klik tab `Category Codes`
7. Ketik Search `laptop`, tekan Enter
8. Verifikasi `Category Name`: `laptop` menemukan `IT Equipment > Laptop / LAP`
9. Ganti isi kotak search dengan `prn`, tekan Enter
10. Verifikasi `Code` tab Categories: `prn` menemukan `Printer / PRN`
11. Verifikasi pencocokan tidak membedakan huruf besar-kecil dan memakai substring (keyword huruf kecil `floor`, `jkt`, `laptop`, dan `prn` menemukan nilai berhuruf kapital dan potongan teks)

### TC-FA-CAID-123: Search tab Asset Names, Divisions, dan Accounts

12. Klik tab `Asset Name Codes`
13. Ketik Search `thinkpad`, tekan Enter
14. Verifikasi `Asset Name`: `thinkpad` menemukan `ThinkPad T490 / T490`
15. Ganti isi kotak search dengan `ljp`, tekan Enter
16. Verifikasi `Code`: `ljp` menemukan `LaserJet Pro / LJP`
17. Klik tab `Division Codes`
18. Ketik Search `human`, tekan Enter
19. Verifikasi `Division Name`: `human` menemukan `Human Resources / HR`
20. Ganti isi kotak search dengan `fin`, tekan Enter
21. Verifikasi `Code`: `fin` menemukan `Finance / FIN`
22. Klik tab `Account Codes`
23. Ketik Search `computer`, tekan Enter
24. Verifikasi `Account Name`: `computer` menemukan `Computer Equipment / 1210`
25. Ganti isi kotak search dengan `1220`, tekan Enter
26. Verifikasi `Code`: `1220` menemukan `Office Furniture / 1220`

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. 26 langkah.
- Pindah tab pada langkah 6, 12, 17, dan 22 adalah langkah TC. Search tiap tab disimpan terpisah selama modal terbuka (TC-FA-CAID-120), sehingga Search tab sebelumnya tidak memengaruhi tab berikutnya.
- Pembagian TC lintas spec: TC-FA-CAID-121 dan 124 ada di spec 051; TC-FA-CAID-125, 126, dan 131 ada di spec 052.
