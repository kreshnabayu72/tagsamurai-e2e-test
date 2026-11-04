---
id: TC-AC-DS-E2E-112-changelog-modified-by-photo-snapshot-dan-no-result
title: "Modal Changelog: Modified By Format Singkat, Entri Photo Set as Default, Snapshot SKU Dihapus, Principal, dan No Result"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-383
  - TC-AC-DS-384
  - TC-AC-DS-386
  - TC-AC-DS-388
  - TC-AC-DS-390
coverage:
  web: automated
---

# Modal Changelog: Modified By Format Singkat, Entri Photo Set as Default, Snapshot SKU Dihapus, Principal, dan No Result

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima, `totalControlSku_automated_{namaCompany}@qwertysystem.net` (nama tampil `Jane Setiawan`, Modified By `Jane S`), `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca, tidak diubah): #29 (SKU Principal inti, termasuk `SFR-VEL-4P`) dan #30 (`SEED-001` sampai `SEED-119`; total 129 SKU Principal), dipasang idempoten oleh seeding di hook `before`. Riwayat Changelog Principal (#33): seed 35 entri bertanggal 01/09/26 sampai 03/10/26 (total pada modal dapat lebih besar karena entri yang ditulis spec lain; spec ini tidak memakai jumlah absolut), termasuk Edit `SFR-VEL-4P` Field `Photo — Set as default` (`Photo 1` menjadi `Photo 2`) oleh `Budi K` (nama tampil `Budi Kurniawan`, Pre-setup #2) dan Delete `UHF Handheld Reader (HHR-ARC-300)` pada 03/10/26 14:20. Riwayat Changelog Distributor PT Cakra Distribusi (#34): 3 entri Create `LOC-NOR-01`, `LOC-NOR-02`, `LOC-NOR-03` oleh `Dewi L` (disiapkan lewat seed). Entri buatan spec lain dipulihkan baseline data uji yang disediakan tim FE/BE (lihat Temuan untuk QA).
- Konfigurasi General Settings (Pre-setup #35): Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone Asia/Jakarta; hanya dibaca, tidak diubah.
- Nilai data diacu lewat `Fixture.deviceSku.<kunci>`; berkas fixture disediakan tim FE.
- Tidak ada state global yang diubah dan tidak ada entitas yang dibuat.

## Test Steps

### TC-AC-DS-383: Modified By format singkat dan tooltip

1. Klik ikon Changelog
2. Verifikasi kolom Modified By pada baris pertama menampilkan teks biasa `Jane S`
3. Hover nilai `Jane S` pada baris pertama
4. Verifikasi tooltip nama lengkap `Jane Setiawan` tampil
5. Ketik Search pada modal `SFR-VEL-4P`, tekan Enter
6. Verifikasi kolom Modified By pada baris Edit `SFR-VEL-4P` menampilkan teks biasa `Budi K`
7. Hover nilai `Budi K` pada baris Edit `SFR-VEL-4P`
8. Verifikasi tooltip nama lengkap `Budi Kurniawan` tampil
9. Pindahkan fokus keyboard ke nilai Modified By pada baris Edit `SFR-VEL-4P`
10. Verifikasi tooltip nama lengkap `Budi Kurniawan` tampil saat fokus keyboard

### TC-AC-DS-384: Entri Photo — Set as default

11. Verifikasi baris Edit `SFR-VEL-4P` menampilkan Field `Photo — Set as default`, Old Value `Photo 1`, dan New Value `Photo 2`
12. Verifikasi tidak ada nilai mentah seperti nama slot teknis pada baris itu

### TC-AC-DS-386: Empty state Search tanpa hasil

13. Ganti isi kotak search modal dengan `tidak-ada-entri`, tekan Enter
14. Verifikasi modal menampilkan ilustrasi dengan judul "No results found" dan deskripsi "Try adjusting your search or filter."

### TC-AC-DS-388: Principal hanya melihat entri SKU Principal

15. Ganti isi kotak search modal dengan `LOC-NOR`, tekan Enter
16. Verifikasi kata kunci `LOC-NOR` tidak menemukan entri: tampil "No results found"
17. Klik `(←)` pada kotak Search modal
18. Verifikasi tabel modal kembali memuat entri SKU Principal
19. Verifikasi entri SKU Distributor (Create `LOC-NOR-01`, `LOC-NOR-02`, `LOC-NOR-03` oleh `Dewi L`) tidak ikut dalam modal

### TC-AC-DS-390: Snapshot SKU yang sudah dihapus

20. Ketik Search pada modal `HHR-ARC-300`, tekan Enter
21. Verifikasi entri Delete tetap tampil dengan SKU `UHF Handheld Reader (HHR-ARC-300)` walau SKU sudah tidak ada di List
22. Klik ikon close `[✕]`

## Notes

- Langkah penghubung (S-03, R-16): langkah 5 mencari baris Edit `SFR-VEL-4P` yang tidak berada di 10 entri pertama; langkah 17 mengosongkan Search agar tabel kembali memuat seluruh entri; langkah 20 mencari entri Delete `HHR-ARC-300` (TC-AC-DS-390 "Cari entri Delete"); langkah 22 menutup modal; tanpa asersi tambahan.
- Asersi absence langkah 16 memakai empty state "No results found" sebagai anchor; langkah 12 didahului langkah 11 yang membuktikan baris itu tampil; langkah 18 (tabel kembali memuat entri SKU Principal, asersi tambahan S-03) menjadi anchor positif absence langkah 19.
- Temuan untuk QA:
  - S-12: asersi bergantung pada nama literal Pre-setup #29, #30, dan #33 (pengecualian S-12 A-11, `suite.md`); TC-AC-DS-388 tidak menyebut jumlah entri, sehingga spec tidak mengasersi jumlah halaman.
  - Fixture rancangan belum diverifikasi ada di environment: riwayat Changelog Distributor (#34) dan nama tampil `Jane Setiawan` dan `Budi Kurniawan`.
  - TC-AC-DS-390 menyebut "walau SKU sudah tidak ada di List" tanpa langkah observasi atas List; spec hanya mengasersi entri Delete di modal (HHR-ARC-300 tidak ada pada Pre-setup #29).
  - TC-AC-DS-384 Expected b ("tidak ada nilai mentah seperti nama slot teknis") tidak menyebut nilai mentah yang dimaksud; spec mengasersi bahwa Old Value dan New Value hanya `Photo 1` dan `Photo 2`.
  - Env `AC_DS_TC_PASSWORD` dan berkas fixture `Fixture.deviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE. Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag-nya belum ditetapkan.
