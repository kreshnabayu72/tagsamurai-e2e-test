---
id: TC-FA-FAAM-E2E-044-create-changelog-create-dan-nama-sama-di-client-lain
title: "Create: Entri Create di Changelog dan Asset Name Sama di Client Lain"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-90
  - TC-FA-FAAM-169
coverage:
  web: automated
---

# Create: Entri Create di Changelog dan Asset Name Sama di Client Lain

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control client utama, `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1; bagian `{namaCompany}` mengikuti penulisan Pre-setup TC), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `FA_TC_PASSWORD`, `FA_CLIENT17_PASSWORD`. Password tidak ditulis di spec atau fixture; setiap nama didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo.
- Hook suite berlaku (lihat `suite.md`): sesi API aktor, seed API per TC, pemulihan state global di hook `after`.
- Data Pre-setup #22 s.d. #25 (kategori, brand, UoM, label) tersedia di client utama: Category leaf `IT Equipment` dan `Electronics > Laptop`, Brand `Dell`, `Lenovo`, `Toyota`, `Apple`, UoM `Unit`, `Pcs`, `Set`, Label `Finance`, `High Priority`, `Fragile`. Nilai Pre-setup mengacu ke `fixtures/fixed-asset-settings-asset-name.json` (fixture baru yang ditetapkan tim FE; tanpa password atau token).
- Akun aktor kedua (ganti akun eksplisit di langkah spec): Total Control client lain (Pre-setup #17), tidak memiliki Asset Name `Dell Latitude`; email akun tidak tertulis di Pre-setup TC (disediakan tim FE; lihat Temuan untuk QA), `Spectra.env.FA_CLIENT17_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite.
- Data Dinamis (suffix per run dan nomor spec): Asset Name `Create Min Item 169 {runId}-044` (client utama) dan `Dell Latitude {runId}-044` yang di-seed lewat API di client utama (salinan nama Pre-setup #10 agar nama yang sama sudah ada di client utama) lalu dibuat lewat UI di client lain.
- Kemampuan teknis: jam server dan jam browser sinkron; nama aktor untuk Modified By mengacu ke `Fixture.fixedAssetSettingsAssetName.actorTotalControl.modifiedBy` (format `[First Name] [Last Initial]`, fixture baru ditetapkan tim FE).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Create Min Item 169 {runId}-044` dan `Dell Latitude {runId}-044` di client utama dan di client lain bila masih ada.

## Test Steps

### TC-FA-FAAM-169: Create sukses menulis satu entri Create di Changelog

1. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
2. Isi field wajib: Asset Name `Create Min Item 169 {runId}-044`, Category (klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`), TAG Type `QR`, Brand `Dell`, UoM `Unit`
3. Klik `[Submit]`
4. Buka Changelog
5. Ketik Search `Create Min Item 169 {runId}-044` di Modal Changelog, tekan Enter
6. Verifikasi Entri Changelog memuat Action `Create`
7. Verifikasi Entri Changelog memuat Asset Name `Create Min Item 169 {runId}-044`
8. Verifikasi Entri Changelog memuat Field `Asset Name`
9. Verifikasi Entri Changelog memuat Old `—`
10. Verifikasi Entri Changelog memuat New `Create Min Item 169 {runId}-044`
11. Verifikasi Entri Changelog memuat Modified By aktor dalam format `[First Name] [Last Initial]`
12. Verifikasi Hanya satu baris untuk `Create Min Item 169 {runId}-044` (atribut konfigurasi awal lain tidak dicatat per baris)
13. Tutup Modal Changelog

### TC-FA-FAAM-90: Asset Name yang sama di client lain diterima

14. Ganti akun: keluar (Logout), lalu login sebagai Total Control client lain (Pre-setup #17; email disediakan tim FE, `Spectra.env.FA_CLIENT17_PASSWORD`), lalu buka Fixed Asset > Settings > Asset Master > Asset Name
15. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
16. Isi field wajib: Asset Name `Dell Latitude {runId}-044`, Category (klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`), TAG Type `QR`, Brand `Dell`, UoM `Unit`
17. Klik `[Submit]`
18. Verifikasi Toast `Success, asset name has been created.` tampil
19. Verifikasi Tidak ada error duplikat `Asset name already exists`

## Notes

- Urutan TC dalam spec: TC-FA-FAAM-169 di client utama lebih dahulu, TC-FA-FAAM-90 sesudah ganti akun ke client lain; sesi dipulihkan ke akun default di hook `after` (S-07).
- Search nama di Modal Changelog adalah langkah penghubung untuk menemukan entri milik spec ini (R-16); entri teratas pada TC dicari lewat nama karena Changelog tumbuh (S-14).
- `Dell Latitude {runId}-044` memakai nama bersuffix agar keberadaan nama yang sama di client utama (precondition TC-FA-FAAM-90) dapat dipenuhi tanpa menulis ke Pre-setup #10 dan tanpa bentrok antar run.
- Temuan untuk QA:
  - TC-FA-FAAM-90 menyebut "Login pada Client lain (Pre-setup #17)" tanpa email dan nama env akun; disediakan tim FE (nama env diusulkan `FA_CLIENT17_PASSWORD`).
  - TC-FA-FAAM-90 Post Condition (Dynamic #78 "tetap ada di Client lain") bertentangan dengan keunikan antar run; spec membersihkan record bersuffix.
