---
id: TC-FA-FAAM-E2E-054-generator-code-fallback-dedup-dan-batas-15
title: "Generator Code: Fallback 6 Karakter dan AN, Suffix Sekuensial, Batas 15, dan Atomik dengan Penyimpanan"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAM-333
  - TC-FA-FAAM-334
  - TC-FA-FAAM-335
  - TC-FA-FAAM-336
  - TC-FA-FAAM-337
  - TC-FA-FAAM-342
coverage:
  web: automated
---

# Generator Code: Fallback 6 Karakter dan AN, Suffix Sekuensial, Batas 15, dan Atomik dengan Penyimpanan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control client utama, `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1; bagian `{namaCompany}` mengikuti penulisan Pre-setup TC), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; setiap nama didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo.
- Hook suite berlaku (lihat `suite.md`): sesi API aktor, seed API per TC, pemulihan state global di hook `after`.
- Data Pre-setup #22 s.d. #25 (kategori, brand, UoM, label) tersedia di client utama: Category leaf `IT Equipment` dan `Electronics > Laptop`, Brand `Dell`, `Lenovo`, `Toyota`, `Apple`, UoM `Unit`, `Pcs`, `Set`, Label `Finance`, `High Priority`, `Fragile`. Nilai Pre-setup mengacu ke `fixtures/fixed-asset-settings-asset-name.json` (fixture baru yang ditetapkan tim FE; tanpa password atau token).
- Data Dinamis: Asset Name pada tabel di bawah dibuat spec ini dengan Code dikosongkan, dan Asset Name `Gen Log Item {runId}-054` (TC-FA-FAAM-342). Nama pada tabel literal tanpa suffix per run karena Code hasil generator diturunkan dari nama; record bernama sama atau ber-Code sama (`LAPTOP`, `AN`, `USEDLA`, `DL2`, `DL3`, `987654321098765`, `987654321098762`) sisa run sebelumnya dihapus lewat API di hook `before` dan record milik spec dihapus di hook `after`.
- Data Pre-setup (hanya dibaca): Asset Name lain ber-Code `DL` (Pre-setup #10m), disediakan oleh seed API.
- Tabel "Variasi nama" (parameter perulangan langkah 1 sampai 6; Asset Name literal sesuai Data Uji TC, Code dikosongkan; baris dijalankan berurutan karena baris 5 bergantung pada baris 4 dan baris 7 pada baris 6): (1) `Laptop` menghasilkan `LAPTOP` (TC-FA-FAAM-333); (2) `日本語 設備` menghasilkan `AN` (TC-FA-FAAM-334); (3) `(Used) Laptop` menghasilkan `USEDLA` (TC-FA-FAAM-335); (4) `Dell Lenovo` menghasilkan `DL2` karena kandidat `DL` sudah dipakai Asset Name lain ber-Code `DL` (TC-FA-FAAM-336, bagian pertama); (5) `Dell Laptop` menghasilkan `DL3` (TC-FA-FAAM-336, bagian kedua); (6) `98765 43210 98765` menghasilkan `987654321098765`, 15 karakter (TC-FA-FAAM-337, bagian pertama); (7) `98765 43210 98765 1` menghasilkan `987654321098762`: kandidat `987654321098765` sudah terpakai sehingga dipotong menjadi `98765432109876` lalu diberi suffix `2`, tepat 15 karakter (TC-FA-FAAM-337, bagian kedua).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API ketujuh Asset Name pada tabel dan `Gen Log Item {runId}-054` (di hook `before` dan `after`); Asset Name ber-Code `DL` Pre-setup #10m tidak dihapus.

## Test Steps

### TC-FA-FAAM-333, 334, 335, 336, 337: Hasil generator Code (perulangan atas tabel "Variasi nama")

1. Untuk setiap baris tabel "Variasi nama" pada Prerequisites: klik `[+ Asset Name]`
2. Isi Asset Name sesuai kolom nama dengan Code dikosongkan dan field wajib lain terisi (Category (klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`), TAG Type `QR`, Brand `Dell`, UoM `Unit`)
3. Klik `[Submit]`
4. Ganti isi kotak search dengan nama pada kolom nama, tekan Enter (kotak Search dibuka bila masih tertutup)
5. Buka Popup Detail record itu dari tabel
6. Verifikasi Code tersimpan sesuai kolom Code tabel dan tidak kosong
7. Tutup Popup Detail
8. Setelah baris terakhir tabel selesai: klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

### TC-FA-FAAM-342: Code hasil generator ikut atomik dengan penyimpanan dan tidak menulis entri log terpisah

9. Klik `[+ Asset Name]`
10. Isi Asset Name `Gen Log Item {runId}-054` dengan Code dikosongkan dan field wajib lain terisi (Category (klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`), TAG Type `QR`, Brand `Dell`, UoM `Unit`)
11. Klik `[Submit]`
12. Buka Changelog
13. Ketik Search `Gen Log Item {runId}-054` di Modal Changelog, tekan Enter
14. Verifikasi Changelog hanya memuat 1 baris Create (Field `Asset Name`) untuk `Gen Log Item {runId}-054`
15. Verifikasi Tidak ada baris Code terpisah untuk `Gen Log Item {runId}-054`
16. Tutup Modal Changelog

## Notes

- Langkah 1 sampai 6 diulang untuk tujuh baris tabel "Variasi nama" (TC-FA-FAAM-333, 334, 335, 336, 337); parameter tiap iterasi ada di Prerequisites dan tidak ada langkah bersyarat (bagian 8b butir 7). Ekspansi: 7 x 7 langkah + 1 langkah penutup + 7 langkah TC-FA-FAAM-342 = 57 langkah.
- Alasan di atas smell 35 langkah: seluruh blok satu kelas harness (Generator Code dengan Code dikosongkan) dan berdiri sendiri; jumlah besar berasal dari perulangan satu pola per baris tabel. Kegagalan satu baris tidak membuat baris lain kehilangan makna, kecuali dua pasang yang sengaja berurutan (baris 4 lalu 5, baris 6 lalu 7) karena Expected-nya bergantung pada keberadaan baris pertama.
- Nama literal dipertahankan (penyimpangan atas suffix per run, S-12) karena Expected Code bergantung pada karakter nama; keunikan dijaga dengan pembersihan di hook `before` dan `after` serta suite serial (Temuan untuk QA).
- TC-FA-FAAM-336 dan 337 masing-masing dibagi dua baris tabel; kedua baris satu TC berada di spec yang sama. TC-FA-FAAM-342 Expected b ("Tidak ada baris Code terpisah") diasersi sesudah anchor positif baris Create tampil pada surface yang sama (bagian 8b butir 2).
- Langkah penghubung (tanpa `Verifikasi`): Search nama untuk menemukan baris target (R-16), penutupan Popup Detail, penutupan Search, dan penutupan Modal Changelog.
- Temuan untuk QA:
  - Expected Code TC-FA-FAAM-333 sampai 337 hanya benar untuk nama persis tanpa suffix; Data Dinamis TC menandai nama "unik per TC" tanpa pola keunikan antar run. Perlu keputusan QA: nama literal dengan pembersihan (dipakai di spec ini) atau Expected berpola.
  - TC-FA-FAAM-336 dan 337 tidak menyebut Category, TAG Type, Brand, dan UoM untuk record kedua; TC-FA-FAAM-336 hanya "Pre-setup #22 s.d. #25 tersedia". Spec memakai nilai Data Uji TC-FA-FAAM-337 (Category `IT Equipment`, TAG Type `QR`, Brand `Dell`, UoM `Unit`).
  - Pre-setup #10m (Asset Name ber-Code `DL`) tidak menyebut nama Asset Name pemilik Code `DL`; disediakan oleh seed API.
