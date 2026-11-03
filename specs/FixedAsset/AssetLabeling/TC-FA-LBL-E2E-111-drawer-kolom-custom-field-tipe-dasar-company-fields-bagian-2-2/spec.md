---
id: TC-FA-LBL-E2E-111-drawer-kolom-custom-field-tipe-dasar-company-fields-bagian-2-2
title: "Drawer Kolom Custom Field Tipe Dasar (Company Fields) (bagian 2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-579
  - TC-FA-LBL-580
coverage:
  web: automated
---

# Drawer Kolom Custom Field Tipe Dasar (Company Fields) (bagian 2/2)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Total Control `Company Fields` (Pre-setup #50), `Fixture.assetLabeling.akun.totalControlFields`, `Spectra.env.FA_TC_FIELDS_PASSWORD`. Login di hook `before` spec ini (menggantikan akun default suite); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`).
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Pre-setup `Company Fields` (#50), hanya dibaca dan dirujuk lewat `Fixture.assetLabeling.fields`: Asset Name `Field Item`; Custom Field Active grup General (Scope `Field Item`): `Field Tier` (Dropdown; opsi `Gold`, `Silver`), `Field Zones` (Multi-Dropdown; opsi `North`, `South`, `East`), `Field Install` (Date), `Field Checked` (DateTime), `Field Qty` (Numeric), `Field Price` (Currency), `Field Rate` (Percentage), `Field Note` (Text), `Field Mail` (Email), `Field Phone` (Phone); label `Field Label` pada aset Active `Field Item - 61` (Asset ID `FAS-061`; Tier `Gold`; Zones `North` dan `South`; Install 05 Jan 2026; Checked 10 Jan 2026 10:00; Qty 5; Price 100000; Rate 10; Note `Alpha Note`; Mail `a@x.com`; Phone `0811-000-061`), `Field Item - 62` (`FAS-062`; Tier `Silver`; Zones `South`; Install 20 Feb 2026; Checked 25 Feb 2026 11:00; Qty 20; Price 250000; Rate 40; Note `Beta Note`), dan `Field Item - 63` (`FAS-063`; seluruh nilai belum diisi).
- Data Dinamis: tidak ada.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.totalControlFields` (email akun Total Control `Company Fields`) dan `Fixture.assetLabeling.fields` (data Pre-setup #50).
- Kemampuan teknis (disediakan tim FE): hapus preferensi kolom Setup Column Drawer di browser (bagian 4).
- State global: konfigurasi kolom Setup Column Drawer Tagged Asset (preferensi browser) diubah dan dipulihkan oleh langkah spec; hook `after` spec ini menghapus preferensi kolom di browser sebagai cadangan, bukan `[Reset to Default]` (bagian 4). Kemampuan menghapus preferensi itu disediakan tim FE. Tidak ada state global lain yang diubah.
- Suite berjalan serial (`parallel: false`).
- Cleanup: spec tidak membuat data. Data Pre-setup hanya dibaca dan tidak diubah (Last Updated tidak berubah).
- Env var: `Spectra.env.FA_TC_FIELDS_PASSWORD`, `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`. `FA_LBL_TC_PASSWORD` dipakai hanya oleh hook `after` untuk mengembalikan sesi ke akun default suite.

## Test Steps

### TC-FA-LBL-579: Kolom Custom Field Numeric, Currency, dan Percentage di Drawer: Search Numeric, Sort numerik, dan Filter range Min-Max

1. Klik chip `Field Label` di kolom Label
2. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, centang `Field Qty`, `Field Price`, dan `Field Rate`, lalu klik `[Save]`
3. Klik icon Search di toolbar Drawer, ketik `20`, tekan Enter
4. Verifikasi hanya `Field Item - 62` tampil (Search Numeric)
5. Klik `(←)` pada kotak Search
6. Klik header kolom `Field Qty` satu kali
7. Verifikasi urutan klik 1: numerik naik `Field Item - 61` (5), `Field Item - 62` (20), `Field Item - 63` (`—`) di akhir
8. Klik header kolom `Field Qty` kedua kali
9. Verifikasi urutan klik 2: `—` di awal, lalu 20, lalu 5
10. Klik header kolom `Field Qty` ketiga kali
11. Verifikasi urutan klik 3 kembali ke default Name A-Z
12. Klik icon Filter di toolbar Drawer, isi `Field Qty` Min `1` dan Max `10`, lalu klik `[Apply]`
13. Verifikasi hanya `Field Item - 61` tampil
14. Buka panel Filter lagi, klik `[Clear Field]`, isi `Field Price` Min `200000` dan Max `300000`, lalu klik `[Apply]`
15. Verifikasi hanya `Field Item - 62` tampil
16. Buka panel Filter lagi, klik `[Clear Field]`, isi `Field Rate` Min `5` dan Max `15`, lalu klik `[Apply]`
17. Verifikasi hanya `Field Item - 61` tampil
18. Buka panel Filter lagi, klik `[Clear Field]`, lalu tutup panel Filter
19. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Field Qty`, `Field Price`, dan `Field Rate`, lalu klik `[Save]`
20. Tutup Drawer Tagged Asset

### TC-FA-LBL-580: Kolom Custom Field Text, Email, dan Phone di Drawer: dicari, tanpa field Filter

21. Klik chip `Field Label` di kolom Label
22. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, centang `Field Note`, `Field Mail`, dan `Field Phone`, lalu klik `[Save]`
23. Klik icon Search di toolbar Drawer, ketik `Alpha Note`, tekan Enter
24. Verifikasi hanya `Field Item - 61` tampil (Search `Alpha Note`)
25. Ganti isi kotak search dengan `a@x.com`, tekan Enter
26. Verifikasi hanya `Field Item - 61` tampil (Search `a@x.com`)
27. Ganti isi kotak search dengan `0811-000-061`, tekan Enter
28. Verifikasi hanya `Field Item - 61` tampil (Search `0811-000-061`)
29. Klik `(←)` pada kotak Search
30. Klik icon Filter di toolbar Drawer dan baca daftar field
31. Verifikasi Filter Panel memuat field `Field Tier` (anchor: panel sudah termuat)
32. Verifikasi Filter Panel tidak memuat field `Field Note`, `Field Mail`, maupun `Field Phone`
33. Tutup panel Filter
34. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Field Note`, `Field Mail`, dan `Field Phone`, lalu klik `[Save]`
35. Tutup Drawer Tagged Asset

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 4c (Drawer Tagged Asset). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03): `Klik (←) pada kotak Search`, `[Clear Field]` terakhir beserta tutup panel Filter, Pemulihan kolom, dan tutup Drawer memulihkan keadaan awal blok berikutnya (S-09).
- Asersi tambahan (S-03): `Verifikasi Filter Panel memuat field Field Tier` ditulis sebagai anchor positif untuk asersi absence field (bagian 8b butir 2); `Field Tier` dipilih karena TC-FA-LBL-577 menetapkan field itu ada di Filter Panel.
- Pembagian TC lintas spec: Custom Field Dropdown, Multi-Dropdown, Date, dan DateTime (TC-FA-LBL-577, 578) ada di spec 110; Custom Field Formula (TC-FA-LBL-581) di spec 178.
- Temuan untuk QA:
  - TC-FA-LBL-579 Langkah Uji 4 menyebut klik 3 Sort "kembali ke default" tanpa menyebut baris; spec memverifikasi urutan Name A-Z ketiga aset.
