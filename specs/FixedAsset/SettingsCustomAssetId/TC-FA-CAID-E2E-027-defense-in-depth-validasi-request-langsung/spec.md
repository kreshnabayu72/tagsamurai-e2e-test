---
id: TC-FA-CAID-E2E-027-defense-in-depth-validasi-request-langsung
title: "Defense-in-Depth: Request Save Langsung dengan Segmen Kosong, Tanpa Increment, Tanpa Separator, dan Initial Company Kosong"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAID-306
  - TC-FA-CAID-307
  - TC-FA-CAID-308
  - TC-FA-CAID-309
coverage:
  web: automated
---

# Defense-in-Depth: Request Save Langsung dengan Segmen Kosong, Tanpa Increment, Tanpa Separator, dan Initial Company Kosong

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control Company Alpha (Pre-setup No 1, `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`); halaman Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip disetel seen untuk akun UI suite; konfigurasi Company Alpha dipulihkan ke baseline B1 dan aset A1 sampai A5 (Pre-setup No 11) ke kondisi awal di `beforeEach` dan `after` lewat sesi API aktor (klien HTTP dan token sesi API disediakan tim FE; token tidak dihitung sebagai sesi web).
- Data Pre-setup No 10: baseline B1 (Master Switch ON, Separator `/ (Slash)`, segmen tercentang Group Code, Category Code, Asset Name Code, Purchase Date, Asset Increment, tanpa Initial Company). Data Pre-setup No 11: A1 Active `JKT/LAP/T490/0926/1`, A2 Draft `JKT/LAP/T490/0926/2`, A3 Waiting for Approval `JKT/LAP/T490/0000/3`, A4 Disposed `JKT/LAP/T490/0926/4`, A5 Deleted. Nilai dibaca dari `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE): penyunting request dan respons pada sesi otomasi (Pre-setup No 26) untuk mengubah payload request Save yang dikirim dari browser (langkah 2, 13, 20, dan 27) dan mengamati respons server; konfirmasi otomatis dialog `beforeunload` bawaan browser oleh harness untuk muat ulang pada form yang belum disimpan (langkah 7, 17, 23, dan 30).
- State: tidak ada perubahan tersimpan yang diharapkan; semua request ditolak server. Hook `after` suite memulihkan baseline.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-306: Request Save dengan daftar segmen kosong ditolak dan alert D-03 tampil

1. Pilih Separator `- (Dash)`
2. Ubah payload request Save lewat penyunting sehingga daftar segmen kosong
3. Klik `[Save]`
4. Verifikasi alert inline severity danger tampil tepat di atas `[Save]` berbunyi `Select at least one segment`
5. Verifikasi form tetap terbuka dan input dipertahankan
6. Verifikasi tidak ada toast terpisah
7. Muat ulang halaman
8. Verifikasi konfigurasi tersimpan tidak berubah: Separator `/ (Slash)`
9. Buka Fixed Asset > Assets > All Assets
10. Verifikasi Asset ID A1 sampai A4 tidak berubah
11. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID

### TC-FA-CAID-307: Request Save tanpa segmen Asset Increment ditolak dengan alert D-03

12. Pilih Separator `- (Dash)`
13. Ubah payload request Save lewat penyunting sehingga daftar segmen hanya memuat `Group Code` dan `Category Code` tanpa `Asset Increment`
14. Klik `[Save]`
15. Verifikasi alert inline di atas `[Save]` berbunyi `Select at least one segment`
16. Verifikasi form tetap terbuka
17. Muat ulang halaman
18. Verifikasi konfigurasi tersimpan tidak berubah: Separator `/ (Slash)`

### TC-FA-CAID-308: Request Save tanpa Separator ditolak server dengan pesan V-04

19. Centang `Initial Company` dan ketik `ABC` pada input Initial Company
20. Ubah payload request Save lewat penyunting sehingga Separator kosong
21. Klik `[Save]`
22. Verifikasi server menolak request dengan pesan `Separator must not be empty`
23. Muat ulang halaman
24. Verifikasi konfigurasi tersimpan tidak berubah: Separator `/ (Slash)`
25. Verifikasi checkbox `Initial Company` tidak tercentang

### TC-FA-CAID-309: Request Save dengan Initial Company dicentang tanpa nilai ditolak server

26. Pilih Separator `- (Dash)`
27. Ubah payload request Save lewat penyunting sehingga entry Initial Company dicentang dengan nilai kosong
28. Klik `[Save]`
29. Verifikasi server menolak request dengan pesan `Initial company must not be empty`
30. Muat ulang halaman
31. Verifikasi konfigurasi tersimpan tidak berubah: Separator `/ (Slash)`
32. Verifikasi checkbox `Initial Company` tidak tercentang

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- `K-1`: spec defense-in-depth dengan Expected respons API tetap FE+BE walau tumpang tindih dengan `tc-settings-custom-asset-id-backend.md`; TC granular tetap sumber dan BE mencatatnya pada tingkat endpoint.
- Request dikirim dari browser dengan payload yang diubah penyunting (pemicu kelas a), sehingga alert D-03 pada TC-FA-CAID-306 dan TC-FA-CAID-307 adalah perilaku FE atas respons server dan diasersi sesuai Expected TC.
- Langkah penghubung (tanpa `Verifikasi`): langkah 9 dan 11 (membuka layar pembaca state dan kembali ke tab Custom Asset ID). Muat ulang pada langkah 7, 17, 23, dan 30 terjadi pada form yang masih dirty; konfirmasi `beforeunload` ditangani harness sesuai Prerequisites, sehingga form berakhir pristine pada nilai tersimpan.
- Absence toast pada langkah 6 memakai alert langkah 4 sebagai anchor positif pada surface yang sama.
- Pembagian TC lintas spec: TC-FA-CAID-306 sampai 309 juga ada di spec 099 (asersi absence entri log atas request yang sama, S-05); spec ini mengasersi alert D-03, pesan penolakan server, dan state konfigurasi.
- Temuan untuk QA:
  - Expected TC-FA-CAID-306 b, TC-FA-CAID-307 b, TC-FA-CAID-308 b, dan TC-FA-CAID-309 b memuat "tidak ada entri log baru" pada tiga surface dan "tidak ada mass update". Asersi absence log atas request yang ditolak tidak ditulis di spec kelas a ini (S-05); asersi itu ada di spec absence 099 yang memuat TC-FA-CAID-306 sampai 309 dengan request ini sebagai pemicu dan baseline sendiri. "Tidak ada mass update" tidak punya langkah observasi di TC dan tidak diasersi.
  - TC-FA-CAID-308 a dan TC-FA-CAID-309 a menyebut "Server menolak request dengan pesan ..." tanpa menyebut tempat pesan tampil di UI; spec mengasersi isi respons server yang diamati lewat penyunting respons (kemampuan disediakan tim FE).
  - TC-FA-CAID-306 a menyebut "input dipertahankan" tanpa menyebut nilai input mana; spec mengasersi form tetap terbuka dengan input yang dipilih langkah 1 dipertahankan (Separator `- (Dash)`).
  - Pemicu TC-FA-CAID-308 ("Ubah Initial Company menjadi tercentang bernilai `ABC` agar `[Save]` aktif") ditulis sebagai langkah 19 mengikuti Langkah Uji.
