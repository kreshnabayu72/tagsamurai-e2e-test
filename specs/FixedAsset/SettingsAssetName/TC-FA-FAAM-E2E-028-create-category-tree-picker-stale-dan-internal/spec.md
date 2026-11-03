---
id: TC-FA-FAAM-E2E-028-create-category-tree-picker-stale-dan-internal
title: "Create: Pilih Category Leaf, Category Dihapus Sesi Lain, dan Berubah Menjadi Internal"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-102
  - TC-FA-FAAM-103
  - TC-FA-FAAM-104
coverage:
  web: automated
---

# Create: Pilih Category Leaf, Category Dihapus Sesi Lain, dan Berubah Menjadi Internal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control client utama, `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1; bagian `{namaCompany}` mengikuti penulisan Pre-setup TC), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; setiap nama didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo.
- Hook suite berlaku (lihat `suite.md`): sesi API aktor, seed API per TC, pemulihan state global di hook `after`.
- Data Pre-setup #22 s.d. #25 (kategori, brand, UoM, label) tersedia di client utama: Category leaf `IT Equipment` dan `Electronics > Laptop`, Brand `Dell`, `Lenovo`, `Toyota`, `Apple`, UoM `Unit`, `Pcs`, `Set`, Label `Finance`, `High Priority`, `Fragile`. Nilai Pre-setup mengacu ke `fixtures/fixed-asset-settings-asset-name.json` (fixture baru yang ditetapkan tim FE; tanpa password atau token).
- Data Dinamis (seed API di hook `before`, suffix per run dan nomor spec): Category leaf `Temp Category 103 {runId}-028` (Pre-setup #22b) dan Category leaf `Temp Leaf 104 {runId}-028` (Pre-setup #22c). Asset Name `Create Min Item {runId}-028` hanya diketik dan tidak tersimpan (Submit selalu ditolak).
- Kemampuan teknis (disediakan tim BE/FE): pelaku kedua lewat sesi API aktor menghapus Category dan menambahkan subcategory pada Category leaf; TC sumber menandai kedua TC sebagai dua sesi paralel, di spec ini dipicu lewat sesi API karena sesi UI kedua tidak diasersi (tanpa konteks UI kedua).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Category `Temp Category 103 {runId}-028` dan `Temp Leaf 104 {runId}-028` beserta subcategory-nya bila masih ada.

## Test Steps

### TC-FA-FAAM-102: Memilih Category leaf lewat Tree Picker menampilkan teks breadcrumb

1. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
2. Klik `[Select Category]`
3. Pilih leaf `Laptop`
4. Klik `[Select]`
5. Verifikasi Tombol tetap berlabel `Select Category`
6. Verifikasi Teks di samping tombol menampilkan breadcrumb read-only `Electronics > Laptop`

### TC-FA-FAAM-103: Category yang dihapus sesi lain ditolak saat Submit dan field ter-clear

7. Isi Asset Name `Create Min Item {runId}-028`
8. Klik `[Select Category]`, pilih leaf `Temp Category 103 {runId}-028`, klik `[Select]`
9. Pilih TAG Type `QR`
10. Pilih Brand `Dell`
11. Pilih UoM `Unit`
12. Hapus Category `Temp Category 103 {runId}-028` lewat sesi API aktor kedua hingga penghapusan tersimpan
13. Klik `[Submit]`
14. Verifikasi Error inline `This category no longer exists. Please select another.` tampil
15. Verifikasi Field Category ter-clear (teks `No category selected`)
16. Verifikasi Field lain (Asset Name, TAG Type, Brand, UoM) tetap terisi

### TC-FA-FAAM-104: Category yang berubah menjadi internal sebelum Submit ditolak dengan pesan khusus

17. Klik `[Select Category]`, pilih leaf `Temp Leaf 104 {runId}-028`, klik `[Select]` (field wajib lain tetap terisi dari TC-FA-FAAM-103)
18. Tambahkan subcategory pada `Temp Leaf 104 {runId}-028` lewat sesi API aktor kedua hingga subcategory tersimpan
19. Klik `[Submit]`
20. Verifikasi Error inline `This category can no longer be selected. Please select another.` tampil
21. Verifikasi Field Category ter-clear (teks `No category selected`)
22. Pulihkan form: klik `[Clear Field]`, lalu klik `[✕]` (form bersih tertutup tanpa dialog)

## Notes

- TC-FA-FAAM-104 melanjutkan form TC-FA-FAAM-103: Asset Name, TAG Type, Brand, dan UoM masih terisi, jadi hanya Category yang dipilih ulang. Bila TC-FA-FAAM-103 gagal, TC-FA-FAAM-104 ikut gagal (dependensi urutan).
- Pelaku kedua memakai sesi API (bukan konteks UI kedua), jadi `P-2` tidak dipakai (keputusan 2026-10-30). Mekanisme API untuk menghapus Category dan menambah subcategory tidak disebut TC; disediakan tim BE/FE tanpa endpoint karangan (S-13).
- Langkah pemulihan `[Clear Field]` lalu `[✕]` (langkah terakhir) adalah langkah penghubung tanpa `Verifikasi`: form dikembalikan bersih sehingga ditutup tanpa dialog `Unsaved Changes` (S-09).
- Temuan untuk QA:
  - TC-FA-FAAM-103 dan 104 berlabel Automation "Manual Only (d) dua sesi paralel", sedangkan spec memicunya lewat sesi API aktor; label TC perlu disamakan bila sesi UI kedua memang diwajibkan.
  - TC-FA-FAAM-103 dan 104 tidak menyebut Data Uji field wajib lain; spec memakai nilai Data Uji TC-FA-FAAM-81 (TAG Type `QR`, Brand `Dell`, UoM `Unit`).
