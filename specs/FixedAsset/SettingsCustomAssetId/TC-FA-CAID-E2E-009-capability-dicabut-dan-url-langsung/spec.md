---
id: TC-FA-CAID-E2E-009-capability-dicabut-dan-url-langsung
title: "Capability Dicabut Saat Tab Terbuka dan URL Langsung Tanpa Akses"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAID-39
  - TC-FA-CAID-40
  - TC-FA-CAID-41
  - TC-FA-CAID-42
coverage:
  web: automated
---

# Capability Dicabut Saat Tab Terbuka dan URL Langsung Tanpa Akses

## Prerequisites

- Mode: FE+BE.
- Login akun aktor pertama (Config-Update) di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka hook `beforeEach` suite untuk akun itu. Akun lain login lewat langkah ganti akun eksplisit.
- Role yang diuji (Company Alpha; email `<prefix>_automated_{namaCompany}@qwertysystem.net`, password dari env, tidak ditulis di spec atau fixture):

| Blok | TC | Role | Pre-setup | Prefix email | Env password |
|---|---|---|---|---|---|
| 1 | TC-FA-CAID-39, 40 | Config-Update (Manage asset ID configuration dengan Read dan Update) | No 3 | `configUpdate` | `Spectra.env.FA_CFGUPD_PASSWORD` |
| 2 | TC-FA-CAID-41 | Config-And-Master (Manage asset ID configuration dengan Update dan Manage asset master data) | No 6 | `configAndMaster` | `Spectra.env.FA_CFGMASTER_PASSWORD` |
| 3 | TC-FA-CAID-42 | Master-Data-Only (Manage asset master data tanpa Manage asset ID configuration) | No 5 | `masterDataOnly` | `Spectra.env.FA_MDONLY_PASSWORD` |

  Nama env password adalah usulan di `suite.md` dan perlu konfirmasi tim FE. Hook `after` spec ini mengembalikan sesi ke akun default suite (Total Control Company Alpha).
- Hook suite (`suite.md`): flag Guided Tooltip disetel seen untuk semua akun UI suite; konfigurasi Company Alpha dipulihkan ke baseline B1 di `beforeEach` lewat sesi API Total Control Company Alpha.
- Data Pre-setup No 10: baseline B1 (Master Switch ON, Separator `/ (Slash)`, segmen tercentang Group Code, Category Code, Asset Name Code, Purchase Date, Asset Increment, tanpa Initial Company). URL tab Custom Asset ID dibaca dari `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Kemampuan teknis: pencabutan dan pemulihan capability Update (Config-Update) dan role Manage asset ID configuration (Config-And-Master) lewat sesi API Total Control Company Alpha, setelah halaman dibuka (disediakan tim FE; mekanisme tidak tertulis di TC, PRD, atau LLD, S-13). Pelaku pencabutan memakai sesi API sehingga bukan konteks kedua; sesi UI akun uji tidak diusir.
- State global: capability Config-Update dan role Config-And-Master; dipulihkan di langkah 8, 16, 25 dan oleh hook `after` spec ini walau spec gagal di tengah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-39: Capability Update dicabut saat form terbuka: Save ditolak (blok 1)

1. Cabut capability Update akun Config-Update lewat sesi API Total Control hingga perubahan tersimpan
2. Pilih Separator `. (Dot)`
3. Klik `[Save]`
4. Verifikasi toast error `You don't have permission to do this.` tampil
5. Verifikasi kontrol mutasi berstatus Disabled 🔖 setelah UI di-refresh
6. Verifikasi tombol `[Save]` tidak tampil (Hidden)
7. Verifikasi Separator menampilkan `/ (Slash)` sehingga konfigurasi tersimpan tidak berubah
8. Pulihkan capability Update akun Config-Update lewat sesi API hingga perubahan tersimpan, lalu muat ulang halaman (F5)

### TC-FA-CAID-40: Capability Update dicabut saat form terbuka: Toggle ditolak (blok 1)

9. Cabut capability Update akun Config-Update lewat sesi API Total Control hingga perubahan tersimpan
10. Geser Master Switch ke OFF
11. Klik `[Disable]` pada dialog `Disable Custom Asset ID`
12. Verifikasi toast error `You don't have permission to do this.` tampil
13. Verifikasi Master Switch kembali ke posisi ON
14. Verifikasi UI di-refresh ke tampilan Read Only dengan kontrol mutasi Disabled 🔖
15. Verifikasi Master Switch tetap ON sesudah UI di-refresh sehingga status Master Switch tersimpan tidak berubah
16. Pulihkan capability Update akun Config-Update lewat sesi API hingga perubahan tersimpan

