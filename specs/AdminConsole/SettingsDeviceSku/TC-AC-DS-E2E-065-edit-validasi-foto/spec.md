---
id: TC-AC-DS-E2E-065-edit-validasi-foto
title: "Edit SKU: Validasi Foto Batas Dua, Resize di Atas 1 MB, dan Format File Picker"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DS-226
  - TC-AC-DS-227
  - TC-AC-DS-228
coverage:
  web: automated
---

# Edit SKU: Validasi Foto Batas Dua, Resize di Atas 1 MB, dan Format File Picker

## Prerequisites

- Mode: FE+BE.
- Akun (password hanya lewat env; semua nama env `AC_DS_*` belum terdaftar di `spectra.config.ts` dan `.env.example`, disediakan tim FE; email akun berbeda dari akun Admin Console lain):

| Peran dalam spec | Email | Env var password |
|---|---|---|
| Aktor utama: Total Control Principal PT Arunika Prima, `Jane Setiawan` (Pre-setup #1) | `totalControlSku_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_TC_PASSWORD` |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (`before`, `beforeEach`, `after`) dinyatakan di `suite.md`; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal).
- Data Pre-setup (dibaca untuk atribut seed, tidak diubah): pohon Category (#25), Device Name (#26), Brand (#27), file foto (#37).
- File foto: `foto-c.jpeg` (150 KB), `foto-besar.jpg` (3 MB), `dokumen.gif` (format tidak didukung) dari Pre-setup #37.
- Data milik spec (S-06, S-12), di-seed idempotent di hook `before` lewat sesi API aktor dan fixture BE yang disediakan tim FE/BE, dihapus di hook `after`: SKU `EDT-{runId}-065` (stok 0, 1 foto, atribut menyamai SKU Pre-setup `HHR-ARC-200`) untuk TC-227 dan TC-228, dan SKU `EDT-{runId}-065-2P` (stok 0, 2 foto dengan foto kedua default, atribut menyamai SKU Pre-setup `HHR-ARC-100`) untuk TC-226. SKU Pre-setup `HHR-ARC-100` dan `HHR-ARC-200` tidak diubah. Efek yang tidak dapat dipulihkan: entri audit trail (Changelog, System Log, Activity Log) bertambah permanen.
- Kemampuan teknis: Pembacaan filter file picker native dan percobaan memilih `dokumen.gif` pada file picker disediakan tim FE (TC tidak memberi caranya; lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`) sesuai `suite.md`.
- Sumber nilai data: Pre-setup TC (#25 sampai #43); berkas `fixtures/settings-device-sku.json` belum ada dan disediakan tim FE dengan kunci mengikuti Pre-setup #29 dan #30 (ditandai di Notes).

## Test Steps

1. Ketik Search `EDT-{runId}-065`, tekan Enter
2. Klik `⋯` pada baris `EDT-{runId}-065-2P`, lalu pilih `Edit`

### TC-AC-DS-226: foto ketiga diblok

3. Coba mengunggah `foto-c.jpeg` sebagai foto ketiga
4. Verifikasi pesan "Maximum 2 photos" tampil
5. Verifikasi foto ketiga tidak ditambahkan
6. Verifikasi kedua foto tersimpan tetap ada
7. Klik `✕` pada header popup Edit SKU
8. Klik `⋯` pada baris `EDT-{runId}-065`, lalu pilih `Edit`

### TC-AC-DS-228: file picker hanya JPG, PNG, JPEG

9. Klik slot Photo kedua sehingga file picker terbuka
10. Verifikasi file picker hanya menampilkan file JPG, PNG, dan JPEG
11. Coba memilih `dokumen.gif`
12. Verifikasi `dokumen.gif` tidak dapat dipilih
13. Verifikasi tidak ada pesan error format

### TC-AC-DS-227: file lebih dari 1 MB di-resize

14. Ganti foto dengan `foto-besar.jpg` (3 MB)
15. Verifikasi tidak ada pesan error ukuran
16. Klik `[Save]`
17. Verifikasi muncul toast sukses "Success, device SKU has been updated."

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`; subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan: TC-228 (negatif) dijalankan sebelum TC-227 (menyimpan) pada popup `EDT-{runId}-065` yang sama (S-10). Langkah 7 menutup popup bersih tanpa dialog.
- Langkah penghubung: Search pada langkah 1 menemukan baris milik spec `EDT-{runId}-065` dan `EDT-{runId}-065-2P` (R-16).
- Post Condition "perubahan tersimpan" dan "entri log tercatat di Changelog, System Log aktor, dan Activity Log" tidak diasersi di spec ini karena TC tidak memberi langkah observasinya; pencatatan log diuji di spec log tiga surface.
- Temuan untuk QA: TC-228 tidak menyatakan cara mengamati filter file picker native dan cara "mencoba memilih" file yang tidak ada dalam daftar; spec mengikuti TC dan kemampuan itu disediakan tim FE. TC-227 menyebut "Ganti foto" pada SKU satu foto tanpa menyatakan slot; spec memakai slot Photo pertama.
- Temuan untuk QA (S-06/S-12): TC-226, TC-227, dan TC-228 menulis atau membuka SKU Pre-setup `HHR-ARC-100` dan `HHR-ARC-200`; spec memakai SKU milik spec bersuffix `{runId}` berkonfigurasi sama (TC-227 menyimpan foto, yang bukan Pre-setup yang dipaksa), sehingga SKU Pre-setup dan Last Modified-nya tidak berubah. TC-226 membutuhkan SKU dua foto dan TC-228 membutuhkan slot Photo kedua kosong, sehingga dua SKU milik spec dipakai.
- Temuan untuk QA (fixture): `fixtures/settings-device-sku.json`, akun Pre-setup #1 dan #2, dan env `AC_DS_*` belum terverifikasi ada di environment; ketersediaannya dipastikan tim FE.
