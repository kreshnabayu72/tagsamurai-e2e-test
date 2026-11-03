---
id: TC-AC-DS-E2E-157-sinkron-master-rename-dan-time-zone
title: "Sinkron Master Data: Rename Device Name, Brand, Category dan Perubahan Time Zone General Settings"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-504
  - TC-AC-DS-505
  - TC-AC-DS-506
  - TC-AC-DS-507
coverage:
  web: automated
---

# Sinkron Master Data: Rename Device Name, Brand, Category dan Perubahan Time Zone General Settings

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`): `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca kecuali disebut lain): pohon Category (#25), Device Name (#26), Brand Principal (#27), SKU inti dan seed (#29, #30), file foto (#37). Konfigurasi General Settings (#35). Modul stok (#39): Hardware Stock dan TAG Stock (Add Stock dan Stock List) pada Principal PT Arunika Prima tersedia.
- State global: nama master diubah dan dipulihkan: Device Name `Wearable TAG` (modul Device Name), Brand `Kinetia` (Global Settings > Brand), Category `Asset TAG` (Settings > Device > Category), Time Zone General Settings entitas uji dari Asia/Jakarta (UTC+07:00) ke opsi pertama selain Asia/Jakarta (offset O; dropdown Time Zone memuat sedikitnya satu opsi selain Asia/Jakarta, general-settings.md §4.3a hanya menjamin `Asia/Jakarta`). Pemulihan nama dilakukan sebagai langkah penghubung per blok dan di hook `after` (seeding dan cleanup deterministik). Suite berjalan serial (`parallel: false`).
- Data Dinamis: tidak ada.
- Nilai data dibaca dari `Fixture.settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).

## Test Steps

### TC-AC-DS-504: Rename Device Name pada master tampil pada baris dan Info Grid Detail

1. Pada modul Device Name ubah nama `Wearable TAG` menjadi `Wearable TAG Pro`
2. Kembali ke List Device SKU lalu muat ulang halaman
3. Ketik Search `TAG-ARC-USR`, tekan Enter
4. Verifikasi baris `TAG-ARC-USR` menampilkan Device Name `Wearable TAG Pro`
5. Klik SKU `TAG-ARC-USR`
6. Verifikasi Info Grid Popup Detail menampilkan Device Name `Wearable TAG Pro`
7. Tutup Popup Detail lalu klik ikon Filter dan klik field Device Name
8. Verifikasi opsi filter Device Name memuat `Wearable TAG Pro`
9. Verifikasi opsi filter Device Name tidak memuat opsi `Wearable TAG`
10. Tutup Filter Panel, klik `(←)` pada kotak Search, lalu pulihkan nama Device Name menjadi `Wearable TAG`

### TC-AC-DS-505: Rename Brand pada master Global Settings tampil pada kolom Brand dan opsi

11. Pada Global Settings > Brand ubah nama `Kinetia` menjadi `Kinetia Pro`
12. Kembali ke List Device SKU lalu muat ulang halaman
13. Ketik Search `BLE-KIN-GW1`, tekan Enter
14. Verifikasi baris `BLE-KIN-GW1` menampilkan badge Brand `Kinetia Pro`
15. Buka Filter Panel lalu klik field Brand
16. Verifikasi opsi filter Brand memuat `Kinetia Pro`
17. Tutup Filter Panel lalu klik tombol `[+ SKU]` dan klik dropdown Brand
18. Verifikasi dropdown Brand pada Popup Register SKU memuat `Kinetia Pro`
19. Tutup Popup Register dengan `[✕]`, klik `(←)` pada kotak Search, lalu pulihkan nama Brand menjadi `Kinetia`

### TC-AC-DS-506: Rename Category pada master tampil pada badge Category dan Sidebar

20. Pada Settings > Device > Category ubah nama `Asset TAG` menjadi `Asset TAG Pro`
21. Kembali ke List Device SKU lalu muat ulang halaman
22. Ketik Search `TAG-ARC-OBJ`, tekan Enter
23. Verifikasi baris `TAG-ARC-OBJ` menampilkan badge Category `Asset TAG Pro`
24. Verifikasi Sidebar Category menampilkan node `Asset TAG Pro`
25. Klik `(←)` pada kotak Search lalu pulihkan nama Category menjadi `Asset TAG`

### TC-AC-DS-507: Perubahan Time Zone General Settings menggeser tampilan Last Modified dan Date Changelog

26. Ketik Search `HHR-ARC-100`, tekan Enter
27. Catat Last Modified `HHR-ARC-100` sebagai T1
28. Klik ikon Changelog lalu catat Date entri pertama Changelog sebagai C1, lalu tutup modal
29. Buka General Settings, buka dropdown Time Zone, pilih opsi pertama pada daftar yang bukan opsi `Asia/Jakarta`, catat offset `(UTC±HH:MM)` pada labelnya sebagai offset O, lalu simpan
30. Muat ulang halaman Device SKU, ketik Search `HHR-ARC-100`, tekan Enter
31. Verifikasi Last Modified `HHR-ARC-100` menampilkan instan yang sama dengan T1 pada offset O: T1 ditambah selisih (O dikurangi UTC+07:00)
32. Klik ikon Changelog
33. Verifikasi Date entri pertama Changelog sama dengan C1 ditambah selisih yang sama
34. Verifikasi format tanggal tetap `dd/MM/yy` dan 24 jam
35. Tutup modal Changelog lalu pulihkan Time Zone General Settings menjadi Asia/Jakarta

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 35, 19, dan 25 (membersihkan Search/Filter/popup dan memulihkan nama master agar blok berikutnya tidak bergantung pada state sebelumnya, S-09), langkah Search untuk menemukan baris target (R-16), serta langkah 7 dan 15 (membuka Filter Panel dan field untuk membaca opsi, lihat Temuan).
- Last Modified `HHR-ARC-100` (T1, langkah 27) dan Date entri pertama Changelog (C1, langkah 28) dibaca saat run, bukan literal Pre-setup, karena nilai Last Modified Pre-setup bergantung pada pemulihan fixture BE antar spec (A-11); asersi memakai selisih offset (TC 507 Expected butir a).
- Expected 504 butir c dipecah menjadi memuat `Wearable TAG Pro` dan tidak memuat `Wearable TAG` (opsi yang sama persis; `Wearable TAG Pro` bukan padanan opsi `Wearable TAG`); anchor absence: opsi `Wearable TAG Pro` pada daftar opsi yang sama. Expected 505 butir b dipecah per surface (opsi filter, dropdown form).
- Pengecualian S-12 A-11: SKU Pre-setup `TAG-ARC-USR`, `BLE-KIN-GW1`, `TAG-ARC-OBJ`, dan `HHR-ARC-100` serta nama master `Wearable TAG` (Device Name), `Kinetia` (Brand), dan `Asset TAG` (Category) bernama literal tanpa suffix; nama master yang di-rename dipulihkan sebagai langkah penghubung per blok dan di hook `after`, dan pemulihan Pre-setup dijamin fixture BE (dinyatakan di `suite.md`).
- Temuan untuk QA:
  - TC 504 langkah 3 dan 4 serta TC 505 langkah 4 tidak menyebut pembukaan Filter Panel untuk Expected tentang opsi filter; spec menambah langkah penghubung membuka Filter Panel (S-14).
  - Langkah rename di modul Device Name, Brand, dan Category dimiliki modul lain; spec menulis tindakan rename saja tanpa rincian UI modul itu (TC tidak merincinya).
  - S-11/S-13: `Fixture.settingsDeviceSku`, 23 env var `AC_DS_*` (termasuk yang dipakai spec ini), dan fixture rancangan Pre-setup yang dirujuk belum terverifikasi ada di environment atau belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar belum dinyatakan di `suite.md` (disediakan tim FE).