### TC-FA-CAID-41: Seluruh capability Custom Asset ID dicabut saat tab terbuka (blok 2)

17. Ganti akun: logout akun Config-Update, lalu login sebagai Config-And-Master (Pre-setup No 6)
18. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID
19. Cabut role Manage asset ID configuration akun Config-And-Master lewat sesi API Total Control hingga perubahan tersimpan; role Manage asset master data tetap
20. Pilih Separator `_ (Underscore)`
21. Klik `[Save]`
22. Verifikasi toast error `You don't have permission to do this.` tampil
23. Verifikasi tab `Custom Asset ID` hilang dari Tabs Bar (Hidden total)
24. Verifikasi pengguna dialihkan ke tab default `Asset Name`
25. Pulihkan role Manage asset ID configuration akun Config-And-Master lewat sesi API hingga perubahan tersimpan
26. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID
27. Verifikasi Separator menampilkan `/ (Slash)` sehingga konfigurasi tidak berubah

### TC-FA-CAID-42: URL tab Custom Asset ID dibuka langsung tanpa akses tab (blok 3)

28. Ganti akun: logout akun Config-And-Master, lalu login sebagai Master-Data-Only (Pre-setup No 5)
29. Ketik URL tab Custom Asset ID langsung di address bar, lalu tekan Enter
30. Verifikasi pengguna dialihkan ke tab default `Asset Name` yang aktif
31. Verifikasi konten tab `Custom Asset ID` tidak ditampilkan (kartu `Custom Asset ID Configuration` tidak ada)
32. Verifikasi Tabs Bar memuat `Asset Name` dan `Labels` saja

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular. Langkah pembuka TC-FA-CAID-39 dan 40 (halaman terbuka) dipenuhi hook `beforeEach` suite. Spec ditulis per blok role karena ganti akun menuntut langkah eksplisit (langkah 17 dan 28).
- Langkah penghubung (tanpa `Verifikasi`): langkah 1, 9, 19 (pencabutan sebagai pemicu lewat sesi API), langkah 2, 3, 10, 11, 20, 21, 29 (aksi TC), langkah 8, 16, 25 (memulihkan capability atau role lewat sesi API; langkah 8 diikuti muat ulang agar form kembali ke state Update), langkah 17, 18, 26, 28 (ganti akun dan membuka halaman).
- Urutan langkah Expected TC-FA-CAID-39 a dan b mengikuti urutan state: konfigurasi tersimpan diamati sesudah UI di-refresh (langkah 7), karena Separator tersimpan hanya terlihat pada form sesudah refresh. Hal yang sama berlaku untuk langkah 15 (TC-FA-CAID-40) dan langkah 27 (TC-FA-CAID-41; konfigurasi diamati sesudah role dipulihkan karena tab Custom Asset ID Hidden saat role dicabut, langkah asersi tambahan di luar urutan TC dan dipakai untuk Expected "konfigurasi tidak berubah").
- Pecahan Expected TC-FA-CAID-40 a: "Master Switch kembali ke ON" (langkah 13) dan "status tersimpan tidak berubah" (langkah 15) masing-masing klausa sendiri.
- Asersi absence langkah 31 (TC-FA-CAID-42) didahului anchor positif tab `Asset Name` aktif (langkah 30).
- Temuan untuk QA:
  - Mekanisme pencabutan capability atau role lewat seed API tidak tertulis di TC, PRD, atau LLD (TC menyebut "lewat seed API"); disediakan tim FE.
  - TC-FA-CAID-41 menyebut "konfigurasi tidak berubah" tanpa cara mengamatinya saat tab Hidden; spec mengamatinya sesudah role dipulihkan (langkah 25 sampai 27).
  - TC-FA-CAID-42 menyebut "URL tab Custom Asset ID diketahui" tanpa nilai URL; nilai dibaca dari fixture yang belum ada.
  - Email akun Pre-setup No 3, 5, 6 hanya tertulis sebagai pola `{namaCompany}`; env var password adalah usulan.
  - Post Condition TC-FA-CAID-39 sampai 42 kosong; tidak ada yang diasersi.
