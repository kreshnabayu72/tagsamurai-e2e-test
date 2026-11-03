---
id: TC-FA-LIC-E2E-167-defense-in-depth-markup-tampil-teks-dan-injeksi-dom-field-quota
title: "Defense-in-Depth: Nama Bermarkup Tampil sebagai Teks dan Injeksi Karakter Terlarang ke Field Allocated Quota"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LIC-452
  - TC-FA-LIC-454
coverage:
  web: automated
---

# Defense-in-Depth: Nama Bermarkup Tampil sebagai Teks dan Injeksi Karakter Terlarang ke Field Allocated Quota

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, kata sandi `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1). Password tidak ditulis di spec atau fixture; nama env `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup #12 (`Fixture.fixedAssetLicense.kuotaHierarki`): hierarki Produksi, Kantor Pusat (Divisi Logistik (Gudang A), Divisi IT, Divisi Keuangan), Cabang Surabaya, Cabang Medan dengan alokasi, Used, dan Reserved sesuai Example Data PRD §4.1.3; disediakan tim FE/BE. Divisi IT beralokasi 100 (TC-FA-LIC-454).
- Data Dinamis TC-FA-LIC-452 (suffix `{runId}-167`): grup bernama `<b>x</b><script>alert(1)</script> {runId}-167` dengan alokasi (menghasilkan entri Changelog: Allocation Quota) dan user bernama `<img src=x> {runId}-167` dengan sesi aktif yang di-Force Logout (menghasilkan entri Changelog: Concurrent User); dibuat lewat API di hook `before` dan dihapus di hook `after` (disediakan tim FE/BE; kontrak seeding tidak tertulis di TC).
- Kemampuan teknis: menyuntik nilai langsung ke DOM field Allocated Quota (manipulasi DOM di browser, disediakan tim FE); dialog `Unsaved Changes` tidak dipakai karena field dikembalikan ke nilai tersimpan sebelum modal ditutup.
- Spec ini tidak mengubah alokasi Pre-setup #12: Save pada TC-FA-LIC-454 ditolak server dan nilai dikembalikan ke `100` sebelum modal ditutup. Suite serial (`parallel: false`).
- Hook dan kemampuan suite (fixture BE penyetel state, sesi API aktor, flag Guided Tooltip): dinyatakan sekali di `suite.md`.

## Test Steps

### TC-FA-LIC-452: Nama grup/pengguna berisi markup tampil sebagai teks pada tabel dan Changelog

1. Buka Tab `Allocation Quota`
2. Verifikasi nama grup bermarkup tampil apa adanya sebagai teks di Tab Allocation Quota (node `All Groups`): tidak dirender sebagai HTML dan tidak ada script berjalan
3. Ketik Search `<b>`, tekan Enter
4. Verifikasi hasil Search `<b>` mencocokkan teks literal: baris grup bermarkup tampil
5. Klik `(←)` pada kotak Search
6. Klik Tab `Concurrent User`
7. Verifikasi nama user bermarkup tampil apa adanya sebagai teks di Tab Concurrent User: tidak dirender sebagai HTML dan tidak ada script berjalan
8. Klik ikon Changelog pada toolbar Tab Concurrent User
9. Verifikasi nama user bermarkup tampil apa adanya sebagai teks di modal Changelog: Concurrent User
10. Tutup modal Changelog: Concurrent User dengan `×`
11. Klik Tab `Allocation Quota`
12. Klik ikon Changelog pada toolbar Section 2
13. Verifikasi nama grup bermarkup tampil apa adanya sebagai teks di modal Changelog: Allocation Quota
14. Tutup modal Changelog: Allocation Quota dengan `×`

### TC-FA-LIC-454: Injeksi karakter terlarang ke DOM field Allocated Quota ditolak server saat Save

15. Buka Tab `Allocation Quota`, lalu klik node `Kantor Pusat`
16. Klik `[Edit]` pada Divisi IT
17. Injeksi nilai `12a` langsung ke DOM field Allocated Quota (bypass filter keystroke)
18. Klik `[Save]`
19. Verifikasi server menolak nilai `12a`
20. Verifikasi modal Edit Allocation tetap terbuka
21. Kembalikan field Allocated Quota ke nilai tersimpan `100`
22. Tutup modal Edit Allocation dengan `[×]`
23. Verifikasi Allocated Quota Divisi IT tetap 100

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): "Buka Tab `Allocation Quota`" yang mengikuti langkah TC, "Klik `(←)` pada kotak Search", penutupan modal Changelog, dan "Kembalikan field Allocated Quota ke nilai tersimpan `100`" (S-09: form dirty). Search `<b>` pada Tab Allocation Quota menemukan baris grup bermarkup (langkah penghubung, R-16).
- Temuan untuk QA:
  - TC-FA-LIC-452 tidak menyebut cara menghasilkan entri Changelog bagi grup dan user bermarkup dan tidak menyebut surface tempat Search `<b>` dijalankan; spec memakai tabel Tab Allocation Quota.
  - TC-FA-LIC-454 Expected tidak menyebut tanda penolakan server yang teramati di UI (toast atau pesan); spec mengasersi penolakan dan modal tetap terbuka.
