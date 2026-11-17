---
id: TC-FA-FAAC-E2E-182-resilience-baca-dan-download
title: "Resilience: Kegagalan Server saat Memuat Tabel, Alert Dependensi Akun, Banner, Dialog D-23, dan Download"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAC-8
  - TC-FA-FAAC-32
  - TC-FA-FAAC-280
  - TC-FA-FAAC-281
  - TC-FA-FAAC-426
sourceRules: ["ST-22", "R-18", "R-14", "§4.1.9#p1", "T-12", "R-15"]
smoke: []
dependsOn: []
trace:
  "ST-22": [4, 7, 16]
  "R-18": [11, 12]
  "R-14": [16, 23, 24]
  "§4.1.9#p1": 17
  "T-12": 27
  "R-15": 27
coverage:
  web: automated
---

# Resilience: Kegagalan Server saat Memuat Tabel, Alert Dependensi Akun, Banner, Dialog D-23, dan Download

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata)
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Kemampuan teknis: `Spectra.intercept` parsial yang memaksa respons HTTP 5xx pada permintaan tertentu (data tabel Asset Class, pembacaan akun Chart of Accounts untuk Alert dependensi akun, pemuatan daftar dialog D-23, pembacaan jumlah banner, permintaan Download) di atas backend nyata; intercept dilepas segera setelah pemicu selesai diamati (S-09). Endpoint tiap permintaan tidak didefinisikan di TC, PRD, atau LLD yang dibaca, sehingga dipilih tim FE saat script.
- Data Pre-setup dibaca, tidak diubah (kecuali keadaan awal dinamis di butir berikutnya): sembilan Asset Class contoh (Tabel Data Uji Pre-setup, nilai mengikuti Example Data PRD §4.1.1): `HEAVY-EQ`, `VEHICLES`, `IT-EQ`, `MACHINERY`, `BLDG`, `STORAGE`, `OFFICE-NEW`, `LAND` (Active) dan `OFFICE-OLD` (Inactive); tepat tiga Asset Name tanpa Asset Class: `Forklift 3T` (Machinery > Warehouse; 6 aset aktif), `Laptop Standard` (IT > Devices; 120 aset aktif), `Crane Rental Unit` (Machinery > Rented; 0 aset aktif) agar banner Asset Name tanpa Asset Class tampil. Kode dan nama literal dipakai apa adanya karena asersi TC bergantung pada nilai itu.
- Keadaan awal dinamis: `Crane Rental Unit` tanpa Asset Class dengan banner tepat 3 menurut precondition TC-280 dan TC-281 (di TC-441 `Crane Rental Unit` ter-assign ke `HEAVY-EQ`); fixture BE menyetelnya pada langkah 13 dan memulihkan keadaan semula sesudah spec.
- Nilai data mengacu ke `Fixture.fixedAssetAssetClass.<kunci>` (berkas `fixtures/fixed-asset-asset-class.json` belum ada; kunci ditetapkan dan disediakan tim FE).
- Hook dan kemampuan suite (flag Guided Tooltip, seed dan fixture BE): dinyatakan sekali di suite.md; suite serial (`parallel: false`).

## Test Steps

### TC-FA-FAAC-8: Gagal memuat tabel Asset Class lalu Try Again

1. Pasang intercept respons 5xx pada permintaan data tabel Asset Class
2. Klik menu `Accounting` di sidebar
3. Klik tab `Asset Class`
4. Verifikasi ErrorState menampilkan teks `Unable to load this data.` dan tombol `[Try Again]`
5. Lepas intercept respons 5xx
6. Klik `[Try Again]`
7. Verifikasi data dimuat ulang dan baris Asset Class tampil

### TC-FA-FAAC-32: Gagal membaca akun untuk Alert dependensi akun

8. Pasang intercept respons 5xx pada pembacaan akun Chart of Accounts untuk Alert dependensi akun
9. Klik tab `Chart of Accounts`, lalu klik tab `Asset Class`
10. Lepas intercept respons 5xx
11. Verifikasi tabel Asset Class tetap tampil dan dapat dipakai
12. Verifikasi Alert dependensi akun tidak ditampilkan

### TC-FA-FAAC-280: Gagal memuat daftar pada dialog D-23 menampilkan ErrorState

13. Setel keadaan awal lewat fixture BE: `Crane Rental Unit` tanpa Asset Class sehingga banner menghitung tepat 3 (precondition TC-280 dan TC-281)
14. Pasang intercept respons 5xx pada pemuatan daftar dialog D-23
15. Klik link `[View asset names]` pada banner
16. Verifikasi badan dialog menampilkan ErrorState `Unable to load this data.` dengan tombol `[Try Again]`
17. Verifikasi footer `[Close]` tetap tampil
18. Lepas intercept respons 5xx
19. Klik `[Close]`

### TC-FA-FAAC-281: Gagal memuat jumlah Asset Name tanpa Asset Class, banner tidak ditampilkan

20. Pasang intercept respons 5xx pada pembacaan jumlah banner Asset Name tanpa Asset Class
21. Klik tab `Chart of Accounts`, lalu klik tab `Asset Class`
22. Lepas intercept respons 5xx
23. Verifikasi tabel Asset Class tetap tampil
24. Verifikasi banner Asset Name tanpa Asset Class tidak ditampilkan

### TC-FA-FAAC-426: Download gagal menampilkan toast error

25. Pasang intercept respons 5xx pada permintaan Download
26. Klik icon `Download`, lalu pilih `Download as CSV`
27. Verifikasi toast `Error, failed to download Asset-Class.` tampil
28. Lepas intercept respons 5xx

## Notes

1. Subjudul `###` memetakan langkah ke id TC granular. Urutan Verifikasi pada TC-32 dan TC-281 dibalik dari urutan Expected TC (tabel tampil lebih dulu, baru Alert atau banner tidak ditampilkan) supaya tabel yang sudah termuat menjadi anchor positif untuk asersi absence (8b butir 2).
2. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 9 dan 21 (pindah ke tab lain lalu kembali ke tab `Asset Class` agar pembacaan akun dan jumlah banner dimuat ulang saat intercept aktif; TC menulis "Klik tab Asset Class" dan "Muat halaman tab Asset Class" untuk pemuatan itu); langkah 13 (fixture BE menyetel keadaan awal dinamis, S-14), langkah 19 (menutup dialog D-23).
3. Intercept dilepas segera sesudah pemicunya diamati (langkah 5, 10, 18, 22, 28; S-09). Kegagalan 5xx adalah objek uji kelas b; tidak ada pemicu kelas lain di spec ini.
4. Temuan untuk QA: TC-8 dan TC-426 tidak menyebut endpoint yang digagalkan; TC-8 menyebut "kegagalan jaringan" untuk melepas intercept, sedangkan TC-426 menyebut "5xx atau jaringan terputus"; spec memakai respons 5xx untuk keduanya. TC-8 tidak menyebut Class Code baris yang tampil sesudah `[Try Again]`; spec hanya mengasersi baris Asset Class tampil. TC-32 dan TC-281 tidak menyebut cara memuat ulang pembacaan; spec memakai pindah tab. Kode literal TC dipakai tanpa suffix `{runId}` karena spec hanya membaca data Pre-setup.
