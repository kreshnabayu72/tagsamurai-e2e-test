---
id: TC-AC-DC-E2E-040-edit-validasi-duplikat-dan-emoji
title: "Edit Category: Duplikat Case-insensitive, Save Duplikat, Unik Mengecualikan Diri Sendiri, dan Emoji Diblok"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DC-108
  - TC-AC-DC-109
  - TC-AC-DC-110
  - TC-AC-DC-105
coverage:
  web: automated
---

# Edit Category: Duplikat Case-insensitive, Save Duplikat, Unik Mengecualikan Diri Sendiri, dan Emoji Diblok

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1, Budi Santoso, tampil di kolom Modified By sebagai `Budi S`): `totalControlDevCat_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar).
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture BE (disediakan tim FE/BE); suite berjalan serial (`parallel: false`).
- Data Pre-setup #14 hanya dibaca dan tidak diubah: node `Hardware` dan `Handheld Reader`. Nama node Pre-setup dibaca dari fixture `Fixture.settingsDeviceCategory.*` (fixture belum ada; disediakan tim FE).
- Data Dinamis milik spec (dibuat lewat sesi API aktor di hook `before`, di bawah `Handheld Reader`; nama bersuffix `{runId}-040`): `Pemindai {runId}-040` (target Edit; namanya tidak berubah selama spec) dan `Saudara {runId}-040` (sibling yang namanya diduplikasi). Hook `after` menghapus keduanya lewat sesi API. Entri Changelog hasil seeding dan cleanup bersifat permanen dan tidak dihapus.
- Nilai uji: `  SAUDARA {runId}-040  ` (TC-108); `😊` dan `🔥` (TC-105).
- Kemampuan teknis: menempel teks dari clipboard ke input (TC-105) disediakan tim FE. Jumlah baris hasil Search pada modal Changelog dapat dibaca sebagai baseline sebelum aksi (disediakan tim FE/BE).

## Test Steps

### Baseline Changelog

1. Expand `Hardware` lalu `Handheld Reader`
2. Klik ikon Changelog pada header Sidebar Category
3. Ketik Search `{runId}-040`, tekan Enter
4. Catat jumlah baris hasil Search sebagai baseline (entri hasil seeding)
5. Klik `[×]` pada modal Changelog

### Duplikat case-insensitive setelah trim (TC-108)

6. Hover node `Pemindai {runId}-040`, klik aksi Edit
7. Ganti isi input dengan `  SAUDARA {runId}-040  `, tunggu 1 detik
8. Verifikasi pesan error inline "Category name already exists"

### Save nama duplikat (TC-109)

9. Klik `[Clear Field]`
10. Ketik `Saudara {runId}-040`, langsung klik `[Save]` sebelum validasi live selesai
11. Verifikasi pesan error inline "Category name already exists"
12. Verifikasi input tetap terbuka dengan nilai `Saudara {runId}-040` dipertahankan

### Validasi unik mengecualikan node yang sedang diedit (TC-110)

13. Klik `[Clear Field]`
14. Ketik ulang `Pemindai {runId}-040`, tunggu 1 detik
15. Verifikasi pesan error "Category name already exists" tidak tampil (anchor: kotak input terisi `Pemindai {runId}-040`)

### Emoji diblok saat diketik atau ditempel (TC-105)

16. Ketik `😊` di akhir nilai, lalu tempel `🔥` ke input
17. Verifikasi nilai input tetap `Pemindai {runId}-040`
18. Verifikasi tidak ada pesan error
19. Tekan Esc

### Pemeriksaan akhir tidak ada perubahan nama dan tidak ada entri baru

20. Verifikasi nama node tetap `Pemindai {runId}-040`
21. Klik ikon Changelog pada header Sidebar Category
22. Ketik Search `{runId}-040`, tekan Enter
23. Verifikasi jumlah baris hasil Search sama dengan baseline
24. Klik `[×]` pada modal Changelog

## Notes

- S-03, langkah penghubung: langkah 1 (membuka cabang tree), langkah 5 dan 24 (menutup modal Changelog), langkah 9 dan 13 (`[Clear Field]` sebagai pembersih error sebelum kasus berikutnya, R-12), langkah 19 (input berisi nilai tersimpan sehingga bersih; Esc menutupnya tanpa dialog, S-09).
- Urutan TC dalam spec: TC-110 sebelum TC-105 karena TC-105 mengasersi nilai input yang sama dengan nilai tersimpan; pemulihan nilai awal oleh TC-110 menjadi prasyarat TC-105.
- S-05: klausa "nama node tidak berubah dan tidak ada entri log" pada TC-109 dan TC-108 dinyatakan sebagai asersi jumlah dengan baseline (langkah 4, 20, 23), bukan asersi absence kelas g.
- Temuan untuk QA:
  - TC memakai node literal Pre-setup #14 `Rugged Scanner` sebagai target Edit dan `Barcode Handheld` sebagai sibling duplikat. Spec memakai node milik spec.
  - TC-110 mengharapkan "tidak ada error"; spec memakai kotak input terisi sebagai anchor positif karena TC tidak menyebut elemen lain.
