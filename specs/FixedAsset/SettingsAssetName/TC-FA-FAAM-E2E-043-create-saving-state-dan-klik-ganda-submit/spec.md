---
id: TC-FA-FAAM-E2E-043-create-saving-state-dan-klik-ganda-submit
title: "Create: Saving State Tombol Submit dan Klik Ganda Cepat Hanya Satu Record"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAM-68
  - TC-FA-FAAM-167
coverage:
  web: automated
---

# Create: Saving State Tombol Submit dan Klik Ganda Cepat Hanya Satu Record

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control client utama, `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1; bagian `{namaCompany}` mengikuti penulisan Pre-setup TC), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; setiap nama didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo.
- Hook suite berlaku (lihat `suite.md`): sesi API aktor, seed API per TC, pemulihan state global di hook `after`.
- Data Pre-setup #22 s.d. #25 (kategori, brand, UoM, label) tersedia di client utama: Category leaf `IT Equipment` dan `Electronics > Laptop`, Brand `Dell`, `Lenovo`, `Toyota`, `Apple`, UoM `Unit`, `Pcs`, `Set`, Label `Finance`, `High Priority`, `Fragile`. Nilai Pre-setup mengacu ke `fixtures/fixed-asset-settings-asset-name.json` (fixture baru yang ditetapkan tim FE; tanpa password atau token).
- Kemampuan teknis: `Spectra.intercept()` menahan respons Create selama 3 detik hanya untuk mengamati state UI (bukan kegagalan yang dipaksakan); intercept dilepas segera setelah respons diterima.
- Data Dinamis (suffix per run dan nomor spec): Asset Name `Create Min Item 68 {runId}-043` dan `Create Min Item 167 {runId}-043`. Pembacaan jumlah entri Changelog memakai Search nama bersuffix (baseline nol).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): lepaskan intercept bila masih aktif; hapus lewat API kedua Asset Name milik spec ini bila masih ada.

## Test Steps

### TC-FA-FAAM-68: Tombol Submit masuk Saving state selama request berlangsung

1. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
2. Isi field wajib: Asset Name `Create Min Item 68 {runId}-043`, Category (klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`), TAG Type `QR`, Brand `Dell`, UoM `Unit`
3. Centang `Stay on this form after submitting` (agar modal tetap terbuka dan kontrol dapat diamati setelah respons)
4. Tunda respons Create 3 detik lewat intercept jaringan
5. Klik `[Submit]`
6. Verifikasi Tombol `[Submit]` menampilkan loading dan disabled
7. Verifikasi `[Clear Field]`, checkbox Stay, dan icon `[✕]` disabled selama request
8. Tunggu respons Create diterima, lalu lepaskan intercept
9. Verifikasi Tombol `[Submit]`, `[Clear Field]`, checkbox Stay, dan icon `[✕]` aktif kembali setelah respons diterima

### TC-FA-FAAM-167: Klik ganda cepat pada Submit hanya membuat satu record

10. Isi field wajib: Asset Name `Create Min Item 167 {runId}-043`, Category (klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`), TAG Type `QR`, Brand `Dell`, UoM `Unit`
11. Klik `[Submit]` dua kali cepat
12. Verifikasi Tombol `[Submit]` disabled setelah klik pertama
13. Klik `[✕]` (form bersih tertutup tanpa dialog)
14. Ketik Search `Create Min Item 167 {runId}-043`, tekan Enter
15. Verifikasi Hanya satu baris `Create Min Item 167 {runId}-043` pada tabel
16. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel
17. Buka Changelog
18. Ketik Search `Create Min Item 167 {runId}-043`, tekan Enter di Modal Changelog
19. Verifikasi Hanya satu entri log Create untuk `Create Min Item 167 {runId}-043`
20. Tutup Modal Changelog

## Notes

- Penambahan langkah (S-03): TC-FA-FAAM-68 tidak mencentang Stay, tetapi Expected c ("setelah respons diterima kontrol aktif kembali") tidak dapat diamati bila modal menutup setelah sukses; spec mencentang Stay agar modal tetap terbuka (Temuan untuk QA).
- Asersi state sementara (bagian 8b butir 5) diperiksa sebelum respons dilepas; intercept dilepas segera setelah respons diterima (S-09).
- Langkah penghubung (tanpa `Verifikasi`): `[✕]` menutup form bersih setelah klik ganda; Search nama untuk menemukan baris target (R-16); Search nama di Modal Changelog; penutupan Search dan Modal Changelog.
- Temuan untuk QA:
  - TC-FA-FAAM-68 Expected c tidak teramati bila modal menutup setelah respons (Stay tidak dicentang); TC perlu menyatakan Stay tercentang atau kondisi lain agar kontrol dapat diamati.
  - TC-FA-FAAM-167 Expected a menulis "satu entri log Create" tanpa menyebut surface log; spec memakai Modal Changelog.
