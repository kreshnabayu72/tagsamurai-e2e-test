---
id: TC-FA-FAAM-E2E-046-create-kuota-paket-starter-dialog-dan-cta-upgrade
title: "Create: Dialog Kuota Paket Starter, OK Mempertahankan Input, dan CTA Upgrade"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-154
  - TC-FA-FAAM-156
  - TC-FA-FAAM-157
coverage:
  web: automated
---

# Create: Dialog Kuota Paket Starter, OK Mempertahankan Input, dan CTA Upgrade

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control client Starter `AutoStarter` berisi 10 Asset Name (kuota 10) (Pre-setup #16). Email akun tidak tertulis di Pre-setup TC (disediakan tim FE; lihat Temuan untuk QA), `Spectra.env.FA_STARTER_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control client utama, `Spectra.env.FA_TC_PASSWORD`).
- Environment variable: `FA_STARTER_PASSWORD`, `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; setiap nama didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo.
- Hook suite berlaku (lihat `suite.md`): sesi API aktor, seed API per TC, pemulihan state global di hook `after`.
- Data Pre-setup #22 s.d. #25 (kategori, brand, UoM, label) tersedia di client utama: Category leaf `IT Equipment` dan `Electronics > Laptop`, Brand `Dell`, `Lenovo`, `Toyota`, `Apple`, UoM `Unit`, `Pcs`, `Set`, Label `Finance`, `High Priority`, `Fragile`. Nilai Pre-setup mengacu ke `fixtures/fixed-asset-settings-asset-name.json` (fixture baru yang ditetapkan tim FE; tanpa password atau token).
- Data Pre-setup #16: client `AutoStarter` plan Starter berisi 10 Asset Name tanpa Category Locked; spec tidak menambah atau menghapus Asset Name.
- Data Dinamis (suffix per run dan nomor spec): Asset Name `Create Min Item {runId}-046` hanya diketik dan tidak tersimpan (Submit ditolak).
- Kemampuan teknis: pembacaan entri teratas Changelog sebagai baseline (S-12).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): tidak ada data yang dibuat; popup ditutup lewat langkah pemulihan eksplisit.

## Test Steps

1. Buka Changelog, catat entri teratas sebagai baseline, lalu tutup Modal Changelog

### TC-FA-FAAM-154, 157, 156: Dialog kuota paket Starter

2. Klik `[+ Asset Name]` sehingga `Popup Create Asset Name` terbuka
3. Isi field wajib: Asset Name `Create Min Item {runId}-046`, Category (klik `[Select Category]`, pilih leaf `IT Equipment`, klik `[Select]`), TAG Type `QR`, Brand `Dell`, UoM `Unit`
4. Klik `[Submit]`
5. Verifikasi Dialog `Asset Name Limit Reached` dengan teks `You've reached your plan limit of 10 asset names. Upgrade your plan to add more.`, tombol `[OK]` dan CTA `[Upgrade]` tampil
6. Verifikasi Dialog memuat tombol `[OK]` primary dan CTA `[Upgrade]` di sampingnya
7. Klik `[OK]`
8. Verifikasi Dialog tertutup
9. Verifikasi Modal Create tetap terbuka dan seluruh input dipertahankan walau Stay tidak tercentang
10. Pulihkan form: klik `[Clear Field]`, lalu klik `[✕]` (form bersih tertutup tanpa dialog)
11. Ketik Search `Create Min Item {runId}-046`, tekan Enter
12. Verifikasi Empty state `No results found` tampil (record tidak dibuat)
13. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel
14. Buka Changelog
15. Verifikasi Entri teratas Changelog sama dengan baseline (tidak ada entri log baru)
16. Tutup Modal Changelog

## Notes

- P-1: TC-FA-FAAM-154 butir b ("tidak ada entri log") diasersi di spec asal karena precondition-nya adalah state berat (client Starter berisi tepat 10 Asset Name); asersi memakai baseline entri teratas Changelog langkah 1 (S-05, S-12).
- Satu alur memenuhi tiga TC: TC-FA-FAAM-154, 157, dan 156 memiliki langkah uji yang identik (buka form, isi field wajib, Submit), sehingga hanya dijalankan sekali; `Verifikasi` TC-FA-FAAM-157 (tombol `[OK]` primary dan CTA di sampingnya) dan TC-FA-FAAM-156 (OK menutup dialog, modal tetap terbuka) dipisah menurut Expected masing-masing.
- Langkah penghubung (tanpa `Verifikasi`): pencatatan baseline, pemulihan form, Search nama sebagai pembuktian absence record dengan empty state sebagai anchor (bagian 8b butir 2), dan penutupan Modal Changelog dan Search.
- Temuan untuk QA:
  - Akun Total Control untuk client `AutoStarter` (Pre-setup #16) tidak tertulis di Pre-setup TC; nama env diusulkan `FA_STARTER_PASSWORD`.
  - TC-FA-FAAM-154, 156, 157 memakai Asset Name `Create Min Item` tanpa suffix; spec bersuffix agar tidak bentrok antar run.
