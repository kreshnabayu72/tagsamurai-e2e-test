---
id: TC-FA-FAAM-E2E-033-create-input-model-batas-karakter-dan-emoji
title: "Create: Input Model (Enter, Batas 120, Nama Sama Beda Brand, Emoji, Hapus Badge)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAM-131
  - TC-FA-FAAM-132
  - TC-FA-FAAM-134
  - TC-FA-FAAM-136
  - TC-FA-FAAM-138
coverage:
  web: automated
---

# Create: Input Model (Enter, Batas 120, Nama Sama Beda Brand, Emoji, Hapus Badge)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control client utama, `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1; bagian `{namaCompany}` mengikuti penulisan Pre-setup TC), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; setiap nama didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo.
- Hook suite berlaku (lihat `suite.md`): sesi API aktor, seed API per TC, pemulihan state global di hook `after`.
- Data Pre-setup #22 s.d. #25 (kategori, brand, UoM, label) tersedia di client utama: Category leaf `IT Equipment` dan `Electronics > Laptop`, Brand `Dell`, `Lenovo`, `Toyota`, `Apple`, UoM `Unit`, `Pcs`, `Set`, Label `Finance`, `High Priority`, `Fragile`. Nilai Pre-setup mengacu ke `fixtures/fixed-asset-settings-asset-name.json` (fixture baru yang ditetapkan tim FE; tanpa password atau token).
- Data Pre-setup (hanya dibaca): Brand #23 `Dell` dan `Lenovo`.
- Data uji: model 120 karakter adalah string `M` berulang 120 kali dan model 121 karakter adalah string yang sama ditambah satu `M`; keduanya hanya diketik dan tidak pernah tersimpan (tidak ada Submit).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): tidak ada data yang dibuat; popup ditutup lewat langkah pemulihan di akhir spec.

## Test Steps

1. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
2. Pilih Brand `Dell`

### TC-FA-FAAM-131: Enter pada input model membuat badge model

3. Ketik `5420` di input model baris `Dell`, lalu tekan Enter
4. Ketik `3310`, lalu tekan Enter
5. Verifikasi Badge `3310` dan `5420` muncul urut A→Z (`3310`, `5420`) tanpa drag reorder
6. Verifikasi Input model berplaceholder `Type a model and press Enter`

### TC-FA-FAAM-132: Nama model tepat 120 karakter diterima dan 121 menampilkan error

7. Ketik model 120 karakter lalu tekan Enter
8. Verifikasi Model 120 karakter menjadi badge
9. Ketik model 121 karakter
10. Verifikasi Error inline `Max. 120 characters` muncul real-time pada input model
11. Hapus isi input model

### TC-FA-FAAM-138: Badge model yang belum dipakai dapat dihapus dengan tombol x

12. Tambahkan model `Temp 1` (ketik, tekan Enter)
13. Klik `×` pada badge `Temp 1`
14. Verifikasi Badge `Temp 1` hilang

### TC-FA-FAAM-136: Emoji pada input model diblok di level input

15. Ketik dan paste emoji `😊` di input model
16. Verifikasi Emoji tidak masuk ke input model
17. Verifikasi Tidak ada pesan error pada input model

### TC-FA-FAAM-134: Nama model yang sama pada Brand berbeda diterima

18. Pilih Brand `Lenovo`
19. Tambahkan model `X1` pada baris `Dell` (ketik, tekan Enter)
20. Tambahkan model `X1` pada baris `Lenovo` (ketik, tekan Enter)
21. Verifikasi Kedua badge `X1` diterima tanpa error duplikat
22. Pulihkan form: klik `[Clear Field]`, lalu klik `[✕]` (form bersih tertutup tanpa dialog)

## Notes

- Urutan TC dalam spec dan alasannya (S-10): badge model dasar (TC-FA-FAAM-131), batas karakter (TC-FA-FAAM-132), hapus badge (TC-FA-FAAM-138), emoji (TC-FA-FAAM-136), lalu Brand kedua (TC-FA-FAAM-134); form dibuka sekali dan Brand `Dell` dipilih sekali karena TC-FA-FAAM-131, 132, 134, 136, 138 sama-sama memakai langkah "Pilih Brand `Dell`".
- langkah "Pilih Brand `Dell`" milik TC-FA-FAAM-134 dipenuhi oleh langkah pilih Brand `Dell` di awal spec; `Dell` sudah memuat badge `3310` dan `5420` serta tidak mengganggu asersi duplikat `X1`.
- Langkah pemulihan `[Clear Field]` lalu `[✕]` (langkah terakhir) adalah langkah penghubung tanpa `Verifikasi`: form dikembalikan bersih sehingga ditutup tanpa dialog `Unsaved Changes` (S-09).
- Temuan untuk QA:
  - TC-FA-FAAM-132 tidak menyebut perilaku model 121 karakter saat Enter ditekan; spec hanya mengasersi error real-time sesuai Expected.
