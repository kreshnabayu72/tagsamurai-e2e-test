---
id: TC-FA-LBL-E2E-110-drawer-kolom-custom-field-tipe-dasar-company-fields-bagian-1-2
title: "Drawer Kolom Custom Field Tipe Dasar (Company Fields) (bagian 1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-577
  - TC-FA-LBL-578
coverage:
  web: automated
---

# Drawer Kolom Custom Field Tipe Dasar (Company Fields) (bagian 1/2)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Total Control `Company Fields` (Pre-setup #50), `Fixture.assetLabeling.akun.totalControlFields`, `Spectra.env.FA_TC_FIELDS_PASSWORD`. Login di hook `before` spec ini (menggantikan akun default suite); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`).
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Pre-setup `Company Fields` (#50), hanya dibaca dan dirujuk lewat `Fixture.assetLabeling.fields`: Asset Name `Field Item`; Custom Field Active grup General (Scope `Field Item`): `Field Tier` (Dropdown; opsi `Gold`, `Silver`), `Field Zones` (Multi-Dropdown; opsi `North`, `South`, `East`), `Field Install` (Date), `Field Checked` (DateTime), `Field Qty` (Numeric), `Field Price` (Currency), `Field Rate` (Percentage), `Field Note` (Text), `Field Mail` (Email), `Field Phone` (Phone), `Field Calc` (Formula: `Field Qty` dikali 2); label `Field Label` pada aset Active `Field Item - 61` (Asset ID `FAS-061`; Tier `Gold`; Zones `North` dan `South`; Install 05 Jan 2026; Checked 10 Jan 2026 10:00; Qty 5; Price 100000; Rate 10; Note `Alpha Note`; Mail `a@x.com`; Phone `0811-000-061`), `Field Item - 62` (`FAS-062`; Tier `Silver`; Zones `South`; Install 20 Feb 2026; Checked 25 Feb 2026 11:00; Qty 20; Price 250000; Rate 40; Note `Beta Note`), dan `Field Item - 63` (`FAS-063`; seluruh nilai belum diisi).
- Data Dinamis: tidak ada.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.totalControlFields` (email akun Total Control `Company Fields`) dan `Fixture.assetLabeling.fields` (data Pre-setup #50).
- Kemampuan teknis (disediakan tim FE): hapus preferensi kolom Setup Column Drawer di browser (bagian 4).
- State global: konfigurasi kolom Setup Column Drawer Tagged Asset (preferensi browser) diubah dan dipulihkan oleh langkah spec; hook `after` spec ini menghapus preferensi kolom di browser sebagai cadangan, bukan `[Reset to Default]` (bagian 4). Kemampuan menghapus preferensi itu disediakan tim FE. Tidak ada state global lain yang diubah.
- Suite berjalan serial (`parallel: false`).
- Cleanup: spec tidak membuat data. Data Pre-setup hanya dibaca dan tidak diubah (Last Updated tidak berubah).
- Env var: `Spectra.env.FA_TC_FIELDS_PASSWORD`, `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`. `FA_LBL_TC_PASSWORD` dipakai hanya oleh hook `after` untuk mengembalikan sesi ke akun default suite.

## Test Steps

### TC-FA-LBL-577: Kolom Custom Field Dropdown dan Multi-Dropdown di Drawer: Search nilai, Sort A-Z, dan Filter multi-select OR

1. Klik chip `Field Label` di kolom Label
2. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, centang `Field Tier` dan `Field Zones`, lalu klik `[Save]`
3. Klik icon Search di toolbar Drawer, ketik `Gold`, tekan Enter
4. Verifikasi hanya `Field Item - 61` tampil
5. Ganti isi kotak search dengan `South`, tekan Enter
6. Verifikasi `Field Item - 61` (North dan South) dan `Field Item - 62` (South) tampil
7. Klik `(←)` pada kotak Search
8. Klik header kolom `Field Tier` satu kali
9. Verifikasi urutan klik 1: A-Z `Gold` (`Field Item - 61`), `Silver` (`Field Item - 62`), `—` (`Field Item - 63`) di akhir
10. Klik header kolom `Field Tier` kedua kali
11. Verifikasi urutan klik 2: `—` di awal, lalu `Silver`, `Gold`
12. Klik header kolom `Field Tier` ketiga kali
13. Verifikasi urutan klik 3 kembali ke default Name A-Z
14. Klik icon Filter di toolbar Drawer, lalu buka dropdown `Field Tier`
15. Verifikasi dropdown `Field Tier` memuat opsi `Gold` dan `Silver`
16. Pilih `Silver`, lalu klik `[Apply]`
17. Verifikasi hanya `Field Item - 62` tampil
18. Buka panel Filter lagi, klik `[Clear Field]`, pilih `Field Zones` = `North`, lalu klik `[Apply]`
19. Verifikasi hanya `Field Item - 61` tampil
20. Buka panel Filter lagi, klik `[Clear Field]`, pilih `Field Zones` = `North` dan `South`, lalu klik `[Apply]`
21. Verifikasi `Field Item - 61` dan `Field Item - 62` tampil (OR)
22. Buka panel Filter lagi, klik `[Clear Field]`, lalu tutup panel Filter
23. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Field Tier` dan `Field Zones`, lalu klik `[Save]`
24. Tutup Drawer Tagged Asset

### TC-FA-LBL-578: Kolom Custom Field Date dan DateTime di Drawer: tidak dicari, Sort tanggal, dan Filter date range

25. Klik chip `Field Label` di kolom Label
26. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, centang `Field Install` dan `Field Checked`, lalu klik `[Save]`
27. Klik icon Search di toolbar Drawer, ketik `20 Feb 2026`, tekan Enter
28. Verifikasi empty state `No results found` untuk Search `20 Feb 2026` (Date)
29. Ganti isi kotak search dengan `25 Feb 2026`, tekan Enter
30. Verifikasi empty state `No results found` untuk Search `25 Feb 2026` (DateTime)
31. Klik `(←)` pada kotak Search
32. Klik header kolom `Field Install` satu kali
33. Verifikasi urutan klik 1: Oldest First `Field Item - 61` (05 Jan 2026), `Field Item - 62` (20 Feb 2026), `Field Item - 63` (`—`) di akhir
34. Klik header kolom `Field Install` kedua kali
35. Verifikasi urutan klik 2: Newest First `—` di awal, lalu `Field Item - 62`, `Field Item - 61`
36. Klik header kolom `Field Install` ketiga kali
37. Verifikasi urutan klik 3 kembali ke default Name A-Z
38. Klik icon Filter di toolbar Drawer, pilih rentang `Field Install` `01 Feb 2026` sampai `28 Feb 2026`, lalu klik `[Apply]`
39. Verifikasi hanya `Field Item - 62` tampil
40. Buka panel Filter lagi, klik `[Clear Field]`, pilih rentang `Field Checked` `01 Jan 2026` sampai `15 Jan 2026`, lalu klik `[Apply]`
41. Verifikasi hanya `Field Item - 61` (10 Jan 2026 10:00) tampil
42. Buka panel Filter lagi, klik `[Clear Field]`, lalu tutup panel Filter
43. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Field Install` dan `Field Checked`, lalu klik `[Save]`
44. Tutup Drawer Tagged Asset

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 4c (Drawer Tagged Asset). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03): `Klik (←) pada kotak Search`, `[Clear Field]` terakhir beserta tutup panel Filter, langkah Pemulihan kolom, dan tutup Drawer memulihkan keadaan awal blok berikutnya (S-09).
- Pembagian TC lintas spec: Custom Field tipe dasar lain (TC-FA-LBL-579 dan 580 di spec 111, TC-FA-LBL-581 di spec 178); semua memakai akun dan data Pre-setup #50 yang sama.
- Ukuran spec (44 langkah, di atas smell 35 langkah): kedua TC satu kelas (fungsional, Search, Sort, dan Filter kolom Custom Field Drawer) pada akun dan data Pre-setup #50 yang sama dan tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah membengkak karena Sort tiga klik dengan satu `Verifikasi` per klik dan tiap klausa Expected menjadi satu `Verifikasi` (S-01).
- Temuan untuk QA:
  - TC-FA-LBL-577 Langkah Uji 5 menyebut klik 3 Sort "kembali ke default Name A-Z" tanpa menyebut baris yang diharapkan; spec memverifikasi urutan Name A-Z ketiga aset `Field Label`.
  - TC-FA-LBL-577 Expected d dan TC-FA-LBL-578 Expected d menyebut `Field Item - 61` dan `Field Item - 62` tampil/tersaring tanpa menyebut baris `Field Item - 63`; spec memakai kuantor "hanya" yang tertulis di TC.
