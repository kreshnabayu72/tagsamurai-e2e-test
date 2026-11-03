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
- Data Pre-setup: SKU inti dan seed (#29, #30), pohon Category (#25), Device Name (#26), Brand (#27), file foto (#37).
- File foto: `foto-c.jpeg` (150 KB), `foto-besar.jpg` (3 MB), `dokumen.gif` (format tidak didukung) dari Pre-setup #37.
- Pemulihan: hook `before` menyiapkan secara idempotent (dilewati bila sudah ada) dan hook `after` memulihkan ke keadaan awal Pre-setup lewat fixture BE yang disediakan tim FE/BE: baris `HHR-ARC-100` (2 foto, foto kedua default) dan baris `HHR-ARC-200` (1 foto) ke jumlah dan urutan foto Pre-setup #29. Efek yang tidak dapat dipulihkan: entri audit trail (Changelog, System Log, Activity Log) bertambah permanen.
- Kemampuan teknis: Pembacaan filter file picker native dan percobaan memilih `dokumen.gif` pada file picker disediakan tim FE (TC tidak memberi caranya; lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`) karena spec memakai data SKU bersama dan nama literal Pre-setup (lihat Notes).
- Sumber nilai data: Pre-setup TC (#25 sampai #43); berkas `fixtures/settings-device-sku.json` belum ada dan disediakan tim FE dengan kunci mengikuti Pre-setup #29 dan #30 (ditandai di Notes).

## Test Steps

1. Klik `⋯` pada baris `HHR-ARC-100`, lalu pilih `Edit`

### TC-AC-DS-226: foto ketiga diblok

2. Coba mengunggah `foto-c.jpeg` sebagai foto ketiga
3. Verifikasi pesan "Maximum 2 photos" tampil
4. Verifikasi foto ketiga tidak ditambahkan
5. Verifikasi kedua foto tersimpan tetap ada
6. Klik `✕` pada header popup Edit SKU
7. Klik `⋯` pada baris `HHR-ARC-200`, lalu pilih `Edit`

### TC-AC-DS-228: file picker hanya JPG, PNG, JPEG

8. Klik slot Photo kedua sehingga file picker terbuka
9. Verifikasi file picker hanya menampilkan file JPG, PNG, dan JPEG
10. Coba memilih `dokumen.gif`
11. Verifikasi `dokumen.gif` tidak dapat dipilih
12. Verifikasi tidak ada pesan error format

### TC-AC-DS-227: file lebih dari 1 MB di-resize

13. Ganti foto dengan `foto-besar.jpg` (3 MB)
14. Verifikasi tidak ada pesan error ukuran
15. Klik `[Save]`
16. Verifikasi muncul toast sukses "Success, device SKU has been updated."

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`; subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan: TC-228 (negatif) dijalankan sebelum TC-227 (menyimpan) pada popup `HHR-ARC-200` yang sama (S-10). Langkah 6 menutup popup bersih tanpa dialog.
- Post Condition "perubahan tersimpan" dan "entri log tercatat di Changelog, System Log aktor, dan Activity Log" tidak diasersi di spec ini karena TC tidak memberi langkah observasinya; pencatatan log diuji di spec log tiga surface.
- Temuan untuk QA: TC-228 tidak menyatakan cara mengamati filter file picker native dan cara "mencoba memilih" file yang tidak ada dalam daftar; spec mengikuti TC dan kemampuan itu disediakan tim FE. TC-227 menyebut "Ganti foto" pada SKU satu foto tanpa menyatakan slot; spec memakai slot Photo pertama.
- Temuan untuk QA (S-12): Lampiran A tidak punya butir untuk modul ini, padahal asersi bergantung pada nama literal Pre-setup #29 dan #30 (mis. `HHR-ARC-200`, `SEED-001`, total 129 SKU). Spec memakai nama literal itu sesuai TC; syarat seeding idempotent, cleanup oleh spec, dan suite serial dipenuhi lewat Pemulihan di Prerequisites. Pengecualian S-12 dan S-06 untuk modul ini belum diputuskan; suite.md belum menyatakan fixture pemulihan Pre-setup.
- Temuan untuk QA (fixture): `fixtures/settings-device-sku.json`, akun Pre-setup #1 dan #2, dan env `AC_DS_*` belum terverifikasi ada di environment; ketersediaannya dipastikan tim FE.
