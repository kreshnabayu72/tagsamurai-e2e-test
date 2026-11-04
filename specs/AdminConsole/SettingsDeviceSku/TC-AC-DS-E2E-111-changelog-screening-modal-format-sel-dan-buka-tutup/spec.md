---
id: TC-AC-DS-E2E-111-changelog-screening-modal-format-sel-dan-buka-tutup
title: "Modal Changelog: Screening, Buka dan Tutup, serta Format Sel Date, Action, SKU, Old Value, dan New Value"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-380
  - TC-AC-DS-381
  - TC-AC-DS-382
coverage:
  web: automated
---

# Modal Changelog: Screening, Buka dan Tutup, serta Format Sel Date, Action, SKU, Old Value, dan New Value

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima, `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca, tidak diubah): #29 (SKU Principal inti) dan #30 (`SEED-001` sampai `SEED-119`; total 129 SKU Principal), dipasang idempoten oleh seeding di hook `before`. Riwayat Changelog Principal (#33): seed 35 entri bertanggal 01/09/26 sampai 03/10/26, termasuk Delete `UHF Handheld Reader (HHR-ARC-300)` pada 03/10/26 14:20 oleh `Jane S`, Create `BLE-KIN-GW1`, dan Edit `HHR-ARC-200`; total pada modal dapat lebih besar karena entri yang ditulis spec lain, sehingga spec ini tidak memakai jumlah absolut: jumlah halaman dibandingkan dengan N yang dibaca dari info pagination pada langkah yang sama, dan baris seed dicari lewat Search (kemampuan baca N disediakan tim FE/BE).
- Konfigurasi General Settings (Pre-setup #35): Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone Asia/Jakarta; hanya dibaca, tidak diubah.
- Nilai data diacu lewat `Fixture.deviceSku.<kunci>`; berkas fixture disediakan tim FE.
- Tidak ada state global yang diubah dan tidak ada entitas yang dibuat.

## Test Steps

### TC-AC-DS-380: Screening modal Changelog

1. Klik ikon Changelog
2. Verifikasi Header: judul "Changelog: Device SKU" dan ikon close `[✕]`
3. Verifikasi Header: Table Tools modal `Search | Filter | Download`
4. Verifikasi Body: kolom `Date (sortable) | Action (sortable) | SKU (sortable) | Field (sortable) | Old Value (sortable) | New Value (sortable) | Modified By (sortable) | Column Visibility (⋯) (unsortable)`
5. Verifikasi Body: baris pertama berurut Newest First, yaitu Date baris pertama tidak lebih lama daripada Date baris kedua
6. Klik ikon Search pada modal
7. Verifikasi Body: placeholder kotak Search "Search action, SKU..."
8. Verifikasi Footer: Pagination default 10 baris per halaman dan jumlah halaman sama dengan pembulatan ke atas N/10, dengan N total entri pada info pagination

### TC-AC-DS-381: Buka dan tutup modal Changelog

9. Klik ikon close `[✕]` pada modal
10. Hover ikon Changelog
11. Verifikasi tooltip `Changelog` tampil
12. Klik ikon Changelog
13. Klik area backdrop di luar modal
14. Verifikasi modal tidak tertutup
15. Verifikasi tidak ada tombol teks "Close" pada modal
16. Klik ikon close `[✕]`
17. Verifikasi modal tertutup dan List kembali terlihat
18. Klik ikon Changelog
19. Tekan Esc
20. Verifikasi modal tertutup dan List kembali terlihat

### TC-AC-DS-382: Format sel modal Changelog

21. Klik ikon Changelog
22. Ketik Search pada modal `HHR-ARC-300`, tekan Enter
23. Verifikasi Date baris Delete `HHR-ARC-300` mengikuti General Settings: `03/10/26 14:20`
24. Verifikasi Action `Delete` tampil sebagai teks biasa, bukan badge
25. Verifikasi SKU tampil sebagai teks biasa (bukan tautan) berformat `Device Name (kode SKU)`: `UHF Handheld Reader (HHR-ARC-300)`
26. Verifikasi baris Delete: Old Value `UHF Handheld Reader (HHR-ARC-300)` dan New Value `—`
27. Ganti isi kotak search modal dengan `BLE-KIN-GW1`, tekan Enter
28. Verifikasi Action `Create` tampil sebagai teks biasa, bukan badge
29. Verifikasi baris Create `BLE-KIN-GW1`: Old Value `—` dan New Value `BLE Gateway (BLE-KIN-GW1)`
30. Ganti isi kotak search modal dengan `HHR-ARC-200`, tekan Enter
31. Verifikasi Action `Edit` tampil sebagai teks biasa, bukan badge
32. Verifikasi baris Edit SKU `HHR-ARC-200`: Old Value `UHF Handheld Reader (HHR-ARC-20)` dan New Value `UHF Handheld Reader (HHR-ARC-200)`
33. Verifikasi kolom SKU pada baris itu memuat pasangan baru `UHF Handheld Reader (HHR-ARC-200)`
34. Klik ikon close `[✕]`

## Notes

- Langkah penghubung (S-03, R-16, S-14): langkah 6 membuka kotak Search agar placeholder teramati (TC-AC-DS-380 tidak memuat langkah ini); langkah 9 menutup modal agar TC-AC-DS-381 mulai dari List; langkah 22, 27, dan 30 mencari baris Delete `HHR-ARC-300`, Create `BLE-KIN-GW1`, dan Edit `HHR-ARC-200` yang tidak dijamin berada di 10 entri pertama; langkah 34 menutup modal; tanpa asersi tambahan.
- Temuan untuk QA:
  - S-12: asersi bergantung pada nama literal Pre-setup #29, #30, dan #33 (pengecualian S-12 A-11, `suite.md`); jumlah entri tidak absolut (Pre-setup #33 dan TC-AC-DS-380 memakai N dari info pagination).
  - TC-AC-DS-382 menyebut baris Create `BLE-KIN-GW1` dan Edit `HHR-ARC-200` tanpa menyebut halamannya, dan baris Delete `HHR-ARC-300` tidak lagi dijamin sebagai baris pertama; spec mencarinya lewat Search modal (langkah 22, 27, dan 30).
  - Env `AC_DS_TC_PASSWORD` dan berkas fixture `Fixture.deviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE. Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag-nya belum ditetapkan.
