---
id: TC-FA-CAT-E2E-153-gerbang-warranty-dan-purchasing-purchase-group-a
title: "Gerbang Warranty dan Custom Field Purchasing pada Popup Detail untuk Purchase Group A: Filter Tidak Mencocokkan No access dan Sel Warranty Tanpa Penanda"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-693
  - TC-FA-CAT-696
coverage:
  web: automated
---

# Gerbang Warranty dan Custom Field Purchasing pada Popup Detail untuk Purchase Group A: Filter Tidak Mencocokkan No access dan Sel Warranty Tanpa Penanda

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Purchase Group A (Pre-setup #53) `purchaseGroupA_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_PGA_PASSWORD` (Manage Asset Master Data: R; Group Role Manage purchase hanya pada group `Head Office` beserta descendant; tanpa View asset value dan Manage accounting). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_PGA_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup yang hanya dibaca (tidak diubah): Pre-setup #21 (Asset Name `Laptop Dell` dan `Laptop HP` menunjuk `Laptop`; `Office Chair` menunjuk `Furniture`), #22 (aset `Laptop Dell - 1` sampai `- 8`, `Laptop HP - 1` sampai `- 4`), #55 (Warranty Expiry dan Asset Value aset `Laptop`), #56 (Custom Field Purchasing `Nilai Kontrak`, lisensi FA-7 aktif; nilai `Laptop Dell - 1` 5000, `Laptop Dell - 2` 0, `Laptop HP - 1` 250, `Laptop HP - 3` di luar group aktor sehingga `No access`), #58 (`Office Chair - 5`, Group `Region Jawa > Jakarta Selatan Distribution Center`, Warranty Expiry hari ini + 10 hari, diisi ulang lewat seed API pada awal tiap run; `Laptop Dell - 2` tanpa nilai Warranty Expiry).
- Kemampuan teknis: pemulihan konfigurasi kolom Setup Column dengan menghapus preferensi kolom di browser (bukan lewat `[Reset to Default]`), dipakai sebagai langkah penghubung dan di hook `after` suite; disediakan tim FE.
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Fixture `fixtures/settings-categories.json` disediakan tim FE.

## Test Steps

### TC-FA-CAT-693: Filter Custom Field Purchasing, baris No access tidak cocok dengan filter apa pun

1. Pilih node `Electronics` pada sidebar
2. Klik elipsis (⋯) pada baris `Laptop` > `Detail`
3. Klik header Actions (⋯) > `Setup Column...`, centang `Nilai Kontrak`, lalu klik `[Save]`
4. Klik icon Filter, isi `Nilai Kontrak` Min `0` dan Max `99999`, lalu klik `[Apply]`
5. Verifikasi hasil memuat `Laptop Dell - 1`, `Laptop Dell - 2`, dan `Laptop HP - 1`
6. Verifikasi baris `Laptop HP - 3` (`No access`) tidak muncul walau rentang mencakup seluruh nilai
7. Tutup Popup Detail dan pulihkan konfigurasi kolom tabel Assets dengan menghapus preferensi kolom di browser

### TC-FA-CAT-696: Sel Warranty Expiry strip dan No access tanpa warna penanda garansi

8. Pilih node `All Categories` pada sidebar
9. Klik elipsis (⋯) pada baris `Furniture` > `Detail`
10. Klik header Actions (⋯) > `Setup Column...`, centang `Warranty Expiry`, lalu klik `[Save]`
11. Hover sel Warranty Expiry `Office Chair - 5`
12. Verifikasi sel Warranty Expiry `Office Chair - 5` menampilkan `No access`
13. Verifikasi sel Warranty Expiry `Office Chair - 5` tampil tanpa warna warning
14. Verifikasi tooltip sel hanya `Requires Manage purchase access in this group.`
15. Tutup Popup Detail, pilih node `Electronics` pada sidebar, lalu buka Popup Detail `Laptop` lewat elipsis (⋯) > `Detail`
16. Hover sel Warranty Expiry `Laptop Dell - 2`
17. Verifikasi sel Warranty Expiry `Laptop Dell - 2` menampilkan `—`
18. Verifikasi sel Warranty Expiry `Laptop Dell - 2` tampil tanpa warna penanda garansi
19. Verifikasi tidak ada tooltip penanda garansi pada sel Warranty Expiry `Laptop Dell - 2`
20. Tutup Popup Detail dan pulihkan konfigurasi kolom tabel Assets dengan menghapus preferensi kolom di browser

## Notes

- Langkah penghubung (S-03, S-09): langkah 1, 8, 15 (memilih node sidebar), langkah 7, 15, 20 (menutup popup dan memulihkan konfigurasi kolom). Memilih node `All Categories` pada langkah 8 dipakai karena `Furniture` berada di daftar root; nama node mengikuti TC-FA-CAT-1.
- Post Condition TC-FA-CAT-693 dan TC-FA-CAT-696 ("dikembalikan lewat `[Reset to Default]` lalu `[Save]`") dipenuhi dengan menghapus preferensi kolom di browser sesuai konvensi bagian 4; kemampuan disediakan tim FE.
- Absence pada langkah 6 diawali anchor langkah 5 (baris pembanding pada surface yang sama); absence tooltip pada langkah 19 diawali langkah 17 (sel tampil) dan hover langkah 16 (anchor tooltip).
- Spec dengan aktor Group Manager (TC-FA-CAT-685) ada di spec 197.
- Temuan untuk QA:
  - Nama env var password akun aktor tidak tertulis di TC; `FA_PGA_PASSWORD` adalah usulan.
  - TC-FA-CAT-693 langkah 1 menyebut baris `Laptop` "setelah memilih node `Electronics`", sedangkan TC-FA-CAT-696 langkah 1 membuka `Furniture` tanpa menyebut node; spec memilih `All Categories` agar baris `Furniture` terlihat.
  - TC-FA-CAT-696 Expected a menyebut "tanpa warna warning" tanpa definisi asersi warna yang dapat diamati; spec memverifikasinya sebagai klausa terpisah.
  - Nilai Min `0` dan Max `99999` pada TC-FA-CAT-693 mencakup `Laptop Dell - 2` bernilai 0; spec mengikuti Expected TC (tiga baris tampil).
