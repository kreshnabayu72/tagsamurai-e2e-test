---
id: TC-FA-FAAM-E2E-057-create-sukses-seluruh-field-opsional-dan-non-tag
title: "Create Sukses: Seluruh Field Opsional Terisi dan TAG Type Non-TAG"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-144
  - TC-FA-FAAM-148
coverage:
  web: automated
---

# Create Sukses: Seluruh Field Opsional Terisi dan TAG Type Non-TAG

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control client utama, `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1; bagian `{namaCompany}` mengikuti penulisan Pre-setup TC), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; setiap nama didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo.
- Hook suite berlaku (lihat `suite.md`): sesi API aktor, seed API per TC, pemulihan state global di hook `after`.
- Data Pre-setup #22 s.d. #25 (kategori, brand, UoM, label) tersedia di client utama: Category leaf `IT Equipment` dan `Electronics > Laptop`, Brand `Dell`, `Lenovo`, `Toyota`, `Apple`, UoM `Unit`, `Pcs`, `Set`, Label `Finance`, `High Priority`, `Fragile`. Nilai Pre-setup mengacu ke `fixtures/fixed-asset-settings-asset-name.json` (fixture baru yang ditetapkan tim FE; tanpa password atau token).
- Data Pre-setup (hanya dibaca): Label #25 `Finance` dan `High Priority`, Brand #23 `Dell`; client utama memiliki subscription Paid (Pre-setup #10) dan lisensi addon `Audit` dan `Tracking` aktif.
- Data Dinamis (suffix per run dan nomor spec): Asset Name `Create Full Item {runId}-057` dengan Code manual `CFI-1` (nilai literal karena batas 15 karakter tidak menampung suffix run; record sisa run sebelumnya dengan Code `CFI-1` dihapus lewat API di hook `before`) dan Asset Name `Create NonTag {runId}-057`.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Asset Name `Create Full Item {runId}-057` dan `Create NonTag {runId}-057` bila masih ada (juga record ber-Code `CFI-1` di hook `before`).

## Test Steps

### TC-FA-FAAM-144: Create dengan seluruh field opsional terisi menyimpan semua nilai

1. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
2. Isi Asset Name `Create Full Item {runId}-057`, Code `CFI-1`
3. Pilih Category leaf `IT Equipment`
4. Pilih TAG Type `RFID` dan `QR`, Default Addon `Audit` dan `Tracking`
5. Pilih Default Label `Finance` dan `High Priority`
6. Pilih Brand `Dell`, tambahkan model `5420` dan `3310`, pilih UoM `Unit`
7. Klik `[Submit]`
8. Verifikasi Toast `Success, asset name has been created.` tampil
9. Ketik Search `Create Full Item {runId}-057`, tekan Enter
10. Buka Popup Detail `Create Full Item {runId}-057` dari tabel
11. Verifikasi Detail menampilkan Code `CFI-1`
12. Verifikasi Detail menampilkan TAG Type icon RFID dan QR
13. Verifikasi Detail menampilkan Default Addon `Audit`, `Tracking`
14. Verifikasi Detail menampilkan Default Label `Finance`, `High Priority`
15. Verifikasi Detail menampilkan Brand `Dell` dengan model `3310`, `5420`
16. Verifikasi Detail menampilkan UoM `Unit`
17. Verifikasi Detail menampilkan Total Asset `0`
18. Tutup Popup Detail, lalu klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

### TC-FA-FAAM-148: Create dengan TAG Type Non-TAG menyimpan tanpa tipe TAG aktif

19. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
20. Isi Asset Name `Create NonTag {runId}-057`, Category `IT Equipment`, TAG Type `Non-TAG`, Brand `Dell`, UoM `Unit`
21. Klik `[Submit]`
22. Ketik Search `Create NonTag {runId}-057`, tekan Enter
23. Verifikasi Baris `Create NonTag {runId}-057` tampil dengan TAG Type teks `Non-TAG` tanpa badge
24. Verifikasi Baris `Create NonTag {runId}-057` menampilkan Default Addon `—`
25. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

## Notes

- Code literal `CFI-1` mengikuti Data Uji TC-FA-FAAM-144 dan tidak dapat bersuffix run (maksimum 15 karakter); keunikannya dijaga dengan pembersihan di hook `before` dan `after` serta suite serial (S-12).
- TC-FA-FAAM-144 dan 148 memakai Category, Brand, dan UoM Pre-setup sebagai pilihan saja (tidak diubah). Langkah penghubung (tanpa `Verifikasi`): Search nama untuk menemukan baris target (R-16) dan penutupan Detail dan Search.
- TC-FA-FAAM-148 langkah Submit tidak punya Expected toast; hasilnya diamati lewat baris di List (langkah Search sekaligus menunggu aksi selesai, bagian 8b butir 8).
