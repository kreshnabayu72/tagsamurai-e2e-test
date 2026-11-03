---
id: TC-AC-DS-E2E-113-changelog-empty-state-dan-scope-distributor
title: "Modal Changelog: Empty State Principal Tanpa SKU dan Scope Distributor Hanya Entri Miliknya"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-385
  - TC-AC-DS-389
coverage:
  web: automated
---

# Modal Changelog: Empty State Principal Tanpa SKU dan Scope Distributor Hanya Entri Miliknya

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal Tanpa SKU, `totalControlFresh_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_FRESH_PASSWORD` (Pre-setup #21; belum ada SKU dan belum ada entri Changelog). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun aktor kedua (langkah 6): Total Control Distributor PT Cakra Distribusi, Local Registration aktif, `totalControlDist_automated_{namaCompany}@qwertysystem.net` (nama tampil `Dewi Lestari`, Modified By `Dewi L`), `Spectra.env.AC_DS_DIST_PASSWORD` (Pre-setup #10). Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal PT Arunika Prima).
- Data Pre-setup (hanya dibaca, tidak diubah): #33 (Changelog Principal, memuat entri `HHR-...` yang tidak boleh terlihat Distributor), #31 (SKU lokal Distributor PT Cakra Distribusi `LOC-NOR-01`, `LOC-NOR-02`, `LOC-NOR-03`), dan #34 (Changelog Distributor PT Cakra Distribusi: 3 entri Create `Rugged Handheld Reader (LOC-NOR-01)`, `BLE Gateway (LOC-NOR-02)`, `Wearable TAG (LOC-NOR-03)` oleh `Dewi L` pada 05/10/26, disiapkan lewat seed). Dipasang idempoten oleh seeding di hook `before`.
- Nilai data diacu lewat `Fixture.deviceSku.<kunci>`; berkas fixture disediakan tim FE (lihat Temuan untuk QA).
- Tidak ada state global yang diubah dan tidak ada entitas yang dibuat.

## Test Steps

### TC-AC-DS-385: Empty state Principal Tanpa SKU

1. Klik ikon Changelog
2. Verifikasi modal menampilkan ilustrasi dengan judul "No changelog yet" dan deskripsi "Activities and changes will appear here."
3. Verifikasi Table Tools modal tetap tampil
4. Verifikasi tabel tidak menampilkan baris
5. Klik ikon close `[✕]`

### TC-AC-DS-389: Distributor hanya melihat entri miliknya

6. Ganti akun: Logout dari Total Control Principal Tanpa SKU, lalu login sebagai Total Control Distributor PT Cakra Distribusi (`totalControlDist_automated_{namaCompany}@qwertysystem.net`)
7. Buka halaman `Settings > Device > Device SKU`
8. Klik ikon Changelog
9. Verifikasi modal memuat 3 entri Create (`Rugged Handheld Reader (LOC-NOR-01)`, `BLE Gateway (LOC-NOR-02)`, `Wearable TAG (LOC-NOR-03)`) oleh `Dewi L`
10. Verifikasi entri SKU Principal dan SKU Distributor lain tidak tampil
11. Ketik Search pada modal `HHR`, tekan Enter
12. Verifikasi kata kunci `HHR` menampilkan "No results found"
13. Klik ikon close `[✕]`

## Notes

- Langkah penghubung (S-03, S-07): langkah 6 sampai 7 adalah ganti akun eksplisit dan membuka halaman karena hook `beforeEach` hanya membuka halaman untuk akun pertama; langkah 5 dan 13 menutup modal; tanpa asersi tambahan.
- Asersi absence langkah 10 didahului langkah 9 yang membuktikan entri milik Distributor tampil di surface yang sama; langkah 12 memakai empty state "No results found" sebagai anchor.
- Temuan untuk QA:
  - Fixture rancangan belum diverifikasi ada di environment: akun Principal Tanpa SKU (#21), riwayat Changelog Distributor (#34), dan SKU lokal Distributor (#31).
  - TC-AC-DS-389 tidak menyebut tanggal entri; spec tidak mengasersi kolom Date.
  - S-12: asersi bergantung pada nama literal Pre-setup #31 dan #33. Lampiran A tidak memuat butir modul ini. Spec mengikuti TC dengan seeding idempoten dan suite serial; keputusan pengecualian nama literal masih terbuka.
  - Env `AC_DS_FRESH_PASSWORD` dan `AC_DS_DIST_PASSWORD` serta berkas fixture `Fixture.deviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE. Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag-nya belum ditetapkan.
