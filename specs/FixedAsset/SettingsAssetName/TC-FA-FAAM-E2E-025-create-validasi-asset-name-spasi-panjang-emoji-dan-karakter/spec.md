---
id: TC-FA-FAAM-E2E-025-create-validasi-asset-name-spasi-panjang-emoji-dan-karakter
title: "Create: Validasi Asset Name (Spasi, Batas 120, Spasi Ujung, Emoji, Karakter Lain)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAM-82
  - TC-FA-FAAM-83
  - TC-FA-FAAM-84
  - TC-FA-FAAM-85
  - TC-FA-FAAM-91
  - TC-FA-FAAM-93
coverage:
  web: automated
---

# Create: Validasi Asset Name (Spasi, Batas 120, Spasi Ujung, Emoji, Karakter Lain)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control client utama, `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1; bagian `{namaCompany}` mengikuti penulisan Pre-setup TC), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; setiap nama didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo.
- Hook suite berlaku (lihat `suite.md`): sesi API aktor, seed API per TC, pemulihan state global di hook `after`.
- Data Pre-setup #22 s.d. #25 (kategori, brand, UoM, label) tersedia di client utama: Category leaf `IT Equipment` dan `Electronics > Laptop`, Brand `Dell`, `Lenovo`, `Toyota`, `Apple`, UoM `Unit`, `Pcs`, `Set`, Label `Finance`, `High Priority`, `Fragile`. Nilai Pre-setup mengacu ke `fixtures/fixed-asset-settings-asset-name.json` (fixture baru yang ditetapkan tim FE; tanpa password atau token).
- Data Dinamis (suffix per run dan nomor spec): Asset Name 120 karakter = string 120 karakter yang diakhiri suffix `{runId}-025` (panjang total tepat 120 termasuk suffix, R-06) (TC-FA-FAAM-83); Asset Name `Çafé & Co. (1/2) #A+ {runId}-025` (TC-FA-FAAM-93). Asset Name 121 karakter pada TC-FA-FAAM-84 adalah string yang sama ditambah satu karakter di depan dan tidak pernah tersimpan.
- Data Pre-setup: field wajib lain memakai Category `IT Equipment`, TAG Type `QR`, Brand `Dell`, UoM `Unit` (Data Uji TC-FA-FAAM-88).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Asset Name 120 karakter dan `Çafé & Co. (1/2) #A+ {runId}-025` bila masih ada.

## Test Steps

### Blokir validasi (sebelum aksi sukses)

1. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
2. Isi Asset Name dengan 3 spasi
3. Klik `[Submit]`
4. Verifikasi Error inline `Asset name must not be empty` tampil di bawah field Asset Name
5. Klik `[Clear Field]`
6. Ketik dan paste emoji `😊` di Asset Name
7. Verifikasi Emoji `😊` tidak masuk ke field Asset Name
8. Verifikasi Tidak ada pesan error inline pada field Asset Name
9. Ketik 121 karakter di Asset Name
10. Verifikasi Error inline `Max. 120 characters` muncul langsung saat karakter ke-121 diketik
11. Isi field wajib lain: Category (klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`), TAG Type `QR`, Brand `Dell`, UoM `Unit`
12. Klik `[Submit]`
13. Verifikasi Tidak ada toast `Success, asset name has been created.` selama error aktif (error inline `Max. 120 characters` masih tampil)
14. Ganti isi Asset Name dengan 120 karakter diikuti 5 spasi di akhir
15. Verifikasi Tidak ada error `Max. 120 characters`

### Aksi sukses

16. Ganti isi Asset Name dengan string 120 karakter yang diakhiri suffix `{runId}-025` (panjang total tepat 120 termasuk suffix, R-06)
17. Klik `[Submit]`
18. Verifikasi Tidak ada error `Max. 120 characters`
19. Verifikasi Toast `Success, asset name has been created.` tampil
20. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
21. Isi Asset Name `Çafé & Co. (1/2) #A+ {runId}-025`
22. Isi field wajib lain: Category (klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`), TAG Type `QR`, Brand `Dell`, UoM `Unit`
23. Klik `[Submit]`
24. Verifikasi Toast `Success, asset name has been created.` tampil tanpa error karakter pada Asset Name

## Notes

- Urutan: semua blokir validasi sebelum Create sukses (S-10); form tidak ditutup di antara kasus yang hanya mengetik, field dikembalikan lewat `[Clear Field]` atau diganti isinya (halaman yang sama dipakai berulang).
- Penambahan asersi (S-03): toast `Success, asset name has been created.` pada TC-FA-FAAM-93 dipakai sebagai bukti "record dibuat" karena Expected hanya menulis "Record dibuat tanpa error karakter"; dan TC-FA-FAAM-84 b diasersi lewat tidak adanya toast sukses dengan error inline sebagai anchor positif.
- TC-FA-FAAM-85 (spasi di ujung) tidak memiliki Expected selain tidak adanya error `Max. 120 characters`; ketikan tidak di-Submit di spec ini.
- Langkah "Ketik 121 karakter" berisi string tetap yang tidak diserahkan ke server (Submit diblokir), sehingga tidak memakai suffix run.
- Temuan untuk QA:
  - TC-FA-FAAM-82 dan 85 tidak menyebut field wajib lain terisi; TC-FA-FAAM-82 hanya menguji error Asset Name sehingga error required lain yang ikut tampil tidak diasersi.
  - TC-FA-FAAM-83 menulis Expected "Toast ..." tanpa menyebut nama unik; spec memakai nama 120 karakter bersuffix agar tidak bentrok antar run.
