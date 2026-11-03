---
id: TC-FA-FAAM-E2E-035-create-uom-opsi-dan-dihapus-sesi-lain
title: "Create: Opsi UoM Single-Select dan UoM Dihapus Sesi Lain"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-140
  - TC-FA-FAAM-141
coverage:
  web: automated
---

# Create: Opsi UoM Single-Select dan UoM Dihapus Sesi Lain

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control client utama, `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1; bagian `{namaCompany}` mengikuti penulisan Pre-setup TC), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; setiap nama didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo.
- Hook suite berlaku (lihat `suite.md`): sesi API aktor, seed API per TC, pemulihan state global di hook `after`.
- Data Pre-setup #22 s.d. #25 (kategori, brand, UoM, label) tersedia di client utama: Category leaf `IT Equipment` dan `Electronics > Laptop`, Brand `Dell`, `Lenovo`, `Toyota`, `Apple`, UoM `Unit`, `Pcs`, `Set`, Label `Finance`, `High Priority`, `Fragile`. Nilai Pre-setup mengacu ke `fixtures/fixed-asset-settings-asset-name.json` (fixture baru yang ditetapkan tim FE; tanpa password atau token).
- Data Pre-setup (hanya dibaca): UoM #24 `Unit`, `Pcs`, `Set`.
- Data Dinamis (seed API di hook `before`, suffix per run dan nomor spec): UoM `Temp UoM 141 {runId}-035` (Pre-setup #24b). Asset Name `Create Min Item {runId}-035` hanya diketik dan tidak tersimpan (Submit ditolak).
- Kemampuan teknis (disediakan tim BE/FE): pelaku kedua lewat sesi API aktor menghapus UoM.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API UoM `Temp UoM 141 {runId}-035` bila masih ada.

## Test Steps

### TC-FA-FAAM-140: Opsi UoM menampilkan Unit Name urut A→Z dengan single-select

1. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
2. Verifikasi Field UoM menampilkan placeholder `Select UoM`
3. Buka dropdown UoM
4. Verifikasi Opsi UoM menampilkan Unit Name (`Pcs`, `Set`, `Unit`) bukan Symbol, urut A→Z
5. Verifikasi Dropdown UoM single-select
6. Tutup dropdown UoM

### TC-FA-FAAM-141: UoM yang dihapus sesi lain ditolak dan field ter-clear

7. Isi Asset Name `Create Min Item {runId}-035`
8. Klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`
9. Pilih TAG Type `QR`
10. Pilih Brand `Dell`
11. Pilih UoM `Temp UoM 141 {runId}-035`
12. Hapus UoM `Temp UoM 141 {runId}-035` lewat sesi API aktor kedua hingga penghapusan tersimpan
13. Klik `[Submit]`
14. Verifikasi Error inline `This UoM no longer exists. Please select another.` tampil
15. Verifikasi Field UoM ter-clear
16. Pulihkan form: klik `[Clear Field]`, lalu klik `[✕]` (form bersih tertutup tanpa dialog)

## Notes

- Opsi `Temp UoM 141 {runId}-035` ikut tampil di dropdown UoM karena seeding TC-FA-FAAM-141 di hook `before`; asersi urutan memakai `Pcs`, `Set`, `Unit` saja (Pcs sebelum Set dan Set sebelum Unit).
- Pelaku kedua lewat sesi API aktor (bukan konteks UI kedua), jadi `P-2` tidak dipakai; mekanisme penghapusan UoM disediakan tim BE/FE tanpa endpoint karangan (S-13).
- Langkah pemulihan `[Clear Field]` lalu `[✕]` (langkah terakhir) adalah langkah penghubung tanpa `Verifikasi`: form dikembalikan bersih sehingga ditutup tanpa dialog `Unsaved Changes` (S-09).
- Temuan untuk QA:
  - TC-FA-FAAM-141 berlabel "Manual Only (d) dua sesi paralel"; spec memicu penghapusan lewat sesi API aktor.
  - TC-FA-FAAM-141 tidak menyebut Data Uji field wajib lain; spec memakai nilai Data Uji TC-FA-FAAM-81.
