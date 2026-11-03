---
id: TC-FA-FAAM-E2E-053-generator-code-token-pemisah-dan-angka
title: "Generator Code: Dua Kata, Pemisah, Token Angka, dan Token Campuran"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-329
  - TC-FA-FAAM-330
  - TC-FA-FAAM-331
  - TC-FA-FAAM-332
coverage:
  web: automated
---

# Generator Code: Dua Kata, Pemisah, Token Angka, dan Token Campuran

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control client utama, `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1; bagian `{namaCompany}` mengikuti penulisan Pre-setup TC), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; setiap nama didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo.
- Hook suite berlaku (lihat `suite.md`): sesi API aktor, seed API per TC, pemulihan state global di hook `after`.
- Data Pre-setup #22 s.d. #25 (kategori, brand, UoM, label) tersedia di client utama: Category leaf `IT Equipment` dan `Electronics > Laptop`, Brand `Dell`, `Lenovo`, `Toyota`, `Apple`, UoM `Unit`, `Pcs`, `Set`, Label `Finance`, `High Priority`, `Fragile`. Nilai Pre-setup mengacu ke `fixtures/fixed-asset-settings-asset-name.json` (fixture baru yang ditetapkan tim FE; tanpa password atau token).
- Data Dinamis: Asset Name pada tabel di bawah dibuat spec ini dengan Code dikosongkan. Nama literal tanpa suffix per run karena Code hasil generator diturunkan dari nama; record bernama sama atau ber-Code sama sisa run sebelumnya dihapus lewat API di hook `before` dan record milik spec dihapus di hook `after`.
- Tabel "Variasi nama" (parameter perulangan langkah 1 sampai 6; Asset Name literal sesuai Data Uji TC, Code dikosongkan): (1) `Dell Latitude Baru` menghasilkan `DLB` (TC-FA-FAAM-329); (2) `Kabel-Data_Pro/Plus` menghasilkan `KDPP` (TC-FA-FAAM-330); (3) `Laptop 15 Inch` menghasilkan `L15I` (TC-FA-FAAM-331); (4) `R2D2 Robot` menghasilkan `RR` (TC-FA-FAAM-332).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API keempat Asset Name pada tabel (di hook `before` dan `after`).

## Test Steps

1. Untuk setiap baris tabel "Variasi nama" pada Prerequisites: klik `[+ Asset Name]`
2. Isi Asset Name sesuai kolom nama dengan Code dikosongkan dan field wajib lain terisi (Category (klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`), TAG Type `QR`, Brand `Dell`, UoM `Unit`)
3. Klik `[Submit]`
4. Ganti isi kotak search dengan nama pada kolom nama, tekan Enter (kotak Search dibuka bila masih tertutup)
5. Buka Popup Detail record itu dari tabel
6. Verifikasi Code tersimpan sesuai kolom Code tabel dan tidak kosong
7. Tutup Popup Detail
8. Setelah baris terakhir tabel selesai: klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

## Notes

- Langkah 1 sampai 6 diulang untuk empat baris tabel "Variasi nama" (TC-FA-FAAM-329, 330, 331, 332); parameter tiap iterasi ada di Prerequisites dan tidak ada langkah bersyarat (bagian 8b butir 7). Ekspansi: 4 x 7 langkah + 1 langkah penutup = 29 langkah.
- Nama literal dipertahankan (penyimpangan atas suffix per run, S-12) karena Expected Code (`DLB`, `KDPP`, `L15I`, `RR`) bergantung pada karakter nama; keunikan dijaga dengan pembersihan di hook `before` dan `after` serta suite serial (Temuan untuk QA).
- Langkah penghubung (tanpa `Verifikasi`): Search nama untuk menemukan baris target (R-16), penutupan Popup Detail, dan penutupan Search di langkah terakhir.
- Temuan untuk QA:
  - Expected Code TC-FA-FAAM-329 sampai 332 hanya benar untuk nama persis tanpa suffix; Data Dinamis TC menandai nama "unik per TC" tanpa pola keunikan antar run. Perlu keputusan QA: nama literal dengan pembersihan (dipakai di spec ini) atau Expected berpola.
