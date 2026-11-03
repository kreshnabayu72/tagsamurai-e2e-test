---
id: TC-FA-FAAM-E2E-039-create-sukses-hanya-field-wajib
title: "Create Sukses: Hanya Field Wajib dengan Code Auto-Generate"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-143
coverage:
  web: automated
---

# Create Sukses: Hanya Field Wajib dengan Code Auto-Generate

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control client utama, `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1; bagian `{namaCompany}` mengikuti penulisan Pre-setup TC), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; setiap nama didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo.
- Hook suite berlaku (lihat `suite.md`): sesi API aktor, seed API per TC, pemulihan state global di hook `after`.
- Data Pre-setup #22 s.d. #25 (kategori, brand, UoM, label) tersedia di client utama: Category leaf `IT Equipment` dan `Electronics > Laptop`, Brand `Dell`, `Lenovo`, `Toyota`, `Apple`, UoM `Unit`, `Pcs`, `Set`, Label `Finance`, `High Priority`, `Fragile`. Nilai Pre-setup mengacu ke `fixtures/fixed-asset-settings-asset-name.json` (fixture baru yang ditetapkan tim FE; tanpa password atau token).
- Data Dinamis: Asset Name `Create Min Item 143` (Data Uji TC-FA-FAAM-143, nama literal karena Code hasil generator `CMI143` diturunkan dari nama; record sisa run sebelumnya dihapus lewat API di hook `before` dan record milik spec dihapus di hook `after`).
- Kemampuan teknis: jam server dan jam browser sinkron (asersi Last Updated memakai toleransi satu menit, S-12). Nama aktor untuk Modified By mengacu ke `Fixture.fixedAssetSettingsAssetName.actorTotalControl.modifiedBy` (format `[First Name] [Last Initial]`, fixture baru ditetapkan tim FE).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Asset Name `Create Min Item 143` bila masih ada (di hook `before` dan `after`).

## Test Steps

1. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
2. Isi Asset Name `Create Min Item 143`
3. Klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`
4. Pilih TAG Type `QR`
5. Pilih Brand `Dell`
6. Pilih UoM `Unit`
7. Klik `[Submit]`
8. Verifikasi Toast `Success, asset name has been created.` tampil
9. Verifikasi Modal tertutup
10. Catat waktu sesudah `[Submit]` sebagai acuan Last Updated
11. Ketik Search `Create Min Item 143`, tekan Enter
12. Verifikasi Baris `Create Min Item 143` tampil di List
13. Buka Popup Detail `Create Min Item 143` dari tabel
14. Verifikasi Detail menampilkan Code terisi otomatis menurut F-FAAM-12: `CMI143`
15. Verifikasi Detail menampilkan Default Addon `—`
16. Verifikasi Detail menampilkan Default Label `—`
17. Verifikasi Detail menampilkan Brand `Dell` dengan model `No Model`
18. Verifikasi Detail menampilkan UoM `Unit`
19. Verifikasi Detail menampilkan Total Asset `0`
20. Verifikasi Modified By berisi nama aktor dalam format `[First Name] [Last Initial]`
21. Verifikasi Last Updated berisi waktu Create (selisih terhadap waktu acuan di bawah satu menit)
22. Tutup Popup Detail, lalu klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

## Notes

- Nama literal `Create Min Item 143` dipakai karena Expected Code `CMI143` bergantung pada nama; ini menyimpang dari suffix per run (S-12) dan dijaga dengan pembersihan di hook `before` dan `after` serta suite serial (Temuan untuk QA).
- Langkah penghubung (tanpa `Verifikasi`): pencatatan waktu pada langkah 10 (dasar asersi Last Updated), Search nama untuk menemukan baris target (R-16), dan penutupan Detail dan Search di langkah terakhir.
- Temuan untuk QA:
  - Post Condition TC-FA-FAAM-143 butir b dan c (dropdown Asset Name di asset-registration dan baris policy transaksi di settings-asset-transactional-policy) tidak punya langkah observasi dan berada di modul lain; tidak diasersi (S-01).
  - Expected Code `CMI143` mengasumsikan nama tanpa suffix per run; TC tidak menyebut cara menjaga keunikan nama antar run. Spec memakai nama literal dan pembersihan; TC sebaiknya menyatakan pola Expected Code bila suffix wajib.
