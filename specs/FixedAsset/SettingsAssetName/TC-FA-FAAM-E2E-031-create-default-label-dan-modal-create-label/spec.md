---
id: TC-FA-FAAM-E2E-031-create-default-label-dan-modal-create-label
title: "Create: Default Label, Tombol [➕], Modal Create Label, dan Label Dihapus Sesi Lain"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-122
  - TC-FA-FAAM-123
  - TC-FA-FAAM-124
  - TC-FA-FAAM-125
  - TC-FA-FAAM-126
coverage:
  web: automated
---

# Create: Default Label, Tombol [➕], Modal Create Label, dan Label Dihapus Sesi Lain

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control client utama, `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1; bagian `{namaCompany}` mengikuti penulisan Pre-setup TC), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun ini adalah akun default suite sehingga hook `after` tidak perlu memulihkan sesi.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; setiap nama didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo.
- Hook suite berlaku (lihat `suite.md`): sesi API aktor, seed API per TC, pemulihan state global di hook `after`.
- Data Pre-setup #22 s.d. #25 (kategori, brand, UoM, label) tersedia di client utama: Category leaf `IT Equipment` dan `Electronics > Laptop`, Brand `Dell`, `Lenovo`, `Toyota`, `Apple`, UoM `Unit`, `Pcs`, `Set`, Label `Finance`, `High Priority`, `Fragile`. Nilai Pre-setup mengacu ke `fixtures/fixed-asset-settings-asset-name.json` (fixture baru yang ditetapkan tim FE; tanpa password atau token).
- Data Dinamis (suffix per run dan nomor spec): Label `Temp Label 126 {runId}-031` (seed API, Pre-setup #25e); Asset Name `Label Keep {runId}-031` hanya diketik dan tidak tersimpan; Label baru yang dibuat spec: `New Tag Label {runId}-031` dan `Stay Label {runId}-031`. Label Pre-setup #25 `Finance` dipakai sebagai label yang bertahan (hanya dibaca).
- Kemampuan teknis (disediakan tim BE/FE): pelaku kedua lewat sesi API aktor menghapus Label `Temp Label 126 {runId}-031`.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Label `Temp Label 126 {runId}-031`, `New Tag Label {runId}-031`, dan `Stay Label {runId}-031` bila masih ada.

## Test Steps

1. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka

### TC-FA-FAAM-122: Default Label opsional dan opsinya berbadge warna A→Z

2. Buka dropdown Default Label
3. Verifikasi Opsi label tampil dengan badge warna aslinya, urut A→Z
4. Verifikasi Field Default Label boleh dikosongkan (caption tanpa tanda wajib `*`)
5. Tutup dropdown Default Label

### TC-FA-FAAM-123, 124: Modal Create Label dan label baru

6. Isi Asset Name `Label Keep {runId}-031`
7. Klik `[➕]` di Default Label
8. Verifikasi Modal Create Label milik modul labeling terbuka
9. Buat label `New Tag Label {runId}-031`, klik `[Submit]` pada modal label
10. Buka dropdown Default Label
11. Verifikasi Label `New Tag Label {runId}-031` muncul di opsi dropdown Default Label
12. Verifikasi Label `New Tag Label {runId}-031` tidak otomatis terpilih
13. Verifikasi Asset Name `Label Keep {runId}-031` dan isian lain tetap ada
14. Tutup dropdown Default Label

### TC-FA-FAAM-125: Modal Create Label dengan Stay on this form aktif

15. Klik `[➕]`
16. Centang `Stay on this form after submitting` pada modal label lalu Submit label `Stay Label {runId}-031`
17. Verifikasi Form label di-reset dan modal label tetap terbuka
18. Tutup modal label
19. Buka dropdown Default Label
20. Verifikasi `Stay Label {runId}-031` ada di opsi Default Label
21. Tutup dropdown Default Label

### TC-FA-FAAM-126: Label yang dihapus sesi lain

22. Isi field wajib lengkap: Category (klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`), TAG Type `QR`, Brand `Dell`, UoM `Unit`
23. Pilih Default Label `Temp Label 126 {runId}-031` dan `Finance`
24. Hapus label `Temp Label 126 {runId}-031` lewat sesi API aktor kedua hingga penghapusan tersimpan
25. Klik `[Submit]`
26. Verifikasi Error inline `Temp Label 126 {runId}-031 no longer exists. Please select another.` tampil
27. Verifikasi Chip `Temp Label 126 {runId}-031` dikosongkan
28. Verifikasi Chip `Finance` bertahan
29. Pulihkan form: klik `[Clear Field]`, lalu klik `[✕]` (form bersih tertutup tanpa dialog)

## Notes

- TC-FA-FAAM-123 dan 124 berbagi satu pembukaan Modal Create Label (pembuatan label pada TC-FA-FAAM-124 melanjutkan modal yang dibuka TC-FA-FAAM-123); Asset Name `Label Keep` diisi lebih dahulu mengikuti TC-FA-FAAM-124 langkah 2.
- TC-FA-FAAM-126 melanjutkan form yang sama: Asset Name `Label Keep` sudah terisi, field wajib lain diisi di langkah ini. Submit selalu ditolak sehingga tidak ada Asset Name tersimpan.
- Penutupan dropdown dan modal label adalah langkah penghubung tanpa `Verifikasi` (S-03); modal label `Stay Label` ditutup tanpa dialog karena form label di-reset.
- Pelaku kedua lewat sesi API aktor (bukan konteks UI kedua), jadi `P-2` tidak dipakai; mekanisme penghapusan Label disediakan tim BE/FE tanpa endpoint karangan (S-13).
- Langkah pemulihan `[Clear Field]` lalu `[✕]` (langkah terakhir) adalah langkah penghubung tanpa `Verifikasi`: form dikembalikan bersih sehingga ditutup tanpa dialog `Unsaved Changes` (S-09).
- Temuan untuk QA:
  - TC-FA-FAAM-124 menulis "buat label `New Tag Label`" tanpa field wajib Modal Create Label (milik modul labeling); spec mengikuti tanpa menebak isi field, rujukan detail modal ada di modul asset-labeling.
  - TC-FA-FAAM-126 berlabel "Manual Only (d) dua sesi paralel"; spec memicu penghapusan lewat sesi API aktor.
