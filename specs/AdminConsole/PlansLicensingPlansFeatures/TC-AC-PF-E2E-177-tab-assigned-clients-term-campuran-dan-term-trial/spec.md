---
id: TC-AC-PF-E2E-177-tab-assigned-clients-term-campuran-dan-term-trial
title: "Tab Assigned Clients: client bertermin campuran dan term Trial"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PF-640
  - TC-AC-PF-747
  - TC-AC-PF-748
coverage:
  web: automated
---

# Tab Assigned Clients: client bertermin campuran dan term Trial

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Total Control, Principal); password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip mengikuti pernyataan di `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE, sesuai `suite.md`): sesi API aktor, klien HTTP, dan fixture backend yang melakukan seeding term campuran dan term Trial serta memulihkan Dataset Plan MT dan Dataset Plan TR ke keadaan awal secara idempoten. Fixture `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis literal sesuai Pre-setup.
- Data Pre-setup (pengecualian S-06/S-12 butir A-14: nama literal tanpa suffix; seeding idempoten dan pemulihan oleh fixture backend di hook `before` dan `after`):
  - Dataset Plan MT: custom plan `Paket Term Campuran` versi terbaru v2; `PT Campur Expired`: term `Expired` v2 lalu term lebih baru `Canceled` v1; `PT Campur Live`: term `Active` v1 lalu term lebih baru `Pending` v2; `PT Campur Terminal`: term `Canceled` lalu `Converted`.
  - Assigned Date dan Assigned By Dataset Plan MT (diasersi langkah 4 dan 5; nilai disediakan tim FE karena TC-AC-PF-640 tidak memberinya): `PT Campur Expired` Assigned Date `10 Jan 26`, Assigned By `John D`; `PT Campur Live` Assigned Date `01 Feb 26`, Assigned By `John D`; `PT Campur Terminal` tidak tampil sehingga nilainya tidak diasersi.
  - Dataset Plan TR: custom plan `Paket Trial` v2; `PT Trial Aktif` term Trial Active v1; `PT Trial Habis` term Trial Expired v1; `PT Trial Menunggu` term Trial Waiting for Approval v1; `PT Paid Satu` term paid Active v1 dengan delta upgrade murni ke v2.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- State global dan pemulihan: spec hanya membaca; Last Updated dan Changelog plan tidak berubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### Client bertermin campuran (TC-AC-PF-640)

1. Klik tab `Custom`, sub-tab `Active`.
2. Klik `Paket Term Campuran`.
3. Klik Tab Assigned Clients.
4. Verifikasi baris `PT Campur Expired` | `Expired` | `v2` | `10 Jan 26` | `John D` tampil (term `Canceled` v1 yang lebih baru dilewati).
5. Verifikasi baris `PT Campur Live` | `Active` | `v1` dengan badge `Outdated` | `01 Feb 26` | `John D` tampil (term live mewakili baris walau ada term `Pending` v2 yang lebih baru).
6. Verifikasi teks footer `Showing 1–2 of 2 entries`.
7. Verifikasi tidak ada baris `PT Campur Terminal` karena seluruh term-nya terminal.
8. Klik ikon row action (⋯) baris `PT Campur Expired`.
9. Verifikasi menu row action `PT Campur Expired` hanya memuat `Detail` (tidak ada term live sebagai target Push Update).
10. Tutup menu row action (tekan Esc).
11. Klik ikon Filter.
12. Buka dropdown Subscription Status.
13. Verifikasi dropdown Subscription Status memuat opsi `Expired`.
14. Verifikasi dropdown Subscription Status tidak memuat opsi `Canceled` maupun `Converted`.
15. Tutup dropdown Subscription Status dan Filter Panel tanpa menerapkan filter.

### Kolom Clients plan Trial (TC-AC-PF-748)

16. Kembali ke Plans & Licensing > Plans & Features > Custom > Active.
17. Verifikasi kolom Clients baris `Paket Trial` bernilai `2` (`PT Trial Aktif` Active dan `PT Paid Satu` Active; `PT Trial Habis` dan `PT Trial Menunggu` tidak dihitung).

### Term Trial pada Tab Assigned Clients (TC-AC-PF-747)

18. Klik `Paket Trial`.
19. Klik Tab Assigned Clients.
20. Verifikasi baris `PT Trial Aktif` berstatus `Active`.
21. Verifikasi baris `PT Trial Habis` berstatus `Expired`.
22. Verifikasi baris `PT Trial Menunggu` berstatus `Waiting for Approval`.
23. Verifikasi baris `PT Paid Satu` berstatus `Active`.
24. Buka Overlay Row Action `PT Trial Aktif`.
25. Verifikasi Overlay Row Action `PT Trial Aktif` hanya memuat `Detail` (tanpa `Push Update`).
26. Tutup Overlay Row Action (tekan Esc).
27. Buka Overlay Row Action `PT Trial Habis`.
28. Verifikasi Overlay Row Action `PT Trial Habis` hanya memuat `Detail` (tanpa `Push Update`).
29. Tutup Overlay Row Action (tekan Esc).
30. Buka Overlay Row Action `PT Trial Menunggu`.
31. Verifikasi Overlay Row Action `PT Trial Menunggu` hanya memuat `Detail` (tanpa `Push Update`).
32. Tutup Overlay Row Action (tekan Esc).
33. Buka Overlay Row Action `PT Paid Satu`.
34. Verifikasi Overlay Row Action `PT Paid Satu` memuat `Detail` dan `Push Update`.
35. Tutup Overlay Row Action (tekan Esc).

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 10, 26, 29, 32, dan 35 (menutup row action menu), 15 (menutup dropdown dan Filter Panel), 16 (kembali ke daftar).
- Urutan TC dalam spec: TC-AC-PF-748 ditulis sebelum TC-AC-PF-747 karena TC-AC-PF-748 hanya mengamati kolom Clients pada daftar Plans List, sedangkan TC-AC-PF-747 membuka Plan Detail `Paket Trial`; dengan begitu kembali ke daftar terjadi sekali.
- Langkah 4 menjadi anchor positif bagi asersi absence baris pada langkah 7, dan langkah 13 bagi langkah 14 (bagian 8b butir 2).
- Langkah 24 sampai 35 mengulang pola buka-verifikasi-tutup untuk empat baris karena Expected TC-AC-PF-747 menuntut asersi Overlay Row Action per baris.
- TC-AC-PF-633 dan TC-AC-PF-634 (client berterm terminal) ada di spec 173.
- Temuan untuk QA:
  - TC-AC-PF-640 (Dataset Plan MT) tidak menyebut Assigned Date dan Assigned By tiap client; spec mengasersi `10 Jan 26`, `01 Feb 26`, dan `John D` pada langkah 4 dan 5 dengan nilai yang disediakan tim FE (lihat Prerequisites). Mohon QA melengkapi Dataset Plan MT di TC-AC-PF-640.
  - TC-AC-PF-747 Expected a menyebut empat baris dalam satu butir tanpa menyebut urutan baris; spec mengasersi status tiap baris tanpa urutan.
  - TC-AC-PF-747 Expected b dan c menyebut "Overlay Row Action" pada baris Trial tanpa menyatakan apakah `Detail` selalu menjadi item pertama; spec mengasersi isi menu tanpa urutan.
