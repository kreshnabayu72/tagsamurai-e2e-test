---
id: TC-FA-CAID-E2E-012-state-tenant-plan-diturunkan-saat-form-terbuka
title: "State Tenant: Plan Diturunkan ke Starter Saat Form Terbuka"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAID-314
  - TC-FA-CAID-315
coverage:
  web: automated
---

# State Tenant: Plan Diturunkan ke Starter Saat Form Terbuka

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka hook `beforeEach` suite.
- Akun aktor: Total Control `Company Downgrade` (Pre-setup No 14, plan awal Growth). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE, password `Spectra.env.FA_DOWNGRADE_TC_PASSWORD` (nama env usulan, perlu konfirmasi tim FE). Hook `after` spec ini mengembalikan sesi ke akun default suite (Total Control Company Alpha). Password tidak ditulis di spec atau fixture.
- Hook suite (`suite.md`): flag Guided Tooltip disetel seen untuk akun UI suite. Baseline Company Alpha yang dipulihkan `beforeEach` suite tidak dipakai spec ini.
- Data Pre-setup No 14: `Company Downgrade` dengan plan Growth, konfigurasi B1 (Master Switch ON, Separator `/ (Slash)`, segmen tercentang Group Code, Category Code, Asset Name Code, Purchase Date, Asset Increment, tanpa Initial Company), dan aset G1 `JKT/LAP/T490/0926/1`, G2 `JKT/LAP/T490/0926/2` (hanya dibaca; dipakai sebagai precondition TC, tidak diasersi). Nilai dibaca dari `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Kemampuan teknis: seed API untuk menurunkan dan memulihkan plan Company Downgrade setelah halaman dibuka (disediakan tim FE/BE, mekanisme tidak tertulis di TC, PRD, atau LLD). Pelaku perubahan plan memakai seed sehingga bukan konteks kedua dan bukan objek asersi.
- State global: plan Company Downgrade (Growth diturunkan ke Starter); dipulihkan ke Growth di langkah 8 dan 16 serta hook `after` spec ini walau spec gagal di tengah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-314: Plan diturunkan ke Starter saat form terbuka: Save ditolak dengan toast T-06

1. Turunkan plan Company Downgrade dari Growth ke Starter lewat seed hingga plan tersimpan, setelah halaman terbuka
2. Pilih Separator `- (Dash)`
3. Klik `[Save]`
4. Verifikasi toast error `Error, failed to save configuration. Your current plan does not include this feature.` tampil
5. Verifikasi UI di-refresh ke state terkunci dan banner D-05 tampil
6. Verifikasi kontrol mutasi tidak dapat dipakai (Disabled)
7. Verifikasi Separator menampilkan `/ (Slash)` sehingga konfigurasi tersimpan tidak berubah
8. Pulihkan plan Company Downgrade ke Growth lewat seed hingga plan tersimpan, lalu muat ulang halaman (F5)

### TC-FA-CAID-315: Plan diturunkan ke Starter saat form terbuka: Toggle ditolak dengan toast T-06

9. Turunkan plan Company Downgrade dari Growth ke Starter lewat seed hingga plan tersimpan, setelah halaman terbuka
10. Geser Master Switch ke OFF
11. Klik `[Disable]` pada dialog `Disable Custom Asset ID`
12. Verifikasi toast error `Error, failed to save configuration. Your current plan does not include this feature.` tampil
13. Verifikasi Master Switch kembali ke posisi ON
14. Verifikasi UI di-refresh ke state terkunci dengan banner D-05
15. Verifikasi Master Switch tetap ON sesudah UI di-refresh sehingga status Master Switch tersimpan tidak berubah
16. Pulihkan plan Company Downgrade ke Growth lewat seed hingga plan tersimpan

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular. Langkah pembuka kedua TC (halaman terbuka) dipenuhi hook `beforeEach` suite.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1 dan 9 (menurunkan plan sebagai pemicu lewat seed), langkah 2, 3, 10, 11 (aksi TC), dan langkah 8 dan 16 (memulihkan plan; langkah 8 diikuti muat ulang agar form kembali ke state Growth).
- Urutan Expected TC-FA-CAID-314 mengikuti urutan state: konfigurasi tersimpan diamati sesudah UI di-refresh (langkah 7), karena Separator tersimpan hanya terlihat pada form sesudah refresh. Hal yang sama berlaku untuk langkah 15.
- Pecahan Expected TC-FA-CAID-314 b: "banner D-05 tampil" (langkah 5) dan "kontrol mutasi tidak dapat dipakai" (langkah 6) masing-masing klausa sendiri. Pecahan TC-FA-CAID-315 a: "Master Switch kembali ke ON" (langkah 13) dan "status tersimpan tidak berubah" (langkah 15).
- Temuan untuk QA:
  - TC-FA-CAID-314 dan 315 menyebut "banner D-05" tanpa judul dan deskripsi; spec hanya mengasersi bahwa banner tampil.
  - Email dan env var password akun Total Control Company Downgrade tidak tertulis di Pre-setup TC (hanya pola `{namaCompany}`); env var adalah usulan.
  - Mekanisme menurunkan plan setelah halaman dibuka tidak tertulis di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).
  - Post Condition TC-FA-CAID-314 dan 315 kosong; tidak ada yang diasersi.
