---
id: TC-FA-FAAM-E2E-032-create-brand-tabel-model-per-brand
title: "Create: Pilih Brand, Tabel Model/Type per Brand, Deselect, dan Brand Dihapus Sesi Lain"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-128
  - TC-FA-FAAM-129
  - TC-FA-FAAM-130
coverage:
  web: automated
---

# Create: Pilih Brand, Tabel Model/Type per Brand, Deselect, dan Brand Dihapus Sesi Lain

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control client utama, `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1; bagian `{namaCompany}` mengikuti penulisan Pre-setup TC), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; setiap nama didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo.
- Hook suite berlaku (lihat `suite.md`): sesi API aktor, seed API per TC, pemulihan state global di hook `after`.
- Data Pre-setup #22 s.d. #25 (kategori, brand, UoM, label) tersedia di client utama: Category leaf `IT Equipment` dan `Electronics > Laptop`, Brand `Dell`, `Lenovo`, `Toyota`, `Apple`, UoM `Unit`, `Pcs`, `Set`, Label `Finance`, `High Priority`, `Fragile`. Nilai Pre-setup mengacu ke `fixtures/fixed-asset-settings-asset-name.json` (fixture baru yang ditetapkan tim FE; tanpa password atau token).
- Data Pre-setup (hanya dibaca): Brand #23 `Dell`, `Lenovo`, `Apple`, `Toyota`.
- Data Dinamis (seed API di hook `before`, suffix per run dan nomor spec): Brand `Temp Brand 130 {runId}-032` (Pre-setup #23b). Tidak ada Asset Name yang tersimpan (Submit selalu ditolak).
- Kemampuan teknis (disediakan tim BE/FE): pelaku kedua lewat sesi API aktor menghapus Brand.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Brand `Temp Brand 130 {runId}-032` bila masih ada.

## Test Steps

1. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka

### TC-FA-FAAM-128: Memilih Brand memunculkan tabel Model/Type per Brand berurut A→Z

2. Buka dropdown Brand
3. Verifikasi Opsi dropdown Brand berurutan A→Z: `Apple` tampil sebelum `Dell` dan `Dell` sebelum `Lenovo`
4. Pilih Brand `Toyota`, lalu pilih Brand `Dell`
5. Verifikasi Tabel dengan header `Brand | Model/Type | Action (🗑)` muncul
6. Verifikasi Baris tabel urut A→Z menurut nama Brand: `Dell`, `Toyota`
7. Verifikasi Chip Brand urut A→Z

### TC-FA-FAAM-129: Deselect chip Brand menghapus baris Brand di tabel

8. Klik `(✕)` chip `Toyota`
9. Verifikasi Baris `Toyota` hilang dari tabel
10. Verifikasi Baris `Dell` tetap

### TC-FA-FAAM-130: Brand yang dihapus sesi lain

11. Isi Asset Name `Create Min Item {runId}-032`
12. Klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`
13. Pilih TAG Type `QR`
14. Pilih UoM `Unit`
15. Pilih Brand `Temp Brand 130 {runId}-032` (Brand `Dell` sudah terpilih)
16. Hapus Brand `Temp Brand 130 {runId}-032` lewat sesi API aktor kedua hingga penghapusan tersimpan
17. Klik `[Submit]`
18. Verifikasi Error inline `Temp Brand 130 {runId}-032 no longer exists. Please select another.` tampil
19. Verifikasi Chip `Temp Brand 130 {runId}-032` dikosongkan
20. Verifikasi Chip `Dell` bertahan
21. Pulihkan form: klik `[Clear Field]`, lalu klik `[✕]` (form bersih tertutup tanpa dialog)

## Notes

- TC-FA-FAAM-129 melanjutkan form TC-FA-FAAM-128 (Brand `Dell` dan `Toyota` sudah terpilih, langkah pilih Brand milik TC-FA-FAAM-129 dipenuhi oleh langkah pilih Brand TC-FA-FAAM-128); TC-FA-FAAM-130 melanjutkan dengan `Dell` yang tersisa.
- Pelaku kedua lewat sesi API aktor (bukan konteks UI kedua), jadi `P-2` tidak dipakai; mekanisme penghapusan Brand disediakan tim BE/FE tanpa endpoint karangan (S-13).
- Langkah pemulihan `[Clear Field]` lalu `[✕]` (langkah terakhir) adalah langkah penghubung tanpa `Verifikasi`: form dikembalikan bersih sehingga ditutup tanpa dialog `Unsaved Changes` (S-09).
- Temuan untuk QA:
  - TC-FA-FAAM-130 berlabel "Manual Only (d) dua sesi paralel"; spec memicu penghapusan lewat sesi API aktor.
  - TC-FA-FAAM-130 tidak menyebut Data Uji field wajib lain; spec memakai nilai Data Uji TC-FA-FAAM-81.
