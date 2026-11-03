---
id: TC-FA-TAG-E2E-352-defense-in-depth-izin-dicabut-saat-dialog-print-qr-dan-halaman-terbuka
title: "Defense-in-Depth: Izin Update Dicabut saat Dialog Print QR Terbuka dan saat Halaman Terbuka, Aksi Tulis Hidden Sesudah Muat Ulang"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1284
  - TC-FA-TAG-1313
coverage:
  web: automated
---

# Defense-in-Depth: Izin Update Dicabut saat Dialog Print QR Terbuka dan saat Halaman Terbuka, Aksi Tulis Hidden Sesudah Muat Ulang

## Prerequisites

- Mode: FE+BE.
- Tabel "Role yang diuji" (tiap blok akun memakai langkah berbeda, ditulis per blok):

| Blok | Role (persis dari Precondition TC) | Akun | Env password |
|---|---|---|---|
| 1 | Manage asset & TAG (Read + Update) dengan Update pada Group Plant A | `manageAssetTagReadUpdateDenganUpdatePadaGroupPlantA_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MU_UPA_PASSWORD` |
| 2 | Manage asset & TAG (Read + Update) (Update: Plant A) | `manageAssetTagReadUpdateUpdatePlantA_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MU_PA_PASSWORD` |

  Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Akun aktor pertama: blok 1. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Spec selesai di akun blok 2; hook `after` mengembalikan sesi ke akun default suite (Total Control). Langkah ganti akun ditulis eksplisit (Logout lalu Login).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) pelaku kedua (Admin) lewat sesi API (login API password, tidak dihitung sebagai sesi web; lihat `suite.md`) yang mencabut dan memulihkan akses Update pengguna di Settings > Role & Permission, tanpa asersi di sesinya; akun Admin disediakan tim FE; (2) pengamatan dialog cetak browser (untuk memastikan dialog tidak terbuka); (3) seed dan pemulihan idempotent lewat fixture backend; (4) penanganan dialog `beforeunload` (konfirmasi otomatis saat halaman dimuat ulang dengan dialog dirty terbuka), dipakai untuk menutup dialog dirty lewat muat ulang halaman; (5) satu reader RFID/NFC tersambung, driver terpasang, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader sebagai precondition TC-FA-TAG-1284 (tidak diasersi). Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Grup tab Paired | 'Excavator 20 Ton' / Plant A / RFID / Total 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; 'Excavator 20 Ton' / Plant B / RFID / 20 / 2 / 5 / 0; 'Laptop Pro 14' / HQ / NFC, QR / 25 / 1 / 0 / 2; 'Forklift Manual' / Plant A / Non TAG / 10 / 0 / 3 / 0 | `grupPaired` |
| Quantity Print QR | 2 | `qtyPrint` |

- State yang diubah dan pemulihannya: akses Update pengguna blok 1 dicabut di langkah 2 dan dipulihkan di langkah 7; Update Plant A pengguna blok 2 dicabut di langkah 11 dan dipulihkan di langkah 17. Hook `after` memulihkan capability pengguna dan sesi walau spec gagal di tengah.

## Test Steps

### Blok 1: Update pada Group Plant A (TC-FA-TAG-1284)

1. Klik tombol `Print QR`
2. Pelaku kedua (Admin) mencabut akses Update pengguna di Settings > Role & Permission lewat sesi API hingga tersimpan
3. Isi `Quantity` dengan 2
4. Klik [Start Print]
5. Verifikasi dialog cetak browser tidak terbuka
6. Verifikasi server menolak permintaan
7. Pelaku kedua memulihkan akses Update pengguna lewat sesi API hingga tersimpan
8. Muat ulang halaman (F5)

### Blok 2: Update Plant A (TC-FA-TAG-1313)

9. Logout dari akun Update pada Group Plant A, lalu Login sebagai akun Manage asset & TAG (Read + Update) (Update: Plant A)
10. Buka Fixed Asset > TAG > Paired
11. Pelaku kedua (Admin) mencabut Update Plant A pengguna lewat sesi API hingga tersimpan
12. Muat ulang tab Paired (F5)
13. Verifikasi tombol `Replace TAG` dan `Print QR` Hidden pada Table Tools
14. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
15. Buka kebab aset pada baris 'Excavator 20 Ton - 220'
16. Verifikasi kebab aset tidak memuat aksi tulis
17. Pelaku kedua memulihkan Update Plant A pengguna lewat sesi API hingga tersimpan

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1284, 1313). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: TC-FA-TAG-1281 s.d. 1283 ada di spec 327 dan TC-FA-TAG-1303 s.d. 1305 ada di spec 328 (izin dicabut saat dialog Replace, Pair, Receive, Receive Manually, dan Decline Report terbuka).
- Pelaku kedua memakai sesi API (keputusan 2026-10-21/30): bukan konteks kedua kelas c dan tidak memakai `P-2`; langkah pemicunya ditulis "... hingga ... tersimpan" (langkah 2, 7, 11, 17).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 7 dan 17 (memulihkan capability), 8 (muat ulang halaman untuk menutup dialog Print QR dirty; dialog `beforeunload` ditangani sesuai Prerequisites), 9 (ganti akun), 10 (membuka halaman sesudah login akun lain), 14 dan 15 (membuka Popup Detail dan kebab aset yang diamati TC-FA-TAG-1313).
- Temuan untuk QA:
  - TC-FA-TAG-1284 menulis Expected butir a ("Dialog cetak browser tidak terbuka") sebelum butir b ("Server menolak permintaan"); spec mengikuti urutan itu.
  - Post Condition TC-FA-TAG-1284 ("Tidak ada kode QR yang dibuat") tanpa langkah observasi di TC tidak diasersi.
  - TC-FA-TAG-1313 menyebut "Periksa Table Tools" untuk Expected butir a; spec mengasersi tombol `Replace TAG` dan `Print QR` Hidden tanpa menambah asersi lain.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
