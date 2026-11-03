---
id: TC-FA-FAAM-E2E-040-create-sukses-code-manual-addon-dan-label
title: "Create Sukses: Code Manual versus Auto, Trim Nama, dan Default Addon"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-86
  - TC-FA-FAAM-100
  - TC-FA-FAAM-145
  - TC-FA-FAAM-146
coverage:
  web: automated
---

# Create Sukses: Code Manual versus Auto, Trim Nama, dan Default Addon

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control client utama, `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1; bagian `{namaCompany}` mengikuti penulisan Pre-setup TC), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; setiap nama didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo.
- Hook suite berlaku (lihat `suite.md`): sesi API aktor, seed API per TC, pemulihan state global di hook `after`.
- Data Pre-setup #22 s.d. #25 (kategori, brand, UoM, label) tersedia di client utama: Category leaf `IT Equipment` dan `Electronics > Laptop`, Brand `Dell`, `Lenovo`, `Toyota`, `Apple`, UoM `Unit`, `Pcs`, `Set`, Label `Finance`, `High Priority`, `Fragile`. Nilai Pre-setup mengacu ke `fixtures/fixed-asset-settings-asset-name.json` (fixture baru yang ditetapkan tim FE; tanpa password atau token).
- Data Dinamis (suffix per run dan nomor spec): Asset Name `  Trim Item {runId}-040  ` (dua spasi di awal dan di akhir; tersimpan sebagai `Trim Item {runId}-040`), `Create Min Item 100 {runId}-040` dengan Code `CRT-01`, `Create Min Item 145 {runId}-040` dengan Code `MANUAL-1`, dan `Create Min Item 146 {runId}-040` dengan Default Addon `Audit`. Code `CRT-01` dan `MANUAL-1` literal karena batas 15 karakter tidak menampung suffix run; record sisa run sebelumnya dengan kedua Code itu dihapus lewat API di hook `before`.
- Data Pre-setup (hanya dibaca): client utama memiliki subscription Paid dan lisensi addon `Audit` aktif (Pre-setup #10).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API keempat Asset Name milik spec ini (dan record ber-Code `CRT-01` serta `MANUAL-1` di hook `before`) bila masih ada.

## Test Steps

### TC-FA-FAAM-86: Asset Name disimpan dalam bentuk ter-trim

1. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
2. Isi field wajib: Asset Name `  Trim Item {runId}-040  `, Category (klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`), TAG Type `QR`, Brand `Dell`, UoM `Unit`
3. Klik `[Submit]`

### TC-FA-FAAM-100: Code valid diterima dan disimpan

4. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
5. Isi field wajib: Asset Name `Create Min Item 100 {runId}-040`, Category (klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`), TAG Type `QR`, Brand `Dell`, UoM `Unit`
6. Isi Code `CRT-01`
7. Klik `[Submit]`

### TC-FA-FAAM-145: Create dengan Code diisi manual berbeda dari Code kosong auto-generate

8. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
9. Isi field wajib: Asset Name `Create Min Item 145 {runId}-040`, Category (klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`), TAG Type `QR`, Brand `Dell`, UoM `Unit`
10. Isi Code `MANUAL-1`
11. Klik `[Submit]`

### TC-FA-FAAM-146: Create dengan Default Addon terisi

12. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
13. Isi field wajib: Asset Name `Create Min Item 146 {runId}-040`, Category (klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`), TAG Type `QR`, Brand `Dell`, UoM `Unit`
14. Pilih Default Addon `Audit`
15. Klik `[Submit]`

### Verifikasi hasil keempat Create

16. Ketik Search `{runId}-040`, tekan Enter
17. Verifikasi Baris tersimpan dengan nama `Trim Item {runId}-040` tanpa spasi tepi
18. Buka Popup Detail `Create Min Item 100 {runId}-040` dari tabel
19. Verifikasi Record tersimpan dengan Code `CRT-01`
20. Tutup Popup Detail
21. Buka Popup Detail `Create Min Item 145 {runId}-040` dari tabel
22. Verifikasi Record tersimpan dengan Code `MANUAL-1`
23. Verifikasi Code `MANUAL-1` bukan hasil generator (bukan turunan nama `Create Min Item 145 {runId}-040`)
24. Tutup Popup Detail
25. Buka Popup Detail `Create Min Item 146 {runId}-040` dari tabel
26. Verifikasi Detail menampilkan Default Addon `Audit`
27. Tutup Popup Detail
28. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

## Notes

- Langkah penghubung (tanpa `Verifikasi`): Search `{runId}-040` mengumpulkan keempat baris milik spec ini untuk satu kali pemeriksaan (R-16), penutupan Popup Detail, dan penutupan Search.
- Urutan dalam spec: empat Create sukses berurutan lalu pemeriksaan hasil, sehingga satu Search menggantikan empat Search; tidak ada aksi yang menghapus data.
- Penambahan asersi (S-03): `Verifikasi` Code `MANUAL-1` bukan turunan nama menjabarkan klausa "bukan hasil generator" pada Expected TC-FA-FAAM-145.
- Sisa langkah pengisian field wajib memakai Data Uji TC-FA-FAAM-145 (Category `IT Equipment`, TAG Type `QR`, Brand `Dell`, UoM `Unit`) untuk keempat TC.
- Temuan untuk QA:
  - TC-FA-FAAM-86 menulis Expected "Baris tersimpan dengan nama `Trim Item`" tanpa Toast; spec tidak mengasersi toast karena tidak ada di Expected.
  - TC-FA-FAAM-100 menulis Data Uji Code `CRT-01` literal tanpa pola keunikan antar run; spec membersihkan record sisa di hook `before`.
