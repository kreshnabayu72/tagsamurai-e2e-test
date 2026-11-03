---
id: TC-FA-FAAM-E2E-026-create-validasi-asset-name-duplikat-dan-debounce
title: "Create: Validasi Asset Name Duplikat (Saat Mengetik, Beda Huruf Besar-Kecil, Debounce 500 ms)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-87
  - TC-FA-FAAM-88
  - TC-FA-FAAM-89
coverage:
  web: automated
---

# Create: Validasi Asset Name Duplikat (Saat Mengetik, Beda Huruf Besar-Kecil, Debounce 500 ms)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control client utama, `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1; bagian `{namaCompany}` mengikuti penulisan Pre-setup TC), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; setiap nama didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo.
- Hook suite berlaku (lihat `suite.md`): sesi API aktor, seed API per TC, pemulihan state global di hook `after`.
- Data Pre-setup #22 s.d. #25 (kategori, brand, UoM, label) tersedia di client utama: Category leaf `IT Equipment` dan `Electronics > Laptop`, Brand `Dell`, `Lenovo`, `Toyota`, `Apple`, UoM `Unit`, `Pcs`, `Set`, Label `Finance`, `High Priority`, `Fragile`. Nilai Pre-setup mengacu ke `fixtures/fixed-asset-settings-asset-name.json` (fixture baru yang ditetapkan tim FE; tanpa password atau token).
- Data Pre-setup (hanya dibaca): Asset Name #10 `Dell Latitude` (Code `DLAT`) sebagai nama yang sudah ada.
- Kemampuan teknis (disediakan tim FE): pengamatan jeda 500 ms (debounce) cek keunikan; spec menunggu 600 ms nyata (di bawah batas 30 detik).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): tidak ada data yang dibuat; popup ditutup lewat langkah pemulihan di akhir spec.

## Test Steps

1. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka

### TC-FA-FAAM-87: Asset Name duplikat menampilkan error saat mengetik

2. Ketik `Dell Latitude` di Asset Name lalu tunggu lebih dari 500 ms tanpa pindah fokus
3. Verifikasi Error inline `Asset name already exists` muncul tanpa menunggu blur

### TC-FA-FAAM-89: Cek keunikan berjalan setelah jeda sekitar 500 ms, bukan per keystroke

4. Kosongkan isi Asset Name
5. Ketik `Dell Latitude` cepat tanpa jeda
6. Verifikasi Segera setelah ketikan terakhir belum ada error pada field Asset Name
7. Tunggu 600 ms
8. Verifikasi Error inline `Asset name already exists` muncul setelah jeda

### TC-FA-FAAM-88: Duplikat tanpa membedakan huruf besar-kecil dan spasi tepi

9. Ganti isi Asset Name dengan `  dell LATITUDE  ` (dua spasi di awal dan di akhir)
10. Isi field wajib lain: Category (klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`), TAG Type `QR`, Brand `Dell`, UoM `Unit`
11. Klik `[Submit]`
12. Verifikasi Error inline `Asset name already exists` tampil
13. Verifikasi Tidak ada toast `Success, asset name has been created.` dan modal tetap terbuka (record tidak dibuat)
14. Pulihkan form: klik `[Clear Field]`, lalu klik `[✕]` (form bersih tertutup tanpa dialog)
15. Ketik Search `Dell Latitude`, tekan Enter
16. Verifikasi Tepat satu baris bernama `Dell Latitude` pada tabel (tidak ada duplikat baru)
17. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

## Notes

- Urutan TC dalam spec: TC-FA-FAAM-87, 89, 88 (kasus yang hanya mengetik lebih dahulu, kasus Submit terakhir) agar form tidak dibuka ulang.
- TC-FA-FAAM-88 "record tidak dibuat" diasersi dua kali: tidak adanya toast sukses dengan modal terbuka (anchor: error inline tampil) dan jumlah baris bernama `Dell Latitude` tetap satu setelah form ditutup. Search pada langkah akhir adalah langkah penghubung untuk menemukan baris pembanding (R-16).
- TC-FA-FAAM-89 ("perhatikan pesan segera" dan "tunggu 600 ms") ditulis sebagai `Verifikasi` dan langkah tunggu pendek (di bawah 30 detik) menurut bagian 6.
- Langkah pemulihan `[Clear Field]` lalu `[✕]` (langkah pemulihan sebelum Search) adalah langkah penghubung tanpa `Verifikasi`: form dikembalikan bersih sehingga ditutup tanpa dialog `Unsaved Changes` (S-09).
