---
id: TC-FA-FAAM-E2E-024-create-required-semua-field-wajib
title: "Create: Error Required Tiap Field Wajib dan Submit Semua Field Kosong"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-81
  - TC-FA-FAAM-101
  - TC-FA-FAAM-106
  - TC-FA-FAAM-127
  - TC-FA-FAAM-139
  - TC-FA-FAAM-142
coverage:
  web: automated
---

# Create: Error Required Tiap Field Wajib dan Submit Semua Field Kosong

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control client utama, `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1; bagian `{namaCompany}` mengikuti penulisan Pre-setup TC), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; setiap nama didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo.
- Hook suite berlaku (lihat `suite.md`): sesi API aktor, seed API per TC, pemulihan state global di hook `after`.
- Data Pre-setup #22 s.d. #25 (kategori, brand, UoM, label) tersedia di client utama: Category leaf `IT Equipment` dan `Electronics > Laptop`, Brand `Dell`, `Lenovo`, `Toyota`, `Apple`, UoM `Unit`, `Pcs`, `Set`, Label `Finance`, `High Priority`, `Fragile`. Nilai Pre-setup mengacu ke `fixtures/fixed-asset-settings-asset-name.json` (fixture baru yang ditetapkan tim FE; tanpa password atau token).
- Data Dinamis: Asset Name `Create Min Item {runId}-024` hanya diketik dan tidak pernah tersimpan karena semua Submit diblokir validasi; tidak ada seeding.
- Tabel "Field yang dikosongkan" (parameter perulangan langkah 10 sampai 14): (1) Asset Name kosong, error `Asset name must not be empty` (TC-FA-FAAM-81); (2) Category kosong, error `Category must not be empty` (TC-FA-FAAM-101); (3) TAG Type kosong, error `Select at least one TAG type or Non-TAG` (TC-FA-FAAM-106); (4) Brand kosong, error `Brand must not be empty` (TC-FA-FAAM-127); (5) UoM kosong, error `UoM must not be empty` (TC-FA-FAAM-139). Nilai valid field lain: Asset Name `Create Min Item {runId}-024`, Category leaf `IT Equipment`, TAG Type `QR`, Brand `Dell`, UoM `Unit` (Data Uji TC-FA-FAAM-81).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): tidak ada data yang dibuat; popup ditutup lewat langkah pemulihan di akhir spec.

## Test Steps

### TC-FA-FAAM-142: Submit dengan semua field wajib kosong menampilkan semua error required

1. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
2. Klik `[Submit]`
3. Verifikasi Error inline `Asset name must not be empty` tampil di bawah field Asset Name
4. Verifikasi Error inline `Category must not be empty` tampil di bawah field Category
5. Verifikasi Error inline `Select at least one TAG type or Non-TAG` tampil di bawah field TAG Type
6. Verifikasi Error inline `Brand must not be empty` tampil di bawah field Brand
7. Verifikasi Error inline `UoM must not be empty` tampil di bawah field UoM
8. Verifikasi Tidak ada toast setelah Submit
9. Verifikasi Modal tetap terbuka

### TC-FA-FAAM-81, 101, 106, 127, 139: Satu field wajib kosong saat Submit (perulangan atas tabel "Field yang dikosongkan")

10. Untuk setiap baris tabel "Field yang dikosongkan" pada Prerequisites: klik `[Clear Field]` (membersihkan error dan isian dari iterasi sebelumnya)
11. Isi semua field wajib lain dengan nilai valid pada tabel, kosongkan field pada kolom "Field yang dikosongkan"
12. Klik `[Submit]`
13. Verifikasi Error inline pada kolom "Error" tabel tampil di bawah field yang kosong
14. Verifikasi Tidak ada toast `Success, asset name has been created.` dan modal tetap terbuka (record tidak dibuat)
15. Setelah baris terakhir tabel selesai: Pulihkan form: klik `[Clear Field]`, lalu klik `[✕]` (form bersih tertutup tanpa dialog)

## Notes

- Langkah 10 sampai 14 diulang untuk lima baris tabel "Field yang dikosongkan" (TC-FA-FAAM-81, 101, 106, 127, 139); parameter tiap iterasi ada di Prerequisites dan tidak ada langkah bersyarat (bagian 8b butir 7). Ekspansi: 9 langkah (TC-FA-FAAM-142) + 5 x 5 langkah + 1 langkah pemulihan = 35 langkah.
- Urutan: TC-FA-FAAM-142 (semua kosong) lebih dahulu sebagai screening, lalu iterasi satu field kosong; `[Clear Field]` di awal tiap iterasi mencegah error identik dari iterasi sebelumnya terbaca ulang (R-12).
- TC-FA-FAAM-81, 101, 106, 127, 139 menulis "Record tidak dibuat" hanya pada TC-FA-FAAM-81; untuk iterasi lain "record tidak dibuat" tidak punya Expected, spec tetap mengasersi pola yang sama agar seragam. Nama uji tidak dicari di List karena Submit selalu diblokir (modal tetap terbuka dan toast sukses tidak ada, dengan error inline sebagai anchor positif).
- Langkah pemulihan `[Clear Field]` lalu `[✕]` (langkah terakhir) adalah langkah penghubung tanpa `Verifikasi`: form dikembalikan bersih sehingga ditutup tanpa dialog `Unsaved Changes` (S-09).
- Temuan untuk QA:
  - TC-FA-FAAM-81 menulis Data Uji lengkap, sedangkan TC-FA-FAAM-101, 106, 127, 139 menulis "Isi field wajib lain" tanpa Data Uji; spec memakai nilai Data Uji TC-FA-FAAM-81 untuk semuanya.
  - TC-FA-FAAM-142 Expected b menulis "tanpa request mutasi yang berhasil" tanpa cara mengamati request; spec mengasersi tidak adanya toast dan modal tetap terbuka.
