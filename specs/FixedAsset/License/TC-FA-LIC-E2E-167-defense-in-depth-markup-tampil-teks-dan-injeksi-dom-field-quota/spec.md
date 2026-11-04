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
- Data Dinamis TC-FA-LIC-452 (suffix `{runId}-167`): grup bernama `<b>x</b><script>alert(1)</script> {runId}-167` dengan alokasi (menghasilkan entri Changelog: Allocation Quota) dan user bernama `<img src=x> {runId}-167` dengan dua sesi: satu sesi aktif (tampil di Tab Concurrent User) dan satu sesi lain yang di-Force Logout (menghasilkan entri Changelog: Concurrent User); dibuat lewat API di hook `before` dan dihapus di hook `after` (disediakan tim FE/BE; kontrak seeding tidak tertulis di TC). Urutan seeding di hook `before`: pemulih Pre-setup #14, lalu grup bermarkup dengan alokasi, lalu user bermarkup dengan sesi aktif, dan Force Logout sesi lain paling akhir; dengan urutan itu entri Changelog: Allocation Quota dan entri Changelog: Concurrent User yang dihasilkan seeding adalah entri terbaru pada urutan default kolom Date dan tampil di halaman 1 modal Changelog masing-masing (langkah 15 sampai 17 dan 21 sampai 23; S-14). Tabel Tab Concurrent User berisi 18 sesi aktif Pre-setup #14 ditambah sesi user bermarkup (lebih dari satu halaman), sehingga baris user bermarkup dibuka lewat Search `{runId}-167`.
- Kemampuan teknis (disediakan tim FE): mengamati eksekusi script pada halaman (langkah 4, 12, 17, dan 23).
- Kemampuan teknis (disediakan tim FE): menyuntik nilai langsung ke DOM field Allocated Quota (manipulasi DOM di browser, langkah 27); intercept respons Save dan membaca status respons (langkah 29); dialog `Unsaved Changes` tidak dipakai karena field dikembalikan ke nilai tersimpan sebelum modal ditutup.
- Spec ini tidak mengubah alokasi Pre-setup #12: Save pada TC-FA-LIC-454 ditolak server dan nilai dikembalikan ke `100` sebelum modal ditutup. Suite serial (`parallel: false`).
- Hook dan kemampuan suite (fixture BE penyetel state, sesi API aktor, flag Guided Tooltip): dinyatakan sekali di `suite.md`.

## Test Steps

### TC-FA-LIC-452: Nama grup/pengguna berisi markup tampil sebagai teks pada tabel dan Changelog

1. Buka Tab `Allocation Quota`
2. Verifikasi nama grup bermarkup tampil apa adanya sebagai teks di Tab Allocation Quota (node `All Groups`)
3. Verifikasi nama grup bermarkup di Tab Allocation Quota (node `All Groups`) tidak dirender sebagai HTML
4. Verifikasi tidak ada script berjalan dari nama grup bermarkup di Tab Allocation Quota (node `All Groups`)
5. Ketik Search `<b>`, tekan Enter
6. Verifikasi hasil Search `<b>` mencocokkan teks literal: baris grup bermarkup tampil
7. Klik `(←)` pada kotak Search
8. Klik Tab `Concurrent User`
9. Ketik Search `{runId}-167`, tekan Enter
10. Verifikasi nama user bermarkup tampil apa adanya sebagai teks di Tab Concurrent User
11. Verifikasi nama user bermarkup di Tab Concurrent User tidak dirender sebagai HTML
12. Verifikasi tidak ada script berjalan dari nama user bermarkup di Tab Concurrent User
13. Klik `(←)` pada kotak Search
14. Klik ikon Changelog pada toolbar Tab Concurrent User
15. Verifikasi nama user bermarkup tampil apa adanya sebagai teks di modal Changelog: Concurrent User
16. Verifikasi nama user bermarkup di modal Changelog: Concurrent User tidak dirender sebagai HTML
17. Verifikasi tidak ada script berjalan dari nama user bermarkup di modal Changelog: Concurrent User
18. Tutup modal Changelog: Concurrent User dengan `×`
19. Klik Tab `Allocation Quota`
20. Klik ikon Changelog pada toolbar Section 2
21. Verifikasi nama grup bermarkup tampil apa adanya sebagai teks di modal Changelog: Allocation Quota
22. Verifikasi nama grup bermarkup di modal Changelog: Allocation Quota tidak dirender sebagai HTML
23. Verifikasi tidak ada script berjalan dari nama grup bermarkup di modal Changelog: Allocation Quota
24. Tutup modal Changelog: Allocation Quota dengan `×`

### TC-FA-LIC-454: Injeksi karakter terlarang ke DOM field Allocated Quota ditolak server saat Save

25. Klik node `Kantor Pusat`
26. Klik `[Edit]` pada Divisi IT
27. Injeksi nilai `12a` langsung ke DOM field Allocated Quota (bypass filter keystroke)
28. Klik `[Save]`
29. Verifikasi server menolak nilai `12a`
30. Verifikasi modal Edit Allocation tetap terbuka
31. Kembalikan field Allocated Quota ke nilai tersimpan `100`
32. Tutup modal Edit Allocation dengan `[×]`
33. Verifikasi Allocated Quota Divisi IT tetap 100

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): "Buka Tab `Allocation Quota`" yang mengikuti langkah TC, "Ketik Search `{runId}-167`, tekan Enter" dan "Klik `(←)` pada kotak Search" (langkah 9 dan 13: Search baris user bermarkup pada tabel multi-halaman, R-16, bagian 8b butir 13, lalu bersihkan Search, 8b.9), penutupan modal Changelog, dan "Kembalikan field Allocated Quota ke nilai tersimpan `100`" (S-09: form dirty). Search `<b>` pada Tab Allocation Quota menemukan baris grup bermarkup (langkah penghubung, R-16).
- Temuan untuk QA:
  - TC-FA-LIC-452 tidak menyebut cara menghasilkan entri Changelog bagi grup dan user bermarkup dan tidak menyebut surface tempat Search `<b>` dijalankan; spec memakai tabel Tab Allocation Quota.
  - TC-FA-LIC-452 Expected a "tidak ada script berjalan" tidak menyebut cara mengamati; spec memakai kemampuan pengamat script di `## Prerequisites`.
  - TC-FA-LIC-454 Expected tidak menyebut tanda penolakan server yang teramati di UI (toast atau pesan); spec mengasersi penolakan dan modal tetap terbuka.
